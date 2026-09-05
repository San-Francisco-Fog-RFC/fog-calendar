# GitHub Copilot instructions

<!-- github-copilot-toolbox:mcp-skills-awareness-begin -->

### MCP & Skills awareness (GitHub Copilot Toolbox)

_Last synced: 2026-09-05T04:00:43.055Z._

- **Full report:** `.github/copilot-toolbox-mcp-skills-awareness.md` in this workspace (auto-overwritten on each scan). Use it as ground truth for configured servers and skill folders.
- **MCP:** For **live tools**, use **Copilot Chat → Agent** and **trust/start** the right servers in the MCP UI.
- **When the user’s task matches a server** (e.g. “open this Confluence page” and a **Confluence** / **Atlassian** MCP is listed), **prefer that server id** and plan on Agent + MCP for actions—not only file search.
- **Skills:** Folders below contain `SKILL.md`; attach or cite paths in chat when relevant.

#### Workspace MCP

- `/Users/melbourne/Documents/antigravity/fog-calendar/.vscode/mcp.json` _(workspace: fog-calendar)_ — _file missing_

_No active workspace servers in mcp.json._

#### User MCP

- `/Users/melbourne/Library/Application Support/Code/User/mcp.json` — _servers defined_

| Server id | Kind | Detail |
|-----------|------|--------|
| lawvie-mcp | http | https://mcp.lawve.ai/mcp |
| open-design | stdio | /Applications/Open Design.app/Contents/Frameworks/Open Design Helper.app/Contents/MacOS/Open Design Helper /Applications/Open Design.app/Contents/Resources/app/prebundled/daemon/daemon-cli.mjs mcp |
| fastmcp-documentation-resource | http | https://abcstark-server.fastmcp.app/mcp |
| MCP_DOCKER | stdio | docker mcp gateway run --profile melb_mcp_server |

#### Project skills

_None found (or no workspace open)._

#### User skills

- **arch-lead** — `/Users/melbourne/.copilot/skills/arch-lead` — Adopt the persona of an Architectural Lead focused on system design,

- **audit-billing** — `/Users/melbourne/.copilot/skills/audit-billing` — Audit law firm billing data (LEDES files, Excel invoices, CSV time entries) for compliance issues, block billing, excessive hours, rate violations, and billing anomalies. Use when: (1) a user provides billing files and a

- **awesome-copilot--acquire-codebase-knowledge** — `/Users/melbourne/.copilot/skills/awesome-copilot--acquire-codebase-knowledge` — Use this skill when the user explicitly asks to map, document, or onboard into an existing codebase. Trigger for prompts like "map this codebase", "document this architecture", "onboard me to this repo", or "create codeb

- **awesome-copilot--add-educational-comments** — `/Users/melbourne/.copilot/skills/awesome-copilot--add-educational-comments` — Add educational comments to the file specified, or prompt asking for file to comment if one is not provided.

- **awesome-copilot--agent-governance** — `/Users/melbourne/.copilot/skills/awesome-copilot--agent-governance` — |

- **awesome-copilot--agentic-eval** — `/Users/melbourne/.copilot/skills/awesome-copilot--agentic-eval` — |

- **awesome-copilot--ai-prompt-engineering-safety-review** — `/Users/melbourne/.copilot/skills/awesome-copilot--ai-prompt-engineering-safety-review` — Comprehensive AI prompt engineering safety review and improvement prompt. Analyzes prompts for safety, bias, security vulnerabilities, and effectiveness while providing detailed improvement recommendations with extensive

- **awesome-copilot--ai-ready** — `/Users/melbourne/.copilot/skills/awesome-copilot--ai-ready` — Make any repo AI-ready — analyzes your codebase and generates AGENTS.md, copilot-instructions.md, CI workflows, issue templates, and more. Mines your PR review patterns and creates files customized to your stack. USE THI

- **awesome-copilot--ai-team-orchestration** — `/Users/melbourne/.copilot/skills/awesome-copilot--ai-team-orchestration` — Bootstrap and run a multi-agent AI development team. Use when: starting a new software project with AI agents, setting up parallel dev/QA teams, creating sprint plans, writing brainstorm prompts with distinct agent voice

- **casing-law** — `/Users/melbourne/.copilot/skills/casing-law` — This skill should be used when the user is writing code with mixed casing conventions, choosing casing for identifiers, enforcing casing consistency across a codebase, or when camelCase and snake_case appear in the same 

- **ccpa-cpra-privacy-expert** — `/Users/melbourne/.copilot/skills/ccpa-cpra-privacy-expert` — >

- **client-memo** — `/Users/melbourne/.copilot/skills/client-memo` — >-

- **corporate** — `/Users/melbourne/.copilot/skills/corporate` — Advises on corporate law matters including entity formation, governance, finance, M&A, securities, venture capital, non-profits, and dissolution. Use when drafting governance documents, structuring transactions, selectin

- **fix** — `/Users/melbourne/.copilot/skills/fix` — Use when you have lint errors, formatting issues, or before committing code to ensure it passes CI.

- **gh-issues** — `/Users/melbourne/.copilot/skills/gh-issues` — Fetch GitHub issues, select candidates, spawn background fix agents, open PRs, and optionally process PR review comments.

- **gog** — `/Users/melbourne/.copilot/skills/gog` — Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

- **hearing-prep** — `/Users/melbourne/.copilot/skills/hearing-prep` — Generates structured hearing preparation briefings from case documents, evidence, authorities, and procedural details. Use when preparing for court hearings, administrative hearings, arbitrations, trials, motion hearings

- **hearing-prep-summary** — `/Users/melbourne/.copilot/skills/hearing-prep-summary` — Produces a quick-reference hearing preparation summary synthesizing pleadings, evidence, witnesses, and governing law into issue matrices, exhibit cross-references, and procedural checklists. Use when preparing for motio

- **hr-business-partner** — `/Users/melbourne/.copilot/skills/hr-business-partner` — >

- **lawyer-analyst** — `/Users/melbourne/.copilot/skills/lawyer-analyst` — |

- **legal-article-summary** — `/Users/melbourne/.copilot/skills/legal-article-summary` — Produces structured summaries of legal scholarship capturing thesis, methodology, key authorities, arguments, and significance. Use when summarizing law review articles, journal articles, case notes, or scholarship for r

- **managing-informed-consent-compliance** — `/Users/melbourne/.copilot/skills/managing-informed-consent-compliance` — Evaluates informed consent practices against state law requirements and institutional policies. Use when auditing consent processes, reviewing consent form adequacy, or managing consent compliance.

- **nonprofit-bylaws** — `/Users/melbourne/.copilot/skills/nonprofit-bylaws` — >-

- **pptx** — `/Users/melbourne/.copilot/skills/pptx` — Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even 

- **public-health-law-summary** — `/Users/melbourne/.copilot/skills/public-health-law-summary` — Generates structured, plain-language summaries of public health legislation and case law with Bluebook citations. Use when summarizing health statutes, vaccination mandates, emergency health powers, disease surveillance 

- **real** — `/Users/melbourne/.copilot/skills/real` — Use gh for GitHub issues, PR status, CI/logs, comments, reviews, releases, and API queries.

- **redundancy-consultation** — `/Users/melbourne/.copilot/skills/redundancy-consultation` — Structure a redundancy consultation process and draft key communications (UK employment law focus). Use when asked to plan a redundancy process, write a redundancy letter, structure a consultation, or manage a reduction 

- **regulatory** — `/Users/melbourne/.copilot/skills/regulatory` — Navigates regulatory compliance, government relations, and administrative law across financial services, healthcare, environmental, FDA, privacy, energy, government contracts, trade, and securities domains. Use when hand

- **request-reviews** — `/Users/melbourne/.copilot/skills/request-reviews` — Generates personalized client review request scripts based on case disposition, client relationship quality, and target platforms (Google, Avvo, Yelp). Produces optimal timing recommendations, platform-specific guidance,

- **search** — `/Users/melbourne/.copilot/skills/search` — Searches the web, legal databases, case law, patents, and case.dev knowledge base via the casedev CLI. Use when the user mentions "search", "legal research", "find cases", "case law", "patent search", "web search", "fetc

- **social-media** — `/Users/melbourne/.copilot/skills/social-media` — Social media strategy, content creation, and platform optimization. Use when creating social content, developing engagement strategies, optimizing for platform algorithms, or building community.

- **sports-law-cases** — `/Users/melbourne/.copilot/skills/sports-law-cases` — Generates structured summaries of sports law cases covering contract disputes, doping violations, and governance controversies. Use when summarizing sports litigation, researching athlete contract disputes, anti-doping a

- **sue** — `/Users/melbourne/.copilot/skills/sue` — A comprehensive AI agent skill for anyone considering or facing a lawsuit. Helps you evaluate whether suing is worth it, understand the litigation process from filing to resolution, prepare your case effectively, navigat

- **surface-performance** — `/Users/melbourne/.copilot/skills/surface-performance` — Transform raw case data exports into a structured performance dashboard -- surfaces KPIs like case volume, resolution time, disposition breakdown, revenue by case type and attorney, intake conversion, and source ROI with

- **using-superpowers** — `/Users/melbourne/.copilot/skills/using-superpowers` — Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

- **verification-loop** — `/Users/melbourne/.copilot/skills/verification-loop` — A comprehensive verification system for Claude Code sessions.

- **web-design** — `/Users/melbourne/.copilot/skills/web-design` — Web graphic design for interfaces, layouts, and visual systems. Use when designing landing pages, dashboards, hero sections, or applying design aesthetics (Bauhaus, Pop Art, Retro, Futuristic). Triggers on "design a", "v

- **arch-lead** — `/Users/melbourne/.claude/skills/arch-lead` — Adopt the persona of an Architectural Lead focused on system design,

- **article-summary** — `/Users/melbourne/.claude/skills/article-summary` — Generates structured 500-800 word summaries of legal articles distilling thesis, methodology, arguments, authorities, conclusions, and significance. Triggers when summarizing legal scholarship, reviewing law review artic

- **audit-billing** — `/Users/melbourne/.claude/skills/audit-billing` — Audit law firm billing data (LEDES files, Excel invoices, CSV time entries) for compliance issues, block billing, excessive hours, rate violations, and billing anomalies. Use when: (1) a user provides billing files and a

- **casing-law** — `/Users/melbourne/.claude/skills/casing-law` — This skill should be used when the user is writing code with mixed casing conventions, choosing casing for identifiers, enforcing casing consistency across a codebase, or when camelCase and snake_case appear in the same 

- **ccpa-cpra-privacy-expert** — `/Users/melbourne/.claude/skills/ccpa-cpra-privacy-expert` — >

- **client-memo** — `/Users/melbourne/.claude/skills/client-memo` — >-

- **corporate** — `/Users/melbourne/.claude/skills/corporate` — Advises on corporate law matters including entity formation, governance, finance, M&A, securities, venture capital, non-profits, and dissolution. Use when drafting governance documents, structuring transactions, selectin

- **fix** — `/Users/melbourne/.claude/skills/fix` — Use when you have lint errors, formatting issues, or before committing code to ensure it passes CI.

- **gh-issues** — `/Users/melbourne/.claude/skills/gh-issues` — Fetch GitHub issues, select candidates, spawn background fix agents, open PRs, and optionally process PR review comments.

- **gog** — `/Users/melbourne/.claude/skills/gog` — Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

- **gsd-add-tests** — `/Users/melbourne/.claude/skills/gsd-add-tests` — Generate tests for a completed phase based on UAT criteria and implementation

- **gsd-ai-integration-phase** — `/Users/melbourne/.claude/skills/gsd-ai-integration-phase` — Generate an AI-SPEC.md design contract for phases that involve building AI systems.

- **gsd-audit-fix** — `/Users/melbourne/.claude/skills/gsd-audit-fix` — Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit

- **gsd-audit-milestone** — `/Users/melbourne/.claude/skills/gsd-audit-milestone` — Audit milestone completion against original intent before archiving

- **gsd-audit-uat** — `/Users/melbourne/.claude/skills/gsd-audit-uat` — Cross-phase audit of all outstanding UAT and verification items

- **gsd-autonomous** — `/Users/melbourne/.claude/skills/gsd-autonomous` — Run all remaining phases autonomously — discuss→plan→execute per phase

- **gsd-capture** — `/Users/melbourne/.claude/skills/gsd-capture` — Capture ideas, tasks, notes, and seeds to their destination

- **gsd-cleanup** — `/Users/melbourne/.claude/skills/gsd-cleanup` — Archive accumulated phase directories from completed milestones

- **gsd-code-review** — `/Users/melbourne/.claude/skills/gsd-code-review` — Review source files changed during a phase for bugs, security issues, and code quality problems

- **gsd-complete-milestone** — `/Users/melbourne/.claude/skills/gsd-complete-milestone` — Archive completed milestone and prepare for next version

- **gsd-config** — `/Users/melbourne/.claude/skills/gsd-config` — Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile

- **gsd-debug** — `/Users/melbourne/.claude/skills/gsd-debug` — Systematic debugging with persistent state across context resets

- **gsd-discuss-phase** — `/Users/melbourne/.claude/skills/gsd-discuss-phase` — Gather phase context through adaptive questioning before planning.

- **gsd-docs-update** — `/Users/melbourne/.claude/skills/gsd-docs-update` — Generate or update project documentation verified against the codebase

- **gsd-eval-review** — `/Users/melbourne/.claude/skills/gsd-eval-review` — Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan.

- **gsd-execute-phase** — `/Users/melbourne/.claude/skills/gsd-execute-phase` — Execute all plans in a phase with wave-based parallelization

- **gsd-explore** — `/Users/melbourne/.claude/skills/gsd-explore` — Socratic ideation and idea routing — think through ideas before committing to plans

- **gsd-extract-learnings** — `/Users/melbourne/.claude/skills/gsd-extract-learnings` — Extract decisions, lessons, patterns, and surprises from completed phase artifacts

- **gsd-fast** — `/Users/melbourne/.claude/skills/gsd-fast` — Execute a trivial task inline — no subagents, no planning overhead

- **gsd-forensics** — `/Users/melbourne/.claude/skills/gsd-forensics` — Post-mortem investigation for failed GSD workflows — diagnoses what went wrong.

- **gsd-graphify** — `/Users/melbourne/.claude/skills/gsd-graphify` — Build, query, and inspect the project knowledge graph in .planning/graphs/

- **gsd-health** — `/Users/melbourne/.claude/skills/gsd-health` — Diagnose planning directory health and optionally repair issues

- **gsd-help** — `/Users/melbourne/.claude/skills/gsd-help` — Show available GSD commands and usage guide

- **gsd-import** — `/Users/melbourne/.claude/skills/gsd-import` — Ingest external plans with conflict detection against project decisions before writing anything.

- **gsd-inbox** — `/Users/melbourne/.claude/skills/gsd-inbox` — Triage and review open GitHub issues and PRs against project templates and contribution guidelines.

- **gsd-ingest-docs** — `/Users/melbourne/.claude/skills/gsd-ingest-docs` — Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo.

- **gsd-manager** — `/Users/melbourne/.claude/skills/gsd-manager` — Interactive command center for managing multiple phases from one terminal

- **gsd-map-codebase** — `/Users/melbourne/.claude/skills/gsd-map-codebase` — Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents

- **gsd-milestone-summary** — `/Users/melbourne/.claude/skills/gsd-milestone-summary` — Generate a comprehensive project summary from milestone artifacts for team onboarding and review

- **gsd-mvp-phase** — `/Users/melbourne/.claude/skills/gsd-mvp-phase` — Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase

- **gsd-new-milestone** — `/Users/melbourne/.claude/skills/gsd-new-milestone` — Start a new milestone cycle — update PROJECT.md and route to requirements

- **gsd-new-project** — `/Users/melbourne/.claude/skills/gsd-new-project` — Initialize a new project with deep context gathering and PROJECT.md

- **gsd-ns-context** — `/Users/melbourne/.claude/skills/gsd-ns-context` — codebase intelligence | map graphify docs learnings

- **gsd-ns-ideate** — `/Users/melbourne/.claude/skills/gsd-ns-ideate` — exploration capture | explore sketch spike spec capture

- **gsd-ns-manage** — `/Users/melbourne/.claude/skills/gsd-ns-manage` — config workspace | workstreams thread update ship inbox

- **gsd-ns-project** — `/Users/melbourne/.claude/skills/gsd-ns-project` — project lifecycle | milestones audits summary

- **gsd-ns-review** — `/Users/melbourne/.claude/skills/gsd-ns-review` — quality gates | code review debug audit security eval ui

- **gsd-ns-workflow** — `/Users/melbourne/.claude/skills/gsd-ns-workflow` — workflow | discuss plan execute verify phase progress

- **gsd-pause-work** — `/Users/melbourne/.claude/skills/gsd-pause-work` — Create context handoff when pausing work mid-phase

- **gsd-phase** — `/Users/melbourne/.claude/skills/gsd-phase` — CRUD for phases in ROADMAP.md — add, insert, remove, or edit phases

- **gsd-plan-phase** — `/Users/melbourne/.claude/skills/gsd-plan-phase` — Create detailed phase plan (PLAN.md) with verification loop

- **gsd-plan-review-convergence** — `/Users/melbourne/.claude/skills/gsd-plan-review-convergence` — Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain.

- **gsd-pr-branch** — `/Users/melbourne/.claude/skills/gsd-pr-branch` — Create a clean PR branch by filtering out .planning/ commits — ready for code review

- **gsd-profile-user** — `/Users/melbourne/.claude/skills/gsd-profile-user` — Generate developer behavioral profile and create Claude-discoverable artifacts

- **gsd-progress** — `/Users/melbourne/.claude/skills/gsd-progress` — Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command

- **gsd-quick** — `/Users/melbourne/.claude/skills/gsd-quick` — Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents

- **gsd-resume-work** — `/Users/melbourne/.claude/skills/gsd-resume-work` — Resume work from previous session with full context restoration

- **gsd-review** — `/Users/melbourne/.claude/skills/gsd-review` — Request cross-AI peer review of phase plans from external AI CLIs

- **gsd-review-backlog** — `/Users/melbourne/.claude/skills/gsd-review-backlog` — Review and promote backlog items to active milestone

- **gsd-secure-phase** — `/Users/melbourne/.claude/skills/gsd-secure-phase` — Retroactively verify threat mitigations for a completed phase

- **gsd-settings** — `/Users/melbourne/.claude/skills/gsd-settings` — Configure GSD workflow toggles and model profile

- **gsd-ship** — `/Users/melbourne/.claude/skills/gsd-ship` — Create PR, run review, and prepare for merge after verification passes

- **gsd-sketch** — `/Users/melbourne/.claude/skills/gsd-sketch` — Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode)

- **gsd-spec-phase** — `/Users/melbourne/.claude/skills/gsd-spec-phase` — Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase.

- **gsd-spike** — `/Users/melbourne/.claude/skills/gsd-spike` — Spike an idea through experiential exploration, or propose what to spike next (frontier mode)

- **gsd-stats** — `/Users/melbourne/.claude/skills/gsd-stats` — Display project statistics — phases, plans, requirements, git metrics, and timeline

- **gsd-surface** — `/Users/melbourne/.claude/skills/gsd-surface` — Toggle which skills are surfaced — apply a profile, list, or disable a cluster without reinstall

- **gsd-thread** — `/Users/melbourne/.claude/skills/gsd-thread` — Manage persistent context threads for cross-session work

- **gsd-ui-phase** — `/Users/melbourne/.claude/skills/gsd-ui-phase` — Generate UI design contract (UI-SPEC.md) for frontend phases

- **gsd-ui-review** — `/Users/melbourne/.claude/skills/gsd-ui-review` — Retroactive 6-pillar visual audit of implemented frontend code

- **gsd-ultraplan-phase** — `/Users/melbourne/.claude/skills/gsd-ultraplan-phase` — [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back.

- **gsd-undo** — `/Users/melbourne/.claude/skills/gsd-undo` — Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks.

- **gsd-update** — `/Users/melbourne/.claude/skills/gsd-update` — Update GSD to latest version with changelog display

- **gsd-validate-phase** — `/Users/melbourne/.claude/skills/gsd-validate-phase` — Retroactively audit and fill Nyquist validation gaps for a completed phase

- **gsd-verify-work** — `/Users/melbourne/.claude/skills/gsd-verify-work` — Validate built features through conversational UAT

- **gsd-workspace** — `/Users/melbourne/.claude/skills/gsd-workspace` — Manage GSD workspaces — create, list, or remove isolated workspace environments

- **gsd-workstreams** — `/Users/melbourne/.claude/skills/gsd-workstreams` — Manage parallel workstreams — list, create, switch, status, progress, complete, and resume

- **hearing-prep** — `/Users/melbourne/.claude/skills/hearing-prep` — Generates structured hearing preparation briefings from case documents, evidence, authorities, and procedural details. Use when preparing for court hearings, administrative hearings, arbitrations, trials, motion hearings

- **hearing-prep-summary** — `/Users/melbourne/.claude/skills/hearing-prep-summary` — Produces a quick-reference hearing preparation summary synthesizing pleadings, evidence, witnesses, and governing law into issue matrices, exhibit cross-references, and procedural checklists. Use when preparing for motio

- **hr-business-partner** — `/Users/melbourne/.claude/skills/hr-business-partner` — >

- **lawyer-analyst** — `/Users/melbourne/.claude/skills/lawyer-analyst` — |

- **legal-article-summary** — `/Users/melbourne/.claude/skills/legal-article-summary` — Produces structured summaries of legal scholarship capturing thesis, methodology, key authorities, arguments, and significance. Use when summarizing law review articles, journal articles, case notes, or scholarship for r

- **managing-informed-consent-compliance** — `/Users/melbourne/.claude/skills/managing-informed-consent-compliance` — Evaluates informed consent practices against state law requirements and institutional policies. Use when auditing consent processes, reviewing consent form adequacy, or managing consent compliance.

- **nonprofit-bylaws** — `/Users/melbourne/.claude/skills/nonprofit-bylaws` — >-

- **pptx** — `/Users/melbourne/.claude/skills/pptx` — Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even 

- **public-health-law-summary** — `/Users/melbourne/.claude/skills/public-health-law-summary` — Generates structured, plain-language summaries of public health legislation and case law with Bluebook citations. Use when summarizing health statutes, vaccination mandates, emergency health powers, disease surveillance 

- **real** — `/Users/melbourne/.claude/skills/real` — Use gh for GitHub issues, PR status, CI/logs, comments, reviews, releases, and API queries.

- **redundancy-consultation** — `/Users/melbourne/.claude/skills/redundancy-consultation` — Structure a redundancy consultation process and draft key communications (UK employment law focus). Use when asked to plan a redundancy process, write a redundancy letter, structure a consultation, or manage a reduction 

- **regulatory** — `/Users/melbourne/.claude/skills/regulatory` — Navigates regulatory compliance, government relations, and administrative law across financial services, healthcare, environmental, FDA, privacy, energy, government contracts, trade, and securities domains. Use when hand

- **request-reviews** — `/Users/melbourne/.claude/skills/request-reviews` — Generates personalized client review request scripts based on case disposition, client relationship quality, and target platforms (Google, Avvo, Yelp). Produces optimal timing recommendations, platform-specific guidance,

- **search** — `/Users/melbourne/.claude/skills/search` — Searches the web, legal databases, case law, patents, and case.dev knowledge base via the casedev CLI. Use when the user mentions "search", "legal research", "find cases", "case law", "patent search", "web search", "fetc

- **social-media** — `/Users/melbourne/.claude/skills/social-media` — Social media strategy, content creation, and platform optimization. Use when creating social content, developing engagement strategies, optimizing for platform algorithms, or building community.

- **sports-law-cases** — `/Users/melbourne/.claude/skills/sports-law-cases` — Generates structured summaries of sports law cases covering contract disputes, doping violations, and governance controversies. Use when summarizing sports litigation, researching athlete contract disputes, anti-doping a

- **sue** — `/Users/melbourne/.claude/skills/sue` — A comprehensive AI agent skill for anyone considering or facing a lawsuit. Helps you evaluate whether suing is worth it, understand the litigation process from filing to resolution, prepare your case effectively, navigat

- **surface-performance** — `/Users/melbourne/.claude/skills/surface-performance` — Transform raw case data exports into a structured performance dashboard -- surfaces KPIs like case volume, resolution time, disposition breakdown, revenue by case type and attorney, intake conversion, and source ROI with

- **ui-craft** — `/Users/melbourne/.claude/skills/ui-craft` — Use for UI design and implementation work to avoid generic AI-looking interfaces. Provides anti-slop rules, a required discovery phase before coding, and guidance for layout, typography, color, motion, accessibility, das

- **ui-craft-dense-dashboard** — `/Users/melbourne/.claude/skills/ui-craft-dense-dashboard` — Dense dashboard / admin / Bloomberg / Retool / data-heavy internal tools. Locked knobs: CRAFT=7, MOTION=3, DENSITY=9. IBM Plex + mono numbers, semantic palette, 4/8px grid, sparklines, tabular-nums. Trigger on: dashboard

- **ui-craft-editorial** — `/Users/melbourne/.claude/skills/ui-craft-editorial` — Editorial / magazine / long-form / Medium / Substack / content-heavy UIs. Locked knobs: CRAFT=9, MOTION=4, DENSITY=3. Serif display + humanist body, wide reading column, drop caps, OpenType. Trigger on: editorial, magazi

- **ui-craft-minimal** — `/Users/melbourne/.claude/skills/ui-craft-minimal` — Minimal / clean / Linear / Notion / Vercel / whitespace-heavy UIs. Locked knobs: CRAFT=8, MOTION=3, DENSITY=2. Monochrome + one accent, Inter/Geist, hairline borders over shadows. Trigger on: minimal, clean, Linear-like,

- **using-superpowers** — `/Users/melbourne/.claude/skills/using-superpowers` — Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

- **verification-loop** — `/Users/melbourne/.claude/skills/verification-loop` — A comprehensive verification system for Claude Code sessions.

- **web-design** — `/Users/melbourne/.claude/skills/web-design` — Web graphic design for interfaces, layouts, and visual systems. Use when designing landing pages, dashboards, hero sections, or applying design aesthetics (Bauhaus, Pop Art, Retro, Futuristic). Triggers on "design a", "v

- **00-andruia-consultant** — `/Users/melbourne/.agents/skills/00-andruia-consultant` — Arquitecto de Soluciones Principal y Consultor Tecnológico de Andru.ia. Diagnostica y traza la hoja de ruta óptima para proyectos de IA en español.

- **007** — `/Users/melbourne/.agents/skills/007` — Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response, and infrastructure security for any project.

- **10-andruia-skill-smith** — `/Users/melbourne/.agents/skills/10-andruia-skill-smith` — Ingeniero de Sistemas de Andru.ia. Diseña, redacta y despliega nuevas habilidades (skills) dentro del repositorio siguiendo el Estándar de Diamante.

- **20-andruia-niche-intelligence** — `/Users/melbourne/.agents/skills/20-andruia-niche-intelligence` — Estratega de Inteligencia de Dominio de Andru.ia. Analiza el nicho específico de un proyecto para inyectar conocimientos, regulaciones y estándares únicos del sector. Actívalo tras definir el nicho.

- **2slides-ppt-generator** — `/Users/melbourne/.agents/skills/2slides-ppt-generator` — AI-powered presentation generation via the 2slides API — create slides from text, match a reference image style, summarize documents into decks, add AI voice narration, and export pages/audio. Use for any \"make slides\"

- **3d-model-generation** — `/Users/melbourne/.agents/skills/3d-model-generation` — Generate 3D models using each::sense AI. Create 3D assets from text or images for games, products, architecture, characters, vehicles, and more with PBR textures.

- **3d-web-experience** — `/Users/melbourne/.agents/skills/3d-web-experience` — Expert in building 3D experiences for the web - Three.js, React

- **60fps-animation** — `/Users/melbourne/.agents/skills/60fps-animation` — This skill should be used when the user asks to "fix janky CSS animation", "make animation 60fps", "stop layout thrashing", "animate width/height/top/left smoothly", "convert animation to transform", "animate box-shadow 

- **ab-test-setup** — `/Users/melbourne/.agents/skills/ab-test-setup` — Structured guide for setting up A/B tests with mandatory gates for hypothesis, metrics, and execution readiness.

- **ab-testing** — `/Users/melbourne/.agents/skills/ab-testing` — When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the user mentions "A/B test," "split test," "experiment," "test this change," "variant

- **acceptance-orchestrator** — `/Users/melbourne/.agents/skills/acceptance-orchestrator` — Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment, and acceptance verification with minimal human re-intervention.

- **accessibility-compliance-accessibility-audit** — `/Users/melbourne/.agents/skills/accessibility-compliance-accessibility-audit` — You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive technology compatibility. Conduct audits, identify barriers, and provide remediation guidance.

- **accessible-animation** — `/Users/melbourne/.agents/skills/accessible-animation` — This skill should be used when the user asks to "respect prefers-reduced-motion", "honor reduced motion", "make my animations accessible", "fix vestibular / motion-sickness issues", "add a useReducedMotion hook", "gate G

- **accesslint-audit** — `/Users/melbourne/.agents/skills/accesslint-audit` — Find and fix WCAG 2.2 accessibility issues. Two modes — report (sweep a codebase or page, produce a prioritized written report, no edits) and fix (audit→edit→verify loop on a target). Prefers direct-CDP live-DOM auditing

- **accesslint-diff** — `/Users/melbourne/.agents/skills/accesslint-diff` — Diff a live page's accessibility violations against a baseline — by default compares uncommitted changes (stash-based), or pass --branch [<name>] to diff against a branch. Reports only new violations introduced, violatio

- **accesslint-scan** — `/Users/melbourne/.agents/skills/accesslint-scan` — Audit a live page for accessibility issues, locate each WCAG violation precisely, and return a selector-grounded fix worklist without editing.

- **accint-solve** — `/Users/melbourne/.agents/skills/accint-solve` — Route agent work through AccInt's MCP memory loop: retrieve prior outcomes, resolve frames, and close commitments with evidence.

- **active-directory-attacks** — `/Users/melbourne/.agents/skills/active-directory-attacks` — Provide comprehensive techniques for attacking Microsoft Active Directory environments. Covers reconnaissance, credential harvesting, Kerberos attacks, lateral movement, privilege escalation, and domain dominance for red

- **activecampaign-automation** — `/Users/melbourne/.agents/skills/activecampaign-automation` — Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment, and tasks. Always search tools first for current schemas.

- **ad-account-auditor** — `/Users/melbourne/.agents/skills/ad-account-auditor` — Use when auditing a paid ad account for incremental contribution, wasted spend, or measurement integrity before scaling; runs a typed 20-item ROAS profile with verified vetoes and a SHIP/FIX/BLOCK/UNDECIDED gate on own e

- **ad-creative** — `/Users/melbourne/.agents/skills/ad-creative` — When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platform. Also use when the user mentions 'ad copy variations,' 'ad

- **ad-creative-builder** — `/Users/melbourne/.agents/skills/ad-creative-builder` — Use when the user asks to "write ad copy", "generate RSA headlines", or "build ad creative at volume"; produces ad units — RSA headlines/descriptions, hooks, and an angle matrix — message-matched to the destination landi

- **ad-test-designer** — `/Users/melbourne/.agents/skills/ad-test-designer` — Use when the user asks to "design an A/B test", "set up a creative/landing test", "run an incrementality test", or "is this result statistically and practically material?"; produces a hypothesis, variant matrix, sample-s

- **address-github-comments** — `/Users/melbourne/.agents/skills/address-github-comments` — Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI.

- **adhx** — `/Users/melbourne/.agents/skills/adhx` — Fetch any X/Twitter post as clean LLM-friendly JSON. Converts x.com, twitter.com, or adhx.com links into structured data with full article content, author info, and engagement metrics. No scraping or browser required.

- **ads** — `/Users/melbourne/.agents/skills/ads` — When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also use when the user mentions 'PPC,' 'paid media,' 'ROAS,' 'CPA,' 'ad campa

- **advanced-evaluation** — `/Users/melbourne/.agents/skills/advanced-evaluation` — This skill should be used when the user asks to "implement LLM-as-judge", "compare model outputs", "create evaluation rubrics", "mitigate evaluation bias", or mentions direct scoring, pairwise comparison, position bias, 

- **advocacy-program-designer** — `/Users/melbourne/.agents/skills/advocacy-program-designer` — Use when the user asks to "design an employee advocacy program", "set up founder-led sharing", or "build a share kit for the team"; produces an advocacy program blueprint in two modes — participation-driven opt-in (defau

- **advogado-criminal** — `/Users/melbourne/.agents/skills/advogado-criminal` — Advogado criminalista especializado em Maria da Penha, violencia domestica, feminicidio, direito penal brasileiro, medidas protetivas, inquerito policial e acao penal.

- **advogado-especialista** — `/Users/melbourne/.agents/skills/advogado-especialista` — Advogado especialista em todas as areas do Direito brasileiro: familia, criminal, trabalhista, tributario, consumidor, imobiliario, empresarial, civil e constitucional.

- **aegisops-ai** — `/Users/melbourne/.agents/skills/aegisops-ai` — Autonomous DevSecOps & FinOps Guardrails. Orchestrates Gemini 3 Flash to audit Linux Kernel patches, Terraform cost drifts, and K8s compliance.

- **after-effects** — `/Users/melbourne/.agents/skills/after-effects` — This skill should be used when the user asks anything about Adobe After Effects — to "write an After Effects expression", "make a wiggle / loopOut / inertial bounce", "rig a control with a slider / null", "build a MOGRT 

- **age-transformation** — `/Users/melbourne/.agents/skills/age-transformation` — Transform faces across ages using each::sense AI. Create age progressions, de-aging effects, baby-to-adult predictions, and aging simulations for entertainment, forensics, and visual effects.

- **agent-creator** — `/Users/melbourne/.agents/skills/agent-creator` — Create custom AI subagents with proper plugin structure, persona generation, and companion routing skills.

- **agent-evaluation** — `/Users/melbourne/.agents/skills/agent-evaluation` — Testing and benchmarking LLM agents including behavioral testing,

- **agent-framework-azure-ai-py** — `/Users/melbourne/.agents/skills/agent-framework-azure-ai-py` — Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK.

- **agent-manager-skill** — `/Users/melbourne/.agents/skills/agent-manager-skill` — Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling.

- **agent-memory-mcp** — `/Users/melbourne/.agents/skills/agent-memory-mcp` — A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions).

- **agent-memory-systems** — `/Users/melbourne/.agents/skills/agent-memory-systems` — Memory is the cornerstone of intelligent agents. Without it, every

- **agent-orchestration-improve-agent** — `/Users/melbourne/.agents/skills/agent-orchestration-improve-agent` — Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration.

- **agent-orchestration-multi-agent-optimize** — `/Users/melbourne/.agents/skills/agent-orchestration-multi-agent-optimize` — Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration. Use when improving agent performance, throughput, or reliability.

- **agent-orchestrator** — `/Users/melbourne/.agents/skills/agent-orchestrator` — Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management.

- **agent-squad** — `/Users/melbourne/.agents/skills/agent-squad` — Main agent orchestrator that coordinates a specialized squad of agents

- **agent-tool-builder** — `/Users/melbourne/.agents/skills/agent-tool-builder` — Tools are how AI agents interact with the world. A well-designed

- **agentflow** — `/Users/melbourne/.agents/skills/agentflow` — Orchestrate autonomous AI development pipelines through your Kanban board (Asana, GitHub Projects, Linear). Manages multi-worker Claude Code dispatch, deterministic quality gates, adversarial review, per-task cost tracki

- **agentfolio** — `/Users/melbourne/.agents/skills/agentfolio` — Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory.

- **agentic-actions-auditor** — `/Users/melbourne/.agents/skills/agentic-actions-auditor` — >

- **agentmail** — `/Users/melbourne/.agents/skills/agentmail` — Email infrastructure for AI agents. Create accounts, send/receive emails, manage webhooks, and check karma balance via the AgentMail API.

- **agentphone** — `/Users/melbourne/.agents/skills/agentphone` — Build AI phone agents with AgentPhone API. Use when the user wants to make phone calls, send/receive SMS, manage phone numbers, create voice agents, set up webhooks, or check usage — anything related to telephony, phone 

- **agents-md** — `/Users/melbourne/.agents/skills/agents-md` — This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up CLAUDE.md", or needs to keep agent instructions concise. Enforces research-backed best practices for 

- **agents-v2-py** — `/Users/melbourne/.agents/skills/agents-v2-py` — Build container-based Foundry Agents with Azure AI Projects SDK (ImageBasedHostedAgentDefinition). Use when creating hosted agents with custom container images in Azure AI Foundry.

- **agenttrace-session-audit** — `/Users/melbourne/.agents/skills/agenttrace-session-audit` — Audit local AI coding-agent sessions with agenttrace for cost, tool failures, latency, anomalies, health, diffs, and CI gates.

- **ai-agent-development** — `/Users/melbourne/.agents/skills/ai-agent-development` — AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents.

- **ai-agents-architect** — `/Users/melbourne/.agents/skills/ai-agents-architect` — Expert in designing and building autonomous AI agents. Masters tool

- **ai-analyzer** — `/Users/melbourne/.agents/skills/ai-analyzer` — AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。

- **ai-avatar-generation** — `/Users/melbourne/.agents/skills/ai-avatar-generation` — Generate AI avatars from photos or text descriptions using each::sense. Create professional headshots, cartoon avatars, 3D characters, fantasy personas, gaming avatars, and consistent character designs for various platfo

- **ai-dev-jobs-mcp** — `/Users/melbourne/.agents/skills/ai-dev-jobs-mcp` — Search 8,400+ AI and ML jobs across 489 companies, inspect listings and employers, match roles, and view salary and market stats via AI Dev Jobs MCP

- **ai-elements** — `/Users/melbourne/.agents/skills/ai-elements` — Build AI chat interfaces using ai-elements components — conversations, messages, tool displays, prompt inputs, and more. Use when the user wants to build a chatbot, AI assistant UI, or any AI-powered chat interface.

- **ai-engineer** — `/Users/melbourne/.agents/skills/ai-engineer` — Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orchestration, and enterprise AI integrations.

- **ai-engineering-toolkit** — `/Users/melbourne/.agents/skills/ai-engineering-toolkit` — 6 production-ready AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent security audit (65-point checklist), eval harness building, and product sense coac

- **ai-headshot-generation** — `/Users/melbourne/.agents/skills/ai-headshot-generation` — Generate professional AI headshots from casual photos using each::sense AI. Create corporate portraits, LinkedIn photos, executive headshots, team photos, and more with consistent, professional quality.

- **ai-influencer-generation** — `/Users/melbourne/.agents/skills/ai-influencer-generation` — Generate consistent AI influencer personas and social media content using each::sense API

- **ai-md** — `/Users/melbourne/.agents/skills/ai-md` — Convert human-written CLAUDE.md into AI-native structured-label format. Battle-tested across 4 models. Same rules, fewer tokens, higher compliance.

- **ai-ml** — `/Users/melbourne/.agents/skills/ai-ml` — AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML pipelines, and AI-powered features.

- **ai-native-cli** — `/Users/melbourne/.agents/skills/ai-native-cli` — Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, and agent self-description.

- **ai-product** — `/Users/melbourne/.agents/skills/ai-product` — Every product will be AI-powered. The question is whether you'll

- **ai-seo** — `/Users/melbourne/.agents/skills/ai-seo` — When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'answer engine optimization,' 'generati

- **ai-studio-image** — `/Users/melbourne/.agents/skills/ai-studio-image` — Geracao de imagens humanizadas via Google AI Studio (Gemini). Fotos realistas estilo influencer ou educacional com iluminacao natural e imperfeicoes sutis.

- **ai-wrapper-product** — `/Users/melbourne/.agents/skills/ai-wrapper-product` — Expert in building products that wrap AI APIs (OpenAI, Anthropic,

- **airflow-dag-patterns** — `/Users/melbourne/.agents/skills/airflow-dag-patterns` — Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelines, orchestrating workflows, or scheduling batch jobs.

- **airtable-automation** — `/Users/melbourne/.agents/skills/airtable-automation` — Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views. Always search tools first for current schemas.

- **akf-trust-metadata** — `/Users/melbourne/.agents/skills/akf-trust-metadata` — The AI native file format. EXIF for AI — stamps every file with trust scores, source provenance, and compliance metadata. Embeds into 20+ formats (DOCX, PDF, images, code). EU AI Act, SOX, HIPAA auditing.

- **album-cover-generation** — `/Users/melbourne/.agents/skills/album-cover-generation` — Generate professional music album covers using each::sense AI. Create artwork for hip-hop, rock, pop, electronic, jazz, classical, indie albums, singles, EPs, and Spotify canvas visuals.

- **algolia-search** — `/Users/melbourne/.agents/skills/algolia-search` — Expert patterns for Algolia search implementation, indexing

- **algorithmic-art** — `/Users/melbourne/.agents/skills/algorithmic-art` — Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output .md files (philosophy), .html files (interactive viewer), and .js files (generative algorithms).

- **alpha-vantage** — `/Users/melbourne/.agents/skills/alpha-vantage` — Access 20+ years of global financial data: equities, options, forex, crypto, commodities, economic indicators, and 50+ technical indicators.

- **amazon-alexa** — `/Users/melbourne/.agents/skills/amazon-alexa` — Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude como cerebro (projeto Auri) e integrar com AWS ecosystem (Lambda, DynamoDB, Polly, Transcribe, Lex, S

- **amplitude-automation** — `/Users/melbourne/.agents/skills/amplitude-automation` — Automate Amplitude tasks via Rube MCP (Composio): events, user activity, cohorts, user identification. Always search tools first for current schemas.

- **analytics** — `/Users/melbourne/.agents/skills/analytics` — When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking," "GA4," "Google Analytics," "conversion tracking," "event tracking," "UTM parameters,

- **analytics-product** — `/Users/melbourne/.agents/skills/analytics-product` — Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto.

- **analytics-tracking** — `/Users/melbourne/.agents/skills/analytics-tracking` — When the user wants to set up, audit, or optimize analytics tracking (GA4, events, conversions). Also use when the user mentions "Google Analytics," "GA4," "event tracking," "conversions," "attribution model," "gtag," "d

- **analyze-project** — `/Users/melbourne/.agents/skills/analyze-project` — Forensic root cause analyzer for Antigravity sessions. Classifies scope deltas, rework patterns, root causes, hotspots, and auto-improves prompts/health.

- **andrej-karpathy** — `/Users/melbourne/.agents/skills/andrej-karpathy` — Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.

- **android-cli** — `/Users/melbourne/.agents/skills/android-cli` — Orchestrates Android development tasks including project creation, deployment, SDK management, and environment diagnostics using the `android` command-line tool.

- **android-dev** — `/Users/melbourne/.agents/skills/android-dev` — Production-grade Android app development guide covering native (Kotlin/Java), cross-platform (Flutter, RN, KMM), and hybrid architectures.

- **android-jetpack-compose-expert** — `/Users/melbourne/.agents/skills/android-jetpack-compose-expert` — Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance, and Material Design 3.

- **android-ui-journey-testing** — `/Users/melbourne/.agents/skills/android-ui-journey-testing` — XML-specified Android UI journey testing, interactive step execution, assertion verification, and JSON outcome reporting.

- **android_ui_verification** — `/Users/melbourne/.agents/skills/android_ui_verification` — Automated end-to-end UI testing and verification on an Android Emulator using ADB.

- **angular** — `/Users/melbourne/.agents/skills/angular` — Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration, and reactive patterns.

- **angular-best-practices** — `/Users/melbourne/.agents/skills/angular-best-practices` — Angular performance optimization and best practices guide. Use when writing, reviewing, or refactoring Angular code for optimal performance, bundle size, and rendering efficiency.

- **angular-migration** — `/Users/melbourne/.agents/skills/angular-migration` — Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes, and routing migration.

- **angular-state-management** — `/Users/melbourne/.agents/skills/angular-state-management` — Master modern Angular state management with Signals, NgRx, and RxJS. Use when setting up global state, managing component stores, choosing between state solutions, or migrating from legacy patterns.

- **angular-ui-patterns** — `/Users/melbourne/.agents/skills/angular-ui-patterns` — Modern Angular UI patterns for loading states, error handling, and data display. Use when building UI components, handling async data, or managing component states.

- **animation-principles** — `/Users/melbourne/.agents/skills/animation-principles` — This skill should be used when the user asks to "make this animation feel natural", "fix motion that feels stiff/floaty/cheap", "my animation looks robotic", "choose an easing curve", "how do I use the Graph Editor", "ad

- **anime-avatar-generation** — `/Users/melbourne/.agents/skills/anime-avatar-generation` — Generate anime-style avatars and characters using each::sense AI. Transform photos into anime, create Ghibli-style portraits, manga characters, chibi avatars, and full character sheets with multiple angles.

- **animejs-animation** — `/Users/melbourne/.agents/skills/animejs-animation` — Advanced JavaScript animation library skill for creating complex, high-performance web animations.

- **anti-reversing-techniques** — `/Users/melbourne/.agents/skills/anti-reversing-techniques` — AUTHORIZED USE ONLY: This skill contains dual-use security techniques. Before proceeding with any bypass or analysis: > 1.

- **anti-sycophancy** — `/Users/melbourne/.agents/skills/anti-sycophancy` — Eliminate sycophantic agreement patterns in AI responses. Load via /skill anti-sycophancy.

- **antigravity-agent-manager** — `/Users/melbourne/.agents/skills/antigravity-agent-manager` — Configure and orchestrate parallel agents using the standalone Antigravity 2.0 Agent Manager and Antigravity IDE.

- **antigravity-design-expert** — `/Users/melbourne/.agents/skills/antigravity-design-expert` — Core UI/UX engineering skill for building highly interactive, spatial, weightless, and glassmorphism-based web interfaces using GSAP and 3D CSS.

- **antigravity-manager** — `/Users/melbourne/.agents/skills/antigravity-manager` — AI coding agent skill for Antigravity Manager — a Tauri v2 + Rust desktop app and Docker service that manages multiple Google/Anthropic accounts and proxies them as standard OpenAI/Anthropic/Gemini API endpoints with int

- **antigravity-skill-orchestrator** — `/Users/melbourne/.agents/skills/antigravity-skill-orchestrator` — A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill combinations using agent-memory-mcp, and prevents skill overuse for simple tasks.

- **antigravity-workflows** — `/Users/melbourne/.agents/skills/antigravity-workflows` — Orchestrate multiple Antigravity skills through guided workflows for SaaS MVP delivery, security audits, AI agent builds, and browser QA.

- **aomi-transact** — `/Users/melbourne/.agents/skills/aomi-transact` — Build natural-language crypto/DeFi agents and EVM MCP plugins (Claude Code, Cursor, Codex, Gemini). Aomi turns prompts into wallet-signed txs on Ethereum, Base, Arbitrum, Optimism, Polygon, Linea — non-custodial, fork-si

- **api-design-principles** — `/Users/melbourne/.agents/skills/api-design-principles` — Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers and stand the test of time.

- **api-documentation** — `/Users/melbourne/.agents/skills/api-documentation` — API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation.

- **api-documentation-generator** — `/Users/melbourne/.agents/skills/api-documentation-generator` — Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices

- **api-documenter** — `/Users/melbourne/.agents/skills/api-documenter` — Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SDKs, and build comprehensive developer portals.

- **api-endpoint-builder** — `/Users/melbourne/.agents/skills/api-endpoint-builder` — Builds production-ready REST API endpoints with validation, error handling, authentication, and documentation. Follows best practices for security and scalability.

- **api-fuzzing-bug-bounty** — `/Users/melbourne/.agents/skills/api-fuzzing-bug-bounty` — Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements. Covers vulnerability discovery, authentication bypass, IDOR exploitation, and API-s

- **api-patterns** — `/Users/melbourne/.agents/skills/api-patterns` — API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination.

- **api-security-best-practices** — `/Users/melbourne/.agents/skills/api-security-best-practices` — Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities

- **api-security-testing** — `/Users/melbourne/.agents/skills/api-security-testing` — API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices.

- **api-testing-observability-api-mock** — `/Users/melbourne/.agents/skills/api-testing-observability-api-mock` — You are an API mocking expert specializing in realistic mock services for development, testing, and demos. Design mocks that simulate real API behavior and enable parallel development.

- **apify-actor-development** — `/Users/melbourne/.agents/skills/apify-actor-development` — Important: Before you begin, fill in the generatedBy property in the meta section of .actor/actor.json. Replace it with the tool and model you're currently using, such as \"Claude Code with Claude Sonnet 4.5\". This help

- **apify-actorization** — `/Users/melbourne/.agents/skills/apify-actorization` — Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-defined JSON input, perform an action, and 

- **apify-audience-analysis** — `/Users/melbourne/.agents/skills/apify-audience-analysis` — Understand audience demographics, preferences, behavior patterns, and engagement quality across Facebook, Instagram, YouTube, and TikTok.

- **apify-brand-reputation-monitoring** — `/Users/melbourne/.agents/skills/apify-brand-reputation-monitoring` — Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors.

- **apify-competitor-intelligence** — `/Users/melbourne/.agents/skills/apify-competitor-intelligence` — Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTube, and TikTok.

- **apify-content-analytics** — `/Users/melbourne/.agents/skills/apify-content-analytics` — Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok.

- **apify-ecommerce** — `/Users/melbourne/.agents/skills/apify-ecommerce` — Extract product data, prices, reviews, and seller information from any e-commerce platform using Apify's E-commerce Scraping Tool.

- **apify-influencer-discovery** — `/Users/melbourne/.agents/skills/apify-influencer-discovery` — Find and evaluate influencers for brand partnerships, verify authenticity, and track collaboration performance across Instagram, Facebook, YouTube, and TikTok.

- **apify-lead-generation** — `/Users/melbourne/.agents/skills/apify-lead-generation` — Scrape leads from multiple platforms using Apify Actors.

- **apify-market-research** — `/Users/melbourne/.agents/skills/apify-market-research` — Analyze market conditions, geographic opportunities, pricing, consumer behavior, and product validation across Google Maps, Facebook, Instagram, Booking.com, and TripAdvisor.

- **apify-trend-analysis** — `/Users/melbourne/.agents/skills/apify-trend-analysis` — Discover and track emerging trends across Google Trends, Instagram, Facebook, YouTube, and TikTok to inform content strategy.

- **apify-ultimate-scraper** — `/Users/melbourne/.agents/skills/apify-ultimate-scraper` — AI-driven data extraction from 55+ Actors across all major platforms. This skill automatically selects the best Actor for your task.

- **app-builder** — `/Users/melbourne/.agents/skills/app-builder` — Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents.

- **app-store-changelog** — `/Users/melbourne/.agents/skills/app-store-changelog` — Generate user-facing App Store release notes from git history since the last tag.

- **app-store-optimization** — `/Users/melbourne/.agents/skills/app-store-optimization` — Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Google Play Store

- **app-store-screenshot-generation** — `/Users/melbourne/.agents/skills/app-store-screenshot-generation` — Generate App Store and Google Play screenshot assets using each::sense AI. Create device-framed screenshots, feature highlights, localized versions, and promotional visuals optimized for iOS App Store and Google Play Sto

- **appdeploy** — `/Users/melbourne/.agents/skills/appdeploy` — Deploy web apps with backend APIs, database, and file storage. Use when the user asks to deploy or publish a website or web app and wants a public URL. Uses HTTP API via curl.

- **apple-notes-search** — `/Users/melbourne/.agents/skills/apple-notes-search` — Semantic + keyword search and connection-discovery across the user's own Apple Notes via the apple-notes MCP server. Use when the user wants to find, recall, or synthesize something from their notes, or surface non-obvio

- **application-performance-performance-optimization** — `/Users/melbourne/.agents/skills/application-performance-performance-optimization` — Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. Use when coordinating performance optimization across the stack.

- **ar-filter-generation** — `/Users/melbourne/.agents/skills/ar-filter-generation` — Generate AR filters and face effects using each::sense AI. Create face filters, beauty effects, makeup overlays, branded AR experiences, and 3D face tracking effects for social media platforms.

- **architect-review** — `/Users/melbourne/.agents/skills/architect-review` — Master software architect specializing in modern architecture

- **architecture** — `/Users/melbourne/.agents/skills/architecture` — Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design.

- **architecture-decision-records** — `/Users/melbourne/.agents/skills/architecture-decision-records` — Comprehensive patterns for creating, maintaining, and managing Architecture Decision Records (ADRs) that capture the context and rationale behind significant technical decisions.

- **architecture-patterns** — `/Users/melbourne/.agents/skills/architecture-patterns` — Master proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design to build maintainable, testable, and scalable systems.

- **architecture-rendering** — `/Users/melbourne/.agents/skills/architecture-rendering` — Generate photorealistic architectural renders and visualizations using each::sense AI. Create exterior views, interior renders, sketch-to-render conversions, and more for architects, designers, and real estate profession

- **arm-cortex-expert** — `/Users/melbourne/.agents/skills/arm-cortex-expert` — Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52, SAMD).

- **article-content** — `/Users/melbourne/.agents/skills/article-content` — When the user wants to write, generate, or create article body content—blog post body, long-form content, how-to guide, listicle. Also use when the user mentions "write article," "article content," "blog post content," "

- **article-illustrations** — `/Users/melbourne/.agents/skills/article-illustrations` — Generate hand-drawn 16:9 article illustrations with the Grav character IP, sparse annotations, and absurd but clear visual metaphors.

- **asana-automation** — `/Users/melbourne/.agents/skills/asana-automation` — Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces. Always search tools first for current schemas.

- **ascii-animation** — `/Users/melbourne/.agents/skills/ascii-animation` — This skill should be used when the user asks to "make an ASCII animation", "build a terminal/CLI intro or loader", "convert an image or video to ASCII art", "add an ASCII shader/post-effect to a canvas or Three.js scene"

- **ask-gemini** — `/Users/melbourne/.agents/skills/ask-gemini` — This skill should be used when the user asks to "ask Gemini", "get Gemini's opinion", "have Gemini review", "improve writing style", "make less AI-sounding", "get feedback on article", "review this draft", "Nano Banana",

- **ask-matt** — `/Users/melbourne/.agents/skills/ask-matt` — Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.

- **ask-questions-if-underspecified** — `/Users/melbourne/.agents/skills/ask-questions-if-underspecified` — Clarify requirements before implementing. Use when serious doubts arise.

- **aso** — `/Users/melbourne/.agents/skills/aso` — When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO audit,' 'app store optimization,' 'optimize my app listing,' 'improve app visibility,' 'app store ranking

- **astro** — `/Users/melbourne/.agents/skills/astro` — Build content-focused websites with Astro — zero JS by default, islands architecture, multi-framework components, and Markdown/MDX support.

- **astropy** — `/Users/melbourne/.agents/skills/astropy` — Astropy is the core Python package for astronomy, providing essential functionality for astronomical research and data analysis.

- **async-python-patterns** — `/Users/melbourne/.agents/skills/async-python-patterns` — Comprehensive guidance for implementing asynchronous Python applications using asyncio, concurrent programming patterns, and async/await for building high-performance, non-blocking systems.

- **atlas-contract** — `/Users/melbourne/.agents/skills/atlas-contract` — Goal-integrity skill. Use for backend/API/persistence, preserve/do-not-change, tests/validation, mocks, rework, multi-part requests. Emits Goal Contracts, Deviation Notices, Phase Checks, Final Audits. Skip for Q&A or tr

- **atlas-ledger** — `/Users/melbourne/.agents/skills/atlas-ledger` — Companion to atlas-contract. Auto-invoked by its Final Audit on caught drift; also use after Post Reviews or user requests to record a mistake. Distills drift into WHEN/DON'T/INSTEAD clauses, writes to Atlas.md after con

- **attack-tree-construction** — `/Users/melbourne/.agents/skills/attack-tree-construction` — Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicating security risks to stakeholders.

- **attribution** — `/Users/melbourne/.agents/skills/attribution` — When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an attribution model, or reconcile conflicting numbers across tools. Also use when the user mentions "attribu

- **attribution-reconciler** — `/Users/melbourne/.agents/skills/attribution-reconciler` — Use when platform-reported conversions disagree with GA4/ecommerce, when you suspect Meta and Google are double-counting the same sales, or for a standing (monthly) reconciliation workbook that de-dups stacked credit aga

- **audience-belief-mapper** — `/Users/melbourne/.agents/skills/audience-belief-mapper` — Use when the user asks to "map what our buyers believe", "capture the objections we keep hearing", or "find the switching forces that move the beachhead"; produces a belief map of the beachhead — held beliefs and mental 

- **audience-mapper** — `/Users/melbourne/.agents/skills/audience-mapper` — Use when the user asks to "analyze my target audience", "build an audience profile for influencer targeting", "research a niche community", or "deep-dive a subculture before partnering with creators"; in audience mode pr

- **audience-segment-builder** — `/Users/melbourne/.agents/skills/audience-segment-builder` — Use when the user asks to "build audience segments from my customer list", "make value-based / lookalike seed lists", "set up exclusion / suppression segments", or "map audiences to funnel stages across platforms"; turns

- **audio-transcriber** — `/Users/melbourne/.agents/skills/audio-transcriber` — Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration

- **audio-visualization** — `/Users/melbourne/.agents/skills/audio-visualization` — Generate audio visualization videos using each::sense AI. Create waveforms, spectrum analyzers, particle effects, 3D visualizations, and beat-synced animations from audio files.

- **audit-context-building** — `/Users/melbourne/.agents/skills/audit-context-building` — Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding.

- **audit-skills** — `/Users/melbourne/.agents/skills/audit-skills` — Expert security auditor for AI Skills and Bundles. Performs non-intrusive static analysis to identify malicious patterns, data leaks, system stability risks, and obfuscated payloads across Windows, macOS, Linux/Unix, and

- **auri-core** — `/Users/melbourne/.agents/skills/auri-core` — Auri: assistente de voz inteligente (Alexa + Claude claude-opus-4-20250805). Visao do produto, persona Vitoria Neural, stack AWS, modelo Free/Pro/Business/Enterprise, roadmap 4 fases, GTM, north star WAC e analise compet

- **auth-implementation-patterns** — `/Users/melbourne/.agents/skills/auth-implementation-patterns` — Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices.

- **autonomous-agent-patterns** — `/Users/melbourne/.agents/skills/autonomous-agent-patterns` — Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://github.com/openai/codex).

- **autonomous-agents** — `/Users/melbourne/.agents/skills/autonomous-agents` — Autonomous agents are AI systems that can independently decompose

- **avalonia-layout-zafiro** — `/Users/melbourne/.agents/skills/avalonia-layout-zafiro` — Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redundancy.

- **avalonia-viewmodels-zafiro** — `/Users/melbourne/.agents/skills/avalonia-viewmodels-zafiro` — Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI.

- **avalonia-zafiro-development** — `/Users/melbourne/.agents/skills/avalonia-zafiro-development` — Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit.

- **avatar-portrait** — `/Users/melbourne/.agents/skills/avatar-portrait` — This skill should be used when the user asks to "create an avatar from a photo", "generate a portrait avatar", "make a profile image", "convert headshot to styled portrait", "team member avatar", "character-style avatar"

- **avoid-ai-writing** — `/Users/melbourne/.agents/skills/avoid-ai-writing` — Audit and rewrite content to remove 21 categories of AI writing patterns with a 43-entry replacement table

- **awareness-stage-mapper** — `/Users/melbourne/.agents/skills/awareness-stage-mapper` — One sentence - what this skill does and when to invoke it

- **aws-cost-cleanup** — `/Users/melbourne/.agents/skills/aws-cost-cleanup` — Automated cleanup of unused AWS resources to reduce costs

- **aws-cost-optimizer** — `/Users/melbourne/.agents/skills/aws-cost-optimizer` — Comprehensive AWS cost analysis and optimization recommendations using AWS CLI and Cost Explorer

- **aws-penetration-testing** — `/Users/melbourne/.agents/skills/aws-penetration-testing` — Provide comprehensive techniques for penetration testing AWS cloud environments. Covers IAM enumeration, privilege escalation, SSRF to metadata endpoint, S3 bucket exploitation, Lambda code extraction, and persistence te

- **aws-serverless** — `/Users/melbourne/.agents/skills/aws-serverless` — Specialized skill for building production-ready serverless

- **aws-skills** — `/Users/melbourne/.agents/skills/aws-skills` — AWS development with infrastructure automation and cloud architecture patterns

- **awt-e2e-testing** — `/Users/melbourne/.agents/skills/awt-e2e-testing` — AI-powered E2E web testing — eyes and hands for AI coding tools. Declarative YAML scenarios, Playwright execution, visual matching (OpenCV + OCR), platform auto-detection (Flutter/React/Vue), learning DB. Install: npx sk

- **ax-extract-workflow** — `/Users/melbourne/.agents/skills/ax-extract-workflow` — Reconstruct workflow behind a past coding-agent artifact using local ax sessions/commits/skills/tool traces. Use when asked how X was built.

- **axiom** — `/Users/melbourne/.agents/skills/axiom` — First-principles assumption auditor. Classifies each hidden assumption (fact / convention / belief / interest-driven), ranks by fragility × impact, and rebuilds conclusions from verified premises. Bilingual: auto-detects

- **azd-deployment** — `/Users/melbourne/.agents/skills/azd-deployment` — Deploy containerized frontend + backend applications to Azure Container Apps with remote builds, managed identity, and idempotent infrastructure.

- **azure-ai-agents-persistent-dotnet** — `/Users/melbourne/.agents/skills/azure-ai-agents-persistent-dotnet` — Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools.

- **azure-ai-agents-persistent-java** — `/Users/melbourne/.agents/skills/azure-ai-agents-persistent-java` — Azure AI Agents Persistent SDK for Java. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools.

- **azure-ai-anomalydetector-java** — `/Users/melbourne/.agents/skills/azure-ai-anomalydetector-java` — Build anomaly detection applications with Azure AI Anomaly Detector SDK for Java. Use when implementing univariate/multivariate anomaly detection, time-series analysis, or AI-powered monitoring.

- **azure-ai-contentsafety-java** — `/Users/melbourne/.agents/skills/azure-ai-contentsafety-java` — Build content moderation applications using the Azure AI Content Safety SDK for Java.

- **azure-ai-contentsafety-py** — `/Users/melbourne/.agents/skills/azure-ai-contentsafety-py` — Azure AI Content Safety SDK for Python. Use for detecting harmful content in text and images with multi-severity classification.

- **azure-ai-contentsafety-ts** — `/Users/melbourne/.agents/skills/azure-ai-contentsafety-ts` — Analyze text and images for harmful content with customizable blocklists.

- **azure-ai-contentunderstanding-py** — `/Users/melbourne/.agents/skills/azure-ai-contentunderstanding-py` — Azure AI Content Understanding SDK for Python. Use for multimodal content extraction from documents, images, audio, and video.

- **azure-ai-document-intelligence-dotnet** — `/Users/melbourne/.agents/skills/azure-ai-document-intelligence-dotnet` — Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using prebuilt and custom models.

- **azure-ai-document-intelligence-ts** — `/Users/melbourne/.agents/skills/azure-ai-document-intelligence-ts` — Extract text, tables, and structured data from documents using prebuilt and custom models.

- **azure-ai-formrecognizer-java** — `/Users/melbourne/.agents/skills/azure-ai-formrecognizer-java` — Build document analysis applications using the Azure AI Document Intelligence SDK for Java.

- **azure-ai-ml-py** — `/Users/melbourne/.agents/skills/azure-ai-ml-py` — Azure Machine Learning SDK v2 for Python. Use for ML workspaces, jobs, models, datasets, compute, and pipelines.

- **azure-ai-openai-dotnet** — `/Users/melbourne/.agents/skills/azure-ai-openai-dotnet` — Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, audio transcription, and assistants.

- **azure-ai-projects-dotnet** — `/Users/melbourne/.agents/skills/azure-ai-projects-dotnet` — Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections, datasets, deployments, evaluations, and indexes.

- **azure-ai-projects-java** — `/Users/melbourne/.agents/skills/azure-ai-projects-java` — Azure AI Projects SDK for Java. High-level SDK for Azure AI Foundry project management including connections, datasets, indexes, and evaluations.

- **azure-ai-projects-py** — `/Users/melbourne/.agents/skills/azure-ai-projects-py` — Build AI applications on Microsoft Foundry using the azure-ai-projects SDK.

- **azure-ai-projects-ts** — `/Users/melbourne/.agents/skills/azure-ai-projects-ts` — High-level SDK for Azure AI Foundry projects with agents, connections, deployments, and evaluations.

- **azure-ai-textanalytics-py** — `/Users/melbourne/.agents/skills/azure-ai-textanalytics-py` — Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. Use for natural language processing on text.

- **azure-ai-transcription-py** — `/Users/melbourne/.agents/skills/azure-ai-transcription-py` — Azure AI Transcription SDK for Python. Use for real-time and batch speech-to-text transcription with timestamps and diarization.

- **azure-ai-translation-document-py** — `/Users/melbourne/.agents/skills/azure-ai-translation-document-py` — Azure AI Document Translation SDK for batch translation of documents with format preservation. Use for translating Word, PDF, Excel, PowerPoint, and other document formats at scale.

- **azure-ai-translation-text-py** — `/Users/melbourne/.agents/skills/azure-ai-translation-text-py` — Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. Use for translating text content in applications.

- **azure-ai-translation-ts** — `/Users/melbourne/.agents/skills/azure-ai-translation-ts` — Text and document translation with REST-style clients.

- **azure-ai-vision-imageanalysis-java** — `/Users/melbourne/.agents/skills/azure-ai-vision-imageanalysis-java` — Build image analysis applications with Azure AI Vision SDK for Java. Use when implementing image captioning, OCR text extraction, object detection, tagging, or smart cropping.

- **azure-ai-vision-imageanalysis-py** — `/Users/melbourne/.agents/skills/azure-ai-vision-imageanalysis-py` — Azure AI Vision Image Analysis SDK for captions, tags, objects, OCR, people detection, and smart cropping. Use for computer vision and image understanding tasks.

- **azure-ai-voicelive-dotnet** — `/Users/melbourne/.agents/skills/azure-ai-voicelive-dotnet` — Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication.

- **azure-ai-voicelive-java** — `/Users/melbourne/.agents/skills/azure-ai-voicelive-java` — Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket.

- **azure-ai-voicelive-py** — `/Users/melbourne/.agents/skills/azure-ai-voicelive-py` — Build real-time voice AI applications with bidirectional WebSocket communication.

- **azure-ai-voicelive-ts** — `/Users/melbourne/.agents/skills/azure-ai-voicelive-ts` — Azure AI Voice Live SDK for JavaScript/TypeScript. Build real-time voice AI applications with bidirectional WebSocket communication.

- **azure-appconfiguration-java** — `/Users/melbourne/.agents/skills/azure-appconfiguration-java` — Azure App Configuration SDK for Java. Centralized application configuration management with key-value settings, feature flags, and snapshots.

- **azure-appconfiguration-py** — `/Users/melbourne/.agents/skills/azure-appconfiguration-py` — Azure App Configuration SDK for Python. Use for centralized configuration management, feature flags, and dynamic settings.

- **azure-appconfiguration-ts** — `/Users/melbourne/.agents/skills/azure-appconfiguration-ts` — Centralized configuration management with feature flags and dynamic refresh.

- **azure-communication-callautomation-java** — `/Users/melbourne/.agents/skills/azure-communication-callautomation-java` — Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions.

- **azure-communication-callingserver-java** — `/Users/melbourne/.agents/skills/azure-communication-callingserver-java` — ⚠️ DEPRECATED: This SDK has been renamed to Call Automation. For new projects, use azure-communication-callautomation instead. This skill is for maintaining legacy code only.

- **azure-communication-chat-java** — `/Users/melbourne/.agents/skills/azure-communication-chat-java` — Build real-time chat applications with thread management, messaging, participants, and read receipts.

- **azure-communication-common-java** — `/Users/melbourne/.agents/skills/azure-communication-common-java` — Azure Communication Services common utilities for Java. Use when working with CommunicationTokenCredential, user identifiers, token refresh, or shared authentication across ACS services.

- **azure-communication-sms-java** — `/Users/melbourne/.agents/skills/azure-communication-sms-java` — Send SMS messages with Azure Communication Services SMS Java SDK. Use when implementing SMS notifications, alerts, OTP delivery, bulk messaging, or delivery reports.

- **azure-compute-batch-java** — `/Users/melbourne/.agents/skills/azure-compute-batch-java` — Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes.

- **azure-containerregistry-py** — `/Users/melbourne/.agents/skills/azure-containerregistry-py` — Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories.

- **azure-cosmos-db-py** — `/Users/melbourne/.agents/skills/azure-cosmos-db-py` — Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles.

- **azure-cosmos-java** — `/Users/melbourne/.agents/skills/azure-cosmos-java` — Azure Cosmos DB SDK for Java. NoSQL database operations with global distribution, multi-model support, and reactive patterns.

- **azure-cosmos-py** — `/Users/melbourne/.agents/skills/azure-cosmos-py` — Azure Cosmos DB SDK for Python (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data.

- **azure-cosmos-rust** — `/Users/melbourne/.agents/skills/azure-cosmos-rust` — Azure Cosmos DB SDK for Rust (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data.

- **azure-cosmos-ts** — `/Users/melbourne/.agents/skills/azure-cosmos-ts` — Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. Use for CRUD operations on documents, queries, bulk operations, and container management.

- **azure-data-tables-java** — `/Users/melbourne/.agents/skills/azure-data-tables-java` — Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API.

- **azure-data-tables-py** — `/Users/melbourne/.agents/skills/azure-data-tables-py` — Azure Tables SDK for Python (Storage and Cosmos DB). Use for NoSQL key-value storage, entity CRUD, and batch operations.

- **azure-eventgrid-dotnet** — `/Users/melbourne/.agents/skills/azure-eventgrid-dotnet` — Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use for event-driven architectures, pub/sub messaging, CloudEvents, and EventGridEvents.

- **azure-eventgrid-java** — `/Users/melbourne/.agents/skills/azure-eventgrid-java` — Build event-driven applications with Azure Event Grid SDK for Java. Use when publishing events, implementing pub/sub patterns, or integrating with Azure services via events.

- **azure-eventgrid-py** — `/Users/melbourne/.agents/skills/azure-eventgrid-py` — Azure Event Grid SDK for Python. Use for publishing events, handling CloudEvents, and event-driven architectures.

- **azure-eventhub-dotnet** — `/Users/melbourne/.agents/skills/azure-eventhub-dotnet` — Azure Event Hubs SDK for .NET.

- **azure-eventhub-java** — `/Users/melbourne/.agents/skills/azure-eventhub-java` — Build real-time streaming applications with Azure Event Hubs SDK for Java. Use when implementing event streaming, high-throughput data ingestion, or building event-driven architectures.

- **azure-eventhub-py** — `/Users/melbourne/.agents/skills/azure-eventhub-py` — Azure Event Hubs SDK for Python streaming. Use for high-throughput event ingestion, producers, consumers, and checkpointing.

- **azure-eventhub-rust** — `/Users/melbourne/.agents/skills/azure-eventhub-rust` — Azure Event Hubs SDK for Rust. Use for sending and receiving events, streaming data ingestion.

- **azure-eventhub-ts** — `/Users/melbourne/.agents/skills/azure-eventhub-ts` — High-throughput event streaming and real-time data ingestion.

- **azure-functions** — `/Users/melbourne/.agents/skills/azure-functions` — Expert patterns for Azure Functions development including isolated

- **azure-identity-dotnet** — `/Users/melbourne/.agents/skills/azure-identity-dotnet` — Azure Identity SDK for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, managed identity, service principals, and developer credentials.

- **azure-identity-java** — `/Users/melbourne/.agents/skills/azure-identity-java` — Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD).

- **azure-identity-py** — `/Users/melbourne/.agents/skills/azure-identity-py` — Azure Identity SDK for Python authentication. Use for DefaultAzureCredential, managed identity, service principals, and token caching.

- **azure-identity-rust** — `/Users/melbourne/.agents/skills/azure-identity-rust` — Azure Identity SDK for Rust authentication. Use for DeveloperToolsCredential, ManagedIdentityCredential, ClientSecretCredential, and token-based authentication.

- **azure-identity-ts** — `/Users/melbourne/.agents/skills/azure-identity-ts` — Authenticate to Azure services with various credential types.

- **azure-keyvault-certificates-rust** — `/Users/melbourne/.agents/skills/azure-keyvault-certificates-rust` — Azure Key Vault Certificates SDK for Rust. Use for creating, importing, and managing certificates.

- **azure-keyvault-keys-rust** — `/Users/melbourne/.agents/skills/azure-keyvault-keys-rust` — Azure Key Vault Keys SDK for Rust. Use for creating, managing, and using cryptographic keys. Triggers: "keyvault keys rust", "KeyClient rust", "create key rust", "encrypt rust", "sign rust".

- **azure-keyvault-keys-ts** — `/Users/melbourne/.agents/skills/azure-keyvault-keys-ts` — Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). Use when creating, encrypting/decrypting, signing, or rotating keys.

- **azure-keyvault-py** — `/Users/melbourne/.agents/skills/azure-keyvault-py` — Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage.

- **azure-keyvault-secrets-rust** — `/Users/melbourne/.agents/skills/azure-keyvault-secrets-rust` — Azure Key Vault Secrets SDK for Rust. Use for storing and retrieving secrets, passwords, and API keys. Triggers: "keyvault secrets rust", "SecretClient rust", "get secret rust", "set secret rust".

- **azure-keyvault-secrets-ts** — `/Users/melbourne/.agents/skills/azure-keyvault-secrets-ts` — Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). Use when storing and retrieving application secrets or configuration values.

- **azure-maps-search-dotnet** — `/Users/melbourne/.agents/skills/azure-maps-search-dotnet` — Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address search, directions, map tiles, IP geolocation, and weather data.

- **azure-messaging-webpubsub-java** — `/Users/melbourne/.agents/skills/azure-messaging-webpubsub-java` — Build real-time web applications with Azure Web PubSub SDK for Java. Use when implementing WebSocket-based messaging, live updates, chat applications, or server-to-client push notifications.

- **azure-messaging-webpubsubservice-py** — `/Users/melbourne/.agents/skills/azure-messaging-webpubsubservice-py` — Azure Web PubSub Service SDK for Python. Use for real-time messaging, WebSocket connections, and pub/sub patterns.

- **azure-mgmt-apicenter-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-apicenter-dotnet` — Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery.

- **azure-mgmt-apicenter-py** — `/Users/melbourne/.agents/skills/azure-mgmt-apicenter-py` — Azure API Center Management SDK for Python. Use for managing API inventory, metadata, and governance across your organization.

- **azure-mgmt-apimanagement-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-apimanagement-dotnet` — Azure Resource Manager SDK for API Management in .NET.

- **azure-mgmt-apimanagement-py** — `/Users/melbourne/.agents/skills/azure-mgmt-apimanagement-py` — Azure API Management SDK for Python. Use for managing APIM services, APIs, products, subscriptions, and policies.

- **azure-mgmt-applicationinsights-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-applicationinsights-dotnet` — Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management.

- **azure-mgmt-arizeaiobservabilityeval-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-arizeaiobservabilityeval-dotnet` — Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET).

- **azure-mgmt-botservice-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-botservice-dotnet` — Azure Resource Manager SDK for Bot Service in .NET. Management plane operations for creating and managing Azure Bot resources, channels (Teams, DirectLine, Slack), and connection settings.

- **azure-mgmt-botservice-py** — `/Users/melbourne/.agents/skills/azure-mgmt-botservice-py` — Azure Bot Service Management SDK for Python. Use for creating, managing, and configuring Azure Bot Service resources.

- **azure-mgmt-fabric-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-fabric-dotnet` — Azure Resource Manager SDK for Fabric in .NET.

- **azure-mgmt-fabric-py** — `/Users/melbourne/.agents/skills/azure-mgmt-fabric-py` — Azure Fabric Management SDK for Python. Use for managing Microsoft Fabric capacities and resources.

- **azure-mgmt-mongodbatlas-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-mongodbatlas-dotnet` — Manage MongoDB Atlas Organizations as Azure ARM resources with unified billing through Azure Marketplace.

- **azure-mgmt-weightsandbiases-dotnet** — `/Users/melbourne/.agents/skills/azure-mgmt-weightsandbiases-dotnet` — Azure Weights & Biases SDK for .NET. ML experiment tracking and model management via Azure Marketplace. Use for creating W&B instances, managing SSO, marketplace integration, and ML observability.

- **azure-microsoft-playwright-testing-ts** — `/Users/melbourne/.agents/skills/azure-microsoft-playwright-testing-ts` — Run Playwright tests at scale with cloud-hosted browsers and integrated Azure portal reporting.

- **azure-monitor-ingestion-java** — `/Users/melbourne/.agents/skills/azure-monitor-ingestion-java` — Azure Monitor Ingestion SDK for Java. Send custom logs to Azure Monitor via Data Collection Rules (DCR) and Data Collection Endpoints (DCE).

- **azure-monitor-ingestion-py** — `/Users/melbourne/.agents/skills/azure-monitor-ingestion-py` — Azure Monitor Ingestion SDK for Python. Use for sending custom logs to Log Analytics workspace via Logs Ingestion API.

- **azure-monitor-opentelemetry-exporter-java** — `/Users/melbourne/.agents/skills/azure-monitor-opentelemetry-exporter-java` — Azure Monitor OpenTelemetry Exporter for Java. Export OpenTelemetry traces, metrics, and logs to Azure Monitor/Application Insights.

- **azure-monitor-opentelemetry-exporter-py** — `/Users/melbourne/.agents/skills/azure-monitor-opentelemetry-exporter-py` — Azure Monitor OpenTelemetry Exporter for Python. Use for low-level OpenTelemetry export to Application Insights.

- **azure-monitor-opentelemetry-py** — `/Users/melbourne/.agents/skills/azure-monitor-opentelemetry-py` — Azure Monitor OpenTelemetry Distro for Python. Use for one-line Application Insights setup with auto-instrumentation.

- **azure-monitor-opentelemetry-ts** — `/Users/melbourne/.agents/skills/azure-monitor-opentelemetry-ts` — Auto-instrument Node.js applications with distributed tracing, metrics, and logs.

- **azure-monitor-query-java** — `/Users/melbourne/.agents/skills/azure-monitor-query-java` — Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources.

- **azure-monitor-query-py** — `/Users/melbourne/.agents/skills/azure-monitor-query-py` — Azure Monitor Query SDK for Python. Use for querying Log Analytics workspaces and Azure Monitor metrics.

- **azure-postgres-ts** — `/Users/melbourne/.agents/skills/azure-postgres-ts` — Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package.

- **azure-resource-manager-cosmosdb-dotnet** — `/Users/melbourne/.agents/skills/azure-resource-manager-cosmosdb-dotnet` — Azure Resource Manager SDK for Cosmos DB in .NET.

- **azure-resource-manager-durabletask-dotnet** — `/Users/melbourne/.agents/skills/azure-resource-manager-durabletask-dotnet` — Azure Resource Manager SDK for Durable Task Scheduler in .NET.

- **azure-resource-manager-mysql-dotnet** — `/Users/melbourne/.agents/skills/azure-resource-manager-mysql-dotnet` — Azure MySQL Flexible Server SDK for .NET. Database management for MySQL Flexible Server deployments.

- **azure-resource-manager-playwright-dotnet** — `/Users/melbourne/.agents/skills/azure-resource-manager-playwright-dotnet` — Azure Resource Manager SDK for Microsoft Playwright Testing in .NET.

- **azure-resource-manager-postgresql-dotnet** — `/Users/melbourne/.agents/skills/azure-resource-manager-postgresql-dotnet` — Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments.

- **azure-resource-manager-redis-dotnet** — `/Users/melbourne/.agents/skills/azure-resource-manager-redis-dotnet` — Azure Resource Manager SDK for Redis in .NET.

- **azure-resource-manager-sql-dotnet** — `/Users/melbourne/.agents/skills/azure-resource-manager-sql-dotnet` — Azure Resource Manager SDK for Azure SQL in .NET.

- **azure-search-documents-dotnet** — `/Users/melbourne/.agents/skills/azure-search-documents-dotnet` — Azure AI Search SDK for .NET (Azure.Search.Documents). Use for building search applications with full-text, vector, semantic, and hybrid search.

- **azure-search-documents-py** — `/Users/melbourne/.agents/skills/azure-search-documents-py` — Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets.

- **azure-search-documents-ts** — `/Users/melbourne/.agents/skills/azure-search-documents-ts` — Build search applications with vector, hybrid, and semantic search capabilities.

- **azure-security-keyvault-keys-dotnet** — `/Users/melbourne/.agents/skills/azure-security-keyvault-keys-dotnet` — Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. Use for key creation, rotation, encryption, decryption, signing, and verification.

- **azure-security-keyvault-keys-java** — `/Users/melbourne/.agents/skills/azure-security-keyvault-keys-java` — Azure Key Vault Keys Java SDK for cryptographic key management. Use when creating, managing, or using RSA/EC keys, performing encrypt/decrypt/sign/verify operations, or working with HSM-backed keys.

- **azure-security-keyvault-secrets-java** — `/Users/melbourne/.agents/skills/azure-security-keyvault-secrets-java` — Azure Key Vault Secrets Java SDK for secret management. Use when storing, retrieving, or managing passwords, API keys, connection strings, or other sensitive configuration data.

- **azure-servicebus-dotnet** — `/Users/melbourne/.agents/skills/azure-servicebus-dotnet` — Azure Service Bus SDK for .NET. Enterprise messaging with queues, topics, subscriptions, and sessions.

- **azure-servicebus-py** — `/Users/melbourne/.agents/skills/azure-servicebus-py` — Azure Service Bus SDK for Python messaging. Use for queues, topics, subscriptions, and enterprise messaging patterns.

- **azure-servicebus-ts** — `/Users/melbourne/.agents/skills/azure-servicebus-ts` — Enterprise messaging with queues, topics, and subscriptions.

- **azure-speech-to-text-rest-py** — `/Users/melbourne/.agents/skills/azure-speech-to-text-rest-py` — Azure Speech to Text REST API for short audio (Python). Use for simple speech recognition of audio files up to 60 seconds without the Speech SDK.

- **azure-storage-blob-java** — `/Users/melbourne/.agents/skills/azure-storage-blob-java` — Build blob storage applications using the Azure Storage Blob SDK for Java.

- **azure-storage-blob-py** — `/Users/melbourne/.agents/skills/azure-storage-blob-py` — Azure Blob Storage SDK for Python. Use for uploading, downloading, listing blobs, managing containers, and blob lifecycle.

- **azure-storage-blob-rust** — `/Users/melbourne/.agents/skills/azure-storage-blob-rust` — Azure Blob Storage SDK for Rust. Use for uploading, downloading, and managing blobs and containers.

- **azure-storage-blob-ts** — `/Users/melbourne/.agents/skills/azure-storage-blob-ts` — Azure Blob Storage JavaScript/TypeScript SDK (@azure/storage-blob) for blob operations. Use for uploading, downloading, listing, and managing blobs and containers.

- **azure-storage-file-datalake-py** — `/Users/melbourne/.agents/skills/azure-storage-file-datalake-py` — Azure Data Lake Storage Gen2 SDK for Python. Use for hierarchical file systems, big data analytics, and file/directory operations.

- **azure-storage-file-share-py** — `/Users/melbourne/.agents/skills/azure-storage-file-share-py` — Azure Storage File Share SDK for Python. Use for SMB file shares, directories, and file operations in the cloud.

- **azure-storage-file-share-ts** — `/Users/melbourne/.agents/skills/azure-storage-file-share-ts` — Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations.

- **azure-storage-queue-py** — `/Users/melbourne/.agents/skills/azure-storage-queue-py` — Azure Queue Storage SDK for Python. Use for reliable message queuing, task distribution, and asynchronous processing.

- **azure-storage-queue-ts** — `/Users/melbourne/.agents/skills/azure-storage-queue-ts` — Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. Use for sending, receiving, peeking, and deleting messages in queues.

- **azure-web-pubsub-ts** — `/Users/melbourne/.agents/skills/azure-web-pubsub-ts` — Real-time messaging with WebSocket connections and pub/sub patterns.

- **backend-architect** — `/Users/melbourne/.agents/skills/backend-architect` — Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems.

- **backend-dev-guidelines** — `/Users/melbourne/.agents/skills/backend-dev-guidelines` — You are a senior backend engineer operating production-grade services under strict architectural and reliability constraints. Use when routes, controllers, services, repositories, express middleware, or prisma database a

- **backend-development-feature-development** — `/Users/melbourne/.agents/skills/backend-development-feature-development` — Orchestrate end-to-end backend feature development from requirements to deployment. Use when coordinating multi-phase feature delivery across teams and services.

- **backend-security-coder** — `/Users/melbourne/.agents/skills/backend-security-coder` — Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend security implementations or security code reviews.

- **background-removal** — `/Users/melbourne/.agents/skills/background-removal` — Remove backgrounds from images using each::sense AI. Create transparent PNGs, replace backgrounds with solid colors or scenes, and handle complex edges like hair with precision.

- **backtesting-frameworks** — `/Users/melbourne/.agents/skills/backtesting-frameworks` — Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates.

- **bamboohr-automation** — `/Users/melbourne/.agents/skills/bamboohr-automation` — Automate BambooHR tasks via Rube MCP (Composio): employees, time-off, benefits, dependents, employee updates. Always search tools first for current schemas.

- **baoyu-infographic** — `/Users/melbourne/.agents/skills/baoyu-infographic` — Generate professional infographics with 21 layout types and 22 visual styles. Analyzes content, recommends layout×style combinations, and generates publication-ready infographics. Use when user asks to create "infographi

- **basecamp-automation** — `/Users/melbourne/.agents/skills/basecamp-automation` — Automate Basecamp project management, to-dos, messages, people, and to-do list organization via Rube MCP (Composio). Always search tools first for current schemas.

- **baseline-ui** — `/Users/melbourne/.agents/skills/baseline-ui` — Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patterns in Tailwind CSS projects. Use when building UI components, reviewing CSS utilities, styling Reac

- **bash-defensive-patterns** — `/Users/melbourne/.agents/skills/bash-defensive-patterns` — Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance and safety.

- **bash-linux** — `/Users/melbourne/.agents/skills/bash-linux` — Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems.

- **bash-pro** — `/Users/melbourne/.agents/skills/bash-pro` — Master of defensive Bash scripting for production automation, CI/CD

- **bash-scripting** — `/Users/melbourne/.agents/skills/bash-scripting` — Bash scripting workflow for creating production-ready shell scripts with defensive patterns, error handling, and testing.

- **batch-visual-production** — `/Users/melbourne/.agents/skills/batch-visual-production` — Produce controlled image series and campaign variants by freezing invariants, varying explicit dimensions, naming outputs, tracking prompts, and preventing visual drift.

- **bats-testing-patterns** — `/Users/melbourne/.agents/skills/bats-testing-patterns` — Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipelines, or requiring test-driven development of shell utilities.

- **bazel-build-optimization** — `/Users/melbourne/.agents/skills/bazel-build-optimization` — Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performance for enterprise codebases.

- **bdi-mental-states** — `/Users/melbourne/.agents/skills/bdi-mental-states` — This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "build cognitive agent", or mentions BDI ont

- **bdistill-behavioral-xray** — `/Users/melbourne/.agents/skills/bdistill-behavioral-xray` — X-ray any AI model's behavioral patterns — refusal boundaries, hallucination tendencies, reasoning style, formatting defaults. No API key needed.

- **bdistill-knowledge-extraction** — `/Users/melbourne/.agents/skills/bdistill-knowledge-extraction` — Extract structured domain knowledge from AI models in-session or from local open-source models via Ollama. No API key needed.

- **beat-sync-editing** — `/Users/melbourne/.agents/skills/beat-sync-editing` — This skill should be used when the user asks to "cut to the beat", "fix the pacing", "edit this sequence", "sync cuts to music/BPM", "add a match cut / J-cut / L-cut", "build a speed ramp", or "plan a shot sequence / edi

- **beautiful-prose** — `/Users/melbourne/.agents/skills/beautiful-prose` — A hard-edged writing style contract for timeless, forceful English prose without modern AI tics. Use when users ask for prose or rewrites that must be clean, exact, concrete, and free of AI cadence, filler, or therapeuti

- **behavioral-modes** — `/Users/melbourne/.agents/skills/behavioral-modes` — AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type.

- **better-auth-best-practices** — `/Users/melbourne/.agents/skills/better-auth-best-practices` — Configure Better Auth server and client, set up database adapters, manage sessions, add plugins, and handle environment variables. Use when users mention Better Auth, betterauth, auth.ts, or need to set up TypeScript aut

- **bevy-ecs-expert** — `/Users/melbourne/.agents/skills/bevy-ecs-expert` — Master Bevy's Entity Component System (ECS) in Rust, covering Systems, Queries, Resources, and parallel scheduling.

- **bid-strategy-planner** — `/Users/melbourne/.agents/skills/bid-strategy-planner` — Use when the user asks to "pick a bid strategy", "set a tCPA/tROAS target", or "plan the learning-phase entry"; produces a bid-strategy choice (tCPA / tROAS / max-conversions / manual CPC), the starting target math, a po

- **bilig-workpaper** — `/Users/melbourne/.agents/skills/bilig-workpaper` — Use formula-backed WorkPaper JSON and MCP tools for agent spreadsheet tasks without driving Excel or a browser UI.

- **bill-gates** — `/Users/melbourne/.agents/skills/bill-gates` — Agente que simula Bill Gates — cofundador da Microsoft, arquiteto da industria de software comercial, estrategista tecnologico global, investidor sistemico e filantropo baseado em dados.

- **billing-automation** — `/Users/melbourne/.agents/skills/billing-automation` — Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation.

- **binary-analysis-patterns** — `/Users/melbourne/.agents/skills/binary-analysis-patterns` — Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic.

- **biopython** — `/Users/melbourne/.agents/skills/biopython` — Biopython is a comprehensive set of freely available Python tools for biological computation. It provides functionality for sequence manipulation, file I/O, database access, structural bioinformatics, phylogenetics, and 

- **bitbucket-automation** — `/Users/melbourne/.agents/skills/bitbucket-automation` — Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). Always search tools first for current schemas.

- **blockchain-developer** — `/Users/melbourne/.agents/skills/blockchain-developer` — Build production-ready Web3 applications, smart contracts, and decentralized systems. Implements DeFi protocols, NFT platforms, DAOs, and enterprise blockchain integrations.

- **blockrun** — `/Users/melbourne/.agents/skills/blockrun` — BlockRun works with Claude Code and Google Antigravity.

- **blog-writing-guide** — `/Users/melbourne/.agents/skills/blog-writing-guide` — This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post or a marketer draft a product announcement.

- **blueprint** — `/Users/melbourne/.agents/skills/blueprint` — Turn a one-line objective into a step-by-step construction plan any coding agent can execute cold. Each step has a self-contained context brief — a fresh agent in a new session can pick up any step without reading prior 

- **book-cover-generation** — `/Users/melbourne/.agents/skills/book-cover-generation` — Generate professional book covers and ebook covers using each::sense API with AI-powered design

- **box-automation** — `/Users/melbourne/.agents/skills/box-automation` — Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit.

- **brainstorming** — `/Users/melbourne/.agents/skills/brainstorming` — Use before creative or constructive work (features, architecture, behavior). Transforms vague ideas into validated designs through disciplined reasoning and collaboration.

- **brand-designer** — `/Users/melbourne/.agents/skills/brand-designer` — Expert in brand identity, logo design, and visual brand systems

- **brand-guidelines** — `/Users/melbourne/.agents/skills/brand-guidelines` — Write copy following Sentry brand guidelines. Use when writing UI text, error messages, empty states, onboarding flows, 404 pages, documentation, marketing copy, or any user-facing content. Covers both Plain Speech (defa

- **brand-guidelines-anthropic** — `/Users/melbourne/.agents/skills/brand-guidelines-anthropic` — To access Anthropic's official brand identity and style resources, use this skill.

- **brand-guidelines-community** — `/Users/melbourne/.agents/skills/brand-guidelines-community` — To access Anthropic's official brand identity and style resources, use this skill.

- **brand-language-codifier** — `/Users/melbourne/.agents/skills/brand-language-codifier` — Use when the user asks to "codify our brand voice", "define naming rules for our products and tiers", or "write the tone-of-voice guide with banned phrases"; produces the brand-level voice canon (register, tone spectrum,

- **brand-motion-guidelines** — `/Users/melbourne/.agents/skills/brand-motion-guidelines` — This skill should be used when the user asks to "write motion guidelines", "create a brand motion system", "define easing and timing tokens", "document our animation principles", "build a motion language like Slack/IBM/K

- **brand-perception-psychologist** — `/Users/melbourne/.agents/skills/brand-perception-psychologist` — One sentence - what this skill does and when to invoke it

- **brand-review** — `/Users/melbourne/.agents/skills/brand-review` — Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. Use when checking a draft before it ships, when auditing copy for voice consi

- **brand-storytelling** — `/Users/melbourne/.agents/skills/brand-storytelling` — Help users craft compelling brand narratives. Use when someone is defining brand strategy, writing company positioning, creating pitch narratives, developing messaging frameworks, or trying to make their company story mo

- **brand-visual-language** — `/Users/melbourne/.agents/skills/brand-visual-language` — A brand's visual tone — playful or serious, rounded or angular — should be consistent across all UI elements. Shape language in typography, border-radius, and iconography communicates personality before a single word is 

- **brand-voice-enforcement** — `/Users/melbourne/.agents/skills/brand-voice-enforcement` — >

- **brave-man** — `/Users/melbourne/.agents/skills/brave-man` — Runs a structured clarifying interview for new project requests before building. Instead of writing code, it outputs a fully specified prompt.md for a fresh agent session to execute, preventing expensive mistakes.

- **brevo-automation** — `/Users/melbourne/.agents/skills/brevo-automation` — Automate Brevo (formerly Sendinblue) email marketing operations through Composio's Brevo toolkit via Rube MCP.

- **brief-generator** — `/Users/melbourne/.agents/skills/brief-generator` — Use when the user asks to "create an influencer brief" or "write a campaign brief"; produces a structured creator brief with deliverables, key messages, creative direction, timeline, disclosure rules, and compensation te

- **brochure-design-generation** — `/Users/melbourne/.agents/skills/brochure-design-generation` — Generate professional brochure designs using each::sense AI. Create tri-fold, bi-fold, corporate, travel, product, real estate, healthcare, educational, event, and service brochures with print-ready layouts.

- **broken-authentication** — `/Users/melbourne/.agents/skills/broken-authentication` — Identify and exploit authentication and session management vulnerabilities in web applications. Broken authentication consistently ranks in the OWASP Top 10 and can lead to account takeover, identity theft, and unauthori

- **brooks-lint** — `/Users/melbourne/.agents/skills/brooks-lint` — AI code reviewer grounded in classic software engineering books for catching design smells, coupling issues, and architectural risks.

- **browser-automation** — `/Users/melbourne/.agents/skills/browser-automation` — Browser automation powers web testing, scraping, and AI agent

- **browser-extension-builder** — `/Users/melbourne/.agents/skills/browser-extension-builder` — Expert in building browser extensions that solve real problems -

- **browsing-styles** — `/Users/melbourne/.agents/skills/browsing-styles` — This skill should be used when the user asks to "browse art styles", "pick a style", "choose a style", "select a style", "list available styles", "search styles", "show style options", "what styles are available", "explo

- **budget-finance** — `/Users/melbourne/.agents/skills/budget-finance` — Build and review operating budgets, forecasts, spending plans, variances, cash views, cost scenarios, unit economics, and financially informed decisions.

- **budget-optimizer** — `/Users/melbourne/.agents/skills/budget-optimizer` — Use when the user asks to "allocate my influencer budget", "optimize spend across tiers", or "compare budget scenarios"; produces a tier/platform/content allocation table, ROI and CPM/CPE projections, scenario comparison

- **budget-pacing-monitor** — `/Users/melbourne/.agents/skills/budget-pacing-monitor` — Use when the user asks to "check pacing", "am I over/under-spending", "is this campaign on track to hit budget", or "why did spend spike/stall mid-flight"; returns a spend-vs-target-curve read, learning-phase status, an 

- **bug-hunter** — `/Users/melbourne/.agents/skills/bug-hunter` — Systematically finds and fixes bugs using proven debugging techniques. Traces from symptoms to root cause, implements fixes, and prevents regression.

- **bugs-are-annoying** — `/Users/melbourne/.agents/skills/bugs-are-annoying` — Adversarial code auditor that hunts down bugs, logic errors, and security flaws. Use for deep correctness passes, not style reviews.

- **build** — `/Users/melbourne/.agents/skills/build` — build

- **build-dashboard** — `/Users/melbourne/.agents/skills/build-dashboard` — Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snaps

- **building-native-ui** — `/Users/melbourne/.agents/skills/building-native-ui` — Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs.

- **bulletmind** — `/Users/melbourne/.agents/skills/bulletmind` — Convert input into clean, structured, hierarchical bullet points for summarization, note-taking, and structured thinking.

- **bullmq-specialist** — `/Users/melbourne/.agents/skills/bullmq-specialist` — BullMQ expert for Redis-backed job queues, background processing,

- **bumblebee** — `/Users/melbourne/.agents/skills/bumblebee` — Run Bumblebee supply-chain inventory and exposure scans on macOS/Linux to detect compromised packages, extensions, and MCP host configs.

- **bun-development** — `/Users/melbourne/.agents/skills/bun-development` — Fast, modern JavaScript/TypeScript development with the Bun runtime, inspired by [oven-sh/bun](https://github.com/oven-sh/bun).

- **burp-suite-testing** — `/Users/melbourne/.agents/skills/burp-suite-testing` — Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, automated vulnerability scanning, and manua

- **burpsuite-project-parser** — `/Users/melbourne/.agents/skills/burpsuite-project-parser` — Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data,

- **business-analyst** — `/Users/melbourne/.agents/skills/business-analyst` — Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI frameworks, predictive models, and strategic recommendations.

- **business-card-generation** — `/Users/melbourne/.agents/skills/business-card-generation` — Generate professional business cards using each::sense AI. Create corporate, creative, minimalist, luxury, and specialty business cards optimized for print at standard 3.5 x 2 inch size.

- **business-document-generator** — `/Users/melbourne/.agents/skills/business-document-generator` — This skill should be used when the user requests to create professional business documents (proposals, business plans, or budgets) from templates. It provides PDF templates and a Python script for generating filled docum

- **busybox-on-windows** — `/Users/melbourne/.agents/skills/busybox-on-windows` — How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows.

- **buywhere-product-catalog** — `/Users/melbourne/.agents/skills/buywhere-product-catalog` — Use BuyWhere's MCP and API surfaces to add product search, price comparison, and deal discovery to AI shopping agents.

- **bytedance-seedance-2-0** — `/Users/melbourne/.agents/skills/bytedance-seedance-2-0` — Generate cinematic videos with native synchronized audio using ByteDance Seedance 2.0 (Fast) via EachLabs. Supports text-to-video (bytedance-seedance-2-0-text-to-video-fast) and image-to-video (bytedance-seedance-2-0-ima

- **c-pro** — `/Users/melbourne/.agents/skills/c-pro` — Write efficient C code with proper memory management, pointer

- **c4-architecture-c4-architecture** — `/Users/melbourne/.agents/skills/c4-architecture-c4-architecture` — Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach.

- **c4-code** — `/Users/melbourne/.agents/skills/c4-code` — Expert C4 Code-level documentation specialist. Analyzes code directories to create comprehensive C4 code-level documentation including function signatures, arguments, dependencies, and code structure.

- **c4-component** — `/Users/melbourne/.agents/skills/c4-component` — Expert C4 Component-level documentation specialist. Synthesizes C4 Code-level documentation into Component-level architecture, defining component boundaries, interfaces, and relationships.

- **c4-container** — `/Users/melbourne/.agents/skills/c4-container` — Expert C4 Container-level documentation specialist.

- **c4-context** — `/Users/melbourne/.agents/skills/c4-context` — Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system features, and external dependencies.

- **cal-com-automation** — `/Users/melbourne/.agents/skills/cal-com-automation` — Automate Cal.com tasks via Rube MCP (Composio): manage bookings, check availability, configure webhooks, and handle teams. Always search tools first for current schemas.

- **calendly-automation** — `/Users/melbourne/.agents/skills/calendly-automation` — Automate Calendly scheduling, event management, invitee tracking, availability checks, and organization administration via Rube MCP (Composio). Always search tools first for current schemas.

- **campaign-architect** — `/Users/melbourne/.agents/skills/campaign-architect` — Use when the user asks to "plan my paid account structure", "pick Search vs PMax", "lay out ad groups / asset groups", or "audit paid-vs-organic cannibalization"; designs campaign-type selection, ad-group/asset-group lay

- **campaign-planner** — `/Users/melbourne/.agents/skills/campaign-planner` — Use when the user asks to "plan an influencer campaign", "build a campaign blueprint", "track or close a creator campaign", or "record a late campaign correction"; produces the plan and, when requested, a non-canonical e

- **canva-automation** — `/Users/melbourne/.agents/skills/canva-automation` — Automate Canva tasks via Rube MCP (Composio): designs, exports, folders, brand templates, autofill. Always search tools first for current schemas.

- **canvas-design** — `/Users/melbourne/.agents/skills/canvas-design` — These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. Output only .md files, .pdf files, and .png files.

- **carrier-relationship-management** — `/Users/melbourne/.agents/skills/carrier-relationship-management` — Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating freight, and maintaining strategic carrier relationships.

- **category-narrative-mapper** — `/Users/melbourne/.agents/skills/category-narrative-mapper` — Use when the user asks to "map the category narrative", "tear down how competitors tell their story", or "find the language conventions in our market"; produces a category narrative map — the dominant stories and points 

- **caveman** — `/Users/melbourne/.agents/skills/caveman` — >

- **cc-skill-backend-patterns** — `/Users/melbourne/.agents/skills/cc-skill-backend-patterns` — Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes.

- **cc-skill-clickhouse-io** — `/Users/melbourne/.agents/skills/cc-skill-clickhouse-io` — ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads.

- **cc-skill-coding-standards** — `/Users/melbourne/.agents/skills/cc-skill-coding-standards` — Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development.

- **cc-skill-continuous-learning** — `/Users/melbourne/.agents/skills/cc-skill-continuous-learning` — Development skill from everything-claude-code

- **cc-skill-frontend-patterns** — `/Users/melbourne/.agents/skills/cc-skill-frontend-patterns` — Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices.

- **cc-skill-project-guidelines-example** — `/Users/melbourne/.agents/skills/cc-skill-project-guidelines-example` — Project Guidelines Skill (Example)

- **cc-skill-security-review** — `/Users/melbourne/.agents/skills/cc-skill-security-review` — This skill ensures all code follows security best practices and identifies potential vulnerabilities. Use when implementing authentication or authorization, handling user input or file uploads, or creating new API endpoi

- **cc-skill-strategic-compact** — `/Users/melbourne/.agents/skills/cc-skill-strategic-compact` — Development skill from everything-claude-code

- **cdk-patterns** — `/Users/melbourne/.agents/skills/cdk-patterns` — Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. Use when designing reusable CDK stacks and L3 constructs.

- **certificate-generation** — `/Users/melbourne/.agents/skills/certificate-generation` — Generate professional certificates, diplomas, and awards using each::sense AI. Create course completion certificates, achievement awards, professional certifications, academic diplomas, and custom branded certificates.

- **change-management** — `/Users/melbourne/.agents/skills/change-management` — Plan organizational change through impact analysis, readiness, sponsorship, communication, training, adoption measures, resistance handling, and reinforcement.

- **changelog-automation** — `/Users/melbourne/.agents/skills/changelog-automation` — Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, generating release notes, or standardizing commit conventions.

- **channel-portfolio-planner** — `/Users/melbourne/.agents/skills/channel-portfolio-planner` — Use when the user asks to "pick which social channels to run", "should we be on X platform or 小红书", or "plan our organic social channel portfolio"; produces an audience/objective-first portfolio with capability/access ma

- **channel-registry** — `/Users/melbourne/.agents/skills/channel-registry` — Use when the user asks to register/query a social channel, record channel state, cadence, governance, voice adaptation, UGC permission, or advocacy facts; curates them through the append-only channels event stream and de

- **chat-widget** — `/Users/melbourne/.agents/skills/chat-widget` — Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. Use when the user wants live chat, customer support chat, real-time messaging, or in-app support.

- **chrome-extension** — `/Users/melbourne/.agents/skills/chrome-extension` — Build Chrome extensions with Manifest V3. Use this skill whenever the user mentions Chrome extension, browser extension, manifest.json, content script, service worker (in extension context), popup, side panel, chrome.run

- **chrome-extension-developer** — `/Users/melbourne/.agents/skills/chrome-extension-developer` — Expert in building Chrome Extensions using Manifest V3. Covers background scripts, service workers, content scripts, and cross-context communication.

- **churn-prevention** — `/Users/melbourne/.agents/skills/churn-prevention` — When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies. Also use when the user mentions 'churn,' 'cancel flow,' 'offboarding,' 'save 

- **cicd-automation-workflow-automate** — `/Users/melbourne/.agents/skills/cicd-automation-workflow-automate` — You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. Design and implement automation that reduces manual work, improves c

- **circleci-automation** — `/Users/melbourne/.agents/skills/circleci-automation` — Automate CircleCI tasks via Rube MCP (Composio): trigger pipelines, monitor workflows/jobs, retrieve artifacts and test metadata. Always search tools first for current schemas.

- **cirq** — `/Users/melbourne/.agents/skills/cirq` — Cirq is Google Quantum AI's open-source framework for designing, simulating, and running quantum circuits on quantum computers and simulators.

- **citation-management** — `/Users/melbourne/.agents/skills/citation-management` — Manage citations systematically throughout the research and writing process.

- **ckw-design** — `/Users/melbourne/.agents/skills/ckw-design` — Frontend design entry point: direction, design system, visual philosophy. Use whenever building or touching the look of any web UI (components, pages, dashboards, React/Vue/HTML-CSS) or when the user says \"make this loo

- **claimable-postgres** — `/Users/melbourne/.agents/skills/claimable-postgres` — Provision instant temporary Postgres databases via Claimable Postgres by Neon (pg.new). No login or credit card required. Use for quick Postgres environments and throwaway DATABASE_URL for prototyping.

- **clarity-gate** — `/Users/melbourne/.agents/skills/clarity-gate` — >

- **clarvia-aeo-check** — `/Users/melbourne/.agents/skills/clarvia-aeo-check` — Score any MCP server, API, or CLI for agent-readiness using Clarvia AEO (Agent Experience Optimization). Search 15,400+ indexed tools before adding them to your workflow.

- **claude-ally-health** — `/Users/melbourne/.agents/skills/claude-ally-health` — A health assistant skill for medical information analysis, symptom tracking, and wellness guidance.

- **claude-api** — `/Users/melbourne/.agents/skills/claude-api` — Build apps with the Claude API or Anthropic SDK. TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`/`claude_agent_sdk`, or user asks to use Claude API, Anthropic SDKs, or Agent SDK. DO NOT TRIGGER when: code impo

- **claude-code-expert** — `/Users/melbourne/.agents/skills/claude-code-expert` — Especialista profundo em Claude Code - CLI da Anthropic. Maximiza produtividade com atalhos, hooks, MCPs, configuracoes avancadas, workflows, CLAUDE.md, memoria, sub-agentes, permissoes e integracao com ecossistemas.

- **claude-code-guide** — `/Users/melbourne/.agents/skills/claude-code-guide` — To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. This skill synthesizes best practices, configuration templates, and advanced usage patterns.

- **claude-d3js-skill** — `/Users/melbourne/.agents/skills/claude-d3js-skill` — This skill provides guidance for creating sophisticated, interactive data visualisations using d3.js.

- **claude-in-chrome-troubleshooting** — `/Users/melbourne/.agents/skills/claude-in-chrome-troubleshooting` — Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

- **claude-monitor** — `/Users/melbourne/.agents/skills/claude-monitor` — Monitor de performance do Claude Code e sistema local. Diagnostica lentidao, mede CPU/RAM/disco, verifica API latency e gera relatorios de saude do sistema.

- **claude-scientific-skills** — `/Users/melbourne/.agents/skills/claude-scientific-skills` — Scientific research and analysis skills

- **claude-settings-audit** — `/Users/melbourne/.agents/skills/claude-settings-audit` — Analyze a repository to generate recommended Claude Code settings.json permissions. Use when setting up a new project, auditing existing settings, or determining which read-only bash commands to allow. Detects tech stack

- **claude-speed-reader** — `/Users/melbourne/.agents/skills/claude-speed-reader` — -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting

- **claude-win11-speckit-update-skill** — `/Users/melbourne/.agents/skills/claude-win11-speckit-update-skill` — Windows 11 system management

- **clean-code** — `/Users/melbourne/.agents/skills/clean-code` — This skill embodies the principles of \"Clean Code\" by Robert C. Martin (Uncle Bob). Use it to transform \"code that works\" into \"code that is clean.\"

- **clerk-auth** — `/Users/melbourne/.agents/skills/clerk-auth` — Expert patterns for Clerk auth implementation, middleware,

- **clickup-automation** — `/Users/melbourne/.agents/skills/clickup-automation` — Automate ClickUp project management including tasks, spaces, folders, lists, comments, and team operations via Rube MCP (Composio). Always search tools first for current schemas.

- **client-revisions** — `/Users/melbourne/.agents/skills/client-revisions` — This skill should be used when the user asks to "stop scope creep", "limit revision rounds", "write SOW revision language", "the client keeps asking for changes", "how do I say this is out of scope", "translate vague fee

- **close-automation** — `/Users/melbourne/.agents/skills/close-automation` — Automate Close CRM tasks via Rube MCP (Composio): create leads, manage calls/SMS, handle tasks, and track notes. Always search tools first for current schemas.

- **closed-loop-delivery** — `/Users/melbourne/.agents/skills/closed-loop-delivery` — Use when a coding task must be completed against explicit acceptance criteria with minimal user re-intervention across implementation, review feedback, deployment, and runtime verification.

- **cloud-architect** — `/Users/melbourne/.agents/skills/cloud-architect` — Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns.

- **cloud-devops** — `/Users/melbourne/.agents/skills/cloud-devops` — Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development.

- **cloud-penetration-testing** — `/Users/melbourne/.agents/skills/cloud-penetration-testing` — Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP).

- **cloudflare-workers-expert** — `/Users/melbourne/.agents/skills/cloudflare-workers-expert` — Expert in Cloudflare Workers and the Edge Computing ecosystem. Covers Wrangler, KV, D1, Durable Objects, and R2 storage.

- **cloudformation-best-practices** — `/Users/melbourne/.agents/skills/cloudformation-best-practices` — CloudFormation template optimization, nested stacks, drift detection, and production-ready patterns. Use when writing or reviewing CF templates.

- **co-marketing** — `/Users/melbourne/.agents/skills/co-marketing` — When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. Use when the user says 'co-marketing,' 'partner marketing,' 'joint campaign,' 'who should we partner with,

- **coda-automation** — `/Users/melbourne/.agents/skills/coda-automation` — Automate Coda tasks via Rube MCP (Composio): manage docs, pages, tables, rows, formulas, permissions, and publishing. Always search tools first for current schemas.

- **code-documentation-code-explain** — `/Users/melbourne/.agents/skills/code-documentation-code-explain` — You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into understandable explanations for developers

- **code-documentation-doc-generate** — `/Users/melbourne/.agents/skills/code-documentation-doc-generate` — You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and i

- **code-refactoring-context-restore** — `/Users/melbourne/.agents/skills/code-refactoring-context-restore` — Use when working with code refactoring context restore

- **code-refactoring-refactor-clean** — `/Users/melbourne/.agents/skills/code-refactoring-refactor-clean` — You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided code to improve its quality, maintainabili

- **code-refactoring-tech-debt** — `/Users/melbourne/.agents/skills/code-refactoring-tech-debt` — You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its impact, and create acti

- **code-review-ai-ai-review** — `/Users/melbourne/.agents/skills/code-review-ai-ai-review` — You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub Copilot, Qodo, GPT-5, C

- **code-review-checklist** — `/Users/melbourne/.agents/skills/code-review-checklist` — Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability

- **code-review-excellence** — `/Users/melbourne/.agents/skills/code-review-excellence` — Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement.

- **code-reviewer** — `/Users/melbourne/.agents/skills/code-reviewer` — Elite code review expert specializing in modern AI-powered code

- **code-simplifier** — `/Users/melbourne/.agents/skills/code-simplifier` — Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Use when asked to "simplify code", "clean up code", "refactor for clarity", "improve readability", or review r

- **codebase-audit-pre-push** — `/Users/melbourne/.agents/skills/codebase-audit-pre-push` — Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues. Checks every file line-by-line for production readiness.

- **codebase-cleanup-deps-audit** — `/Users/melbourne/.agents/skills/codebase-cleanup-deps-audit` — You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilities, licensing issues, outdated packages, and

- **codebase-cleanup-refactor-clean** — `/Users/melbourne/.agents/skills/codebase-cleanup-refactor-clean` — You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided code to improve its quality, maintainabili

- **codebase-cleanup-tech-debt** — `/Users/melbourne/.agents/skills/codebase-cleanup-tech-debt` — You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its impact, and create acti

- **codebase-design** — `/Users/melbourne/.agents/skills/codebase-design` — Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when an

- **codebase-to-wordpress-converter** — `/Users/melbourne/.agents/skills/codebase-to-wordpress-converter` — Expert skill for converting any codebase (React/HTML/Next.js) into a pixel-perfect, SEO-optimized, and dynamic WordPress theme.

- **codex-agent-setup** — `/Users/melbourne/.agents/skills/codex-agent-setup` — >-

- **codex-fable5** — `/Users/melbourne/.agents/skills/codex-fable5` — Apply Fable-inspired discipline to Codex work: inspect first, track goals and findings, ground conclusions in evidence, verify before completion, and adapt Claude/Fable prompt guidance without identity or provider claims

- **codex-review** — `/Users/melbourne/.agents/skills/codex-review` — Professional code review with auto CHANGELOG generation, integrated with Codex AI. Use when you want professional code review before commits, you need automatic CHANGELOG generation, or reviewing large-scale refactoring.

- **cold-email** — `/Users/melbourne/.agents/skills/cold-email` — Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails, cold email campaigns, sales development emails, or SDR emails. Also use when the 

- **cold-outbound-sequencer** — `/Users/melbourne/.agents/skills/cold-outbound-sequencer` — Use when the user asks to "build a B2B cold-outbound sequence", "design reply-triage branching", "plan a domain warmup / sending throttle", or "make my outbound CAN-SPAM / opt-in compliant"; produces a multi-step outboun

- **color-motion** — `/Users/melbourne/.agents/skills/color-motion` — This skill should be used when the user asks to "build a color palette for a motion piece", "make a gradient background", "animate a color transition", "interpolate colors smoothly", "fix muddy/gray gradients", "convert 

- **comfyui-gateway** — `/Users/melbourne/.agents/skills/comfyui-gateway` — REST API gateway for ComfyUI servers. Workflow management, job queuing, webhooks, caching, auth, rate limiting, and image delivery (URL + base64).

- **comic-panel-generation** — `/Users/melbourne/.agents/skills/comic-panel-generation` — Generate comic and manga panels, strips, and pages using each::sense AI. Create superhero comics, manga pages, webtoons, action sequences, and convert photos to comic art with consistent characters.

- **commercial-product-visuals** — `/Users/melbourne/.agents/skills/commercial-product-visuals` — Create commercial product imagery, packshots, hero shots, lifestyle scenes, catalog visuals, ads, and product compositions with geometry and branding controls.

- **commit** — `/Users/melbourne/.agents/skills/commit` — ALWAYS use this skill when committing code changes — never commit directly without it. Creates commits following Sentry conventions with proper conventional commit format and issue references. Trigger on any commit, git 

- **community-launch-runner** — `/Users/melbourne/.agents/skills/community-launch-runner` — Use when the user asks to "launch on Product Hunt / Hacker News", "prepare community or directory launch submissions", or "plan the launch submission waves"; produces per-platform submission packages — a Product Hunt tag

- **community-marketing** — `/Users/melbourne/.agents/skills/community-marketing` — Build and leverage online communities to drive product growth and brand loyalty. Use when the user wants to create a community strategy, grow a Discord or Slack community, manage a forum or subreddit, build brand advocat

- **competitive-landscape** — `/Users/melbourne/.agents/skills/competitive-landscape` — Comprehensive frameworks for analyzing competition, identifying differentiation opportunities, and developing winning market positioning strategies.

- **competitor-alternatives** — `/Users/melbourne/.agents/skills/competitor-alternatives` — You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluators, and position your product effectively.

- **competitor-analysis** — `/Users/melbourne/.agents/skills/competitor-analysis` — Use when the user asks to "analyze competitors" or "竞品分析"; benchmarks competitor keywords, content, backlinks, AI citations, and traffic share into strengths, weaknesses, and an action plan. Not for a pairwise topic-cove

- **competitor-profiling** — `/Users/melbourne/.agents/skills/competitor-profiling` — When the user wants to research, profile, or analyze competitors from their URLs. Also use when the user mentions 'competitor profile,' 'competitor research,' 'competitor analysis,' 'profile this competitor,' 'analyze co

- **competitor-tracker** — `/Users/melbourne/.agents/skills/competitor-tracker` — Use when the user asks to "track competitor influencer marketing", "see who my rivals partner with", or "benchmark my influencer program"; produces a competitor partnership roster, campaign and content-strategy breakdown

- **competitors** — `/Users/melbourne/.agents/skills/competitors` — When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alternative page,' 'vs page,' 'competitor comparison,' 'comparison page,' '[Product]

- **complexity-cuts** — `/Users/melbourne/.agents/skills/complexity-cuts` — Lower Big-O on existing code via a one-transformation-at-a-time playbook with verify-revert-stop. For new code use lemmaly; for math-level wins escalate to mathguard.

- **composio-cli** — `/Users/melbourne/.agents/skills/composio-cli` — Help users operate the published Composio CLI to find the right tool, connect accounts, inspect schemas, execute tools, subscribe to trigger events with `composio listen`, script workflows with `composio run`, and call a

- **composition-patterns** — `/Users/melbourne/.agents/skills/composition-patterns` — Use when working with composition-patterns tasks or workflows

- **comprehensive-review-full-review** — `/Users/melbourne/.agents/skills/comprehensive-review-full-review` — Use when working with comprehensive review full review

- **comprehensive-review-pr-enhance** — `/Users/melbourne/.agents/skills/comprehensive-review-pr-enhance` — >

- **computer-use-agents** — `/Users/melbourne/.agents/skills/computer-use-agents` — Build AI agents that interact with computers like humans do -

- **computer-vision-expert** — `/Users/melbourne/.agents/skills/computer-vision-expert` — SOTA Computer Vision Expert (2026). Specialized in YOLO26, Segment Anything 3 (SAM 3), Vision Language Models, and real-time spatial analysis.

- **concise-planning** — `/Users/melbourne/.agents/skills/concise-planning` — Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist.

- **conductor-implement** — `/Users/melbourne/.agents/skills/conductor-implement` — Execute tasks from a track's implementation plan following TDD workflow

- **conductor-manage** — `/Users/melbourne/.agents/skills/conductor-manage` — Manage track lifecycle: archive, restore, delete, rename, and cleanup

- **conductor-new-track** — `/Users/melbourne/.agents/skills/conductor-new-track` — Create a new track with specification and phased implementation plan

- **conductor-revert** — `/Users/melbourne/.agents/skills/conductor-revert` — Git-aware undo by logical work unit (track, phase, or task)

- **conductor-setup** — `/Users/melbourne/.agents/skills/conductor-setup` — Configure a Rails project to work with Conductor (parallel coding agents)

- **conductor-status** — `/Users/melbourne/.agents/skills/conductor-status` — Display project status, active tracks, and next actions

- **conductor-validator** — `/Users/melbourne/.agents/skills/conductor-validator` — Validates Conductor project artifacts for completeness,

- **confluence-automation** — `/Users/melbourne/.agents/skills/confluence-automation` — Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio). Always search tools first for current schemas.

- **consent-registry** — `/Users/melbourne/.agents/skills/consent-registry` — Use when the user asks to "log this subscriber''s opt-in", record unsubscribes/complaints, or query lawful basis; curates pseudonymous consent facts through the append-only consent stream and applies suppression/erasure 

- **constant-time-analysis** — `/Users/melbourne/.agents/skills/constant-time-analysis` — Analyze cryptographic code to detect operations that leak secret data through execution timing variations.

- **container-security-hardening** — `/Users/melbourne/.agents/skills/container-security-hardening` — >

- **content-amplifier** — `/Users/melbourne/.agents/skills/content-amplifier` — Use when the user asks to "amplify influencer content with paid media", "set up whitelisting or Spark Ads", "decide which posts to boost", "repurpose influencer content", "turn one video into multiple ads", or "build a U

- **content-creator** — `/Users/melbourne/.agents/skills/content-creator` — Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks.

- **content-gap-analysis** — `/Users/melbourne/.agents/skills/content-gap-analysis` — Use when the user asks to "find content gaps", "竞品写了什么", or "还应该写什么"; builds a competitor-relative coverage map of missing topics, keyword gaps, and editorial-calendar opportunities. Not for raw keyword demand discovery 

- **content-infographic** — `/Users/melbourne/.agents/skills/content-infographic` — Generate SVG and HTML infographics with brand-aware design. Use when user wants to create an infographic, data visualization, process flow, comparison chart, stat card, or visual data summary.

- **content-marketer** — `/Users/melbourne/.agents/skills/content-marketer` — Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven performance marketing.

- **content-quality-auditor** — `/Users/melbourne/.agents/skills/content-quality-auditor` — Use when auditing content quality, E-E-A-T, or publish readiness; runs a typed 80-item CORE-EEAT profile with evidence coverage, veto checks, and a fix plan. Not for structural tags/headers alone — use on-page-seo-checke

- **content-strategy** — `/Users/melbourne/.agents/skills/content-strategy` — When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. Also use when the user mentions "content strategy," "what should I write about," "content ideas," "blog s

- **content-writer** — `/Users/melbourne/.agents/skills/content-writer` — Use when the user asks to "write SEO content", "draft a blog post / landing page", "update outdated content", or "fix traffic/ranking decay"; two modes — new drafts pages with keywords, headers, snippets, and evidence bo

- **context-agent** — `/Users/melbourne/.agents/skills/context-agent` — Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte.

- **context-compression** — `/Users/melbourne/.agents/skills/context-compression` — When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request.

- **context-degradation** — `/Users/melbourne/.agents/skills/context-degradation` — Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diagnosing failures and designing resilient systems.

- **context-driven-development** — `/Users/melbourne/.agents/skills/context-driven-development` — Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignment through structured project documentation.

- **context-fundamentals** — `/Users/melbourne/.agents/skills/context-fundamentals` — Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, message

- **context-guardian** — `/Users/melbourne/.agents/skills/context-guardian` — Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.

- **context-management-context-restore** — `/Users/melbourne/.agents/skills/context-management-context-restore` — Use when working with context management context restore

- **context-management-context-save** — `/Users/melbourne/.agents/skills/context-management-context-save` — Use when working with context management context save

- **context-manager** — `/Users/melbourne/.agents/skills/context-manager` — Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory systems.

- **context-optimization** — `/Users/melbourne/.agents/skills/context-optimization` — Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically increase context windows but to make better u

- **context-window-management** — `/Users/melbourne/.agents/skills/context-window-management` — Strategies for managing LLM context windows including

- **context7-auto-research** — `/Users/melbourne/.agents/skills/context7-auto-research` — Automatically fetch latest library/framework documentation for Claude Code via Context7 API. Use when you need up-to-date documentation for libraries and frameworks or asking about React, Next.js, Prisma, or any other po

- **contract-helper** — `/Users/melbourne/.agents/skills/contract-helper` — Use when the user asks to "draft an influencer contract", "review these agreement terms", or "build a partnership template"; produces a full influencer agreement framework (scope, compensation, usage rights, exclusivity,

- **conventional-git** — `/Users/melbourne/.agents/skills/conventional-git` — Conventional Commits v1.0.0 branch naming, worktree naming, and commit message standards for GitHub and GitLab projects. Use when creating branches, naming worktrees, writing commits, generating commit messages, reviewin

- **conversation-memory** — `/Users/melbourne/.agents/skills/conversation-memory` — Persistent memory systems for LLM conversations including

- **conversion-signal-qa** — `/Users/melbourne/.agents/skills/conversion-signal-qa` — Use when the user asks to "QA my conversion tracking before launch", "check my UTMs / pixel / event firing", "set up a tracking pre-flight", or "set the dedup rule so Meta and Google stop double-counting"; builds and fix

- **conversion-value-mapper** — `/Users/melbourne/.agents/skills/conversion-value-mapper` — Use when the user asks to "set up conversion values so tROAS optimizes profit not orders", "map margin onto my purchase value", "build value rules for lead / phone / signup conversions", or "stop bidding to revenue when 

- **convertkit-automation** — `/Users/melbourne/.agents/skills/convertkit-automation` — Automate ConvertKit (Kit) tasks via Rube MCP (Composio): manage subscribers, tags, broadcasts, and broadcast stats. Always search tools first for current schemas.

- **convex** — `/Users/melbourne/.agents/skills/convex` — Convex reactive backend expert: schema design, TypeScript functions, real-time subscriptions, auth, file storage, scheduling, and deployment.

- **copilot-sdk** — `/Users/melbourne/.agents/skills/copilot-sdk` — Build applications that programmatically interact with GitHub Copilot. The SDK wraps the Copilot CLI via JSON-RPC, providing session management, custom tools, hooks, MCP server integration, and streaming across Node.js, 

- **copy-editing** — `/Users/melbourne/.agents/skills/copy-editing` — When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. Also use when the user mentions 'edit this copy,' 'review my copy,' 'copy feedback,' 'proofread,' 'polish this,' 'make

- **copywriting** — `/Users/melbourne/.agents/skills/copywriting` — When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pages, about pages, or product pages. Also use when the user says "write copy for,

- **copywriting-cta** — `/Users/melbourne/.agents/skills/copywriting-cta` — Designs end-of-article CTAs — copy, layout, placement, A/B test plan, accessibility — for blog posts, newsletters, and essays. Use whenever the user asks to write, review, or improve a CTA at the bottom of an article; me

- **copywriting-hooks** — `/Users/melbourne/.agents/skills/copywriting-hooks` — >

- **copywriting-prose-creator** — `/Users/melbourne/.agents/skills/copywriting-prose-creator` — Codifies how a person or brand writes — lexicon, syntax, rhythm, structure, signature moves — into a PROSE.md guide, independent of emotional tone. Builds from SOUL.md and TONE.md, ports a guide to another channel, or re

- **copywriting-psychologist** — `/Users/melbourne/.agents/skills/copywriting-psychologist` — One sentence - what this skill does and when to invoke it

- **copywriting-tone-of-voice-creator** — `/Users/melbourne/.agents/skills/copywriting-tone-of-voice-creator` — Builds a brand tone of voice guide (TONE.md) — voice attributes with do's/don'ts, NN/g positioning, tone modulation matrix, lexicon, channel rules — for downstream content skills to consume. Also ports an existing TONE.m

- **core-components** — `/Users/melbourne/.agents/skills/core-components` — Core component library and design system patterns. Use when building UI, using design tokens, or working with the component library.

- **cost-optimization** — `/Users/melbourne/.agents/skills/cost-optimization` — Strategies and patterns for optimizing cloud costs across AWS, Azure, and GCP.

- **cpp-pro** — `/Users/melbourne/.agents/skills/cpp-pro` — Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance optimization.

- **cqrs-implementation** — `/Users/melbourne/.agents/skills/cqrs-implementation` — Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced systems.

- **create-branch** — `/Users/melbourne/.agents/skills/create-branch` — Create a git branch following Sentry naming conventions. Use when asked to "create a branch", "new branch", "start a branch", "make a branch", "switch to a new branch", or when starting new work on the default branch.

- **create-environment** — `/Users/melbourne/.agents/skills/create-environment` — >-

- **create-issue-gate** — `/Users/melbourne/.agents/skills/create-issue-gate` — Use when starting a new implementation task and an issue must be created with strict acceptance criteria gating before execution.

- **create-pr** — `/Users/melbourne/.agents/skills/create-pr` — Alias for sentry-skills:pr-writer. Use when users explicitly ask for "create-pr" or reference the legacy skill name. Redirects to the canonical PR writing workflow.

- **creative-brief** — `/Users/melbourne/.agents/skills/creative-brief` — This skill should be used when the user asks to "write a creative brief", "build a motion brief", "the client doesn't know what they want", "turn this vague client request into a brief", "what questions should I ask the 

- **creative-director** — `/Users/melbourne/.agents/skills/creative-director` — Lead visual creative work from brief to art direction, concept selection, production plan, consistency rules, iteration, and final creative approval.

- **creator-content-auditor** — `/Users/melbourne/.agents/skills/creator-content-auditor` — Use when the user asks to "review this influencer content" or "check if this post meets brand guidelines"; runs the typed STAR pre-publish gate, scores Trust and Appeal on the deliverable, folds in the creator Suitabilit

- **creator-registry** — `/Users/melbourne/.agents/skills/creator-registry` — Use when the user asks "what did we pay this creator last time" or to "update the creator roster"; curates creator identity, rate, rights, exclusivity, compliance-event, and performance facts through the append-only crea

- **cred-omega** — `/Users/melbourne/.agents/skills/cred-omega` — CISO operacional enterprise para gestao total de credenciais e segredos.

- **crewai** — `/Users/melbourne/.agents/skills/crewai` — Expert in CrewAI - the leading role-based multi-agent framework

- **crisis-incident-management** — `/Users/melbourne/.agents/skills/crisis-incident-management` — Coordinate management response to business incidents with facts, severity, containment, owners, communications, decisions, recovery, and post-incident actions.

- **crisis-response-planner** — `/Users/melbourne/.agents/skills/crisis-response-planner` — Use when the user asks to "build our social crisis protocol", "mentions are exploding — what do we do first", or "when do we pause the posting queue"; produces a 1-5 severity ladder with tunable Estimated trigger thresho

- **cro** — `/Users/melbourne/.agents/skills/cro` — When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing pages, feature pages, lead capture forms, or contact forms. Also use when the u

- **crossframe** — `/Users/melbourne/.agents/skills/crossframe` — Use when the user explicitly invokes CrossFrame or 跨尺度结构诊断 for Chinese-canonical structural diagnosis of complex relationships, organizations, institutions, public disputes, or long-term evolution.

- **crossframe-casebook** — `/Users/melbourne/.agents/skills/crossframe-casebook` — Use when CrossFrame Suite routes explicit Chinese casebook work: turning materials into reusable cases, anonymized entries, mechanisms, and retrieval indexes.

- **crossframe-critical** — `/Users/melbourne/.agents/skills/crossframe-critical` — Use only when the user explicitly names crossframe-critical for a Chinese structural critique dossier, article plan, or long-form critical essay.

- **crossframe-debate** — `/Users/melbourne/.agents/skills/crossframe-debate` — Use when CrossFrame Suite routes explicit Chinese proposition testing, debate analysis, hidden-premise review, rebuttal design, or withdrawal condition checks.

- **crossframe-dialogue** — `/Users/melbourne/.agents/skills/crossframe-dialogue` — Use when CrossFrame Suite routes explicit Chinese reader replies, editor responses, consultation-style short answers, or boundary-aware structural advice.

- **crossframe-essay** — `/Users/melbourne/.agents/skills/crossframe-essay` — Use when explicit CrossFrame work needs a Chinese critical insight essay, commentary, concept essay, public piece, or structure-to-article draft after diagnosis.

- **crossframe-notebook** — `/Users/melbourne/.agents/skills/crossframe-notebook` — Use when CrossFrame Suite routes explicit Chinese notes for books, theories, articles, excerpts, bidirectional reading, absorption, or conflict mapping.

- **crossframe-org** — `/Users/melbourne/.agents/skills/crossframe-org` — Use when CrossFrame Suite routes explicit Chinese analysis of teams, projects, organizations, responsibility chains, feedback write-back, repair, or retrospectives.

- **crossframe-public** — `/Users/melbourne/.agents/skills/crossframe-public` — Use when CrossFrame Suite routes explicit Chinese analysis of public issues, platform governance, policy, institutional responsibility, appeals, or compliance evidence.

- **crossframe-review** — `/Users/melbourne/.agents/skills/crossframe-review` — Use when explicit CrossFrame output needs review for reasoning fidelity, evidence boundaries, source anchors, concept drift, article collapse, or repair steps.

- **crossframe-suite** — `/Users/melbourne/.agents/skills/crossframe-suite` — Use when the user explicitly invokes CrossFrame Suite for Chinese structural diagnosis workflows across relationships, organizations, public issues, philosophy, research, or essay output.

- **crossframe-teach** — `/Users/melbourne/.agents/skills/crossframe-teach` — Use when CrossFrame Suite routes explicit Chinese teaching of CrossFrame concepts, misreading boundaries, plain-language examples, signals, or exercises.

- **crxjs** — `/Users/melbourne/.agents/skills/crxjs` — CRXJS Chrome extension development — true HMR for popup, options, content scripts, side panels, manifest-driven builds, dynamic content script imports (`?script`, `?script&module`), and `defineManifest` for type-safe man

- **crypto-bd-agent** — `/Users/melbourne/.agents/skills/crypto-bd-agent` — Production-tested patterns for building AI agents that autonomously discover, > evaluate, and acquire token listings for cryptocurrency exchanges.

- **csharp-pro** — `/Users/melbourne/.agents/skills/csharp-pro` — Write modern C# code with advanced features like records, pattern matching, and async/await. Optimizes .NET applications, implements enterprise patterns, and ensures comprehensive testing.

- **customer-psychographic-profiler** — `/Users/melbourne/.agents/skills/customer-psychographic-profiler` — One sentence - what this skill does and when to invoke it

- **customer-research** — `/Users/melbourne/.agents/skills/customer-research` — When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "talk to customers," "analyze transcripts," "customer interviews," "survey analysi

- **customer-support** — `/Users/melbourne/.agents/skills/customer-support` — Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences.

- **customs-trade-compliance** — `/Users/melbourne/.agents/skills/customs-trade-compliance` — Codified expertise for customs documentation, tariff classification, duty optimisation, restricted party screening, and regulatory compliance across multiple jurisdictions.

- **cv-generator** — `/Users/melbourne/.agents/skills/cv-generator` — Generate professional, ATS-optimized CVs for FlowCV, Canva, Google Docs, or Word. Handles multi-source merging, JD targeting, seniority adaptation, and humanized rewriting. Outputs paste-ready text with an ATS flaw repor

- **daily** — `/Users/melbourne/.agents/skills/daily` — Documentation and capabilities reference for Daily

- **daily-gift** — `/Users/melbourne/.agents/skills/daily-gift` — Relationship-aware daily gift engine with five-stage creative pipeline — editorial judgment, synthesis, concept generation, visual strategy, and rendering in H5, image, or video

- **daily-management-review** — `/Users/melbourne/.agents/skills/daily-management-review` — Run a concise daily management review of commitments, calendar, blockers, follow-ups, delegation, decisions, capacity, and today’s critical outcomes.

- **daily-news-report** — `/Users/melbourne/.agents/skills/daily-news-report` — Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports.

- **dark-social-attributor** — `/Users/melbourne/.agents/skills/dark-social-attributor` — Use when the user asks to "figure out where our direct traffic really comes from", "measure dark social", "add a how-did-you-hear-about-us field", or "show social drives signups without click data"; produces a share-link

- **dashboard-builder** — `/Users/melbourne/.agents/skills/dashboard-builder` — Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard instead of a vanity board.

- **dashboarding** — `/Users/melbourne/.agents/skills/dashboarding` — Create, modify, and organise Grafana dashboards including panels, variables, transformations,

- **data-engineer** — `/Users/melbourne/.agents/skills/data-engineer` — Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and cloud-native data platforms.

- **data-engineering-data-driven-feature** — `/Users/melbourne/.agents/skills/data-engineering-data-driven-feature` — Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis, implementation, and experimentation.

- **data-engineering-data-pipeline** — `/Users/melbourne/.agents/skills/data-engineering-data-pipeline` — You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for batch and streaming data processing.

- **data-quality-frameworks** — `/Users/melbourne/.agents/skills/data-quality-frameworks` — Implement data quality validation with Great Expectations, dbt tests, and data contracts. Use when building data quality pipelines, implementing validation rules, or establishing data contracts.

- **data-scientist** — `/Users/melbourne/.agents/skills/data-scientist` — Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling, and business intelligence.

- **data-storytelling** — `/Users/melbourne/.agents/skills/data-storytelling` — Transform raw data into compelling narratives that drive decisions and inspire action.

- **data-structure-protocol** — `/Users/melbourne/.agents/skills/data-structure-protocol` — Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist without re-reading the whole repo.

- **data-visualization** — `/Users/melbourne/.agents/skills/data-visualization` — Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles l

- **database** — `/Users/melbourne/.agents/skills/database` — Database development and operations workflow covering SQL, NoSQL, database design, migrations, optimization, and data engineering.

- **database-admin** — `/Users/melbourne/.agents/skills/database-admin` — Expert database administrator specializing in modern cloud databases, automation, and reliability engineering.

- **database-architect** — `/Users/melbourne/.agents/skills/database-architect` — Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database architectures.

- **database-cloud-optimization-cost-optimize** — `/Users/melbourne/.agents/skills/database-cloud-optimization-cost-optimize` — You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings opportunities, and implement cost-effectiv

- **database-design** — `/Users/melbourne/.agents/skills/database-design` — Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases.

- **database-migration** — `/Users/melbourne/.agents/skills/database-migration` — Master database schema and data migrations across ORMs (Sequelize, TypeORM, Prisma), including rollback strategies and zero-downtime deployments.

- **database-migrations-migration-observability** — `/Users/melbourne/.agents/skills/database-migrations-migration-observability` — Migration monitoring, CDC, and observability infrastructure

- **database-migrations-sql-migrations** — `/Users/melbourne/.agents/skills/database-migrations-sql-migrations` — SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, and SQL Server. Focus on data integrity and rollback plans.

- **database-optimizer** — `/Users/melbourne/.agents/skills/database-optimizer` — Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures.

- **database-schema-designer** — `/Users/melbourne/.agents/skills/database-schema-designer` — Design robust, scalable database schemas for SQL and NoSQL databases. Provides normalization guidelines, indexing strategies, migration patterns, constraint design, and performance optimization. Ensures data integrity, q

- **datadog-automation** — `/Users/melbourne/.agents/skills/datadog-automation` — Automate Datadog tasks via Rube MCP (Composio): query metrics, search logs, manage monitors/dashboards, create events and downtimes. Always search tools first for current schemas.

- **dbos-golang** — `/Users/melbourne/.agents/skills/dbos-golang` — Guide for building reliable, fault-tolerant Go applications with DBOS durable workflows. Use when adding DBOS to existing Go code, creating workflows and steps, or using queues for concurrency control.

- **dbos-python** — `/Users/melbourne/.agents/skills/dbos-python` — Guide for building reliable, fault-tolerant Python applications with DBOS durable workflows. Use when adding DBOS to existing Python code, creating workflows and steps, or using queues for concurrency control.

- **dbos-typescript** — `/Users/melbourne/.agents/skills/dbos-typescript` — Guide for building reliable, fault-tolerant TypeScript applications with DBOS durable workflows. Use when adding DBOS to existing TypeScript code, creating workflows and steps, or using queues for concurrency control.

- **dbt-transformation-patterns** — `/Users/melbourne/.agents/skills/dbt-transformation-patterns` — Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental processing.

- **ddd-context-mapping** — `/Users/melbourne/.agents/skills/ddd-context-mapping` — Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns.

- **ddd-strategic-design** — `/Users/melbourne/.agents/skills/ddd-strategic-design` — Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains.

- **ddd-tactical-patterns** — `/Users/melbourne/.agents/skills/ddd-tactical-patterns` — Apply DDD tactical patterns in code using entities, value objects, aggregates, repositories, and domain events with explicit invariants.

- **debug-buttercup** — `/Users/melbourne/.agents/skills/debug-buttercup` — All pods run in namespace crs. Use when pods in the crs namespace are in CrashLoopBackOff, OOMKilled, or restarting, multiple services restart simultaneously (cascade failure), or redis is unresponsive or showing AOF war

- **debugger** — `/Users/melbourne/.agents/skills/debugger` — Debugging specialist for errors, test failures, and unexpected

- **debugging-strategies** — `/Users/melbourne/.agents/skills/debugging-strategies` — Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches.

- **debugging-toolkit** — `/Users/melbourne/.agents/skills/debugging-toolkit` — Use when working with debugging toolkit smart debug (Alias for debugging-toolkit-smart-debug)

- **debugging-toolkit-smart-debug** — `/Users/melbourne/.agents/skills/debugging-toolkit-smart-debug` — Use when working with debugging toolkit smart debug

- **decision-navigator** — `/Users/melbourne/.agents/skills/decision-navigator` — Guide stuck or overwhelmed users through targeted branching questions until they reach concrete next steps.

- **decision-support** — `/Users/melbourne/.agents/skills/decision-support` — Frame management decisions, compare options against explicit criteria, test assumptions, map trade-offs and risks, and produce a decision recommendation.

- **deck-creator** — `/Users/melbourne/.agents/skills/deck-creator` — This skill should be used when the user asks to "create a deck", "make a presentation", "build slides", "pitch deck", "investor deck", "sales presentation", "design a deck", "interactive presentation", "presenter mode", 

- **deep-research** — `/Users/melbourne/.agents/skills/deep-research` — Deep research on any topic — broad parallel web searches, multi-source validation, confidence tracking, and a cited Markdown report. Use whenever the deliverable is a thorough sourced report rather than a quick answer: '

- **defi-protocol-templates** — `/Users/melbourne/.agents/skills/defi-protocol-templates` — Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance applications or smart contract protocols.

- **defuddle** — `/Users/melbourne/.agents/skills/defuddle` — Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or analyze, for online documentation, article

- **delegation-accountability** — `/Users/melbourne/.agents/skills/delegation-accountability` — Design effective delegation with clear outcomes, authority, constraints, checkpoints, escalation rules, acceptance criteria, and accountability follow-up.

- **deliverability-qa** — `/Users/melbourne/.agents/skills/deliverability-qa` — Use when the user asks to "run a deliverability pre-flight before I send", "check my SPF/DKIM/DMARC/BIMI", "why am I landing in spam / promotions", or "score my sender reputation and list hygiene"; runs the ONE-TIME pre-

- **dependency-management-deps-audit** — `/Users/melbourne/.agents/skills/dependency-management-deps-audit` — You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilities, licensing issues, outdated packages, and

- **dependency-upgrade** — `/Users/melbourne/.agents/skills/dependency-upgrade` — Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches.

- **deploy-to-vercel** — `/Users/melbourne/.agents/skills/deploy-to-vercel` — Deploy applications and websites to Vercel. Use when the user requests deployment actions like \"deploy my app\", \"deploy and give me the link\", \"push this live\", or \"create a preview deployment\".

- **deployment-engineer** — `/Users/melbourne/.agents/skills/deployment-engineer` — Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation.

- **deployment-pipeline-design** — `/Users/melbourne/.agents/skills/deployment-pipeline-design` — Architecture patterns for multi-stage CI/CD pipelines with approval gates and deployment strategies.

- **deployment-procedures** — `/Users/melbourne/.agents/skills/deployment-procedures` — Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts.

- **deployment-validation-config-validate** — `/Users/melbourne/.agents/skills/deployment-validation-config-validate` — You are a configuration management expert specializing in validating, testing, and ensuring the correctness of application configurations. Create comprehensive validation schemas, implement configurat

- **depth-map-generation** — `/Users/melbourne/.agents/skills/depth-map-generation` — Generate depth maps from images using each::sense AI. Create depth estimation for 3D effects, parallax animations, VR/AR applications, focus effects, and stereo image generation.

- **design-handoff** — `/Users/melbourne/.agents/skills/design-handoff` — Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, a

- **design-it** — `/Users/melbourne/.agents/skills/design-it` — Routes frontend design tasks to 48 specific UI styles. Triggers for websites, app screens, or UI components requesting a specific aesthetic.

- **design-md** — `/Users/melbourne/.agents/skills/design-md` — Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files

- **design-orchestration** — `/Users/melbourne/.agents/skills/design-orchestration` — Orchestrates design workflows by routing work through brainstorming, multi-agent review, and execution readiness in the correct order.

- **design-spells** — `/Users/melbourne/.agents/skills/design-spells` — Curated micro-interactions and design details that add "magic" and personality to websites and apps.

- **design-taste-frontend** — `/Users/melbourne/.agents/skills/design-taste-frontend` — Use when building high-agency frontend interfaces with strict design taste, calibrated color, responsive layout, and motion rules.

- **deterministic-design** — `/Users/melbourne/.agents/skills/deterministic-design` — Render the UI and prove it's balanced + usable: a deterministic layout audit (centroid / optical-center / pixel-oracle balance via explicit math + annotated screenshot) plus a vision-judged Nielsen usability audit by a s

- **devcontainer-setup** — `/Users/melbourne/.agents/skills/devcontainer-setup` — Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configu

- **development** — `/Users/melbourne/.agents/skills/development` — Comprehensive web, mobile, and backend development workflow bundling frontend, backend, full-stack, and mobile development skills for end-to-end application delivery.

- **devops-deploy** — `/Users/melbourne/.agents/skills/devops-deploy` — DevOps e deploy de aplicacoes — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como codigo e monitoramento.

- **devops-troubleshooter** — `/Users/melbourne/.agents/skills/devops-troubleshooter` — Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability.

- **diagnosing-bugs** — `/Users/melbourne/.agents/skills/diagnosing-bugs` — Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.

- **diary** — `/Users/melbourne/.agents/skills/diary` — Unified Diary System: A context-preserving automated logger for multi-project development.

- **differential-review** — `/Users/melbourne/.agents/skills/differential-review` — Security-focused code review for PRs, commits, and diffs.

- **digital-twin-generation** — `/Users/melbourne/.agents/skills/digital-twin-generation` — Generate photorealistic digital twins and avatar clones using each::sense AI. Create AI-powered digital representations for video calls, corporate communications, customer service, and multilingual content.

- **directory-submissions** — `/Users/melbourne/.agents/skills/directory-submissions` — When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, and discovery. Also use when the user mentions "directory submissions," "submit t

- **discord-automation** — `/Users/melbourne/.agents/skills/discord-automation` — Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions. Always search tools first for current schemas.

- **discord-bot-architect** — `/Users/melbourne/.agents/skills/discord-bot-architect` — Specialized skill for building production-ready Discord bots.

- **discord-graphics-generation** — `/Users/melbourne/.agents/skills/discord-graphics-generation` — Generate Discord server graphics using each::sense AI. Create server icons, banners, role icons, welcome graphics, event banners, bot avatars, emojis, and more optimized for Discord's format requirements.

- **dispatching-parallel-agents** — `/Users/melbourne/.agents/skills/dispatching-parallel-agents` — Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies

- **distributed-debugging-debug-trace** — `/Users/melbourne/.agents/skills/distributed-debugging-debug-trace` — You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools. Configure debugging workflows, implement tracing solutions, and establish troubleshoo

- **distributed-tracing** — `/Users/melbourne/.agents/skills/distributed-tracing` — Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices.

- **django-access-review** — `/Users/melbourne/.agents/skills/django-access-review` — django-access-review

- **django-perf-review** — `/Users/melbourne/.agents/skills/django-perf-review` — Django performance code review. Use when asked to "review Django performance", "find N+1 queries", "optimize Django", "check queryset performance", "database performance", "Django ORM issues", or audit Django code for pe

- **django-pro** — `/Users/melbourne/.agents/skills/django-pro` — Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and deployment.

- **doc-coauthoring** — `/Users/melbourne/.agents/skills/doc-coauthoring` — This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gathering, Refinement & Structure, and Reader Testi

- **doc2math** — `/Users/melbourne/.agents/skills/doc2math` — Convert narrative technical documents into grounded Mathematical Problem Specifications with variables, constraints, objectives, and uncertainty.

- **docker-expert** — `/Users/melbourne/.agents/skills/docker-expert` — You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patterns, and production deployment strategies b

- **docs-architect** — `/Users/melbourne/.agents/skills/docs-architect` — Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to produce long-form technical manuals and ebooks.

- **document-control-knowledge** — `/Users/melbourne/.agents/skills/document-control-knowledge` — Organize management documents, versions, decisions, records, naming, ownership, approval status, retention logic, and reusable organizational knowledge.

- **documentation** — `/Users/melbourne/.agents/skills/documentation` — Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing.

- **documentation-generation-doc-generate** — `/Users/melbourne/.agents/skills/documentation-generation-doc-generate` — You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and i

- **documentation-templates** — `/Users/melbourne/.agents/skills/documentation-templates` — Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation.

- **docusign-automation** — `/Users/melbourne/.agents/skills/docusign-automation` — Automate DocuSign tasks via Rube MCP (Composio): templates, envelopes, signatures, document management. Always search tools first for current schemas.

- **docx-official** — `/Users/melbourne/.agents/skills/docx-official` — A user may ask you to create, edit, or analyze the contents of a .docx file. A .docx file is essentially a ZIP archive containing XML files and other resources that you can read or edit. You have different tools and work

- **domain-authority-auditor** — `/Users/melbourne/.agents/skills/domain-authority-auditor` — Use when auditing domain authority, trust, or citation credibility; runs a peer-relative 40-item CITE profile with evidence coverage and verified manipulation/penalty veto checks. Not for page-level content quality — use

- **domain-driven-design** — `/Users/melbourne/.agents/skills/domain-driven-design` — Plan and route Domain-Driven Design work from strategic modeling to tactical implementation and evented architecture patterns.

- **domain-modeling** — `/Users/melbourne/.agents/skills/domain-modeling` — Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an architectural decision, or when another skill needs to maintain the domain model.

- **dos-verify-done-claims** — `/Users/melbourne/.agents/skills/dos-verify-done-claims` — Before accepting an agent's 'done / shipped / fixed' claim, verify it against ground truth (git ancestry + the commit's own diff) using the DOS kernel's `dos verify` and `dos commit-audit` — never the agent's own narrati

- **dotnet-architect** — `/Users/melbourne/.agents/skills/dotnet-architect` — Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns.

- **dotnet-backend** — `/Users/melbourne/.agents/skills/dotnet-backend` — Build ASP.NET Core 8+ backend services with EF Core, auth, background jobs, and production API patterns.

- **dotnet-backend-patterns** — `/Users/melbourne/.agents/skills/dotnet-backend-patterns` — Master C#/.NET patterns for building production-grade APIs, MCP servers, and enterprise backends with modern best practices (2024/2025).

- **draft** — `/Users/melbourne/.agents/skills/draft` — >

- **drizzle-orm-expert** — `/Users/melbourne/.agents/skills/drizzle-orm-expert` — Expert in Drizzle ORM for TypeScript — schema design, relational queries, migrations, and serverless database integration. Use when building type-safe database layers with Drizzle.

- **dropbox-automation** — `/Users/melbourne/.agents/skills/dropbox-automation` — Automate Dropbox file management, sharing, search, uploads, downloads, and folder operations via Rube MCP (Composio). Always search tools first for current schemas.

- **dwarf-expert** — `/Users/melbourne/.agents/skills/dwarf-expert` — Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions

- **dx-optimizer** — `/Users/melbourne/.agents/skills/dx-optimizer` — Developer Experience specialist. Improves tooling, setup, and workflows. Use PROACTIVELY when setting up new projects, after team feedback, or when development friction is noticed.

- **dynamic-content-personalizer** — `/Users/melbourne/.agents/skills/dynamic-content-personalizer` — Use when the user asks to "personalize the email", "add merge tags / dynamic content", "set up conditional blocks per segment", or "make first-name and product-recommendation fields fall back safely"; produces a merge-ta

- **e2e-testing** — `/Users/melbourne/.agents/skills/e2e-testing` — End-to-end testing workflow with Playwright for browser automation, visual regression, cross-browser testing, and CI/CD integration.

- **e2e-testing-patterns** — `/Users/melbourne/.agents/skills/e2e-testing-patterns` — Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before users do.

- **each-sense** — `/Users/melbourne/.agents/skills/each-sense` — each::sense is the intelligent layer for generative media. A unified AI agent that generates marketing assets, ads, product images, videos, and creative content. It knows all AI models and automatically selects the best 

- **eachlabs-face-swap** — `/Users/melbourne/.agents/skills/eachlabs-face-swap` — Swap faces between images using EachLabs AI. Use when the user wants to replace or swap faces in photos.

- **eachlabs-fashion-ai** — `/Users/melbourne/.agents/skills/eachlabs-fashion-ai` — Generate fashion model imagery, virtual try-on, runway videos, and campaign visuals using EachLabs AI. Use when the user needs fashion content, model photography, or virtual try-on.

- **eachlabs-image-edit** — `/Users/melbourne/.agents/skills/eachlabs-image-edit` — Edit, transform, upscale, and enhance images using EachLabs AI models. Supports image editing, style transfer, background removal, upscaling, inpainting, face swap, virtual try-on, 3D generation, and image analysis. Use 

- **eachlabs-image-generation** — `/Users/melbourne/.agents/skills/eachlabs-image-generation` — Generate new images from text prompts using EachLabs AI models. Supports text-to-image with multiple model families including Flux, GPT Image, Gemini, Imagen, Seedream, and more. Use when the user wants to create new ima

- **eachlabs-music** — `/Users/melbourne/.agents/skills/eachlabs-music` — Generate songs, instrumentals, lyrics, and podcasts using EachLabs Mureka AI models. Also supports song extension, stem separation, and song recognition. Use when the user wants to create music, lyrics, or audio content.

- **eachlabs-product-visuals** — `/Users/melbourne/.agents/skills/eachlabs-product-visuals` — Generate professional e-commerce product photography and videos using EachLabs AI models. Product shots, background replacement, lifestyle scenes, and 360-degree views. Use when the user needs product images for e-commer

- **eachlabs-video-edit** — `/Users/melbourne/.agents/skills/eachlabs-video-edit` — Edit, transform, extend, upscale, and enhance videos using EachLabs AI models. Supports lip sync, video translation, subtitle generation, audio merging, style transfer, and video extension. Use when the user wants to edi

- **eachlabs-video-generation** — `/Users/melbourne/.agents/skills/eachlabs-video-generation` — Generate new videos from text prompts, images, or reference inputs using EachLabs AI models. Supports text-to-video, image-to-video, transitions, motion control, talking head, and avatar generation. Use when the user wan

- **eachlabs-voice-audio** — `/Users/melbourne/.agents/skills/eachlabs-voice-audio` — Text-to-speech, speech-to-text, voice conversion, and audio processing using EachLabs AI models. Supports ElevenLabs TTS, Whisper transcription with diarization, and RVC voice conversion. Use when the user needs TTS, tra

- **eachlabs-workflows** — `/Users/melbourne/.agents/skills/eachlabs-workflows` — Build and orchestrate multi-step AI workflows combining multiple EachLabs models. Create custom pipelines, trigger executions, and manage workflow versions. Use when the user needs to chain multiple AI models or automate

- **earllm-build** — `/Users/melbourne/.agents/skills/earllm-build` — Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline.

- **early-access-designer** — `/Users/melbourne/.agents/skills/early-access-designer` — Use when the user asks to "design an early access program", "set up a waitlist and beta stages", or "define beta graduation criteria"; produces a waitlist→concept→alpha→beta→GA stage ladder with per-stage purpose and opt

- **ecl-harness-engineer** — `/Users/melbourne/.agents/skills/ecl-harness-engineer` — Create or audit ECL Agent Harness infrastructure: AGENTS.md, change tracking, repository guidance, lint checks, CI gates, and agent handoff docs.

- **edit-image** — `/Users/melbourne/.agents/skills/edit-image` — This skill should be used when the user asks to "edit an image", "modify a photo", "inpaint", "outpaint", "extend an image", "replace object in image", "add element to image", "resize image for social media", "crop image

- **efficient-web-research** — `/Users/melbourne/.agents/skills/efficient-web-research` — >

- **ejentum-reasoning-harness** — `/Users/melbourne/.agents/skills/ejentum-reasoning-harness` — MCP server exposing four cognitive harness modes (reasoning, code, anti-deception, memory). Each call returns an engineered scaffold (failure pattern, procedure, suppression vectors, falsification test) the agent ingests

- **electron-development** — `/Users/melbourne/.agents/skills/electron-development` — Master Electron desktop app development with secure IPC, contextIsolation, preload scripts, multi-process architecture, electron-builder packaging, code signing, and auto-update.

- **elixir-pro** — `/Users/melbourne/.agents/skills/elixir-pro` — Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. Masters concurrency, fault tolerance, and distributed systems.

- **elon-musk** — `/Users/melbourne/.agents/skills/elon-musk` — Agente que simula Elon Musk com profundidade psicologica e comunicacional de alta fidelidade. Ativado para: \"fale como Elon\", \"simule Elon Musk\", \"o que Elon diria sobre X\", \"first principles thinking\", \"think l

- **email-and-newsletter** — `/Users/melbourne/.agents/skills/email-and-newsletter` — >-

- **email-banner-generation** — `/Users/melbourne/.agents/skills/email-banner-generation` — Generate email marketing banners and headers using each::sense AI. Create newsletter headers, promotional banners, welcome emails, and seasonal campaigns optimized for email-safe dimensions and best practices.

- **email-creative-builder** — `/Users/melbourne/.agents/skills/email-creative-builder` — Use when the user asks to "write the email", "draft subject lines", or "build email creative"; produces the pre-click unit — subject-line variants + preheader, body copy, one clear CTA, and a plain-text alt — message-mat

- **email-quality-auditor** — `/Users/melbourne/.agents/skills/email-quality-auditor` — Use when the user asks to "audit an email program" or "is this campaign safe to send"; runs a typed 20-item SEND profile with authentication, consent, opt-out, and claim veto checks on own evidence. Not for building deli

- **email-render-builder** — `/Users/melbourne/.agents/skills/email-render-builder` — Use when the user asks to "build the email HTML", "make this email responsive", "fix dark-mode rendering", or "QA the email across clients"; produces the coded HTML build — a responsive table layout, dark-mode + accessib

- **email-sequence** — `/Users/melbourne/.agents/skills/email-sequence` — You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, and move people toward conversion.

- **email-sequence-designer** — `/Users/melbourne/.agents/skills/email-sequence-designer` — Use when the user asks to "design a welcome flow", "set up an abandoned-cart sequence", "build a light re-engagement branch inside a lifecycle flow", or "plan a cold-outbound sequence"; produces general lifecycle automat

- **email-systems** — `/Users/melbourne/.agents/skills/email-systems` — Email has the highest ROI of any marketing channel. $36 for every

- **emails** — `/Users/melbourne/.agents/skills/emails` — When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence," "drip campaign," "nurture sequence," "onboar

- **embedding-strategies** — `/Users/melbourne/.agents/skills/embedding-strategies` — Guide to selecting and optimizing embedding models for vector search applications.

- **emblemai-crypto-wallet** — `/Users/melbourne/.agents/skills/emblemai-crypto-wallet` — Crypto wallet management across 7 blockchains via EmblemAI Agent Hustle API. Balance checks, token swaps, portfolio analysis, and transaction execution for Solana, Ethereum, Base, BSC, Polygon, Hedera, and Bitcoin.

- **emergency-card** — `/Users/melbourne/.agents/skills/emergency-card` — 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。

- **emoji-sticker-generation** — `/Users/melbourne/.agents/skills/emoji-sticker-generation` — Generate custom emoji and sticker packs using each::sense AI. Create personalized emoji from photos, expression packs, animated stickers, and platform-specific emoji sets for Slack, Discord, WhatsApp, and more.

- **emotional-arc-designer** — `/Users/melbourne/.agents/skills/emotional-arc-designer` — One sentence - what this skill does and when to invoke it

- **employment-contract-templates** — `/Users/melbourne/.agents/skills/employment-contract-templates` — Templates and patterns for creating legally sound employment documentation including contracts, offer letters, and HR policies.

- **energy-procurement** — `/Users/melbourne/.agents/skills/energy-procurement` — Codified expertise for electricity and gas procurement, tariff optimisation, demand charge management, renewable PPA evaluation, and multi-facility energy cost management.

- **engagement-inbox-manager** — `/Users/melbourne/.agents/skills/engagement-inbox-manager` — Use when the user asks to "triage our comments, DMs, and mentions", "draft replies to this thread", "can we repost this fan post", or "set up inbox SLAs and an escalation path"; produces a ranked triage queue with regist

- **enhance-prompt** — `/Users/melbourne/.agents/skills/enhance-prompt` — Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context, and structures output for better generation results.

- **entity-registry** — `/Users/melbourne/.agents/skills/entity-registry` — Use when the user asks to "optimize entity presence", reconcile an entity identity, or update canonical Knowledge Graph facts; audits and maintains machine-facing identity, sameAs, schema, disambiguation, and AI-recognit

- **entity-seo** — `/Users/melbourne/.agents/skills/entity-seo` — When the user wants to optimize for entity recognition, Knowledge Graph, or entity-based SEO. Also use when the user mentions "entity SEO," "entity optimization," "Knowledge Graph," "Knowledge Panel," "entity signals," "

- **environment-setup-guide** — `/Users/melbourne/.agents/skills/environment-setup-guide` — Guide developers through setting up development environments with proper tools, dependencies, and configurations

- **error-debugging-error-analysis** — `/Users/melbourne/.agents/skills/error-debugging-error-analysis` — You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability solutions.

- **error-debugging-error-trace** — `/Users/melbourne/.agents/skills/error-debugging-error-trace` — You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implement structured logging, and ensure teams ca

- **error-debugging-multi-agent-review** — `/Users/melbourne/.agents/skills/error-debugging-multi-agent-review` — Use when working with error debugging multi agent review

- **error-detective** — `/Users/melbourne/.agents/skills/error-detective` — Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes.

- **error-diagnostics-error-analysis** — `/Users/melbourne/.agents/skills/error-diagnostics-error-analysis` — You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability solutions.

- **error-diagnostics-error-trace** — `/Users/melbourne/.agents/skills/error-diagnostics-error-trace` — You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implement structured logging,

- **error-diagnostics-smart-debug** — `/Users/melbourne/.agents/skills/error-diagnostics-smart-debug` — Use when working with error diagnostics smart debug

- **error-handling-patterns** — `/Users/melbourne/.agents/skills/error-handling-patterns` — Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging experiences.

- **ethical-hacking-methodology** — `/Users/melbourne/.agents/skills/ethical-hacking-methodology` — Master the complete penetration testing lifecycle from reconnaissance through reporting. This skill covers the five stages of ethical hacking methodology, essential tools, attack techniques, and professional reporting fo

- **evaluation** — `/Users/melbourne/.agents/skills/evaluation` — Build evaluation frameworks for agent systems. Use when testing agent performance systematically, validating context engineering choices, or measuring improvements over time.

- **event-sourcing-architect** — `/Users/melbourne/.agents/skills/event-sourcing-architect` — Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestration, and eventual consistency patterns. Use PROACTIVELY for event-sourced systems, a

- **event-staffing-compliance** — `/Users/melbourne/.agents/skills/event-staffing-compliance` — Assess worker-classification and compliance risk for temporary event staffing in the US and Canada — W-2 vs 1099, misclassification penalties, joint-employer liability, COI, and wage/hour rules. Includes live state-by-st

- **event-staffing-ordering** — `/Users/melbourne/.agents/skills/event-staffing-ordering` — Order W-2 compliant temporary event staff for conventions, trade shows, festivals, concerts, sporting events, and brand activations across 300+ US and Canadian markets via TempGuru. Covers city coverage, role pricing, av

- **event-store-design** — `/Users/melbourne/.agents/skills/event-store-design` — Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistence patterns.

- **events** — `/Users/melbourne/.agents/skills/events` — When the user wants to plan, run, sponsor, speak at, or get pipeline from events — webinars, conferences, trade shows, meetups, dinners, workshops, virtual summits, or user conferences. Also use when the user mentions 'e

- **evolution** — `/Users/melbourne/.agents/skills/evolution` — This skill enables makepad-skills to self-improve continuously during development.

- **exa-search** — `/Users/melbourne/.agents/skills/exa-search` — Semantic search, similar content discovery, and structured research using Exa API. Use when you need semantic/embeddings-based search, finding similar content, or searching by category (company, people, research papers, 

- **examprep-ai** — `/Users/melbourne/.agents/skills/examprep-ai` — Exam preparation assistant that converts syllabi, past papers, or notes into a ranked High Score Roadmap. Covers theory, numericals, MCQs, coding, and lab prep, ordered Easy → Medium → Hard. Use for last-minute revision,

- **executing-plans** — `/Users/melbourne/.agents/skills/executing-plans` — Use when you have a written implementation plan to execute in a separate session with review checkpoints

- **executive-assistant** — `/Users/melbourne/.agents/skills/executive-assistant` — Organize a manager’s workload, commitments, follow-ups, briefings, agenda, deadlines, and next actions from messages, notes, documents, or plans.

- **explain-like-socrates** — `/Users/melbourne/.agents/skills/explain-like-socrates` — >

- **expo-api-routes** — `/Users/melbourne/.agents/skills/expo-api-routes` — Guidelines for creating API routes in Expo Router with EAS Hosting

- **expo-cicd-workflows** — `/Users/melbourne/.agents/skills/expo-cicd-workflows` — Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflows/, or wants help with EAS build pipelines

- **expo-deployment** — `/Users/melbourne/.agents/skills/expo-deployment` — Deploy Expo apps to production

- **expo-dev-client** — `/Users/melbourne/.agents/skills/expo-dev-client` — Build and distribute Expo development clients locally or via TestFlight

- **expo-tailwind-setup** — `/Users/melbourne/.agents/skills/expo-tailwind-setup` — Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling

- **expo-ui-jetpack-compose** — `/Users/melbourne/.agents/skills/expo-ui-jetpack-compose` — expo-ui-jetpack-compose

- **expo-ui-swift-ui** — `/Users/melbourne/.agents/skills/expo-ui-swift-ui` — expo-ui-swift-ui

- **eye-color-changer** — `/Users/melbourne/.agents/skills/eye-color-changer` — Change eye colors in photos using each::sense AI. Transform natural eye colors, create fantasy effects, heterochromia, glowing eyes, and more with realistic blending and natural-looking results.

- **face-morphing** — `/Users/melbourne/.agents/skills/face-morphing` — Morph, blend, and transform faces using each::sense AI. Create face morphs, celebrity blends, family resemblance predictions, gender swaps, and animated transitions between faces.

- **faf-expert** — `/Users/melbourne/.agents/skills/faf-expert` — Advanced .faf (Foundational AI-context Format) specialist. IANA-registered format, MCP server config, championship scoring, bi-directional sync.

- **faf-wizard** — `/Users/melbourne/.agents/skills/faf-wizard` — Done-for-you .faf generator. One-click AI context for any project - new, legacy, or famous. Auto-detects stack, scores readiness, works everywhere.

- **fal-audio** — `/Users/melbourne/.agents/skills/fal-audio` — Text-to-speech and speech-to-text using fal.ai audio models

- **fal-generate** — `/Users/melbourne/.agents/skills/fal-generate` — Generate images and videos using fal.ai AI models

- **fal-image-edit** — `/Users/melbourne/.agents/skills/fal-image-edit` — AI-powered image editing with style transfer and object removal

- **fal-platform** — `/Users/melbourne/.agents/skills/fal-platform` — Platform APIs for model management, pricing, and usage tracking

- **fal-upscale** — `/Users/melbourne/.agents/skills/fal-upscale` — Upscale and enhance image and video resolution using AI

- **fal-workflow** — `/Users/melbourne/.agents/skills/fal-workflow` — Generate workflow JSON files for chaining AI models

- **family-health-analyzer** — `/Users/melbourne/.agents/skills/family-health-analyzer` — 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议

- **fastapi-pro** — `/Users/melbourne/.agents/skills/fastapi-pro` — Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async patterns.

- **fastapi-router-py** — `/Users/melbourne/.agents/skills/fastapi-router-py` — Create FastAPI routers following established patterns with proper authentication, response models, and HTTP status codes.

- **fastapi-templates** — `/Users/melbourne/.agents/skills/fastapi-templates` — Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building new FastAPI applications or setting up backend API projects.

- **fatigue-frequency-manager** — `/Users/melbourne/.agents/skills/fatigue-frequency-manager` — Use when the user asks to "is my ad fatiguing", "why is CTR dropping at scale", or "should I rotate creative / widen the audience"; reads frequency, CTR and CVR decay against an early-flight baseline and returns Rotate-c

- **favicon** — `/Users/melbourne/.agents/skills/favicon` — Generate favicons from a source image

- **fda-food-safety-auditor** — `/Users/melbourne/.agents/skills/fda-food-safety-auditor` — Expert AI auditor for FDA Food Safety (FSMA), HACCP, and PCQI compliance. Reviews food facility records and preventive controls.

- **fda-medtech-compliance-auditor** — `/Users/melbourne/.agents/skills/fda-medtech-compliance-auditor` — Expert AI auditor for Medical Device (SaMD) compliance, IEC 62304, and 21 CFR Part 820. Reviews DHFs, technical files, and software validation.

- **ffuf-claude-skill** — `/Users/melbourne/.agents/skills/ffuf-claude-skill` — Web fuzzing with ffuf

- **ffuf-web-fuzzing** — `/Users/melbourne/.agents/skills/ffuf-web-fuzzing` — Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests, auto-calibration, and result analysis

- **figma-automation** — `/Users/melbourne/.agents/skills/figma-automation` — Automate Figma tasks via Rube MCP (Composio): files, components, design tokens, comments, exports. Always search tools first for current schemas.

- **file-organizer** — `/Users/melbourne/.agents/skills/file-organizer` — 6. Reduces Clutter: Identifies old files you probably don't need anymore

- **file-path-traversal** — `/Users/melbourne/.agents/skills/file-path-traversal` — Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary files on the server, potentially including sensitive configuration files, credentials, and source code

- **file-uploads** — `/Users/melbourne/.agents/skills/file-uploads` — Expert at handling file uploads and cloud storage. Covers S3,

- **filesystem-context** — `/Users/melbourne/.agents/skills/filesystem-context` — Use for file-based context management, dynamic context discovery, and reducing context window bloat. Offload context to files for just-in-time loading.

- **find-bugs** — `/Users/melbourne/.agents/skills/find-bugs` — Find bugs, security vulnerabilities, and code quality issues in local branch changes. Use when asked to review changes, find bugs, security review, or audit code on the current branch.

- **find-skills** — `/Users/melbourne/.agents/skills/find-skills` — Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used w

- **finishing-a-development-branch** — `/Users/melbourne/.agents/skills/finishing-a-development-branch` — Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup

- **firebase** — `/Users/melbourne/.agents/skills/firebase` — Firebase gives you a complete backend in minutes - auth, database,

- **firecrawl-scraper** — `/Users/melbourne/.agents/skills/firecrawl-scraper` — Deep web scraping, screenshots, PDF parsing, and website crawling using Firecrawl API. Use when you need deep content extraction from web pages, page interaction is required (clicking, scrolling, etc.), or you want scree

- **firmware-analyst** — `/Users/melbourne/.agents/skills/firmware-analyst` — Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering.

- **fit-scorer** — `/Users/melbourne/.agents/skills/fit-scorer` — Use when the user asks to "score this influencer", "rank these creators for our campaign", or "tell me which influencer is the best fit"; produces the typed STAR Suitability (S) read plus a separately labeled campaign-fi

- **fitness-analyzer** — `/Users/melbourne/.agents/skills/fitness-analyzer` — 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。

- **fix-review** — `/Users/melbourne/.agents/skills/fix-review` — Verify fix commits address audit findings without new bugs

- **fixing-accessibility** — `/Users/melbourne/.agents/skills/fixing-accessibility` — Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding interactive controls, forms, dialogs, or reviewing WCAG compliance.

- **fixing-metadata** — `/Users/melbourne/.agents/skills/fixing-metadata` — Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, JSON-LD structured data, and robots directives. Use when adding or reviewing SEO and social 

- **fixing-motion-performance** — `/Users/melbourne/.agents/skills/fixing-motion-performance` — Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use when animations stutter, transitions jank, or reviewing CSS/JS animation performan

- **floor-plan-generation** — `/Users/melbourne/.agents/skills/floor-plan-generation` — Generate floor plans and architectural layouts using each::sense AI. Create apartment designs, house layouts, office spaces, retail stores, restaurants, and 3D visualizations with furniture arrangements and measurements.

- **flowhunt-skill** — `/Users/melbourne/.agents/skills/flowhunt-skill` — Automation discovery audit skill. Walks through a 5-question workflow intake, then audits Gmail/Calendar/Slack/task trackers to identify automation opportunities. Use when a user wants to discover what processes in their

- **flutter-expert** — `/Users/melbourne/.agents/skills/flutter-expert` — Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment.

- **flyer-design-generation** — `/Users/melbourne/.agents/skills/flyer-design-generation` — Generate professional flyers and leaflets using each::sense AI. Create event flyers, promotional materials, real estate listings, restaurant menus, and more with eye-catching designs optimized for print and digital distr

- **food-database-query** — `/Users/melbourne/.agents/skills/food-database-query` — Food Database Query

- **food-photography-generation** — `/Users/melbourne/.agents/skills/food-photography-generation` — Generate professional food photography using each::sense API for restaurant menus, food delivery apps, recipe blogs, and social media content

- **form-cro** — `/Users/melbourne/.agents/skills/form-cro` — Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote, and checkout forms.

- **fp-async** — `/Users/melbourne/.agents/skills/fp-async` — Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples

- **fp-backend** — `/Users/melbourne/.agents/skills/fp-backend` — Functional programming patterns for Node.js/Deno backend development using fp-ts, ReaderTaskEither, and functional dependency injection

- **fp-data-transforms** — `/Users/melbourne/.agents/skills/fp-data-transforms` — Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access

- **fp-either-ref** — `/Users/melbourne/.agents/skills/fp-either-ref` — Quick reference for Either type. Use when user needs error handling, validation, or operations that can fail with typed errors.

- **fp-errors** — `/Users/melbourne/.agents/skills/fp-errors` — Stop throwing everywhere - handle errors as values using Either and TaskEither for cleaner, more predictable code

- **fp-option-ref** — `/Users/melbourne/.agents/skills/fp-option-ref` — Quick reference for Option type. Use when user needs to handle nullable values, optional data, or wants to avoid null checks.

- **fp-pipe-ref** — `/Users/melbourne/.agents/skills/fp-pipe-ref` — Quick reference for pipe and flow. Use when user needs to chain functions, compose operations, or build data pipelines in fp-ts.

- **fp-pragmatic** — `/Users/melbourne/.agents/skills/fp-pragmatic` — A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead

- **fp-react** — `/Users/melbourne/.agents/skills/fp-react` — Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Works with React 18/19, Next.js 14/15.

- **fp-refactor** — `/Users/melbourne/.agents/skills/fp-refactor` — Comprehensive guide for refactoring imperative TypeScript code to fp-ts functional patterns

- **fp-taskeither-ref** — `/Users/melbourne/.agents/skills/fp-taskeither-ref` — Quick reference for TaskEither. Use when user needs async error handling, API calls, or Promise-based operations that can fail.

- **fp-ts-errors** — `/Users/melbourne/.agents/skills/fp-ts-errors` — Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. Use when implementing error handling patterns with fp-ts.

- **fp-ts-pragmatic** — `/Users/melbourne/.agents/skills/fp-ts-pragmatic` — A practical, jargon-free guide to fp-ts functional programming - the 80/20 approach that gets results without the academic overhead. Use when writing TypeScript with fp-ts library.

- **fp-ts-react** — `/Users/melbourne/.agents/skills/fp-ts-react` — Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Use when building React apps with functional programming patterns. Works with React 18/19, Next.js 14/15.

- **fp-types-ref** — `/Users/melbourne/.agents/skills/fp-types-ref` — Quick reference for fp-ts types. Use when user asks which type to use, needs Option/Either/Task decision help, or wants fp-ts imports.

- **framework-migration-code-migrate** — `/Users/melbourne/.agents/skills/framework-migration-code-migrate` — You are a code migration expert specializing in transitioning codebases between frameworks, languages, versions, and platforms. Generate comprehensive migration plans, automated migration scripts, and

- **framework-migration-deps-upgrade** — `/Users/melbourne/.agents/skills/framework-migration-deps-upgrade` — You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. Plan and execute dependency updates with minimal risk, proper testing, and clear migration pa

- **framework-migration-legacy-modernize** — `/Users/melbourne/.agents/skills/framework-migration-legacy-modernize` — Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling gradual replacement of outdated components while maintaining continuous business operations through ex

- **free-tool-strategy** — `/Users/melbourne/.agents/skills/free-tool-strategy` — You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract organic traffic, and build brand awareness.

- **free-tools** — `/Users/melbourne/.agents/skills/free-tools` — When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also use when the user mentions "engineering as marketing," "free tool," "marketing too

- **freshdesk-automation** — `/Users/melbourne/.agents/skills/freshdesk-automation` — Automate Freshdesk helpdesk operations including tickets, contacts, companies, notes, and replies via Rube MCP (Composio). Always search tools first for current schemas.

- **freshservice-automation** — `/Users/melbourne/.agents/skills/freshservice-automation` — Automate Freshservice ITSM tasks via Rube MCP (Composio): create/update tickets, bulk operations, service requests, and outbound emails. Always search tools first for current schemas.

- **frontend-api-integration-patterns** — `/Users/melbourne/.agents/skills/frontend-api-integration-patterns` — Production-ready patterns for integrating frontend applications with backend APIs, including race condition handling, request cancellation, retry strategies, error normalization, and UI state management.

- **frontend-design** — `/Users/melbourne/.agents/skills/frontend-design` — You are a frontend designer-engineer, not a layout generator.

- **frontend-design-deslop** — `/Users/melbourne/.agents/skills/frontend-design-deslop` — Designs distinctive, non-generic UI — typography, OKLCH color, design tokens (DESIGN.md), layout, components, motion, dark mode, accessibility — for landing pages, SaaS apps, dashboards, ecommerce, decks, docs, portfolio

- **frontend-dev-guidelines** — `/Users/melbourne/.agents/skills/frontend-dev-guidelines` — You are a senior frontend engineer operating under strict architectural and performance standards. Use when creating components or pages, adding new features, or fetching or mutating data.

- **frontend-developer** — `/Users/melbourne/.agents/skills/frontend-developer` — Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture.

- **frontend-mobile-development-component-scaffold** — `/Users/melbourne/.agents/skills/frontend-mobile-development-component-scaffold` — You are a React component architecture expert specializing in scaffolding production-ready, accessible, and performant components. Generate complete component implementations with TypeScript, tests, s

- **frontend-mobile-security-xss-scan** — `/Users/melbourne/.agents/skills/frontend-mobile-security-xss-scan` — You are a frontend security specialist focusing on Cross-Site Scripting (XSS) vulnerability detection and prevention. Analyze React, Vue, Angular, and vanilla JavaScript code to identify injection poi

- **frontend-security-coder** — `/Users/melbourne/.agents/skills/frontend-security-coder` — Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns.

- **frontend-slides** — `/Users/melbourne/.agents/skills/frontend-slides` — Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files.

- **frontend-ui-dark-ts** — `/Users/melbourne/.agents/skills/frontend-ui-dark-ts` — A modern dark-themed React UI system using Tailwind CSS and Framer Motion. Designed for dashboards, admin panels, and data-rich applications with glassmorphism effects and tasteful animations.

- **fsi-compliance-checker** — `/Users/melbourne/.agents/skills/fsi-compliance-checker` — Maps code, architecture, and infrastructure changes to specific control IDs in PCI-DSS v4.0 and MAS TRM (Singapore financial regulator), producing an audit-traceable findings report with per-control remediation.

- **full-output-enforcement** — `/Users/melbourne/.agents/skills/full-output-enforcement` — Use when a task requires exhaustive unabridged output, complete files, or strict prevention of placeholders and skipped code.

- **full-stack-orchestration-full-stack-feature** — `/Users/melbourne/.agents/skills/full-stack-orchestration-full-stack-feature` — Use when working with full stack orchestration full stack feature

- **game-asset-generation** — `/Users/melbourne/.agents/skills/game-asset-generation` — Generate game art assets using each::sense AI. Create 2D sprites, character sprite sheets, seamless textures, UI elements, icons, tilesets, loading screens, logos, and concept art for games.

- **game-development** — `/Users/melbourne/.agents/skills/game-development` — Game development orchestrator. Routes to platform-specific skills based on project needs.

- **gcp-cloud-run** — `/Users/melbourne/.agents/skills/gcp-cloud-run` — Specialized skill for building production-ready serverless

- **gdb-cli** — `/Users/melbourne/.agents/skills/gdb-cli` — GDB debugging assistant for AI agents - analyze core dumps, debug live processes, investigate crashes and deadlocks with source code correlation

- **gdpr-data-handling** — `/Users/melbourne/.agents/skills/gdpr-data-handling` — Practical implementation guide for GDPR-compliant data processing, consent management, and privacy controls.

- **gemini-api-dev** — `/Users/melbourne/.agents/skills/gemini-api-dev` — The Gemini API provides access to Google's most advanced AI models. Key capabilities include:

- **gemini-api-integration** — `/Users/melbourne/.agents/skills/gemini-api-integration` — Use when integrating Google Gemini API into projects. Covers model selection, multimodal inputs, streaming, function calling, and production best practices.

- **gemini-infographic** — `/Users/melbourne/.agents/skills/gemini-infographic` — >

- **geminiignore-finops** — `/Users/melbourne/.agents/skills/geminiignore-finops` — Configure and optimize .geminiignore files for AI context window efficiency and token cost reduction (FinOps).

- **generate-icon** — `/Users/melbourne/.agents/skills/generate-icon` — This skill should be used when the user asks to "generate an icon", "create a favicon", "make an app icon", "create iOS icon", "create Android icon", "generate PWA icons", "make desktop app icon", "create Windows icon", 

- **generate-image** — `/Users/melbourne/.agents/skills/generate-image` — This skill should be used when the user asks to "generate an image", "create a banner", "make artwork", "create an illustration", "generate a logo", "make a graphic", "design a header", "AI art", "img2img", "social share

- **generate-svg** — `/Users/melbourne/.agents/skills/generate-svg` — This skill should be used when the user asks to "generate SVG", "create SVG", "make a logo", "create vector graphics", "generate icon", "make vector illustration", "vectorize image", or needs scalable vector graphics gen

- **generate-video** — `/Users/melbourne/.agents/skills/generate-video` — This skill should be used when the user asks to "generate a video", "create a video", "animate an image", "text to video", "image to video", "make a video clip", "video from image", "bring this image to life", "subject-c

- **generative-illustration** — `/Users/melbourne/.agents/skills/generative-illustration` — This skill should be used when the user asks to "make an animated illustration", "animate an illustration", "make a generative motion piece" / "动态平面", "turn AI-generated art into something that moves", "make a poetic or 

- **geo-content-optimizer** — `/Users/melbourne/.agents/skills/geo-content-optimizer` — Use when the user asks to "optimize for AI citations"; improves citation readiness for ChatGPT, Perplexity, AI Overviews, Gemini, and Claude. Not for structural on-page SEO — use on-page-seo-checker; not for net-new draf

- **geo-fundamentals** — `/Users/melbourne/.agents/skills/geo-fundamentals` — Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity).

- **geoffrey-hinton** — `/Users/melbourne/.agents/skills/geoffrey-hinton` — Agente que simula Geoffrey Hinton — Godfather of Deep Learning, Prêmio Turing 2018, criador do backpropagation e das Deep Belief Networks.

- **gh-review-requests** — `/Users/melbourne/.agents/skills/gh-review-requests` — Fetch unread GitHub notifications for open PRs where review is requested from a specified team or opened by a team member. Use when asked to "find PRs I need to review", "show my review requests", "what needs my review",

- **gha-security-review** — `/Users/melbourne/.agents/skills/gha-security-review` — Find exploitable vulnerabilities in GitHub Actions workflows. Every finding MUST include a concrete exploitation scenario — if you can't build the attack, don't report it.

- **git-advanced-workflows** — `/Users/melbourne/.agents/skills/git-advanced-workflows` — Master advanced Git techniques to maintain clean history, collaborate effectively, and recover from any situation with confidence.

- **git-hooks-automation** — `/Users/melbourne/.agents/skills/git-hooks-automation` — Master Git hooks setup with Husky, lint-staged, pre-commit framework, and commitlint. Automate code quality gates, formatting, linting, and commit message enforcement before code reaches CI.

- **git-pr-review** — `/Users/melbourne/.agents/skills/git-pr-review` — Generate a concise and structured PR description from commit history with minimal token usage

- **git-pr-workflows-git-workflow** — `/Users/melbourne/.agents/skills/git-pr-workflows-git-workflow` — Orchestrate a comprehensive git workflow from code review through PR creation, leveraging specialized agents for quality assurance, testing, and deployment readiness. This workflow implements modern g

- **git-pr-workflows-onboard** — `/Users/melbourne/.agents/skills/git-pr-workflows-onboard` — You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first organizations, technical team integration, and accelerated learning methodologies. You

- **git-pr-workflows-pr-enhance** — `/Users/melbourne/.agents/skills/git-pr-workflows-pr-enhance` — You are a PR optimization expert specializing in creating high-quality pull requests that facilitate efficient code reviews. Generate comprehensive PR descriptions, automate review processes, and ensu

- **git-pushing** — `/Users/melbourne/.agents/skills/git-pushing` — Stage all changes, create a conventional commit, and push to the remote branch. Use when explicitly asks to push changes (\"push this\", \"commit and push\"), mentions saving work to remote (\"save to github\", \"push to

- **github** — `/Users/melbourne/.agents/skills/github` — When the user wants to use GitHub for SEO, parasite SEO, GEO, open source marketing, README optimization, or curated Awesome lists. Also use when the user mentions "GitHub," "GitHub SEO," "GitHub parasite SEO," "GitHub G

- **github-actions-advanced** — `/Users/melbourne/.agents/skills/github-actions-advanced` — >

- **github-actions-templates** — `/Users/melbourne/.agents/skills/github-actions-templates` — Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications.

- **github-automation** — `/Users/melbourne/.agents/skills/github-automation` — Automate GitHub repositories, issues, pull requests, branches, CI/CD, and permissions via Rube MCP (Composio). Manage code workflows, review PRs, search code, and handle deployments programmatically.

- **github-issue-creator** — `/Users/melbourne/.agents/skills/github-issue-creator` — Turn error logs, screenshots, voice notes, and rough bug reports into crisp, developer-ready GitHub issues with repro steps, impact, and evidence.

- **github-workflow-automation** — `/Users/melbourne/.agents/skills/github-workflow-automation` — Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices.

- **gitlab-automation** — `/Users/melbourne/.agents/skills/gitlab-automation` — Automate GitLab project management, issues, merge requests, pipelines, branches, and user operations via Rube MCP (Composio). Always search tools first for current schemas.

- **gitlab-ci-patterns** — `/Users/melbourne/.agents/skills/gitlab-ci-patterns` — Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment.

- **gitops-workflow** — `/Users/melbourne/.agents/skills/gitops-workflow` — Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments.

- **glassmorphism** — `/Users/melbourne/.agents/skills/glassmorphism` — This skill should be used when the user asks to "add a glassmorphism effect", "frosted glass UI", "Apple liquid glass style", "frosted blur card", "translucent glass panel animation", "make a frosted nav bar", "build a g

- **global-chat-agent-discovery** — `/Users/melbourne/.agents/skills/global-chat-agent-discovery` — Discover and search 18K+ MCP servers and AI agents across 6+ registries using Global Chat's cross-protocol directory and MCP server.

- **gmail-automation** — `/Users/melbourne/.agents/skills/gmail-automation` — Lightweight Gmail integration with standalone OAuth authentication. No MCP server required.

- **go-concurrency-patterns** — `/Users/melbourne/.agents/skills/go-concurrency-patterns` — Master Go concurrency with goroutines, channels, sync primitives, and context. Use when building concurrent Go applications, implementing worker pools, or debugging race conditions.

- **go-playwright** — `/Users/melbourne/.agents/skills/go-playwright` — Expert capability for robust, stealthy, and efficient browser automation using Playwright Go.

- **go-rod-master** — `/Users/melbourne/.agents/skills/go-rod-master` — Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth anti-bot-detection patterns.

- **goal-analyzer** — `/Users/melbourne/.agents/skills/goal-analyzer` — 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。

- **godot-4-migration** — `/Users/melbourne/.agents/skills/godot-4-migration` — Specialized guide for migrating Godot 3.x projects to Godot 4 (GDScript 2.0), covering syntax changes, Tweens, and exports.

- **godot-gdscript-patterns** — `/Users/melbourne/.agents/skills/godot-gdscript-patterns` — Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementing game systems, or learning GDScript best practices.

- **golang-pro** — `/Users/melbourne/.agents/skills/golang-pro` — Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices.

- **google-ad-creative-generation** — `/Users/melbourne/.agents/skills/google-ad-creative-generation` — Generate Google Ads creatives using each::sense AI. Create display ads, YouTube thumbnails, Discovery ads, Performance Max assets, and responsive display ads optimized for Google's ad formats and best practices.

- **google-analytics-automation** — `/Users/melbourne/.agents/skills/google-analytics-automation` — Automate Google Analytics tasks via Rube MCP (Composio): run reports, list accounts/properties, funnels, pivots, key events. Always search tools first for current schemas.

- **google-calendar-automation** — `/Users/melbourne/.agents/skills/google-calendar-automation` — Lightweight Google Calendar integration with standalone OAuth authentication. No MCP server required.

- **google-docs-automation** — `/Users/melbourne/.agents/skills/google-docs-automation` — Lightweight Google Docs integration with standalone OAuth authentication. No MCP server required.

- **google-drive-automation** — `/Users/melbourne/.agents/skills/google-drive-automation` — Lightweight Google Drive integration with standalone OAuth authentication. No MCP server required. Full read/write access.

- **google-sheets-automation** — `/Users/melbourne/.agents/skills/google-sheets-automation` — Lightweight Google Sheets integration with standalone OAuth authentication. No MCP server required. Full read/write access.

- **google-slides-automation** — `/Users/melbourne/.agents/skills/google-slides-automation` — Lightweight Google Slides integration with standalone OAuth authentication. No MCP server required. Full read/write access.

- **googlesheets-automation** — `/Users/melbourne/.agents/skills/googlesheets-automation` — Automate Google Sheets operations (read, write, format, filter, manage spreadsheets) via Rube MCP (Composio). Read/write data, manage tabs, apply formatting, and search rows programmatically.

- **gpt-image-v2** — `/Users/melbourne/.agents/skills/gpt-image-v2` — Generate and edit images using OpenAI's GPT Image v2 via EachLabs. Supports text-to-image (gpt-image-v2-text-to-image) and instruction-based editing (gpt-image-v2-edit). Use when the user specifically asks for GPT Image 

- **gpt-taste** — `/Users/melbourne/.agents/skills/gpt-taste` — Use when generating elite GSAP-heavy frontend pages with strict AIDA structure, wide hero typography, and gapless bento grids.

- **grafana-dashboards** — `/Users/melbourne/.agents/skills/grafana-dashboards` — Create and manage production-ready Grafana dashboards for comprehensive system observability.

- **graphic-design** — `/Users/melbourne/.agents/skills/graphic-design` — Professional graphic design principles for digital and print media. Use when creating visual designs, choosing color palettes, typography, layouts, or providing design feedback.

- **graphql** — `/Users/melbourne/.agents/skills/graphql` — GraphQL gives clients exactly the data they need - no more, no

- **graphql-architect** — `/Users/melbourne/.agents/skills/graphql-architect` — Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced caching, and design real-time systems.

- **grill-me** — `/Users/melbourne/.agents/skills/grill-me` — A relentless interview to sharpen a plan or design.

- **grill-with-docs** — `/Users/melbourne/.agents/skills/grill-with-docs` — A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.

- **grilling** — `/Users/melbourne/.agents/skills/grilling` — Interview the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.

- **growth-engine** — `/Users/melbourne/.agents/skills/growth-engine` — Motor de crescimento para produtos digitais -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs e aquisicao organica.

- **grpc-golang** — `/Users/melbourne/.agents/skills/grpc-golang` — Build production-ready gRPC services in Go with mTLS, streaming, and observability. Use when designing Protobuf contracts with Buf or implementing secure service-to-service transport.

- **gsap-web** — `/Users/melbourne/.agents/skills/gsap-web` — This skill should be used when the user asks to "build a scroll animation", "add ScrollTrigger", "pin a section while scrolling", "scrub an animation to scroll", "create a hero timeline", "do a horizontal scroll section"

- **hair-color-changer** — `/Users/melbourne/.agents/skills/hair-color-changer` — Change hair color in photos using each::sense AI. Transform hair to any color including natural shades, fantasy colors, ombre effects, highlights, and more.

- **handoff** — `/Users/melbourne/.agents/skills/handoff` — Compact the current conversation into a handoff document for another agent to pick up.

- **hasdata** — `/Users/melbourne/.agents/skills/hasdata` — Use HasData APIs for web scraping and structured web data extraction.

- **hasdata-cli** — `/Users/melbourne/.agents/skills/hasdata-cli` — Command-line access to search, scraping, and structured web data.

- **haskell-pro** — `/Users/melbourne/.agents/skills/haskell-pro` — Expert Haskell engineer specializing in advanced type systems, pure

- **headline-psychologist** — `/Users/melbourne/.agents/skills/headline-psychologist` — One sentence - what this skill does and when to invoke it

- **health-trend-analyzer** — `/Users/melbourne/.agents/skills/health-trend-analyzer` — 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结果、情绪睡眠），相关性分析，变化检测，以及交互式HTML可视化报告（ECharts图表）。

- **helium-mcp** — `/Users/melbourne/.agents/skills/helium-mcp` — Connect to Helium's MCP server for news research, media bias analysis, balanced perspectives, stock/options data, and semantic meme search across 3.2M+ articles and 5,000+ sources

- **helm-chart-scaffolding** — `/Users/melbourne/.agents/skills/helm-chart-scaffolding` — Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications.

- **helpdesk-automation** — `/Users/melbourne/.agents/skills/helpdesk-automation` — Automate HelpDesk tasks via Rube MCP (Composio): list tickets, manage views, use canned responses, and configure custom fields. Always search tools first for current schemas.

- **hierarchical-agent-memory** — `/Users/melbourne/.agents/skills/hierarchical-agent-memory` — Scoped CLAUDE.md memory system that reduces context token spend. Creates directory-level context files, tracks savings via dashboard, and routes agents to the right sub-context.

- **hig-components-content** — `/Users/melbourne/.agents/skills/hig-components-content` — Apple Human Interface Guidelines for content display components.

- **hig-components-controls** — `/Users/melbourne/.agents/skills/hig-components-controls` — Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

- **hig-components-dialogs** — `/Users/melbourne/.agents/skills/hig-components-dialogs` — Apple HIG guidance for presentation components including alerts, action sheets, popovers, sheets, and digit entry views.

- **hig-components-layout** — `/Users/melbourne/.agents/skills/hig-components-layout` — Apple Human Interface Guidelines for layout and navigation components.

- **hig-components-menus** — `/Users/melbourne/.agents/skills/hig-components-menus` — Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

- **hig-components-search** — `/Users/melbourne/.agents/skills/hig-components-search` — Apple HIG guidance for navigation-related components including search fields, page controls, and path controls.

- **hig-components-status** — `/Users/melbourne/.agents/skills/hig-components-status` — Apple HIG guidance for status and progress UI components including progress indicators, status bars, and activity rings.

- **hig-components-system** — `/Users/melbourne/.agents/skills/hig-components-system` — Apple HIG guidance for system experience components: widgets, live activities, notifications, complications, home screen quick actions, top shelf, watch faces, app clips, and app shortcuts.

- **hig-foundations** — `/Users/melbourne/.agents/skills/hig-foundations` — Apple Human Interface Guidelines design foundations.

- **hig-inputs** — `/Users/melbourne/.agents/skills/hig-inputs` — Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

- **hig-patterns** — `/Users/melbourne/.agents/skills/hig-patterns` — Apple Human Interface Guidelines interaction and UX patterns.

- **hig-platforms** — `/Users/melbourne/.agents/skills/hig-platforms` — Apple Human Interface Guidelines for platform-specific design.

- **hig-project-context** — `/Users/melbourne/.agents/skills/hig-project-context` — Create or update a shared Apple design context document that other HIG skills use to tailor guidance.

- **hig-technologies** — `/Users/melbourne/.agents/skills/hig-technologies` — Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

- **high-end-visual-design** — `/Users/melbourne/.agents/skills/high-end-visual-design` — Use when designing expensive agency-grade interfaces with premium fonts, spatial rhythm, soft depth, and fluid microinteractions.

- **hologram-content-generation** — `/Users/melbourne/.agents/skills/hologram-content-generation` — Generate hologram and 3D display content using each::sense AI. Create holographic product displays, presenters, 3D logos, interactive menus, event content, museum exhibits, retail displays, and trade show holograms.

- **hono** — `/Users/melbourne/.agents/skills/hono` — Build ultra-fast web APIs and full-stack apps with Hono — runs on Cloudflare Workers, Deno, Bun, Node.js, and any WinterCG-compatible runtime.

- **hosted-agents** — `/Users/melbourne/.agents/skills/hosted-agents` — Build background agents in sandboxed environments. Use for hosted coding agents, sandboxed VMs, Modal sandboxes, and remote coding environments.

- **hosted-agents-v2-py** — `/Users/melbourne/.agents/skills/hosted-agents-v2-py` — Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry.

- **hr-people-management** — `/Users/melbourne/.agents/skills/hr-people-management` — Support job design, workforce planning, recruitment, onboarding, objectives, performance reviews, development plans, and structured people decisions.

- **hr-pro** — `/Users/melbourne/.agents/skills/hr-pro` — Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations.

- **html-injection-testing** — `/Users/melbourne/.agents/skills/html-injection-testing` — Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vulnerability enables attackers to modify page appearance, create phishing pages, and 

- **hubspot-automation** — `/Users/melbourne/.agents/skills/hubspot-automation` — Automate HubSpot CRM operations (contacts, companies, deals, tickets, properties) via Rube MCP using Composio integration.

- **hubspot-integration** — `/Users/melbourne/.agents/skills/hubspot-integration` — Expert patterns for HubSpot CRM integration including OAuth

- **hugging-face-cli** — `/Users/melbourne/.agents/skills/hugging-face-cli` — Use the Hugging Face Hub CLI (`hf`) to download, upload, and manage models, datasets, and Spaces.

- **hugging-face-community-evals** — `/Users/melbourne/.agents/skills/hugging-face-community-evals` — Run local evaluations for Hugging Face Hub models with inspect-ai or lighteval.

- **hugging-face-dataset-viewer** — `/Users/melbourne/.agents/skills/hugging-face-dataset-viewer` — Query Hugging Face datasets through the Dataset Viewer API for splits, rows, search, filters, and parquet links.

- **hugging-face-datasets** — `/Users/melbourne/.agents/skills/hugging-face-datasets` — Create and manage datasets on Hugging Face Hub. Supports initializing repos, defining configs/system prompts, streaming row updates, and SQL-based dataset querying/transformation. Designed to work alongside HF MCP server

- **hugging-face-evaluation** — `/Users/melbourne/.agents/skills/hugging-face-evaluation` — Add and manage evaluation results in Hugging Face model cards. Supports extracting eval tables from README content, importing scores from Artificial Analysis API, and running custom model evaluations with vLLM/lighteval.

- **hugging-face-gradio** — `/Users/melbourne/.agents/skills/hugging-face-gradio` — Build or edit Gradio apps, layouts, components, and chat interfaces in Python.

- **hugging-face-jobs** — `/Users/melbourne/.agents/skills/hugging-face-jobs` — Run workloads on Hugging Face Jobs with managed CPUs, GPUs, TPUs, secrets, and Hub persistence.

- **hugging-face-model-trainer** — `/Users/melbourne/.agents/skills/hugging-face-model-trainer` — Train or fine-tune TRL language models on Hugging Face Jobs, including SFT, DPO, GRPO, and GGUF export.

- **hugging-face-paper-publisher** — `/Users/melbourne/.agents/skills/hugging-face-paper-publisher` — Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to models/datasets, claiming authorship, and generating professional markdown-based research articles.

- **hugging-face-papers** — `/Users/melbourne/.agents/skills/hugging-face-papers` — Read and analyze Hugging Face paper pages or arXiv papers with markdown and papers API metadata.

- **hugging-face-tool-builder** — `/Users/melbourne/.agents/skills/hugging-face-tool-builder` — Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping and intermediate processing where helpful. You can access the API directly, as well a

- **hugging-face-trackio** — `/Users/melbourne/.agents/skills/hugging-face-trackio` — Track ML experiments with Trackio using Python logging, alerts, and CLI metric retrieval.

- **hugging-face-vision-trainer** — `/Users/melbourne/.agents/skills/hugging-face-vision-trainer` — Train or fine-tune vision models on Hugging Face Jobs for detection, classification, and SAM or SAM2 segmentation.

- **humaniseur-fr** — `/Users/melbourne/.agents/skills/humaniseur-fr` — Remove AI-writing patterns from French text and inject voice and personality. Use when editing, reviewing, or rewriting French content that reads like ChatGPT or Claude output. Detects and fixes 38 patterns: AI vocabular

- **humanize-chinese** — `/Users/melbourne/.agents/skills/humanize-chinese` — Detect and rewrite AI-like Chinese text with a practical workflow for scoring, humanization, academic AIGC reduction, and style conversion. Use when the user asks to 去AI味, 降AIGC, 去除AI痕迹, 论文降重, 知网检测, 维普检测, humanize chines

- **humanizer-en-asd-ste100** — `/Users/melbourne/.agents/skills/humanizer-en-asd-ste100` — Write or rewrite English into ASD-STE100 Simplified Technical English and strip AI artifacts (decorative emojis, Markdown residue) from technical documentation — maintenance manuals, procedures, medical device instructio

- **hybrid-cloud-architect** — `/Users/melbourne/.agents/skills/hybrid-cloud-architect` — Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware).

- **hybrid-cloud-networking** — `/Users/melbourne/.agents/skills/hybrid-cloud-networking` — Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute.

- **hybrid-search-implementation** — `/Users/melbourne/.agents/skills/hybrid-search-implementation` — Combine vector and keyword search for improved retrieval. Use when implementing RAG systems, building search engines, or when neither approach alone provides sufficient recall.

- **i18n-localization** — `/Users/melbourne/.agents/skills/i18n-localization` — Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support.

- **iconsax-library** — `/Users/melbourne/.agents/skills/iconsax-library` — Extensive icon library and AI-driven icon generation skill for premium UI/UX design.

- **idea-darwin** — `/Users/melbourne/.agents/skills/idea-darwin` — Darwinian idea evolution engine — toss rough ideas onto an evolution island, let them compete, crossbreed, and mutate through structured rounds to surface your strongest concepts.

- **idea-os** — `/Users/melbourne/.agents/skills/idea-os` — Five-phase pipeline (triage → clarify → research → PRD → plan) that turns a raw idea into four linked files: clarifying questions, deep research, a PRD with non-goals and metrics, and a phased execution plan with mermaid

- **identity-mirror** — `/Users/melbourne/.agents/skills/identity-mirror` — One sentence - what this skill does and when to invoke it

- **idor-testing** — `/Users/melbourne/.agents/skills/idor-testing` — Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities in web applications.

- **ii-commons** — `/Users/melbourne/.agents/skills/ii-commons` — Deterministic search across arXiv, PubMed/PMC, and US policy corpora with daily freshness cutoffs.

- **illustration-concept-art** — `/Users/melbourne/.agents/skills/illustration-concept-art` — Create illustration, editorial art, conceptual imagery, stylized scenes, icons, mascots, story visuals, and concept art with controlled style and composition.

- **ilya-sutskever** — `/Users/melbourne/.agents/skills/ilya-sutskever` — Agente que simula Ilya Sutskever — co-fundador da OpenAI, ex-Chief Scientist, fundador da SSI. Use quando quiser perspectivas sobre: AGI safety-first, consciência de IA, scaling laws, deep learning profundo, o episódio d

- **image** — `/Users/melbourne/.agents/skills/image` — When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product mockups, profile banners, listing visuals, or brand assets. Also use when the user mentions 'AI imag

- **image-editing-retouching** — `/Users/melbourne/.agents/skills/image-editing-retouching` — Plan and execute image edits, cleanup, retouching, object removal/addition, background changes, relighting, reframing, restoration, and targeted visual corrections.

- **image-generation-orchestrator** — `/Users/melbourne/.agents/skills/image-generation-orchestrator` — Execute or route image generation and editing through available image tools, with provider fallback, file handling, safe credentials, and reproducible settings.

- **image-generator** — `/Users/melbourne/.agents/skills/image-generator` — Generate and edit images using Gemini's Nano Banana Pro model (gemini-3-pro-image-preview). Use this skill when the user asks you to generate images, create visuals, edit photos, create logos, generate product mockups, o

- **image-outpainting** — `/Users/melbourne/.agents/skills/image-outpainting` — Extend and expand images beyond their original boundaries using each::sense AI. Create panoramic views, convert aspect ratios, add backgrounds, and uncrop photos intelligently.

- **image-prompt-engineering** — `/Users/melbourne/.agents/skills/image-prompt-engineering` — Turn a visual brief into precise model-ready image prompts covering subject, composition, camera, lighting, environment, materials, styling, constraints, and output.

- **image-relighting** — `/Users/melbourne/.agents/skills/image-relighting` — Relight photos and images using each::sense AI. Transform lighting conditions, add studio lighting, golden hour effects, dramatic shadows, neon glows, and match lighting to any environment.

- **image-studio** — `/Users/melbourne/.agents/skills/image-studio` — Studio de geracao de imagens inteligente — roteamento automatico entre ai-studio-image (fotos humanizadas/influencer) e stability-ai (arte/ ilustracao/edicao). Detecta o tipo de imagem solicitada e escolhe o modelo ideal

- **image-to-video** — `/Users/melbourne/.agents/skills/image-to-video` — Transform static images into dynamic videos using each::sense AI. Create animations, Ken Burns effects, cinemagraphs, product showcases, and motion graphics from still photos.

- **image-upscaling** — `/Users/melbourne/.agents/skills/image-upscaling` — Upscale images using each::sense AI. Enhance resolution for web, print, large format displays, with options for face enhancement, noise reduction, and AI art optimization.

- **imagen** — `/Users/melbourne/.agents/skills/imagen` — AI image generation skill powered by Google Gemini, enabling seamless visual content creation for UI placeholders, documentation, and design assets.

- **improve-codebase-architecture** — `/Users/melbourne/.agents/skills/improve-codebase-architecture` — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.

- **inbox-action-management** — `/Users/melbourne/.agents/skills/inbox-action-management` — Triage management email, chat, notes, and requests into actions, decisions, delegations, waiting items, calendar needs, risks, and follow-ups.

- **inbox-placement-monitor** — `/Users/melbourne/.agents/skills/inbox-placement-monitor` — Use when the user asks to "track where my emails are actually landing after I send", "read my seed-list inbox vs spam vs promotions results", "trend my Gmail Postmaster / Microsoft SNDS reputation", or "did placement dro

- **incident-responder** — `/Users/melbourne/.agents/skills/incident-responder` — Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management.

- **incident-response-incident-response** — `/Users/melbourne/.agents/skills/incident-response-incident-response` — Use when working with incident response incident response

- **incident-response-smart-fix** — `/Users/melbourne/.agents/skills/incident-response-smart-fix` — [Extended thinking: This workflow implements a sophisticated debugging and resolution pipeline that leverages AI-assisted debugging tools and observability platforms to systematically diagnose and res

- **incident-runbook-templates** — `/Users/melbourne/.agents/skills/incident-runbook-templates` — Production-ready templates for incident response runbooks covering detection, triage, mitigation, resolution, and communication.

- **indexing-issue-auditor** — `/Users/melbourne/.agents/skills/indexing-issue-auditor` — High-level technical SEO and site architecture auditor. Invoke to scan local or live environments for indexing, crawl budget, and structural errors.

- **industrial-brutalist-ui** — `/Users/melbourne/.agents/skills/industrial-brutalist-ui` — Use when creating raw industrial or tactical telemetry UIs with rigid grids, stark typography, CRT effects, and high-density data.

- **infinite-gratitude** — `/Users/melbourne/.agents/skills/infinite-gratitude` — Multi-agent research skill for parallel research execution (10 agents, battle-tested with real case studies).

- **influence-and-negotiation** — `/Users/melbourne/.agents/skills/influence-and-negotiation` — Influence and negotiation toolkit for any interaction needing another person's agreement, even when the user never says 'negotiation'. Covers B2B sales, salary reviews and raise asks, collective bargaining and unions, ha

- **influencer-discovery** — `/Users/melbourne/.agents/skills/influencer-discovery` — Use when the user asks to "find influencers", "build an influencer list", or "discover creators in [niche]"; produces a multi-platform candidate pool, per-influencer evidence profiles, authenticity red-flag screening, an

- **influencer-marketing** — `/Users/melbourne/.agents/skills/influencer-marketing` — When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals, briefing creators, disclosure compliance, and measuring ROI. Also use

- **infographic** — `/Users/melbourne/.agents/skills/infographic` — Create template-based infographics with space-separated key-value syntax (NOT YAML). Best for KPI dashboards, timelines, roadmaps, SWOT analysis, funnels, comparisons, and org charts with quick visual impact.

- **infographic-creator** — `/Users/melbourne/.agents/skills/infographic-creator` — Create beautiful infographics based on given text content. Use when users request to create infographics.

- **infographic-generation** — `/Users/melbourne/.agents/skills/infographic-generation` — Generate professional infographics using each::sense AI. Create statistical, process, comparison, timeline, list, geographic, hierarchical, resume, report, and social media infographics optimized for visual communication

- **infographic-outline-creator** — `/Users/melbourne/.agents/skills/infographic-outline-creator` — |

- **ingest-youtube** — `/Users/melbourne/.agents/skills/ingest-youtube` — Pull a YouTube video transcript into a queryable markdown vault with yt-dlp subtitle discovery, VTT cleanup, metadata frontmatter, and capture-seed stubs.

- **inngest** — `/Users/melbourne/.agents/skills/inngest` — Inngest expert for serverless-first background jobs, event-driven

- **instagram** — `/Users/melbourne/.agents/skills/instagram` — Integracao completa com Instagram via Graph API. Publicacao, analytics, comentarios, DMs, hashtags, agendamento, templates e gestao de contas Business/Creator.

- **instagram-automation** — `/Users/melbourne/.agents/skills/instagram-automation` — Automate Instagram tasks via Rube MCP (Composio): create posts, carousels, manage media, get insights, and publishing limits. Always search tools first for current schemas.

- **instagram-content-generation** — `/Users/melbourne/.agents/skills/instagram-content-generation` — Generate Instagram content using each::sense AI. Create feed posts, stories, reels covers, carousels, quote graphics, and brand visuals optimized for Instagram's formats and engagement best practices.

- **interactive-portfolio** — `/Users/melbourne/.agents/skills/interactive-portfolio` — Expert in building portfolios that actually land jobs and clients -

- **intercom-automation** — `/Users/melbourne/.agents/skills/intercom-automation` — Automate Intercom tasks via Rube MCP (Composio): conversations, contacts, companies, segments, admins. Always search tools first for current schemas.

- **interior-design-visualization** — `/Users/melbourne/.agents/skills/interior-design-visualization` — Visualize interior design transformations using each::sense AI. Redesign rooms, change styles, update color schemes, and preview renovations from photos of your existing spaces.

- **internal-comms** — `/Users/melbourne/.agents/skills/internal-comms` — Write internal communications such as status reports, leadership updates, 3P updates, newsletters, FAQs, incident reports, and project updates using repeatable internal formats.

- **internal-comms-anthropic** — `/Users/melbourne/.agents/skills/internal-comms-anthropic` — To write internal communications, use this skill for:

- **internal-comms-community** — `/Users/melbourne/.agents/skills/internal-comms-community` — To write internal communications, use this skill for:

- **interview-coach** — `/Users/melbourne/.agents/skills/interview-coach` — Full job search coaching system — JD decoding, resume, storybank, mock interviews, transcript analysis, comp negotiation. 23 commands, persistent state.

- **invariant-guard** — `/Users/melbourne/.agents/skills/invariant-guard` — Correctness-first: forces writing the function contract, loop invariant, termination argument, and edge cases BEFORE code. Catches Boyer-Moore, leftmost binary search, QuickSelect traps.

- **inventory-demand-planning** — `/Users/melbourne/.agents/skills/inventory-demand-planning` — Codified expertise for demand forecasting, safety stock optimisation, replenishment planning, and promotional lift estimation at multi-location retailers.

- **invoice-generation** — `/Users/melbourne/.agents/skills/invoice-generation` — Generate professional invoices, receipts, quotes, and financial documents using each::sense AI. Create branded business documents with automatic calculations, multi-currency support, and customizable layouts.

- **ios-debugger-agent** — `/Users/melbourne/.agents/skills/ios-debugger-agent` — Debug the current iOS project on a booted simulator with XcodeBuildMCP.

- **ios-developer** — `/Users/melbourne/.agents/skills/ios-developer` — Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store optimization.

- **issues** — `/Users/melbourne/.agents/skills/issues` — Interact with GitHub issues - create, list, and view issues.

- **istio-traffic-management** — `/Users/melbourne/.agents/skills/istio-traffic-management` — Comprehensive guide to Istio traffic management for production service mesh deployments.

- **it-manager-hospital** — `/Users/melbourne/.agents/skills/it-manager-hospital` — World-class Hospital IT Management Advisor specializing in clinical safety, digital maturity (HIMSS/ONA/JCI), and HIS/PEP ecosystems.

- **it-manager-pro** — `/Users/melbourne/.agents/skills/it-manager-pro` — Elite IT Management Advisor specializing in data-driven strategy, executive communication, and human-centric leadership for the 2026 digital era.

- **iterate-pr** — `/Users/melbourne/.agents/skills/iterate-pr` — Iterate on a PR until CI passes. Use when you need to fix CI failures, address review feedback, or continuously push fixes until all checks are green. Automates the feedback-fix-push-wait cycle.

- **itil-expert** — `/Users/melbourne/.agents/skills/itil-expert` — Expert advisor for ITIL 4 and ITIL 5 (2026 digital product paradigm), specialized in AI-native governance, sustainability, and value co-creation.

- **java-pro** — `/Users/melbourne/.agents/skills/java-pro` — Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem including GraalVM, Project Loom, and cloud-native patterns.

- **javascript-mastery** — `/Users/melbourne/.agents/skills/javascript-mastery` — 33+ essential JavaScript concepts every developer should know, inspired by [33-js-concepts](https://github.com/leonardomso/33-js-concepts).

- **javascript-pro** — `/Users/melbourne/.agents/skills/javascript-pro` — Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility.

- **javascript-testing-patterns** — `/Users/melbourne/.agents/skills/javascript-testing-patterns` — Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern testing frameworks and best practices.

- **javascript-typescript-typescript-scaffold** — `/Users/melbourne/.agents/skills/javascript-typescript-typescript-scaffold` — You are a TypeScript project architecture expert specializing in scaffolding production-ready Node.js and frontend applications. Generate complete project structures with modern tooling (pnpm, Vite, N

- **jira-automation** — `/Users/melbourne/.agents/skills/jira-automation` — Automate Jira tasks via Rube MCP (Composio): issues, projects, sprints, boards, comments, users. Always search tools first for current schemas.

- **jobgpt** — `/Users/melbourne/.agents/skills/jobgpt` — Job search automation, auto apply, resume generation, application tracking, salary intelligence, and recruiter outreach using the JobGPT MCP server.

- **jobs-to-be-done-analyst** — `/Users/melbourne/.agents/skills/jobs-to-be-done-analyst` — One sentence - what this skill does and when to invoke it

- **jq** — `/Users/melbourne/.agents/skills/jq` — Expert jq usage for JSON querying, filtering, transformation, and pipeline integration. Practical patterns for real shell workflows.

- **json-canvas** — `/Users/melbourne/.agents/skills/json-canvas` — Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating visual canvases, mind maps, flowcharts, or when the user mentions Canvas files in Obsi

- **julia-pro** — `/Users/melbourne/.agents/skills/julia-pro` — Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices.

- **junta-leiloeiros** — `/Users/melbourne/.agents/skills/junta-leiloeiros` — Coleta e consulta dados de leiloeiros oficiais de todas as 27 Juntas Comerciais do Brasil. Scraper multi-UF, banco SQLite, API FastAPI e exportacao CSV/JSON.

- **k6-load-testing** — `/Users/melbourne/.agents/skills/k6-load-testing` — Comprehensive k6 load testing skill for API, browser, and scalability testing. Write realistic load scenarios, analyze results, and integrate with CI/CD.

- **k8s-manifest-generator** — `/Users/melbourne/.agents/skills/k8s-manifest-generator` — Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims.

- **k8s-security-policies** — `/Users/melbourne/.agents/skills/k8s-security-policies` — Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes.

- **kaizen** — `/Users/melbourne/.agents/skills/kaizen` — Guide for continuous improvement, error proofing, and standardization. Use this skill when the user wants to improve code quality, refactor, or discuss process improvements.

- **kanban-markdown** — `/Users/melbourne/.agents/skills/kanban-markdown` — Create, read, update, move, and manage kanban board feature files backed by markdown with YAML frontmatter. Use when working with kanban boards, task/feature tracking, `.devtool/features/` directories, feature files with

- **keyword-extractor** — `/Users/melbourne/.agents/skills/keyword-extractor` — >

- **keyword-research** — `/Users/melbourne/.agents/skills/keyword-research` — Use when the user asks to "find keywords", "挖词", or "搜什么词"; prioritizes search volume, keyword difficulty, intent, and topic clusters from provided or connected data. Not for competitor-relative coverage gaps — use conte

- **kinetic-typography** — `/Users/melbourne/.agents/skills/kinetic-typography` — This skill should be used when the user asks to "animate a headline", "make a kinetic typography video", "do a split-text reveal", "stagger text by character/word/line", "make a lyric or caption video", "animate a variab

- **klaviyo-automation** — `/Users/melbourne/.agents/skills/klaviyo-automation` — Automate Klaviyo tasks via Rube MCP (Composio): manage email/SMS campaigns, inspect campaign messages, track tags, and monitor send jobs. Always search tools first for current schemas.

- **kotler-macro-analyzer** — `/Users/melbourne/.agents/skills/kotler-macro-analyzer` — Professional PESTEL/SWOT analysis agent based on Kotler's methodology for strategic market audits.

- **kotlin-coroutines-expert** — `/Users/melbourne/.agents/skills/kotlin-coroutines-expert` — Expert patterns for Kotlin Coroutines and Flow, covering structured concurrency, error handling, and testing.

- **kpi-dashboard-design** — `/Users/melbourne/.agents/skills/kpi-dashboard-design` — Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions.

- **kpi-performance** — `/Users/melbourne/.agents/skills/kpi-performance` — Design and analyze KPIs, targets, baselines, trends, variances, drivers, leading indicators, corrective actions, and performance review scorecards.

- **kubernetes-architect** — `/Users/melbourne/.agents/skills/kubernetes-architect` — Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration.

- **kubernetes-deployment** — `/Users/melbourne/.agents/skills/kubernetes-deployment` — Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations.

- **kubestellar-console** — `/Users/melbourne/.agents/skills/kubestellar-console` — Multi-cluster Kubernetes dashboard with AI-powered operations via MCP server and 10+ built-in agent skills

- **lambda-lang** — `/Users/melbourne/.agents/skills/lambda-lang` — Native agent-to-agent language for compact multi-agent messaging. A shared tongue agents speak directly, not a translation layer. 340+ atoms across 7 domains; 3x smaller than natural language.

- **lambdatest-agent-skills** — `/Users/melbourne/.agents/skills/lambdatest-agent-skills` — Production-grade test automation skills for 46 frameworks across E2E, unit, mobile, BDD, visual, and cloud testing in 15+ languages.

- **landing-experience-checker** — `/Users/melbourne/.agents/skills/landing-experience-checker` — Use when the user asks to "pre-launch check the landing page", "run a Quality-Score preflight", or "verify ad-to-page message match before launch"; produces an ad↔page continuity report — message-match gaps, above-the-fo

- **landing-optimizer** — `/Users/melbourne/.agents/skills/landing-optimizer` — Use when the user asks to "optimize our landing page for influencer traffic", "fix our promo-code landing page", or "improve conversion from a creator campaign"; produces a message-match audit, page-structure and social-

- **landing-page-generator** — `/Users/melbourne/.agents/skills/landing-page-generator` — Generates high-converting Next.js/React landing pages with Tailwind CSS. Uses PAS, AIDA, and BAB frameworks for optimized copy/components (Heroes, Features, Pricing). Focuses on Core Web Vitals/SEO.

- **langchain-architecture** — `/Users/melbourne/.agents/skills/langchain-architecture` — Master the LangChain framework for building sophisticated LLM applications with agents, chains, memory, and tool integration.

- **langfuse** — `/Users/melbourne/.agents/skills/langfuse` — Expert in Langfuse - the open-source LLM observability platform.

- **langgraph** — `/Users/melbourne/.agents/skills/langgraph` — Expert in LangGraph - the production-grade framework for building

- **laravel-expert** — `/Users/melbourne/.agents/skills/laravel-expert` — Senior Laravel Engineer role for production-grade, maintainable, and idiomatic Laravel solutions. Focuses on clean architecture, security, performance, and modern standards (Laravel 10/11+).

- **laravel-security-audit** — `/Users/melbourne/.agents/skills/laravel-security-audit` — Security auditor for Laravel applications. Analyzes code for vulnerabilities, misconfigurations, and insecure practices using OWASP standards and Laravel security best practices.

- **last30days** — `/Users/melbourne/.agents/skills/last30days` — Research a topic from the last 30 days on Reddit + X + Web, become an expert, and write copy-paste-ready prompts for the user's target tool.

- **latex-paper-conversion** — `/Users/melbourne/.agents/skills/latex-paper-conversion` — This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer, IPOL) to another format (e.g., MDPI, IEEE, Nature). It automates extraction, injection, fixing formattin

- **launch** — `/Users/melbourne/.agents/skills/launch` — When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product Hunt,' 'feature release,' 'announcement,' 'go-to-market,' 'beta launch,' 'early 

- **launch-asset-packager** — `/Users/melbourne/.agents/skills/launch-asset-packager` — Use when the user asks to "package the launch assets", "build a press kit", or "prep the store listing and go-live checklist"; produces a tier-scoped launch asset manifest with production status — a press kit spec (facts

- **launch-day-conductor** — `/Users/melbourne/.agents/skills/launch-day-conductor` — Use when the user asks to "run my launch day", "build a launch day runbook / war room", or "decide CONTINUE or ROLLBACK after the push"; produces a pre-conditions gate check (launch-readiness-auditor SHIP verdict + the a

- **launch-feedback-synthesizer** — `/Users/melbourne/.agents/skills/launch-feedback-synthesizer` — Use when the user asks to "triage launch feedback", "cluster reviews, comments, and board posts into themes", or "set up a you asked, we shipped loop"; produces a feedback theme digest (frequency, severity, representativ

- **launch-monitor** — `/Users/melbourne/.agents/skills/launch-monitor` — Use when the user asks to "monitor my launch", "track our Product Hunt / Hacker News ranking", or "watch the launch window"; runs the T-0 to T+30 window watch — pre-launch instrumentation verification (UTM/event checks, 

- **launch-readiness-auditor** — `/Users/melbourne/.agents/skills/launch-readiness-auditor` — Use when the user asks to "audit our launch plan", "are we ready to launch", or evaluate launch execution/outcomes; runs one typed RAMP preflight, execution, or outcome profile without mixing time horizons. Not for recor

- **launch-registry** — `/Users/melbourne/.agents/skills/launch-registry` — Use when the user asks to "log this launch", query a launch date/embargo, record a stage transition, or update submissions/outcomes; curates launch facts through the append-only launches event stream with optimistic revi

- **launch-retro-analyzer** — `/Users/melbourne/.agents/skills/launch-retro-analyzer` — Use when the user asks to "run a launch retro / post-mortem", "compare launch results vs targets by channel", or "decide what to keep or kill for the next launch"; produces a structured D1/W1/M1 retrospective — a per-cha

- **launch-strategy** — `/Users/melbourne/.agents/skills/launch-strategy` — You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into users.

- **launch-tier-planner** — `/Users/melbourne/.agents/skills/launch-tier-planner` — Use when the user asks to "plan my launch tier", "how big should this launch be", or "build a launch risk register with kill criteria"; produces a tier decision (Tier 1 flagship all-channel / Tier 2 targeted / Tier 3 cha

- **launch-window-planner** — `/Users/melbourne/.agents/skills/launch-window-planner` — Use when the user asks to "pick a launch date", "plan the launch window", or "set the embargo and lift time"; produces a candidate-window comparison table (conflict / tailwind / risk per window) built from industry-event

- **lead-magnets** — `/Users/melbourne/.agents/skills/lead-magnets` — When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the user mentions "lead magnet," "gated content," "content upgrade," "downloadable," "ebook," "cheat shee

- **learn** — `/Users/melbourne/.agents/skills/learn` — Help a user learn a topic through adaptive tutoring, lesson planning, practice, retrieval checks, explanations, study guides, or exercises. Use when the user asks to learn, understand, practice, drill, review, study, or 

- **legacy-modernizer** — `/Users/melbourne/.agents/skills/legacy-modernizer` — Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility.

- **legal-advisor** — `/Users/melbourne/.agents/skills/legal-advisor` — Draft privacy policies, terms of service, disclaimers, and legal notices. Creates GDPR-compliant texts, cookie policies, and data processing agreements.

- **legal-hold** — `/Users/melbourne/.agents/skills/legal-hold` — Issue, refresh, release, or report on legal holds — drafts the hold notice as .docx, updates legal_hold fields in _log.yaml, and calendars the next refresh. Use when the user says "issue a hold", "refresh hold", "release

- **legal-response** — `/Users/melbourne/.agents/skills/legal-response` — Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. Use when responding to data subject requests, litigation hold

- **legal-risk-assessment** — `/Users/melbourne/.agents/skills/legal-risk-assessment` — Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matt

- **legal-writing** — `/Users/melbourne/.agents/skills/legal-writing` — >

- **leiloeiro-avaliacao** — `/Users/melbourne/.agents/skills/leiloeiro-avaliacao` — Avaliacao pericial de imoveis em leilao. Valor de mercado, liquidacao forcada, ABNT NBR 14653, metodos comparativo/renda/custo, CUB e margem de seguranca.

- **leiloeiro-edital** — `/Users/melbourne/.agents/skills/leiloeiro-edital` — Analise e auditoria de editais de leilao judicial e extrajudicial. Riscos ocultos, clausulas perigosas, debitos, ocupante e classificacao da oportunidade.

- **leiloeiro-ia** — `/Users/melbourne/.agents/skills/leiloeiro-ia` — Especialista em leiloes judiciais e extrajudiciais de imoveis. Analise juridica, pericial e de mercado integrada. Orquestra os 5 modulos especializados.

- **leiloeiro-juridico** — `/Users/melbourne/.agents/skills/leiloeiro-juridico` — Analise juridica de leiloes: nulidades, bem de familia, alienacao fiduciaria, CPC arts 829-903, Lei 9514/97, onus reais, embargos e jurisprudencia.

- **leiloeiro-mercado** — `/Users/melbourne/.agents/skills/leiloeiro-mercado` — Analise de mercado imobiliario para leiloes. Liquidez, desagio tipico, ROI, estrategias de saida (flip/reforma/renda), Selic 2025 e benchmark CDI/FII.

- **leiloeiro-risco** — `/Users/melbourne/.agents/skills/leiloeiro-risco` — Analise de risco em leiloes de imoveis. Score 36 pontos, riscos juridicos/financeiros/operacionais, stress test 4 cenarios e ROI ponderado por risco.

- **lemmaly** — `/Users/melbourne/.agents/skills/lemmaly` — Algorithm-first discipline: state Big-O, data structure, and algorithm family BEFORE writing loops, queries, or recursion. Catches O(n^2), N+1, and brute-force defaults.

- **lesson-generator** — `/Users/melbourne/.agents/skills/lesson-generator` — Build compact, standalone multi-lesson course artifacts with lesson navigation, objectives, flashcards, quizzes, and source links.

- **lex** — `/Users/melbourne/.agents/skills/lex` — Centralized 'Truth Engine' for cross-jurisdictional legal context (US, EU, CA) and contract scaffolding.

- **lightning-architecture-review** — `/Users/melbourne/.agents/skills/lightning-architecture-review` — Review Bitcoin Lightning Network protocol designs, compare channel factory approaches, and analyze Layer 2 scaling tradeoffs. Covers trust models, on-chain footprint, consensus requirements, HTLC/PTLC compatibility, live

- **lightning-channel-factories** — `/Users/melbourne/.agents/skills/lightning-channel-factories` — Technical reference on Lightning Network channel factories, multi-party channels, LSP architectures, and Bitcoin Layer 2 scaling without soft forks. Covers Decker-Wattenhofer, timeout trees, MuSig2 key aggregation, HTLC/

- **lightning-factory-explainer** — `/Users/melbourne/.agents/skills/lightning-factory-explainer` — Explain Bitcoin Lightning channel factories and the SuperScalar protocol — scalable Lightning onboarding using shared UTXOs, Decker-Wattenhofer trees, timeout-signature trees, MuSig2, and Taproot. No soft fork required.

- **linear-automation** — `/Users/melbourne/.agents/skills/linear-automation` — Automate Linear tasks via Rube MCP (Composio): issues, projects, cycles, teams, labels. Always search tools first for current schemas.

- **linear-claude-skill** — `/Users/melbourne/.agents/skills/linear-claude-skill` — Manage Linear issues, projects, and teams

- **linkedin-automation** — `/Users/melbourne/.agents/skills/linkedin-automation` — Automate LinkedIn tasks via Rube MCP (Composio): create posts, manage profile, company info, comments, and image uploads. Always search tools first for current schemas.

- **linkedin-cli** — `/Users/melbourne/.agents/skills/linkedin-cli` — Use when automating LinkedIn via CLI: fetch profiles, search people/companies, send messages, manage connections, create posts, and Sales Navigator.

- **linkedin-content-generation** — `/Users/melbourne/.agents/skills/linkedin-content-generation` — Generate LinkedIn content graphics using each::sense AI. Create professional post images, article headers, company banners, event promotions, thought leadership visuals, and personal brand content optimized for LinkedIn'

- **linkedin-content-generator** — `/Users/melbourne/.agents/skills/linkedin-content-generator` — AI-powered LinkedIn content suite: generate posts, carousels, newsletters, and 30-day calendars with niche-specific SEO rules and a reinforcement-learning personal memory system.

- **linkedin-ghostwriting** — `/Users/melbourne/.agents/skills/linkedin-ghostwriting` — B2B LinkedIn ghostwriting — hooks, post structures, and copywriting frameworks for conversion-focused posts. Use when the user wants to write LinkedIn content, create ghostwritten posts, ghostwrite for a founder or execu

- **linkedin-posts** — `/Users/melbourne/.agents/skills/linkedin-posts` — When the user wants to create LinkedIn post copy or optimize for LinkedIn. Also use when the user mentions "LinkedIn post," "LinkedIn article," "professional post," "post to LinkedIn," "LinkedIn content," "LinkedIn copy,

- **linkedin-profile-optimizer** — `/Users/melbourne/.agents/skills/linkedin-profile-optimizer` — High-intent expert for LinkedIn profile checks, authority building, and SEO optimization. Invoke to audit, rewrite, and enhance profiles for top 1% positioning.

- **linkerd-patterns** — `/Users/melbourne/.agents/skills/linkerd-patterns` — Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes.

- **lint-and-validate** — `/Users/melbourne/.agents/skills/lint-and-validate` — MANDATORY: Run appropriate validation tools after EVERY code change. Do not finish a task until the code is error-free.

- **linux-privilege-escalation** — `/Users/melbourne/.agents/skills/linux-privilege-escalation` — Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and security weaknesses that allow elevation from low-privilege user access to root-lev

- **linux-shell-scripting** — `/Users/melbourne/.agents/skills/linux-shell-scripting` — Provide production-ready shell script templates for common Linux system administration tasks including backups, monitoring, user management, log analysis, and automation. These scripts serve as building blocks for securi

- **linux-troubleshooting** — `/Users/melbourne/.agents/skills/linux-troubleshooting` — Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures.

- **list-growth-designer** — `/Users/melbourne/.agents/skills/list-growth-designer` — Use when the user asks to "grow my email list", "design a lead magnet / signup incentive", "set up double opt-in", or "plan a referral / recommendation loop"; produces a list-growth plan — acquisition channels, lead-magn

- **list-hygiene-monitor** — `/Users/melbourne/.agents/skills/list-hygiene-monitor` — Use when the user asks to "watch my list health over time", "flag decaying / unengaged subscribers on a schedule", "why is my open rate drifting down / bounces creeping up", or "build me a re-permission and prune worklis

- **list-segment-builder** — `/Users/melbourne/.agents/skills/list-segment-builder` — Use when the user asks to "build email segments from my list", "make engaged / lapsed / RFM segments", "set up cart-abandoner or lifecycle-stage audiences", or "build a suppression list of unsubscribes and bounces"; turn

- **llm-app-patterns** — `/Users/melbourne/.agents/skills/llm-app-patterns` — Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices.

- **llm-application-dev-ai-assistant** — `/Users/melbourne/.agents/skills/llm-application-dev-ai-assistant` — You are an AI assistant development expert specializing in creating intelligent conversational interfaces, chatbots, and AI-powered applications. Design comprehensive AI assistant solutions with natur

- **llm-application-dev-langchain-agent** — `/Users/melbourne/.agents/skills/llm-application-dev-langchain-agent` — You are an expert LangChain agent developer specializing in production-grade AI systems using LangChain 0.1+ and LangGraph.

- **llm-application-dev-prompt-optimize** — `/Users/melbourne/.agents/skills/llm-application-dev-prompt-optimize` — You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques including constitutional AI, chain-of-thought reasoning, and model-specific optimizati

- **llm-council** — `/Users/melbourne/.agents/skills/llm-council` — Run Fireworks-hosted open-weight model councils that compare responses and synthesize a final answer.

- **llm-evaluation** — `/Users/melbourne/.agents/skills/llm-evaluation` — Master comprehensive evaluation strategies for LLM applications, from automated metrics to human evaluation and A/B testing.

- **llm-ops** — `/Users/melbourne/.agents/skills/llm-ops` — LLM Operations -- RAG, embeddings, vector databases, fine-tuning, prompt engineering avancado, custos de LLM, evals de qualidade e arquiteturas de IA para producao.

- **llm-prompt-optimizer** — `/Users/melbourne/.agents/skills/llm-prompt-optimizer` — Use when improving prompts for any LLM. Applies proven prompt engineering techniques to boost output quality, reduce hallucinations, and cut token usage.

- **llm-structured-output** — `/Users/melbourne/.agents/skills/llm-structured-output` — >

- **local-legal-seo-audit** — `/Users/melbourne/.agents/skills/local-legal-seo-audit` — Audit and improve local SEO for law firms, attorneys, forensic experts and legal/professional services sites with local presence, focusing on GBP, directories, E-E-A-T and practice/location pages.

- **local-llm-expert** — `/Users/melbourne/.agents/skills/local-llm-expert` — Master local LLM inference, model selection, VRAM optimization, and local deployment using Ollama, llama.cpp, vLLM, and LM Studio. Expert in quantization formats (GGUF, EXL2) and local AI privacy.

- **local-seo** — `/Users/melbourne/.agents/skills/local-seo` — When the user wants to optimize for local search, set up Google Business Profile, or build local citations. Also use when the user mentions "local SEO," "Google Business Profile," "Google Maps," "NAP," "citations," "loca

- **logic-lens** — `/Users/melbourne/.agents/skills/logic-lens` — AI-powered Claude Code skill that performs deep code review using formal logic and reasoning frameworks to detect bugs, anti-patterns, and security risks beyond what linters catch.

- **logistics-exception-management** — `/Users/melbourne/.agents/skills/logistics-exception-management` — Codified expertise for handling freight exceptions, shipment delays, damages, losses, and carrier disputes. Informed by logistics professionals with 15+ years operational experience.

- **logo-animation** — `/Users/melbourne/.agents/skills/logo-animation` — This skill should be used when the user asks to "animate our logo", "make a logo intro/stinger", "build a brand reveal", "create an app splash animation", "loop a loader logo", "draw on our SVG mark", "morph an icon into

- **logo-generation** — `/Users/melbourne/.agents/skills/logo-generation` — Generate professional logos using each::sense AI. Create wordmarks, icon logos, combination marks, monograms, mascots, emblems, and abstract logos for brands, startups, and businesses.

- **loki-mode** — `/Users/melbourne/.agents/skills/loki-mode` — Version 2.35.0 | PRD to Production | Zero Human Intervention > Research-enhanced: OpenAI SDK, DeepMind, Anthropic, AWS Bedrock, Agent SDK, HN Production (2025)

- **longbridge** — `/Users/melbourne/.agents/skills/longbridge` — 125+ agent skills for Longbridge Securities — real-time quotes, charts, fundamentals, portfolio analysis, options, and more for HK/US/A-share/SG markets. Trilingual: Simplified Chinese, Traditional Chinese, English.

- **lookdev** — `/Users/melbourne/.agents/skills/lookdev` — Human-in-the-loop web studio to tune AI-generated output by eye. Stand up a local interactive studio (sliders, pickers, drag handles) or an inline edit/highlight/comment annotation studio for prose & media, instead of gu

- **lookdev-auto** — `/Users/melbourne/.agents/skills/lookdev-auto` — Automated visual tuning: a vision or video model rates rendered variants in a loop. Render several labeled variants into one artifact, ask the model to rate them and suggest better values, render the suggestions, ask it 

- **loop-library** — `/Users/melbourne/.agents/skills/loop-library` — Find, compare, adapt, and design bounded AI-agent feedback loops with explicit checks, stop rules, guardrails, and handoffs.

- **loss-aversion-designer** — `/Users/melbourne/.agents/skills/loss-aversion-designer` — One sentence - what this skill does and when to invoke it

- **lottie-animation** — `/Users/melbourne/.agents/skills/lottie-animation` — This skill should be used when the user asks to "add a Lottie animation", "play a .lottie or .json animation", "integrate a Bodymovin/After Effects animation on web or mobile", "control Lottie playback / segments", "make

- **lovable-cleanup** — `/Users/melbourne/.agents/skills/lovable-cleanup` — Audits and strips Lovable scaffolding from Vite + React projects — removes lovable-tagger, swaps placeholder assets, prunes unused Radix deps, and cleans generated docs so the codebase ships as yours.

- **m365-agents-dotnet** — `/Users/melbourne/.agents/skills/m365-agents-dotnet` — Microsoft 365 Agents SDK for .NET. Build multichannel agents for Teams/M365/Copilot Studio with ASP.NET Core hosting, AgentApplication routing, and MSAL-based auth.

- **m365-agents-py** — `/Users/melbourne/.agents/skills/m365-agents-py` — Microsoft 365 Agents SDK for Python. Build multichannel agents for Teams/M365/Copilot Studio with aiohttp hosting, AgentApplication routing, streaming responses, and MSAL-based auth.

- **m365-agents-ts** — `/Users/melbourne/.agents/skills/m365-agents-ts` — Microsoft 365 Agents SDK for TypeScript/Node.js.

- **machine-learning-ops-ml-pipeline** — `/Users/melbourne/.agents/skills/machine-learning-ops-ml-pipeline` — Design and implement a complete ML pipeline for: $ARGUMENTS

- **macos-cleaner** — `/Users/melbourne/.agents/skills/macos-cleaner` — Analyze and reclaim macOS disk space through intelligent cleanup recommendations. This skill should be used when users report disk space issues, need to clean up their Mac, or want to understand what's consuming storage.

- **macos-menubar-tuist-app** — `/Users/melbourne/.agents/skills/macos-menubar-tuist-app` — Build, refactor, or review SwiftUI macOS menubar apps that use Tuist.

- **macos-screen-recorder** — `/Users/melbourne/.agents/skills/macos-screen-recorder` — macOS screen recorder that captures the main display PLUS system audio via ScreenCaptureKit — no BlackHole/loopback driver, no sudo, just the standard Screen Recording permission. CLI-driven; fills the headless-screen-re

- **macos-spm-app-packaging** — `/Users/melbourne/.agents/skills/macos-spm-app-packaging` — Scaffold, build, sign, and package SwiftPM macOS apps without Xcode projects.

- **magic-animator** — `/Users/melbourne/.agents/skills/magic-animator` — AI-powered animation tool for creating motion in logos, UI, icons, and social media assets.

- **magic-ui-generator** — `/Users/melbourne/.agents/skills/magic-ui-generator` — Utilizes Magic by 21st.dev to generate, compare, and integrate multiple production-ready UI component variations.

- **mailchimp-automation** — `/Users/melbourne/.agents/skills/mailchimp-automation` — Automate Mailchimp email marketing including campaigns, audiences, subscribers, segments, and analytics via Rube MCP (Composio). Always search tools first for current schemas.

- **mailtrap-managing-contacts** — `/Users/melbourne/.agents/skills/mailtrap-managing-contacts` — Manage Mailtrap contacts, lists, segments, custom fields, imports, CRM syncs, and campaign audiences through the UI or API.

- **mailtrap-sending-emails** — `/Users/melbourne/.agents/skills/mailtrap-sending-emails` — Configure or troubleshoot Mailtrap live email sending with Email API, SMTP, transactional streams, bulk streams, or batches.

- **mailtrap-setting-up-sending-domain** — `/Users/melbourne/.agents/skills/mailtrap-setting-up-sending-domain` — Add or verify a Mailtrap sending domain, troubleshoot DNS propagation, publish SPF/DKIM/DMARC records, and complete compliance.

- **mailtrap-testing-with-sandbox** — `/Users/melbourne/.agents/skills/mailtrap-testing-with-sandbox` — Capture outbound email in Mailtrap Email Sandbox for development, staging, CI, HTML inspection, spam checks, and fake inbox tests.

- **make-automation** — `/Users/melbourne/.agents/skills/make-automation` — Automate Make (Integromat) tasks via Rube MCP (Composio): operations, enums, language and timezone lookups. Always search tools first for current schemas.

- **makepad-animation** — `/Users/melbourne/.agents/skills/makepad-animation` — |

- **makepad-basics** — `/Users/melbourne/.agents/skills/makepad-basics` — |

- **makepad-deployment** — `/Users/melbourne/.agents/skills/makepad-deployment` — |

- **makepad-dsl** — `/Users/melbourne/.agents/skills/makepad-dsl` — |

- **makepad-event-action** — `/Users/melbourne/.agents/skills/makepad-event-action` — |

- **makepad-font** — `/Users/melbourne/.agents/skills/makepad-font` — |

- **makepad-layout** — `/Users/melbourne/.agents/skills/makepad-layout` — |

- **makepad-platform** — `/Users/melbourne/.agents/skills/makepad-platform` — |

- **makepad-reference** — `/Users/melbourne/.agents/skills/makepad-reference` — This category provides reference materials for debugging, code quality, and advanced layout patterns.

- **makepad-shaders** — `/Users/melbourne/.agents/skills/makepad-shaders` — |

- **makepad-skills** — `/Users/melbourne/.agents/skills/makepad-skills` — Makepad UI development skills for Rust apps: setup, patterns, shaders, packaging, and troubleshooting.

- **makepad-splash** — `/Users/melbourne/.agents/skills/makepad-splash` — |

- **makepad-widgets** — `/Users/melbourne/.agents/skills/makepad-widgets` — Version: makepad-widgets (dev branch) | Last Updated: 2026-01-19 > > Check for updates: https://crates.io/crates/makepad-widgets

- **malware-analyst** — `/Users/melbourne/.agents/skills/malware-analyst` — Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. Masters sandbox analysis, behavioral analysis, and malware family identification.

- **manage-skills** — `/Users/melbourne/.agents/skills/manage-skills` — Discover, list, create, edit, toggle, copy, move, and delete AI agent skills across 11 tools (Cursor, Claude, Agents, Windsurf, Copilot, Codex, Cline, Aider, Continue, Roo Code, Augment)

- **management-core** — `/Users/melbourne/.agents/skills/management-core` — Apply a common management operating model when work spans goals, actions, decisions, risks, priorities, accountability, cadence, or executive synthesis.

- **management-reporting** — `/Users/melbourne/.agents/skills/management-reporting` — Create concise executive, weekly, monthly, operational, project, or board-style management reports focused on performance, variance, risk, and decisions.

- **manifest** — `/Users/melbourne/.agents/skills/manifest` — Install and configure the Manifest observability plugin for your agents. Use when setting up telemetry, configuring API keys, or troubleshooting the plugin.

- **market-sizing-analysis** — `/Users/melbourne/.agents/skills/market-sizing-analysis` — Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM) for startup opportunities.

- **marketing-council** — `/Users/melbourne/.agents/skills/marketing-council` — When the user wants multiple expert perspectives on a marketing question — a simulated board of advisors staffed by legendary marketers (Seth Godin, David Ogilvy, Eugene Schwartz, April Dunford, Rory Sutherland, Alex Hor

- **marketing-ideas** — `/Users/melbourne/.agents/skills/marketing-ideas` — When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. Also use when the user asks for 'marketing ideas,' 'growth ideas,' 'how to market,' 'marketing strategies,' 'marketing t

- **marketing-loops** — `/Users/melbourne/.agents/skills/marketing-loops` — When the user wants to set up a recurring, self-running marketing workflow — a repeatable loop an AI agent runs on a cadence (weekly, daily, on a trigger) rather than a one-off task. Also use when the user mentions 'mark

- **marketing-plan** — `/Users/melbourne/.agents/skills/marketing-plan` — When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. Also use when the user mentions "marketing plan," "growth plan," "GTM plan," "go-to-market plan," "AARRR plan,

- **marketing-psychology** — `/Users/melbourne/.agents/skills/marketing-psychology` — When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when the user mentions 'psychology,' 'mental models,' 'cognitive bias,' 'persuasion,' 'behavioral science

- **matematico-tao** — `/Users/melbourne/.agents/skills/matematico-tao` — Matemático ultra-avançado inspirado em Terence Tao. Análise rigorosa de código e arquitetura com teoria matemática profunda: teoria da informação, teoria dos grafos, complexidade computacional, álgebra linear, análise es

- **mathguard** — `/Users/melbourne/.agents/skills/mathguard` — Math-heavy escalation for n >= 10^6 — Bloom, HyperLogLog, Count-Min, MinHash/LSH, FFT, JL projection, sweep line. Use when classical O(n log n) is the floor and approximate or math wins.

- **matplotlib** — `/Users/melbourne/.agents/skills/matplotlib` — Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots.

- **maxia** — `/Users/melbourne/.agents/skills/maxia` — Connect to MAXIA AI-to-AI marketplace on Solana. Discover, buy, sell AI services. Earn USDC. 13 MCP tools, A2A protocol, DeFi yields, sentiment analysis, rug detection.

- **mcp-builder** — `/Users/melbourne/.agents/skills/mcp-builder` — Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world t

- **mcp-builder-ms** — `/Users/melbourne/.agents/skills/mcp-builder-ms` — Use this skill when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

- **mcp-tool-developer** — `/Users/melbourne/.agents/skills/mcp-tool-developer` — Build Model Context Protocol (MCP) servers and tools from scratch. Full-stack MCP development with TypeScript/Python, testing, deployment, and registry publishing.

- **medium-posts** — `/Users/melbourne/.agents/skills/medium-posts` — When the user wants to write, publish, republish, or optimize posts on Medium.com (canonical tags, distribution, Medium SEO). Also use when the user mentions "Medium," "Medium article," "Medium story," "Medium publishing

- **meeting-management** — `/Users/melbourne/.agents/skills/meeting-management` — Prepare agendas and decision briefs, structure meetings, and turn notes or transcripts into decisions, actions, owners, deadlines, and follow-ups.

- **meme-generation** — `/Users/melbourne/.agents/skills/meme-generation` — Generate memes using each::sense AI. Create classic meme templates, custom memes, brand memes, reaction memes, comparison memes, trending formats, and more for social media, marketing, and entertainment.

- **memory-forensics** — `/Users/melbourne/.agents/skills/memory-forensics` — Comprehensive techniques for acquiring, analyzing, and extracting artifacts from memory dumps for incident response and malware analysis.

- **memory-management** — `/Users/melbourne/.agents/skills/memory-management` — Use when the user asks to "remember project context", review saved findings, initialize runtime memory, archive stale work, reconcile notes, or erase a subject; manages authorized HOT/WARM/COLD working memory across all 

- **memory-safety-patterns** — `/Users/melbourne/.agents/skills/memory-safety-patterns` — Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management.

- **memory-systems** — `/Users/melbourne/.agents/skills/memory-systems` — Design short-term, long-term, and graph-based memory architectures. Use when building agents that must persist across sessions, needing to maintain entity consistency across conversations, or implementing reasoning over 

- **mental-health-analyzer** — `/Users/melbourne/.agents/skills/mental-health-analyzer` — 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。

- **menu-design-generation** — `/Users/melbourne/.agents/skills/menu-design-generation` — Generate professional restaurant, cafe, and bar menu designs using each::sense AI. Create print-ready menus, digital displays, QR code menus, and seasonal specials with stunning food photography and elegant typography la

- **mercury-mcp** — `/Users/melbourne/.agents/skills/mercury-mcp` — Cheatsheet for the Mercury (proton) MCP tools. Use when connected to the Mercury MCP server to look up which mercury_* tool to call for messaging teammates, threads, tasks, automations, or admin team-graph edits.

- **mermaid-expert** — `/Users/melbourne/.agents/skills/mermaid-expert` — Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling.

- **mesh-memory** — `/Users/melbourne/.agents/skills/mesh-memory` — Self-hosted semantic memory for AI agents via MCP. Save worklogs, decisions, and notes, then recall them across sessions by meaning, not keyword. Postgres + pgvector with auto-tagging.

- **message-house-builder** — `/Users/melbourne/.agents/skills/message-house-builder` — Use when the user asks to "build a message house", "write a PR-FAQ for our launch", or "define the launch narrative and value pillars"; derives from the positioning canvas a message house — tagline, one-liner, three valu

- **message-system-architect** — `/Users/melbourne/.agents/skills/message-system-architect` — Use when the user asks to "author our durable brand message hierarchy", "build the brand message house that seeds the canon", or "define the main narrative, three pillars, and tagline for the whole brand"; produces the D

- **message-test-designer** — `/Users/melbourne/.agents/skills/message-test-designer` — Use when the user asks to "test our messaging before we scale it", "design a message-market-fit panel", or "run a 5-second comprehension test on our new tagline"; produces a message-test design spec — hypothesis, panel a

- **meta-ad-creative-generation** — `/Users/melbourne/.agents/skills/meta-ad-creative-generation` — Generate Meta (Facebook & Instagram) ad creatives using each::sense AI. Create feed ads, stories, reels, carousel images, and video ads optimized for Meta's ad formats and best practices.

- **metasploit-framework** — `/Users/melbourne/.agents/skills/metasploit-framework` — ⚠️ AUTHORIZED USE ONLY > This skill is for educational purposes or authorized security assessments only. > You must have explicit, written permission from the system owner before using this tool. > Misuse of this tool is

- **micro-interaction** — `/Users/melbourne/.agents/skills/micro-interaction` — This skill should be used when the user asks to "add a hover/press effect", "animate a toggle or switch", "build an animated like button", "make a toast/snackbar slide in", "animate a drawer or modal", "animate list reor

- **micro-saas-launcher** — `/Users/melbourne/.agents/skills/micro-saas-launcher` — Expert in launching small, focused SaaS products fast - the indie

- **microservices-patterns** — `/Users/melbourne/.agents/skills/microservices-patterns` — Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience patterns for building distributed systems.

- **microsoft-azure-webjobs-extensions-authentication-events-dotnet** — `/Users/melbourne/.agents/skills/microsoft-azure-webjobs-extensions-authentication-events-dotnet` — Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions.

- **microsoft-teams-automation** — `/Users/melbourne/.agents/skills/microsoft-teams-automation` — Automate Microsoft Teams tasks via Rube MCP (Composio): send messages, manage channels, create meetings, handle chats, and search messages. Always search tools first for current schemas.

- **minecraft-bukkit-pro** — `/Users/melbourne/.agents/skills/minecraft-bukkit-pro` — Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs.

- **minimalist-ui** — `/Users/melbourne/.agents/skills/minimalist-ui` — Use when creating clean editorial interfaces with warm monochrome palettes, crisp borders, restrained motion, and flat bento layouts.

- **miro-automation** — `/Users/melbourne/.agents/skills/miro-automation` — Automate Miro tasks via Rube MCP (Composio): boards, items, sticky notes, frames, sharing, connectors. Always search tools first for current schemas.

- **mise-configurator** — `/Users/melbourne/.agents/skills/mise-configurator` — Generate production-ready mise.toml setups for local development, CI/CD pipelines, and toolchain standardization.

- **mixpanel-automation** — `/Users/melbourne/.agents/skills/mixpanel-automation` — Automate Mixpanel tasks via Rube MCP (Composio): events, segmentation, funnels, cohorts, user profiles, JQL queries. Always search tools first for current schemas.

- **ml-engineer** — `/Users/melbourne/.agents/skills/ml-engineer` — Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B testing, and monitoring.

- **ml-pipeline-workflow** — `/Users/melbourne/.agents/skills/ml-pipeline-workflow` — Complete end-to-end MLOps pipeline orchestration from data preparation through model deployment.

- **mlops-engineer** — `/Users/melbourne/.agents/skills/mlops-engineer` — Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools.

- **mmx-cli** — `/Users/melbourne/.agents/skills/mmx-cli` — Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. Use when the user wants to create media content, chat with MiniMax models, perform web search, or manage MiniMax API resources from 

- **moatmri** — `/Users/melbourne/.agents/skills/moatmri` — Analyze AI disruption pressure across a business, map competitive exposure, and produce a 90-day defensive action plan.

- **mobile-design** — `/Users/melbourne/.agents/skills/mobile-design` — (Mobile-First · Touch-First · Platform-Respectful)

- **mobile-developer** — `/Users/melbourne/.agents/skills/mobile-developer` — Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrations, offline sync, and app store optimization.

- **mobile-security-coder** — `/Users/melbourne/.agents/skills/mobile-security-coder` — Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns.

- **mock-hunter** — `/Users/melbourne/.agents/skills/mock-hunter` — Audit a live web page in five phases (catalog, click, trace, classify, report) to identify mock data, hardcoded values, LLM-generated metrics, and broken endpoints. Outputs a markdown report with REAL/MOCK/LLM/HARDCODED/

- **modern-javascript-patterns** — `/Users/melbourne/.agents/skills/modern-javascript-patterns` — Comprehensive guide for mastering modern JavaScript (ES6+) features, functional programming patterns, and best practices for writing clean, maintainable, and performant code.

- **molykit** — `/Users/melbourne/.agents/skills/molykit` — |

- **momentum-planner** — `/Users/melbourne/.agents/skills/momentum-planner` — Use when the user asks to "keep the launch momentum going after launch week", "plan a changelog / release-notes cadence as GTM", or "is this update worth a relaunch"; produces a T+1→T+30 momentum plan — a launch-moment c

- **monday-automation** — `/Users/melbourne/.agents/skills/monday-automation` — Automate Monday.com work management including boards, items, columns, groups, subitems, and updates via Rube MCP (Composio). Always search tools first for current schemas.

- **monetization** — `/Users/melbourne/.agents/skills/monetization` — Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e modelos de negocio SaaS.

- **monopoly** — `/Users/melbourne/.agents/skills/monopoly` — >

- **monorepo-architect** — `/Users/melbourne/.agents/skills/monorepo-architect` — Expert in monorepo architecture, build systems, and dependency management at scale. Masters Nx, Turborepo, Bazel, and Lerna for efficient multi-project development. Use PROACTIVELY for monorepo setup,

- **monorepo-management** — `/Users/melbourne/.agents/skills/monorepo-management` — Build efficient, scalable monorepos that enable code sharing, consistent tooling, and atomic changes across multiple packages and applications.

- **monte-carlo-monitor-creation** — `/Users/melbourne/.agents/skills/monte-carlo-monitor-creation` — Guides creation of Monte Carlo monitors via MCP tools, producing monitors-as-code YAML for CI/CD deployment.

- **monte-carlo-prevent** — `/Users/melbourne/.agents/skills/monte-carlo-prevent` — Surfaces Monte Carlo data observability context (table health, alerts, lineage, blast radius) before SQL/dbt edits.

- **monte-carlo-push-ingestion** — `/Users/melbourne/.agents/skills/monte-carlo-push-ingestion` — Expert guide for pushing metadata, lineage, and query logs to Monte Carlo from any data warehouse.

- **monte-carlo-validation-notebook** — `/Users/melbourne/.agents/skills/monte-carlo-validation-notebook` — Generates SQL validation notebooks for dbt PR changes with before/after comparison queries.

- **monthly-business-review** — `/Users/melbourne/.agents/skills/monthly-business-review` — Run a monthly business review across objectives, KPIs, finances, projects, customers, operations, people, risks, decisions, and next-month priorities.

- **moodle-external-api-development** — `/Users/melbourne/.agents/skills/moodle-external-api-development` — This skill guides you through creating custom external web service APIs for Moodle LMS, following Moodle's external API framework and coding standards.

- **motion-art-direction** — `/Users/melbourne/.agents/skills/motion-art-direction` — This skill should be used when the user asks to "direct a motion graphics video", "do creative/art direction for a video", "define a motion language", "set the tone and pacing", "make the animation feel consistent", "dec

- **motion-background** — `/Users/melbourne/.agents/skills/motion-background` — This skill should be used when the user asks to "add an animated background", "build a mesh/gradient background", "make an aurora/shader background", "add constellation/particle background", "animated hero background", o

- **motion-pricing** — `/Users/melbourne/.agents/skills/motion-pricing` — This skill should be used when the user asks to "quote a motion project", "estimate this animation job", "how much should I charge for this video", "what's my day rate", "build a quote", "price a 30-second explainer", or

- **moyu** — `/Users/melbourne/.agents/skills/moyu` — >

- **mtls-configuration** — `/Users/melbourne/.agents/skills/mtls-configuration` — Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate management, or securing internal service communication.

- **multi-advisor** — `/Users/melbourne/.agents/skills/multi-advisor` — Conselho de especialistas — consulta multiplos agentes do ecossistema em paralelo para analise multi-perspectiva de qualquer topico. Ativa personas, especialistas e agentes tecnicos simultaneamente, cada um pela sua otic

- **multi-agent-architect** — `/Users/melbourne/.agents/skills/multi-agent-architect` — Design and optimize production-grade multi-agent systems with LangGraph, LangChain, and DeepAgents for complex AI workflows.

- **multi-agent-brainstorming** — `/Users/melbourne/.agents/skills/multi-agent-brainstorming` — Simulate a structured peer-review process using multiple specialized agents to validate designs, surface hidden assumptions, and identify failure modes before implementation.

- **multi-agent-patterns** — `/Users/melbourne/.agents/skills/multi-agent-patterns` — This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create swarm architecture", "coordinate multiple agents", or mentions multi-agent patterns, context isolation,

- **multi-agent-task-orchestrator** — `/Users/melbourne/.agents/skills/multi-agent-task-orchestrator` — Route tasks to specialized AI agents with anti-duplication, quality gates, and 30-minute heartbeat monitoring

- **multi-cloud-architecture** — `/Users/melbourne/.agents/skills/multi-cloud-architecture` — Decision framework and patterns for architecting applications across AWS, Azure, and GCP.

- **multi-platform-apps-multi-platform** — `/Users/melbourne/.agents/skills/multi-platform-apps-multi-platform` — Build and deploy the same feature consistently across web, mobile, and desktop platforms using API-first architecture and parallel implementation strategies.

- **music-video-generation** — `/Users/melbourne/.agents/skills/music-video-generation` — Generate music videos using each::sense AI. Create visualizers, lyric videos, animated music videos, concert visuals, and genre-specific aesthetics synchronized to audio.

- **n8n-code-javascript** — `/Users/melbourne/.agents/skills/n8n-code-javascript` — Write JavaScript code in n8n Code nodes. Use when writing JavaScript in n8n, using $input/$json/$node syntax, making HTTP requests with $helpers, working with dates using DateTime, troubleshooting Code node errors, or ch

- **n8n-code-python** — `/Users/melbourne/.agents/skills/n8n-code-python` — Write Python code in n8n Code nodes. Use when writing Python in n8n, using _input/_json/_node syntax, working with standard library, or need to understand Python limitations in n8n Code nodes.

- **n8n-expression-syntax** — `/Users/melbourne/.agents/skills/n8n-expression-syntax` — Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, or working with webhook data in workflows.

- **n8n-mcp-tools-expert** — `/Users/melbourne/.agents/skills/n8n-mcp-tools-expert` — Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, managing workflows, or using any n8n-mcp tool. Provides tool selection guidance, paramet

- **n8n-node-configuration** — `/Users/melbourne/.agents/skills/n8n-node-configuration` — Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail levels, or learning common configuration pattern

- **n8n-validation-expert** — `/Users/melbourne/.agents/skills/n8n-validation-expert` — Expert guide for interpreting and fixing n8n validation errors.

- **n8n-workflow-patterns** — `/Users/melbourne/.agents/skills/n8n-workflow-patterns` — Proven architectural patterns for building n8n workflows.

- **nanobanana-infographic** — `/Users/melbourne/.agents/skills/nanobanana-infographic` — Create sleek, low-noise infographic prompts and render workflows with Nano Banana 2 for posts, decks, reports, and explainers. Trigger on infographic, Nano Banana 2, Gemini image, executive visual, blog diagram, or prese

- **nanobanana-ppt-skills** — `/Users/melbourne/.agents/skills/nanobanana-ppt-skills` — AI-powered PPT generation with document analysis and styled images

- **narrative-baseline-mapper** — `/Users/melbourne/.agents/skills/narrative-baseline-mapper` — Use when the user asks to "map what our surfaces say today", "inventory our current messaging", or "find the gap between what we say and what we mean"; produces the narrative baseline — a surface-by-surface inventory of 

- **narrative-cascade-planner** — `/Users/melbourne/.agents/skills/narrative-cascade-planner` — Use when the user asks to "plan how our narrative lands on every surface", "write per-surface message-match specs", or "brief each creative builder from the canon"; maps the narrative-registry canon onto every flagship s

- **narrative-drift-monitor** — `/Users/melbourne/.agents/skills/narrative-drift-monitor` — Use when the user asks to "check if our surfaces have drifted from the canon", "watch for competitor repositioning", or "define when we should reposition"; produces a drift report — self-drift per flagship surface vs the

- **narrative-enablement-kit** — `/Users/melbourne/.agents/skills/narrative-enablement-kit` — Use when the user asks to "make everyone tell the same story", "write our elevator pitch ladder", or "build a spokesperson Q&A and approved boilerplate pack"; derives from the narrative-registry canon, message house, and

- **narrative-quality-auditor** — `/Users/melbourne/.agents/skills/narrative-quality-auditor` — Use when the user asks to "audit our brand narrative" or "is this message on-canon"; runs separate typed TALE truth, system, or effectiveness profiles and never averages them into one composite. Checks differentiation, c

- **narrative-registry** — `/Users/melbourne/.agents/skills/narrative-registry` — Use when the user asks to record/query the brand narrative canon, tagline, message hierarchy, voice/naming rules, or a canon re-version; curates complete versioned canon events through the append-only narrative stream an

- **narrative-resonance-monitor** — `/Users/melbourne/.agents/skills/narrative-resonance-monitor` — Use when the user asks to "measure how our narrative is landing", "track echo rate against our canon lexicon", or "check how AI answer engines describe our brand"; produces a resonance report — echo rate (overlap of mark

- **native-data-fetching** — `/Users/melbourne/.agents/skills/native-data-fetching` — Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, caching, offline support, and Expo Router data loaders (useLoaderData).

- **neon-postgres** — `/Users/melbourne/.agents/skills/neon-postgres` — Expert patterns for Neon serverless Postgres, branching, connection

- **nerdzao-elite** — `/Users/melbourne/.agents/skills/nerdzao-elite` — Senior Elite Software Engineer (15+) and Senior Product Designer. Full workflow with planning, architecture, TDD, clean code, and pixel-perfect UX validation.

- **nerdzao-elite-gemini-high** — `/Users/melbourne/.agents/skills/nerdzao-elite-gemini-high` — Modo Elite Coder + UX Pixel-Perfect otimizado especificamente para Gemini 3.1 Pro High. Workflow completo com foco em qualidade máxima e eficiência de tokens.

- **nestjs-expert** — `/Users/melbourne/.agents/skills/nestjs-expert` — You are an expert in Nest.js with deep knowledge of enterprise-grade Node.js application architecture, dependency injection patterns, decorators, middleware, guards, interceptors, pipes, testing strategies, database inte

- **network-101** — `/Users/melbourne/.agents/skills/network-101` — Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, and security testing against properly configu

- **network-engineer** — `/Users/melbourne/.agents/skills/network-engineer` — Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization.

- **networkx** — `/Users/melbourne/.agents/skills/networkx` — NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs.

- **new-rails-project** — `/Users/melbourne/.agents/skills/new-rails-project` — Create a new Rails project

- **news-sentiment-engine** — `/Users/melbourne/.agents/skills/news-sentiment-engine` — Multi-source RSS news aggregation with Claude-powered sentiment analysis and structured briefing output

- **newsletter-creation-curation** — `/Users/melbourne/.agents/skills/newsletter-creation-curation` — Industry-adaptive B2B newsletter creation with stage, role, and geography-aware workflows

- **newsletter-generation** — `/Users/melbourne/.agents/skills/newsletter-generation` — Use this skill when the user requests to generate, create, write, or draft a newsletter, email digest, weekly roundup, industry briefing, or curated content summary. Supports topic-based research, content curation from m

- **newsletter-monetization-planner** — `/Users/melbourne/.agents/skills/newsletter-monetization-planner` — Use when the user asks to "monetize my newsletter", "build a sponsorship rate card", or "model paid-subscription revenue"; produces a revenue model (paid tiers, ad/sponsorship inventory + CPM/flat rate card, referral/boo

- **newsletter-sponsorship-finder** — `/Users/melbourne/.agents/skills/newsletter-sponsorship-finder` — >

- **nextjs-app-router-patterns** — `/Users/melbourne/.agents/skills/nextjs-app-router-patterns` — Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development.

- **nextjs-best-practices** — `/Users/melbourne/.agents/skills/nextjs-best-practices` — Next.js App Router principles. Server Components, data fetching, routing patterns.

- **nextjs-seo-indexing** — `/Users/melbourne/.agents/skills/nextjs-seo-indexing` — Fix SEO indexing issues, crawl budget problems, and Search Console coverage errors for Next.js apps. Covers canonical tags, noindex audits, sitemap health, static rendering, and internal linking.

- **nextjs-supabase-auth** — `/Users/melbourne/.agents/skills/nextjs-supabase-auth` — Expert integration of Supabase Auth with Next.js App Router

- **nft-art-generation** — `/Users/melbourne/.agents/skills/nft-art-generation` — Generate NFT artwork using each::sense AI. Create PFP collections, generative art, 1/1 pieces, pixel art, 3D renders, animated NFTs, and trait-based characters for Web3 projects.

- **nft-standards** — `/Users/melbourne/.agents/skills/nft-standards` — Master ERC-721 and ERC-1155 NFT standards, metadata best practices, and advanced NFT features.

- **nodejs-backend-patterns** — `/Users/melbourne/.agents/skills/nodejs-backend-patterns` — Comprehensive guidance for building scalable, maintainable, and production-ready Node.js backend applications with modern frameworks, architectural patterns, and best practices.

- **nodejs-best-practices** — `/Users/melbourne/.agents/skills/nodejs-best-practices` — Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying.

- **nosql-expert** — `/Users/melbourne/.agents/skills/nosql-expert` — Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). Focuses on mental models, query-first modeling, single-table design, and avoiding hot partitions in high-scale systems.

- **not-a-vibe-coder** — `/Users/melbourne/.agents/skills/not-a-vibe-coder` — Turns vague prompts into 8 structured planning files for brand new projects. DO NOT use on existing codebases.

- **not-human-search-mcp** — `/Users/melbourne/.agents/skills/not-human-search-mcp` — Search AI-ready websites, inspect indexed site details, verify MCP endpoints, and discover tools and APIs using the Not Human Search MCP server

- **notebooklm** — `/Users/melbourne/.agents/skills/notebooklm` — Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser session, retrieves the answer exclusively from your uploaded documents, and closes.

- **notion-automation** — `/Users/melbourne/.agents/skills/notion-automation` — Automate Notion tasks via Rube MCP (Composio): pages, databases, blocks, comments, users. Always search tools first for current schemas.

- **notion-template-business** — `/Users/melbourne/.agents/skills/notion-template-business` — Expert in building and selling Notion templates as a business - not

- **nsfw-content-generation** — `/Users/melbourne/.agents/skills/nsfw-content-generation` — Generate NSFW and adult content using each::sense API with safety checker disabled. Supports artistic nude, glamour, boudoir, fantasy, and mature themed content creation with full creative freedom.

- **nsfw-image-generation** — `/Users/melbourne/.agents/skills/nsfw-image-generation` — Generate adult images, artistic nudes, glamour photography, and fantasy art using the each::sense API with safety checker disabled

- **nsfw-video-generation** — `/Users/melbourne/.agents/skills/nsfw-video-generation` — Generate adult video content using each::sense API with safety checker disabled

- **nutrition-analyzer** — `/Users/melbourne/.agents/skills/nutrition-analyzer` — 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。

- **nx-workspace-patterns** — `/Users/melbourne/.agents/skills/nx-workspace-patterns` — Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands.

- **object-removal** — `/Users/melbourne/.agents/skills/object-removal` — Remove unwanted objects, people, text, and imperfections from photos using each::sense AI. Clean up images with intelligent inpainting that seamlessly fills removed areas.

- **objection-preemptor** — `/Users/melbourne/.agents/skills/objection-preemptor` — One sentence - what this skill does and when to invoke it

- **observability-engineer** — `/Users/melbourne/.agents/skills/observability-engineer` — Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows.

- **observability-monitoring-monitor-setup** — `/Users/melbourne/.agents/skills/observability-monitoring-monitor-setup` — You are a monitoring and observability expert specializing in implementing comprehensive monitoring solutions. Set up metrics collection, distributed tracing, log aggregation, and create insightful da

- **observability-monitoring-slo-implement** — `/Users/melbourne/.agents/skills/observability-monitoring-slo-implement` — You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering practices. Design comprehensive SLO frameworks, establish meaningful SLIs, and create 

- **obsidian-bases** — `/Users/melbourne/.agents/skills/obsidian-bases` — Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the user mentions Bases, table views, card view

- **obsidian-cli** — `/Users/melbourne/.agents/skills/obsidian-cli` — Use the Obsidian CLI to read, create, search, and manage vault content, or to develop and debug Obsidian plugins and themes from the command line.

- **obsidian-clipper-template-creator** — `/Users/melbourne/.agents/skills/obsidian-clipper-template-creator` — Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available variables, or format clipped content.

- **obsidian-markdown** — `/Users/melbourne/.agents/skills/obsidian-markdown` — Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files in Obsidian, or when the user mentions wikilinks, callouts, fro

- **occupational-health-analyzer** — `/Users/melbourne/.agents/skills/occupational-health-analyzer` — 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。

- **odoo-accounting-setup** — `/Users/melbourne/.agents/skills/odoo-accounting-setup` — Expert guide for configuring Odoo Accounting: chart of accounts, journals, fiscal positions, taxes, payment terms, and bank reconciliation.

- **odoo-automated-tests** — `/Users/melbourne/.agents/skills/odoo-automated-tests` — Write and run Odoo automated tests using TransactionCase, HttpCase, and browser tour tests. Covers test data setup, mocking, and CI integration.

- **odoo-backup-strategy** — `/Users/melbourne/.agents/skills/odoo-backup-strategy` — Complete Odoo backup and restore strategy: database dumps, filestore backup, automated scheduling, cloud storage upload, and tested restore procedures.

- **odoo-docker-deployment** — `/Users/melbourne/.agents/skills/odoo-docker-deployment` — Production-ready Docker and docker-compose setup for Odoo with PostgreSQL, persistent volumes, environment-based configuration, and Nginx reverse proxy.

- **odoo-ecommerce-configurator** — `/Users/melbourne/.agents/skills/odoo-ecommerce-configurator` — Expert guide for Odoo eCommerce and Website: product catalog, payment providers, shipping methods, SEO, and order-to-fulfillment workflow.

- **odoo-edi-connector** — `/Users/melbourne/.agents/skills/odoo-edi-connector` — Guide for implementing EDI (Electronic Data Interchange) with Odoo: X12, EDIFACT document mapping, partner onboarding, and automated order processing.

- **odoo-hr-payroll-setup** — `/Users/melbourne/.agents/skills/odoo-hr-payroll-setup` — Expert guide for Odoo HR and Payroll: salary structures, payslip rules, leave policies, employee contracts, and payroll journal entries.

- **odoo-inventory-optimizer** — `/Users/melbourne/.agents/skills/odoo-inventory-optimizer` — Expert guide for Odoo Inventory: stock valuation (FIFO/AVCO), reordering rules, putaway strategies, routes, and multi-warehouse configuration.

- **odoo-l10n-compliance** — `/Users/melbourne/.agents/skills/odoo-l10n-compliance` — Country-specific Odoo localization: tax configuration, e-invoicing (CFDI, FatturaPA, SAF-T), fiscal reporting, and country chart of accounts setup.

- **odoo-manufacturing-advisor** — `/Users/melbourne/.agents/skills/odoo-manufacturing-advisor` — Expert guide for Odoo Manufacturing: Bills of Materials (BoM), Work Centers, routings, MRP planning, and production order workflows.

- **odoo-migration-helper** — `/Users/melbourne/.agents/skills/odoo-migration-helper` — Step-by-step guide for migrating Odoo custom modules between versions (v14→v15→v16→v17). Covers API changes, deprecated methods, and view migration.

- **odoo-module-developer** — `/Users/melbourne/.agents/skills/odoo-module-developer` — Expert guide for creating custom Odoo modules. Covers __manifest__.py, model inheritance, ORM patterns, and module structure best practices.

- **odoo-orm-expert** — `/Users/melbourne/.agents/skills/odoo-orm-expert` — Master Odoo ORM patterns: search, browse, create, write, domain filters, computed fields, and performance-safe query techniques.

- **odoo-performance-tuner** — `/Users/melbourne/.agents/skills/odoo-performance-tuner` — Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, and profiling tools.

- **odoo-project-timesheet** — `/Users/melbourne/.agents/skills/odoo-project-timesheet` — Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts, and invoicing from timesheets.

- **odoo-purchase-workflow** — `/Users/melbourne/.agents/skills/odoo-purchase-workflow` — Expert guide for Odoo Purchase: RFQ → PO → Receipt → Vendor Bill workflow, purchase agreements, vendor price lists, and 3-way matching.

- **odoo-qweb-templates** — `/Users/melbourne/.agents/skills/odoo-qweb-templates` — Expert in Odoo QWeb templating for PDF reports, email templates, and website pages. Covers t-if, t-foreach, t-field, and report actions.

- **odoo-rpc-api** — `/Users/melbourne/.agents/skills/odoo-rpc-api` — Expert on Odoo's external JSON-RPC and XML-RPC APIs. Covers authentication, model calls, record CRUD, and real-world integration examples in Python, JavaScript, and curl.

- **odoo-sales-crm-expert** — `/Users/melbourne/.agents/skills/odoo-sales-crm-expert` — Expert guide for Odoo Sales and CRM: pipeline stages, quotation templates, pricelists, sales teams, lead scoring, and forecasting.

- **odoo-security-rules** — `/Users/melbourne/.agents/skills/odoo-security-rules` — Expert in Odoo access control: ir.model.access.csv, record rules (ir.rule), groups, and multi-company security patterns.

- **odoo-shopify-integration** — `/Users/melbourne/.agents/skills/odoo-shopify-integration` — Connect Odoo with Shopify: sync products, inventory, orders, and customers using the Shopify API and Odoo's external API or connector modules.

- **odoo-upgrade-advisor** — `/Users/melbourne/.agents/skills/odoo-upgrade-advisor` — Step-by-step Odoo version upgrade advisor: pre-upgrade checklist, community vs enterprise upgrade path, OCA module compatibility, and post-upgrade validation.

- **odoo-woocommerce-bridge** — `/Users/melbourne/.agents/skills/odoo-woocommerce-bridge` — Sync Odoo with WooCommerce: products, inventory, orders, and customers via WooCommerce REST API and Odoo external API.

- **odoo-xml-views-builder** — `/Users/melbourne/.agents/skills/odoo-xml-views-builder` — Expert at building Odoo XML views: Form, List, Kanban, Search, Calendar, and Graph. Generates correct XML for Odoo 14-17 with proper visibility syntax.

- **offer-claims-registry** — `/Users/melbourne/.agents/skills/offer-claims-registry` — Use when the user asks to "register this claim", "log our current offers", or "where is the proof for this figure"; curates claim wording, evidence, disclosures, terms, review dates, and live offers through the append-on

- **offers** — `/Users/melbourne/.agents/skills/offers` — When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee design, scarcity/urgency, naming, and payment structure. Also use when the

- **office-productivity** — `/Users/melbourne/.agents/skills/office-productivity` — Office productivity workflow covering document creation, spreadsheet automation, presentation generation, and integration with LibreOffice and Microsoft Office formats.

- **offsite-signal-analyzer** — `/Users/melbourne/.agents/skills/offsite-signal-analyzer` — Use when the user asks to "analyze backlinks", "analyze my off-site signals", or "track AI traffic / ChatGPT / Perplexity referrals"; profiles referring domains, anchor-text mix, toxic links, and disavow candidates (back

- **on-call-handoff-patterns** — `/Users/melbourne/.agents/skills/on-call-handoff-patterns` — Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts.

- **on-page-seo-checker** — `/Users/melbourne/.agents/skills/on-page-seo-checker` — Use when the user asks to "audit on-page SEO" or "diagnose why a single page dropped"; scores titles, meta, header structure, keyword placement, links, and images with prioritized fixes. Not for E-E-A-T / publish-readine

- **onboarding** — `/Users/melbourne/.agents/skills/onboarding` — When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user mentions "onboarding flow," "activation rate," "user activation," "first-run experie

- **onboarding-cro** — `/Users/melbourne/.agents/skills/onboarding-cro` — You are an expert in user onboarding and activation. Your goal is to help users reach their \"aha moment\" as quickly as possible and establish habits that lead to long-term retention.

- **onboarding-psychologist** — `/Users/melbourne/.agents/skills/onboarding-psychologist` — One sentence - what this skill does and when to invoke it

- **one-drive-automation** — `/Users/melbourne/.agents/skills/one-drive-automation` — Automate OneDrive file management, search, uploads, downloads, sharing, permissions, and folder operations via Rube MCP (Composio). Always search tools first for current schemas.

- **open-dynamic-workflows** — `/Users/melbourne/.agents/skills/open-dynamic-workflows` — Plan, orchestrate, and adversarially verify parallel AI coding agents with a dynamic multi-agent workflow engine.

- **openapi-spec-generation** — `/Users/melbourne/.agents/skills/openapi-spec-generation` — Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation, generating SDKs, or ensuring API contract compliance.

- **openclaw-github-repo-commander** — `/Users/melbourne/.agents/skills/openclaw-github-repo-commander` — 7-stage super workflow for GitHub repo audit, cleanup, PR review, and competitor analysis

- **operations-management** — `/Users/melbourne/.agents/skills/operations-management` — Improve day-to-day operations through process mapping, capacity, handoffs, service levels, bottlenecks, incidents, standard work, and operating cadence.

- **optimize-images** — `/Users/melbourne/.agents/skills/optimize-images` — This skill should be used when the user asks to "optimize images", "compress images", "reduce image file size", "make images smaller", "optimize PNGs", "optimize JPEGs", "speed up website images", "reduce bundle size ima

- **options-flow-analyzer** — `/Users/melbourne/.agents/skills/options-flow-analyzer` — Real vs lottery call separation for options P/C ratio analysis — prevents signal inversion from deep OTM noise

- **oral-health-analyzer** — `/Users/melbourne/.agents/skills/oral-health-analyzer` — 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。

- **orchestrate-batch-refactor** — `/Users/melbourne/.agents/skills/orchestrate-batch-refactor` — Plan and execute large refactors with dependency-aware work packets and parallel analysis.

- **os-scripting** — `/Users/melbourne/.agents/skills/os-scripting` — Operating system and shell scripting troubleshooting workflow for Linux, macOS, and Windows. Covers bash scripting, system administration, debugging, and automation.

- **oss-hunter** — `/Users/melbourne/.agents/skills/oss-hunter` — Automatically hunt for high-impact OSS contribution opportunities in trending repositories.

- **osterwalder-canvas-architect** — `/Users/melbourne/.agents/skills/osterwalder-canvas-architect` — Iterative consultant agent for building and validating logically consistent 9-block Business Model Canvases.

- **outlook-automation** — `/Users/melbourne/.agents/skills/outlook-automation` — Automate Outlook tasks via Rube MCP (Composio): emails, calendar, contacts, folders, attachments. Always search tools first for current schemas.

- **outlook-calendar-automation** — `/Users/melbourne/.agents/skills/outlook-calendar-automation` — Automate Outlook Calendar tasks via Rube MCP (Composio): create events, manage attendees, find meeting times, and handle invitations. Always search tools first for current schemas.

- **outreach-manager** — `/Users/melbourne/.agents/skills/outreach-manager` — Use when the user asks to "write influencer outreach", "follow up with a creator", "pitch a journalist, hunter, or launch partner", or "negotiate partnership terms"; produces personalized pitches, multi-touch follow-up s

- **packaging-design-generation** — `/Users/melbourne/.agents/skills/packaging-design-generation` — Generate professional product packaging designs using each::sense AI. Create box designs, food packaging, cosmetic containers, beverage labels, supplement bottles, coffee bags, candle packaging, gift boxes, shopping bags

- **page-cro** — `/Users/melbourne/.agents/skills/page-cro` — Analyze and optimize individual pages for conversion performance.

- **page-play-builder** — `/Users/melbourne/.agents/skills/page-play-builder` — Use when the user asks to "build programmatic SEO pages", "generate pages at scale", "rank on a high-authority third-party site", "borrow domain authority", "build a vs / alternative page", "do local SEO", "optimize a Go

- **page-transition-animation** — `/Users/melbourne/.agents/skills/page-transition-animation` — This skill should be used when the user asks to "animate page or route transitions", "add a page transition or crossfade between views", "animate route changes in Next.js App Router", "use the View Transitions API", "Ani

- **pagerduty-automation** — `/Users/melbourne/.agents/skills/pagerduty-automation` — Automate PagerDuty tasks via Rube MCP (Composio): manage incidents, services, schedules, escalation policies, and on-call rotations. Always search tools first for current schemas.

- **pagespeed-enhancer** — `/Users/melbourne/.agents/skills/pagespeed-enhancer` — Scan, audit, and fix web performance issues across all four Lighthouse/PageSpeed Insights pillars — Performance, Accessibility, Best Practices, and SEO — in structured batches.

- **paid-ads** — `/Users/melbourne/.agents/skills/paid-ads` — You are an expert performance marketer with direct access to ad platform accounts. Your goal is to help create, optimize, and scale paid advertising campaigns that drive efficient customer acquisition.

- **paid-measurement-loop** — `/Users/melbourne/.agents/skills/paid-measurement-loop` — Use when the user asks to "read back" a paid campaign change, "did this ad change work", or "compare ROAS/CPA before and after"; reads ROAS/CPA against a control over a fixed readback window and returns a Promote / Keep-

- **pakistan-payments-stack** — `/Users/melbourne/.agents/skills/pakistan-payments-stack` — Design and implement production-grade Pakistani payment integrations (JazzCash, Easypaisa, bank/PSP rails, optional Raast) for SaaS with PKR billing, webhook reliability, and reconciliation.

- **papers-skill** — `/Users/melbourne/.agents/skills/papers-skill` — Skill for academic research workflows: search Semantic Scholar (200M+ papers), inspect citations, download arXiv PDFs, and extract PDF text. Bundles a self-contained Python CLI.

- **parallel-agents** — `/Users/melbourne/.agents/skills/parallel-agents` — Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives.

- **parasite-seo** — `/Users/melbourne/.agents/skills/parasite-seo` — When the user wants to choose or execute third-party platform SEO (high-authority sites for rankings or backlinks). Also use when the user mentions "parasite SEO," "parasitic SEO," "barnacle SEO," "hosted content," "thir

- **participation-warmup-planner** — `/Users/melbourne/.agents/skills/participation-warmup-planner` — Use when the user asks to "plan the participation ramp before we promote", "how much account history or karma do we need in this community", or "design entry incentives and member lifecycle for our own Discord"; produces

- **particle-system** — `/Users/melbourne/.agents/skills/particle-system` — This skill should be used when the user asks to "build a particle system", "make confetti/snow/smoke/sparks", "create a connected-dot/constellation network background", "add a flow-field or curl-noise particle effect", "

- **payment-integration** — `/Users/melbourne/.agents/skills/payment-integration` — Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. Use PROACTIVELY when implementing payments, billing, or subscription features.

- **paypal-integration** — `/Users/melbourne/.agents/skills/paypal-integration` — Master PayPal payment integration including Express Checkout, IPN handling, recurring billing, and refund workflows.

- **paywall-upgrade-cro** — `/Users/melbourne/.agents/skills/paywall-upgrade-cro` — You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at moments when they've experienced enough value to justify the commitment.

- **paywalls** — `/Users/melbourne/.agents/skills/paywalls` — When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall," "upgrade screen," "upgrade modal," "upsell," "feature gate," "conver

- **pci-compliance** — `/Users/melbourne/.agents/skills/pci-compliance` — Master PCI DSS (Payment Card Industry Data Security Standard) compliance for secure payment processing and handling of cardholder data.

- **pdf-conversion-router** — `/Users/melbourne/.agents/skills/pdf-conversion-router` — Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX, or structured notes and the agent must choose the best extraction route, settings, and cleanup strategy for maximum fidelity and rea

- **pdf-official** — `/Users/melbourne/.agents/skills/pdf-official` — This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see reference.md. If you need to fill out a PDF for

- **pentest-checklist** — `/Users/melbourne/.agents/skills/pentest-checklist` — Provide a comprehensive checklist for planning, executing, and following up on penetration tests. Ensure thorough preparation, proper scoping, and effective remediation of discovered vulnerabilities.

- **pentest-commands** — `/Users/melbourne/.agents/skills/pentest-commands` — Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation, password cracking, and web application testing. Enable quick command lookup during security assessments.

- **performance-analyzer** — `/Users/melbourne/.agents/skills/performance-analyzer` — Use when the user asks to "analyze influencer campaign performance", "compare influencers", or "find what content worked"; produces metric scorecards vs target and benchmark, platform/influencer/content rankings, engagem

- **performance-engineer** — `/Users/melbourne/.agents/skills/performance-engineer` — Expert performance engineer specializing in modern observability,

- **performance-monitor** — `/Users/melbourne/.agents/skills/performance-monitor` — Use when the user asks to "generate an SEO report", "出月报", "set SEO alerts", or "排名掉了提醒我"; two modes — report builds multi-metric traffic/ranking/authority/content dashboards, and alert configures threshold notifications

- **performance-optimizer** — `/Users/melbourne/.agents/skills/performance-optimizer` — Identifies and fixes performance bottlenecks in code, databases, and APIs. Measures before and after to prove improvements.

- **performance-profiling** — `/Users/melbourne/.agents/skills/performance-profiling` — Performance profiling principles. Measurement, analysis, and optimization techniques.

- **performance-testing-review-ai-review** — `/Users/melbourne/.agents/skills/performance-testing-review-ai-review` — You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub Copilot, Qodo, GPT-5, C

- **performance-testing-review-multi-agent-review** — `/Users/melbourne/.agents/skills/performance-testing-review-multi-agent-review` — Use when working with performance testing review multi agent review

- **permission-manager** — `/Users/melbourne/.agents/skills/permission-manager` — Manage opencode permissions: review always-allow lists, suggest safe read-only commands, configure permission patterns

- **personal-tool-builder** — `/Users/melbourne/.agents/skills/personal-tool-builder` — Expert in building custom tools that solve your own problems first.

- **pet-portrait-generation** — `/Users/melbourne/.agents/skills/pet-portrait-generation` — Generate custom pet portraits using each::sense AI. Create realistic, artistic, and stylized pet portraits from photos - including cartoon, renaissance, watercolor, pop art, anime styles, and custom product mockups.

- **phase-gated-debugging** — `/Users/melbourne/.agents/skills/phase-gated-debugging` — Use when debugging any bug. Enforces a 5-phase protocol where code edits are blocked until root cause is confirmed. Prevents premature fix attempts.

- **photo-colorization** — `/Users/melbourne/.agents/skills/photo-colorization` — Colorize black and white photos using each::sense AI. Bring old family portraits, historical images, vintage photographs, and archival footage to life with intelligent, context-aware colorization.

- **photo-restoration** — `/Users/melbourne/.agents/skills/photo-restoration` — Restore and enhance old, damaged, or degraded photos using each::sense AI. Fix scratches, tears, fading, water damage, colorize black and white photos, and restore faces in historical images.

- **photopea-embedded-editor** — `/Users/melbourne/.agents/skills/photopea-embedded-editor` — Embed Photopea in web apps using photopea.js. Covers embedding, file I/O, scripting, exporting, layers, text, filters, and the full Photoshop-compatible API.

- **photorealistic-portrait** — `/Users/melbourne/.agents/skills/photorealistic-portrait` — Design and generate realistic professional, editorial, lifestyle, fashion, cinematic, and profile portraits with controlled identity, lighting, pose, lens, and retouching.

- **php-pro** — `/Users/melbourne/.agents/skills/php-pro` — Write idiomatic PHP code with generators, iterators, SPL data

- **pinterest-pin-generation** — `/Users/melbourne/.agents/skills/pinterest-pin-generation` — Generate Pinterest pin images using each::sense AI. Create standard pins, idea pins, product pins, recipe pins, infographics, and more optimized for Pinterest's formats and best practices.

- **pipecat-friday-agent** — `/Users/melbourne/.agents/skills/pipecat-friday-agent` — Build a low-latency, Iron Man-inspired tactical voice assistant (F.R.I.D.A.Y.) using Pipecat, Gemini, and OpenAI.

- **pipedrive-automation** — `/Users/melbourne/.agents/skills/pipedrive-automation` — Automate Pipedrive CRM operations including deals, contacts, organizations, activities, notes, and pipeline management via Rube MCP (Composio). Always search tools first for current schemas.

- **pitch-narrative-builder** — `/Users/melbourne/.agents/skills/pitch-narrative-builder` — Use when the user asks to "build our pitch deck narrative", "write a fundraising story", or "structure the sales pitch narrative"; derives from the narrative canon a company pitch/deck narrative — problem → the undeniabl

- **pitch-psychologist** — `/Users/melbourne/.agents/skills/pitch-psychologist` — One sentence - what this skill does and when to invoke it

- **pixel-avatar** — `/Users/melbourne/.agents/skills/pixel-avatar` — Compatibility alias for legacy pixel-avatar requests. Use this skill when old prompts explicitly reference pixel-avatar, then route to avatar-portrait with a pixel-art style requirement.

- **placement-exclusion-manager** — `/Users/melbourne/.agents/skills/placement-exclusion-manager` — Use when the user asks to "build my brand-safety exclusion lists", "set placement / topic / content exclusions before launch", "add network and audience exclusions", or "prep the A1 brand-safety evidence for the auditor"

- **plaid-fintech** — `/Users/melbourne/.agents/skills/plaid-fintech` — Expert patterns for Plaid API integration including Link token

- **plan-writing** — `/Users/melbourne/.agents/skills/plan-writing` — Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work.

- **planning-with-files** — `/Users/melbourne/.agents/skills/planning-with-files` — Work like Manus: Use persistent markdown files as your \"working memory on disk.\"

- **platform-norm-profiler** — `/Users/melbourne/.agents/skills/platform-norm-profiler` — Use when the user asks to "build the norm card for this platform", "what are the char limits and visible-fold cutoffs here", "is the LinkedIn link-in-first-comment thing documented or folklore", or "which of our platform

- **playwright-java** — `/Users/melbourne/.agents/skills/playwright-java` — Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5, Allure reporting, and parallel execution.

- **playwright-skill** — `/Users/melbourne/.agents/skills/playwright-skill` — IMPORTANT - Path Resolution: This skill can be installed in different locations (plugin system, manual installation, global, or project-specific). Before executing any commands, determine the skill directory based on whe

- **plotly** — `/Users/melbourne/.agents/skills/plotly` — Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static publication figures use matplotlib or scienti

- **podcast-generation** — `/Users/melbourne/.agents/skills/podcast-generation` — Generate real audio narratives from text content using Azure OpenAI's Realtime API.

- **polars** — `/Users/melbourne/.agents/skills/polars` — Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in memory. Lazy evaluation, parallel execution, Apache Arrow backend. Best for 1-100GB datasets, ETL pipeline

- **polis-protocol** — `/Users/melbourne/.agents/skills/polis-protocol` — Coordinate multi-vendor AI agents as a self-improving team — a learning router assigns work by track record and citizens can amend the protocol's own rules.

- **popup-cro** — `/Users/melbourne/.agents/skills/popup-cro` — Create and optimize popups, modals, overlays, slide-ins, and banners to increase conversions without harming user experience or brand trust.

- **popups** — `/Users/melbourne/.agents/skills/popups` — When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user mentions "exit intent," "popup conversions," "modal optimization," "lead capture p

- **portfolio-pmo** — `/Users/melbourne/.agents/skills/portfolio-pmo` — Coordinate multiple projects through portfolio priorities, capacity, dependencies, governance, benefits, health, escalation, and executive portfolio reporting.

- **portrait-enhancement** — `/Users/melbourne/.agents/skills/portrait-enhancement` — Enhance portrait photos using each::sense AI. Professional-grade retouching including skin smoothing, teeth whitening, eye enhancement, blemish removal, lighting adjustment, and more.

- **positioning-mapper** — `/Users/melbourne/.agents/skills/positioning-mapper` — Use when the user asks to "map our positioning", "name our competitive alternatives", or "pick a beachhead segment for the launch"; produces a Dunford-style positioning canvas — named competitive alternatives (including 

- **positioning-truth-tracer** — `/Users/melbourne/.agents/skills/positioning-truth-tracer` — Use when the user asks to "check our positioning against what we can actually ship", "trace which differentiators we can defend", or "reconcile the positioning canvas with the claims ledger"; reconciles the reused positi

- **posix-shell-pro** — `/Users/melbourne/.agents/skills/posix-shell-pro` — Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-compliant shell (dash, ash, sh, bash --posix).

- **poster-campaign-design** — `/Users/melbourne/.agents/skills/poster-campaign-design` — Create posters, match announcements, event key art, campaign ads, flyers, and promotional compositions using generated imagery plus exact typography and brand assets.

- **poster-design-generation** — `/Users/melbourne/.agents/skills/poster-design-generation` — Generate professional poster designs using each::sense AI. Create movie posters, event posters, motivational posters, product launch visuals, vintage designs, travel posters, and more with AI-powered creative generation.

- **postgres** — `/Users/melbourne/.agents/skills/postgres` — PostgreSQL best practices, query optimization, connection troubleshooting, and performance improvement. Load when working with Postgres databases.

- **postgres-best-practices** — `/Users/melbourne/.agents/skills/postgres-best-practices` — Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations.

- **postgresql** — `/Users/melbourne/.agents/skills/postgresql` — Design a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features

- **postgresql-optimization** — `/Users/melbourne/.agents/skills/postgresql-optimization` — PostgreSQL database optimization workflow for query tuning, indexing strategies, performance analysis, and production database management.

- **posthog-automation** — `/Users/melbourne/.agents/skills/posthog-automation` — Automate PostHog tasks via Rube MCP (Composio): events, feature flags, projects, user profiles, annotations. Always search tools first for current schemas.

- **postmark-automation** — `/Users/melbourne/.agents/skills/postmark-automation` — Automate Postmark email delivery tasks via Rube MCP (Composio): send templated emails, manage templates, monitor delivery stats and bounces. Always search tools first for current schemas.

- **postmortem-writing** — `/Users/melbourne/.agents/skills/postmortem-writing` — Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence.

- **powershell-windows** — `/Users/melbourne/.agents/skills/powershell-windows` — PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling.

- **pptx-official** — `/Users/melbourne/.agents/skills/pptx-official` — A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx file is essentially a ZIP archive containing XML files and other resources that you can read or edit. You have different tools and work

- **pr-merge-champion** — `/Users/melbourne/.agents/skills/pr-merge-champion` — Optimize pull requests for quick approval and merging by ensuring clean diffs, comprehensive self-reviews, and structured documentation.

- **pr-writer** — `/Users/melbourne/.agents/skills/pr-writer` — Create pull requests following Sentry's engineering practices.

- **preference-frequency-manager** — `/Users/melbourne/.agents/skills/preference-frequency-manager` — Use when the user asks to "build a preference center", "set up a frequency opt-down ladder", "give people a step-down instead of unsubscribe", or "design a topic/cadence preference page"; produces a preference-center fie

- **presentation-generation** — `/Users/melbourne/.agents/skills/presentation-generation` — Generate professional presentations and slide decks using each::sense AI. Create pitch decks, business presentations, training materials, conference talks, and more with AI-powered slide generation.

- **press-media-relations** — `/Users/melbourne/.agents/skills/press-media-relations` — Use when the user asks to "build a media list for my launch", "write a launch press release", or "pitch press under embargo"; produces a three-tier media and analyst list (Tier 1 exclusive candidates, Tier 2 vertical pre

- **press-release-writer** — `/Users/melbourne/.agents/skills/press-release-writer` — Write professional press releases for any occasion, media type, and region. Use when the user wants to write, draft, or improve a press release, communiqué de presse, media announcement, or news release — including produ

- **price-psychology-strategist** — `/Users/melbourne/.agents/skills/price-psychology-strategist` — One sentence - what this skill does and when to invoke it

- **pricing** — `/Users/melbourne/.agents/skills/pricing` — When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'pricing tiers,' 'freemium,' 'free trial,' 'packaging,' 'price increase,' 'value metric,' '

- **pricing-packaging-planner** — `/Users/melbourne/.agents/skills/pricing-packaging-planner` — Use when the user asks to "plan launch pricing", "design pricing tiers / packaging", or "set up a launch discount / early-bird offer"; produces a launch pricing and packaging plan — tier structure and naming, a value-to-

- **pricing-strategy** — `/Users/melbourne/.agents/skills/pricing-strategy` — Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives.

- **prisma-expert** — `/Users/melbourne/.agents/skills/prisma-expert` — You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling, and database operations across PostgreSQL, MySQL, and SQLite.

- **privacy-by-design** — `/Users/melbourne/.agents/skills/privacy-by-design` — Use when building apps that collect user data. Ensures privacy protections are built in from the start—data minimization, consent, encryption.

- **privilege-escalation-methods** — `/Users/melbourne/.agents/skills/privilege-escalation-methods` — Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on compromised Linux and Windows systems. Essential for penetration testing post-exploitation phase and r

- **procurement-supplier-management** — `/Users/melbourne/.agents/skills/procurement-supplier-management` — Plan purchases, structure requirements, compare suppliers, manage RFQs, evaluate bids, track commitments, supplier performance, risks, and renewals.

- **product-design** — `/Users/melbourne/.agents/skills/product-design` — Design de produto nivel Apple — sistemas visuais, UX flows, acessibilidade, linguagem visual proprietaria, design tokens, prototipagem e handoff. Cobre Figma, design systems, tipografia, cor, espacamento, motion design e

- **product-feed-optimizer** — `/Users/melbourne/.agents/skills/product-feed-optimizer` — Use when the user asks to "optimize my Shopping feed", "fix product disapprovals", "improve product titles/attributes", or "build feed-driven PMax asset groups"; audits and rewrites the Shopping/Performance Max product f

- **product-inventor** — `/Users/melbourne/.agents/skills/product-inventor` — Product Inventor e Design Alchemist de nivel maximo — combina Product Thinking, Design Systems, UI Engineering, Psicologia Cognitiva, Storytelling e execucao impecavel nivel Jobs/Apple.

- **product-manager** — `/Users/melbourne/.agents/skills/product-manager` — Senior PM agent with 6 knowledge domains, 30+ frameworks, 12 templates, and 32 SaaS metrics with formulas. Pure Markdown, zero scripts.

- **product-manager-toolkit** — `/Users/melbourne/.agents/skills/product-manager-toolkit` — Essential tools and frameworks for modern product management, from discovery to delivery.

- **product-marketing** — `/Users/melbourne/.agents/skills/product-marketing` — When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' 'who is my target audience,' 'des

- **product-marketing-context** — `/Users/melbourne/.agents/skills/product-marketing-context` — Create or update a reusable product marketing context document with positioning, audience, ICP, use cases, and messaging. Use at the start of a project to avoid repeating core marketing context across tasks.

- **product-photo-generation** — `/Users/melbourne/.agents/skills/product-photo-generation` — Generate professional product photography using each::sense API for e-commerce, marketing, and catalog imagery

- **production-audit** — `/Users/melbourne/.agents/skills/production-audit` — Audit a shipped repo for production-readiness gaps across RLS, webhooks, secrets, grants, Stripe idempotency, mobile UX, and deployment health.

- **production-code-audit** — `/Users/melbourne/.agents/skills/production-code-audit` — Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-level professional quality with optimizations

- **production-scheduling** — `/Users/melbourne/.agents/skills/production-scheduling` — Codified expertise for production scheduling, job sequencing, line balancing, changeover optimisation, and bottleneck resolution in discrete and batch manufacturing.

- **professional-communication** — `/Users/melbourne/.agents/skills/professional-communication` — Draft or improve management emails, messages, memos, announcements, requests, escalations, follow-ups, and stakeholder communications with clear intent.

- **professional-proofreader** — `/Users/melbourne/.agents/skills/professional-proofreader` — >

- **programmatic-seo** — `/Users/melbourne/.agents/skills/programmatic-seo` — When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," "location pages," "[keyword] + 

- **progressive-estimation** — `/Users/melbourne/.agents/skills/progressive-estimation` — Estimate AI-assisted and hybrid human+agent development work with research-backed PERT statistics and calibration feedback loops

- **progressive-web-app** — `/Users/melbourne/.agents/skills/progressive-web-app` — Build Progressive Web Apps (PWAs) with offline support, installability, and caching strategies. Trigger whenever the user mentions PWA, service workers, web app manifests, Workbox, 'add to home screen', or wants their we

- **project-development** — `/Users/melbourne/.agents/skills/project-development` — This skill covers the principles for identifying tasks suited to LLM processing, designing effective project architectures, and iterating rapidly using agent-assisted development.

- **project-management** — `/Users/melbourne/.agents/skills/project-management` — Plan and control projects using scope, deliverables, milestones, work breakdown, owners, dependencies, risks, change control, status, and acceptance criteria.

- **project-skill-audit** — `/Users/melbourne/.agents/skills/project-skill-audit` — Audit a project and recommend the highest-value skills to add or update.

- **projection-patterns** — `/Users/melbourne/.agents/skills/projection-patterns` — Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing query performance in event-sourced systems.

- **prometheus-configuration** — `/Users/melbourne/.agents/skills/prometheus-configuration` — Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules.

- **prompt-caching** — `/Users/melbourne/.agents/skills/prompt-caching` — Caching strategies for LLM prompts including Anthropic prompt

- **prompt-engineer** — `/Users/melbourne/.agents/skills/prompt-engineer` — Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density, RACE, RISE, STAR, SOAP, CLEAR, GROW)

- **prompt-engineering** — `/Users/melbourne/.agents/skills/prompt-engineering` — Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn prompting strategies, or debug agent behavior.

- **prompt-engineering-patterns** — `/Users/melbourne/.agents/skills/prompt-engineering-patterns` — Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability.

- **prompt-library** — `/Users/melbourne/.agents/skills/prompt-library` — A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) and community best practices.

- **promql-cli** — `/Users/melbourne/.agents/skills/promql-cli` — CLI for querying Prometheus and PromQL-compatible engines (Thanos, Cortex, VictoriaMetrics, Grafana Mimir, Grafana Tempo...) — instant queries, range queries, metric discovery (metrics/labels/meta subcommands), output fo

- **proof-point-packager** — `/Users/melbourne/.agents/skills/proof-point-packager` — Use when the user asks to "package our proof points", "build reusable stat cards and case snippets", or "put proof where each pillar makes its claim"; turns claims-ledger-approved proofs into reusable proof modules — sta

- **prospecting** — `/Users/melbourne/.agents/skills/prospecting` — When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or local small businesses. Also use when the user mentions "prospecting," "build a prospect list," "find

- **protect-mcp-governance** — `/Users/melbourne/.agents/skills/protect-mcp-governance` — Agent governance skill for MCP tool calls — Cedar policy authoring, shadow-to-enforce rollout, and Ed25519 receipt verification.

- **protocol-reverse-engineering** — `/Users/melbourne/.agents/skills/protocol-reverse-engineering` — Comprehensive techniques for capturing, analyzing, and documenting network protocols for security research, interoperability, and debugging.

- **prototype** — `/Users/melbourne/.agents/skills/prototype` — Build a throwaway prototype to flesh out a design — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route.

- **public-relations** — `/Users/melbourne/.agents/skills/public-relations` — When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). Also use when the user mentions 'PR,' 'public relations,' 'press,' 'press release,

- **pubmed-database** — `/Users/melbourne/.agents/skills/pubmed-database` — Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use this for direct HTTP/REST work or custom A

- **puzzle-activity-planner** — `/Users/melbourne/.agents/skills/puzzle-activity-planner` — Plan puzzle-based activities for classrooms, parties, and events with pre-configured generator links

- **pydantic-ai** — `/Users/melbourne/.agents/skills/pydantic-ai` — Build production-ready AI agents with PydanticAI — type-safe tool use, structured outputs, dependency injection, and multi-model support.

- **pydantic-models-py** — `/Users/melbourne/.agents/skills/pydantic-models-py` — Create Pydantic models following the multi-model pattern for clean API contracts.

- **pypict-skill** — `/Users/melbourne/.agents/skills/pypict-skill` — Pairwise test generation

- **python-development** — `/Users/melbourne/.agents/skills/python-development` — You are a Python project architecture expert specializing in scaffolding production-ready Python applications. Generate complete project structures with modern tooling (uv, FastAPI, Django), type hint (Alias for python-d

- **python-development-python-scaffold** — `/Users/melbourne/.agents/skills/python-development-python-scaffold` — You are a Python project architecture expert specializing in scaffolding production-ready Python applications. Generate complete project structures with modern tooling (uv, FastAPI, Django), type hint

- **python-fastapi-development** — `/Users/melbourne/.agents/skills/python-fastapi-development` — Python FastAPI backend development with async patterns, SQLAlchemy, Pydantic, authentication, and production API patterns.

- **python-packaging** — `/Users/melbourne/.agents/skills/python-packaging` — Comprehensive guide to creating, structuring, and distributing Python packages using modern packaging tools, pyproject.toml, and publishing to PyPI.

- **python-patterns** — `/Users/melbourne/.agents/skills/python-patterns` — Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying.

- **python-performance-optimization** — `/Users/melbourne/.agents/skills/python-performance-optimization` — Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving application performance.

- **python-pptx-generator** — `/Users/melbourne/.agents/skills/python-pptx-generator` — Generate complete Python scripts that build polished PowerPoint decks with python-pptx and real slide content.

- **python-pro** — `/Users/melbourne/.agents/skills/python-pro` — Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest Python ecosystem including uv, ruff, pydantic, and FastAPI.

- **python-testing-patterns** — `/Users/melbourne/.agents/skills/python-testing-patterns` — Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing testing best practices.

- **q-infographics** — `/Users/melbourne/.agents/skills/q-infographics` — Convert documents into business stories and infographics. Use for turning reports, documents, or text into visual summaries or infographics.

- **qiskit** — `/Users/melbourne/.agents/skills/qiskit` — Qiskit is the world's most popular open-source quantum computing framework with 13M+ downloads. Build quantum circuits, optimize for hardware, execute on simulators or real quantum computers, and analyze results. Support

- **qr-code-generation** — `/Users/melbourne/.agents/skills/qr-code-generation` — Generate artistic and stylized QR codes using each::sense AI. Create branded QR codes, QR codes with logos, artistic designs, and custom themes that remain scannable while looking visually stunning.

- **quality-continuous-improvement** — `/Users/melbourne/.agents/skills/quality-continuous-improvement` — Run structured problem solving, root-cause analysis, corrective actions, quality reviews, lessons learned, and continuous improvement cycles.

- **quality-nonconformance** — `/Users/melbourne/.agents/skills/quality-nonconformance` — Codified expertise for quality control, non-conformance investigation, root cause analysis, corrective action, and supplier quality management in regulated manufacturing.

- **quant-analyst** — `/Users/melbourne/.agents/skills/quant-analyst` — Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statistical arbitrage.

- **quarterly-planning-review** — `/Users/melbourne/.agents/skills/quarterly-planning-review` — Run quarterly strategy and planning reviews covering assumptions, objectives, portfolio value, capacity, budget outlook, risks, trade-offs, and next-quarter commitments.

- **radix-ui-design-system** — `/Users/melbourne/.agents/skills/radix-ui-design-system` — Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component patterns for production-grade UI libraries.

- **rag-engineer** — `/Users/melbourne/.agents/skills/rag-engineer` — Expert in building Retrieval-Augmented Generation systems. Masters

- **rag-implementation** — `/Users/melbourne/.agents/skills/rag-implementation` — RAG (Retrieval-Augmented Generation) implementation workflow covering embedding selection, vector database setup, chunking strategies, and retrieval optimization.

- **rank-tracker** — `/Users/melbourne/.agents/skills/rank-tracker` — Use when the user asks to "track rankings" or "查排名"; measures keyword and SERP-position deltas over time from provided exports or connected tools, including AI-response checks. Not for multi-metric stakeholder reports or

- **rayden-code** — `/Users/melbourne/.agents/skills/rayden-code` — Generate React code with Rayden UI components using correct props, tokens, and premium layout patterns

- **rayden-use** — `/Users/melbourne/.agents/skills/rayden-use` — Build and maintain Rayden UI components and screens in Figma via Figma MCP with full design token enforcement

- **react-best-practices** — `/Users/melbourne/.agents/skills/react-best-practices` — Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Use when writing new React components or Next.js pages, implementing data fetching (client or server-side), or review

- **react-component-performance** — `/Users/melbourne/.agents/skills/react-component-performance` — Diagnose slow React components and suggest targeted performance fixes.

- **react-flow-architect** — `/Users/melbourne/.agents/skills/react-flow-architect` — Build production-ready ReactFlow applications with hierarchical navigation, performance optimization, and advanced state management.

- **react-flow-node-ts** — `/Users/melbourne/.agents/skills/react-flow-node-ts` — Create React Flow node components following established patterns with proper TypeScript types and store integration.

- **react-modernization** — `/Users/melbourne/.agents/skills/react-modernization` — Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation.

- **react-native-architecture** — `/Users/melbourne/.agents/skills/react-native-architecture` — Production-ready patterns for React Native development with Expo, including navigation, state management, native modules, and offline-first architecture.

- **react-native-skills** — `/Users/melbourne/.agents/skills/react-native-skills` — Use when working with react-native-skills tasks or workflows

- **react-nextjs-development** — `/Users/melbourne/.agents/skills/react-nextjs-development` — React and Next.js 14+ application development with App Router, Server Components, TypeScript, Tailwind CSS, and modern frontend patterns.

- **react-patterns** — `/Users/melbourne/.agents/skills/react-patterns` — Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices.

- **react-state-management** — `/Users/melbourne/.agents/skills/react-state-management` — Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or choosing between state management solutions.

- **react-ui-patterns** — `/Users/melbourne/.agents/skills/react-ui-patterns` — Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or managing UI states.

- **reactivation-specialist** — `/Users/melbourne/.agents/skills/reactivation-specialist` — Use when the user asks to "build a win-back campaign", "re-engage lapsed subscribers", "run a re-permission / re-consent sweep", or "sunset my dead list"; produces a closed-loop reactivation program — a lapsed-cohort def

- **readme** — `/Users/melbourne/.agents/skills/readme` — You are an expert technical writer creating comprehensive project documentation. Your goal is to write a README.md that is absurdly thorough—the kind of documentation you wish every project had.

- **real-estate-photo-generation** — `/Users/melbourne/.agents/skills/real-estate-photo-generation` — Generate professional real estate photography, virtual staging, interior design visuals, and architectural renders using each::sense API

- **recallmax** — `/Users/melbourne/.agents/skills/recallmax` — FREE — God-tier long-context memory for AI agents. Injects 500K-1M clean tokens, auto-summarizes with tone/intent preservation, compresses 14-turn history into 800 tokens.

- **receiving-code-review** — `/Users/melbourne/.agents/skills/receiving-code-review` — Code review requires technical evaluation, not emotional performance.

- **recsys-pipeline-architect** — `/Users/melbourne/.agents/skills/recsys-pipeline-architect` — Designs composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framework

- **recursive-context-pruning-token-budgeting** — `/Users/melbourne/.agents/skills/recursive-context-pruning-token-budgeting` — Optimizes AI agent performance by pruning redundant context, managing token usage, and enforcing ultra-concise, direct-to-value responses.

- **red-team-tactics** — `/Users/melbourne/.agents/skills/red-team-tactics` — Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting.

- **red-team-tools** — `/Users/melbourne/.agents/skills/red-team-tools` — Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance, vulnerability discovery, and bug bounty hunting. Automate common tasks while maintaining thorough coverage of 

- **reddit-automation** — `/Users/melbourne/.agents/skills/reddit-automation` — Automate Reddit tasks via Rube MCP (Composio): search subreddits, create posts, manage comments, and browse top content. Always search tools first for current schemas.

- **redesign-existing-projects** — `/Users/melbourne/.agents/skills/redesign-existing-projects` — Use when upgrading existing websites or apps by auditing generic UI patterns and applying premium design fixes without rewrites.

- **reference-builder** — `/Users/melbourne/.agents/skills/reference-builder` — Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searchable reference materials.

- **reference-image-composition** — `/Users/melbourne/.agents/skills/reference-image-composition` — Use one or more reference images to preserve people, products, logos, locations, poses, style cues, or composition while creating a controlled new visual.

- **referral-program** — `/Users/melbourne/.agents/skills/referral-program` — You are an expert in viral growth and referral marketing with access to referral program data and third-party tools. Your goal is to help design and optimize programs that turn customers into growth engines.

- **referrals** — `/Users/melbourne/.agents/skills/referrals` — When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. Also use when the user mentions 'referral,' 'affiliate,' 'ambassador,' 'word of mouth,' 'viral loop,' 

- **rehabilitation-analyzer** — `/Users/melbourne/.agents/skills/rehabilitation-analyzer` — 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议

- **remote-gpu-trainer** — `/Users/melbourne/.agents/skills/remote-gpu-trainer` — Deploy, monitor, and debug long GPU jobs on RENTED/remote instances (AutoDL, RunPod, vast.ai, Lambda, Slurm, K8s): teardown/billing safety, spot resilience, resumable checkpointing, OOM/NaN triage.

- **remotion** — `/Users/melbourne/.agents/skills/remotion` — Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays

- **remotion-best-practices** — `/Users/melbourne/.agents/skills/remotion-best-practices` — Best practices for Remotion - Video creation in React

- **remotion-video** — `/Users/melbourne/.agents/skills/remotion-video` — This skill should be used when the user asks to "make a video with Remotion", "create a programmatic/data-driven video in React", "render an MP4/GIF from code", "animate with useCurrentFrame/interpolate/spring", "sync vi

- **render-automation** — `/Users/melbourne/.agents/skills/render-automation` — Automate Render tasks via Rube MCP (Composio): services, deployments, projects. Always search tools first for current schemas.

- **report-generator** — `/Users/melbourne/.agents/skills/report-generator` — Use when the user asks to "create a campaign report", "build an executive summary", or "deliver client results"; produces audience-tailored influencer marketing reports (executive, client, internal team) with data tables

- **requesting-code-review** — `/Users/melbourne/.agents/skills/requesting-code-review` — Use when completing tasks, implementing major features, or before merging to verify work meets requirements

- **resource-capacity-management** — `/Users/melbourne/.agents/skills/resource-capacity-management` — Plan and balance people, time, workload, and delivery capacity across teams and projects using demand, constraints, priorities, dependencies, and bottlenecks.

- **resume-design-generation** — `/Users/melbourne/.agents/skills/resume-design-generation` — Generate professional resume and CV designs using each::sense AI. Create modern, creative, minimalist, executive, tech, academic, infographic, two-column, ATS-friendly, and portfolio-style resumes optimized for various i

- **returns-reverse-logistics** — `/Users/melbourne/.agents/skills/returns-reverse-logistics` — Codified expertise for returns authorisation, receipt and inspection, disposition decisions, refund processing, fraud detection, and warranty claims management.

- **reverse-engineer** — `/Users/melbourne/.agents/skills/reverse-engineer` — Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. Masters IDA Pro, Ghidra, radare2, x64dbg, and modern RE toolchains.

- **revops** — `/Users/melbourne/.agents/skills/revops` — When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. Also use when the user mentions 'RevOps,' 'revenue operations,' 'lead scoring,' 'lead routing,' 'MQL,'

- **rich-elicitation** — `/Users/melbourne/.agents/skills/rich-elicitation` — Asks clarifying questions in multiple rounds before starting ambiguous tasks. Fires when 2+ task dimensions each have 3+ viable answers.

- **risk-management** — `/Users/melbourne/.agents/skills/risk-management` — Identify, assess, prioritize, mitigate, monitor, and escalate operational, project, financial, supplier, compliance, and strategic management risks.

- **risk-manager** — `/Users/melbourne/.agents/skills/risk-manager` — Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses.

- **risk-metrics-calculation** — `/Users/melbourne/.agents/skills/risk-metrics-calculation` — Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monitoring systems.

- **robius-app-architecture** — `/Users/melbourne/.agents/skills/robius-app-architecture` — |

- **robius-event-action** — `/Users/melbourne/.agents/skills/robius-event-action` — |

- **robius-matrix-integration** — `/Users/melbourne/.agents/skills/robius-matrix-integration` — |

- **robius-state-management** — `/Users/melbourne/.agents/skills/robius-state-management` — |

- **robius-widget-patterns** — `/Users/melbourne/.agents/skills/robius-widget-patterns` — |

- **roi-calculator** — `/Users/melbourne/.agents/skills/roi-calculator` — Use when the user asks to "calculate influencer ROI", "prove campaign value", or "what was our ROAS"; produces direct ROI/ROAS, earned media value, attribution-modeled revenue, LTV-based ROI, and a stakeholder-ready summ

- **ruby-pro** — `/Users/melbourne/.agents/skills/ruby-pro` — Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem development, and testing frameworks.

- **runapi-cli** — `/Users/melbourne/.agents/skills/runapi-cli` — Generate AI images, videos, and music/audio from agents using the RunAPI CLI.

- **runaway-guard** — `/Users/melbourne/.agents/skills/runaway-guard` — Cost-safety discipline for paid AI / inference APIs: treat $-cost as a third complexity dimension alongside time and space. Forces a written per-run $-cap, per-day $-cap, max-iterations bound, concurrency limit, and a ma

- **rust-async-patterns** — `/Users/melbourne/.agents/skills/rust-async-patterns` — Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when building async Rust applications, implementing concurrent systems, or debugging async code.

- **rust-pro** — `/Users/melbourne/.agents/skills/rust-pro` — Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming.

- **saas-multi-tenant** — `/Users/melbourne/.agents/skills/saas-multi-tenant` — Design and implement multi-tenant SaaS architectures with row-level security, tenant-scoped queries, shared-schema isolation, and safe cross-tenant admin patterns in PostgreSQL and TypeScript.

- **saas-mvp-launcher** — `/Users/melbourne/.agents/skills/saas-mvp-launcher` — Use when planning or building a SaaS MVP from scratch. Provides a structured roadmap covering tech stack, architecture, auth, payments, and launch checklist.

- **saga-orchestration** — `/Users/melbourne/.agents/skills/saga-orchestration` — Patterns for managing distributed transactions and long-running business processes.

- **sales-automator** — `/Users/melbourne/.agents/skills/sales-automator` — Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. Use PROACTIVELY for sales outreach or lead nurturing. 

- **sales-enablement** — `/Users/melbourne/.agents/skills/sales-enablement` — When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user mentions 'sales deck,' 'pitch deck,' 'one-pager,' 'leave-behind,' 'objection handl

- **sales-enablement-kit** — `/Users/melbourne/.agents/skills/sales-enablement-kit` — Use when the user asks to "build battle cards", "prep the sales team for launch", or "write the internal launch FAQ"; produces the internal enablement kit for a sales-led launch — battle cards vs each named alternative (

- **salesforce-automation** — `/Users/melbourne/.agents/skills/salesforce-automation` — Automate Salesforce tasks via Rube MCP (Composio): leads, contacts, accounts, opportunities, SOQL queries. Always search tools first for current schemas.

- **salesforce-development** — `/Users/melbourne/.agents/skills/salesforce-development` — Expert patterns for Salesforce platform development including

- **sam-altman** — `/Users/melbourne/.agents/skills/sam-altman` — Agente que simula Sam Altman — CEO da OpenAI, ex-presidente da Y Combinator, arquiteto da era AGI.

- **sankhya-dashboard-html-jsp-custom-best-pratices** — `/Users/melbourne/.agents/skills/sankhya-dashboard-html-jsp-custom-best-pratices` — This skill should be used when the user asks for patterns, best practices, creation, or fixing of Sankhya dashboards using HTML, JSP, Java, and SQL.

- **sast-configuration** — `/Users/melbourne/.agents/skills/sast-configuration` — Static Application Security Testing (SAST) tool setup, configuration, and custom rule creation for comprehensive security scanning across multiple programming languages.

- **satori** — `/Users/melbourne/.agents/skills/satori` — Clinically informed wisdom companion blending psychology and philosophy into a structured thinking partner

- **scala-pro** — `/Users/melbourne/.agents/skills/scala-pro` — Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pekko, Akka, Spark, ZIO/Cats Effect, and reactive architectures.

- **scanning-tools** — `/Users/melbourne/.agents/skills/scanning-tools` — Master essential security scanning tools for network discovery, vulnerability assessment, web application testing, wireless security, and compliance validation. This skill covers tool selection, configuration, and practi

- **scanpy** — `/Users/melbourne/.agents/skills/scanpy` — Scanpy is a scalable Python toolkit for analyzing single-cell RNA-seq data, built on AnnData. Apply this skill for complete single-cell workflows including quality control, normalization, dimensionality reduction, cluste

- **scarcity-urgency-psychologist** — `/Users/melbourne/.agents/skills/scarcity-urgency-psychologist` — One sentence - what this skill does and when to invoke it

- **schema** — `/Users/melbourne/.agents/skills/schema` — When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup," "structured data," "JSON-LD," "rich snippets," "schema.org," "FAQ schema," "p

- **schema-markup** — `/Users/melbourne/.agents/skills/schema-markup` — Design, validate, and optimize schema.org structured data for eligibility, correctness, and measurable SEO impact.

- **schema-markup-generator** — `/Users/melbourne/.agents/skills/schema-markup-generator` — Generate and implement JSON-LD structured data for web apps, blogs, FAQs, and SaaS sites. Supports WebSite, SoftwareApplication, BlogPosting, FAQPage, HowTo, and more.

- **scientific-writing** — `/Users/melbourne/.agents/skills/scientific-writing` — This is the core skill for the deep research and writing tool—combining AI-driven deep research with well-formatted written outputs. Every document produced is backed by comprehensive literature search and verified citat

- **scikit-learn** — `/Users/melbourne/.agents/skills/scikit-learn` — Machine learning in Python with scikit-learn. Use for classification, regression, clustering, model evaluation, and ML pipelines.

- **screen-reader-testing** — `/Users/melbourne/.agents/skills/screen-reader-testing` — Practical guide to testing web applications with screen readers for comprehensive accessibility validation.

- **screenshots** — `/Users/melbourne/.agents/skills/screenshots` — Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or documentation.

- **screenstudio-alt** — `/Users/melbourne/.agents/skills/screenstudio-alt` — Open-source headless Screen Studio alternative: auto speed-up of idle, auto-zoom on click clusters, keystroke overlay chips, smoothed synthetic cursor, and 9:16 vertical export that follows the action — post-production f

- **scroll-experience** — `/Users/melbourne/.agents/skills/scroll-experience` — Expert in building immersive scroll-driven experiences - parallax

- **seaborn** — `/Users/melbourne/.agents/skills/seaborn` — Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plotting, multivariate analysis, automatic statistical estimation, and complex multi-pa

- **seamless-pattern-generation** — `/Users/melbourne/.agents/skills/seamless-pattern-generation` — Generate seamless, tileable patterns using each::sense AI. Create repeating patterns for textiles, wallpapers, gift wrap, digital backgrounds, and surface designs that tile perfectly without visible seams.

- **search-specialist** — `/Users/melbourne/.agents/skills/search-specialist` — Expert web researcher using advanced search techniques and

- **search-term-miner** — `/Users/melbourne/.agents/skills/search-term-miner` — Use when the user asks to "mine my search terms", "find new keywords from converting queries", "build a negative-keyword list", or "cut wasted paid spend"; harvests converting queries into new keywords/ad-groups, builds 

- **secrets-management** — `/Users/melbourne/.agents/skills/secrets-management` — Secure secrets management practices for CI/CD pipelines using Vault, AWS Secrets Manager, and other tools.

- **section-dividers** — `/Users/melbourne/.agents/skills/section-dividers` — This skill should be used when the user asks to "create section dividers", "make transparent dividers", "generate decorative borders", "create parallax dividers", "design section transitions", "make HR dividers", "crysta

- **security-audit** — `/Users/melbourne/.agents/skills/security-audit` — Comprehensive security auditing workflow covering web application testing, API security, penetration testing, vulnerability scanning, and security hardening.

- **security-auditor** — `/Users/melbourne/.agents/skills/security-auditor` — Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks.

- **security-bluebook-builder** — `/Users/melbourne/.agents/skills/security-bluebook-builder` — Build a minimal but real security policy for sensitive apps. The output is a single, coherent Blue Book document using MUST/SHOULD/CAN language, with explicit assumptions, scope, and security gates.

- **security-compliance-compliance-check** — `/Users/melbourne/.agents/skills/security-compliance-compliance-check` — You are a compliance expert specializing in regulatory requirements for software systems including GDPR, HIPAA, SOC2, PCI-DSS, and other industry standards. Perform comprehensive compliance audits and provide implementat

- **security-requirement-extraction** — `/Users/melbourne/.agents/skills/security-requirement-extraction` — Derive security requirements from threat models and business context. Use when translating threats into actionable requirements, creating security user stories, or building security test cases.

- **security-scanning-security-dependencies** — `/Users/melbourne/.agents/skills/security-scanning-security-dependencies` — You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and supply chain security. Scan project dependencies across multiple ecosystems to identify vulnerabilities, assess risks, and

- **security-scanning-security-hardening** — `/Users/melbourne/.agents/skills/security-scanning-security-hardening` — Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls.

- **security-scanning-security-sast** — `/Users/melbourne/.agents/skills/security-scanning-security-sast` — Static Application Security Testing (SAST) for code vulnerability

- **seek-and-analyze-video** — `/Users/melbourne/.agents/skills/seek-and-analyze-video` — Seek and analyze video content using Memories.ai Large Visual Memory Model for persistent video intelligence

- **segment-automation** — `/Users/melbourne/.agents/skills/segment-automation` — Automate Segment tasks via Rube MCP (Composio): track events, identify users, manage groups, page views, aliases, batch operations. Always search tools first for current schemas.

- **segment-cdp** — `/Users/melbourne/.agents/skills/segment-cdp` — Expert patterns for Segment Customer Data Platform including

- **segment-image** — `/Users/melbourne/.agents/skills/segment-image` — This skill should be used when the user asks to "segment an image", "identify objects", "extract objects", "generate masks", "find objects in image", or needs AI-powered image segmentation.

- **semgrep-rule-creator** — `/Users/melbourne/.agents/skills/semgrep-rule-creator` — Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

- **semgrep-rule-variant-creator** — `/Users/melbourne/.agents/skills/semgrep-rule-variant-creator` — Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for eac

- **send-experiment-designer** — `/Users/melbourne/.agents/skills/send-experiment-designer` — Use when the user asks to "design an email A/B test", "set up a multivariate subject/CTA test", "run a send-time test", "build a hold-out group", or "is this email result statistically and practically material?"; produce

- **sendgrid-automation** — `/Users/melbourne/.agents/skills/sendgrid-automation` — Automate SendGrid email delivery workflows including marketing campaigns (Single Sends), contact and list management, sender identity setup, and email analytics through Composio's SendGrid toolkit.

- **senior-architect** — `/Users/melbourne/.agents/skills/senior-architect` — Complete toolkit for senior architect with modern tools and best practices.

- **senior-frontend** — `/Users/melbourne/.agents/skills/senior-frontend` — Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. Use when building React components, optimizing Next.js performance, analyzing bundle sizes, scaffolding frontend projects, impleme

- **senior-fullstack** — `/Users/melbourne/.agents/skills/senior-fullstack` — Complete toolkit for senior fullstack with modern tools and best practices.

- **sentry-automation** — `/Users/melbourne/.agents/skills/sentry-automation` — Automate Sentry tasks via Rube MCP (Composio): manage issues/events, configure alerts, track releases, monitor projects and teams. Always search tools first for current schemas.

- **seo** — `/Users/melbourne/.agents/skills/seo` — Run a broad SEO audit across technical SEO, on-page SEO, schema, sitemaps, content quality, AI search readiness, and GEO. Use as the umbrella skill when the user asks for a full SEO analysis or strategy.

- **seo-aeo-blog-writer** — `/Users/melbourne/.agents/skills/seo-aeo-blog-writer` — Writes long-form blog posts with TL;DR block, definition sentence, comparison table, and 5-question FAQ for SEO ranking and AEO citation. Activate when the user wants to write a blog post, article, or long-form content p

- **seo-aeo-content-cluster** — `/Users/melbourne/.agents/skills/seo-aeo-content-cluster` — Builds a topical authority map with a pillar page, prioritised cluster articles, content types, internal link map, and content gap analysis. Activate when the user wants to build a content cluster, topic map, or content 

- **seo-aeo-content-quality-auditor** — `/Users/melbourne/.agents/skills/seo-aeo-content-quality-auditor` — Audits content for SEO and AEO performance with scored reports, severity-ranked fix lists, and projected scores after fixes. Activate when the user wants to audit, review, or score content for SEO or AEO compliance.

- **seo-aeo-internal-linking** — `/Users/melbourne/.agents/skills/seo-aeo-internal-linking` — Maps internal link opportunities between pages with anchor text, placement instructions, orphan page detection, and cannibalization checks. Activate when the user wants to build an internal linking strategy or find link 

- **seo-aeo-keyword-research** — `/Users/melbourne/.agents/skills/seo-aeo-keyword-research` — Researches and prioritises SEO keywords with AEO question queries, difficulty tiers, cannibalization checks, and a content map. Activate when the user wants to find keywords, research search terms, or build a keyword str

- **seo-aeo-landing-page-writer** — `/Users/melbourne/.agents/skills/seo-aeo-landing-page-writer` — Writes complete, structured landing pages optimized for SEO ranking, AEO citation, and visitor conversion. Activate when the user wants to write or generate a landing page for a product, service, or offer.

- **seo-aeo-meta-description-generator** — `/Users/melbourne/.agents/skills/seo-aeo-meta-description-generator` — Writes 3 title tag variants and 3 meta description variants per page with SERP preview, OG tags, and Twitter Card tags. Activate when the user wants to write meta tags, title tags, or social sharing tags for any page.

- **seo-aeo-schema-generator** — `/Users/melbourne/.agents/skills/seo-aeo-schema-generator` — Generates valid JSON-LD structured data for 10 schema types with rich result eligibility validation and implementation-ready script blocks. Activate when the user wants to generate schema markup, JSON-LD, or structured d

- **seo-audit** — `/Users/melbourne/.agents/skills/seo-audit` — When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page SEO," "meta tags review," "SEO heal

- **seo-authority-builder** — `/Users/melbourne/.agents/skills/seo-authority-builder` — Analyzes content for E-E-A-T signals and suggests improvements to

- **seo-cannibalization-detector** — `/Users/melbourne/.agents/skills/seo-cannibalization-detector` — Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. Use PROACTIVELY when reviewing similar content.

- **seo-competitor-pages** — `/Users/melbourne/.agents/skills/seo-competitor-pages` — >

- **seo-content** — `/Users/melbourne/.agents/skills/seo-content` — >

- **seo-content-auditor** — `/Users/melbourne/.agents/skills/seo-content-auditor` — Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations based on established guidelines.

- **seo-content-planner** — `/Users/melbourne/.agents/skills/seo-content-planner` — Creates comprehensive content outlines and topic clusters for SEO.

- **seo-content-refresher** — `/Users/melbourne/.agents/skills/seo-content-refresher` — Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need updating. Use PROACTIVELY for older content.

- **seo-content-writer** — `/Users/melbourne/.agents/skills/seo-content-writer` — Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices. Use PROACTIVELY for content creation tasks.

- **seo-dataforseo** — `/Users/melbourne/.agents/skills/seo-dataforseo` — Use DataForSEO for live SERPs, keyword metrics, backlinks, competitor analysis, on-page checks, and AI visibility data. Trigger when the user needs real SEO data rather than static guidance.

- **seo-forensic-incident-response** — `/Users/melbourne/.agents/skills/seo-forensic-incident-response` — Investigate sudden drops in organic traffic or rankings and run a structured forensic SEO incident response with triage, root-cause analysis and recovery plan.

- **seo-fundamentals** — `/Users/melbourne/.agents/skills/seo-fundamentals` — Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality, and how modern search engines evaluate pages.

- **seo-geo** — `/Users/melbourne/.agents/skills/seo-geo` — Optimize content for AI Overviews, ChatGPT, Perplexity, and other AI search systems. Use when improving GEO, AI citations, llms.txt readiness, crawler accessibility, and passage-level citability.

- **seo-hreflang** — `/Users/melbourne/.agents/skills/seo-hreflang` — >

- **seo-image-gen** — `/Users/melbourne/.agents/skills/seo-image-gen` — Generate SEO-focused images such as OG cards, hero images, schema assets, product visuals, and infographics. Use when image generation is part of an SEO workflow or content publishing task.

- **seo-images** — `/Users/melbourne/.agents/skills/seo-images` — >

- **seo-keyword-strategist** — `/Users/melbourne/.agents/skills/seo-keyword-strategist` — Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. Prevents over-optimization. Use PROACTIVELY for content optimization.

- **seo-meta-optimizer** — `/Users/melbourne/.agents/skills/seo-meta-optimizer` — Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyword-rich metadata. Use PROACTIVELY for new content.

- **seo-page** — `/Users/melbourne/.agents/skills/seo-page` — >

- **seo-plan** — `/Users/melbourne/.agents/skills/seo-plan` — >

- **seo-programmatic** — `/Users/melbourne/.agents/skills/seo-programmatic` — Plan and audit programmatic SEO pages generated at scale from structured data. Use when designing templates, URL systems, internal linking, quality gates, and index-bloat safeguards for pages at scale.

- **seo-schema** — `/Users/melbourne/.agents/skills/seo-schema` — >

- **seo-sitemap** — `/Users/melbourne/.agents/skills/seo-sitemap` — >

- **seo-snippet-hunter** — `/Users/melbourne/.agents/skills/seo-snippet-hunter` — Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices. Use PROACTIVELY for question-based content.

- **seo-structure-architect** — `/Users/melbourne/.agents/skills/seo-structure-architect` — Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates search-friendly content organization.

- **seo-technical** — `/Users/melbourne/.agents/skills/seo-technical` — Audit technical SEO across crawlability, indexability, security, URLs, mobile, Core Web Vitals, structured data, JavaScript rendering, and related platform signals like robots.txt and AI crawler access.

- **sequence-psychologist** — `/Users/melbourne/.agents/skills/sequence-psychologist` — One sentence - what this skill does and when to invoke it

- **serp-analysis** — `/Users/melbourne/.agents/skills/serp-analysis` — Use when the user asks to "analyze the SERP" or "SERP分析"; maps SERP features, layout, ranking factors, search intent, AI Overviews, and snippet opportunities for a query. Not for keyword demand discovery — use keyword-re

- **serp-markup-builder** — `/Users/melbourne/.agents/skills/serp-markup-builder` — Use when the user asks to "optimize meta tags", "write title tags / meta descriptions", "add Open Graph or Twitter cards", or "generate schema / JSON-LD" for FAQ, HowTo, Article, Product, or LocalBusiness rich-result can

- **server-management** — `/Users/melbourne/.agents/skills/server-management` — Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands.

- **service-mesh-expert** — `/Users/melbourne/.agents/skills/service-mesh-expert` — Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and multi-cluster mesh con

- **service-mesh-observability** — `/Users/melbourne/.agents/skills/service-mesh-observability` — Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments.

- **session-handoff** — `/Users/melbourne/.agents/skills/session-handoff` — Creates comprehensive handoff documents for seamless AI agent session transfers. Triggered when: (1) user requests handoff/memory/context save, (2) context window approaches capacity, (3) major task milestone completed, 

- **setup** — `/Users/melbourne/.agents/skills/setup` — This skill should be used when the user asks to "set up gemskills", "configure gemskills", "choose default image/video provider", "use OpenAI for images", "use xAI/Grok for video", "switch image model", "which providers 

- **setup-matt-pocock-skills** — `/Users/melbourne/.agents/skills/setup-matt-pocock-skills` — Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills.

- **sexual-health-analyzer** — `/Users/melbourne/.agents/skills/sexual-health-analyzer` — Sexual Health Analyzer

- **shadcn** — `/Users/melbourne/.agents/skills/shadcn` — Manages shadcn/ui components and projects, providing context, documentation, and usage patterns for building modern design systems.

- **shader-glsl** — `/Users/melbourne/.agents/skills/shader-glsl` — This skill should be used when the user asks to "write a fragment shader", "make a GLSL gradient/noise/plasma background", "create an image transition (dissolve, displacement, glitch)", "add distortion or chromatic aberr

- **shader-programming-glsl** — `/Users/melbourne/.agents/skills/shader-programming-glsl` — Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects.

- **share-of-voice-tracker** — `/Users/melbourne/.agents/skills/share-of-voice-tracker` — Use when the user asks to "track our share of voice", "what share of the conversation do we own vs competitors", or "trend our SOV this quarter"; computes SOV% = brand mentions ÷ (brand + competitor panel mentions) per p

- **sharp-coder** — `/Users/melbourne/.agents/skills/sharp-coder` — >

- **sharp-edges** — `/Users/melbourne/.agents/skills/sharp-edges` — sharp-edges

- **shellcheck-configuration** — `/Users/melbourne/.agents/skills/shellcheck-configuration` — Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability.

- **shodan-reconnaissance** — `/Users/melbourne/.agents/skills/shodan-reconnaissance` — Provide systematic methodologies for leveraging Shodan as a reconnaissance tool during penetration testing engagements.

- **shopify-apps** — `/Users/melbourne/.agents/skills/shopify-apps` — Expert patterns for Shopify app development including Remix/React

- **shopify-automation** — `/Users/melbourne/.agents/skills/shopify-automation` — Automate Shopify tasks via Rube MCP (Composio): products, orders, customers, inventory, collections. Always search tools first for current schemas.

- **shopify-development** — `/Users/melbourne/.agents/skills/shopify-development` — Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid.

- **short-video-scripter** — `/Users/melbourne/.agents/skills/short-video-scripter` — Use when the user asks to "script this short video", "write a TikTok / Reels / Shorts script", "给这条抖音或视频号视频写脚本", or "fix the hook — viewers drop off in the first seconds"; produces timestamped beat-sheet scripts on the r

- **shot-composition** — `/Users/melbourne/.agents/skills/shot-composition` — This skill should be used when the user asks to "compose a frame", "set up a grid", "plan shot composition", "place the focal point", "decide where elements enter and exit", "add a parallax/camera move", "adapt a layout 

- **signup** — `/Users/melbourne/.agents/skills/signup` — When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup conversions," "registration friction," "signup form optimization," "free trial si

- **signup-flow-cro** — `/Users/melbourne/.agents/skills/signup-flow-cro` — You are an expert in optimizing signup and registration flows. Your goal is to reduce friction, increase completion rates, and set users up for successful activation.

- **similarity-search-patterns** — `/Users/melbourne/.agents/skills/similarity-search-patterns` — Implement efficient similarity search with vector databases. Use when building semantic search, implementing nearest neighbor queries, or optimizing retrieval performance.

- **simplify-code** — `/Users/melbourne/.agents/skills/simplify-code` — Review a diff for clarity and safe simplifications, then optionally apply low-risk fixes.

- **site-architecture** — `/Users/melbourne/.agents/skills/site-architecture` — When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. Also use when the user mentions "sitemap," "site map," "visual sitemap," "site structure," 

- **site-launch-checklist** — `/Users/melbourne/.agents/skills/site-launch-checklist` — Pre-launch checklist for shipping a new website or web app. Scope: analytics (GA4, PostHog, Google Search Console, Ahrefs), DNS, TLS and backups, legal and CNIL/GDPR compliance, security headers, SEO and GEO (robots.txt,

- **site-structure-optimizer** — `/Users/melbourne/.agents/skills/site-structure-optimizer` — Use when the user asks to "plan my site structure", "design the page hierarchy / navigation / URL taxonomy", "fix internal linking", or "find orphan pages"; runs two modes — architecture (hierarchy, nav, URL patterns, hu

- **skill-audit** — `/Users/melbourne/.agents/skills/skill-audit` — Pre-install security scanner for AI agent skills. 7.5% of 14,706 skills are malicious. Audit before you trust.

- **skill-check** — `/Users/melbourne/.agents/skills/skill-check` — Validate Claude Code skills against the agentskills specification. Catches structural, semantic, and naming issues before users do.

- **skill-creator** — `/Users/melbourne/.agents/skills/skill-creator` — To create new CLI skills following Anthropic's official best practices with zero manual configuration. This skill automates brainstorming, template application, validation, and installation processes while maintaining pr

- **skill-creator-ms** — `/Users/melbourne/.agents/skills/skill-creator-ms` — Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. Use when creating new skills or updating existing skills.

- **skill-developer** — `/Users/melbourne/.agents/skills/skill-developer` — Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, following Anthropic's official best practices including the 500-line rule and progressive disclosure pattern.

- **skill-improver** — `/Users/melbourne/.agents/skills/skill-improver` — Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards. Use when improving a skill with multiple quality issues, iterating on a new skill until it meets standards, or auto

- **skill-installer** — `/Users/melbourne/.agents/skills/skill-installer` — Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao.

- **skill-issue** — `/Users/melbourne/.agents/skills/skill-issue` — Find out why a coding-agent skill won't fire — grade each SKILL.md A–F on activation, simulate which skill a prompt triggers, and flag collisions where one silently shadows another.

- **skill-optimizer** — `/Users/melbourne/.agents/skills/skill-optimizer` — Diagnose and optimize Agent Skills (SKILL.md) with real session data and research-backed static analysis. Works with Claude Code, Codex, and any Agent Skills-compatible agent.

- **skill-progressive-disclosure-design** — `/Users/melbourne/.agents/skills/skill-progressive-disclosure-design` — Decide how to split skill content between SKILL.md and reference files for context efficiency and reliable triggering. Use this whenever creating a new Claude skill, refactoring an existing one, or when a SKILL.md is gro

- **skill-rails-upgrade** — `/Users/melbourne/.agents/skills/skill-rails-upgrade` — Analyze Rails apps and provide upgrade assessments

- **skill-router** — `/Users/melbourne/.agents/skills/skill-router` — Use when the user is unsure which skill to use or where to start. Interviews the user with targeted questions and recommends the best skill(s) from the installed library for their goal.

- **skill-scanner** — `/Users/melbourne/.agents/skills/skill-scanner` — Scan agent skills for security issues before adoption. Detects prompt injection, malicious code, excessive permissions, secret exposure, and supply chain risks.

- **skill-seekers** — `/Users/melbourne/.agents/skills/skill-seekers` — -Automatically convert documentation websites, GitHub repositories, and PDFs into Claude AI skills in minutes.

- **skill-sentinel** — `/Users/melbourne/.agents/skills/skill-sentinel` — Auditoria e evolucao do ecossistema de skills. Qualidade de codigo, seguranca, custos, gaps, duplicacoes, dependencias e relatorios de saude.

- **skill-suggester** — `/Users/melbourne/.agents/skills/skill-suggester` — Scan prompt history for recurring patterns and unmet needs, then propose new skills or command templates

- **skill-writer** — `/Users/melbourne/.agents/skills/skill-writer` — Create and improve agent skills following the Agent Skills specification. Use when asked to create, write, or update skills.

- **skin-health-analyzer** — `/Users/melbourne/.agents/skills/skin-health-analyzer` — Analyze skin health data, identify skin problem patterns, assess skin health status. Supports correlation analysis with nutrition, chronic diseases, and medication data.

- **skyvern-browser-automation** — `/Users/melbourne/.agents/skills/skyvern-browser-automation` — AI-powered browser automation — navigate sites, fill forms, extract structured data, log in with stored credentials, and build reusable workflows.

- **slack-automation** — `/Users/melbourne/.agents/skills/slack-automation` — Automate Slack workspace operations including messaging, search, channel management, and reaction workflows through Composio's Slack toolkit.

- **slack-bot-builder** — `/Users/melbourne/.agents/skills/slack-bot-builder` — Build Slack apps using the Bolt framework across Python,

- **slack-gif-creator** — `/Users/melbourne/.agents/skills/slack-gif-creator` — A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack.

- **sleep-analyzer** — `/Users/melbourne/.agents/skills/sleep-analyzer` — 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。

- **slo-implementation** — `/Users/melbourne/.agents/skills/slo-implementation` — Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets.

- **smart-git-automation** — `/Users/melbourne/.agents/skills/smart-git-automation` — Smart change detection, auto branch naming, and streamlined commit/PR workflow

- **sms** — `/Users/melbourne/.agents/skills/sms` — When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts, post-purchase, win-back, promotional sends, or transactional/auth SMS. Also use when the user mentions

- **smtp-penetration-testing** — `/Users/melbourne/.agents/skills/smtp-penetration-testing` — Conduct comprehensive security assessments of SMTP (Simple Mail Transfer Protocol) servers to identify vulnerabilities including open relays, user enumeration, weak authentication, and misconfiguration.

- **snowflake-development** — `/Users/melbourne/.agents/skills/snowflake-development` — Comprehensive Snowflake development assistant covering SQL best practices, data pipeline design (Dynamic Tables, Streams, Tasks, Snowpipe), Cortex AI functions, Cortex Agents, Snowpark Python, dbt integration, performanc

- **snyk-agent-scan-compliance** — `/Users/melbourne/.agents/skills/snyk-agent-scan-compliance` — Compliance expert for snyk-agent-scan — the agent skill file scanner — NOT for other Snyk CLI tools (snyk test, snyk code SAST, snyk iac, snyk container). Fixes alerts through content restructuring, never by suppressing 

- **social** — `/Users/melbourne/.agents/skills/social` — When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms, or wants to do social listening and engagement triage. Also use 

- **social-calendar-builder** — `/Users/melbourne/.agents/skills/social-calendar-builder` — Use when the user asks to "build our social posting calendar", "set weekly slots and queue depth per channel", or "plan the evergreen recycle rotation"; produces the always-on brand calendar — pillar allocation with hero

- **social-carousel-generation** — `/Users/melbourne/.agents/skills/social-carousel-generation` — Generate social media carousel content using each::sense AI. Create educational slides, product showcases, storytelling sequences, tutorials, and more for Instagram, LinkedIn, Facebook, and other platforms.

- **social-content** — `/Users/melbourne/.agents/skills/social-content` — You are an expert social media strategist with direct access to a scheduling platform that publishes to all major social networks. Your goal is to help create engaging content that builds audience, drives engagement, and

- **social-creative-builder** — `/Users/melbourne/.agents/skills/social-creative-builder` — Use when the user asks to "turn this idea into posts for every platform", "write the X thread / LinkedIn post / 小红书 note", or "spec the carousel slides"; turns one idea into N platform-native ready-to-paste packages — po

- **social-measurement-loop** — `/Users/melbourne/.agents/skills/social-measurement-loop` — Use when the user asks to "run the weekly social readout", "which denominator does our engagement rate use", or "which posts won this week and what changes next cycle"; produces the organic-social metric dictionary (ever

- **social-media-visuals** — `/Users/melbourne/.agents/skills/social-media-visuals` — Produce platform-ready social visual concepts and image assets with strong hierarchy, mobile readability, brand consistency, crop safety, and reusable campaign variants.

- **social-metadata-hardening** — `/Users/melbourne/.agents/skills/social-metadata-hardening` — Fix social sharing previews so URLs render as rich cards on Facebook, LinkedIn, X/Twitter, WhatsApp, Telegram, and more. Covers OG tags, Twitter cards, absolute image URLs, and debugging.

- **social-orchestrator** — `/Users/melbourne/.agents/skills/social-orchestrator` — Orquestrador unificado de canais sociais — coordena Instagram, Telegram e WhatsApp em um unico fluxo de trabalho. Publicacao cross-channel, metricas unificadas, reutilizacao de conteudo por formato, agendamento sincroniz

- **social-post-writer-seo** — `/Users/melbourne/.agents/skills/social-post-writer-seo` — Social Media Strategist and Content Writer. Creates clear, engaging social media posts for Instagram, LinkedIn, and Facebook.

- **social-proof-architect** — `/Users/melbourne/.agents/skills/social-proof-architect` — One sentence - what this skill does and when to invoke it

- **social-pulse-monitor** — `/Users/melbourne/.agents/skills/social-pulse-monitor` — Use when the user asks to "monitor brand mentions", "set up social listening", "did anything spike about us this week", or "watch these accounts for buying triggers"; runs always-on keyless listening — a versioned listen

- **social-quality-auditor** — `/Users/melbourne/.agents/skills/social-quality-auditor` — Use when the user asks to "audit our social presence" or "is this batch safe to publish"; runs either the typed ECHO asset gate or a separate program-maturity profile, with channel-truth, claim, disclosure, manipulation,

- **social-selling-planner** — `/Users/melbourne/.agents/skills/social-selling-planner` — Use when the user asks to "set up my founder social-selling routine", "build a daily engagement block for target accounts", or "turn funding / hiring signals into selling plays"; produces the founder/seller daily operati

- **socialclaw** — `/Users/melbourne/.agents/skills/socialclaw` — Agent-first social media publishing skill — schedule and publish posts across 13 platforms (X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Reddit, WordPress, Pinterest) via a single workspace

- **software-architecture** — `/Users/melbourne/.agents/skills/software-architecture` — Guide for quality focused software architecture. This skill should be used when users want to write code, design architecture, analyze code, in any case that relates to software development.

- **solidity-security** — `/Users/melbourne/.agents/skills/solidity-security` — Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns.

- **spark-optimization** — `/Users/melbourne/.agents/skills/spark-optimization` — Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. Use when improving Spark performance, debugging slow jobs, or scaling data processing pipelines.

- **spec-to-code-compliance** — `/Users/melbourne/.agents/skills/spec-to-code-compliance` — Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protoco

- **speckit-updater** — `/Users/melbourne/.agents/skills/speckit-updater` — SpecKit Safe Update

- **speed** — `/Users/melbourne/.agents/skills/speed` — Launch RSVP speed reader for text

- **spline-3d-integration** — `/Users/melbourne/.agents/skills/spline-3d-integration` — Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API.

- **sponsored-newsletter-finder** — `/Users/melbourne/.agents/skills/sponsored-newsletter-finder` — >

- **sql-injection-testing** — `/Users/melbourne/.agents/skills/sql-injection-testing` — Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sanitization mechanisms.

- **sql-optimization-patterns** — `/Users/melbourne/.agents/skills/sql-optimization-patterns` — Transform slow database queries into lightning-fast operations through systematic optimization, proper indexing, and query plan analysis.

- **sql-pro** — `/Users/melbourne/.agents/skills/sql-pro` — Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data modeling, and hybrid analytical systems.

- **sqlmap-database-pentesting** — `/Users/melbourne/.agents/skills/sqlmap-database-pentesting` — Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap.

- **square-automation** — `/Users/melbourne/.agents/skills/square-automation` — Automate Square tasks via Rube MCP (Composio): payments, orders, invoices, locations. Always search tools first for current schemas.

- **squirrel** — `/Users/melbourne/.agents/skills/squirrel` — Full-cycle AI coding skill: plans, builds, tests, lints, fixes bugs, and writes production-grade docs. Auto-detects project state and adapts its 8-phase pipeline.

- **sred-project-organizer** — `/Users/melbourne/.agents/skills/sred-project-organizer` — Take a list of projects and their related documentation, and organize them into the SRED format for submission.

- **sred-work-summary** — `/Users/melbourne/.agents/skills/sred-work-summary` — Go back through the previous year of work and create a Notion doc that groups relevant links into projects that can then be documented as SRED projects.

- **ssh-penetration-testing** — `/Users/melbourne/.agents/skills/ssh-penetration-testing` — Conduct comprehensive SSH security assessments including enumeration, credential attacks, vulnerability exploitation, tunneling techniques, and post-exploitation activities. This skill covers the complete methodology for

- **stability-ai** — `/Users/melbourne/.agents/skills/stability-ai` — Geracao de imagens via Stability AI (SD3.5, Ultra, Core). Text-to-image, img2img, inpainting, upscale, remove-bg, search-replace. 15 estilos artisticos.

- **stakeholder-management** — `/Users/melbourne/.agents/skills/stakeholder-management` — Map stakeholders, influence, interests, expectations, commitments, communication needs, resistance, sponsorship, and engagement actions for management work.

- **startup-analyst** — `/Users/melbourne/.agents/skills/startup-analyst` — Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early-stage companies.

- **startup-business-analyst-business-case** — `/Users/melbourne/.agents/skills/startup-business-analyst-business-case` — Generate comprehensive investor-ready business case document with

- **startup-business-analyst-financial-projections** — `/Users/melbourne/.agents/skills/startup-business-analyst-financial-projections` — Create detailed 3-5 year financial model with revenue, costs, cash

- **startup-business-analyst-market-opportunity** — `/Users/melbourne/.agents/skills/startup-business-analyst-market-opportunity` — Generate comprehensive market opportunity analysis with TAM/SAM/SOM

- **startup-financial-modeling** — `/Users/melbourne/.agents/skills/startup-financial-modeling` — Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for early-stage startups.

- **startup-metrics-framework** — `/Users/melbourne/.agents/skills/startup-metrics-framework` — Comprehensive guide to tracking, calculating, and optimizing key performance metrics for different startup business models from seed through Series A.

- **statsmodels** — `/Users/melbourne/.agents/skills/statsmodels` — Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wide range of statistical methods.

- **steve-jobs** — `/Users/melbourne/.agents/skills/steve-jobs` — Agente que simula Steve Jobs — cofundador da Apple, CEO da Pixar, fundador da NeXT, o maior designer de produtos tecnologicos da historia e o mais influente apresentador de produtos do mundo.

- **sticker-design-generation** — `/Users/melbourne/.agents/skills/sticker-design-generation` — Generate custom sticker designs using each::sense AI. Create die-cut stickers, vinyl decals, kawaii designs, brand logos, emoji packs, laptop stickers, bumper stickers, planner stickers, holographic effects, and complete

- **stitch-design-taste** — `/Users/melbourne/.agents/skills/stitch-design-taste` — Use when generating Google Stitch DESIGN.md systems for premium typography, color, layout, motion intent, and anti-generic UI rules.

- **stitch-loop** — `/Users/melbourne/.agents/skills/stitch-loop` — Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern

- **stitch-ui-design** — `/Users/melbourne/.agents/skills/stitch-ui-design` — Expert guidance for crafting effective prompts in Google Stitch, the AI-powered UI design tool by Google Labs. This skill helps create precise, actionable prompts that generate high-quality UI designs for web and mobile 

- **story-bank-builder** — `/Users/melbourne/.agents/skills/story-bank-builder` — Use when the user asks to "build a story bank", "collect our origin and customer stories", or "assemble reusable proof stories for the message"; assembles reusable narrative units — origin, founder, customer, transformat

- **strategic-narrative-designer** — `/Users/melbourne/.agents/skills/strategic-narrative-designer` — Use when the user asks to "design our change narrative", "build the old-world-to-new-game story arc", or "frame the shift our category is undergoing"; produces a Raskin-style strategic narrative arc — old world → the und

- **strategic-planning** — `/Users/melbourne/.agents/skills/strategic-planning` — Turn strategic ambitions into choices, objectives, initiatives, assumptions, KPIs, milestones, resource needs, risks, and an executable roadmap.

- **stride-analysis-patterns** — `/Users/melbourne/.agents/skills/stride-analysis-patterns` — Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or creating security documentation.

- **stripe-automation** — `/Users/melbourne/.agents/skills/stripe-automation` — Automate Stripe tasks via Rube MCP (Composio): customers, charges, subscriptions, invoices, products, refunds. Always search tools first for current schemas.

- **stripe-integration** — `/Users/melbourne/.agents/skills/stripe-integration` — Master Stripe payment processing integration for robust, PCI-compliant payment flows including checkout, subscriptions, webhooks, and refunds.

- **style-creator** — `/Users/melbourne/.agents/skills/style-creator` — This skill should be used when the user asks to "add a new style", "create a style", "add an art style", "new aesthetic", "custom style", "make a style for", or needs to add a new art style to the gemskills style library

- **style-transfer** — `/Users/melbourne/.agents/skills/style-transfer` — Transform photos into stunning artistic styles using each::sense AI. Apply Van Gogh, Picasso, anime, watercolor, oil painting, and more to any image.

- **subagent-driven-development** — `/Users/melbourne/.agents/skills/subagent-driven-development` — Use when executing implementation plans with independent tasks in the current session

- **subagent-orchestrator** — `/Users/melbourne/.agents/skills/subagent-orchestrator` — Coordinate quota-aware parallel subagents for large, multi-file Antigravity tasks.

- **subject-line-lab** — `/Users/melbourne/.agents/skills/subject-line-lab` — Use when the user asks to "generate subject line variants", "pre-score my subject lines", or "will this subject get truncated / trigger spam filters"; produces a labeled subject + preheader variant set and a per-variant 

- **subject-line-psychologist** — `/Users/melbourne/.agents/skills/subject-line-psychologist` — One sentence - what this skill does and when to invoke it

- **substack-ghostwriting** — `/Users/melbourne/.agents/skills/substack-ghostwriting` — Write, optimize, and grow Substack content — newsletter issues (email-first) and web posts (web-first essays). Covers voice matching, Substack algorithm and Notes strategy, email formatting, SEO, growth tactics, and paid

- **subtitle-generation** — `/Users/melbourne/.agents/skills/subtitle-generation` — Generate subtitles and captions for videos using each::sense AI. Create auto-generated subtitles, multi-language captions, animated TikTok-style text, SRT/VTT exports, speaker diarization, and burned-in subtitles.

- **supabase-automation** — `/Users/melbourne/.agents/skills/supabase-automation` — Automate Supabase database queries, table management, project administration, storage, edge functions, and SQL execution via Rube MCP (Composio). Always search tools first for current schemas.

- **super-code** — `/Users/melbourne/.agents/skills/super-code` — Standing house style to enforce dense, correct, and idiomatic code on all coding tasks. Minimizes code bloat and agent operation overhead.

- **superpowers-lab** — `/Users/melbourne/.agents/skills/superpowers-lab` — Lab environment for Claude superpowers

- **supply-chain-risk-auditor** — `/Users/melbourne/.agents/skills/supply-chain-risk-auditor` — Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements.

- **survey-generator** — `/Users/melbourne/.agents/skills/survey-generator` — Generate source-backed AI/ML survey paper artifacts with curated bibliographies and Fireworks/Kimi HTML rendering.

- **sveltekit** — `/Users/melbourne/.agents/skills/sveltekit` — Build full-stack web applications with SvelteKit — file-based routing, SSR, SSG, API routes, and form actions in one framework.

- **svg-animation** — `/Users/melbourne/.agents/skills/svg-animation` — This skill should be used when the user asks to "animate an SVG", "make a line draw itself on", "do a stroke draw-on / signature animation", "morph one shape into another", "move an element along a path", "animate an ico

- **swift-concurrency-expert** — `/Users/melbourne/.agents/skills/swift-concurrency-expert` — Review and fix Swift concurrency issues such as actor isolation and Sendable violations.

- **swiftui-expert-skill** — `/Users/melbourne/.agents/skills/swiftui-expert-skill` — Write, review, or improve SwiftUI code following best practices for state management, view composition, performance, and iOS 26+ Liquid Glass adoption. Use when building new SwiftUI features, refactoring existing views, 

- **swiftui-liquid-glass** — `/Users/melbourne/.agents/skills/swiftui-liquid-glass` — Implement or review SwiftUI Liquid Glass APIs with correct fallbacks and modifier order.

- **swiftui-performance-audit** — `/Users/melbourne/.agents/skills/swiftui-performance-audit` — Audit SwiftUI performance issues from code review and profiling evidence.

- **swiftui-ui-patterns** — `/Users/melbourne/.agents/skills/swiftui-ui-patterns` — Apply proven SwiftUI UI patterns for navigation, sheets, async state, and reusable screens.

- **swiftui-view-refactor** — `/Users/melbourne/.agents/skills/swiftui-view-refactor` — Refactor SwiftUI views into smaller components with stable, explicit data flow.

- **sympy** — `/Users/melbourne/.agents/skills/sympy` — SymPy is a Python library for symbolic mathematics that enables exact computation using mathematical symbols rather than numerical approximations.

- **systematic-debugging** — `/Users/melbourne/.agents/skills/systematic-debugging` — Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

- **systems-programming-rust-project** — `/Users/melbourne/.agents/skills/systems-programming-rust-project` — You are a Rust project architecture expert specializing in scaffolding production-ready Rust applications. Generate complete project structures with cargo tooling, proper module organization, testing

- **tailwind-best-practices** — `/Users/melbourne/.agents/skills/tailwind-best-practices` — Tailwind CSS styling guidelines for Mastra Playground UI. This skill should be used when writing, reviewing, or refactoring styling code in packages/playground-ui and packages/playground to ensure design system consisten

- **tailwind-css-patterns** — `/Users/melbourne/.agents/skills/tailwind-css-patterns` — Provides comprehensive Tailwind CSS utility-first styling patterns including responsive design, layout utilities, flexbox, grid, spacing, typography, colors, and modern CSS best practices. Use when styling React/Vue/Svel

- **tailwind-design-system** — `/Users/melbourne/.agents/skills/tailwind-design-system` — Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, and accessibility.

- **tailwind-patterns** — `/Users/melbourne/.agents/skills/tailwind-patterns` — Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture.

- **tailwind-v4-shadcn** — `/Users/melbourne/.agents/skills/tailwind-v4-shadcn` — | Production-tested setup for Tailwind CSS v4 with shadcn/ui, Vite, and React. Use when: initializing React projects with Tailwind v4, setting up shadcn/ui, implementing dark mode, debugging CSS variable issues, fixing t

- **tailwindcss-advanced-layouts** — `/Users/melbourne/.agents/skills/tailwindcss-advanced-layouts` — |

- **talking-head-video** — `/Users/melbourne/.agents/skills/talking-head-video` — Generate talking head videos using each::sense AI. Create AI presenters, lip-sync avatars, corporate spokespersons, training videos, and multi-language content from photos, scripts, or audio files.

- **tanstack-query-expert** — `/Users/melbourne/.agents/skills/tanstack-query-expert` — Expert in TanStack Query (React Query) — asynchronous state management. Covers data fetching, stale time configuration, mutations, optimistic updates, and Next.js App Router (SSR) integration.

- **task-intelligence** — `/Users/melbourne/.agents/skills/task-intelligence` — Protocolo de Inteligência Pré-Tarefa — ativa TODOS os agentes relevantes do ecossistema ANTES de executar qualquer tarefa solicitada pelo usuário.

- **task-prioritization** — `/Users/melbourne/.agents/skills/task-prioritization` — Prioritize tasks and commitments by impact, urgency, deadlines, dependencies, effort, reversibility, delegation potential, and strategic importance.

- **tattoo-design-generation** — `/Users/melbourne/.agents/skills/tattoo-design-generation` — Generate custom tattoo designs using each::sense AI. Create traditional, Japanese, minimalist, geometric, watercolor, blackwork, realistic, floral, and script tattoo designs optimized for various styles and placements.

- **tavily-web** — `/Users/melbourne/.agents/skills/tavily-web` — Web search, content extraction, crawling, and research capabilities using Tavily API. Use when you need to search the web for current information, extracting content from URLs, or crawling websites.

- **tcm-constitution-analyzer** — `/Users/melbourne/.agents/skills/tcm-constitution-analyzer` — 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。

- **tdd** — `/Users/melbourne/.agents/skills/tdd` — Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.

- **tdd-orchestrator** — `/Users/melbourne/.agents/skills/tdd-orchestrator` — Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices.

- **tdd-workflow** — `/Users/melbourne/.agents/skills/tdd-workflow` — Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle.

- **tdd-workflows** — `/Users/melbourne/.agents/skills/tdd-workflows` — Use when working with tdd workflows tdd cycle (Alias for tdd-workflows-tdd-cycle)

- **tdd-workflows-tdd-cycle** — `/Users/melbourne/.agents/skills/tdd-workflows-tdd-cycle` — Use when working with tdd workflows tdd cycle

- **tdd-workflows-tdd-green** — `/Users/melbourne/.agents/skills/tdd-workflows-tdd-green` — Implement the minimal code needed to make failing tests pass in the TDD green phase.

- **tdd-workflows-tdd-red** — `/Users/melbourne/.agents/skills/tdd-workflows-tdd-red` — Generate failing tests for the TDD red phase to define expected behavior and edge cases.

- **tdd-workflows-tdd-refactor** — `/Users/melbourne/.agents/skills/tdd-workflows-tdd-refactor` — Use when working with tdd workflows tdd refactor

- **teach** — `/Users/melbourne/.agents/skills/teach` — Teach the user a new skill or concept, within this workspace.

- **team-collaboration-issue** — `/Users/melbourne/.agents/skills/team-collaboration-issue` — You are a GitHub issue resolution expert specializing in systematic bug investigation, feature implementation, and collaborative development workflows. Your expertise spans issue triage, root cause an

- **team-collaboration-standup-notes** — `/Users/melbourne/.agents/skills/team-collaboration-standup-notes` — You are an expert team communication specialist focused on async-first standup practices, AI-assisted note generation from commit history, and effective remote team coordination patterns.

- **team-composition-analysis** — `/Users/melbourne/.agents/skills/team-composition-analysis` — Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed through Series A.

- **team-group-photo** — `/Users/melbourne/.agents/skills/team-group-photo` — This skill should be used when the user asks to "create team photo", "generate group portrait", "make team banner", "team image in any style", "group shot with multiple people", or needs a composite image featuring multi

- **team-management** — `/Users/melbourne/.agents/skills/team-management` — Help managers set team goals, clarify roles, balance workload, run 1:1s, give feedback, resolve coordination problems, and improve team execution.

- **technical-article-writer** — `/Users/melbourne/.agents/skills/technical-article-writer` — Write technical articles and blog posts for developer audiences — tutorials, explainers, benchmarks, bug hunts, postmortems, and 'we rewrote it in X' posts — with title variants and developer-grade article structure. Use

- **technical-change-tracker** — `/Users/melbourne/.agents/skills/technical-change-tracker` — Track code changes with structured JSON records, state machine enforcement, and AI session handoff for bot continuity

- **technical-seo-checker** — `/Users/melbourne/.agents/skills/technical-seo-checker` — Use when the user asks to "check technical SEO"; audits crawlability, indexing, Core Web Vitals, robots.txt, sitemaps, canonicals, redirects, and migrations. Not for on-page tags or content — use on-page-seo-checker. 技术S

- **telegram** — `/Users/melbourne/.agents/skills/telegram` — Integracao completa com Telegram Bot API. Setup com BotFather, mensagens, webhooks, inline keyboards, grupos, canais. Boilerplates Node.js e Python.

- **telegram-automation** — `/Users/melbourne/.agents/skills/telegram-automation` — Automate Telegram tasks via Rube MCP (Composio): send messages, manage chats, share photos/documents, and handle bot commands. Always search tools first for current schemas.

- **telegram-bot-builder** — `/Users/melbourne/.agents/skills/telegram-bot-builder` — Expert in building Telegram bots that solve real problems - from

- **telegram-mini-app** — `/Users/melbourne/.agents/skills/telegram-mini-app` — Expert in building Telegram Mini Apps (TWA) - web apps that run

- **temporal-golang-pro** — `/Users/melbourne/.agents/skills/temporal-golang-pro` — Use when building durable distributed systems with Temporal Go SDK. Covers deterministic workflow rules, mTLS worker configs, and advanced patterns.

- **temporal-python-pro** — `/Users/melbourne/.agents/skills/temporal-python-pro` — Master Temporal workflow orchestration with Python SDK. Implements durable workflows, saga patterns, and distributed transactions. Covers async/await, testing strategies, and production deployment.

- **temporal-python-testing** — `/Users/melbourne/.agents/skills/temporal-python-testing` — Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific testing scenarios.

- **terraform-aws-modules** — `/Users/melbourne/.agents/skills/terraform-aws-modules` — Terraform module creation for AWS — reusable modules, state management, and HCL best practices. Use when building or reviewing Terraform AWS infrastructure.

- **terraform-infrastructure** — `/Users/melbourne/.agents/skills/terraform-infrastructure` — Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale.

- **terraform-module-library** — `/Users/melbourne/.agents/skills/terraform-module-library` — Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure.

- **terraform-skill** — `/Users/melbourne/.agents/skills/terraform-skill` — Terraform infrastructure as code best practices

- **terraform-specialist** — `/Users/melbourne/.agents/skills/terraform-specialist` — Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns.

- **test-automator** — `/Users/melbourne/.agents/skills/test-automator` — Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing strategies with advanced CI/CD integration.

- **test-driven-development** — `/Users/melbourne/.agents/skills/test-driven-development` — Use when implementing any feature or bugfix, before writing implementation code

- **test-fixing** — `/Users/melbourne/.agents/skills/test-fixing` — Systematically identify and fix all failing tests using smart grouping strategies. Use when explicitly asks to fix tests (\"fix these tests\", \"make tests pass\"), reports test failures (\"tests are failing\", \"test su

- **testing-patterns** — `/Users/melbourne/.agents/skills/testing-patterns` — Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or following TDD red-green-refactor cycle.

- **testing-qa** — `/Users/melbourne/.agents/skills/testing-qa` — Comprehensive testing and QA workflow covering unit testing, integration testing, E2E testing, browser automation, and quality assurance.

- **testing-strategy** — `/Users/melbourne/.agents/skills/testing-strategy` — Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or te

- **theme-factory** — `/Users/melbourne/.agents/skills/theme-factory` — This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it can be applied to any artifact.

- **threat-mitigation-mapping** — `/Users/melbourne/.agents/skills/threat-mitigation-mapping` — Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiveness.

- **threat-modeling-expert** — `/Users/melbourne/.agents/skills/threat-modeling-expert` — Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use PROACTIVELY for security architecture reviews, thr

- **threejs-animation** — `/Users/melbourne/.agents/skills/threejs-animation` — Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or blending animations.

- **threejs-fundamentals** — `/Users/melbourne/.agents/skills/threejs-fundamentals` — Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarchies, or working with transforms.

- **threejs-geometry** — `/Users/melbourne/.agents/skills/threejs-geometry` — Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertices, building custom meshes, or optimizing with instanced rendering.

- **threejs-interaction** — `/Users/melbourne/.agents/skills/threejs-interaction` — Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection, adding camera controls, or creating interactive 3D experiences.

- **threejs-lighting** — `/Users/melbourne/.agents/skills/threejs-lighting` — Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing lighting performance.

- **threejs-loaders** — `/Users/melbourne/.agents/skills/threejs-loaders` — Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing loading progress.

- **threejs-materials** — `/Users/melbourne/.agents/skills/threejs-materials` — Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating custom shaders, or optimizing material performance.

- **threejs-postprocessing** — `/Users/melbourne/.agents/skills/threejs-postprocessing` — Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creating custom screen-space shaders.

- **threejs-shaders** — `/Users/melbourne/.agents/skills/threejs-shaders` — Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing fragment shaders, or extending built-in materials.

- **threejs-skills** — `/Users/melbourne/.agents/skills/threejs-skills` — Create 3D scenes, interactive experiences, and visual effects using Three.js. Use when user requests 3D graphics, WebGL experiences, 3D visualizations, animations, or interactive 3D elements.

- **threejs-textures** — `/Users/melbourne/.agents/skills/threejs-textures` — Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimization.

- **tidy-project** — `/Users/melbourne/.agents/skills/tidy-project` — >-

- **tiktok-ad-creative-generation** — `/Users/melbourne/.agents/skills/tiktok-ad-creative-generation` — Generate TikTok-native ad creatives using each::sense API - vertical videos, Spark Ads style, trending formats, and UGC aesthetics

- **tiktok-automation** — `/Users/melbourne/.agents/skills/tiktok-automation` — Automate TikTok tasks via Rube MCP (Composio): upload/publish videos, post photos, manage content, and view user profiles/stats. Always search tools first for current schemas.

- **tmux** — `/Users/melbourne/.agents/skills/tmux` — Expert tmux session, window, and pane management for terminal multiplexing, persistent remote workflows, and shell scripting automation.

- **to-issues** — `/Users/melbourne/.agents/skills/to-issues` — Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices.

- **to-prd** — `/Users/melbourne/.agents/skills/to-prd` — Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.

- **todoist-automation** — `/Users/melbourne/.agents/skills/todoist-automation` — Automate Todoist task management, projects, sections, filtering, and bulk operations via Rube MCP (Composio). Always search tools first for current schemas.

- **tokenwise** — `/Users/melbourne/.agents/skills/tokenwise` — Measurement-driven model router for Claude Code. Routes Haiku/Sonnet/Opus per task class, logs every routed task with real $ numbers, and A/B tests cheaper tiers before you trust the savings.

- **tool-design** — `/Users/melbourne/.agents/skills/tool-design` — Build tools that agents can use effectively, including architectural reduction patterns. Use when creating new tools for agent systems, debugging tool-related failures or misuse, or optimizing existing tool sets for bett

- **tool-use-guardian** — `/Users/melbourne/.agents/skills/tool-use-guardian` — FREE — Intelligent tool-call reliability wrapper. Monitors, retries, fixes, and learns from tool failures. Auto-recovers from truncated JSON, timeouts, rate limits, and mid-chain failures.

- **tools-page-seo-optimizer** — `/Users/melbourne/.agents/skills/tools-page-seo-optimizer` — Framework-agnostic SEO workflow for any site with multiple tool, product, or feature pages. Covers duplicate content, unique meta tags, heading hierarchy, internal linking, URL slugs, E-E-A-T, content registry pattern fo

- **top-web-vulnerabilities** — `/Users/melbourne/.agents/skills/top-web-vulnerabilities` — Provide a comprehensive, structured reference for the 100 most critical web application vulnerabilities organized by category. This skill enables systematic vulnerability identification, impact assessment, and remediatio

- **track-management** — `/Users/melbourne/.agents/skills/track-management` — Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs, and refactors. Applies to spec.md, plan.md, and track lifecycle operations.

- **training-report** — `/Users/melbourne/.agents/skills/training-report` — Produce a professional training/workshop report as a .docx file. Use this skill whenever the user mentions "training report", "workshop report", "compte rendu", "compte rendu de formation", "formation report", "debriefin

- **transformers-js** — `/Users/melbourne/.agents/skills/transformers-js` — Run Hugging Face models in JavaScript or TypeScript with Transformers.js in Node.js or the browser.

- **travel-health-analyzer** — `/Users/melbourne/.agents/skills/travel-health-analyzer` — 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。

- **trello-automation** — `/Users/melbourne/.agents/skills/trello-automation` — Automate Trello boards, cards, and workflows via Rube MCP (Composio). Create cards, manage lists, assign members, and search across boards programmatically.

- **trend-spotter** — `/Users/melbourne/.agents/skills/trend-spotter` — Use when the user asks to "find trending topics", "what trends should my brand jump on", or "time a campaign around a cultural moment"; produces a ranked trend report with brand-fit scores, format calls (rising/peak/decl

- **triage** — `/Users/melbourne/.agents/skills/triage` — Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs.

- **trigger-dev** — `/Users/melbourne/.agents/skills/trigger-dev` — Trigger.dev expert for background jobs, AI workflows, and reliable

- **trpc-fullstack** — `/Users/melbourne/.agents/skills/trpc-fullstack` — Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions, and Next.js/React integration patterns.

- **trust-calibrator** — `/Users/melbourne/.agents/skills/trust-calibrator` — One sentence - what this skill does and when to invoke it

- **tshirt-design-generation** — `/Users/melbourne/.agents/skills/tshirt-design-generation` — Generate print-ready t-shirt and apparel designs using each::sense AI. Create graphic tees, typography designs, vintage styles, illustrations, and more for custom apparel printing.

- **turborepo-caching** — `/Users/melbourne/.agents/skills/turborepo-caching` — Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching.

- **tutorial-engineer** — `/Users/melbourne/.agents/skills/tutorial-engineer` — Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with hands-on examples.

- **twilio-communications** — `/Users/melbourne/.agents/skills/twilio-communications` — Build communication features with Twilio: SMS messaging, voice

- **twitch-overlay-generation** — `/Users/melbourne/.agents/skills/twitch-overlay-generation` — Generate Twitch and streaming overlays using each::sense AI. Create webcam frames, starting soon screens, BRB screens, alerts, chat boxes, panels, emotes, subscriber badges, and channel banners optimized for streaming pl

- **twitter-automation** — `/Users/melbourne/.agents/skills/twitter-automation` — Automate Twitter/X tasks via Rube MCP (Composio): posts, search, users, bookmarks, lists, media. Always search tools first for current schemas.

- **typescript-advanced-types** — `/Users/melbourne/.agents/skills/typescript-advanced-types` — Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped types, template literal types, and utility types for building robust, type-safe applications.

- **typescript-expert** — `/Users/melbourne/.agents/skills/typescript-expert` — TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration strategies, and modern tooling.

- **typescript-pro** — `/Users/melbourne/.agents/skills/typescript-pro` — Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patterns.

- **ugc-video-generation** — `/Users/melbourne/.agents/skills/ugc-video-generation` — Generate authentic user-generated content (UGC) style videos including testimonials, unboxings, reviews, and selfie-style content using each::sense API

- **ui-a11y** — `/Users/melbourne/.agents/skills/ui-a11y` — Audit a StyleSeed-based component or page for WCAG 2.2 AA issues and apply practical accessibility fixes where the code makes them safe.

- **ui-component** — `/Users/melbourne/.agents/skills/ui-component` — Generate a new UI component that follows StyleSeed Toss conventions for structure, tokens, accessibility, and component ergonomics.

- **ui-page** — `/Users/melbourne/.agents/skills/ui-page` — Scaffold a new mobile-first page using StyleSeed Toss layout patterns, section rhythm, and existing shell components.

- **ui-pattern** — `/Users/melbourne/.agents/skills/ui-pattern` — Generate reusable UI patterns such as card sections, grids, lists, forms, and chart wrappers using StyleSeed Toss primitives.

- **ui-review** — `/Users/melbourne/.agents/skills/ui-review` — Review UI code for StyleSeed design-system compliance, accessibility, mobile ergonomics, spacing discipline, and implementation quality.

- **ui-setup** — `/Users/melbourne/.agents/skills/ui-setup` — Interactive StyleSeed setup wizard for choosing app type, brand color, visual style, typography, and the first screen scaffold.

- **ui-skills** — `/Users/melbourne/.agents/skills/ui-skills` — Opinionated, evolving constraints to guide agents when building interfaces

- **ui-tokens** — `/Users/melbourne/.agents/skills/ui-tokens` — List, add, and update StyleSeed design tokens while keeping JSON sources, CSS variables, and dark-mode values in sync.

- **ui-ux-designer** — `/Users/melbourne/.agents/skills/ui-ux-designer` — Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools.

- **ui-ux-pro-max** — `/Users/melbourne/.agents/skills/ui-ux-pro-max` — Comprehensive design guide for web and mobile applications. Use when designing new UI components or pages, choosing color palettes and typography, or reviewing code for UX issues.

- **ui-visual-validator** — `/Users/melbourne/.agents/skills/ui-visual-validator` — Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification.

- **ui-web-visual-assets** — `/Users/melbourne/.agents/skills/ui-web-visual-assets` — Generate coherent web and app visual assets such as hero imagery, backgrounds, illustrations, empty states, feature art, thumbnails, and decorative UI graphics.

- **uncle-bob-craft** — `/Users/melbourne/.agents/skills/uncle-bob-craft` — Use when performing code review, writing or refactoring code, or discussing architecture; complements clean-code and does not replace project linter/formatter.

- **uniprot-database** — `/Users/melbourne/.agents/skills/uniprot-database` — Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple databases, prefer bioservices (unified interface to 40+ services). Use this for dire

- **unit-testing-test-generate** — `/Users/melbourne/.agents/skills/unit-testing-test-generate` — Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus.

- **unity-ai-game-creator** — `/Users/melbourne/.agents/skills/unity-ai-game-creator` — Transform raw game ideas into complete Unity projects with AI-powered asset generation, scene blueprints, music/SFX prompts, and step-by-step development procedures using Unity 6+ and modern AI tools.

- **unity-developer** — `/Users/melbourne/.agents/skills/unity-developer` — Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, and cross-platform deployment.

- **unity-ecs-patterns** — `/Users/melbourne/.agents/skills/unity-ecs-patterns` — Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler.

- **unreal-engine-cpp-pro** — `/Users/melbourne/.agents/skills/unreal-engine-cpp-pro` — Expert guide for Unreal Engine 5.x C++ development, covering UObject hygiene, performance patterns, and best practices.

- **unship** — `/Users/melbourne/.agents/skills/unship` — Compare AI agent-made UI variants locally in a real app, then keep one and clean up unused temporary code.

- **unslop** — `/Users/melbourne/.agents/skills/unslop` — Post-process AI-generated text through the unslop CLI to strip AI writing patterns before publishing

- **unsplash-integration** — `/Users/melbourne/.agents/skills/unsplash-integration` — Integration skill for searching and fetching high-quality, free-to-use professional photography from Unsplash.

- **upgrading-expo** — `/Users/melbourne/.agents/skills/upgrading-expo` — Upgrade Expo SDK versions

- **upscale-image** — `/Users/melbourne/.agents/skills/upscale-image` — This skill should be used when the user asks to "upscale an image", "increase image resolution", "make image bigger", "enlarge image", or "enhance image resolution". Requires Vertex AI credentials.

- **upstash-qstash** — `/Users/melbourne/.agents/skills/upstash-qstash` — Upstash QStash expert for serverless message queues, scheduled

- **user-thoughts** — `/Users/melbourne/.agents/skills/user-thoughts` — >-

- **using-git-worktrees** — `/Users/melbourne/.agents/skills/using-git-worktrees` — Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching.

- **using-neon** — `/Users/melbourne/.agents/skills/using-neon` — Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant restore, and scale-to-zero. It's fully compatible with Postgres and works with any language, framework, o

- **using-superpowers** — `/Users/melbourne/.agents/skills/using-superpowers` — Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

- **uv-package-manager** — `/Users/melbourne/.agents/skills/uv-package-manager` — Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project management and dependency workflows.

- **ux-audit** — `/Users/melbourne/.agents/skills/ux-audit` — Audit screens against Nielsen's heuristics and mobile UX best practices using the StyleSeed Toss design language as the implementation context.

- **ux-copy** — `/Users/melbourne/.agents/skills/ux-copy` — Generate UX microcopy in StyleSeed's Toss-inspired voice for buttons, empty states, errors, toasts, confirmations, and form guidance.

- **ux-feedback** — `/Users/melbourne/.agents/skills/ux-feedback` — Add loading, empty, error, and success feedback states to StyleSeed components and pages with practical mobile-first rules.

- **ux-flow** — `/Users/melbourne/.agents/skills/ux-flow` — Design user flows and screen structure using StyleSeed UX patterns such as progressive disclosure, hub-and-spoke navigation, and information pyramids.

- **ux-persuasion-engineer** — `/Users/melbourne/.agents/skills/ux-persuasion-engineer` — One sentence - what this skill does and when to invoke it

- **uxui-principles** — `/Users/melbourne/.agents/skills/uxui-principles` — Evaluate interfaces against 168 research-backed UX/UI principles, detect antipatterns, and inject UX context into AI coding sessions.

- **variant-analysis** — `/Users/melbourne/.agents/skills/variant-analysis` — Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audit

- **varlock** — `/Users/melbourne/.agents/skills/varlock` — Secure-by-default environment variable management for Claude Code sessions.

- **varlock-claude-skill** — `/Users/melbourne/.agents/skills/varlock-claude-skill` — Secure environment variable management ensuring secrets are never exposed in Claude sessions, terminals, logs, or git commits

- **vector-database-engineer** — `/Users/melbourne/.agents/skills/vector-database-engineer` — Expert in vector databases, embedding strategies, and semantic search implementation. Masters Pinecone, Weaviate, Qdrant, Milvus, and pgvector for RAG applications, recommendation systems, and similar

- **vector-index-tuning** — `/Users/melbourne/.agents/skills/vector-index-tuning` — Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure.

- **vercel-ai-sdk-expert** — `/Users/melbourne/.agents/skills/vercel-ai-sdk-expert` — Expert in the Vercel AI SDK. Covers Core API (generateText, streamText), UI hooks (useChat, useCompletion), tool calling, and streaming UI components with React and Next.js.

- **vercel-automation** — `/Users/melbourne/.agents/skills/vercel-automation` — Automate Vercel tasks via Rube MCP (Composio): manage deployments, domains, DNS, env vars, projects, and teams. Always search tools first for current schemas.

- **vercel-cli-with-tokens** — `/Users/melbourne/.agents/skills/vercel-cli-with-tokens` — Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. \"deploy to vercel\", \"set up vercel\", \"add environment 

- **vercel-deployment** — `/Users/melbourne/.agents/skills/vercel-deployment` — Expert knowledge for deploying to Vercel with Next.js

- **vercel-optimize** — `/Users/melbourne/.agents/skills/vercel-optimize` — Audit deployed Vercel apps for cost and performance issues using metrics, project config, code scans, and version-aware recommendations.

- **vercel-react-view-transitions** — `/Users/melbourne/.agents/skills/vercel-react-view-transitions` — Guide React and Next.js view transitions, shared element animations, route transitions, transition types, and reduced-motion-safe UI state animation.

- **verification-before-completion** — `/Users/melbourne/.agents/skills/verification-before-completion` — Claiming work is complete without verification is dishonesty, not efficiency. Use when ANY variation of success/completion claims, ANY expression of satisfaction, or ANY positive statement about work state.

- **vexor** — `/Users/melbourne/.agents/skills/vexor` — Vector-powered CLI for semantic file search with a Claude/Codex skill

- **vexor-cli** — `/Users/melbourne/.agents/skills/vexor-cli` — Semantic file discovery via `vexor`. Use whenever locating where something is implemented/loaded/defined in a medium or large repo, or when the file location is unclear. Prefer this over manual browsing.

- **vibe-code-auditor** — `/Users/melbourne/.agents/skills/vibe-code-auditor` — Audit rapidly generated or AI-produced code for structural flaws, fragility, and production risks.

- **vibe-code-cleanup** — `/Users/melbourne/.agents/skills/vibe-code-cleanup` — Safe production cleanup and hardening for vibe-coded fullstack apps (Next.js, React, Node.js, etc.). Removes dead imports, unused files, and broken references without breaking routes or APIs.

- **vibecode-production-qa-validator** — `/Users/melbourne/.agents/skills/vibecode-production-qa-validator` — 13-phase production QA for fullstack Next.js apps: build verification, SEO tags, OG images, favicon, route regression, API auth, page speed, lazy load, vulnerability scan, UI/UX cards, error boundaries, database, secure 

- **vibers-code-review** — `/Users/melbourne/.agents/skills/vibers-code-review` — Human review workflow for AI-generated GitHub projects with spec-based feedback, security review, and follow-up PRs from the Vibers service.

- **viboscope** — `/Users/melbourne/.agents/skills/viboscope` — Psychological compatibility matching — find cofounders, collaborators, and friends through validated psychometrics

- **video** — `/Users/melbourne/.agents/skills/video` — When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. Also use when the user mentions 'video production,' 'AI video,' 'Remotion,' 'Hyperframes,' 'HeyGen,' 'Synthesia

- **video-background-removal** — `/Users/melbourne/.agents/skills/video-background-removal` — Remove, replace, or modify video backgrounds using each::sense AI. Create transparent backgrounds, virtual offices, green screen effects without green screens, blur effects, and professional video compositing.

- **video-color-grading** — `/Users/melbourne/.agents/skills/video-color-grading` — Apply professional color grading and correction to videos using each::sense AI. Create cinematic looks, film emulations, color corrections, and stylized grades for any video content.

- **video-content-extractor** — `/Users/melbourne/.agents/skills/video-content-extractor` — Extract key frames from MP4 videos at configurable intervals, run Tesseract OCR, and generate structured Markdown reports with video metadata and timestamped text transcripts.

- **video-delivery-specs** — `/Users/melbourne/.agents/skills/video-delivery-specs` — This skill should be used when the user asks "what are the specs for Instagram Reels / TikTok / YouTube / broadcast", "export settings for social", "what aspect ratio and bitrate", "how do I repurpose 16:9 to 9:16", "saf

- **video-format-conversion** — `/Users/melbourne/.agents/skills/video-format-conversion` — Convert videos between formats, codecs, and aspect ratios using each::sense AI. Support for MP4, WebM, GIF, ProRes, and social media optimized outputs.

- **video-highlight-extraction** — `/Users/melbourne/.agents/skills/video-highlight-extraction` — Extract highlights, best moments, and key clips from long videos using each::sense AI. Perfect for gaming highlights, sports clips, podcast moments, webinar summaries, meeting recaps, and auto-trailer generation.

- **video-localization** — `/Users/melbourne/.agents/skills/video-localization` — Localize and dub videos using each::sense AI. Translate audio, generate subtitles, clone voices, and create lip-synced multilingual versions of your video content.

- **video-noise-reduction** — `/Users/melbourne/.agents/skills/video-noise-reduction` — Reduce noise and grain from videos using each::sense AI. Denoise low light footage, remove high ISO grain, enhance security camera video, restore old footage, and improve webcam quality.

- **video-speed-adjustment** — `/Users/melbourne/.agents/skills/video-speed-adjustment` — Adjust video speed using each::sense AI. Create slow motion, time-lapse, hyperlapse, speed ramps, reverse effects, and cinematic slow-mo with frame interpolation for smooth playback.

- **video-stabilization** — `/Users/melbourne/.agents/skills/video-stabilization` — Stabilize shaky video footage using each::sense AI. Remove camera shake from handheld footage, action cameras, drones, and more with intelligent motion correction.

- **video-trimming** — `/Users/melbourne/.agents/skills/video-trimming` — Trim, cut, and split videos using each::sense AI. Extract specific segments, remove intros/outros, create social media clips, detect scenes automatically, and batch process multiple videos.

- **video-watermark** — `/Users/melbourne/.agents/skills/video-watermark` — Add or remove watermarks from videos using each::sense AI. Add logo watermarks, text overlays, transparent watermarks, animated watermarks, and remove unwanted watermarks from TikTok, stock footage, and other sources.

- **videodb** — `/Users/melbourne/.agents/skills/videodb` — Video and audio perception, indexing, and editing. Ingest files/URLs/live streams, build visual/spoken indexes, search with timestamps, edit timelines, add overlays/subtitles, generate media, and create real-time alerts.

- **videodb-skills** — `/Users/melbourne/.agents/skills/videodb-skills` — Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK.

- **viral-generator-builder** — `/Users/melbourne/.agents/skills/viral-generator-builder` — Expert in building shareable generator tools that go viral - name

- **virtual-staging** — `/Users/melbourne/.agents/skills/virtual-staging` — Transform empty rooms into beautifully furnished spaces using each::sense AI. Create photorealistic virtual staging for real estate listings, commercial properties, and interior design visualization.

- **virtual-try-on** — `/Users/melbourne/.agents/skills/virtual-try-on` — AI-powered virtual try-on for clothing, accessories, makeup, hairstyles, and more using each::sense API

- **visual-brand-guardian** — `/Users/melbourne/.agents/skills/visual-brand-guardian` — Enforce brand identity across generated visuals using approved logos, colors, visual codes, typography intent, spacing, composition, and consistency checks.

- **visual-content** — `/Users/melbourne/.agents/skills/visual-content` — When the user wants to plan, create, or repurpose visual content (images, infographics, social post images) across channels. Also use when the user mentions "content images," "social media images," "infographic," "visual

- **visual-emotion-engineer** — `/Users/melbourne/.agents/skills/visual-emotion-engineer` — One sentence - what this skill does and when to invoke it

- **visual-planner** — `/Users/melbourne/.agents/skills/visual-planner` — This skill should be used when the user asks to "plan a workflow", "diagram an agent system", "visualize an architecture", "map out a pipeline", "create a flow diagram", "draw agent connections", "design a multi-agent sy

- **visual-quality-control** — `/Users/melbourne/.agents/skills/visual-quality-control` — Audit generated and edited images for brief compliance, realism, identity, anatomy, geometry, text/logo fidelity, brand consistency, artifacts, crops, and delivery readiness.

- **vizcom** — `/Users/melbourne/.agents/skills/vizcom` — AI-powered product design tool for transforming sketches into full-fidelity 3D renders.

- **voice-agents** — `/Users/melbourne/.agents/skills/voice-agents` — Voice agents represent the frontier of AI interaction - humans

- **voice-ai-development** — `/Users/melbourne/.agents/skills/voice-ai-development` — Expert in building voice AI applications - from real-time voice

- **voice-ai-engine-development** — `/Users/melbourne/.agents/skills/voice-ai-engine-development` — Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis with interrupt handling and multi-provider support

- **voice-dossier-builder** — `/Users/melbourne/.agents/skills/voice-dossier-builder` — Use when the user asks to "codify how our founder sounds", "build a founder voice dossier", or "set our content pillars"; runs an 80%-extraction interview over the user''s OWN posts, emails, and decks (never competitor s

- **vscode-extension-guide-en** — `/Users/melbourne/.agents/skills/vscode-extension-guide-en` — Guide for VS Code extension development from scaffolding to Marketplace publication

- **vtuber-avatar-generation** — `/Users/melbourne/.agents/skills/vtuber-avatar-generation` — Generate VTuber avatars and character designs using each::sense AI. Create anime-style avatars, Live2D ready characters, expression sheets, full body designs, and accessories for virtual content creators.

- **vulnerability-scanner** — `/Users/melbourne/.agents/skills/vulnerability-scanner` — Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization.

- **warren-buffett** — `/Users/melbourne/.agents/skills/warren-buffett` — Agente que simula Warren Buffett — o maior investidor do seculo XX e XXI, CEO da Berkshire Hathaway, discipulo de Benjamin Graham e socio intelectual de Charlie Munger.

- **wcag-audit-patterns** — `/Users/melbourne/.agents/skills/wcag-audit-patterns` — Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies.

- **web-artifacts-builder** — `/Users/melbourne/.agents/skills/web-artifacts-builder` — To build powerful frontend claude.ai artifacts, follow these steps:

- **web-design-guidelines** — `/Users/melbourne/.agents/skills/web-design-guidelines` — Review files for compliance with Web Interface Guidelines.

- **web-media-getter** — `/Users/melbourne/.agents/skills/web-media-getter` — One query across free image / video / GIF APIs (stock + historical/archival + GIF engines), returning normalized, license-tagged results with optional top-K download + attribution sidecar. The retrieval peer to local sem

- **web-performance-optimization** — `/Users/melbourne/.agents/skills/web-performance-optimization` — Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance

- **web-scraper** — `/Users/melbourne/.agents/skills/web-scraper` — Web scraping inteligente multi-estrategia. Extrai dados estruturados de paginas web (tabelas, listas, precos). Paginacao, monitoramento e export CSV/JSON.

- **web-security-testing** — `/Users/melbourne/.agents/skills/web-security-testing` — Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access control issues.

- **web3-testing** — `/Users/melbourne/.agents/skills/web3-testing` — Master comprehensive testing strategies for smart contracts using Hardhat, Foundry, and advanced testing patterns.

- **webapp-testing** — `/Users/melbourne/.agents/skills/webapp-testing` — To test local web applications, write native Python Playwright scripts.

- **webflow-automation** — `/Users/melbourne/.agents/skills/webflow-automation` — Automate Webflow CMS collections, site publishing, page management, asset uploads, and ecommerce orders via Rube MCP (Composio). Always search tools first for current schemas.

- **wechat-official-account-strategist** — `/Users/melbourne/.agents/skills/wechat-official-account-strategist` — Grow WeChat Official Accounts (微信公众号) with high-conversion content strategy, title formulas, article architecture, and Mini-Program integration.

- **wedding-invitation-generation** — `/Users/melbourne/.agents/skills/wedding-invitation-generation` — Generate beautiful wedding invitations, save the dates, RSVP cards, and wedding programs using each::sense AI. Create classic, modern, floral, rustic, destination, and cultural wedding stationery designs.

- **weekly-management-review** — `/Users/melbourne/.agents/skills/weekly-management-review` — Run a recurring weekly management review across goals, commitments, KPIs, projects, people, finances, risks, decisions, and next-week priorities.

- **weightloss-analyzer** — `/Users/melbourne/.agents/skills/weightloss-analyzer` — 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段

- **wellally-tech** — `/Users/melbourne/.agents/skills/wellally-tech` — Integrate multiple digital health data sources, connect to [WellAlly.tech](https://www.wellally.tech/) knowledge base, providing data import and knowledge reference for personal health management systems.

- **whatsapp-automation** — `/Users/melbourne/.agents/skills/whatsapp-automation` — Automate WhatsApp Business tasks via Rube MCP (Composio): send messages, manage templates, upload media, and handle contacts. Always search tools first for current schemas.

- **whatsapp-cloud-api** — `/Users/melbourne/.agents/skills/whatsapp-cloud-api` — Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python.

- **wiki-architect** — `/Users/melbourne/.agents/skills/wiki-architect` — You are a documentation architect that produces structured wiki catalogues and onboarding guides from codebases.

- **wiki-builder** — `/Users/melbourne/.agents/skills/wiki-builder` — Create and maintain reusable research wikis with source provenance, configurable structure, and local markdown outputs.

- **wiki-changelog** — `/Users/melbourne/.agents/skills/wiki-changelog` — Generate structured changelogs from git history. Use when user asks \"what changed recently\", \"generate a changelog\", \"summarize commits\" or user wants to understand recent development activity.

- **wiki-onboarding** — `/Users/melbourne/.agents/skills/wiki-onboarding` — Generate two complementary onboarding documents that together give any engineer — from newcomer to principal — a complete understanding of a codebase. Use when user asks for onboarding docs or getting-started guides, use

- **wiki-page-writer** — `/Users/melbourne/.agents/skills/wiki-page-writer` — You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth.

- **wiki-qa** — `/Users/melbourne/.agents/skills/wiki-qa` — Answer repository questions grounded entirely in source code evidence. Use when user asks a question about the codebase, user wants to understand a specific file, function, or component, or user asks \"how does X work\" 

- **wiki-researcher** — `/Users/melbourne/.agents/skills/wiki-researcher` — You are an expert software engineer and systems analyst. Use when user asks \"how does X work\" with expectation of depth, user wants to understand a complex system spanning many files, or user asks for architectural ana

- **wiki-vitepress** — `/Users/melbourne/.agents/skills/wiki-vitepress` — Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams. Use when user asks to \"build a site\" or \"package as VitePress\", user runs the /deep-wiki

- **windows-privilege-escalation** — `/Users/melbourne/.agents/skills/windows-privilege-escalation` — Provide systematic methodologies for discovering and exploiting privilege escalation vulnerabilities on Windows systems during penetration testing engagements.

- **windows-shell-reliability** — `/Users/melbourne/.agents/skills/windows-shell-reliability` — Reliable command execution on Windows: paths, encoding, and common binary pitfalls.

- **wireshark-analysis** — `/Users/melbourne/.agents/skills/wireshark-analysis` — Execute comprehensive network traffic analysis using Wireshark to capture, filter, and examine network packets for security investigations, performance optimization, and troubleshooting.

- **wordpress** — `/Users/melbourne/.agents/skills/wordpress` — Complete WordPress development workflow covering theme development, plugin creation, WooCommerce integration, performance optimization, and security hardening. Includes WordPress 7.0 features: Real-Time Collaboration, AI

- **wordpress-centric-high-seo-optimized-blogwriting-skill** — `/Users/melbourne/.agents/skills/wordpress-centric-high-seo-optimized-blogwriting-skill` — Generate clean, human-sounding, SEO-optimized WordPress blog posts with optional Yoast metadata, JSON-LD schema markup, and image SEO planning. Supports modular batch output.

- **wordpress-penetration-testing** — `/Users/melbourne/.agents/skills/wordpress-penetration-testing` — Assess WordPress installations for common vulnerabilities and WordPress 7.0 attack surfaces.

- **wordpress-plugin-development** — `/Users/melbourne/.agents/skills/wordpress-plugin-development` — WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, security best practices, and WordPress 7.0 features: Real-Time Collaboration, AI Connectors, Abilities API, DataViews

- **wordpress-theme-development** — `/Users/melbourne/.agents/skills/wordpress-theme-development` — WordPress theme development workflow covering theme architecture, template hierarchy, custom post types, block editor support, responsive design, and WordPress 7.0 features: DataViews, Pattern Editing, Navigation Overlay

- **wordpress-woocommerce-development** — `/Users/melbourne/.agents/skills/wordpress-woocommerce-development` — WooCommerce store development workflow covering store setup, payment integration, shipping configuration, customization, and WordPress 7.0 features: AI connectors, DataViews, and collaboration tools.

- **workflow-automation** — `/Users/melbourne/.agents/skills/workflow-automation` — Workflow automation is the infrastructure that makes AI agents

- **workflow-orchestration-patterns** — `/Users/melbourne/.agents/skills/workflow-orchestration-patterns` — Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices for building reliable distributed systems.

- **workflow-patterns** — `/Users/melbourne/.agents/skills/workflow-patterns` — Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git commits for tasks, or understanding the verification protocol.

- **wrike-automation** — `/Users/melbourne/.agents/skills/wrike-automation` — Automate Wrike project management via Rube MCP (Composio): create tasks/folders, manage projects, assign work, and track progress. Always search tools first for current schemas.

- **writing-great-skills** — `/Users/melbourne/.agents/skills/writing-great-skills` — Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable.

- **writing-plans** — `/Users/melbourne/.agents/skills/writing-plans` — Use when you have a spec or requirements for a multi-step task, before touching code

- **writing-skills** — `/Users/melbourne/.agents/skills/writing-skills` — Use when creating, updating, or improving agent skills.

- **x-article-publisher-skill** — `/Users/melbourne/.agents/skills/x-article-publisher-skill` — Publish articles to X/Twitter

- **x-twitter-scraper** — `/Users/melbourne/.agents/skills/x-twitter-scraper` — X/Twitter automation skill for tweet search, follower export, posting, DMs, webhooks, MCP, SDKs, Hermes Tweet, and TweetClaw.

- **x402-express-wrapper** — `/Users/melbourne/.agents/skills/x402-express-wrapper` — Wrapper oficial de M2MCent (Node.js) para inyectar muros de pago x402 en APIs o servidores Model Context Protocol (MCP). Usar al construir nuevos servicios que requieran monetización máquina a máquina.

- **xiaohongshu-content-strategist** — `/Users/melbourne/.agents/skills/xiaohongshu-content-strategist` — Create viral Xiaohongshu (小红书) content with platform-native strategy, save-rate optimization, trending formats, and search SEO for China's #1 lifestyle platform.

- **xlsx-official** — `/Users/melbourne/.agents/skills/xlsx-official` — Unless otherwise stated by the user or existing template

- **xss-html-injection** — `/Users/melbourne/.agents/skills/xss-html-injection` — Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demonstrate exploitation techniques for session hijacking and credential theft, and vali

- **xvary-stock-research** — `/Users/melbourne/.agents/skills/xvary-stock-research` — Thesis-driven equity analysis from public SEC EDGAR and market data; /analyze, /score, /compare workflows with bundled Python tools (Claude Code, Cursor, Codex).

- **yann-lecun** — `/Users/melbourne/.agents/skills/yann-lecun` — Agente que simula Yann LeCun — inventor das Convolutional Neural Networks, Chief AI Scientist da Meta, Prêmio Turing 2018.

- **yann-lecun-debate** — `/Users/melbourne/.agents/skills/yann-lecun-debate` — Sub-skill de debates e posições de Yann LeCun. Cobre críticas técnicas detalhadas aos LLMs, rivalidades intelectuais (LeCun vs Hinton, Sutskever, Russell, Yudkowsky, Bostrom), lista completa de rejeições a afirmações mai

- **yann-lecun-filosofia** — `/Users/melbourne/.agents/skills/yann-lecun-filosofia` — Sub-skill filosófica e pedagógica de Yann LeCun.

- **yann-lecun-tecnico** — `/Users/melbourne/.agents/skills/yann-lecun-tecnico` — Sub-skill técnica de Yann LeCun. Cobre CNNs, LeNet, backpropagation, JEPA (I-JEPA, V-JEPA, MC-JEPA), AMI (Advanced Machinery of Intelligence), Self-Supervised Learning (SimCLR, MAE, BYOL), Energy-Based Models (EBMs) e có

- **yao-meta-skill** — `/Users/melbourne/.agents/skills/yao-meta-skill` — Create, refactor, evaluate, and package agent skills from workflows, prompts, transcripts, docs, or notes. Use for skill creation, reusable workflow packaging, skill improvement, evals, and team-ready distribution.

- **yes-md** — `/Users/melbourne/.agents/skills/yes-md` — 6-layer AI governance: safety gates, evidence-based debugging, anti-slack detection, and machine-enforced hooks. Makes AI safe, thorough, and honest.

- **yield-intelligence** — `/Users/melbourne/.agents/skills/yield-intelligence` — Passive income portfolio analysis — activate when user asks about dividend yields, Treasury rates, REIT income, monthly passive income goals, or portfolio yield optimization. Scans 4 asset classes, ranks by risk-adjusted

- **youtube-automation** — `/Users/melbourne/.agents/skills/youtube-automation` — Automate YouTube tasks via Rube MCP (Composio): upload videos, manage playlists, search content, get analytics, and handle comments. Always search tools first for current schemas.

- **youtube-full** — `/Users/melbourne/.agents/skills/youtube-full` — Fetch YouTube transcripts, search videos, browse channels, and extract playlists via TranscriptAPI — no yt-dlp, no Google API key, works from any cloud server.

- **youtube-notetaker** — `/Users/melbourne/.agents/skills/youtube-notetaker` — Turn YouTube talks into local study notes with slides, transcripts, editable annotations, and a markdown-backed viewer.

- **youtube-seo-optimizer** — `/Users/melbourne/.agents/skills/youtube-seo-optimizer` — >

- **youtube-summarizer** — `/Users/melbourne/.agents/skills/youtube-summarizer` — Extract transcripts from YouTube videos and generate comprehensive, detailed summaries using intelligent analysis frameworks

- **youtube-thumbnail-generation** — `/Users/melbourne/.agents/skills/youtube-thumbnail-generation` — Generate click-worthy YouTube thumbnails with high CTR designs using each::sense API

- **youtube-video-generation** — `/Users/melbourne/.agents/skills/youtube-video-generation` — Generate YouTube videos and Shorts using each::sense AI. Create faceless videos, explainers, tutorials, product reviews, compilations, and more optimized for YouTube's formats and best practices.

- **zapier-make-patterns** — `/Users/melbourne/.agents/skills/zapier-make-patterns` — No-code automation democratizes workflow building. Zapier and Make

- **zendesk-automation** — `/Users/melbourne/.agents/skills/zendesk-automation` — Automate Zendesk tasks via Rube MCP (Composio): tickets, users, organizations, replies. Always search tools first for current schemas.

- **zeroize-audit** — `/Users/melbourne/.agents/skills/zeroize-audit` — Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code han

- **zipai-optimizer** — `/Users/melbourne/.agents/skills/zipai-optimizer` — Ultra-dense token optimizer skill for prompt caching, log pruning, AST-based inspection, and minified JSON payloads.

- **zod-validation-expert** — `/Users/melbourne/.agents/skills/zod-validation-expert` — Expert in Zod — TypeScript-first schema validation. Covers parsing, custom errors, refinements, type inference, and integration with React Hook Form, Next.js, and tRPC.

- **zoho-crm-automation** — `/Users/melbourne/.agents/skills/zoho-crm-automation` — Automate Zoho CRM tasks via Rube MCP (Composio): create/update records, search contacts, manage leads, and convert leads. Always search tools first for current schemas.

- **zoom-automation** — `/Users/melbourne/.agents/skills/zoom-automation` — Automate Zoom meeting creation, management, recordings, webinars, and participant tracking via Rube MCP (Composio). Always search tools first for current schemas.

- **zustand-store-ts** — `/Users/melbourne/.agents/skills/zustand-store-ts` — Create Zustand stores following established patterns with proper TypeScript types and middleware.

- **adapt** — `/Users/melbourne/.cursor/skills/adapt` — Responsive layout pass covering breakpoints, touch targets, safe areas, and fluid type. Use when the UI has layout or touch issues on mobile/tablet, when adding a new screen that hasn't been tested across viewports, or w

- **animate** — `/Users/melbourne/.cursor/skills/animate` — Motion design pass — adds purposeful animations or removes excessive ones, respecting MOTION_INTENSITY and the project's animation stack. Use when the user asks to add animation, "make it feel smoother", fix janky transi

- **audit** — `/Users/melbourne/.cursor/skills/audit` — Technical UI audit — a11y, performance, responsive. Produces a prioritized findings table. Invoke when the user asks for audit on their UI, or mentions 'audit' alongside design / UI / frontend work.

- **bolder** — `/Users/melbourne/.cursor/skills/bolder` — Amplify personality — raises layout variance and motion, strengthens typography and one signature detail, without slop. Use when the UI works but feels safe, flat, or "template-y", or when the user says "bolder", "more p

- **brief** — `/Users/melbourne/.cursor/skills/brief` — Write or update the project's durable design brief at .ui-craft/brief.md. Invoke when the user asks for brief on their UI, or mentions 'brief' alongside design / UI / frontend work.

- **clarify** — `/Users/melbourne/.cursor/skills/clarify` — UX copy review across buttons, errors, empty states, and form hints — critiques by default, applies only on request. Use when copy feels vague, generic, or AI-sounding, or when the user says "fix the labels", "improve er

- **colorize** — `/Users/melbourne/.cursor/skills/colorize` — Color strategy pass — introduces a single accent at 3-5 intentional placements, or reduces an over-colored UI back to 90% neutral. Use when the UI has no color identity, uses blue by default, or is shouting with too many

- **craft** — `/Users/melbourne/.cursor/skills/craft` — One-shot build pipeline for a complete surface from an outcome recipe — inputs (or defaults) → composition → theme → build order → acceptance bar. Use when the user asks for a whole surface ("build me a dashboard", "hazm

- **critique** — `/Users/melbourne/.cursor/skills/critique` — Design lens critique covering visual hierarchy, clarity, and anti-slop patterns — produces a findings table, no code edits unless asked. Use when the user wants a design review, says "what's wrong with this UI", or needs

- **delight** — `/Users/melbourne/.cursor/skills/delight` — Delight pass — adds one or two memorable micro-interactions (copy specificity, hover choreography, state transitions, one signature detail) without decoration or confetti. Use when the UI works but feels generic, or when

- **distill** — `/Users/melbourne/.cursor/skills/distill` — Reduction pass — cuts content, structure, visuals, and dead code that doesn't answer a user question or drive an action, respecting CRAFT_LEVEL. Use when the UI feels cluttered, has too many CTAs, walls of text, or decor

- **extract** — `/Users/melbourne/.cursor/skills/extract` — Refactoring pass — extracts repeated Tailwind class combos and markup into components, and lifts magic values into design tokens. Use when the codebase has obvious duplication, hardcoded hex values or pixel sizes, or whe

- **finalize** — `/Users/melbourne/.cursor/skills/finalize` — Pre-ship gate — runs detector, verifies brief and tokens, applies the 10-pass finish bar, ranks findings by feedback hierarchy. Use when the user wants to ship, merge, or finalize a surface and needs a verdict (READY / N

- **harden** — `/Users/melbourne/.cursor/skills/harden` — Production-readiness pass — audits and implements the full non-happy-path matrix: loading skeletons, empty states, error messages, partial data, i18n, offline, permissions, and first-run guidance. Use when preparing a su

- **heuristic** — `/Users/melbourne/.cursor/skills/heuristic` — Produce a scored heuristic critique of the UI using Nielsen's 10 + 6 design laws + optional persona walkthroughs. Outputs a machine-parseable scorecard plus a 0-100 UsabilityScore (the judged companion to the determinist

- **polish** — `/Users/melbourne/.cursor/skills/polish` — Final craft pass applying the compound details from the polish checklist — micro-typography, spacing rhythm, hover states, and a signature detail — directly to code. Use when the surface is functionally complete but feel

- **quieter** — `/Users/melbourne/.cursor/skills/quieter` — Tone down visual noise — lowers variance and motion, simplifies layout and color weight, keeps hierarchy clear. Use when the UI feels loud, busy, or over-designed, or when the user says "quieter", "more restrained", "sim

- **redesign** — `/Users/melbourne/.cursor/skills/redesign` — Redesign an existing site or app without losing what already works — audits the current surface first, classifies what to preserve (brand, IA, SEO, content), picks a refresh/reskin/rebuild scope, then modernizes delibera

- **remember** — `/Users/melbourne/.cursor/skills/remember` — Record a learned design constraint from a correction into the project brief. Invoke when the user asks for remember on their UI, or mentions 'remember' alongside design / UI / frontend work.

- **sddesign** — `/Users/melbourne/.cursor/skills/sddesign` — Full spec-driven pipeline — walks brief → tokens → shape (spec) → craft (build) → converge → ship in one guided run. Writes `.ui-craft/spec.md`. Run when starting a net-new surface from scratch. Invoke when the user asks

- **shape** — `/Users/melbourne/.cursor/skills/shape` — Wireframe-first pass — outputs an ASCII layout + state list + content inventory + question list before any code. Use when starting a new screen from scratch or when the user's brief is still ambiguous. Invoke when the us

- **social-media** — `/Users/melbourne/.cursor/skills/social-media` — Social media strategy, content creation, and platform optimization. Use when creating social content, developing engagement strategies, optimizing for platform algorithms, or building community.

- **start** — `/Users/melbourne/.cursor/skills/start` — Front door. Reads the current project (framework, tokens, brief, spec, harness) and reports what ui-craft can do right now, then routes you to the right next step. Run this first if you're new or unsure where to begin. N

- **tokens** — `/Users/melbourne/.cursor/skills/tokens` — Audit or establish the project's 3-layer token spine. Invoke when the user asks for tokens on their UI, or mentions 'tokens' alongside design / UI / frontend work.

- **typeset** — `/Users/melbourne/.cursor/skills/typeset` — Typography pass covering font choice, modular scale, tracking, leading, weight hierarchy, and micro-typography details. Use when fonts feel generic (default Inter with no reason), the scale is ad hoc, hierarchy is flat, 

- **ui-craft** — `/Users/melbourne/.cursor/skills/ui-craft` — Use for UI design and implementation work to avoid generic AI-looking interfaces. Provides anti-slop rules, a required discovery phase before coding, and guidance for layout, typography, color, motion, accessibility, das

- **ui-craft-dense-dashboard** — `/Users/melbourne/.cursor/skills/ui-craft-dense-dashboard` — Dense dashboard / admin / Bloomberg / Retool / data-heavy internal tools. Locked knobs: CRAFT=7, MOTION=3, DENSITY=9. IBM Plex + mono numbers, semantic palette, 4/8px grid, sparklines, tabular-nums. Trigger on: dashboard

- **ui-craft-editorial** — `/Users/melbourne/.cursor/skills/ui-craft-editorial` — Editorial / magazine / long-form / Medium / Substack / content-heavy UIs. Locked knobs: CRAFT=9, MOTION=4, DENSITY=3. Serif display + humanist body, wide reading column, drop caps, OpenType. Trigger on: editorial, magazi

- **ui-craft-minimal** — `/Users/melbourne/.cursor/skills/ui-craft-minimal` — Minimal / clean / Linear / Notion / Vercel / whitespace-heavy UIs. Locked knobs: CRAFT=8, MOTION=3, DENSITY=2. Monochrome + one accent, Inter/Geist, hairline borders over shadows. Trigger on: minimal, clean, Linear-like,

- **unhappy** — `/Users/melbourne/.cursor/skills/unhappy` — State-first design pass — inventories and implements all non-happy states (loading, empty, error, partial, conflict, offline) before the happy path, and refactors impossible boolean state to proper state machines. Use wh

<!-- github-copilot-toolbox:mcp-skills-awareness-end -->
