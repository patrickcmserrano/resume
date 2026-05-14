# Preparação Completa — Entrevista Buzzlabs

---

## PARTE 1: ESTRATÉGIA

### Objetivo da entrevista
Não é provar que você sabe Clojure. Eles já viram o currículo. O objetivo é fazer com que saiam pensando: *"esse cara pensa como a gente pensa, resolve o tipo de problema que a gente resolve, e vai comunicar bem com nossos clientes."*

### Sua vantagem real
Você tem algo raro: 7 anos de Clojure em produção **em consultoria**, não em empresa de produto. Isso significa:
- Você adaptou a mesma stack para domínios completamente diferentes
- Você aprendeu a defender decisões técnicas para clientes não-técnicos
- Você entregou sistemas completos (schema → UI) com autonomia

Esse perfil é exatamente o que uma consultoria Clojure precisa. Não minimize isso.

### Os três medos do entrevistador
Todo entrevistador está inconscientemente verificando:
1. **Vai entregar?** — histórico de projetos completos, métricas reais
2. **Vai se comunicar?** — clareza técnica, honestidade sobre gaps
3. **Vai se integrar?** — colaboração, autonomia calibrada, sem ego

Suas respostas devem, direta ou indiretamente, responder a esses três medos.

### Tom correto
- **Confiante, não arrogante.** Você tem 7 anos de experiência real. Fale como quem sabe o que faz.
- **Honesto sobre gaps, não defensivo.** Kafka, Erlang — você sabe o que não tem e por quê.
- **Curioso, não ansioso.** Faça perguntas genuínas. Mostre que está avaliando a Buzzlabs tanto quanto eles estão te avaliando.

---

## PARTE 2: NARRATIVA PESSOAL

### Resposta para "Me fale sobre você" (versão de 90 segundos)

> "Sou engenheiro Clojure/ClojureScript fullstack há 7 anos. Trabalhei em consultoria durante todo esse período — o que na prática significa que cada projeto foi um domínio diferente: gateway de pagamentos, marketplace B2B, plataforma imobiliária, motor multi-adquirente com 25 integrações. Em todos entregava as duas pontas: do modelo Datomic ao componente Fulcro na tela.
>
> Nos últimos dois anos construí o Ark Engine — primeiro uma versão em Clojure com XTDB e Polylith, depois uma reescrita em Go por custo de cloud. Esse projeto me deu benchmarks reais de latência, experiência com race conditions em sistemas concorrentes e uma visão muito clara de onde o modelo mental funcional faz diferença independente da linguagem.
>
> Agora quero voltar para consultoria. Projeto solo resolve autonomia mas não resolve colaboração, e é em ambiente de equipe que eu produzo melhor. A Buzzlabs tem a stack que quero continuar desenvolvendo e o modelo de trabalho que conheço."

**Por que essa resposta funciona:**
- Abre com o que importa para eles (Clojure, fullstack, consultoria)
- Dá contexto sem listar o currículo
- Antecipa a pergunta sobre Go/Clojure sem parecer defensivo
- Termina com motivação genuína, não com "estou em busca de novos desafios"

---

## PARTE 3: PERGUNTAS TÉCNICAS — RESPOSTAS EM CAMADAS

*Cada resposta tem uma versão curta (use se a pergunta for casual) e uma versão profunda (use se aprofundarem).*

---

### CLOJURE / ECOSSISTEMA

---

**"Qual sua experiência com Clojure?"**

*Curta:* "7 anos em produção, todos em consultoria. Pathom 3, Datomic, Clara Rules, Fulcro RAD no backend e frontend."

*Profunda:* "O que mais me marca nesses 7 anos não é uma biblioteca específica mas um padrão que se repetiu em projetos diferentes: sistemas Clojure que duram — que são legíveis e modificáveis por quem não os escreveu — tendem a ter dados como centro, não objetos ou procedimentos. Isso se manifesta em Pathom (resolvers declarativos em vez de chamadas acopladas), Datomic (schema como dado, queries como dado), Clara Rules (regras como dado). Quando cheguei no Ark Engine e precisei resolver race conditions em Go, o que funcionou foi aplicar o mesmo princípio: dados imutáveis em vez de estado compartilhado."

---

**"O que é Pathom 3 e como você o usou?"**

