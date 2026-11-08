# Evidence: future-nerds

## Original Montessori

None. This is a record-system adapter.

## Modern professional guidance

- GDPR Article 5 (D1): purpose, minimization, accuracy, storage limitation, confidentiality. Official text: [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng). Not a full legal analysis; local education law not assessed.
- F1 for billing-control context when FN financial tools are in play.

## FutureNerds public contract (T1)

- [https://www.futurenerds.dev/api/openapi](https://www.futurenerds.dev/api/openapi) fetched 8 Nov 2026. Use this URL at runtime; do not rely on the snapshot below if the live document differs.
- Authoring snapshot (same GET): OpenAPI `3.1.0`, `info.version` `1.0.0`, server `https://www.futurenerds.dev`, 452 unique `operationId`s. HTTP `bearerAuth` JWT described as a Supabase access token. Paths `/api/mcp/tools/{operationId}`; `account_context_get` is POST with an empty JSON object.
- Selected identity, child, observation, assessment, incident, absence, message, calendar, and billing contracts inspected. Operation names used in the skill (`account_context_get`, `child_get`, `child_list`, `observation_create`, `progress_assessment_create`, `incident_report_file`, `absence_report`, `message_send`, `message_school_wide_send`, `parent_invitation_send`, `billing_invoice_send`, `billing_invoice_create`, and related send/pay/refund/cancel tools) were present in that snapshot.
- No authenticated request. No MCP session. Bearer REST only.
- Role enums vary; a parameter cannot confer a role.
- Notification effects taken from operation summaries (observation, assessment, incident, absence, invoice send). Re-read the live summary before a write.

## Packaging boundary (T2-T5)

Skills-only plugin. No guessed MCP server. Agent Skills spec: [agentskills.io/specification](https://agentskills.io/specification). Portable plugin schema: [agent-plugins.org](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json).

## Hapa Family

Not used.

## Editorial adaptations

- Stricter-of-prose-or-schema for `confirm`.
- Human approval of exact payload, beyond `confirm: true`.
- Duplicate-name stop.
- No retry on uncertain mutation.
