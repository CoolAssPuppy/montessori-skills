# Evidence: future-nerds

## Original Montessori

None. This is a record-system adapter.

## Modern professional guidance

- GDPR Article 5 (D1): purpose, minimization, accuracy, storage limitation, confidentiality. Official text: [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng). Not a full legal analysis; local education law not assessed.
- F1 for billing-control context when FN financial tools are in play.

## FutureNerds public contract (T1)

- [https://www.futurenerds.dev/api/openapi](https://www.futurenerds.dev/api/openapi) read 8 Nov 2026. OpenAPI 3.1.0, info version 1.0.0, server https://www.futurenerds.dev.
- 452 operations enumerated. Selected identity, child, observation, assessment, incident, absence, message, calendar, and billing contracts inspected.
- No authenticated request. No MCP session. Bearer REST only.
- `account_context_get`: empty object; lists schools, roles, actions.
- Role enums vary; a parameter cannot confer a role.
- Notification effects taken from operation summaries (observation, assessment, incident, absence, invoice send).

## Packaging boundary (T2-T5)

Skills-only plugin. No guessed MCP server. Agent Skills spec: [agentskills.io/specification](https://agentskills.io/specification). Portable plugin schema: [agent-plugins.org](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).

## Hapa Family

Not used.

## Editorial adaptations

- Stricter-of-prose-or-schema for `confirm`.
- Human approval of exact payload, beyond `confirm: true`.
- Duplicate-name stop.
- No retry on uncertain mutation.