*Curta:* "Motor de resolução de grafos de dados. Você declara resolvers — 'dado X produzo Y' — e o Pathom compõe o caminho automaticamente. Usei para integrar 25+ gateways de pagamento sem acoplar o core de negócio às APIs de cada gateway."

*Profunda:* "O insight central do Pathom é que sistemas complexos frequentemente falham não por bugs mas por acoplamento: para obter um dado, você precisa saber de onde ele vem. Pathom inverte isso. O cliente (seja uma UI em Fulcro ou um processo interno) pede atributos via EQL sem saber de onde vêm. O motor descobre o caminho.

No Octopus Pay isso foi crucial: um pagamento Cielo e um pagamento Adyen têm respostas completamente diferentes. Com Pathom, ambos resolvem para os mesmos atributos canônicos (`:payment/status`, `:payment/transaction-id`). O código de negócio nunca toca especificidades de gateway. Para adicionar um novo gateway, você escreve os resolvers de normalização — nada mais muda.

A migração Pathom 2→3 foi significativa porque o 3 executa resolvers em paralelo por padrão e introduziu o Pathom Index, que permite introspectar o grafo completo — útil para debugging e para gerar documentação automática das capacidades do sistema."

---

**"O que é Datomic e quando você escolheria sobre PostgreSQL?"**

*Curta:* "Base de dados Datalog imutável. O histórico é o dado — você não atualiza, você acrescenta fatos. Escolho quando auditabilidade e evolução de schema são requisitos do negócio."

*Profunda:* "Datomic resolve um problema que a maioria dos sistemas financeiros tem mas trata com gambiarra: 'mostre-me o estado do sistema em um ponto específico do passado.' Em PostgreSQL você precisaria de tabelas de auditoria, triggers, ou event sourcing manual. Em Datomic isso é uma query: `(d/as-of db timestamp)`.

No Octopus Pay, regulação de pagamentos exige rastreabilidade total: quem autorizou, quando, com qual estado do sistema. Com Datomic isso vem de graça. Com PostgreSQL teríamos construído um sistema de auditoria paralelo que inevitavelmente divergiria.

O trade-off real: Datomic tem único writer por banco — não escala escrita horizontalmente. Para sistemas com volume muito alto de escrita concorrente, PostgreSQL ou Cassandra são mais adequados. Datomic brilha quando você tem muito mais leitura que escrita e quando o modelo de dados é complexo e evolutivo."

---

**"O que é Clara Rules? Dê um exemplo concreto."**

*Curta:* "Motor de regras Rete para Clojure. Forward-chaining: você define fatos e regras, o motor infere consequências. Usei para lógica financeira que muda com frequência e precisa ser auditável."

*Profunda:* "O problema que Clara resolve é o 'if-else que virou árvore': lógica financeira que começa simples e vira uma cadeia de condicionais espalhada pelo código, impossível de testar em isolamento e de explicar para o cliente.

Exemplo do Zougue MPMS: cálculo de faturamento de um pedido marketplace depende de tipo de seller, categoria do produto, regime tributário, se é frete próprio ou terceirizado, se tem desconto negociado. Isso vira 40 casos de if-else ou vira regras Clara declarativas:

```clojure
(defrule calcular-comissao-seller-premium
  [Pedido (= ?total total) (= :premium tipo-seller)]
  [ConfigComissao (= :premium tier) (= ?taxa taxa)]
  =>
  (insert! (->Comissao (* ?total ?taxa))))
```

Cada regra é uma unidade testável. O cliente pode ler (com tradução mínima) e validar se a regra está correta. Adicionar um novo caso é adicionar uma nova regra — sem tocar nas existentes. E o motor Rete garante eficiência mesmo com centenas de regras, porque só reavalia o que mudou."

---

**"O que é Fulcro RAD?"**

*Curta:* "Rapid Application Development sobre Fulcro. Você descreve atributos do domínio uma vez e o RAD gera forms, reports e routing automaticamente. Poderoso quando o backend já é Datomic."

*Profunda:* "Fulcro RAD parte de uma observação: boa parte do trabalho em aplicações administrativas é repetitiva — forms de edição, listagens com filtros, paginação, validação. RAD gera isso a partir de atributos declarados.

