> Web version: [patrickcmserrano.github.io/resume](https://patrickcmserrano.github.io/resume/)

<div align="center">

# Patrick Serrano

**Senior Fullstack Engineer**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-patrickcmserrano-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/patrickcmserrano)
[![GitHub](https://img.shields.io/badge/GitHub-patrickcmserrano-181717?style=flat&logo=github&logoColor=white)](https://github.com/patrickcmserrano)
[![Email](https://img.shields.io/badge/Email-patrickcmserrano%40gmail.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:patrickcmserrano@gmail.com)

</div>

---

> 7+ years building high-throughput financial systems, payment orchestration platforms, and quantitative trading infrastructure. I work across the full stack — from distributed messaging pipelines and bitemporal data models on the backend to reactive desktop and web interfaces on the frontend. My background in Physics sharpened how I reason about systems: precision, invariants, and what happens at the boundary conditions.

---

## Technical Profile

| Area | Technologies |
|---|---|
| **Languages** | Go, Clojure, TypeScript, ClojureScript, Python, SQL |
| **Frontend** | Svelte 5, React, Next.js, Fulcro, Reagent, React Native, Wails v2, Tailwind CSS |
| **Backend** | Go (Chi, WebSocket), Node.js, NestJS, Fastify, Clojure (Pathom 3, Pedestal, Reitit, Onyx) |
| **Databases** | PostgreSQL, Datomic, Redis, DynamoDB, MongoDB |
| **Messaging** | NATS JetStream, Kafka, RabbitMQ, AWS SQS, Redis Streams |
| **Architecture** | Event-Driven, CQRS, Event Sourcing, Microservices, Clean Architecture, Polylith |
| **Infra / DevOps** | AWS (ECS, Lambda, SQS, SSM), Docker, Kubernetes, Pulumi, CI/CD, GitHub Actions |
| **Financial Domain** | Payment Gateways (Adyen, Cielo, Pagar.me, Getnet), Anti-Fraud (ClearSale, Konduto), VTEX |

---

## Professional Experience

### Quantitative Trading Infrastructure — Ark Engine
**Lead Architect & Developer** &nbsp;·&nbsp; 2025 – Present

High-performance automated trading engine with ultra-low latency event processing, bitemporal auditability, and a desktop interface for portfolio management across multiple exchanges.

- Redesigned the core decision engine from Python to Go, achieving end-to-end event processing latency of **~43µs**
- Built a multi-exchange data collection pipeline normalized over NATS JetStream, ensuring backtesting and production execute against the same event log
- Migrated transport layer from HTTP to native IPC, reducing RAM usage by **78%** and cutting streaming latency by **100×**
- Implemented a "dual-store" pattern using XTDB (Valid Time / Transaction Time) to structurally eliminate lookahead bias and guarantee 100% financial auditability
- Developed high-performance desktop interface with Wails v2 and Svelte 5, streaming live order state via WebSocket; headless collector runs 24/7 on VPS with stateful checkpoint/recovery

`Go 1.23` `Svelte 5` `Wails v2` `NATS JetStream` `XTDB` `PostgreSQL` `WebSocket` `Docker`

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

**Bachelor's in Physics** (incomplete) — Universidade Federal Fluminense &nbsp;·&nbsp; 2015 – 2018

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

<div align="center">

*This repository contains the LaTeX source files and compiled PDFs for targeted resume variants.*

</div>
