# Release review (0.1.0 authored draft)

Date: 8 November 2026. Scope: first authored version of all 33 catalog skills. User authorized creation and writing. No merge, marketplace submission, global install, FN backend, or production deployment.

## Package

- Branch: `cursor/montessori-skills-library-9b0f`
- Plugin name: `montessori-skills` version `0.1.0`
- Skills: 33 (10 parent, 12 guide, 10 admin, 1 FutureNerds)
- Layout: root `plugin.json` (Agent Plugins 1.0.0) + `.claude-plugin/plugin.json` + shared `skills/`
- No `mcp.json`. No ChatGPT App. No license file.

## License and identity

License choice is **pending**. No SPDX identifier was authorized, so no LICENSE file and no `license` field. Claude Code's plugin-directory profile (`claude plugin validate --profile directory`) refuses that on purpose. Author name and GitHub URL in the manifests match the verified GitHub profile for `CoolAssPuppy` (Prashant Sridharan). No email, support URL, or privacy URL was added.

## Expert review

**Pending.** No external Montessori guide, safety specialist, disability/access reviewer, privacy counsel, or accountant has reviewed this package. Do not treat CI as that review.

## Tests run vs not run

Run (static), 8 Nov 2026, Python 3.12.3:

- `python3 scripts/validate.py` → `PASS static validation: 33 skills`
- `python3 -m unittest discover -s tests -v` → 7 tests OK
- `python3 scripts/generate_local_refs.py --check` → copies match
- `agentskills validate` on each of 33 skill dirs via `skills-ref` 0.1.1 (`agentskills, version 0.1.1`)
- Portable `plugin.json` against fetched Agent Plugins schema 1.0.0 (`jsonschema` 4.26.0)
- `npx @anthropic-ai/claude-code plugin validate . --strict` → `Validation passed` (Claude Code 2.1.319). Directory profile still reports `LICENSE_MISSING` and `ICON_MISSING`; those are not a load-time failure on the default profile. Directory submission was not requested.
- Standalone copy of `skills/montessori-at-home` with in-folder references

Not run, and not marked passed:

- Executed model evaluations of fixture prompts (`evals/README.md`; `model_evaluations_run: false`)
- Authenticated FutureNerds calls
- ChatGPT/Codex GUI marketplace install
- Claude Code `/plugin install` against a registered marketplace
- Live child or school data
- Public plugin directory submission (`--profile directory` would fail without a license)

## Content audit notes

- Historical isolation, spoiled-food consequences, required eye contact, and infant floor-bed certification are excluded as procedures.
- Administrative billing skills use F1 (England academy-trust guidance) plus supplied ledgers; they do not treat Montessori texts as accounting authority.
- E2 full article was not read. Crossref abstract and metadata were.
- FN public OpenAPI was read; no token was used.

## Remaining decisions

- License
- Whether to add author metadata
- Qualified human review before any school use
- Whether a real FN connector will ever be packaged (needs verified transport, not a guessed MCP URL)
