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
- **Honesto sobre gaps, não defensivo.** Kafka — você sabe o que não tem e por quê.
- **Curioso, não ansioso.** Faça perguntas genuínas. Mostre que está avaliando a Buzzlabs tanto quanto eles estão te avaliando.

---

## PARTE 2: O QUE O HUMANO QUE LER SEU CURRÍCULO VAI PENSAR

Antes de qualquer entrevista, alguém vai ler duas páginas sobre você e formar uma impressão. Essa impressão chega na sala antes de você. Conheça ela.

---

**Ao ver "Projeto Independente" no topo (2025-Atual):**
*"Está desempregado. Por quanto tempo? Está desesperado?"*

→ A carta de apresentação já endereça isso. Na entrevista, mencione o Ark Engine como trabalho deliberado e delimitado — não como "o que fiz enquanto procurava emprego". A linguagem importa: "dediquei tempo integral para construir X" é diferente de "fiquei sem emprego e resolvi fazer um projeto".

---

**Sobre a Indicação (Leandro):**
*Isso é um trunfo forte de credibilidade.*
→ Na primeira oportunidade natural, mencione: "Acompanho o trabalho da Buzzlabs há um tempo e o Leandro me recomendou fortemente a cultura da empresa. Quando vi o alinhamento da stack, fez todo sentido me candidatar." Isso estabelece "social proof" imediata.

---

**Ao ver XTDB:**
*"Nunca ouvi falar. É confiável? É relevante?"*

→ Esteja pronto para explicar em 30 segundos: "É o Datomic com bitemporalidade nativa — mesmo modelo Datalog, criado pela JUXT, open source. A Nubank usa Datomic; XTDB resolve o mesmo problema com uma dimensão a mais de tempo." Contextualizar com Datomic e Nubank torna o desconhecido familiar.

---

**Ao ver "Consultoria em Software" sem nome de empresa:**
*"Por que está escondendo? Teve problema lá?"*

→ Se perguntarem diretamente: "Prefiro não divulgar o nome do cliente por razões de confidencialidade do projeto — é o padrão em consultoria." Simples, profissional, sem elaboração.

---

**Ao ver Go no currículo de um candidato Clojure:**
*"Ele é realmente especialista em Clojure ou está se vendendo como tal?"*

→ O currículo já está estruturado para responder isso: Ark Engine abre com XTDB/Polylith/Redis Streams antes de mencionar Go. Na entrevista, posicione a versão em Go como um **benchmark deliberado**. "Quis validar até onde o modelo mental funcional de imutabilidade e snapshots (que Clojure facilita) poderia ser levado em termos de latência bruta (~43µs) e economia de infraestrutura. A conclusão foi que os princípios funcionais são a chave da estabilidade, independente da linguagem, mas que Clojure é a ferramenta ideal para a complexidade do negócio."

---

**Ao ver Octopus Pay (2022-2025) com 7 bullets densos:**
*"Isso é impressionante — mas fez tudo isso sozinho?"*

→ Você confirmou que sim — todas as integrações, você mesmo. Esteja preparado para detalhar qualquer bullet com um exemplo específico. O mais provável de ser explorado: Pathom 3, Clara Rules e Fulcro RAD.

---

**Ao ver "Bacharelado em Física" sem conclusão:**
*"Largou a faculdade?"*

→ Se perguntarem: "Migrei para Engenharia de Software em 2024, que é mais alinhado com o que pratico." Não é abandono — é correção de rota. A Física dá credencial implícita de raciocínio matemático que vale manter na conversa.

---

**Ao ver Polylith nas habilidades:**
*"Poucos engenheiros usam Polylith. Esse cara pensa em arquitetura de verdade."*

→ Esse é um diferencial positivo para a Buzzlabs, que provalmente conhece Polylith. Não subestime — mencione com naturalidade.

---

## PARTE 3: NARRATIVA PESSOAL

### Resposta para "Me fale sobre você" (versão de 90 segundos)