No Octopus Pay, declarávamos algo como:

```clojure
(defattr payment-id :payment/id :uuid
  {::attr/identity? true
   ::attr/label "ID do Pagamento"})

(defattr payment-status :payment/status :string
  {::attr/label "Status"
   ::attr/enumerated-values #{:pending :approved :rejected}})
```

E o RAD gerava report com filtro por status, form de detalhes com validação, routing entre páginas. Sem escrever UI. Para um dashboard administrativo de backoffice, isso significa semanas de desenvolvimento viram dias.

O que torna isso especialmente poderoso no ecossistema Clojure é que o schema Datomic e o schema RAD podem ser o mesmo — você não mantém dois modelos de dados."

---

**"Explique o race condition que você resolveu no Ark Engine."**

*Curta:* "Estado compartilhado entre FractalEngine e FSM causava leituras rasgadas. Resolvi com event chaining: FractalEngine produz snapshot imutável (AnalyzedEvent) que o FSM consome — sem acesso a estado externo."

*Profunda:* "O sistema original tinha uma topologia fan-out: um candle chegava, o FractalEngine calculava os indicadores (Alligator, AO, AC, MFI) e atualizava campos em memória, e publicava um evento para o FSM consumir. O FSM então lia os indicadores direto do FractalEngine.

O problema: entre o FractalEngine publicar o evento e o FSM ler os indicadores, um segundo candle podia chegar. O FractalEngine sobrescrevia os indicadores. O FSM tomava decisão com os indicadores do candle 2, mas acreditando que eram do candle 1. Torn read.

O redesign: FractalEngine não expõe estado. Quando termina de processar um candle, encapsula todos os valores calculados em um `AnalyzedEvent` struct imutável e o publica via NATS. O FSM só recebe esse struct — não tem referência ao FractalEngine, não pode ler estado externo.

```
candle 1 → FractalEngine → AnalyzedEvent{jaw:X, ao:Y, ...} → NATS → FSM
candle 2 → FractalEngine → AnalyzedEvent{jaw:X', ao:Y', ...} → NATS → FSM
```

Cada decisão do FSM é determinística dado o AnalyzedEvent que recebeu. Sem estado compartilhado, race condition é estruturalmente impossível.

O benefício colateral foi o backtesting: replay de AnalyzedEvents históricos produz exatamente as mesmas decisões que produção. Determinismo garantido."

---

**"O que é bitemporalidade e como o XTDB a implementa?"**

*Curta:* "Dois eixos de tempo: quando o fato foi verdadeiro no mundo (Valid Time) e quando o sistema registrou (Transaction Time). XTDB os trata como dimensões independentes da query."

*Profunda:* "O problema que bitemporalidade resolve é sutil mas crítico em sistemas financeiros: *o que o sistema sabia, quando*.

Imagine: às 14h30, um trader recebe um sinal e executa uma ordem. Às 16h00, você descobre que o dado de mercado que chegou às 14h20 estava errado — foi corrigido pela exchange às 15h50. Em um banco de dados convencional, a correção sobrescreve o dado original. Você não consegue mais reconstruir o que o sistema sabia às 14h30.

Com XTDB:
- **Valid Time**: quando o fato foi verdadeiro no domínio (o preço às 14h20)
- **Transaction Time**: quando o sistema registrou esse fato (14h20 para o dado original, 15h50 para a correção)

Você pode consultar: "dê-me os dados com Valid Time 14h20 como o sistema os conhecia em Transaction Time 14h29." Você reconstrói exatamente o estado de conhecimento do sistema no momento da decisão. Isso é o que torna backtesting verdadeiramente livre de lookahead bias — estruturalmente, não por disciplina de código."

---

**"O que é Polylith?"**

*Curta:* "Arquitetura de monorepo onde cada componente é uma caixa-preta com interface explícita. Elimina acoplamento implícito entre partes do sistema."

*Profunda:* "Polylith parte de uma crítica ao monólito tradicional: o problema não é que o código está junto, é que as dependências são implícitas. Em um monólito convencional, qualquer módulo pode chamar qualquer outro — o acoplamento cresce invisível até que mudar uma coisa quebra outra inesperada.

