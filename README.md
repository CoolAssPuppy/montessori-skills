# Montessori skills

Task-specific skills for parents, guides, and school administrators. 33 skills in one tree: 10 parent, 12 guide, 10 administrator, and 1 optional FutureNerds adapter.

They organize observation, preparation, and drafting from supplied facts. They do not diagnose children, invent albums or fees, or claim that Montessori programs are universally superior. A 2023 Campbell review reports pooled positive program-level outcomes; a 2026 *Review of Educational Research* abstract (full article not read) questions how credible those advantages are. That disagreement is recorded, not settled.

Primary Montessori texts, AMI/AMS pages, Hapa Family videos (transcripts read), safety authorities, and accounting guidance are cited in each skill's `references/evidence.md`. Attribution is local. None of those organizations endorsed this repository. No external Montessori guide has reviewed these skills yet.

License: not chosen. See [docs/release-review.md](docs/release-review.md).

## Install

Format checks run 8 Nov 2026: Python 3.12.3, `skills-ref` 0.1.1 (`agentskills validate` on all 33), `jsonschema` 4.26.0 on root `plugin.json`, Claude Code 2.1.319 `claude plugin validate . --strict` (passed). Host login and marketplace listing were not performed. A license is still pending, so `--profile directory` is expected to refuse a public Claude directory submission.

**Standalone skill** (any client that loads a skill folder):

```bash
cp -R skills/montessori-at-home ~/.agents/skills/montessori-at-home
```

Point the copy at the client you use. Each folder contains `SKILL.md` and `references/` so it works without the rest of the repo.

**Claude Code plugin** from a local checkout:

```bash
claude plugin validate . --strict
# then load this directory as a plugin, or /plugin-dir, depending on your Claude Code build
```

Claude discovers `skills/` at the plugin root. Manifest: `.claude-plugin/plugin.json`.

**Portable Agent Plugins / Codex** (root `plugin.json`, schema [1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)):

```bash
python3 scripts/validate.py
```

Local Codex/ChatGPT marketplace wiring is documented by OpenAI as a separate step (`marketplace.json` pointing at this folder). This repo is a skills plugin. It has no MCP server and is not a ChatGPT App. Public directory submission was not requested.

FutureNerds is optional. 32 skills produce their artifact with no FN account. Do not put API tokens in chat or in git.

## How to read a row

Audience is the primary reader. Other people may still use the skill. The example is fictional. Source method: [research/source-registry.md](research/source-registry.md).


### Parents

| Skill | Purpose | Example prompt |
| --- | --- | --- |
| [`montessori-at-home`](skills/montessori-at-home/) | Help a family choose a manageable Montessori approach for its actual home and child. | Help us start Montessori at home with our 4-year-old who keeps pouring water at the kitchen sink. We rent a small apartment and already have a low stool. |
| [`prepared-home-environment`](skills/prepared-home-environment/) | Review a home area for safe access, independent participation, and family use. | Review our kitchen for a 2-year-old who uses a walker, plus a crawling baby. The detergent lives under the sink and a bookcase is free-standing. |
| [`everyday-independence`](skills/everyday-independence/) | Break an ordinary self-care or household task into achievable steps with responsive adult help. | Show me how to teach our 5-year-old to put on a jacket without taking over, including what to do on rushed mornings. |
| [`montessori-family-routines`](skills/montessori-family-routines/) | Make a recurring home routine predictable without unnecessary conflict or rigid timing. | School mornings are a fight. Help us make getting out the door calmer for our 6-year-old who wants to finish drawing. |
| [`grace-and-courtesy`](skills/grace-and-courtesy/) | Prepare respectful communication for a concrete social situation. | Our 6-year-old grabs toys when a friend visits. Help us practice asking for a turn, including if our child uses a communication board. |
| [`respectful-limits`](skills/respectful-limits/) | Respond to a difficult moment while protecting safety, dignity, and access. | Our 3-year-old threw a wooden puzzle toward a sibling. What do we do in the moment, and what do we change afterward? |
| [`montessori-school-transitions`](skills/montessori-school-transitions/) | Prepare a child and family for starting school, a new classroom, or a change of program. | Our child starts a 3-6 classroom next month and has never been in group care. Build a transition plan using the school's arrival notes. |
| [`montessori-school-visit`](skills/montessori-school-visit/) | Help a family observe and question a prospective school against its needs. | We tour a mixed-age 3-6 class on Thursday. Our child uses a mobility aid. What should we watch and ask? |
| [`montessori-conference-preparation`](skills/montessori-conference-preparation/) | Help a family turn observations and concerns into a useful conference agenda. | Conference next week. Our child loves pouring work but avoids group line time. Make a one-page agenda from our notes and the school's last report. |
| [`montessori-terms-explained`](skills/montessori-terms-explained/) | Explain a Montessori term in the context where a family encountered it. | The guide wrote that our child is 'normalizing' during the morning work cycle. Explain that word for this 4-year-old classroom. |