> "Sou engenheiro Clojure/ClojureScript fullstack há 7 anos, todos em consultoria. Cada projeto foi um domínio diferente — gateway de pagamentos, marketplace B2B, plataforma imobiliária, motor multi-adquirente com 25+ integrações — e em todos entregava as duas pontas: do schema Datomic ao componente Fulcro na tela.
>
> De julho de 2025 até agora trabalhei de forma independente no Ark Engine — uma infraestrutura de trading algorítmico. Comecei com Clojure, XTDB para persistência bitemporal e Polylith como arquitetura. Depois migrei para Go por custo operacional de cloud, preservando os mesmos princípios: snapshots imutáveis, pipeline event-driven, FSM determinístico. Esse projeto me deu benchmarks reais de latência e uma visão muito clara de onde o modelo mental funcional faz diferença independente da linguagem.
>
> Agora quero voltar para consultoria. Projeto solo resolve autonomia mas não resolve colaboração, e é em equipe que eu produzo melhor. A Buzzlabs tem a stack que quero continuar desenvolvendo e o modelo de trabalho que conheço."

**Por que essa resposta funciona:**
- Abre com o que importa para eles (Clojure, fullstack, consultoria)
- Dá contexto sem listar o currículo
- Menciona o período independente com naturalidade, não com desculpa
- Antecipa a pergunta sobre Go/Clojure sem parecer defensivo
- Termina com motivação genuína

---

## PARTE 4: PERGUNTAS TÉCNICAS — RESPOSTAS EM CAMADAS

*Cada resposta tem uma versão curta (use se a pergunta for casual) e uma versão profunda (use se aprofundarem).*

---

### CLOJURE / ECOSSISTEMA

**"Qual sua experiência com Clojure?"**

*Curta:* "7 anos em produção, todos em consultoria. Pathom 3, Datomic, Clara Rules, Fulcro RAD no backend e frontend."

*Profunda:* "O que mais me marca nesses 7 anos não é uma biblioteca específica mas um padrão que se repetiu: sistemas Clojure que duram — que são legíveis e modificáveis por quem não os escreveu — tendem a ter dados como centro, não objetos ou procedimentos. Isso se manifesta em Pathom (resolvers declarativos em vez de chamadas acopladas), Datomic (schema como dado, queries como dado), Clara Rules (regras como dado). Quando precisei resolver race conditions no Ark Engine em Go, o que funcionou foi aplicar o mesmo princípio: dados imutáveis em vez de estado compartilhado. A linguagem mudou; o modelo mental não."

---

**"O que é Pathom 3 e como você o usou?"**

*Curta:* "Motor de resolução de grafos de dados. Você declara resolvers — 'dado X produzo Y' — e o Pathom compõe o caminho automaticamente. Usei para integrar 25+ gateways de pagamento sem acoplar o core de negócio às APIs de cada gateway."

*Profunda:* "O insight central do Pathom é que sistemas complexos frequentemente falham não por bugs mas por acoplamento: para obter um dado, você precisa saber de onde ele vem. Pathom inverte isso. O cliente pede atributos via EQL sem saber de onde vêm — o motor descobre o caminho.

No Octopus Pay: um pagamento Cielo e um pagamento Adyen têm respostas completamente diferentes. Com Pathom, ambos resolvem para os mesmos atributos canônicos (`:payment/status`, `:payment/transaction-id`). O código de negócio nunca toca especificidades de gateway. Adicionar um novo gateway é escrever os resolvers de normalização — nada mais muda.

A migração Pathom 2→3 foi significativa: o v3 executa resolvers em paralelo por padrão e introduziu o Pathom Index para introspectar o grafo completo. Queries que demoravam por resolução serial ficaram visivelmente mais rápidas após a migração."

---

**"O que é Datomic e quando você escolheria sobre PostgreSQL?"**

*Curta:* "Base de dados Datalog imutável. O histórico é o dado — você não atualiza, você acrescenta fatos. Escolho quando auditabilidade e evolução de schema são requisitos do negócio."