No Ark Engine Clojure, a divisão era:
- **Gravity** (infraestrutura): conectores de exchange, Redis Streams, XTDB — tudo que depende do mundo externo
- **Laws** (risco): Risk Guard, limites constitucionais — isolado porque nada deve bypassar risco
- **Strategy** (lógica): sinais, decisões — puro, sem dependências de infra

O Risk Guard como componente isolado foi a decisão mais importante: a estratégia literalmente não consegue executar uma ordem sem passar pelo Risk Guard. Isso não é uma convenção de código — é a estrutura do sistema. Um bug na estratégia não pode causar liquidação forçada porque ela não tem acesso ao executor."

---

### KAFKA / MENSAGERIA

---

**"Você não tem Kafka em produção. Isso é um problema?"**

*Resposta:*
"É uma lacuna operacional, não conceitual. Os padrões que Kafka implementa — particionamento, consumer groups com offset, exactly-once semântico, backpressure, dead letter queue — eu implementei com Redis Streams no Ark Engine Clojure e com NATS JetStream no Ark Streams.

A curva de aprendizado de Kafka está em operações de cluster: configuração de brokers, replicação, tuning de performance, monitoramento de lag. Não está nos padrões de streaming distribuído — esses eu conheço na prática.

Tenho interesse direto em fechar essa lacuna. É uma das razões pelas quais consultoria faz sentido agora: projetos variados aumentam a chance de trabalhar com Kafka em contexto real, que é a única forma de consolidar conhecimento operacional."

---

**"Qual a diferença entre Kafka, NATS JetStream e Redis Streams?"**

| | Kafka | NATS JetStream | Redis Streams |
|---|---|---|---|
| **Durabilidade** | Alta (replicação multi-broker) | Média (JetStream persiste) | Média (AOF/RDB) |
| **Latência** | ~ms | sub-ms | sub-ms |
| **Operação** | Cluster complexo | Processo único | Processo único |
| **Throughput** | Altíssimo (TB/dia) | Alto | Alto |
| **Consumer Groups** | Sim | Sim | Sim |
| **Exactly-once** | Sim (transacional) | Sim | Semântico |
| **Ecossistema** | Rico (Connect, Streams) | Crescendo | Limitado |

"Para 95% dos casos de uso de streaming distribuído, os três entregam. Kafka é a escolha quando o volume é muito alto, quando você precisa do ecossistema (Kafka Connect para integrações, Kafka Streams para processamento), ou quando o time já opera. NATS e Redis são escolhas pragmáticas quando você quer os padrões sem o overhead operacional."

---

### ARK ENGINE — TÉCNICO

---

**"Como você mediu a latência de 43 µs?"**

"Benchmarks Go com `testing.B`. A metodologia foi:
1. Warmup de 100 candles para trazer os indicadores a steady state (sem contar custo de inicialização)
2. `b.ResetTimer()` após o warmup
3. `b.ReportAllocs()` para capturar alocações junto com latência
4. `log.SetOutput(io.Discard)` para eliminar I/O de logs do hot path — sem isso, a primeira medição deu 387ms/op (o log dominava)
5. Medições separadas: FractalEngine isolado (~35 µs), FSM isolado (~1 µs), pipeline completo end-to-end (~43 µs)

O gap entre 35+1 e 43 µs é serialização JSON do AnalyzedEvent + latência do mock NATS. Em produção com NATS real em localhost, essa parte seria um pouco maior."

---

**"Por que Go e não Clojure para a reescrita?"**

"A versão Clojure foi construída com XTDB — que tem custo de cloud relevante para produção. NATS JetStream é praticamente gratuito. A decisão foi operacional, não técnica.

Se eu fosse construir para um contexto com infraestrutura já disponível (como uma consultoria com cluster gerenciado), a versão Clojure com XTDB teria vantagens claras: bitemporalidade nativa, modelo de dados mais rico, ecossistema mais adequado para análise de séries temporais financeiras.

Para um projeto independente sem receita ainda, Go + NATS foi a escolha pragmática que permitiu o projeto existir."

---

## PARTE 4: PERGUNTAS COMPORTAMENTAIS (FORMATO STAR)

*Situação → Tarefa → Ação → Resultado*

---

**"Me conte sobre um problema técnico difícil que você resolveu."**

