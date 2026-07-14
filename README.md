# standard-asvs

The **OWASP Application Security Verification Standard (ASVS)** expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/rhodium-org/throughline-compose).

This repository holds no code. It is a directory of small YAML items with permanent
UIDs, validated by `tl check`. Consumers import it under a namespace and reference
its clauses as `asvs:SR-0003`.

## Status

The **complete v4.0.3 edition** —
<!-- tl:count type == 'user_requirement' -->
14
<!-- tl:end --> chapters and
<!-- tl:count type == 'system_requirement' -->
278
<!-- tl:end --> verification requirements, generated from OWASP's official
machine-readable export and published to [`docs/spec.md`](docs/spec.md):

- `INT-0001` — the root intent (why ASVS exists), `normative: false`.
- Chapters `V1`…`V14` as `user_requirement`s that `derives_from` the intent.
- Every non-retired verification requirement as a `system_requirement` that
  `implements` its chapter. (Clauses OWASP retired as `[DELETED]` in 4.0.3 carry no
  level and are intentionally omitted.)

The counts above are rendered from the live graph by the `tl:count` directive, so
they cannot drift. Re-run [`tools/generate_from_owasp.py`](tools/generate_from_owasp.py)
against a newer OWASP export to extend the graph; it preserves every existing
UID↔clause mapping and only allocates UIDs for clauses that have none yet.

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0001`…), immutable and never the
  ASVS number. The published number lives in `attrs.source_ref` (`"V2.1.1"`); the
  ASVS L1/L2/L3 grade in `attrs.level` (the lowest level at which the requirement
  applies).
- **Editions are git tags of this one repo.** v4.0.3 is tagged `v4.0.3`; v5.0.0 will
  be authored as a delta on the same graph and tagged `v5.0.0`. A consumer pins
  `asvs@v4.0.3`.

## Composing it

In a consuming throughline project's `throughline.toml`:

```toml
[[sources]]
namespace = "asvs"
path = "vendor/standard-asvs"   # or a pinned checkout
```

Then reference a clause from your own items:

```yaml
links:
- target: asvs:SR-0003          # ASVS V2.1.1, minimum password length
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