*Profunda:* "Datomic resolve um problema que a maioria dos sistemas financeiros tem mas trata com gambiarra: 'mostre-me o estado do sistema em um ponto específico do passado.' Em PostgreSQL você precisaria de tabelas de auditoria, triggers, ou event sourcing manual. Em Datomic isso é uma query: `(d/as-of db timestamp)`.

No Octopus Pay, regulação de pagamentos exige rastreabilidade total. Com Datomic isso vem de graça. Com PostgreSQL teríamos construído um sistema de auditoria paralelo que inevitavelmente divergiria.

O trade-off real: Datomic tem único writer por banco — não escala escrita horizontalmente. Para volume muito alto de escrita concorrente, PostgreSQL é mais adequado. Datomic brilha quando você tem muito mais leitura que escrita e quando o modelo de dados é complexo e evolutivo."

---

**"O que é Clara Rules? Dê um exemplo concreto."**

*Curta:* "Motor de regras Rete para Clojure. Forward-chaining: você define fatos e regras, o motor infere consequências. Usei para lógica financeira que muda com frequência e precisa ser auditável."

*Profunda:* "O problema que Clara resolve é o 'if-else que virou árvore': lógica financeira que começa simples e vira uma cadeia de condicionais impossível de testar em isolamento e de explicar para o cliente.

Exemplo do Zougue MPMS: cálculo de comissão de um pedido marketplace depende de tipo de seller, categoria do produto, regime tributário, frete. Isso vira dezenas de condicionais ou vira regras Clara declarativas:

```clojure
(defrule calcular-comissao-seller-premium
  [Pedido (= ?total total) (= :premium tipo-seller)]
  [ConfigComissao (= :premium tier) (= ?taxa taxa)]
  =>
  (insert! (->Comissao (* ?total ?taxa))))
```

Cada regra é uma unidade testável. O cliente pode ler e validar se a regra está correta. Adicionar um novo caso é adicionar uma nova regra — sem tocar nas existentes. O motor Rete reavalia só o que mudou, então performance não degrada com centenas de regras."

---

**"O que é Fulcro RAD?"**

*Curta:* "Rapid Application Development sobre Fulcro. Você descreve atributos do domínio uma vez e o RAD gera forms, reports e routing automaticamente. Poderoso quando o backend já é Datomic."

*Profunda:* "Fulcro RAD parte de uma observação: boa parte do trabalho em aplicações administrativas é repetitiva — forms, listagens com filtros, paginação, validação. RAD gera isso a partir de atributos declarados.

No Octopus Pay:
```clojure
(defattr payment-status :payment/status :string
  {::attr/label "Status"
   ::attr/enumerated-values #{:pending :approved :rejected}})
```
E o RAD gerava report com filtro por status, form com validação, routing entre páginas — sem escrever UI. O que torna isso especialmente poderoso no ecossistema Clojure é que o schema Datomic e o schema RAD podem ser o mesmo. Você não mantém dois modelos de dados."

---

**"O que é Polylith?"**

*Curta:* "Arquitetura de monorepo onde cada componente é uma caixa-preta com interface explícita. Elimina acoplamento implícito entre partes do sistema."

*Profunda:* "O problema do monólito não é que o código está junto — é que as dependências são implícitas. Qualquer módulo pode chamar qualquer outro e o acoplamento cresce invisível.

No Ark Engine Clojure a divisão era:
- **Gravity** (infraestrutura): conectores de exchange, Redis Streams, XTDB
- **Laws** (risco): Risk Guard, limites constitucionais
- **Strategy** (lógica): sinais, decisões — puro, sem dependências de infra

O Risk Guard isolado foi a decisão mais importante: a estratégia literalmente não consegue executar uma ordem sem passar pelo Risk Guard. Isso não é convenção de código — é estrutura. Um bug na estratégia não pode causar liquidação porque ela não tem acesso ao executor."

---

**"O que é XTDB e como diferente do Datomic?"**

*Curta:* "Mesmo modelo Datalog imutável do Datomic, com bitemporalidade nativa: Valid Time separado de Transaction Time. Criado pela JUXT, open source."

