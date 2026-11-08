---
name: factual-observation-notes
description: Rewrite supplied notes as an objective observation with context, supplied time, action or exact quote, assistance, and a separately labeled interpretation. Use when a guide has raw notes to clean. For choosing a next lesson from observations, use observation-to-lesson-plan. For a family-facing report, use progress-report-drafting. Never invent times, quotes, or outcomes.
metadata:
  audience: "Guides"
---

# Write an objective observation

Turn the guide's actual notes into a record another adult could recognize.

## When to use

A guide has raw notes, voice memos, or a short log to clean.

To choose a next lesson, use `observation-to-lesson-plan`. To draft a report, use `progress-report-drafting`. To message one family, use `family-school-messages`.

## Inputs

- The guide's notes, unchanged
- Date, time, and place only if supplied
- Child code or initials the school already uses in this task
- Classroom / program
- Whether the audience is staff-only or family-facing
- Support plan details only if already authorized for this record

## Procedure

1. Copy source locators: who wrote the notes, when they were taken if stated.
2. Fill fields from *Spontaneous Activity in Education* ch. III's observation interests, as a modern log, not as Montessori's form: chosen activity, start and end if known, repetition, persistence amid distraction, resumption after interruption, peer interaction, adult assistance.
3. Put actions and exact quotes only when they appear in the notes. Missing time stays `not recorded`.
4. Place interpretation, motive, and "readiness" talk in a separate labeled field. Elise Arevalo (AMI) asks for objective notes, planned observation, reflection, and referral when concerns persist.
5. Mark one-off versus repeated only when the supplied notes cover more than one event.
6. Check audience. A family-facing sentence needs fewer identifiers and no other child's name.
7. If FutureNerds write is requested, read [references/integration.md](references/integration.md). `observation_create` with `is_parent_visible: true` notifies guardians. Show the payload and flags before any write.

Do not invent progress. Do not diagnose. NAEYC equity guidance: watch observer bias; assess strengths.

## Output

```
Context: program, place, date/time (or not recorded)
Observed: actions / exact quote
Assistance: what the adult did
Social: peers only as needed, no extra names
Interpretation (labeled): ...
Question: ...
Audience: staff | family
Missing: ...
```

## Adaptations

Preserve AAC, sign, or gesture as valid communication in the observed field. Write in the language of the school's record policy.

## Safeguards

See [references/records.md](references/records.md). A pseudonym can still identify a child. One event is not a trend.

## Optional FN

Standalone record first. Writes are optional, authorized, and payload-specific.

## Sources and limits

See [references/evidence.md](references/evidence.md).
