---
name: future-nerds
description: Use verified FutureNerds REST capabilities with account_context_get first, then a role the user actually holds, a minimal read, a proposed payload, and explicit approval before any write or notification. Use when the user names FutureNerds or FN records. Other skills still produce a standalone artifact when FN is unavailable. Do not collect tokens, guess MCP, or treat confirm:true as human approval.
metadata:
  audience: "Integration"
---

# Use FutureNerds with explicit checks

Optional adapter. Educational skills in this library still work with no FN account.

## Prerequisite

A host that can send authenticated HTTP JSON to FutureNerds using a bearer token the host already holds. Do not paste tokens into chat or git. Do not add `mcp.json`.

GET [https://www.futurenerds.dev/api/openapi](https://www.futurenerds.dev/api/openapi) and use that document's current `operationId` values, methods, and paths. Schema version and operation-count snapshots are in [references/evidence.md](references/evidence.md).

The public document describes HTTP bearer JWT (Supabase access token) and paths `/api/mcp/tools/{operationId}`. Reads often use POST. That is REST, not proof of MCP, OAuth, or a plugin connector.

## When to use

The user names FutureNerds, FN, or a documented FN operation, and wants records read or a change proposed.

If they want an observation written as prose, start with `factual-observation-notes`. One family email: `family-school-messages`. Invoice explanation: `tuition-billing-explanations`. Then return here only for the record-system step.

## Procedure

1. Confirm the operation exists in the live OpenAPI before proposing a call.
2. Call **`account_context_get`** with `{}` first. Use returned `schools[].school_id`, `roles`, and capabilities. If `next_step` says to create a school, stop; this skill does not create tenants.
3. Resolve **school and a role actually held**. Duplicate school names: ask. A role argument cannot grant permission. If the user is only `parent`, do not call administrator-only billing list.
4. **Minimal read.** Prefer `child_get` with an id over `child_list`. If `child_list` returns two "Jordan"s, stop for `child_id`. Do not export a roster for a generic lesson.
5. **Standalone artifact** from the relevant skill, using only returned or user-supplied facts.
6. **Propose** the exact JSON body, visibility flags, and notification table. Known effects from the contract summaries (re-check live text):
   - `observation_create` parent-visible: notifies guardians; `is_private` summary: notifies nobody
   - `progress_assessment_create` `shared_with_parent`: notifies guardians
   - `incident_report_file`: notifies every involved child's guardians in-app, email, push
   - `absence_report`: emails staff; future dates; refuses past/closed/duplicate teacher dates
   - `message_send`: one thread; prose requires confirm
   - `message_school_wide_send`: every active classroom; prose requires confirm
   - `parent_invitation_send` / bulk: emails invitations; prose requires confirm
   - `billing_invoice_send` / resend / bulk send: emails parent + notification; prose requires confirm
   - `billing_invoice_create` / pay / refund / cancel: financial mutation; prose requires confirm; `confirm` may be optional in JSON schema; still require human approval of this payload; `service_month` pattern `YYYY-MM-01`
7. **Approval** is the user accepting this artifact, audience, and effect. `confirm: true` does not replace that. Show the draft. Wait.
8. **Execute once.** Report `success`, ids, `meta.requestId`. Uncertain result: do not retry a mutation. Reads may be retried.
9. **No access:** keep the standalone artifact and state the limitation.

## Output

- Context summary (schools, roles, chosen pair)
- Minimal-read plan
- Standalone artifact
- Proposed payload
- Notification/recipient review
- Approval state
- Result or limitation

## Tests the agent must refuse

Wrong school; role not in context; duplicate display names without ids; leaking another child; sending because the user said "draft"; retrying pay/send after an unknown error; filling `child_id` with a made-up value.

## Safeguards

Credentials never in chat or git. Synthetic data in examples. See [references/integration.md](references/integration.md) and [references/records.md](references/records.md).

## Sources and limits

See [references/evidence.md](references/evidence.md). Runtime authorization was not tested. No live child or school data was accessed while authoring.