*Profunda:* "Ambos são Datalog com imutabilidade. A diferença é bitemporalidade: XTDB separa quando o fato foi verdadeiro no mundo (Valid Time) de quando o sistema registrou (Transaction Time). Datomic tem apenas Transaction Time.

Para trading isso importa: imagine que às 14h30 um sinal dispara uma ordem. Às 16h você descobre que o dado de mercado das 14h20 estava errado — a exchange o corrigiu às 15h50. Em PostgreSQL, a correção sobrescreve o original. Em XTDB, você consulta 'o que o sistema sabia às 14h29 sobre o dado das 14h20' — e reconstrói exatamente o estado de conhecimento no momento da decisão. Isso é lookahead bias eliminado por propriedade estrutural, não por disciplina de código."

---

**"Explique o race condition que você resolveu no Ark Engine."**

*Curta:* "Estado compartilhado entre FractalEngine e FSM causava leituras rasgadas. Resolvi com event chaining: FractalEngine produz snapshot imutável (AnalyzedEvent) que o FSM consome — sem acesso a estado externo."

*Profunda:* "Na topologia fan-out original, o FractalEngine calculava os indicadores e os atualizava em campos em memória, depois publicava um evento. O FSM lia os indicadores diretamente do FractalEngine. O problema: entre publicar o evento e o FSM ler, um segundo candle podia chegar e sobrescrever os indicadores. O FSM tomava decisão com dados do candle 2, achando que eram do candle 1. Torn read clássico.

O redesign: FractalEngine não expõe estado. Ao terminar de processar um candle, encapsula tudo num `AnalyzedEvent` struct imutável e publica via NATS. O FSM recebe só esse struct — não tem referência ao FractalEngine.

```
candle 1 → FractalEngine → AnalyzedEvent{jaw:X, ao:Y} → NATS → FSM
candle 2 → FractalEngine → AnalyzedEvent{jaw:X', ao:Y'} → NATS → FSM
```

Cada decisão do FSM é determinística dado o AnalyzedEvent. Race condition é estruturalmente impossível. O benefício colateral: backtesting replay de AnalyzedEvents históricos produz exatamente as mesmas decisões que produção."

---

### KAFKA / MENSAGERIA

**"Você não tem Kafka em produção. Isso é um problema?"**

"É uma lacuna operacional, não conceitual. Os padrões que Kafka implementa — particionamento, consumer groups com offset, exactly-once semântico, backpressure, dead letter queue — implementei com Redis Streams no Ark Engine Clojure e com NATS JetStream no Go.

A curva de Kafka está em operações de cluster: configuração de brokers, replicação, tuning, monitoramento de lag. Não está nos padrões de streaming distribuído — esses conheço na prática. Tenho interesse direto em fechar essa lacuna, e consultoria com projetos variados é o lugar certo para isso."

---

**"Qual a diferença entre Kafka, NATS JetStream e Redis Streams?"**

| | Kafka | NATS JetStream | Redis Streams |
|---|---|---|---|
| **Durabilidade** | Alta (replicação multi-broker) | Média (persiste em disco) | Média (AOF/RDB) |
| **Latência** | ~ms | sub-ms | sub-ms |
| **Operação** | Cluster complexo | Processo único | Processo único |
| **Throughput** | Altíssimo | Alto | Alto |
| **Consumer Groups** | Sim | Sim | Sim |
| **Exactly-once** | Sim (transacional) | Sim | Semântico |
| **Ecossistema** | Rico (Connect, Streams) | Crescendo | Limitado |

"Para 95% dos casos de uso, os três entregam. Kafka é a escolha quando o volume é muito alto, quando você precisa do ecossistema, ou quando o time já opera. NATS e Redis são pragmáticos quando você quer os padrões sem o overhead operacional."

---

## PARTE 5: PERGUNTAS COMPORTAMENTAIS (FORMATO STAR)

*Situação → Tarefa → Ação → Resultado*

---

**"Me conte sobre um problema técnico difícil que você resolveu."**

