# Sage Task Breakdown v2 (30 weeks, clean rebuild)

Follows [sage_master_plan.md](file:///C:/Users/mstfy/.gemini/antigravity-cli/brain/f34838b2-b1f6-4bad-9500-6c845ca76728/sage_master_plan.md). IDs are stable, so you can paste them into GitHub Projects.

**Owners:** 1 PM · 2 Backend lead · 3 Backend/data · 4 DevOps/QA · 5 AI lead · 6 AI eng · 7 Planner/ML · 8 BI (+FE in phase 2) · 9 FE lead · 10 FE/test.
**Size:** S ≤ 1 day · M = 2-3 days · L ≈ 1 week. **Gates:** G1 wk 4 · G2 wk 10 · G3 wk 15 · G4 wk 19 · G5 wk 24 · G6 wk 30.

## PM
| ID | Task | Wk | Size | Done when |
|---|---|---|---|---|
| PM-01 | Kickoff, GitHub Projects board, 15 two-week sprints | 1 | M | All members assigned |
| PM-02 | Student interviews (5-10) → use cases | 1-2 | L | Supervisor signs off |
| PM-03 | SRS v1 | 2-4 | L | Squad leads reviewed |
| PM-04 | Risk register + weekly log template | 2 | S | Reviewed each sprint |
| PM-05 | Related-work note: reference apps studied (incl. Shiori), originality statement | 1-2 | S | Supervisor informed |
| PM-06 | Sprint planning/review/retro | 1-30 | recurring | Notes in `docs/sprints/` |
| PM-07 | Gate demos (G1-G5) | 4,10,15,19,24 | M each | Checklist signed |
| PM-08 | Thesis ch. 1-3 | 16-22 | L | Draft in repo |
| PM-09 | Thesis ch. 4-7 with squad inputs | 25-28 | L | Draft reviewed |
| PM-10 | Docs freeze, proofreading, demo script, 2 rehearsals | 29-30 | M | Tag `v1.0` |

## Squad A: Platform and Data (2, 3, 4)
| ID | Task | Owner | Wk | Size | Depends | Done when |
|---|---|---|---|---|---|---|
| A-01 | Dev environment: Docker SQL Server 2025, FastAPI skeleton, `.env.example`, setup guide | 4 | 1 | M | none | Every member runs `/health` |
| A-02 | ERD v1 (all MVP entities incl. grades/semesters/assessments) | 3 | 2-3 | L | PM-02 | Reviewed by all squads |
| A-03 | Vector decision: SQL Server `VECTOR` vs ChromaDB spike | 2,5 | 3-4 | M | A-01 | Recorded in SDD |
| A-04 | API contract (OpenAPI) for MVP CRUD + auth | 2 | 3-4 | L | A-02 | Merged; TS types generated |
| A-05 | CI: ruff, pytest, alembic check, web lint/build; branch protection, `CODEOWNERS` | 4 | 3-4 | M | A-01 | Red build blocks merge |
| A-06 | Alembic baseline + core tables | 3 | 5 | M | A-02 | `alembic upgrade head` on clean DB |
| A-07 | Auth: register/login, argon2 hashing, JWT access + refresh | 2 | 5-6 | L | A-06 | Tests pass |
| A-08 | Google OAuth login | 2 | 7 | M | A-07 | Login works |
| A-09 | CRUD: courses, topics, assignments, events | 3 | 5-7 | L | A-06 | Contract tests pass |
| A-10 | CRUD: semesters, assessments, grades + GPA service | 3 | 7-8 | L | A-09 | GPA unit tests pass |
| A-11 | CRUD: notes, decks, flashcards (SM-2 fields) | 3 | 8-9 | M | A-09 | Contract tests pass |
| A-12 | Row-Level Security + two-user isolation tests | 4 | 9-10 | M | A-09 | Zero leaks |
| A-13 | Materials API: upload, list, delete, status; size/type limits | 2 | 10-11 | M | A-06 | Upload stored |
| A-14 | Gamification API: XP, streaks, focus sessions | 3 | 12-13 | M | A-09 | Events award XP |
| A-15 | Indexes + query tuning | 3 | 16-17 | M | A-10 | CRUD p95 < 300 ms |
| A-16 | Audit log, backup/restore script, restore test | 4 | 17-18 | M | A-06 | Restore verified |
| A-17 | Replanning event queue (grade, quiz, deadline, missed task) | 2,3 | 20-21 | L | C-08 | Events delivered |
| A-18 | Notifications (in-app) | 3 | 21-22 | M | A-17 | Visible in test |
| A-19 | Load test (locust) | 4 | 24-25 | M | G5 | Report p95/p99 |
| A-20 | Security review: OWASP, secrets scan, rate limits, upload checks | 4 | 25-26 | L | A-19 | Findings closed |
| A-21 | Staging deployment (API + DB + web), HTTPS | 4 | 25-27 | L | A-20 | Public URL works |
| A-22 | Deployment guide + runbook | 4 | 27 | M | A-21 | Another member deploys from doc |

## Squad B: AI / RAG (5, 6; 10 on eval data)
| ID | Task | Owner | Wk | Size | Depends | Done when |
|---|---|---|---|---|---|---|
| B-01 | RAG/embeddings/eval reading + 1-page summaries | 5,6 | 1-2 | L | none | Shared |
| B-02 | Collect 15-20 course files, 3 subjects, with permission (not in git) | 6,10 | 1-3 | M | none | `eval/data` manifest |
| B-03 | Embedding benchmark (bge-small, MiniLM, +1) | 5 | 3-4 | M | B-02 | Numbers recorded |
| B-04 | PDF extraction with page numbers (PyMuPDF) | 6 | 3-5 | M | B-02 | Text + pages |
| B-05 | `VectorStore` interface + SQL Server adapter | 5 | 5-7 | L | A-03 | Tests pass |
| B-06 | DOCX + PPTX parsing (slides + notes) | 6 | 6-7 | M | B-04 | 3 formats parse |
| B-07 | Chunking (500-800 tokens, 100 overlap, metadata) | 6 | 7-8 | M | B-06 | Chunk stats report |
| B-08 | Ingestion job: upload → parse → chunk → embed → store | 5,6 | 9-11 | L | B-05, A-13 | Status `ready` |
| B-09 | `llm` service: Gemini client, retries, cache, rate limit | 5 | 8-9 | M | A-01 | Unit tests with mock |
| B-10 | Prompt v1: context-only, citations, refusal | 5 | 10 | M | B-09 | Versioned prompt file |
| B-11 | Retrieval API: top-k, user/course filter, threshold | 5 | 11-12 | L | B-08 | Scored chunks |
| B-12 | Chat endpoint: retrieve → generate (stream) → cite → log | 5,6 | 12-13 | L | B-10, B-11 | Cited answer end-to-end |
| B-13 | Refusal logic + out-of-scope tests | 5 | 13-14 | M | B-12 | 25 test questions pass |
| B-14 | Summaries per file/topic | 6 | 13-14 | M | B-12 | Endpoint works |
| B-15 | Eval set v1: 60+ question/answer/source triples | 10,5 | 11-14 | L | B-02 | Committed |
| B-16 | Retrieval eval script (Recall@k, MRR) | 5 | 14-15 | M | B-15 | In report |
| B-17 | Topic extraction + chunk tagging | 6 | 16-17 | L | B-08 | Spot-checked |
| B-18 | Quiz generator (MCQ + short answer), JSON schema, retries | 5,6 | 16-18 | L | B-17 | Valid JSON ≥ 98% |
| B-19 | Quiz scoring → `quiz_attempts` per topic | 6 | 18 | M | B-18 | Feeds mastery |
| B-20 | Flashcard generation from materials | 6 | 18-19 | M | B-17, A-11 | Cards in decks |
| B-21 | Syllabus import via parser + LLM extraction | 6 | 20-21 | M | B-06 | Assignments created |
| B-22 | Answer eval: faithfulness, relevance, citation accuracy | 5,10 | 20-23 | L | B-15 | Eval report v1 |
| B-23 | Tuning: chunk size, k, threshold, re-ranking | 5,6 | 22-24 | L | B-22 | Documented deltas |
| B-24 | Final eval on frozen dataset | 5,10 | 25-26 | L | G5 | Tables + charts |
| B-25 | Privacy: no PII in prompts, delete-materials removes vectors | 5 | 25 | M | B-08 | Test passes |
| B-26 | Evaluation chapter inputs | 5 | 27-28 | M | B-24 | Handed to PM |

## Squad C: Planner and BI (7, 8)
| ID | Task | Owner | Wk | Size | Depends | Done when |
|---|---|---|---|---|---|---|
| C-01 | Study mastery models, BKT, SM-2, scheduling | 7 | 1-2 | L | none | Summary |
| C-02 | Formula doc: mastery, priority, scheduler, replanning | 7 | 2-4 | L | C-01 | Supervisor reviewed |
| C-03 | Seed-data spec: student profiles (strong/weak/busy) | 7 | 3-4 | M | A-02 | Reviewed |
| C-04 | Deterministic seeder (`python -m app.seed`) | 7,3 | 6-9 | L | A-06, C-03 | Loads N students |
| C-05 | Power BI: read-only login + `vw_*` views | 8 | 9-11 | M | A-10 | Report opens |
| C-06 | Power BI star model + DAX measures | 8 | 11-13 | L | C-05 | Model doc |
| C-07 | Mastery engine v1 | 7 | 11-14 | L | C-04 | Unit tests |
| C-08 | Priority + greedy scheduler v1 with "why" strings | 7 | 14-17 | L | C-07 | Plans for seeded students |
| C-09 | Planner API: generate, accept, done/missed | 7,3 | 17-18 | L | C-08 | Contract tests |
| C-10 | Weak-topics API + explanations | 7 | 18-19 | M | C-07, B-19 | Ranked topics |
| C-11 | Planner eval harness | 7 | 19-21 | L | C-08 | Runs on profiles |
| C-12 | LLM-plan baseline for same profiles | 7 | 20-21 | M | C-11, B-09 | Baseline saved |
| C-13 | Adaptive replanning on events | 7,2 | 21-23 | L | A-17 | Plan updates in test |
| C-14 | Weight tuning + sensitivity analysis | 7 | 23-26 | L | C-12, C-13 | Justified weights |
| C-15 | Dashboard 1: grades + GPA trends | 8 | 18-20 | M | C-06 | Published |
| C-16 | Dashboard 2: mastery + weak areas | 8 | 20-22 | M | C-10 | Published |
| C-17 | Dashboard 3: planned vs done hours, workload heatmap | 8 | 22-24 | M | C-13 | Published |
| C-18 | Dashboard 4 (admin): usage, feedback, eval metrics | 8 | 24-26 | M | B-22 | Published |
| C-19 | Stretch: BKT vs weighted mean | 7 | 24-27 | L | C-14 | Comparison table |
| C-20 | Planner + BI chapter inputs | 7,8 | 27-28 | M | C-14 | Handed to PM |

## Squad D: Frontend and QA (9, 10; 8 in weeks 5-10)
| ID | Task | Owner | Wk | Size | Depends | Done when |
|---|---|---|---|---|---|---|
| D-01 | Reference study: feature inventory of Shiori + 2 other apps (notes only, no code) | 9,10 | 1-2 | M | none | Inventory doc |
| D-02 | Sage brand + design system (colors, type, spacing, components) in Figma | 9 | 2-4 | L | D-01 | Reviewed |
| D-03 | Wireframes: all MVP pages | 9,10 | 3-4 | L | PM-03 | Reviewed |
| D-04 | Web scaffold: router, layout shell, auth pages, API client from OpenAPI | 9 | 4-6 | L | A-04 | Login against API |
| D-05 | Component library (shadcn/ui-based, Sage-themed) | 9,8 | 5-6 | L | D-02 | Storybook or demo page |
| D-06 | Dashboard + Courses + Assignments | 9,10 | 6-8 | L | A-09 | E2E green |
| D-07 | Calendar | 8 | 7-8 | M | A-09 | E2E green |
| D-08 | Grades + GPA + semester views | 10,8 | 8-9 | L | A-10 | E2E green |
| D-09 | Notes (markdown editor) | 8 | 9-10 | M | A-11 | E2E green |
| D-10 | Playwright suite + test plan; G2 regression run | 10 | 6-10 | L | D-06 | Green at G2 |
| D-11 | Materials library page | 9 | 11-12 | M | A-13 | Upload/delete works |
| D-12 | Sage chat: streaming, citations, "not found" state, history | 9 | 12-15 | L | B-12 | Citations open file/page |
| D-13 | Summaries UI | 10 | 14-15 | M | B-14 | Works |
| D-14 | Flashcards + SRS review | 10 | 16-18 | L | A-11, B-20 | Reviews scheduled |
| D-15 | Quiz UI + results | 9 | 17-19 | L | B-18 | Attempts saved |
| D-16 | Mastery + weak-topics view | 9 | 19 | M | C-10 | Matches API |
| D-17 | Focus timer, XP, streaks | 10 | 19-20 | M | A-14 | XP on events |
| D-18 | Planner UI: generate, accept, reorder, "why this task" | 9 | 21-24 | L | C-09 | Updates visible |
| D-19 | Analytics page (Recharts) + Power BI links | 10,8 | 22-24 | M | C-15 | Visible |
| D-20 | Notifications UI | 10 | 22-23 | S | A-18 | In header |
| D-21 | Accessibility + responsive check | 10 | 25 | M | G5 | Checklist passed |
| D-22 | User study: 10+ students, SUS | 10,1 | 26-27 | L | A-21 | Results sheet |
| D-23 | UX fixes from study | 9 | 27-28 | M | D-22 | Top 10 closed |
| D-24 | User manual + test report | 9,10 | 28-29 | M | D-23 | PDFs in docs |

## Critical path
`A-02 → A-06 → A-09 → D-06 (G2)` → `B-04 → B-08 → B-11 → B-12 → D-12 (G3)` → `B-17 → B-18 → C-10 (G4)` → `C-08 → A-17 → C-13 → D-18 (G5)`.

## Sprint 1 (weeks 1-2)
- [ ] PM-01, PM-02, PM-04, PM-05
- [ ] A-01 (done by setup below), A-02 started
- [ ] B-01, B-02
- [ ] C-01
- [ ] D-01, D-02 started
