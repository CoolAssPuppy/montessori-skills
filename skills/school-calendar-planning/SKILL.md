---
name: school-calendar-planning
description: Organize proposed school dates around approved constraints, timezone, audience, conflicts, and protected work periods. Use for term planning and event placement. For the notice that announces a date, use school-announcements. Do not invent holidays or staff availability. Calendar writes can notify attendees.
metadata:
  audience: "Admin"
---

# Place dates around the educational day

Build a draft calendar from supplied constraints. Protect work periods the school already defined.

## When to use

Someone is proposing term events, photo day, parent education, or a festival.

The notice itself: `school-announcements`. Classroom-level day: `mixed-age-work-cycle`.

## Inputs

- Term dates, closures, required events already approved
- Timezone
- Staff and room constraints that were supplied
- Audience for each event
- School's work-period times by program

## Procedure

1. Import fixed dates with sources. Everything else is a proposal.
2. Protect age-appropriate work periods (AMS current durations on A2; school handbook wins). A6: place specialties around work.
3. Check room, staff, and access (ramps, captions, childcare for evening parent events if the school offers it).
4. Show conflicts instead of hiding them. Name the approver.
5. White: consistent communication with staff and families. Calendar planning is not a send.
6. FN `calendar_create` / `event_create` are writes and may notify. Confirm owning calendar, timezone, recipients, and approval ([references/integration.md](references/integration.md)).

Do not invent holidays, statutory day counts, or staff availability.

## Output

- Draft table: date, start/end with timezone, audience, source/owner, dependencies, conflict, protected work impacted, approval status
- Unresolved conflicts
- What remains a proposal

## Adaptations

List a remote or recorded option only if the school already offers one.

## Safeguards

Scheduling advice does not override an approved accessibility plan.

## Sources and limits

See [references/evidence.md](references/evidence.md).