> **S:** No Octopus Pay, a migração Pathom 2→3 tinha prazo — a versão 2 estava sendo descontinuada e funcionalidades que precisávamos só existiam no 3.
>
> **T:** Migrar sem downtime em sistema de pagamentos em produção, com 25+ integrações dependendo dos resolvers existentes.
>
> **A:** Primeiro mapeei o grafo completo de dependências usando o Pathom Index do v3. Identifiquei resolvers de alta criticidade (gateway calls) e baixo risco (atributos calculados locais). Migrei em camadas: atributos folha primeiro, intermediários depois, entradas que tocavam integrações externas por último. Cada camada tinha testes de regressão antes de ir para produção.
>
> **R:** Migração sem incidente. Benefício colateral: Pathom 3 com resolução paralela por padrão acelerou queries que antes eram seriais.

---

**"Me conte sobre uma situação em que você discordou de uma decisão técnica."**

> **S:** Cliente queria persistir snapshots de estado em PostgreSQL em vez de Datomic para "simplificar".
>
> **T:** O domínio era auditoria financeira — rastreabilidade era requisito regulatório, não opcional.
>
> **A:** Em vez de argumentar por preferência técnica, traduzi para risco de negócio: "Quando o auditor perguntar qual era o estado do sistema quando essa transação foi aprovada, qual é a resposta com PostgreSQL?" Mostrei o custo de construir auditoria ad hoc versus o que Datomic entrega nativamente. Propus um spike de 2 dias para demonstrar.
>
> **R:** Cliente aprovou Datomic após o spike. A chave foi transformar a discussão de "qual tecnologia você prefere" para "qual risco você quer assumir."

---

**"Como você lida com um cliente que quer algo tecnicamente errado?"**

> "Primeiro entendo o que está por trás do pedido. Clientes raramente pedem soluções técnicas — pedem resultados de negócio com uma solução técnica acoplada. Quando separo as duas coisas, geralmente consigo propor algo que atende o resultado sem o problema técnico. Se após a explicação o cliente insiste, documento o risco, implemento com o mínimo de dano possível e mantenho a conversa aberta."

---

**"Me conte sobre uma entrega que não correu como planejado."**

> **S:** No Zougue MPMS, a integração VTEX para simulação de carrinho tinha comportamento não documentado — a API retornava 200 com corpo de erro em cenários de estoque.
>
> **T:** O sistema marcava pedidos como aprovados quando deveriam estar em erro.
>
> **A:** Adicionei logging detalhado das respostas VTEX, identifiquei os 3 cenários não documentados, escrevi um adapter que normalizava esses casos para o modelo canônico de erro, adicionei testes com os payloads reais capturados.
>
> **R:** Zero regressões após o fix. Aprendizado: validar APIs de terceiros com payloads reais em staging antes de produção — especialmente VTEX, que tem comportamentos não documentados frequentes.

---

## PARTE 6: PERGUNTAS DIFÍCEIS — SEM RODEIOS

**"O Ark Engine lucra?"**

"Não ainda. A infraestrutura é sólida e os benchmarks são reais. O que falta é edge de estratégia — indicadores de preço sozinhos não têm expectativa positiva consistente em mercados eficientes porque todo participante os vê. Os próximos passos são dados de microestrutura: funding rate arbitrage, liquidation-driven entries. Mas o que é relevante para a Buzzlabs é a infraestrutura: event-driven, imutável, testada, com métricas medidas."

---

**"Por que você saiu da consultoria em julho de 2025?"**

"Para ter tempo integral para o Ark Engine. A versão Clojure com XTDB e Polylith exigia um nível de foco incompatível com projetos de cliente. Agora que o sistema está estável, retorno à consultoria — que é o ambiente onde produzo melhor e onde quero continuar."

---

**"Você consegue trabalhar com outros desenvolvedores depois de quase um ano solo?"**

"Consultoria de 2018 a 2025 foi trabalho em equipe por definição — cada cliente tinha um time. O período solo foi intencional e delimitado. Prefiro código revisado: revisão encontra o que você não vê quando está próximo demais do problema."

