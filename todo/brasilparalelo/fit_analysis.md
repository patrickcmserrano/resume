# Análise de Fit — Brasil Paralelo

**Data:** 2026-06-04

## Score de aderência

**Requisitos obrigatórios:** 4/4 ✅
**Diferenciais cobertos:** 6/8

### Pontos fortes

- 7 anos de Clojure/ClojureScript — stack primário da empresa
- Motor de pagamentos multi-adquirente (25+ integrações): prova de sistema crítico complexo
- PostgreSQL em uso (Ark Streams)
- Linux nativo
- Sistemas distribuídos: NATS JetStream, WebSocket, streaming de estado em tempo real
- Ciclo completo de desenvolvimento (planejamento → deploy → monitoramento)

### Lacunas honestas

| Gap | Impacto | Argumento de mitigação |
|-----|---------|----------------------|
| SmartTV (WebOS/Tizen) | Diferencial, não requisito | Curva de aprendizado curta dado background funcional/JS |
| MPEG-DASH, ffmpeg, DRM/HDCP | Diferencial, não requisito | Exp. em streaming de estado RT (NATS, WebSocket) + arquitetura 24/7 |

## Ajustes recomendados no CV

1. **Cabeçalho** — inverter para Clojure-first: `"Engenheiro de Software Sênior Fullstack (Clojure · ClojureScript · TypeScript)"`
2. **Resumo** — manter frase sobre "código discutido antes de entregue / testes como documentação executável"
3. **PostgreSQL explícito** — adicionar bullet no projeto Ark Streams mencionando PostgreSQL (hoje o CV puxa mais Datomic)

## Estratégia salarial (PJ)

- **Âncora recomendada:** R$ 24.000/mês
- **Piso mental:** R$ 20.000
- **Teto defensável:** R$ 28.000
- **Referência de mercado 2026:** sênior CLT ≥ R$ 13.000 → PJ típico 30–50% maior
- **Justificativa:** 7 anos, Clojure (nicho), motor de pagamentos crítico
