---
name: family-school-messages
description: Draft a recipient-specific message from a guide to one family about a concrete child or classroom matter. Use for individual emails or notes. For a school-wide notice, use school-announcements. For a conference agenda, use montessori-conference-preparation. Show the exact draft and any notification effect before sending.
metadata:
  audience: "Guides"
---

# Draft a message to one family

Write for a named recipient about one matter. Do not send from a draft request.

## When to use

A guide needs to tell **one** family something specific: an injury already documented, a request for a meeting, a missing item, a celebration of observed work.

School-wide: `school-announcements`. Conference agenda: `montessori-conference-preparation`. Observation record: `factual-observation-notes`.

## Inputs

- Relationship and channel (email, notebook, FN thread)
- Topic and verified facts
- Intended audience (which adults)
- What response is requested
- School policy on incidents and medical information

## Procedure

1. Separate event from interpretation. White (AMS 2023): listen, clarify, share goals, rehearse sensitive conversations.
2. State the shared concern in plain language. Invite the family's view.
3. Keep other children unnamed. Keep medical details to approved recipients.
4. Ask for a specific response: a time to talk, a signature, a spare shirt.
5. Show the exact draft. If FN `message_send` is in play, it is a write that the OpenAPI prose marks as requiring `confirm: true`, and it sends to a **thread**, not the whole school. `message_school_wide_send` belongs to school-announcements. Read [references/integration.md](references/integration.md).
6. Urgent safeguarding or injury: a qualified human and the school's procedure go first. The draft can wait.

Hapa Family grace-and-courtesy: respectful tone, no forced apology from the child in the message.

## Output

- Purpose
- Verified facts
- Accessible explanation
- Requested response
- Proposed follow-up
- Recipients
- Channel
- Notification/side-effect note
- Approval checkbox (empty until the user approves this text)

## Adaptations

Write in the family's language when you can. Offer a phone option if the school uses it.

## Safeguards

See [references/records.md](references/records.md). No diagnosis, no unapproved policy exception, no send-on-draft.

## Sources and limits

See [references/evidence.md](references/evidence.md).
