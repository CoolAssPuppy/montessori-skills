#!/usr/bin/env python3
"""Render README.md from research/catalog.json so names, purposes, and examples stay aligned."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "research" / "catalog.json").read_text())

INTRO = """# Montessori skills

33 Agent Skills for parents, guides, and school administrators. They turn supplied facts into observation notes, environment checks, lesson preparations, family messages, and office drafts. Ten skills are for parents, twelve for guides, ten for administrators, and one optional FutureNerds adapter.

The same `skills/` tree is packaged as standalone skill folders and as one plugin, `montessori-skills` 0.1.0: Claude Code via `.claude-plugin/plugin.json`, Portable Agent Plugins via root `plugin.json`.

They do not diagnose children, invent albums or fees, or claim program-level efficacy. No external Montessori educator has reviewed this package. Original material is CC0 1.0 (SPDX: CC0-1.0); cited third-party works keep their own terms. See [Limits](#limits).

## Install

Draft commands pin branch `cursor/montessori-skills-library-9b0f` because `main` still has only the initial README. Validation does not load a plugin or install a skill.

### Validation (not a load)

Executed 8 Nov 2026 on a checkout of this branch (Python 3.12.3, `skills-ref` 0.1.1, `jsonschema` 4.26.0, Claude Code 2.1.319):

```bash
git clone --branch cursor/montessori-skills-library-9b0f https://github.com/CoolAssPuppy/montessori-skills.git
cd montessori-skills
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
npx --yes @anthropic-ai/claude-code plugin validate . --strict
```

`python3 scripts/validate.py` checks catalog counts, skill frontmatter, local citations, and portable `plugin.json`. It does not install anything.

### Skills: `npx skills add`

Documented CLI (`skills` 1.7.6): `npx skills add <package> --list` lists; `--skill <name>` or `--skill '*'` copies. Executed 8 Nov 2026 in a temporary project directory with `--copy -y -a claude-code`, no `-g`, not the user home. One skill and all 33 copied into that project's `.claude/skills/`, including `references/evidence.md`.

```bash
# list 33 skills, no install
npx --yes skills add https://github.com/CoolAssPuppy/montessori-skills.git#cursor/montessori-skills-library-9b0f --list

# one skill into the current project
npx --yes skills add https://github.com/CoolAssPuppy/montessori-skills.git#cursor/montessori-skills-library-9b0f --skill everyday-independence -a claude-code --copy -y

# all 33 into the current project
npx --yes skills add https://github.com/CoolAssPuppy/montessori-skills.git#cursor/montessori-skills-library-9b0f --skill '*' -a claude-code --copy -y
```

Use the `.git#branch` form. A GitHub `/tree/branch` URL truncates a slash-containing branch name, so the CLI looks for ref `cursor` and fails. After a local clone of this branch, `npx skills add ./ --skill everyday-independence -a claude-code --copy -y` is the same install against the checkout.

Each `skills/<slug>/` folder is also copyable on its own (`SKILL.md` plus `references/`). Point the copy at the skill directory your client documents. Do not treat `~/.agents/skills` as a required path.

### Claude Code plugin

Documented session load ([create a plugin](https://code.claude.com/docs/en/plugins/create), [plugin commands reference](https://code.claude.com/docs/en/plugins/cli-reference)): from the repository root, which holds `.claude-plugin/plugin.json` and `skills/`.

Executed 8 Nov 2026 (Claude Code 2.1.319):

```bash
npx --yes @anthropic-ai/claude-code --plugin-dir . plugin list --json
```

Returned `id` `montessori-skills@inline`, `scope` `session`, `enabled` true. The same `plugin list` without `--plugin-dir` reported no installed plugins. Session load does not write the user plugin store.

An interactive chat that invoked a skill was not run. `claude plugin marketplace add` / `plugin install` would write host config and were not executed.

### Portable Agent Plugins / Codex

Root `plugin.json` uses [schema 1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json). This repo also includes `.agents/plugins/marketplace.json` with `source.path` `./`, matching OpenAI's [repo marketplace](https://developers.openai.com/plugins/build/plugins) layout for a plugin at the clone root.

Documented Codex CLI (not executed; `codex` was not on PATH):

```bash
codex plugin marketplace add CoolAssPuppy/montessori-skills --ref cursor/montessori-skills-library-9b0f
```

or, from a checkout, `codex plugin marketplace add .`. ChatGPT desktop install from that marketplace was not run. This plugin has no MCP server and is not a ChatGPT App.

FutureNerds is optional. Thirty-two skills produce their artifact with no FN account. Do not put API tokens in chat or in git.

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
- Maria Montessori editions used: 1912 *The Montessori Method*; 1914 *Dr. Montessori's Own Handbook*; 1917 *Spontaneous Activity in Education*; selected later chapters and quotations listed in the source registry.
- Read-depth labels, program-outcomes literature (E1/E2), and link-check notes live in [research/source-registry.md](research/source-registry.md). Skills do not adjudicate that literature.
- No external Montessori guide, safety specialist, disability reviewer, privacy counsel, or accountant has reviewed this package.
- Original skills, code, and docs are CC0 1.0. Citations do not relicense Montessori, Hapa, AMS/AMI, or other third-party works. See [NOTICE](NOTICE) and [LICENSE](LICENSE).
- Static checks, executed install commands, and unevaluated fixture cases: [docs/release-review.md](docs/release-review.md).
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
