> Web version: [patrickcmserrano.github.io/resume/](https://patrickcmserrano.github.io/resume/)

<div align="center">

# Patrick Serrano

**Senior Software Engineer (Backend · AI Infrastructure)**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-patrickcmserrano-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/patrickcmserrano)
[![GitHub](https://img.shields.io/badge/GitHub-patrickcmserrano-181717?style=flat&logo=github&logoColor=white)](https://github.com/patrickcmserrano)
[![Email](https://img.shields.io/badge/Email-patrickcmserrano%40gmail.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:patrickcmserrano@gmail.com)

</div>

---

> 7+ years building high-throughput financial systems, payment orchestration platforms, and quantitative trading infrastructure. More recently I have been building corporate AI infrastructure: LLM routing and on-demand serving (Go, Clojure, Slurm, vLLM), agent pipelines, and grounded RAG with governance and auditing. My background in Physics sharpened how I reason about systems: precision, invariants, and what happens at the boundary conditions.

---

## Technical Profile

| Area | Technologies |
|---|---|
| **Languages** | Go, Clojure, TypeScript, ClojureScript, Python, SQL |
| **Frontend** | Svelte 5, React, Fulcro, Reagent, React Native, Wails v2, Tailwind CSS |
| **Backend** | Go (Chi, WebSocket), Node.js, Clojure (Pathom 3, Pedestal, Reitit, Onyx) |
| **Databases** | PostgreSQL, Datomic, Redis |
| **Messaging** | NATS JetStream, Onyx, AWS SQS |
| **AI / LLM** | LLM orchestration (routing, fallback, circuit breaking), on-demand serving (vLLM/Slurm, tensor-parallel, NVFP4), hybrid RAG (dense + BM25 + RRF), cross-encoder rerank, Claude API, Ollama, NVIDIA NIM |
| **Architecture** | Event-Driven, CQRS, Microservices, Clean Architecture, Polylith, ETL Pipelines |
| **Infra / DevOps** | AWS (ECS, Lambda, SQS, SSM), FreeBSD (VNET jails, ZFS, pf), Slurm, WireGuard, OpenTofu/Terraform, Ansible, Docker, Pulumi, CI/CD, GitHub Actions, Prometheus |
| **Financial Domain** | Payment Gateways (Adyen, Cielo, eRede, Pagar.me, Mercado Pago, Getnet, Tuna, Unico), Anti-Fraud (ClearSale, Konduto), E-commerce (VTEX, Loja Integrada) |

---

## Professional Experience

### Corporate AI Platform & Agent Factory — NeoTek / AI Factory
**Technical Partnership · innovation-sector client** &nbsp;·&nbsp; 2026 – Present

Agent-assisted engineering infrastructure built in partnership with Ian Fernandez (NeoTek MaaS Industries): a control loop joining context, model routing, and execution, with agents operating in isolated, auditable workspaces. Sustains in production a corporate LLM chat portal (RAG, SSO, and per-user isolation) delivered to an innovation-sector client.

- Built a multi-provider inference router in Go — a single OpenAI-compatible endpoint over multiple models (own GPU fleet + serverless), with declarative routing policies, fallback chains, retry with backoff+jitter, and per-provider circuit breaking
- Delivered on-demand LLM serving on GPU (Clojure + Slurm + vLLM): a vLLM 0.26→0.28 upgrade cut **TTFT from 0.43s to 0.02s (−95%)**; two-node tensor-parallel serving on DGX Spark with fixed per-node placement to eliminate eviction thrash
- Built the observe/plan/act/verify agent pipeline (Clojure): multi-role orchestrator (planner → implementer → tests → reviewer → gate) with a declarative agent-role layer — **815 tests / 3104 assertions**
- Proved security and compliance end to end: immutable audit trail (SHA-256 chained hash, integrity-verification endpoint), fail-closed stop chain, egress allowlist, and PII redaction
- Ran Infrastructure as Code on FreeBSD: OpenTofu + Ansible, VNET jails, WireGuard networking, and deny-by-default pf — reproducible provisioning and verifiable deploys
- Added compute-estate cost telemetry (power collector + Slurm GPU-hours → aggregator), Prometheus metrics, and an embedded operations dashboard

`Go` `Clojure` `ClojureScript` `FreeBSD` `Slurm` `vLLM` `WireGuard` `OpenTofu` `Ansible` `Open WebUI` `Qdrant` `Prometheus` `Docker`

---

### Multi-Tenant AI Agent Engine — Rohana / Daelaam
**Independent Project** &nbsp;·&nbsp; 2026 – Present

Conversational AI engine in Clojure for per-tenant agents, with RAG grounded on each client's own documents, schedule guardrails, and LGPD-by-design physical isolation. Channels are WhatsApp and Telegram; the full pipeline is validated end to end (webhook → message bus → Pathom graph → response).

- **Pathom 3 as orchestrator:** each agent capability (tenant → intent → guardrail → rag → llm → response) is an independent resolver — the graph resolves only what each message needs
- **Physical multi-tenant isolation:** a dedicated vector index per tenant (TurboVec in-process via libpython-clj; Qdrant as an alternative provider) with the tenant id stamped by the store and validated fail-closed on every search — zero cross-client leakage (LGPD by construction)
- **Fail-closed privacy gate:** every LLM call is scrubbed by Presidio (pt-BR NLP analyzer + anonymizer); ingestion sanitizes before embedding, and any component being unavailable refuses the operation rather than leaking
- **Message bus &amp; grounding:** migrated the event bus from NATS JetStream to an embedded Aeron media driver (IPC), and grounding is only marked true when the answer cites a real retrieved source — not when it merely avoids the refusal phrase
- **Zero-code tenant onboarding:** each client is a single .edn file with persona, schedule guardrails, RAG collection, and active channels — automated deploy to VPS via GitHub Actions
- **OSM lead Probe:** OpenStreetMap scraper → 5-signal digital presence score → Telegram alert; 88 SMB leads validated in Niterói at zero API cost

`Clojure` `Pathom 3` `Aeron` `TurboVec` `Qdrant` `NATS JetStream` `Presidio` `FastAPI` `Claude API` `NVIDIA NIM` `Ollama` `Datahike` `Telegram Bot API`

---

### Algorithmic Trading Platform — Ark
**Lead Architect & Developer** &nbsp;·&nbsp; 2025 – 2026

Proprietary event-driven trading platform spanning research, live market data, strategy, and order execution — built as a Clojure/Polylith foundation (bitemporal risk engine) and later re-implemented in Go, with availability, resilience, and traceability as first-class requirements.

- **Risk engine as code ("constitution"):** hard stops in BigDecimal for drawdown, leverage, position size and data staleness, expressed as pure components and verified with generative tests (test.check) — bitemporal history persisted in XTDB for exact time-travel reconstruction
- **Clojure → Go re-architecture:** migrated a Clojure/Polylith system (XTDB + Redis Streams) to a single Go binary on NATS JetStream, keeping the same event-driven, immutable-log principles while removing the JVM and broker footprint
- **Multi-exchange pipeline:** Bitget, OKX and Bybit (plus Yahoo Finance macro) normalized onto one NATS JetStream event log — backtesting and live paper trading run against the same events by structural design
- **Measured performance:** HTTP → native IPC transport migration cut streaming latency ~**100×** (~100–200µs → ~1µs) and desktop memory usage **70–78%**; indicator pipeline benchmark **~66µs / 100 candles** (scaling linearly to 0.7ms at 1000)
- **Order execution on Bitget:** signed REST adapter (place/close, SL/TP, leverage and margin-mode) behind a RiskGuard with a kill-switch and reconciliation, running in shadow/paper mode gated by pre-registered validation criteria
- **Desktop terminal:** Wails v2 + Svelte 5 with a Go↔frontend IPC bridge, real-time streaming of market, aggression and liquidation data, and multi-symbol/multi-monitor layouts — released as v1.2.1 with CI (Gitleaks, Go build/test, frontend build)

`Go` `Clojure` `ClojureScript` `Polylith` `XTDB` `NATS JetStream` `Redis Streams` `Wails v2` `Svelte 5` `Chi` `Malli` `Prometheus` `Docker`

---

### Multi-Acquirer Payment Platform — Octopus Pay
**Senior Software Engineer** &nbsp;·&nbsp; 2022 – 2025

High-availability financial orchestration platform managing 25+ live integrations for e-commerce and payment gateways, processing millions of financial events per month.

- Architected **Summon**, a high-throughput ETL engine ingesting, enriching, and processing financial events with strict delivery guarantees and circuit-breaker patterns
- Designed and maintained 25+ canonical adapters for payment gateways (Adyen, Cielo, Pagar.me) and anti-fraud systems, maintaining **99.99% uptime** on critical flows
- Implemented a transactional-analytical architecture using Datomic (immutable log) and Pathom 3, enabling real-time derivation of hundreds of computed financial attributes via EQL/Datalog
- Built full-stack administrative dashboards in ClojureScript + Fulcro RAD with direct Datomic/Datalog integration; added operational alerting on routing and approval intelligence
- Managed cloud infrastructure via Pulumi (AWS) and authored comprehensive test suites — unit, integration, and contract — enforcing correctness-first bug discipline
- Conducted rigorous code reviews, pair programming sessions, and mentored junior/mid-level engineers on architecture and testing discipline

`Clojure` `ClojureScript` `Datomic` `Pathom 3` `Fulcro RAD` `Clara Rules` `Onyx` `AWS` `Pulumi`

---

### B2B Marketplace Platform — Zougue / MPMS
**Backend Engineer** &nbsp;·&nbsp; 2020 – 2022

Enterprise-grade marketplace management platform integrated with major e-commerce ecosystems.

- Built complex integration endpoints with VTEX for inventory, pricing, and order management across high-volume SKU updates
- Developed a white-label marketplace portal with magic-link authentication and per-client Metabase analytics powered by Datalog queries against immutable data history
- Designed multi-tenant Datomic schemas and Pathom resolvers for multi-seller marketplace queries with real-time computed attributes
- Implemented forward-chaining business rules in Clara Rules for order routing and financial attribute computation

`Clojure` `ClojureScript` `Fulcro` `Datomic` `Pathom 3` `Clara Rules` `VTEX` `Metabase`

---

<details>
<summary><strong>Earlier Experience (2018 – 2019)</strong></summary>

<br>

**Real Estate Platform** — Full-stack mobile and web application built from scratch for decentralized property listing and negotiation. Iterated continuously on UX based on real user feedback.

`ClojureScript` `Fulcro` `React Native`

**Fintech Payment Gateway** — Front-end development and early financial integrations for a payment gateway startup, establishing foundations in payment flow traceability and security practices.

`ClojureScript` `Fulcro` `REST APIs`

</details>

---

## Education

**Bachelor's in Software Engineering** — Descomplica Faculdade Digital &nbsp;·&nbsp; 2024 – Present

**Bachelor's in Physics (incomplete)** — Universidade Federal Fluminense &nbsp;·&nbsp; 2015 – 2018

**Full Cycle 3.0** — OAuth 2.0, Keycloak, Kafka, Microservices, Hexagonal Architecture, DDD, Kubernetes, Terraform, Observability

---

## Languages

| Language | Level |
|---|---|
| Portuguese | Native |
| English | Advanced — Full Professional Fluency |
| German | Basic |
| Spanish | Basic |

---

## Project Structure & PDF Generation

This repository uses a structured directory layout for managing resume versions tailored to different companies and roles.

### Project Layout
- [_base/](_base/) — Baseline LaTeX CVs in Portuguese ([Patrick_Serrano_CV_2026.tex](_base/Patrick_Serrano_CV_2026.tex)) and English ([Patrick_Serrano_CV_EN_2026.tex](_base/Patrick_Serrano_CV_EN_2026.tex)).
- [in-progress/](in-progress/) — Active applications and interview preparation materials (e.g. Arco Educação, Stone, Buzzlabs).
- [todo/](todo/) — Drafts, JD analyses, and target CV files for potential/upcoming candidacies (e.g. Brasil Paralelo, OLX, Globo).
- [archived/](archived/) — Older, unmaintained resume versions.

### Source of Truth
- [resume.yaml](resume.yaml) is the single source of truth for the web version ([index.html](index.html)) and [README.md](README.md).
- Regenerate them with:
  ```bash
  python3 build.py
  ```
- Check that the web source (`resume.yaml`) and the LaTeX sources (`_base/*.tex`) list the same experience entries:
  ```bash
  python3 consistency.py
  ```
  Both checks run in CI (job `check-generated`) and fail the build if the sources drift.

### How to Compile PDFs Locally
Because compiling LaTeX requires a large set of TeX packages and engines, you can compile any `.tex` file locally using Docker without needing to install TeX Live on your host system:

1. **Navigate** to the directory containing the `.tex` file you want to compile:
   ```bash
   cd todo/brasilparalelo
   ```
2. **Run the compiler** inside the `ghcr.io/xu-cheng/texlive-full` Docker container:
   ```bash
   docker run --rm -v "$(pwd)":/workdir -w /workdir ghcr.io/xu-cheng/texlive-full pdflatex Patrick_Serrano_CV_BrasilParalelo_2026.tex
   ```
   This compiles the `.tex` file and produces the output `.pdf` file in the same directory.

### Automation with GitHub Actions
When you push changes on the `master` branch to GitHub, the configured Actions workflow (defined in [.github/workflows/build-cv.yml](.github/workflows/build-cv.yml)) automatically compiles the configured `.tex` resume files and uploads them as workflow build artifacts.

