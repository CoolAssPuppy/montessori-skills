---
name: school-announcements
description: Draft a school-wide notice from approved facts for an identified audience, with verified date, required action, contact, and access checks. Use for all-school or all-classroom notices. For a message to one family, use family-school-messages. Show exact wording and recipients before any send.
metadata:
  audience: "Admin"
---

# Draft a school-wide notice

Tell a defined audience what changed, when, and what they must do.

## When to use

A fact that applies to many families or all staff: calendar change, drill, closure, policy reminder.

One family: `family-school-messages`. Date placement: `school-calendar-planning`.

## Inputs

- Approved fact and who approved it
- Audience (all families, one program, staff)
- Date, timezone, links, costs already decided
- Contact for questions
- Languages the school supports

## Procedure

1. What changes, who is affected, source, required action.
2. Verify date and timezone against the calendar draft, not against memory.
3. Explain a Montessori term only if the notice is unreadable without it.
4. Access: translation, caption, plain language (S6).
5. White/A6: clear communication; do not present a proposal as settled policy.
6. FN `message_school_wide_send` sends to every active classroom and the OpenAPI prose requires confirm. That is different from `message_send` (one thread). Show wording, classrooms, and effects ([references/integration.md](references/integration.md)).

Do not expose individual records. Do not fabricate urgency. Accreditation claims need their own verification.

## Output

- Subject/title
- Body
- Audience
- Required action
- Contact
- Access checks
- Recipients / classrooms
- Side-effect note
- Approval checkbox

## Adaptations

Short SMS version only if the school uses SMS and the same facts fit.

## Safeguards

See [references/records.md](references/records.md). No automatic send.

## Sources and limits

See [references/evidence.md](references/evidence.md).
