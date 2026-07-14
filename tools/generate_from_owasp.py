#!/usr/bin/env python3
"""Generate the ASVS throughline source from OWASP's official machine-readable data.

This reads the flat JSON export OWASP publishes for an ASVS edition and emits one
throughline item per chapter (a `user_requirement`) and per verification requirement
(a `system_requirement`), grounded chapter -> intent and requirement -> chapter.

Two invariants make re-running safe and faithful:

* **UIDs are permanent.** The mapping from an ASVS clause (its `source_ref`, e.g.
  ``V2.1.1``) to a throughline UID is derived from the items already on disk. Existing
  items are never rewritten; only clauses that have no item yet get a freshly allocated
  UID, in ASVS document order, continuing from the highest number already used. So the
  curated slice that predates this script keeps its exact UIDs and hand-written titles.
* **Deleted clauses are skipped.** OWASP keeps retired clause numbers as
  ``[DELETED, ...]`` tombstones with no level; those are not verification requirements
  and get no item.

Usage:  python tools/generate_from_owasp.py tools/asvs-4.0.3.flat.json
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = REPO / "chapters"          # user_requirement, prefix UR
REQS_DIR = REPO / "requirements"          # system_requirement, prefix SR
SPEC = REPO / "docs" / "spec.md"
INTENT = "INT-0001"
EDITION = "5.0.0"


def _levels(r: dict) -> int | None:
    """Lowest ASVS level (1/2/3) at which the clause applies, or None if retired.

    Two export shapes are supported: v4.0.3's three per-level marker columns
    (``level1``/``level2``/``level3``) and v5.0.0's single ``L`` field carrying the
    level number directly. A clause with neither is a retired tombstone.
    """
    lv = str(r.get("L", "")).strip()
    if lv in ("1", "2", "3"):
        return int(lv)
    for i, key in enumerate(("level1", "level2", "level3"), start=1):
        if r.get(key, "").strip():
            return i
    return None


_MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_PROACTIVE = re.compile(r"\s*\((?:C\d+(?:,\s*)?)+\)\s*$")
_WS = re.compile(r"\s+")


def clean_text(desc: str) -> str:
    t = _MD_LINK.sub(r"\1", desc.strip())   # [C1](url) -> C1, [text](url) -> text
    t = _PROACTIVE.sub("", t)               # drop trailing proactive-control refs
    return _WS.sub(" ", t).strip()


def short_title(text: str) -> str:
    """A concise label distilled from the requirement text."""
    t = re.sub(r"^Verify(\s+that)?\s+", "", text, flags=re.IGNORECASE)
    t = (t[:1].upper() + t[1:]) if t else t
    clause = re.split(r"[,;.]", t, maxsplit=1)[0].strip()
    if len(clause) > 100:
        clause = clause[:100].rsplit(" ", 1)[0]
    return clause


def _scan_existing(dir_: Path) -> dict[str, str]:
    """Map source_ref -> UID for the items already on disk, and record the max number."""
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max_num(ref2uid: dict[str, str], prefix: str) -> int:
    nums = [int(u.split("-")[1]) for u in ref2uid.values() if u.startswith(prefix + "-")]
    return max(nums, default=0)


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=80),
        encoding="utf-8",
    )


SPEC_HEADER = """\
# OWASP ASVS {edition} — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is a faithful, complete cut of **OWASP ASVS v{edition}**: every chapter is
a `user_requirement`, and every verification requirement is a `system_requirement`
that `implements` its chapter. The published ASVS number lives in `attrs.source_ref`
(e.g. `V1.1.1`); the ASVS level in `attrs.level`. The throughline UIDs are this
source's own and immutable — a consumer cites a clause as `asvs:SR-0001`, never by its
ASVS number.

It carries
<!-- tl:count type == 'user_requirement' -->
<!-- tl:end --> chapters and
<!-- tl:count type == 'system_requirement' -->
<!-- tl:end --> verification requirements.

## Purpose

<!-- tl:item INT-0001 -->
<!-- tl:end -->
"""


def generate_spec(ch_ref2uid: dict[str, str], chapter_name: dict[str, str],
                  seen_ch: list[str]) -> None:
    """Write docs/spec.md: a hand-owned header plus, per chapter in document order, a
    tl:item block for its UR and a tl:table of its requirements. `tl docs` injects the
    live content into the markers."""
    parts = [SPEC_HEADER.format(edition=EDITION)]
    for cid in seen_ch:
        parts.append(f"## {cid} {chapter_name[cid]}\n")
        parts.append(f"<!-- tl:item {ch_ref2uid[cid]} -->\n<!-- tl:end -->\n")
        flt = (
            "type == 'system_requirement' and "
            f"attrs.get('source_ref').startswith('{cid}.')"
        )
        parts.append(f"<!-- tl:table {flt} -->\n<!-- tl:end -->\n")
    SPEC.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main(src: str) -> int:
    reqs = yaml.safe_load(Path(src).read_text(encoding="utf-8"))["requirements"]

    ch_ref2uid = _scan_existing(CHAPTERS_DIR)
    sr_ref2uid = _scan_existing(REQS_DIR)
    next_ur = _max_num(ch_ref2uid, "UR") + 1
    next_sr = _max_num(sr_ref2uid, "SR") + 1

    # Chapters, in document order.
    seen_ch: list[str] = []
    chapter_name: dict[str, str] = {}
    for r in reqs:
        cid = r["chapter_id"]
        if cid in seen_ch:
            continue
        seen_ch.append(cid)
        chapter_name[cid] = r["chapter_name"]
        if cid in ch_ref2uid:
            continue  # keep the existing (possibly hand-curated) chapter item
        uid = f"UR-{next_ur:04d}"
        next_ur += 1
        ch_ref2uid[cid] = uid
        _dump(CHAPTERS_DIR / f"{uid}.yml", {
            "uid": uid,
            "type": "user_requirement",
            "status": "approved",
            "title": f"{cid} {r['chapter_name']}",
            "text": f"Verification requirements for {r['chapter_name']} ({cid}).",
            "links": [{"target": INTENT, "type": "derives_from"}],
            "attrs": {"source_ref": cid},
        })

    # Verification requirements, in document order.
    written = 0
    for r in reqs:
        ref = r["req_id"]
        level = _levels(r)
        if level is None:
            continue  # [DELETED, ...] tombstone — not a requirement
        if ref in sr_ref2uid:
            continue  # keep the existing item and its curated title, untouched
        uid = f"SR-{next_sr:04d}"
        next_sr += 1
        sr_ref2uid[ref] = uid
        text = clean_text(r["req_description"])
        _dump(REQS_DIR / f"{uid}.yml", {
            "uid": uid,
            "type": "system_requirement",
            "status": "approved",
            "title": short_title(text),
            "text": text,
            "links": [{"target": ch_ref2uid[r["chapter_id"]], "type": "implements"}],
            "attrs": {"source_ref": ref, "level": level},
        })
        written += 1

    generate_spec(ch_ref2uid, chapter_name, seen_ch)

    print(f"chapters: {len(seen_ch)} total, {len(ch_ref2uid)} mapped")
    print(f"requirements: {written} new items written, {len(sr_ref2uid)} total mapped")
    print(f"spec: {SPEC} regenerated for {len(seen_ch)} chapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else str(REPO / "tools/asvs-4.0.3.flat.json")))
