---
name: family-onboarding
description: Build a staged welcome checklist and packet for a newly enrolled family from approved dates, contacts, and required actions. Use after enrollment. For a prospective inquiry, use admissions-inquiry-replies. For the child's first-day plan, use montessori-school-transitions. Do not treat a draft invitation as sent.
metadata:
  audience: "Admin"
---

# Welcome an enrolled family

Stage required forms, orientation, and first-week people. Use the packet the school already approved.

## When to use

Enrollment is in progress or complete and the family needs to know what happens next.

Prospective questions: `admissions-inquiry-replies`. Child's first days: `montessori-school-transitions`. Policy details: `school-handbook-procedures`.

## Inputs

- Enrollment status as recorded
- Approved welcome packet and handbook sections
- Start date, classroom, named contacts
- Required vs optional items
- Family language and access needs already offered

## Procedure

1. Confirm status from records. If a signature or deposit is missing, say enrollment is incomplete.
2. Split **required actions and deadlines** from **optional orientation**.
3. Explain arrival, pickup, illness, and how the school talks to families, quoting the handbook.
4. Invite access information through the private channel the school names. Do not collect extra identity data.
5. S7: collaboration on the first days; White: goals from the start. Put a question block for the family.
6. Track unanswered questions with an owner.
7. FN `parent_invitation_send` emails an invitation and the OpenAPI prose requires confirm. Show recipients before any send ([references/integration.md](references/integration.md)).

Parent-education wording does not bind; handbook excerpts do.

## Output

- Staged checklist (before day 1 / week 1 / first month)
- Contacts
- Required forms and dates (from packet)
- Orientation offers
- Family questions
- Unresolved items
- Source version

## Adaptations

Packet in the family's language or with a reader. Access routes for the building from published information.

## Safeguards

See [references/records.md](references/records.md). No invented settling-in requirement.

## Sources and limits

See [references/evidence.md](references/evidence.md).
