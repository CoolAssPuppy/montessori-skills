# Montessori skills

33 Agent Skills for parents, guides, and school administrators. They turn supplied facts into observation notes, environment checks, lesson preparations, family messages, and office drafts. Ten skills are for parents, twelve for guides, ten for administrators, and one optional FutureNerds adapter.

The same `skills/` tree is packaged as standalone skill folders and as one plugin, `montessori-skills` 0.1.0: Claude Code via `.claude-plugin/plugin.json`, Portable Agent Plugins via root `plugin.json`.

They do not diagnose children, invent albums or fees, or claim program-level efficacy. No external Montessori educator has reviewed this package. Original material is CC0 1.0 (SPDX: CC0-1.0); cited third-party works keep their own terms.

## Install

Draft commands pin branch `cursor/montessori-skills-library-9b0f` because `main` still has only the initial README. Validation does not load a plugin or install a skill.

### Validation (not a load)

Executed 8 Nov 2026 on a checkout of this branch (Python 3.12.3, `skills-ref` 0.1.1, `jsonschema` 4.26.0, Claude Code 2.1.319):

```bash
git clone --branch cursor/montessori-skills-library-9b0f https://github.com/CoolAssPuppy/montessori-skills.git
cd montessori-skills
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
npx --yes @anthropic-ai/claude-code plugin validate . --strict
```

`python3 scripts/validate.py` checks catalog counts, skill frontmatter, local citations, and portable `plugin.json`. It does not install anything.

### Skills: `npx skills add`

Documented CLI (`skills` 1.7.6): `npx skills add <package> --list` lists; `--skill <name>` or `--skill '*'` copies. Executed 8 Nov 2026 in a temporary project directory with `--copy -y -a claude-code`, no `-g`, not the user home. One skill and all 33 copied into that project's `.claude/skills/`, including `references/evidence.md`.

```bash
# list 33 skills, no install
npx --yes skills add https://github.com/CoolAssPuppy/montessori-skills.git#cursor/montessori-skills-library-9b0f --list

# one skill into the current project
npx --yes skills add https://github.com/CoolAssPuppy/montessori-skills.git#cursor/montessori-skills-library-9b0f --skill everyday-independence -a claude-code --copy -y

# all 33 into the current project
npx --yes skills add https://github.com/CoolAssPuppy/montessori-skills.git#cursor/montessori-skills-library-9b0f --skill '*' -a claude-code --copy -y
```

Use the `.git#branch` form. A GitHub `/tree/branch` URL truncates a slash-containing branch name, so the CLI looks for ref `cursor` and fails. After a local clone of this branch, `npx skills add ./ --skill everyday-independence -a claude-code --copy -y` is the same install against the checkout.

Each `skills/<slug>/` folder is also copyable on its own (`SKILL.md` plus `references/`). Point the copy at the skill directory your client documents. Do not treat `~/.agents/skills` as a required path.

### Claude Code plugin

Documented session load ([create a plugin](https://code.claude.com/docs/en/plugins/create), [plugin commands reference](https://code.claude.com/docs/en/plugins/cli-reference)): from the repository root, which holds `.claude-plugin/plugin.json` and `skills/`.

Executed 8 Nov 2026 (Claude Code 2.1.319):

```bash
npx --yes @anthropic-ai/claude-code --plugin-dir . plugin list --json
```

Returned `id` `montessori-skills@inline`, `scope` `session`, `enabled` true. The same `plugin list` without `--plugin-dir` reported no installed plugins. Session load does not write the user plugin store.

An interactive chat that invoked a skill was not run. `claude plugin marketplace add` / `plugin install` would write host config and were not executed.

### Portable Agent Plugins / Codex

Root `plugin.json` uses [schema 1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json). This repo also includes `.agents/plugins/marketplace.json` with `source.path` `./`, matching OpenAI's [repo marketplace](https://developers.openai.com/plugins/build/plugins) layout for a plugin at the clone root.

Documented Codex CLI (not executed; `codex` was not on PATH):

```bash
codex plugin marketplace add CoolAssPuppy/montessori-skills --ref cursor/montessori-skills-library-9b0f
```

or, from a checkout, `codex plugin marketplace add .`. ChatGPT desktop install from that marketplace was not run. This plugin has no MCP server and is not a ChatGPT App.

FutureNerds is optional. Thirty-two skills produce their artifact with no FN account. Do not put API tokens in chat or in git.

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