> **S:** No Octopus Pay, a migração Pathom 2→3 tinha um prazo — a versão 2 estava sendo descontinuada e algumas funcionalidades novas que precisávamos só existiam no 3.
>
> **T:** Migrar sem downtime em um sistema de pagamentos em produção, com 25+ integrações ativas dependendo dos resolvers existentes.
>
> **A:** Primeiro mapeei o grafo completo de dependências entre resolvers — o Pathom Index do v3 ajudou nisso. Identifiquei os resolvers de alta criticidade (gateway calls) e os de baixo risco (atributos calculados locais). Migrei em camadas: primeiro os atributos folha sem dependências, depois os intermediários, por último os de entrada que tocavam as integrações externas. Cada camada tinha testes de regressão antes de ir para produção.
>
> **R:** Migração sem incidente. O benefício colateral foi que o Pathom 3 executava resolvers em paralelo por padrão — queries que demoravam por resolução serial ficaram significativamente mais rápidas.

---

**"Me conte sobre uma situação em que você discordou de uma decisão técnica."**

> **S:** Em um projeto, o cliente queria persistir snapshots de estado em PostgreSQL em vez de Datomic para "simplificar".
>
> **T:** O domínio era auditoria financeira — rastreabilidade era requisito regulatório.
>
> **A:** Em vez de argumentar em termos de preferência técnica, traduzi para o risco do negócio: "com PostgreSQL, quando o auditor perguntar qual era o estado do sistema quando essa transação foi aprovada, qual é a resposta?" Mostrei o custo de construir auditoria ad hoc em PostgreSQL versus o que Datomic entrega nativamente. Propus um spike de 2 dias para demonstrar.
>
> **R:** O cliente aprovou Datomic após o spike. A chave foi transformar a discussão de "qual tecnologia você prefere" para "qual risco você quer assumir."

---

**"Como você lida com um cliente que quer algo tecnicamente errado?"**

> "Primeiro, entendo o que está por trás do pedido. Clientes raramente pedem soluções técnicas — pedem resultados de negócio com uma solução técnica acoplada. Quando separo as duas coisas, geralmente consigo propor algo que atende o resultado sem o problema técnico. Se após a explicação o cliente insiste, documento o risco, implemento com o mínimo de dano possível e mantenho a conversa aberta."

---

**"Me conte sobre uma entrega que não correu como planejado."**

> **S:** No Zougue MPMS, a integração com VTEX para simulação de carrinho tinha um comportamento não documentado — a API retornava 200 com corpo de erro em alguns cenários de estoque.
>
> **T:** O sistema estava marcando pedidos como aprovados quando deveriam estar em erro.
>
> **A:** Adicionei logging detalhado dos corpos de resposta VTEX, identifiquei os 3 cenários não documentados, escrevi um adapter que normalizava esses casos para o modelo canônico de erro do sistema, e adicionei testes com os payloads reais capturados.
>
> **R:** Zero regressões após o fix. O aprendizado foi validar APIs de terceiros com payloads reais em staging antes de ir para produção — especialmente com VTEX, que tem comportamentos não documentados frequentes.

---

## PARTE 5: PERGUNTAS DIFÍCEIS — SEM RODEIOS

---

**"O Ark Engine lucra?"**

"Não ainda. A infraestrutura é sólida e os benchmarks são reais. O que falta é edge de estratégia — indicadores de preço sozinhos não têm expectativa positiva consistente em mercados eficientes, porque todo participante os vê. Os próximos passos são dados de microestrutura: funding rate arbitrage (delta-neutral, sem exposição direcional), liquidation-driven entries. Mas isso está fora do escopo da vaga. O que é relevante para a Buzzlabs é a infraestrutura que construí — event-driven, imutável, testada."

---

**"Por que você saiu da consultoria em 2025?"**

"Para ter tempo integral para o Ark Engine. A versão Clojure com XTDB exigia um nível de foco que não era compatível com projetos de consultoria. Agora que o sistema está estável e documentado, retorno à consultoria — que é o ambiente onde produzo melhor."

---

**"Você consegue trabalhar com outros desenvolvedores depois de dois anos solo?"**

"Consultoria de 2018 a 2025 foi trabalho em equipe por definição — cada cliente tinha um time. O período solo foi intencional e delimitado. Prefiro código revisado: encontra o que você não vê quando está próximo demais do problema."

