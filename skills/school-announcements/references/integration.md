# Optional FutureNerds notes

Read this file only when the user asks to read or write FutureNerds records, or when this skill's optional FN step is in use. Educational and planning artifacts in this skill still work with no FN access.

Public contract inspected: OpenAPI 3.1.0, API version 1.0.0, server `https://www.futurenerds.dev`, [live OpenAPI](https://www.futurenerds.dev/api/openapi). Authentication in that contract is an HTTP bearer JWT described as a Supabase access token. Paths are named `/api/mcp/tools/...` and many reads use POST. That names a REST surface. It does not verify a deployed MCP protocol endpoint, OAuth onboarding, or an installable connector. Do not add guessed `mcp.json` servers or collect a token in chat or in this repository.

No authenticated call was made while authoring these skills. Runtime authorization, row isolation, pagination, and notification delivery are unverified.

## Required order

1. Call `account_context_get` with an empty JSON object through a client-approved integration. It lists the signed-in account's schools, roles, and available actions.
2. Choose a `school_id` returned for this account. If more than one school is listed, stop and ask which school.
3. Choose a `role` the user actually holds at that school. Tool arguments cannot grant a role. Enums vary by operation: `child_list` allows administrator/teacher/assistant; `observation_list` also allows parent; `billing_invoice_list` allows administrator only.
4. Read the minimum records needed. Do not fetch a whole roster to write a generic activity.
5. If two children share a name, stop until the user supplies the `child_id` (or another unique record id).
6. Produce the standalone artifact first. Then show the exact proposed payload, visibility flags, recipients, and notification effects.
7. Obtain explicit approval for that exact change, audience, and effect. `confirm: true` in a schema is not that approval. Some billing operations declare `confirm: true` in prose while listing `confirm` as an optional property; use the stricter rule and still wait for human approval of the artifact.
8. If approved, execute once through the sanctioned interface and report the returned result, including `meta.requestId` when present. If the result is uncertain, do not retry a mutation.

If there is no connection, wrong school, missing role, or the user declines: keep the standalone artifact and state the access limit.

## Documented side effects

| Operation | Class | Notification or effect |
| --- | --- | --- |
| `observation_create` with `is_parent_visible: true` | write | Notifies the child's guardians |
| `observation_create` with `is_private: true` | write | Summary says a staff-private observation notifies nobody |
| `progress_assessment_create` with `shared_with_parent: true` | write | Notifies guardians |
| `incident_report_file` | write | Notifies every involved child's guardians in-app, by email, and by push |
| `absence_report` | write | Emails the school's staff |
| `message_send` | write; prose requires `confirm: true` | Sends to one thread |
| `message_school_wide_send` | write; prose requires `confirm: true` | Sends an announcement to every active classroom |
| `parent_invitation_send` / `parent_invitation_send_bulk` | write; prose requires `confirm: true` | Emails parent invitations |
| `calendar_create` / `event_create` | write | May notify attendees; confirm calendar, timezone, and recipients |
| `billing_invoice_send` / `billing_invoice_resend` / `billing_invoice_bulk_send` | write; prose requires `confirm: true` | Emails the parent and creates an invoice notification |
| `billing_invoice_create` / `pay` / `refund` / `cancel` | write; prose requires `confirm: true` | Changes financial records |
| `billing_invoice_csv_export` | read | Exports sensitive billing data |
| `child_list` | read | Returns roster data including guardian info |

`billing_invoice_create` summaries truncate around `service_month`. The line-item schema requires `YYYY-MM-01`, not a plain `YYYY-MM`.

## Hard stops

- Do not put credentials, bearer tokens, or school secrets in chat or git.
- Do not invent child ids, observation times, payments, or quotes to make a payload valid.
- Do not send, file, pay, refund, export, or invite because the user asked you to draft.
- Do not continue after a wrong-school or missing-role result by swapping `school_id` or `role` until `account_context_get` shows that pair.
- Synthetic fixtures only in tests and examples.