---

**"O que você não sabe que gostaria de aprender na Buzzlabs?"**

"Kafka em produção com volume real. Trabalhar com um time maior de Clojure — toda minha experiência foi em squads pequenos. E qualquer domínio que a Buzzlabs atenda que eu ainda não trabalhei — cada domínio novo em consultoria Clojure é uma oportunidade de ver onde o ecossistema resolve algo de forma inesperadamente elegante."

---

**"Por que não criou sua própria consultoria?"**

"Já cogitei. O que me falta para isso não é técnico — é a rede de clientes que uma consultoria estabelecida tem. Prefiro construir essa reputação dentro de um time que já tem credibilidade no mercado antes de considerar algo independente."

---

## PARTE 7: PERGUNTAS PARA FAZER AO ENTREVISTADOR

*Escolha 3-4 dependendo do fluxo. Quem faz perguntas inteligentes parece mais competente do que quem só responde bem.*

**Sobre o trabalho:**
- "Qual é o projeto atual mais tecnicamente desafiador que a equipe está trabalhando?"
- "Como é a divisão entre backend Clojure e frontend ClojureScript nos projetos recentes?"
- "Quando um cliente chega com um problema, como a equipe decide a stack? Há casos em que vocês recomendam não usar Clojure?"
- "Qual é o ciclo típico de um projeto — desde a proposta até a entrega?"

**Sobre a equipe:**
- "Como é estruturado o onboarding de um novo engenheiro num projeto em andamento?"
- "Como a equipe lida com revisão de código?"
- "Qual foi a última decisão técnica importante que a equipe debateu? Como chegaram ao consenso?"

**Sobre crescimento:**
- "Como vocês lidam com gaps como o Kafka — há projetos que expõem o time a tecnologias novas?"
- "Existe espaço para contribuir com open source no ecossistema Clojure dentro dos projetos?"

**Sobre a Buzzlabs:**
- "O que diferencia a Buzzlabs de outras consultorias Clojure?"
- "Qual foi o projeto mais complexo que a equipe entregou nos últimos dois anos?"

---

## PARTE 8: COMPARAÇÕES TÉCNICAS PARA REFERÊNCIA RÁPIDA

### Datomic vs XTDB
| | Datomic | XTDB |
|---|---|---|
| **Modelo** | Datalog, imutável | Datalog, bitemporal |
| **Tempo** | Transaction Time | Valid Time + Transaction Time |
| **Backend** | Próprio (DynamoDB, SQL) | RocksDB, JDBC |
| **Licença** | Comercial (free pequeno porte) | Open source |
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

### Fulcro vs React/SPA tradicional
| | Fulcro | React + Redux/Zustand |
|---|---|---|
| **Estado** | Mapa normalizado Clojure | Atoms/stores JS |
| **Fetching** | EQL declarativo (Pathom) | Imperativo (useEffect, RTK Query) |
| **Linguagem** | ClojureScript (mesma do backend) | JavaScript/TypeScript |
| **Vantagem** | Stack unificada, sem impedância | Ecossistema enorme |

---

## PARTE 9: CONCEITOS PARA REVISAR

Se a entrevista for técnica com código:

**Alta probabilidade:**
1. **Resolver Pathom simples** — sintaxe de `defresolver`, como declarar input/output
2. **Query Datalog** — `[:find ?e :where [?e :user/email "x@y.com"]]`
3. **Atom + swap!** — gestão de estado imutável, diferença de `reset!`
4. **Malli schema básico** — `[:map [:name :string] [:age :int]]` e como validar
5. **Diferença entre `map`, `reduce`, `transduce`** — e quando usar cada

**Média probabilidade:**
6. **core.async** — `chan`, `go`, `>!`, `<!`, diferença de thread-blocking vs park
7. **O que é uma transducer** — composição de transformações sem coleção intermediária
8. **Como Clojure lida com nil** — `nil` é falsy, `some->`, `when-let`, `nil-safe`
9. **XTDB query básica** — `(xt/q db '{:find [?e] :where [[?e :user/name "Patrick"]]})`
10. **Polylith structure** — components vs bases vs projects