### Guides

| Skill | Purpose | Example prompt |
| --- | --- | --- |
| [`factual-observation-notes`](skills/factual-observation-notes/) | Turn a guide's actual notes into a clear, objective observation. | Turn these notes into an observation and keep interpretation separate: 10:12, Mira chose the pink tower, built it twice, left it on the rug when called to snack. |
| [`observation-to-lesson-plan`](skills/observation-to-lesson-plan/) | Choose a small teaching or environmental response from observed evidence and the supplied curriculum. | From this week's notes and our 3-6 practical-life album, propose one next presentation or environment change. Do not invent a lesson we do not have. |
| [`montessori-lesson-preparation`](skills/montessori-lesson-preparation/) | Prepare a guide to present a named lesson from the school's approved curriculum. | Prepare me to present the number rods from our school's 3-6 math album. The child has already used the red rods. |
| [`mixed-age-work-cycle`](skills/mixed-age-work-cycle/) | Plan a mixed-age work period around observed needs and actual school constraints. | Plan tomorrow's 3-hour work cycle for 24 children in 3-6, one assistant, snack prep, and a 10:30 music specialist. |
| [`classroom-environment-review`](skills/classroom-environment-review/) | Review whether a classroom supports safe, accessible, purposeful work. | Walk our 6-9 room from this morning's notes: a blocked aisle, unanchored shelf, and a language table with missing pieces. |
| [`material-care-and-rotation`](skills/material-care-and-rotation/) | Maintain safe, complete materials and make justified availability changes. | The binomial cube is missing a cube and the polishing tray has not been chosen in three weeks. What do we repair, keep, or change? |
| [`montessori-curriculum-map`](skills/montessori-curriculum-map/) | Organize a supplied curriculum across relevant ages, areas, prerequisites, and evidence of learning. | Map this supplied 6-12 cultural album across connections and prerequisites. Do not add lessons that are not in the file. |
| [`progress-report-drafting`](skills/progress-report-drafting/) | Draft a child's progress report from supplied observations, work, and the school's rubric. | Draft Jordan's spring report from these observations and our rubric. Leave blanks where evidence is missing. |
| [`learning-portfolios`](skills/learning-portfolios/) | Select and explain work samples that show learning over time. | From this folder, choose 5 samples that show Jordan's writing from September to March and note what each sample can and cannot show. |
| [`family-school-messages`](skills/family-school-messages/) | Draft a clear message between a guide and family about a concrete matter. | Draft a note to Mira's parents about yesterday's playground fall using only these facts. Do not send it. |
| [`inclusive-lesson-adaptations`](skills/inclusive-lesson-adaptations/) | Identify barriers and adapt a supplied lesson while preserving its objective. | Adapt our pouring lesson for a child who uses a wheelchair and AAC. Keep the same objective and list how we will see whether the concept is there. |
| [`substitute-guide-handoff`](skills/substitute-guide-handoff/) | Prepare a temporary guide to maintain continuity using approved classroom plans and procedures. | I have a medical appointment Thursday. Prepare a handoff for an AMI-trained substitute using our classroom plan and allergy list channel. |

