> Web version: [patrickcmserrano.github.io/resume/](https://patrickcmserrano.github.io/resume/)

<div align="center">

# Patrick Serrano

**Senior Fullstack Engineer**

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

### Quantitative Trading Infrastructure — Ark Engine
**Lead Architect & Developer** &nbsp;·&nbsp; 2025 – Present

Proprietary financial platform in Go for collecting, processing, and executing orders across multiple exchanges — with availability, resilience, and traceability treated as first-class requirements.

- Built a multi-exchange pipeline (Bitget, Binance, Bybit, OKX + Yahoo Finance) with normalized events over NATS JetStream — backtesting and production run against the same event log by structural design
- Designed for availability from day one: headless collector runs 24/7 on VPS with periodic state checkpoint and transparent reconnection after network failures
- Migrated transport layer from HTTP to native IPC: **70–78% less RAM**, **100× lower streaming latency**; pipeline benchmark **~66µs / 100 candles**
- Integrated real order execution on Bitget — SL/TP management, leverage and margin controls; signal and execution in the same system, no friction between analysis and action
- Developed high-performance desktop interface with Wails v2 and Svelte 5, streaming live order state via WebSocket

`Go 1.23` `Svelte 5` `Wails v2` `NATS JetStream` `PostgreSQL` `WebSocket` `Docker`

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

