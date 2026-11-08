#!/usr/bin/env python3
"""Render README.md from research/catalog.json so names, purposes, and examples stay aligned."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "research" / "catalog.json").read_text())

INTRO = """# Montessori skills

Task-specific skills for parents, guides, and school administrators. 33 skills in one tree: 10 parent, 12 guide, 10 administrator, and 1 optional FutureNerds adapter.

They organize observation, preparation, and drafting from supplied facts. They do not diagnose children, invent albums or fees, or claim that Montessori programs are universally superior. A 2023 Campbell review reports pooled positive program-level outcomes; a 2026 *Review of Educational Research* abstract (full article not read) questions how credible those advantages are. That disagreement is recorded, not settled.

Primary Montessori texts, AMI/AMS pages, Hapa Family videos (transcripts read), safety authorities, and accounting guidance are cited in each skill's `references/evidence.md`. Attribution is local. None of those organizations endorsed this repository. No external Montessori guide has reviewed these skills yet.

License: not chosen. See [docs/release-review.md](docs/release-review.md).

## Install

Format checks run 8 Nov 2026: Python 3.12.3, `skills-ref` 0.1.1 (`agentskills validate` on all 33), `jsonschema` 4.26.0 on root `plugin.json`, Claude Code 2.1.319 `claude plugin validate . --strict` (passed). Host login and marketplace listing were not performed. A license is still pending, so `--profile directory` is expected to refuse a public Claude directory submission.

**Standalone skill** (any client that loads a skill folder):

```bash
cp -R skills/montessori-at-home ~/.agents/skills/montessori-at-home
```

Point the copy at the client you use. Each folder contains `SKILL.md` and `references/` so it works without the rest of the repo.

**Claude Code plugin** from a local checkout:

```bash
claude plugin validate . --strict
# then load this directory as a plugin, or /plugin-dir, depending on your Claude Code build
```

Claude discovers `skills/` at the plugin root. Manifest: `.claude-plugin/plugin.json`.

**Portable Agent Plugins / Codex** (root `plugin.json`, schema [1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)):

```bash
python3 scripts/validate.py
```

Local Codex/ChatGPT marketplace wiring is documented by OpenAI as a separate step (`marketplace.json` pointing at this folder). This repo is a skills plugin. It has no MCP server and is not a ChatGPT App. Public directory submission was not requested.

FutureNerds is optional. 32 skills produce their artifact with no FN account. Do not put API tokens in chat or in git.

## How to read a row

Audience is the primary reader. Other people may still use the skill. The example is fictional. Source method: [research/source-registry.md](research/source-registry.md).

"""

FOOTER = """
## Related skills

Several names sit next to each other on purpose:

- `family-school-messages` is one family, one matter. `school-announcements` is a defined group.
- `factual-observation-notes` cleans notes. `observation-to-lesson-plan` chooses a next move. `montessori-lesson-preparation` prepares a named album lesson. `progress-report-drafting` writes the period report.
- `tuition-billing-explanations` explains an invoice. `payment-record-reconciliation` matches independent payment evidence.

## Limits

- School curriculum, handbooks, calendars, agreements, and ledgers supplied at runtime control school-specific facts.
- Current choking, infant sleep, and furniture-anchoring guidance override historical or practitioner examples that conflict with them.
- Hapa Family is parent/practitioner testimony. Credit is local to the skills that used those videos.
- Maria Montessori editions used: 1912 *The Montessori Method*; 1914 *Dr. Montessori's Own Handbook*; 1917 *Spontaneous Activity in Education*; selected later chapters/quotations listed in the source registry.
"""


def table(audience: str) -> str:
    rows = [s for s in CATALOG["skills"] if s["audience"] == audience]
    lines = [
        f"### {audience}",
        "",
        "| Skill | Purpose | Example prompt |",
        "| --- | --- | --- |",
    ]
    for s in rows:
        slug = s["slug"]
        purpose = s["purpose"].replace("|", "\\|")
        example = s["example_prompt"].replace("|", "\\|")
        lines.append(f"| [`{slug}`](skills/{slug}/) | {purpose} | {example} |")
    return "\n".join(lines)


def main() -> None:
    parts = [
        INTRO,
        table("Parents"),
        "",
        table("Guides"),
        "",
        table("Admin"),
        "",
        table("Integration"),
        FOOTER,
    ]
    text = "\n".join(parts).rstrip() + "\n"
    (ROOT / "README.md").write_text(text)
    print("wrote README.md")


if __name__ == "__main__":
    main()
