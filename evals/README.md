# Eval cases

`tests/fixtures/behavior_cases.json` holds trigger, safety, FutureNerds authorization, and financial fixtures.

`model_evaluations_run` is `false`. On 8 Nov 2026 Claude Code 2.1.319 (`npx @anthropic-ai/claude-code -p`) returned `Not logged in · Please run /login`. No API key was present. Fixture prompts were not sent to a model. Static tests only check that the fixtures are well-formed, that catalog names exist, that invoice line math ties, and that skill text contains required safety strings.

A manual content walkthrough of those cases is in [docs/release-review.md](../docs/release-review.md). Do not report the cases as passed model evaluations.