### Admin

| Skill | Purpose | Example prompt |
| --- | --- | --- |
| [`admissions-inquiry-replies`](skills/admissions-inquiry-replies/) | Answer a prospective family's questions using the school's actual program and admissions information. | A family asked if we have a 4-year-old space in January and whether we offer sliding scale. Reply using only the attached admissions sheet. |
| [`family-onboarding`](skills/family-onboarding/) | Help a newly enrolled family understand people, routines, communication, and next actions. | The Rivera family enrolled in the 3-6 class starting 12 January. Build a welcome checklist from our packet and mark missing dates. |
| [`school-handbook-procedures`](skills/school-handbook-procedures/) | Turn an approved handbook section into a clear operational checklist without changing policy. | Turn the late-pickup section on pages 14-15 of the 2026 handbook into a staff checklist. Do not add sanctions. |
| [`montessori-staff-onboarding`](skills/montessori-staff-onboarding/) | Orient a new staff member to their actual role, Montessori practice, and school procedures. | Our new assistant starts Monday in the 0-3 community. Draft a two-week orientation from our staff handbook and observation policy. |
| [`school-calendar-planning`](skills/school-calendar-planning/) | Organize proposed school dates around approved constraints and the educational day. | Place parent-education night, photo day, and the autumn festival around our protected morning work periods using the attached term dates. |
| [`school-announcements`](skills/school-announcements/) | Draft a school-wide notice from approved facts and an identified audience. | Draft a notice that Thursday's work cycle ends at 11:00 for a fire drill. Audience is staff and families. Do not send. |
| [`tuition-billing-explanations`](skills/tuition-billing-explanations/) | Explain a family's tuition schedule or invoice using the actual agreement, policy, and ledger. | Explain invoice 1042 using the attached agreement and ledger. Do not change amounts or mark it paid. |
| [`payment-record-reconciliation`](skills/payment-record-reconciliation/) | Compare payment records with independent source evidence and identify differences. | Compare the March Stripe export with our ledger. List matches, unmatched items, and timing differences. Propose no journals. |
| [`family-feedback-review`](skills/family-feedback-review/) | Summarize family feedback accurately and turn it into reviewable questions or actions. | Summarize these 18 anonymous survey comments into themes, keep contrary views, and list owner questions. Do not draft replies. |
| [`montessori-parent-workshops`](skills/montessori-parent-workshops/) | Plan a focused parent workshop around a real family question and the school's practice. | Plan a 60-minute workshop on cleanup at home after three families asked about morning mess. Use our 3-6 practical-life practice. |

### Integration

| Skill | Purpose | Example prompt |
| --- | --- | --- |
| [`future-nerds`](skills/future-nerds/) | Help an authorized user use verified FutureNerds capabilities safely, with explicit tenant, role, data, and side-effect checks. | I want to record a private observation for synthetic child c_demo_001. Show the exact payload and who would be notified before anything is written. |

## Related skills

Several names sit next to each other on purpose:

- `family-school-messages` is one family, one matter. `school-announcements` is a defined group.
- `factual-observation-notes` cleans notes. `observation-to-lesson-plan` chooses a next move. `montessori-lesson-preparation` prepares a named album lesson. `progress-report-drafting` writes the period report.
- `tuition-billing-explanations` explains an invoice. `payment-record-reconciliation` matches independent payment evidence.

## Limits

- School curriculum, handbooks, calendars, agreements, and ledgers supplied at runtime control school-specific facts.
- Current choking, infant sleep, and furniture-anchoring guidance override historical or practitioner examples that conflict with them.
- Hapa Family is parent/practitioner testimony. Credit is local to the skills that used those videos.
- Maria Montessori editions used: 1912 *The Montessori Method*; 1914 *Dr. Montessori's Own Handbook*; 1917 *Spontaneous Activity in Education*; selected later chapters/quotations listed in the source registry.
