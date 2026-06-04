# Processo Seletivo — Isaac (Arco Educação)
## Software Engineer II · Backend (Go) · Time de Identidade & Plataforma

**Data de inscrição:** 2026-06-03
**Status:** Inscrito — aguardando retorno

---

## Arquivos desta pasta

| Arquivo | Descrição |
|---|---|
| `Patrick_Serrano_Backend_Go_Isaac_2026.tex` | Currículo fonte LaTeX |
| `Patrick_Serrano_Backend_Go_Isaac_2026.pdf` | Currículo PDF enviado |
| `ENTREVISTA_ISAAC_PREP.md` | Guia de preparação: STAR situations, perguntas técnicas, plano de estudos |
| `ENTREVISTA_ISAAC_PREP.pdf` | Versão PDF do guia |
| `jd.md` | Job description original |
| `stack.md` | Tech stack do isaac (via stackshare) |

---

## Sobre a vaga

**Time:** Identidade & Plataforma — guarda dados sensíveis, gerenciamento de acesso, acelera outras squads.
**Foco:** Go backend, APIs, microserviços distribuídos.
**Stack confirmada:** Go (Fiber), PostgreSQL, Redis, Kafka + Debezium, Kubernetes, Rancher, Terraform, GCP, GitHub Actions, Datadog, Sentry.

---

## O currículo

### Decisões tomadas
- **Título:** "Sênior Backend (Clojure · Go)" — honesto sobre as duas linguagens, Go em destaque
- **Resumo:** narrativa pessoal — Física interrompida, consultoria, Ark Streams como produto real, transição para produto
- **Ark Streams:** reescrito com ângulo de produto — origem na frustração real de operar cripto, visão de democratização, decisões arquiteturais com evidência
- **Octopus Pay:** mantido com adição de testes (clojure.test + Midje, fixtures de lifecycle) e pair programming
- **Formação Complementar:** FC 3.0 em linha única temática — Segurança, Mensageria, Arquitetura, DevOps

### Gaps honestos documentados
| Gap | Como apresentar |
|---|---|
| PostgreSQL sem produção pesada | "Conceitos ACID via Datomic. Drivers Go estou solidificando." |
| Kafka sem produção | "Mesmos padrões do NATS JetStream que uso em produção. API diferente, modelo mental o mesmo." |
| Kubernetes básico | "Uso Docker extensivamente. K8s estou no nível de operar, não de administrar." |
| GCP vs AWS | "Experiência em AWS, conceitos de cloud portáveis." |

---

## Plano de estudos (por prioridade)

### Bloco 1 — Identidade (fazer primeiro)
1. **Autenticação e Keycloak — FC 3.0** (0% → concluir)
   - OAuth 2.0, OpenID Connect, Keycloak, JWT, CSRF, Replay Attack
2. **JWT, ACL, RBAC — FC 4.0** (0% → quando liberado)

### Bloco 2 — Stack do isaac
3. **Kafka — FC 3.0** (36% → concluir + emitir certificado)
4. **Arquitetura Hexagonal — FC 3.0** (50% → concluir + emitir certificado)
5. **PostgreSQL + pgx em Go** — estudo prático
6. **Testes em Go** — testing, httptest, table-driven, mocks

### Bloco 3 — Complementar
7. **Kubernetes — FC 3.0** (7% → operacional básico)
8. **Terraform — FC 3.0** (0% → uma sessão)

### Certificados FC 3.0 a emitir antes da entrevista
- [ ] Kafka (terminar 36%)
- [ ] Arquitetura Hexagonal (terminar 50%)
- [x] EDA — Event Driven Architecture
- [x] Arquitetura baseada em Microsserviços
- [x] Fundamentos de Arquitetura de Software
- [x] Domain Driven Design
- [x] SOLID Express

---

## STAR Situations preparadas

Detalhes completos em `ENTREVISTA_ISAAC_PREP.md`. Resumo:

| # | Situação | Tema |
|---|---|---|
| S1 | Migração Pathom 2→3 em produção | Liderança técnica, disseminação |
| S2 | Risk Guard no Ark Streams | Segurança por design arquitetural |
| S3 | Suíte de testes do Octopus Pay | Qualidade, disciplina de testes |
| S4 | Framework Summon / ETL | Extensibilidade, produto escalável |
| S5 | Eliminação divergência backtest/produção | Consistência em sistemas distribuídos |

---

## Considerações sobre o processo

### Pontos fortes do perfil
- 7 anos em sistemas financeiros reais (domínio do isaac)
- Ark Streams como projeto em produção que o próprio autor usa — autenticidade rara
- Histório de consultoria com clientes reais e comunicação direta
- Clojure → Go: modelo mental funcional portável, não troca de tecnologia por modismo
- Testes como disciplina documentada em código real

### O que pode surgir na entrevista
- "Por que mudar de Clojure para Go?" → resposta preparada no STAR guide
- Perguntas de segurança/identidade (JWT, OAuth2, RBAC) → estudar Bloco 1
- Live coding em Go → praticar testes e error handling idiomático
- Pergunta sobre o Ark Streams → contar a história do produto, não listar features

### Contexto da empresa
- isaac é uma empresa do Grupo Arco Educação — Edtech + Fintech
- Time de Identidade é plataforma — outras squads dependem do que entregam
- Valorizam franqueza, transparência e equipe — cultura explicitada na JD

---

*Inscrito em 2026-06-03. Aguardando próximos passos.*
