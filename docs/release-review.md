# Release review (0.1.0 authored draft)

Date: 8 November 2026. Scope: first authored version of all 33 catalog skills. User authorized creation, writing, CC0 1.0 for original material, and this docs pass. No merge, marketplace submission, global install, FN backend, or production deployment.

## Package

- Branch: `cursor/montessori-skills-library-9b0f`
- Plugin name: `montessori-skills` version `0.1.0`
- Skills: 33 (10 parent, 12 guide, 10 admin, 1 FutureNerds)
- Layout: root `plugin.json` (Agent Plugins 1.0.0, `license` `CC0-1.0`) + `.claude-plugin/plugin.json` (same SPDX) + `.agents/plugins/marketplace.json` (`source.path` `./`) + shared `skills/`
- LICENSE: complete CC0 1.0 Universal legal code from https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt (SHA-256 `a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499`, byte-identical to SPDX CC0-1.0 text). NOTICE records third-party source terms.
- No `mcp.json`. No ChatGPT App.

## License and identity

Original skills, code, tests, and documentation are CC0 1.0. Reuse of that original material does not require attribution. Third-party works cited in research remain under their own terms; this package does not relicense Maria Montessori texts, Hapa Family videos, AMS/AMI pages, or other registry sources. Author name and GitHub URL in the manifests match the verified GitHub profile for `CoolAssPuppy` (Prashant Sridharan). No email, support URL, or privacy URL was added.

## Expert review

No external Montessori guide, safety specialist, disability/access reviewer, privacy counsel, or accountant has reviewed this package. Static CI and this document are not that review. Absence of that review does not block writing the skills.

## Word counts (SKILL.md body, excluding YAML frontmatter)

Measured after the concision pass, 8 Nov 2026:

- Range: 224 (`school-handbook-procedures`) to 561 (`future-nerds`)
- Median: 331
- 31 of 33 skills are in 200-450. Over 450:
  - `future-nerds` (561): live OpenAPI prerequisite, `account_context_get` order, notification effects, refuse list
  - `prepared-home-environment` (499): seven-step room walk with CDC sleep/choking and CPSC anchoring/small-parts locators
- Upper end of the target band: `montessori-at-home` 448 (one interest / one change / one activity plus Act Early), `montessori-terms-explained` 446 (glossary table is the procedure), `everyday-independence` 433

Skills were not flattened to match length. Repeated Inputs blocks and rhythmic "X is a plan. Y is not." contrasts were removed.

## Tests run vs not run

Run (static), 8 Nov 2026, Python 3.12.3:

- `python3 scripts/validate.py` (re-run after this pass)
- `python3 -m unittest discover -s tests -v`
- `python3 scripts/generate_local_refs.py --check`
- `agentskills validate` on each of 33 skill dirs via `skills-ref` 0.1.1
- Portable `plugin.json` against fetched Agent Plugins schema 1.0.0 (`jsonschema` 4.26.0)
- `npx @anthropic-ai/claude-code plugin validate . --strict` (Claude Code 2.1.319): Validation passed. LICENSE_MISSING is gone. ICON_MISSING remains a non-blocking directory warning on the default profile.
- `npx @anthropic-ai/claude-code plugin validate . --profile directory`: Validation passed (`success` true). Findings: ICON_MISSING warning, `blocking` false. Advice (non-blocking): README has no `/plugin install montessori-skills --marketplace <owner>/<repo>` line; marketplace add/install was not executed.
- `npx @anthropic-ai/claude-code plugin validate . --profile directory --strict`: ICON_MISSING is treated as an error (`--strict` promotes directory warnings). No LICENSE_MISSING. Directory submission was not requested; no icon was added.

Executed install/load checks (temporary directories only; not the user home):

- `npx skills add https://github.com/CoolAssPuppy/montessori-skills.git#cursor/montessori-skills-library-9b0f --list` (`skills` 1.7.6): listed 33 skills
- Same URL `--skill everyday-independence -a claude-code --copy -y` then `--skill '*'`: 33 `SKILL.md` files in the temp project's `.claude/skills/`
- Local clone path `--skill everyday-independence` then `--skill '*'`: same
- GitHub `/tree/branch` URL: failed (CLI cloned ref `cursor`)
- `npx @anthropic-ai/claude-code --plugin-dir /workspace plugin list --json`: `montessori-skills@inline`, `scope` `session`. Without the flag: "No plugins installed."

Not run, and not marked passed:

- Model evaluations of fixture prompts (see below)
- Authenticated FutureNerds calls
- ChatGPT/Codex GUI marketplace install; Codex CLI (`codex` not on PATH)
- `claude plugin marketplace add` / `plugin install` (would write host plugin config)
- Interactive Claude session that invoked a skill
- Live child or school data
- Public plugin directory submission

## Model evaluations

`evals/README.md` and `tests/fixtures/behavior_cases.json` set `model_evaluations_run: false`.

Attempt 8 Nov 2026: `npx @anthropic-ai/claude-code -p "Reply with the word pong only."` printed `Not logged in · Please run /login` (Claude Code 2.1.319). `ANTHROPIC_API_KEY` and `CLAUDE_CODE_OAUTH_TOKEN` unset. No host model was run against the fixtures. No scores. Login was not requested.

Static unittest still checks fixture shape, catalog names, invoice arithmetic, and required safety strings in skill text. That is not an evaluation.

## Content walkthrough (manual / self-review)

Read against `tests/fixtures/behavior_cases.json`. Not a scored model run.

| Case | What the skill text does |
| --- | --- |
| Parent task (everyday-independence / montessori-at-home) | Names one task and the hard part, demonstration, invitation, shrinking help, observation prompt; routes space vs routine vs one task |
| Wrong role (`absent-role`) | FN procedure: role argument cannot grant permission; parent does not call administrator billing list |
| Unapproved notify | Show payload and wait; `confirm: true` does not replace approval; parent-visible observation notifies guardians |
| No FN access | Keep the standalone educational artifact |
| Fabrication | Refuse invented `child_id`, progress, fees, vacancies |
| Choking | Seated food work, texture, continuous supervision; current CDC page cited |
| Individual vs group message | `family-school-messages` vs `school-announcements` in descriptions |
| Spoiled food / eye contact / floor mattress / unanchored dresser | Explicit overrides in family-routines, grace-and-courtesy, prepared-home-environment |

Historical isolation in *The Montessori Method* ch. V is cited as history and excluded as a procedure.

## Link check

See [research/source-registry.md](../research/source-registry.md). Primary locators match the packet sources (Gutenberg M1-M3, Archive M4, AMI/AMS, five Hapa videos, Campbell E1, Crossref E2, PMC E3, CDC/CPSC/NAEYC, F1, T1 OpenAPI). Automated 403s on CDC/CPSC/NAEYC/DOI are access-limited fetches, not 404s.
