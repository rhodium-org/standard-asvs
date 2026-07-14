# standard-asvs

The **OWASP Application Security Verification Standard (ASVS)** expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/rhodium-org/throughline-compose).

This repository holds no code. It is a directory of small YAML items with permanent
UIDs, validated by `tl check`. Consumers import it under a namespace and reference
its clauses as `asvs:SR-0001`.

## Status

This branch (`main`) is the **complete v5.0.0 edition** —
<!-- tl:count type == 'user_requirement' -->
17
<!-- tl:end --> chapters and
<!-- tl:count type == 'system_requirement' -->
345
<!-- tl:end --> verification requirements, generated from OWASP's official
machine-readable export and published to [`docs/spec.md`](docs/spec.md):

- `INT-0001` — the root intent (why ASVS exists), `normative: false`.
- Chapters `V1`…`V17` as `user_requirement`s that `derives_from` the intent.
- Every verification requirement as a `system_requirement` that `implements` its
  chapter, carrying its ASVS level (`L1`/`L2`/`L3`) in `attrs.level`.

The counts above are rendered from the live graph by the `tl:count` directive, so
they cannot drift. Re-run [`tools/generate_from_owasp.py`](tools/generate_from_owasp.py)
against a newer OWASP export to extend the graph; it preserves every existing
UID↔clause mapping and only allocates UIDs for clauses that have none yet.

## Editions — release branches, not one graph

ASVS v4 → v5 is a full renumber and restructure, not an increment: a v4 clause number
has no clean v5 equivalent. So each edition is its own **release branch** of this one
repo, tagged for point releases, and a consumer pins the edition it wants:

| Edition | Branch | Tag | Shape |
|---|---|---|---|
| **v5.0.0** (current) | `main` | `v5.0.0` | 17 chapters, 345 requirements |
| **v4.0.3** | `release/v4` | `v4.0.3` | 14 chapters, 278 requirements |

Each edition has its **own UID space starting at `UR-0001`/`SR-0001`**. Because a
consumer resolves exactly one ref, the two never collide — `asvs:SR-0003` means
whatever `SR-0003` is *at the edition you pinned*. To correct an edition, commit to its
branch and cut a new tag (`v5.0.1`, `v4.0.4`).

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0001`…), immutable and never the
  ASVS number. The published number lives in `attrs.source_ref` (`"V1.1.1"`); the
  ASVS L1/L2/L3 grade in `attrs.level` (the lowest level at which the requirement
  applies).

## Composing it

In a consuming throughline project's `throughline.toml`:

```toml
[[sources]]
namespace = "asvs"
url = "https://github.com/rhodium-org/standard-asvs"
ref = "v5.0.0"                  # pin an edition: "v5.0.0" or "v4.0.3"
```

(For local side-by-side development you can use `path = "vendor/standard-asvs"`
instead of `url`/`ref`.)

Then reference a clause from your own items:

```yaml
links:
- target: asvs:SR-0003          # ASVS v5.0.0 V1.2.1, context-relevant output encoding
  type: satisfies
```

`tl-compose check` resolves the reference; bare `tl check` fails fast and points you
at `tl-compose`.

## Local checks

```sh
pip install throughline
tl check --strict     # the graph must stay sound
tl docs --check       # docs/spec.md must match the graph
```

## Provenance

ASVS is © the OWASP Foundation, licensed CC BY-SA 4.0. See [NOTICE](NOTICE) and
https://github.com/OWASP/ASVS. This repository is Apache-2.0 for its structure and
tooling; the reproduced requirement text remains OWASP's.
