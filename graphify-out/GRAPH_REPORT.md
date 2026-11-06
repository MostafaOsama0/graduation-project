# Graph Report - Graduation project  (2026-11-06)

## Corpus Check
- Corpus is ~7,467 words - fits in a single context window. You may not need a graph.

## Summary
- 211 nodes · 235 edges · 22 communities (12 shown, 10 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Frontend Dependencies & Tooling
- Backend Config & Database Session
- System Architecture & Data Model
- Docker & Infrastructure Orchestration
- Frontend TypeScript App Config
- Vite Build TypeScript Config
- React UI Application Entry
- UI Platform Icons & Sprites
- Project Scope & Team Breakdown
- Oxlint Linter Configuration
- Frontend NPM Scripts
- Brand Assets & Hero Media
- Root TypeScript Solution Config
- Project Risk Register
- Sage API Service Container

## God Nodes (most connected - your core abstractions)
1. `compilerOptions` - 18 edges
2. `compilerOptions` - 15 edges
3. `db` - 7 edges
4. `db-init` - 7 edges
5. `healthcheck` - 6 edges
6. `Sage System Architecture` - 6 edges
7. `Core Relational and Vector Data Model` - 6 edges
8. `SVG Icon Sprite Sheet` - 6 edges
9. `Settings` - 5 edges
10. `health_db()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Sage Project Goal & Original Contributions` --conceptually_related_to--> `Sage AI Academic Assistant`  [INFERRED]
  docs/plans/sage_master_plan.md → README.md
- `Web Application HTML Root` --conceptually_related_to--> `Web Frontend React Application`  [INFERRED]
  apps/web/index.html → README.md
- `React TypeScript Vite Application Template` --conceptually_related_to--> `Web Frontend React Application`  [INFERRED]
  apps/web/README.md → README.md
- `Squad D: Frontend & QA Task Breakdown` --conceptually_related_to--> `Web Frontend React Application`  [INFERRED]
  docs/plans/sage_task_breakdown.md → README.md
- `Contract-First API Design` --rationale_for--> `Core API FastAPI Service`  [INFERRED]
  docs/plans/sage_master_plan.md → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **RAG Ingestion and Cited Retrieval Flow** — docs_plans_sage_master_plan_rag_pipeline, docs_plans_sage_master_plan_vector_store_abstraction, docs_plans_sage_master_plan_entity_chunk, docs_plans_sage_master_plan_entity_citation [EXTRACTED 1.00]
- **Mastery Tracking and Adaptive Scheduling Loop** — docs_plans_sage_master_plan_mastery_model, docs_plans_sage_master_plan_adaptive_scheduler, docs_plans_sage_master_plan_entity_mastery, docs_plans_sage_master_plan_entity_study_task, docs_plans_sage_master_plan_task_lifecycle [EXTRACTED 1.00]
- **Multi-Squad Critical Path Dependency Flow** — docs_plans_sage_task_breakdown_critical_path, docs_plans_sage_task_breakdown_squad_a, docs_plans_sage_task_breakdown_squad_b, docs_plans_sage_task_breakdown_squad_c, docs_plans_sage_task_breakdown_squad_d [EXTRACTED 1.00]
- **Social & Community Platform Icons** — apps_web_public_icons_blueskyicon, apps_web_public_icons_discordicon, apps_web_public_icons_githubicon, apps_web_public_icons_socialicon, apps_web_public_icons_xicon [EXTRACTED 1.00]
- **Web Frontend Brand & Tooling Assets** — apps_web_public_favicon_favicon, apps_web_src_assets_hero_heroillustration, apps_web_src_assets_react_reactlogo, apps_web_src_assets_vite_vitelogo [INFERRED 0.85]

## Communities (22 total, 10 thin omitted)

### Community 0 - "Frontend Dependencies & Tooling"
Cohesion: 0.08
Nodes (32): dependencies, react-dom@^19.2.8, react-router@^8.4.0, @tanstack/react-query@^5.104.1, devDependencies, oxlint@^1.81.0, tailwindcss@^4.3.3, @tailwindcss/vite@^4.3.3 (+24 more)

### Community 1 - "Backend Config & Database Session"
Cohesion: 0.08
Nodes (6): get_settings(), Settings, Base, get_db(), health(), health_db()

### Community 2 - "System Architecture & Data Model"
Cohesion: 0.10
Nodes (27): Web Application HTML Root, Oxlint Linter Configuration, React TypeScript Vite Application Template, Adaptive Study Scheduler, Master System Architecture, Core Relational and Vector Data Model, Chunk Entity, Citation Entity (+19 more)

### Community 3 - "Docker & Infrastructure Orchestration"
Cohesion: 0.07
Nodes (28): condition, container_name, environment, healthcheck, image, depends_on, entrypoint, environment (+20 more)

### Community 4 - "Frontend TypeScript App Config"
Cohesion: 0.10
Nodes (19): compilerOptions, allowArbitraryExtensions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection (+11 more)

### Community 5 - "Vite Build TypeScript Config"
Cohesion: 0.12
Nodes (16): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, lib, module, moduleDetection, noEmit, noFallthroughCasesInSwitch (+8 more)

### Community 6 - "React UI Application Entry"
Cohesion: 0.28
Nodes (3): react@^19.2.8, App(), react

### Community 7 - "UI Platform Icons & Sprites"
Cohesion: 0.29
Nodes (7): Bluesky Social Icon, Discord Social Icon, Documentation Navigation Icon, GitHub Platform Icon, SVG Icon Sprite Sheet, Social Profile Icon, X Platform Icon

### Community 8 - "Project Scope & Team Breakdown"
Cohesion: 0.33
Nodes (7): Sage Project Plans Directory, Confirmed Technical Decisions, Tiered Feature Scope (MVP, Should, Stretch), Sage Project Goal & Original Contributions, Four-Squad Team Allocation, Squad PM Task Breakdown, Sage AI Academic Assistant

### Community 9 - "Oxlint Linter Configuration"
Cohesion: 0.33
Nodes (5): plugins, rules, react/only-export-components, react/rules-of-hooks, $schema

### Community 10 - "Frontend NPM Scripts"
Cohesion: 0.40
Nodes (5): scripts, build, dev, lint, preview

### Community 11 - "Brand Assets & Hero Media"
Cohesion: 0.50
Nodes (4): Web Application Favicon, Hero Illustration, React Framework Logo, Vite Bundler Logo

## Knowledge Gaps
- **16 isolated node(s):** `sage-api`, `Power BI Analytics`, `Oxlint Linter Configuration`, `Web Application HTML Root`, `Confirmed Technical Decisions` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 108 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `react` connect `React UI Application Entry` to `Frontend Dependencies & Tooling`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **What connects `sage-api`, `Power BI Analytics`, `Oxlint Linter Configuration` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Frontend Dependencies & Tooling` be split into smaller, more focused modules?**
  _Cohesion score 0.08377896613190731 - nodes in this community are weakly interconnected._
- **Should `Backend Config & Database Session` be split into smaller, more focused modules?**
  _Cohesion score 0.0846774193548387 - nodes in this community are weakly interconnected._
- **Should `System Architecture & Data Model` be split into smaller, more focused modules?**
  _Cohesion score 0.0960591133004926 - nodes in this community are weakly interconnected._
- **Should `Docker & Infrastructure Orchestration` be split into smaller, more focused modules?**
  _Cohesion score 0.07142857142857142 - nodes in this community are weakly interconnected._
- **Should `Frontend TypeScript App Config` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._