---

**"O que você não sabe que gostaria de aprender na Buzzlabs?"**

"Kafka em produção com volume real. Experiência com times maiores de Clojure — toda minha experiência foi em squads pequenos. E qualquer domínio que a Buzzlabs atenda que eu não tenha trabalhado — cada domínio novo em consultoria Clojure é uma oportunidade de ver onde o ecossistema brilha de formas inesperadas."

---

## PARTE 6: PERGUNTAS PARA FAZER AO ENTREVISTADOR

*Essas perguntas mostram que você pesquisou, que pensa em nível de sistema e que está avaliando a Buzzlabs tanto quanto eles te avaliam. Escolha 3-4 dependendo do fluxo da conversa.*

**Sobre o trabalho:**
- "Qual é o projeto atual mais técnicamente desafiador que a equipe está trabalhando?"
- "Como é a divisão entre backend Clojure e frontend ClojureScript nos projetos recentes?"
- "Quando um cliente chega com um problema, como a equipe decide a stack? Há casos em que vocês recomendam não usar Clojure?"
- "Qual é o ciclo típico de um projeto — desde a proposta até a entrega?"

**Sobre a equipe:**
- "Como é estruturado o onboarding de um novo engenheiro num projeto em andamento?"
- "Como a equipe lida com revisão de código? Existe processo de PR ou é mais informal?"
- "Qual foi a última decisão técnica importante que a equipe debateu? Como chegaram ao consenso?"

**Sobre crescimento:**
- "Existe espaço para contribuir com open source no ecossistema Clojure dentro dos projetos?"
- "Como vocês lidam com o Kafka gap de alguém que vem de NATS/Redis Streams?"

**Sobre a Buzzlabs em si:**
- "O que diferencia a Buzzlabs de outras consultorias Clojure do mercado?"
- "Qual foi o maior projeto que a equipe entregou nos últimos dois anos?"

---

## PARTE 7: COMPARAÇÕES TÉCNICAS PARA REFERÊNCIA RÁPIDA

### Datomic vs XTDB
| | Datomic | XTDB |
|---|---|---|
| **Modelo** | Datalog, imutável | Datalog, bitemporal |
| **Tempo** | Transaction Time | Valid Time + Transaction Time |
| **Backend** | Próprio (DynamoDB, SQL) | RocksDB, JDBC, outros |
| **Licença** | Comercial (gratuito pequeno porte) | Open source |
| **Maturidade** | Alta (Cognitect/Nubank) | Média (JUXT) |
| **Quando usar** | Auditoria, queries Datalog ricas | Lookahead bias crítico, bitemporalidade real |

### NATS JetStream vs Redis Streams vs Kafka
| | NATS JetStream | Redis Streams | Kafka |
|---|---|---|---|
| **Operação** | Processo único | Processo único | Cluster |
| **Durabilidade** | Persistência em disco | AOF configurável | Replicação multi-broker |
| **Throughput** | Alto | Alto | Altíssimo |
| **Ecossistema** | Crescendo | Limitado | Rico |
| **Custo de infra** | Mínimo | Mínimo | Significativo |
| **Quando usar** | Microserviços, IoT, baixa latência | Cache + streaming | Volume alto, ecossistema necessário |

### Fulcro vs React/SPA tradicional
| | Fulcro | React + Redux/Zustand |
|---|---|---|
| **Estado** | Mapa normalizado Clojure | Atoms/stores JS |
| **Fetching** | EQL declarativo (Pathom) | Imperativo (useEffect, RTK Query) |
| **Linguagem** | ClojureScript (mesma do backend) | JavaScript/TypeScript |
| **Debug** | Portal, REPL | DevTools |
| **Curva** | Alta | Moderada |
| **Vantagem** | Stack unificada, sem impedância front/back | Ecossistema enorme |

---

## PARTE 8: CONCEITOS PARA REVISAR (SE TIVER TEMPO)

Se a entrevista for técnica com código, esses temas têm alta probabilidade:

1. **Escrever um resolver Pathom simples** — saber a sintaxe de `defresolver` e `pc/defresolver`
2. **Query Datalog básica** — `[:find ?e :where [?e :user/email "x@y.com"]]`
3. **Atom + swap! em Clojure** — gestão de estado imutável
4. **core.async básico** — `chan`, `go`, `>!`, `<!`
5. **Diferença entre `map`, `reduce`, `transduce`** — e quando usar cada
6. **O que é uma transducer** — composição de transformações sem coleção intermediária
7. **Como Clojure lida com nil** — `nil` é falsy, `nil-safe` com `some->`, `when-let`

---

## PARTE 9: ARMADILHAS — O QUE NÃO FAZER

- **Não fale mal do cliente anterior** (mesmo sem nomear a empresa). Fale em aprendizados.
- **Não minimize o Go**. O Ark Streams é bom trabalho de engenharia. Não se desculpe por ele.
- **Não exagere no Kafka**. "Conheço os padrões" é honesto e forte. "Já trabalhei com Kafka" seria mentira.
- **Não fale que precisa muito do emprego**. Mesmo que seja verdade. Desespero reduz poder de negociação e gera dúvida sobre julgamento.
- **Não responda "não sei" sem continuar**. "Não trabalhei com isso especificamente, mas o padrão que conheço é X, imagino que Y seria a diferença" demonstra pensamento, não lacuna.
- **Não deixe silêncios longos sem preencher**. Se precisar pensar, diga "deixa eu pensar um segundo."
- **Não pergunte sobre salário na primeira entrevista**. Deixe eles trazerem o assunto.

---

## PARTE 10: ABERTURA E FECHAMENTO

### Abertura (primeiros 2 minutos)
- Aperto de mão firme, contato visual
- "Obrigado pela oportunidade" — diga uma vez, não repita
- Se perguntarem "como você está" — "bem, animado para a conversa" — não entre em detalhes pessoais

### Fechamento (últimos 5 minutos)
Quando perguntarem "tem mais alguma pergunta?" — **sempre tenha**. Use uma das perguntas da Parte 6.

Antes de encerrar, faça uma declaração de interesse explícita:
> "Saio dessa conversa com mais interesse do que entrei. A stack, o modelo de consultoria e o tipo de problema que vocês resolvem são exatamente o ambiente em que quero trabalhar. Qual é o próximo passo do processo?"

Perguntar sobre o próximo passo é assertivo — não é despero, é profissionalismo.

### Follow-up (24h após)
Envie um e-mail curto para quem te entrevistou:

> **Assunto:** Obrigado — Entrevista [data]
>
> Obrigado pela conversa de ontem. A discussão sobre [mencionar algo específico que foi dito] confirmou meu interesse na vaga.
> Fico à disposição para qualquer informação adicional.
>
> Patrick

Referência a algo específico da conversa prova que você estava presente — não é e-mail genérico.

---

## PARTE 11: NEGOCIAÇÃO

- **Não dê o primeiro número se puder evitar.** "Qual é o range da vaga?" é uma resposta válida.
- **Se precisar dar um número**, dê acima do que você aceitaria. É mais fácil ceder do que subir.
- **Não negocie contra você mesmo.** Se eles demorarem para responder, não reduza sua proposta para "facilitar". Silêncio não é negativa.
- **O que negociar além de salário**: modalidade de contrato (PJ vs CLT), horário flexível, primeiro projeto — pergunte sobre o que está em andamento.
- **Se a oferta vier abaixo do esperado**: "Fico feliz com o interesse. O que me faria aceitar sem hesitar seria X — tem espaço para isso?" Uma pergunta, não uma exigência.

---

## RESUMO EXECUTIVO

Você tem um perfil forte para essa vaga. Os pontos que vão decidir:

1. **Demonstrar que pensa em Clojure**, não que sabe Clojure — a diferença é falar sobre imutabilidade, composição e dados como princípios, não como bibliotecas.
2. **Transformar o Kafka gap em honestidade qualificada** — você conhece os padrões, falta experiência operacional, tem interesse real.
3. **Contar a história do Ark Engine corretamente** — Clojure primeiro, Go por custo, mesmos princípios.
4. **Mostrar que você entrega** — cada projeto tem resultado concreto, não apenas tecnologias listadas.
5. **Fazer boas perguntas** — quem faz perguntas inteligentes sobre o trabalho parece mais competente do que quem só responde bem.
