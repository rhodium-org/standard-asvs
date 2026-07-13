# OWASP ASVS — throughline source (v4.0.3 slice)

This document is generated from the graph. The prose between `tl:item` markers is
injected by `tl docs` — edit the YAML items, not the injected regions.

Each chapter is a `user_requirement` grouping the standard; each verification
requirement is a `system_requirement` that `implements` its chapter. The published
ASVS number lives in `attrs.source_ref`; the ASVS level in `attrs.level`.

## Purpose

<!-- tl:item INT-0001 -->
**INT-0001 — An application's security is verifiable against a graded, testable baseline** — `intent`, status `approved`

> The OWASP Application Security Verification Standard exists so that an application's security controls can be verified against a normative, level-graded set of requirements — giving developers, testers and procurers a shared baseline rather than ad-hoc judgement.

**source_ref**: ASVS 4.0.3
<!-- tl:end -->

## V1 Architecture, Design and Threat Modeling

<!-- tl:item UR-0001 -->
**UR-0001 — V1 Architecture, Design and Threat Modeling** — `user_requirement`, status `approved`

> Security controls are designed in, not bolted on — the application has a secure development lifecycle, threat modeling, and a documented, verifiable security architecture.

**source_ref**: V1
<!-- tl:end -->

<!-- tl:item SR-0001 -->
**SR-0001 — Secure software development lifecycle** — `system_requirement`, status `approved`

> Verify the use of a secure software development lifecycle that addresses security in all stages of development.

**source_ref**: V1.1.1 · **level**: 2
<!-- tl:end -->

<!-- tl:item SR-0002 -->
**SR-0002 — Threat modeling for design changes** — `system_requirement`, status `approved`

> Verify the use of threat modeling for every design change or sprint planning to identify threats, plan for countermeasures, facilitate appropriate risk responses, and guide security testing.

**source_ref**: V1.1.2 · **level**: 2
<!-- tl:end -->

## V2 Authentication

<!-- tl:item UR-0002 -->
**UR-0002 — V2 Authentication** — `user_requirement`, status `approved`

> The application verifies the identity of users securely — password strength, storage, recovery and general authenticator controls are all held to a graded baseline.

**source_ref**: V2
<!-- tl:end -->

<!-- tl:item SR-0003 -->
**SR-0003 — Minimum password length** — `system_requirement`, status `approved`

> Verify that user set passwords are at least 12 characters in length (after multiple spaces are combined).

**source_ref**: V2.1.1 · **level**: 1
<!-- tl:end -->

<!-- tl:item SR-0004 -->
**SR-0004 — Long passwords permitted** — `system_requirement`, status `approved`

> Verify that passwords of at least 64 characters are permitted, and that passwords of more than 128 characters are denied.

**source_ref**: V2.1.2 · **level**: 1
<!-- tl:end -->

<!-- tl:item SR-0005 -->
**SR-0005 — No password truncation** — `system_requirement`, status `approved`

> Verify that password truncation is not performed. However, consecutive multiple spaces may be replaced by a single space.

**source_ref**: V2.1.3 · **level**: 1
<!-- tl:end -->

<!-- tl:item SR-0006 -->
**SR-0006 — Passwords checked against breached sets** — `system_requirement`, status `approved`

> Verify that passwords submitted during account registration, login, and password change are checked against a set of breached passwords either locally (such as the top 1,000 or 10,000 most common passwords which match the system's password policy) or using an external API.

**source_ref**: V2.1.7 · **level**: 1
<!-- tl:end -->