---

## PARTE 10: ARMADILHAS — O QUE NÃO FAZER

- **Não fale mal do cliente anterior.** Fale em aprendizados.
- **Não minimize o Go.** O Ark Streams é bom trabalho de engenharia. Não se desculpe por ele.
- **Não exagere no Kafka.** "Conheço os padrões, falta experiência operacional" é honesto e forte.
- **Não demonstre desespero.** Mesmo que precise muito. Desespero gera dúvida sobre julgamento.
- **Não responda "não sei" sem continuar.** "Não trabalhei com isso especificamente, mas o padrão que conheço é X" demonstra pensamento, não lacuna.
- **Não deixe silêncios longos.** Se precisar pensar, diga "deixa eu pensar um segundo."
- **Não pergunte sobre salário na primeira entrevista.** Deixe eles trazerem o assunto.
- **Não elabore demais sobre o que o Ark Engine não faz.** Fale do que faz e do que vem a seguir.

---

## PARTE 11: ABERTURA E FECHAMENTO

### Abertura (primeiros 2 minutos)
- "Obrigado pela oportunidade" — diga uma vez, não repita
- Se perguntarem "como você está" → "bem, animado para a conversa" — sem detalhes pessoais
- Se for remota: teste áudio e câmera 10 minutos antes; fundo neutro; iluminação na frente, não atrás

### Fechamento (últimos 5 minutos)
Quando perguntarem "tem mais alguma pergunta?" — **sempre tenha**. Use uma da Parte 7.

Antes de encerrar, declare interesse explicitamente:
> "Saio dessa conversa com mais interesse do que entrei. A stack, o modelo de consultoria e o tipo de problema que vocês resolvem são exatamente o ambiente em que quero trabalhar. Qual é o próximo passo do processo?"

Perguntar sobre o próximo passo é assertivo — não é desespero, é profissionalismo.

### Follow-up (24h após)
E-mail curto para quem te entrevistou:

> **Assunto:** Obrigado — Entrevista [data]
>
> Obrigado pela conversa de ontem. A discussão sobre [algo específico que foi dito — não genérico] confirmou meu interesse na vaga. Fico à disposição para qualquer informação adicional.
>
> Patrick

A referência específica prova que você estava presente — e diferencia de um e-mail template.

---

## PARTE 12: NEGOCIAÇÃO

- **Não dê o primeiro número se puder evitar.** "Qual é o range da vaga?" é uma resposta válida.
- **Se precisar dar um número**, dê acima do que você aceitaria. É mais fácil ceder do que subir.
- **Não negocie contra você mesmo.** Se demorarem a responder, não reduza a proposta para "facilitar". Silêncio não é negativa.
- **Além de salário:** modalidade de contrato (PJ vs CLT), horário flexível, projeto inicial — pergunte sobre o que está em andamento.
- **Se a oferta vier abaixo:** "Fico feliz com o interesse. O que me faria aceitar sem hesitar seria X — tem espaço para isso?" Uma pergunta, não uma exigência.

---

## RESUMO EXECUTIVO

Você tem um perfil forte para essa vaga. O que vai decidir:

1. **Demonstrar que pensa em Clojure** — fale sobre imutabilidade, composição e dados como princípios, não como bibliotecas.
2. **Contar a história do Ark Engine corretamente** — Clojure primeiro com XTDB/Polylith, Go por custo operacional, mesmos princípios preservados.
3. **Transformar o Kafka gap em honestidade qualificada** — padrões conhecidos na prática, lacuna operacional, interesse real em fechar.
4. **Mostrar que você entrega** — cada projeto tem resultado concreto, não apenas tecnologias listadas.
5. **Não demonstrar que precisa** — mesmo que precise. Confiança calibrada é o que diferencia sênior de júnior em entrevista.
6. **Fazer boas perguntas** — quem pergunta bem parece mais competente do que quem só responde bem.
