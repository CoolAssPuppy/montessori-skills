# Eval cases

`tests/fixtures/behavior_cases.json` holds trigger, safety, FutureNerds authorization, and financial fixtures.

`model_evaluations_run` is `false`. No host-logged agent was run against these prompts. Static tests only check that the fixtures are well-formed, that catalog names exist, and that skill text contains required safety strings.

Do not report these cases as passed model evaluations.
