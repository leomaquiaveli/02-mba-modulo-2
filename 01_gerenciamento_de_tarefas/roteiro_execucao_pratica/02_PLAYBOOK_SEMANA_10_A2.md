# Playbook 2 — Semana 10 (A2)

> **Projeto:** MBA Inteli Módulo 2 — Case Vitaliza (2º Movimento: AGIR — Submissão 60d `08/12`, Revelação `10/12`, Entrega Final `18/12/2026`)  
> **Ambiente de Dados:** Google BigQuery ([`thermal-origin-470820-e7.vitaliza_inteli_modulo_2`](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2))  
> **Objetivo:** conduzir qualquer integrante do grupo na **construção completa dos seus próprios entregáveis de Negócios (6 Slides do Conselho) e de Tecnologia da Semana 10**, aprendendo na prática como funcionam a **Extração Multimodal com IA Generativa (Texto + Imagens de Mapas de Calor)**, o **Teste de Ablação**, a **Comparação de 4 Algoritmos Supervisionados (Logística, Árvores, Random Forest e Gradient Boosting)**, a **Modelagem Causal de Uplift (Siegel)**, a **Alocação Financeira de Orçamento (Profit Analytics)** e o **Redator Generativo de CRM com Briefing Fechado**.
>
> **Seus arquivos (na sua pasta em `membros/`):**
> * Negócios A2 (os 6 slides do Conselho): `membros/nome_membro_1/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md`
> * Tecnologia A2 (multimodal, 4 modelos de 60 dias, uplift e redator de CRM): `membros/nome_membro_1/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`
>
> **Artefatos oficiais do grupo (só para a comparação no fim de cada passo; não peça ao agente para lê-los antes disso):**
> * [`artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md`](../../artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md)
> * [`artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`](../../artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md)

---

## O que cada passo produz

| Passo | O que você aprende | O que constrói no `ARTEFATO_NEGOCIOS_SEMANA10_A2.md` (6 slides do Conselho) | O que constrói no `ARTEFATO_TECH_SEMANA10_A2.md` (Seções 1 a 4) |
| :--- | :--- | :--- | :--- |
| **Passo 01** | Narrativa para o Conselho (Série B) e avaliação de arquitetura de produto (*Win-Back* vs. *Forecasting* vs. *Uplift* frente ao Strava). | **Slide 1:** Diagnóstico do Problema e Série B;<br>**Slide 2:** Os 4 Perfis e os 2 Fatos Vitais (`70,22%` Lojas e `995` *Sleeping Dogs*);<br>**Slide 3:** Caminho A vs. Caminho B vs. Nossa Arquitetura Prescritiva. | **Seção 1:** Arquitetura Ponta a Ponta das 5 Peças na Semana 10 (Diagrama Mermaid integrando Tabelas, Textos, Heatmaps, 4 Modelos e Motor de Uplift/CRM). |
| **Passo 02** | Engenharia de IA Generativa & Visão: Extração com Schema JSON tipado, Contagem de Pixels por Cor vs. VLM em `25.473` PNGs, *Tokenomics* e **Teste de Ablação**. | Insumos de personalização e custo de IA (`R$ 420/mês` no orçamento global). | **Seção 2 Completa (Peça 2 / Obj. 5):** Contratos JSON de Extração, Comparação Pixels (R$ 0) vs. VLM em `heatmaps_90d/` e **Teste de Ablação** (`PR-AUC 0,5714 ➔ 0,5986`, `+2,72 p.p.`). |
| **Passo 03** | Ciência de Dados Supervisionada: comparação *Out-of-Time* entre modelos lineares e ensembles de árvores (**Logística, Árvore, Bagging/RF e Boosting**). | Base preditiva que alimenta a priorização de risco nos Slides 3 e 4. | **Seção 3 Completa (Peça 3 / Obj. 4):** Tabela comparativa das **4 Famílias Supervisionadas (60d)** (`ROC-AUC = 0,7858`, `PR-AUC = 0,5986`, `Lift@10% = 2,96x`). |
| **Passo 04** | Inferência Causal e **Uplift Modeling (Eric Siegel)**: análise de Teste A/B controlado (`campanha_ago26.csv`), isolando *Persuadíveis* e provando os *Sleeping Dogs*. | **Slide 4 Completo:** Prova Causal do Experimento de `10/08/2026` (`14.120` sorteados) — **Tabela 4.1** (Por Plano) e **Tabela 4.2** (Prova Empírica dos *Sleeping Dogs*: `+9,16 p.p.` de churn induzido). | **Seção 4.1 (Peça 4 / Obj. 6):** Algoritmo da Regra Prescritiva de Contato em 5 Regras determinísticas. |
| **Passo 05** | *Profit-Driven Analytics* (Verbeke et al.) e GenAI com Guardrails: alocação ótima de **R$ 40k/mês** (`300 CS` + `1.500 WA`), DRE de **Lucro Líquido (`+R$ 207,8k`)** e **Copywriting com Briefing Fechado**. | **Slide 5 Completo:** Matriz Prescritiva de Alocação Mensal e ROI (`+786%`);<br>**Slide 6 Completo:** Matriz de Riscos, Gatilhos (*Kill-Switch*) e Contingência. | **Seção 4.2 Completa (Peça 5 / Obj. 8):** Exemplos Reais de Saída do Redator Generativo com Briefing Fechado (Exemplos A e B). |

---

## PASSO 01 — Diagnóstico para o Board (Slides 1 e 2) e Comparação Estratégica Caminho A vs. B (Slide 3 + Arquitetura Tech Seção 1)

### O que este passo ensina
Na Semana 10, você não está apresentando um relatório acadêmico: você está no papel da **Camila Ferraz (VP de Crescimento e Retenção)** diante do **Conselho de Administração da Vitaliza**, que precisa decidir onde investir para defender o valuation da **Série B** após o anúncio do **Strava Premium** no Brasil.
Existem duas propostas rivais na mesa da diretoria:
* **Caminho A (*Win-Back Reativo* — "O Bombeiro"):** Colocar uma oferta automática quando o cliente clica em *"Cancelar"* no site. **Por que falha sozinho?** Porque **70,22% da base (`10.359` clientes)** assina via App Store ou Google Play e cancela nas configurações do celular, sem passar pelo site da Vitaliza.
* **Caminho B Puro (*Engagement Forecasting* — "O Detector de Fumaça"):** Calcular um score diário de risco de churn e disparar mensagens para todo mundo com risco alto. **Por que é perigoso sozinho?** Porque existem **`995` clientes inativos (`0` treinos) que ainda estão com a renovação ligada pagando `R$ 24,0 mil/mês` por esquecimento (*Sleeping Dogs*)**. Se o Caminho B mandar um alerta para eles, eles se lembram da assinatura e cancelam.
* **Nossa Recomendação (Arquitetura Prescritiva de Uplift):** Une a capacidade preditiva do Caminho B com o **Filtro Causal de Uplift (Siegel)**, agindo nos **Persuadíveis** e mantendo silêncio absoluto nos **Sleeping Dogs**.

---

### Raciocínio do passo

**Pergunta de negócio:** quanto a Vitaliza está perdendo, quem está saindo e qual das propostas da diretoria consegue alcançar essas pessoas? Quem pergunta é o Conselho de Administração, a quem Camila Ferraz (VP de Crescimento e Retenção) apresenta. Da resposta depende a escolha entre financiar o Caminho A, defendido por Patrícia (Head de CS), o Caminho B, defendido por Marcelo (Head de Produto), ou uma combinação dos dois. Rita Fontes (CFO) vai pedir o tamanho do problema em reais antes de discutir qualquer solução.

**Onde olhar e por quê:**

| Fonte | O que usar | Por que é necessária |
| :--- | :--- | :--- |
| Tabela `assinaturas` | `status_atual`, `plano_atual`, `canal_cobranca`, `renovacao_automatica` | Define quem é pagante ativo no corte, quanto paga, por onde paga e quem já desligou a renovação. |
| Tabela `uso_mensal` (`mes = '2026-09'`) | `atividades` (treinos no mês) | Mede o hábito no último mês antes do corte. Sem ela não é possível separar quem treina de quem só paga. |
| `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md`, seção 4 | preços, taxas das lojas (15%), do cartão (3,5%) e do Pix (0,99%) | São as regras que transformam preço de tabela em receita líquida, que é o que entra no caixa. |
| `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md`, seções 1 e 2 | posições de Patrícia, Marcelo, Diego Almeida (CTO) e Rita Fontes; os dois fatores críticos | Mostra o conflito que o Slide 3 precisa resolver. |
| `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` (e o seu A1) | os 4 clusters e a divisão dos inertes em 1.318 e 995 | Os segmentos do Slide 2 vêm da A1. A A2 não cria segmentos novos; ela reaproveita os da Semana 5. |

**Sequência de raciocínio:**

1. **Fixar a população: 14.753 pagantes ativos em 30/09/2026.** Por quê: as 14.813 assinaturas ativas incluem 60 cortesias, que não pagam. Incluí-las muda todos os percentuais. O filtro é `status_atual = 'ativa'` e `plano_atual IN ('mensal', 'anual')`.
2. **Converter preço em receita líquida mensal.** Por quê: o Conselho decide sobre o dinheiro que fica com a Vitaliza, e a loja retém 15%. O plano anual é dividido por 12 apenas para comparar com o mensal; o caixa do anual entra de uma vez.
3. **Medir a perda já contratada (renovação desligada).** Por quê: esses 2.250 clientes ainda pagam, mas já decidiram sair ao fim do ciclo. É receita que se perde mesmo que nada mais aconteça.
4. **Cruzar com os treinos de setembro para formar os 4 segmentos.** Por quê: o cancelamento se concentra onde o hábito cai abaixo de 5 treinos por mês. Perfis diferentes pedem ações diferentes, e essa é a base de tudo o que vem nos Passos 04 e 05.
5. **Testar o Caminho A contra o canal de cobrança.** Por quê: quem paga pela App Store ou pelo Google Play cancela nas configurações do celular. A oferta no botão "Cancelar" do site não aparece para esses 70,22%.
6. **Testar o Caminho B contra os inertes com renovação ligada.** *Sleeping Dog* (cão que dorme) é o cliente que não usa o app, continua pagando por esquecimento e tende a cancelar quando é lembrado da assinatura. Por quê: um score de risco coloca essas pessoas no topo da lista (zero treinos), e contatá-las provoca o cancelamento. A prova causal desse efeito está no Passo 04.
7. **Concluir que nenhum caminho isolado resolve.** A recomendação usa a previsão do Caminho B e acrescenta um filtro que decide quem deve ou não ser contatado.

**Armadilhas comuns:**

* **Usar 14.813 em vez de 14.753.** Como notar: os percentuais ficam próximos, mas não iguais aos do gabarito.
* **Somar o preço bruto (R$ 39,90) como receita.** Como notar: o MRR (receita recorrente mensal) passa de R$ 409.941.
* **Chamar todo inerte de Sleeping Dog.** Os 2.313 inertes incluem 1.318 que já desligaram a renovação. Só os 995 com renovação ligada são o grupo a proteger com silêncio.
* **Esquecer a premissa de quem não tem linha em `uso_mensal`.** O prompt pede para tratar ausência de registro como zero treinos. Confira se o agente fez isso (`LEFT JOIN` com `COALESCE(..., 0)`) e declare a premissa.
* **Ignorar o preço de influenciador.** A conta usa R$ 299,90 para todo plano anual. Quem entrou pagando R$ 239,90 no primeiro ano paga menos, então o MRR do anual pode estar levemente acima do real. Registre como limitação.
* **Misturar o deck narrativo com o Data Room.** Os números de setembro/2025 da narrativa (27.901 pagantes, churn de 10,2%) não entram nas contas. A regra do case é: em dados e contas, vale o Data Room.
* **Agente do BigQuery usando coluna que não existe.** O agente também erra. Se aparecer erro de coluna inexistente, peça a ele para listar o esquema da tabela e refazer a consulta com os nomes reais, sem mudar a lógica.

**Como conferir sozinho:**

* 2.082 (anual) + 168 (mensal) = 2.250; 2.250 ÷ 14.753 = 15,25%.
* 10.359 ÷ 14.753 = 70,22%; App Store 36,57% + Google Play 33,65% = 70,22%.
* Os 4 segmentos somam a base: 4.089 + 2.960 + 5.391 + 2.313 = 14.753, e os percentuais, somados, cobrem a base inteira.
* Os inertes se dividem sem sobra: 995 + 1.318 = 2.313.
* R$ 409.941 × 12 ≈ R$ 4,92 milhões por ano.
* O pico de abril confere com o resumo do case: 1.154 ÷ 14.237 ≈ 8,1%.

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `assinaturas`, `uso_mensal` e `usuarios`

* **Prompt para o agente do BigQuery:**
  ```text
  Para abrirmos a apresentação ao Conselho de Administração da Vitaliza (Slides 1, 2 e 3 da Semana 10), consolide sobre os 14.753 pagantes ativos em 30/09/2026 (assinaturas com status_atual = 'ativa' e plano_atual IN ('mensal', 'anual'), cruzando com uso_mensal no mes = '2026-09' por LEFT JOIN; quem não tem linha conta com 0 atividades):
  1. Qual é a Receita Líquida Mensal total e Anualizada (12x) da base pagante, e quantos assinantes (N e %) já desligaram a renovação (renovacao_automatica = 'nao') no plano anual e no plano mensal?
  2. Mostre a tabela resumida dos 4 segmentos comportamentais (1. Atletas Sociais de Rua & GPS; 2. Praticantes Regulares Vídeo; 3. Entusiastas Oscilantes 1-4 treinos; 4. Pagantes Inertes 0 treinos) com Volume (N e %), média de atividades no mês e % Renovação Desligada. Regras: Cluster 1 = atividades >= 5 e atividades_ar_livre >= atividades / 2; Cluster 2 = atividades >= 5 e o restante; Cluster 3 = 1 a 4 atividades; Cluster 4 = 0.
  3. Destaque os 2 Fatos Vitais que inviabilizam o Caminho A puro (Win-Back apenas no botão cancelar do site): (a) quantos pagantes (N e %) estão na App Store e Google Play, e (b) quantos inativos com 0 atividades ainda estão com a renovação ligada (renovacao_automatica = 'sim') pagando por inércia (Sleeping Dogs) e qual a receita líquida mensal deles.
  ```

---

### Ação 2: Conferir o resultado
* **Estoque de Perda Contratada:** `14.753` pagantes ativos (`R$ 409.941/mês` ou `R$ 4,92 milhões/ano`), com **`2.250` (`15,25%`)** já com renovação desligada (`2.082` no anual e `168` no mensal).
* **Fato Vital 1 (Cegueira das Lojas):** **`10.359` pagantes (`70,22%`)** estão na App Store ou Google Play (o Caminho A só enxerga os `29,78%` do site).
* **Fato Vital 2 (*Sleeping Dogs*):** **`995` inativos (`0` treinos)** ainda estão com renovação ligada pagando **`R$ 24,0 mil/mês`** por esquecimento.

---

### Ação 3: Escrever os Slides 1, 2 e 3 e a Seção 1 de Tecnologia com o agente de código

Você escreve; o agente ajuda. Antes de abrir o agente, rascunhe em poucas linhas o título e a decisão de cada slide a partir do seu resultado da Ação 1. Compare com o artefato oficial só no final.

**Estrutura dos slides e da seção:**

| Item | Slide 1 — Diagnóstico | Slide 2 — Quem cancela | Slide 3 — Caminho A vs. B | Tech Seção 1 — Arquitetura |
| :--- | :--- | :--- | :--- | :--- |
| **Título (frase de conclusão)** | Diz o tamanho da perda, não o tema. Exemplo: "15,25% dos pagantes já desligaram a renovação e vão sair ao fim do ciclo". | Diz onde o risco está. | Diz qual caminho recomendamos e por quê. | Diz como as peças se conectam. |
| **O número que importa** | 2.250 assinantes com renovação desligada, sobre R$ 409.941/mês de receita líquida. | 70,22% nas lojas e 995 *Sleeping Dogs*. | Cobertura de 29,78% do Caminho A; risco de +9,16 p.p. do Caminho B sem filtro. | 14.753 pagantes na entrada, mesma população em todas as peças. |
| **Tabela de apoio** | Evolução do churn (5,6% em 2025, 6,6% em 2026, pico de 8,1% em abril). | Os 4 segmentos com volume, treinos e % de renovação desligada. | Três colunas (A, B, recomendação) por quatro dimensões (mecanismo, cobertura, risco, Strava). | Diagrama Mermaid: fontes, Peça 2, Peça 3, Peças 4 e 5. |
| **Decisão pedida ao Conselho** | Reconhecer que a perda contratada justifica agir agora. | Aceitar que perfis diferentes recebem ações diferentes, incluindo silêncio. | Aprovar a arquitetura combinada em vez de A ou B isolados. | Aprovar que todas as peças usam o mesmo corte (30/09/2026) e a mesma população. |

```text
Estou construindo os meus entregáveis da Semana 10 (A2) na minha pasta `membros/nome_membro_1/semana_10_A2/` (troque pelo nome da minha pasta em `membros/`). Edite APENAS arquivos dentro dessa pasta. Não altere nada em `artefatos_negocios/`, `artefatos_tecnologia/` nem em qualquer outro lugar do repositório.

Resultado que obtive no BigQuery no Passo 01:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Meu rascunho de título, número principal e decisão pedida para cada slide:
"""
[COLE AQUI O SEU RASCUNHO]
"""

Trabalhe em quatro etapas e pare ao final de cada uma para eu confirmar:
1. EXPLIQUE DE VOLTA: em linguagem de negócio, diga o que o meu resultado mostra (tamanho da perda contratada, os 4 segmentos, os 2 fatos vitais) e por que esses fatos enfraquecem o Caminho A e o Caminho B quando usados sozinhos. Aponte qualquer número que não feche, por exemplo segmentos que não somam 14.753 ou percentuais que não fecham a base inteira.
2. REDIJA NA MINHA PASTA: a partir do meu resultado e do meu rascunho, escreva os Slides 1, 2 e 3 no meu `ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e a Seção 1 (diagrama Mermaid das 5 peças) no meu `ARTEFATO_TECH_SEMANA10_A2.md`. Cada slide deve ter título em forma de conclusão, o número principal, uma tabela de apoio e a decisão pedida ao Conselho. Preserve o meu texto quando ele estiver correto e indique a fonte (tabela, query ou documento) de cada número.
3. COMPARE NO FINAL: só agora leia os Slides 1 a 3 de `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e a Seção 1 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`. Liste as diferenças em três grupos: números divergentes, argumentos que faltam no meu e pontos em que o meu está mais claro. Não copie trechos do artefato oficial para o meu arquivo; eu decido o que ajustar.
4. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_10_A2/`, nunca `git add .`). Faça o commit no padrão do `03_GUIA_GIT.md`, seção 6: no título, `docs(membros):` seguido do que foi feito neste passo 01 do A2; na descrição, um tópico para cada alteração feita nos arquivos (um ou mais). Não coloque o meu nome na mensagem: o Git já registra o autor. Me mostre a mensagem antes de commitar e depois o hash. Em seguida rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (os *Sleeping Dogs* por plano e canal):**
   ```text
   Dentro dos 995 assinantes ativos que tiveram 0 atividades em setembro (uso_mensal, mes = '2026-09', ou sem linha nesse mês) mas ainda estão com renovacao_automatica = 'sim' (os nossos Sleeping Dogs), quantos são do plano anual e quantos são do plano mensal? E qual é a distribuição deles entre App Store, Google Play e Site?
   ```
2. **No agente do repositório ou no NotebookLM (Caminho A, Caminho B e o Strava):**
   ```text
   Leia o arquivo `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md` e o Slide 3 de `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md`. Me ajude a montar um argumento curto explicando para o Conselho por que o lançamento do Strava Premium no Brasil obriga a Vitaliza a ir além do Win-Back reativo (Caminho A), mas por que o Caminho B puro sem filtro de Uplift daria prejuízo.
   ```

---

## PASSO 02 — Peça 2 (Objetivo 5): Extração Multimodal de Texto e Imagem (`heatmaps_90d/`), Tokenomics e Teste de Ablação

### O que este passo ensina
O Objetivo 5 do case faz uma pergunta muito prática de engenharia de IA: **"Processar textos livres (`onboarding`, `tickets_suporte`, `feed_posts`) e `25.473` imagens de mapas de calor (`heatmaps_90d/`) melhora a previsão de churn o suficiente para pagar o custo dos tokens?"**
Aqui você aprende 3 conceitos modernos de IA Generativa aplicada a Ciência de Dados:
1. **Extração com Schema JSON Fixo (*Structured Outputs*):** Em vez de pedir um resumo aberto ao Gemini, exigimos que ele devolva um JSON tipado com variáveis booleanas e categóricas (`motivacao_onboarding`, `suporte_falha_tecnica_gps`, `feed_mencao_lesao_ou_dor`) que entram direto como colunas na tabela de Machine Learning.
2. **Sistematização Determinística em Imagens (Pixels vs. VLM):** Como os `25.473` mapas de calor de `heatmaps_90d/` usam cores fixas (`verde` = parque, `azul` = água, `areia` = praia, `amarelo` = avenida), contar a proporção de pixels por cor via Python (`Pillow`/`NumPy`) extrai o ambiente de treino e a variação de intensidade (`30/09` vs `31/07`) a **custo R$ 0,00 de API**.
3. **Teste de Ablação (*Ablation Study*):** É o experimento onde treinamos exatamente o mesmo algoritmo (**Gradient Boosting**) duas vezes: primeiro **sem** as colunas de texto/imagem (**Modelo A: `PR-AUC = 0,5714`**) e depois **com** as colunas de texto/imagem (**Modelo B: `PR-AUC = 0,5986`**), provando um ganho real de **`+2,72 p.p.`** por **R$ 280/mês** no lote de 14.753 ativos.

---

### Raciocínio do passo

**Pergunta de negócio:** vale pagar para ler o que os clientes escrevem e os mapas de calor das rotas? O ganho na previsão de churn compensa o custo de processamento? Diego Almeida (CTO) já alertou para o esforço de engenharia sobre 13 fontes desconectadas. Rita Fontes (CFO) quer saber se o custo cabe no teto de R$ 40.000/mês. Da resposta depende incluir ou não as variáveis de texto e imagem no modelo de produção e reservar o custo de IA no orçamento (linha 7 do Slide 5, R$ 420/mês, que cobre extração e redação).

**Onde olhar e por quê:**

| Fonte | O que usar | Por que é necessária |
| :--- | :--- | :--- |
| Tabela `onboarding` | `respondido_em`, `objetivo_texto` | Guarda a meta que o cliente declarou ao entrar. Hipótese: quem tem meta clara e prazo permanece mais. |
| Tabela `tickets_suporte` | `aberto_em`, `status`, `texto_cliente` | Mostra fricção técnica (GPS, sincronização), intenção declarada de cancelar e chamados sem resposta. |
| Tabela `feed_posts` | `data_hora`, `texto`, `curtidas` | Mostra menções a dor, lesão, pausa ou desânimo antes do corte. |
| ZIPs de `heatmaps_90d/` em `documentos/exhibits-m2/heatmaps/` | PNGs de 31/07 e de 30/09 | Mostram onde e com que intensidade a pessoa treina (parque, água, praia, avenida). |
| `src/02_pipeline_gemini_multimodal_crm.py` | funções `extract_heatmap_pixels_from_zip` e `extract_text_signals` | Mostra como o grupo implementou a contagem de pixels (custo R$ 0) e a extração de texto com schema. O script lê uma amostra de 5 PNGs para demonstrar o método. |
| `relatorios/simulacao_gemini_crm.json` | campos `gemini_api_mode` e `ablation_reference_metrics` | Registra se a execução usou a API do Gemini ou o modo offline e guarda os números da ablação. |
| `00_comece_por_aqui/03_trilha_ia_generativa_e_multimodal/01_EXTRACAO_MULTIMODAL_E_COPYWRITING_CRM.md` | seções 3, 5, 6, 8 e 9 | Traz as regras: corte temporal, comparação justa entre pixels e visão, amostra rotulada à mão, custo e ablação. |

**Sequência de raciocínio:**

1. **Decidir antes quais campos extrair e por quê.** Para cada campo, escreva a fonte, a hipótese e quando a Vitaliza passou a saber daquilo. Por quê: sem hipótese, extrai-se tudo e paga-se por variáveis que não ajudam a decisão.
2. **Filtrar tudo até 30/09/2026 23:59:59.** Por quê: texto posterior ao corte é vazamento de dados (*data leakage*, quando o modelo usa informação que não existiria no momento da decisão). O resultado fica bom no teste e falha na operação.
3. **Exigir resposta em schema JSON fixo.** Schema é um formato com campos e tipos definidos antes (verdadeiro/falso, categoria, número). Por quê: o modelo de churn só aceita colunas. Um resumo livre não vira coluna, e o validador consegue rejeitar respostas fora do formato.
4. **Testar primeiro a contagem de pixels nos mapas.** Por quê: os mapas usam paleta fixa (verde = parque, azul = água, areia = praia, amarelo = avenida). Contar cores custa R$ 0 e dá sempre o mesmo resultado. Um VLM (modelo de linguagem que lê imagens) só se justifica se medir algo que a contagem não mede, e com custo por imagem dentro do orçamento.
5. **Validar contra uma amostra rotulada à mão.** Por quê: um JSON válido pode estar errado. Só a comparação com respostas humanas mostra a taxa de erro de cada campo.
6. **Rodar o teste de ablação.** Treina-se o mesmo algoritmo, na mesma divisão temporal, sem e com as variáveis novas. Por quê: é a única forma de atribuir o ganho às variáveis novas, e não a outro algoritmo ou a outro período.
7. **Ler o ganho na métrica certa.** PR-AUC mede a qualidade da lista quando a classe de interesse (quem sai) é minoria; vai de 0 a 1, maior é melhor. Brier mede o erro médio das probabilidades; menor é melhor. Por quê: a cota de WhatsApp e CS é gasta no topo da lista, e é ali que o PR-AUC mostra diferença.
8. **Comparar ganho com custo.** R$ 280/mês equivale a cerca de R$ 0,019 por assinante no lote de 14.753. Por quê: a pergunta do Objetivo 5 é econômica. O ganho na previsão precisa pagar o custo de processamento.

**Armadilhas comuns:**

* **Ler os volumes de texto como número de pagantes.** As 63.929 respostas de onboarding incluem usuários que não pagam. O custo é calculado sobre o lote de 14.753 ativos.
* **Usar `pesquisa_saida` como variável do modelo.** Ela é respondida por quem já saiu, ou seja, revela o desfecho.
* **Ler a diferença entre os mapas de 31/07 e 30/09 como a mudança de um mês.** Cada imagem cobre 90 dias, e as janelas se sobrepõem.
* **Atribuir os +2,72 p.p. só ao texto.** O Modelo B soma texto e pixels juntos. A ablação do grupo não separa as fontes, enquanto o guia recomenda medir texto e imagem separadamente. Declare isso como limitação.
* **Tratar chamado com intenção explícita de cancelar como sinal antecipado.** Às vezes ele já é o próprio desfecho. Verifique a data do chamado em relação ao corte.
* **Esquecer o modo offline.** Sem a variável `GEMINI_API_KEY`, o script usa uma extração determinística calibrada, sem chamar o Gemini. O relatório deve dizer qual modo foi usado.
* **Confundir R$ 280 com R$ 420.** R$ 280 é a extração de texto da Peça 2. Os R$ 420 do Slide 5 cobrem as Peças 2 e 5 (extração e redação). Os artefatos não detalham a divisão do restante; se o Conselho perguntar, essa é uma lacuna a explicar.

**Como conferir sozinho:**

* 12.426 + 13.047 = 25.473 PNGs.
* 0,5986 − 0,5714 = 0,0272, ou seja, +2,72 p.p. O Brier caiu de 0,1352 para 0,1330, o que é melhora.
* O Modelo B tem exatamente os números do Gradient Boosting + Multimodal do Passo 03 (0,7858 / 0,5986 / 0,1330). Se os dois passos divergirem, um deles está errado.
* 14.753 × R$ 0,019 ≈ R$ 280.
* Peça ao agente do BigQuery a data máxima de cada fonte de texto depois do filtro. Nenhuma pode passar de 30/09/2026.
* Rode o script localmente (comando no `README.md` de `artefatos_tecnologia/semana_10_A2/`) e abra `relatorios/simulacao_gemini_crm.json`. Os valores de `ablation_reference_metrics` estão registrados no script como referência; o treino dos Modelos A e B não está no repositório. Você confere a coerência dos números, mas não consegue recalculá-los sem o código de treino do grupo.

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `onboarding`, `tickets_suporte` e `feed_posts`

* **Prompt para o agente do BigQuery:**
  ```text
  Para a Peça 2 (Objetivo 5 — Extração Multimodal de Texto e Imagem), consulte as bases de texto até '2026-09-30':
  1. Mostre o volume de registros válidos até 30/09/2026 em onboarding (respondido_em), tickets_suporte (aberto_em) e feed_posts (data_hora).
  2. Em tickets_suporte, quantos chamados mencionam no texto_cliente falha de GPS/sincronização ou intenção de cancelamento/preço, e quantos têm status 'aberto' ou 'sem_resposta'?
  3. Em feed_posts, mostre 5 exemplos reais de posts (coluna texto) que mencionam dor, lesão, pausa ou desânimo nos treinos.
  4. Cruze esses sinais com a tabela assinaturas e compare a taxa de renovação desligada (renovacao_automatica = 'nao') de quem tem ticket pendente ou menção negativa com a de quem não tem.
  ```

---

### Ação 2: Conferir o resultado
* **Volumes até o corte:** `onboarding` (`63.929`), `tickets_suporte` (`4.422`), `feed_posts` (`119.187`) e `heatmaps_90d/` (`12.426` PNGs em `31/07` + `13.047` PNGs em `30/09`).
* **Resultado do Teste de Ablação (Gradient Boosting 150 árvores):**
  * **Modelo A (Somente Tabelas e Logs):** `ROC-AUC = 0,7798` | `PR-AUC = 0,5714` | `Brier = 0,1352` | Custo = `R$ 0,00`.
  * **Modelo B (Tabelas + Features Extraídas de Texto/Suporte/Feed + Pixels):** **`ROC-AUC = 0,7858`** | **`PR-AUC = 0,5986` (`+2,72 p.p.`)** | **`Brier = 0,1330`** | Custo = **`R$ 280,00 / mês`**.

---

### Ação 3: Escrever a Seção 2 com o agente de código

Escreva primeiro, com suas palavras, a frase de conclusão da Seção 2 e a lista de campos que você extrairia, com a hipótese de cada um. Depois use o agente para redigir e, por último, para comparar com o artefato oficial.

**Estrutura da seção:**

| Subseção | O que precisa conter |
| :--- | :--- |
| **Título da seção (frase de conclusão)** | O resultado e a decisão em uma linha. Exemplo de forma: "Texto e imagem aumentam o PR-AUC em X p.p. por R$ Y/mês; recomendamos manter". |
| **2.1 Contrato de extração** | Um exemplo de JSON com os campos de texto e de mapa de calor; para cada campo, a fonte, a hipótese e a regra de corte temporal (até 30/09/2026). |
| **2.2 Pixels vs. VLM** | Tabela com critérios (custo, repetibilidade, o que mede, limitação) para os dois métodos e a escolha feita. |
| **2.3 Teste de ablação** | Tabela Modelo A vs. Modelo B (ROC-AUC, PR-AUC, Brier, custo) e a conclusão: o ganho paga o custo? |
| **Limitações** | Ablação com texto e pixels juntos; modo de execução do script (API ou offline); métricas sem código de treino no repositório. |

```text
Estou construindo o meu `ARTEFATO_TECH_SEMANA10_A2.md` na minha pasta `membros/nome_membro_1/semana_10_A2/` (troque pelo nome da minha pasta). Edite APENAS arquivos dentro dessa pasta. Não altere `artefatos_tecnologia/` nem qualquer outro lugar do repositório.

Resultado que obtive no BigQuery no Passo 02 (fontes de texto livre: onboarding, suporte e feed):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Meu rascunho da frase de conclusão e dos campos que eu extrairia, com a hipótese de cada um:
"""
[COLE AQUI O SEU RASCUNHO]
"""

Trabalhe em quatro etapas e pare ao final de cada uma para eu confirmar:
1. EXPLIQUE DE VOLTA: em linguagem simples, diga o que o meu resultado mostra sobre as três fontes de texto, por que cada campo do meu rascunho poderia ajudar a prever a saída, e o que o teste de ablação (Modelo A: PR-AUC 0,5714; Modelo B: PR-AUC 0,5986; custo R$ 280/mês) permite e não permite concluir. Leia `src/02_pipeline_gemini_multimodal_crm.py` e me diga em qual modo ele roda sem `GEMINI_API_KEY` e quantos PNGs ele lê na amostra.
2. REDIJA NA MINHA PASTA: escreva a Seção 2 (2.1 contrato JSON, 2.2 pixels vs. VLM, 2.3 ablação, limitações) no meu `ARTEFATO_TECH_SEMANA10_A2.md`, usando o meu resultado e o meu rascunho. Indique a fonte de cada número (query, script, relatório JSON ou documento do case).
3. COMPARE NO FINAL: só agora leia a Seção 2 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md` e liste as diferenças: números divergentes, campos ou argumentos que faltam no meu, e pontos em que o meu está mais claro ou mais honesto sobre limitações. Não copie trechos do artefato oficial; eu decido o que ajustar.
4. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_10_A2/`, nunca `git add .`). Faça o commit no padrão do `03_GUIA_GIT.md`, seção 6: no título, `docs(membros):` seguido do que foi feito neste passo 02 do A2; na descrição, um tópico para cada alteração feita nos arquivos (um ou mais). Não coloque o meu nome na mensagem: o Git já registra o autor. Me mostre a mensagem antes de commitar e depois o hash. Em seguida rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (o que os clientes escrevem antes de sair):**
   ```text
   Cruze assinaturas (clientes com renovacao_automatica = 'nao') com tickets_suporte e feed_posts. Mostre 5 casos reais de clientes que desligaram a renovação, exibindo o que postaram no feed (texto) e o que escreveram no suporte (texto_cliente) até 30/09/2026.
   ```
2. **No agente do repositório ou no NotebookLM (como a IA lê textos e mapas de calor):**
   ```text
   Leia o guia `00_comece_por_aqui/03_trilha_ia_generativa_e_multimodal/README.md` e o relatório já pronto em `relatorios/simulacao_gemini_crm.json`. Me explique em linguagem de negócios como os textos do suporte/onboarding e os mapas de calor ajudam a descobrir o motivo real pelo qual o cliente está parando de treinar, e se o gasto de R$ 280/mês com essa leitura de IA se paga.
   ```

---

## PASSO 03 — Peça 3 (Objetivo 4): Comparação das 4 Famílias de Modelos Supervisionados em 60 Dias

### O que este passo ensina
No Objetivo 4 completo, o case pede para comparar **4 famílias clássicas de Machine Learning Supervisionado**:
1. **Regressão Logística (Linear):** Soma pesos lineares para cada variável. É fácil de explicar, mas não captura sozinha quando **duas coisas combinadas** explodem o risco (ex.: ser do *Plano Mensal* **E** cair para *1 treino* **E** ter *ticket sem resposta*).
2. **Árvore de Decisão (`max_depth=5`):** Cria regras do tipo `SE treinos < 3 E plano = mensal ENTÃO risco = alto`. Concentra muito bem o topo 10% (`Lift = 2,97x`), mas uma árvore sozinha é instável.
3. **Bagging / Random Forest (`200` árvores em paralelo):** Treina 200 árvores independentes sorteando amostras e tira a média, reduzindo a variância (`ROC-AUC = 0,7850`).
4. **Gradient Boosting + Multimodal (`150` árvores sequenciais):** Cada nova árvore foca em corrigir os erros das árvores anteriores. Combinado com as variáveis extraídas de texto e heatmaps, é o nosso **Modelo Campeão (`ROC-AUC = 0,7858` | `PR-AUC = 0,5986`)**.

---

### Raciocínio do passo

**Pergunta de negócio:** qual modelo deve ordenar a fila de clientes que disputam as 1.500 mensagens de WhatsApp e os 300 atendimentos de CS? Marcelo (Head de Produto) defende o score preditivo diário e precisa mostrar que ele acerta. Diego Almeida (CTO) vai manter o modelo em produção e quer saber se a complexidade compensa. O Conselho precisa confiar que a lista não é arbitrária. Da resposta depende qual algoritmo gera a submissão de previsões de 60 dias em 08/12/2026 e alimenta a priorização dos Passos 04 e 05.

**Onde olhar e por quê:**

| Fonte | O que usar | Por que é necessária |
| :--- | :--- | :--- |
| Tabelas `assinaturas`, `uso_mensal` (`mes = '2026-09'`) e `tickets_suporte` | `plano_atual`, `atividades`, `status` do chamado, `renovacao_automatica` | São as variáveis da query de interação desta Ação 1. Mostram se o risco de uma combinação é maior do que a soma das partes. |
| Tabela `pagamentos` | `status` e `tentativa` da cobrança | Falha de cobrança é causa de saída sem decisão do cliente; entra no Modelo A e na Ação 4. |
| `00_comece_por_aqui/04_contexto_extra/01_VISAO_DETALHADA_SEMANA5_VS_SEMANA10.md`, seção 4, item 2 | definição de saída em 60 dias | O alvo do modelo: renovação desligada ou sem assinatura vigente em 29/11/2026. |
| `00_comece_por_aqui/02_trilha_ciencia_de_dados_e_ml/02_CLUSTERIZACAO_E_CHURN_SUPERVISIONADO.md`, seções 9, 10 e 20 | contrato do alvo, divisão temporal com embargo, critérios para promover o campeão | Explica como comparar modelos sem trapaça temporal e por que o campeão não é escolhido só pela maior nota. |
| Seção 3 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md` | hiperparâmetros e métricas | Registra a configuração de cada família (por exemplo, `max_depth=5` na árvore). Leia só na comparação final. |

**Sequência de raciocínio:**

1. **Fixar o alvo.** Saída em 60 dias é estar com a renovação desligada ou sem assinatura vigente em 29/11/2026. Por quê: sem uma definição única, os modelos não são comparáveis, e é essa a regra usada na revelação de 10/12.
2. **Treinar no passado e testar em um período posterior (validação *out-of-time*).** Por quê: o modelo será usado no futuro. Embaralhar as datas coloca informação do futuro no treino e infla a nota. Entre treino e teste há um intervalo (embargo) para que a janela de 60 dias de um não invada o outro.
3. **Começar pela Regressão Logística.** Por quê: é simples e explicável. Qualquer modelo mais complexo precisa superá-la para justificar o esforço que o CTO vai assumir.
4. **Olhar a query de interação.** Ela cruza plano, faixa de treino e chamado pendente. Por quê: se uma combinação (por exemplo, mensal, poucos treinos e chamado sem resposta) tem risco muito acima das partes, modelos de árvore tendem a capturar isso melhor do que a logística. É a justificativa de negócio para testar árvores.
5. **Comparar as 4 famílias nas mesmas métricas.** ROC-AUC mede a capacidade de colocar quem sai acima de quem fica (0,5 equivale a sorteio; 1,0 é perfeito). PR-AUC e Brier foram definidos no Passo 02. Lift@10% diz quantas vezes a taxa de saída no topo 10% da lista supera a média da base. O topo 10% corresponde aproximadamente à cota de 1.500 WhatsApps.
6. **Escolher pelo uso real.** Por quê: a lista alimenta uma cota fixa, então o acerto no topo (PR-AUC e Lift) pesa mais do que a média geral. O critério final do case é o lucro da regra de decisão (Verbeke et al., 2012), não a nota estatística.
7. **Registrar o limite do score.** O score diz quem tende a sair. Ele não diz se o contato vai mudar essa decisão. Por quê: quem decide quem contatar é o Passo 04.

**Armadilhas comuns:**

* **Ler a query desta Ação 1 como previsão.** Ela descreve a renovação desligada em 30/09. O modelo prevê o que acontece até 29/11, que só será conhecido em 10/12.
* **Achar que o campeão vence em tudo.** A Árvore de Decisão tem Lift@10% de 2,97x, acima dos 2,96x do campeão. O Random Forest tem ROC-AUC de 0,7850, quase igual a 0,7858. A vantagem do campeão está no PR-AUC (0,5986 contra 0,5839).
* **Comparar modelos com variáveis diferentes.** Pela tabela, só o campeão usa as variáveis multimodais. O mesmo Gradient Boosting sem elas (Modelo A do Passo 02) tem PR-AUC de 0,5714, abaixo do Random Forest. Parte do ganho deve ser atribuída às variáveis novas. Diga isso no texto.
* **Tratar diferença na terceira casa decimal como certeza.** O guia de ML diz que, se o ganho for pequeno e instável, o modelo mais simples pode ser preferível. Pergunte se o ganho se repete em mais de um corte temporal.
* **Afirmar "maior lucro líquido" sem a conta.** O artefato oficial não traz o lucro por modelo. Se for usar essa frase, peça a conta ao grupo ou escreva que o critério de lucro será aplicado.
* **Usar variáveis posteriores ao corte**, como pesquisa de saída ou curtidas acumuladas depois de 30/09.

**Como conferir sozinho:**

* Da Logística ao Gradient Boosting, ROC-AUC e PR-AUC crescem e o Brier cai. Se a sua tabela não mostrar essa ordem, há erro de transcrição.
* A linha 4 da tabela é igual ao Modelo B do Passo 02.
* 10% de 14.753 dá cerca de 1.475, próximo da cota de 1.500 WhatsApps. É por isso que o Lift é medido no topo 10%.
* Na sua query, a soma de `n_clientes` de todas as linhas deve dar 14.753.
* Não há script de treino desses 4 modelos no repositório; os valores vêm do relatório do grupo. Você confere a coerência interna, mas não reproduz os números sem o código. Se precisar defender os números na banca, peça ao grupo o notebook ou script de treino.

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `assinaturas`, `uso_mensal` e `tickets_suporte`

* **Prompt para o agente do BigQuery:**
  ```text
  Para o Objetivo 4 (Classificação Supervisionada de Churn em 60 dias), extraia no BigQuery as regras de negócio não-lineares que diferenciam uma Árvore de Decisão / Gradient Boosting de uma Regressão Logística simples:
  Cruze assinaturas (14.753 pagantes ativos) com uso_mensal (mes = '2026-09', coluna atividades; sem linha conta como 0) e tickets_suporte. Compare a taxa de renovação desligada (renovacao_automatica = 'nao') combinando simultaneamente: Plano (mensal vs anual) x Faixa de atividades (0, 1-4, 5+) x Presença de ticket pendente (status 'aberto' ou 'sem_resposta', aberto_em até 30/09/2026). Mostre n_clientes em cada combinação. Mostre como a interação entre essas variáveis concentra o risco no topo 10% da base (cota de 1.500 WhatsApps).
  ```

---

### Ação 2: Conferir o resultado
| Família Supervisionada | ROC-AUC | PR-AUC | Brier Score | Lift @ Topo 10% (`1.500` WA) | Papel |
| :--- | ---: | ---: | ---: | ---: | :--- |
| **1. Regressão Logística (Baseline)** | `0,7522` | `0,5079` | `0,1504` | `2,55x` | Referência linear interpretável. |
| **2. Árvore de Decisão (`max_depth=5`)** | `0,7691` | `0,5420` | `0,1372` | **`2,97x`** | Regras de negócio transparentes. |
| **3. Bagging / Random Forest (`200` árvores)** | `0,7850` | `0,5839` | `0,1333` | `2,93x` | Redução de variância em dados tabulares. |
| **4. Gradient Boosting + Multimodal (`150` árvores)** | **`0,7858`** | **`0,5986`** | **`0,1330`** | **`2,96x`** | **Modelo Campeão** em precisão/recall e lucro líquido. |

---

### Ação 3: Escrever a Seção 3 com o agente de código

Antes do agente, escreva em duas ou três frases qual modelo você escolheria e por quê, olhando a tabela da Ação 2 e a query de interação. Inclua o ponto em que o campeão perde para outro modelo.

**Estrutura da seção:**

| Item | O que precisa conter |
| :--- | :--- |
| **Título (frase de conclusão)** | Qual modelo ordena a fila e em qual métrica ele ganha. |
| **Contrato temporal** | Três linhas: data de corte, janela de 60 dias até 29/11/2026, definição de saída. |
| **O número que importa** | PR-AUC do campeão (0,5986) contra a referência logística (0,5079), e o Lift@10% ligado à cota de 1.500 WhatsApps. |
| **Tabela de apoio** | As 4 famílias com hiperparâmetros principais, ROC-AUC, PR-AUC, Brier e Lift@10%. |
| **Evidência de negócio** | Uma ou duas linhas da query de interação que mostram uma combinação de risco que a logística capta mal. |
| **Decisão e limites** | Qual modelo vai para produção, por que não o Random Forest ou a Árvore, e o que a seção não prova (efeito do contato, lucro por modelo). |

```text
Estou construindo o meu `ARTEFATO_TECH_SEMANA10_A2.md` na minha pasta `membros/nome_membro_1/semana_10_A2/` (troque pelo nome da minha pasta). Edite APENAS arquivos dentro dessa pasta. Não altere `artefatos_tecnologia/` nem qualquer outro lugar do repositório.

Resultado que obtive no BigQuery no Passo 03 (interação entre plano, faixa de treino e chamado pendente):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Minha escolha de modelo e o motivo, em poucas frases:
"""
[COLE AQUI O SEU RASCUNHO]
"""

Trabalhe em quatro etapas e pare ao final de cada uma para eu confirmar:
1. EXPLIQUE DE VOLTA: sem jargão matemático, diga o que a minha query mostra sobre combinações de risco, o que significam ROC-AUC, PR-AUC, Brier e Lift@10% para a cota de 1.500 WhatsApps, e se a minha escolha de modelo se sustenta. Aponte onde o campeão (Gradient Boosting + Multimodal) não é o melhor e se a comparação com o Random Forest é justa, já que só o campeão usa variáveis de texto e imagem.
2. REDIJA NA MINHA PASTA: escreva a Seção 3 no meu `ARTEFATO_TECH_SEMANA10_A2.md` com título em forma de conclusão, contrato temporal, tabela das 4 famílias, uma evidência da minha query e um parágrafo de decisão e limites. Indique a fonte de cada número.
3. COMPARE NO FINAL: só agora leia a Seção 3 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md` e liste as diferenças: números divergentes, argumentos que faltam no meu e pontos em que o meu está mais claro. Não copie trechos do artefato oficial; eu decido o que ajustar.
4. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_10_A2/`, nunca `git add .`). Faça o commit no padrão do `03_GUIA_GIT.md`, seção 6: no título, `docs(membros):` seguido do que foi feito neste passo 03 do A2; na descrição, um tópico para cada alteração feita nos arquivos (um ou mais). Não coloque o meu nome na mensagem: o Git já registra o autor. Me mostre a mensagem antes de commitar e depois o hash. Em seguida rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (o perfil de maior risco da base):**
   ```text
   Cruze assinaturas (14.753 pagantes ativos) com uso_mensal (mes = '2026-09'), pagamentos (status = 'recusado') e tickets_suporte (status 'aberto' ou 'sem_resposta'). Quais combinações de plano_atual, faixa de atividades e problemas de pagamento ou suporte têm mais de 40% de renovacao_automatica = 'nao'?
   ```
2. **No agente do repositório ou no NotebookLM (os 4 algoritmos sem jargão):**
   ```text
   Leia o guia `00_comece_por_aqui/02_trilha_ciencia_de_dados_e_ml/02_CLUSTERIZACAO_E_CHURN_SUPERVISIONADO.md` e a Seção 3 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`. Me explique sem jargão matemático a diferença prática entre Regressão Logística, Árvore de Decisão, Random Forest e Gradient Boosting, e por que usamos o critério de lucro líquido em reais (e não só AUC) para escolher o modelo vencedor.
   ```

---

## PASSO 04 — Peça 4 (Objetivo 6): O Experimento de `10/08/2026` (`campanha_ago26`) e a Prova dos *Sleeping Dogs* vs. *Persuadíveis*

### O que este passo ensina
Este é o ponto alto da teoria de **Uplift Modeling (Eric Siegel)**:
* Prever que alguém tem **alto risco de sair** não significa que mandar uma mensagem vai salvar essa pessoa.
* Em `10/08/2026`, a Vitaliza sorteou **`14.120` pagantes** em 4 grupos (`controle`, `desafio`, `cupom`, `conteudo`). Quando cruzamos esse experimento no BigQuery com a frequência de treino no mês anterior ao sorteio (**julho/2026**), descobrimos **a prova matemática dos 4 Quadrantes de Siegel**:
  1. **Nos Inativos (`0` treinos em julho — `N = 2.685`):** Quem ficou no **Controle (sem receber mensagem)** teve **`51,86%`** de saída/desligamento. Mas quem recebeu **Desafio subiu para `61,02%` (`+9,16 p.p.` a mais de cancelamento)**, quem recebeu **Conteúdo subiu para `60,39%` (`+8,53 p.p.` pior)** e quem recebeu **Cupom subiu para `57,95%` (`+6,09 p.p.` pior)**. Ou seja: **mandar mensagem para quem tem 0 treinos acorda o *Sleeping Dog* e faz a Vitaliza perder dinheiro.**
  2. **Nos Oscilantes (`1 a 4` treinos em julho — `N = 5.241`):** O tratamento reduz a saída de `25,19%` (Controle) para **`20,37%` no Desafio (`+4,82 p.p.` de retenção ganha)** e **`21,45%` no Cupom (`+3,74 p.p.` ganho)** — e no plano mensal o **Cupom reduz a saída de `17,99%` para `10,63%` (`+7,36 p.p.` de Uplift)**. Esses são os **Persuadíveis**.

---

### Raciocínio do passo

**Pergunta de negócio:** para quem uma mensagem muda o resultado, e para quem ela piora? Patrícia (Head de CS) e Marcelo (Head de Produto) propõem contatar clientes, cada um com um gatilho diferente. Rita Fontes (CFO) não quer gastar onde o contato não muda nada. O Conselho precisa de prova de que a política funciona antes de aprovar o orçamento. Da resposta depende a regra de contato: quem recebe mensagem, com qual oferta, e quem fica em silêncio.

**Onde olhar e por quê:**

| Fonte | O que usar | Por que é necessária |
| :--- | :--- | :--- |
| Tabela `campanha_ago26` | `user_id`, `grupo`, `canal`, `oferta`, `abriu_push`, `abriu_email`, `clicou` | É o sorteio de 10/08/2026. É o único lugar do Data Room com comparação justa entre contatar e não contatar. |
| Tabela `assinaturas` | `status_atual`, `renovacao_automatica`, `plano_atual` | Dá o desfecho de cada sorteado no corte de 30/09/2026. |
| Tabela `uso_mensal` (`mes = '2026-07'`) | `atividades` (treinos no mês) | Mede o uso antes do sorteio, para dividir os sorteados em faixas sem contaminação pela campanha. |
| `00_comece_por_aqui/01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md`, seções 4 e 5 | pergunta causal, intenção de tratar, gates de validade, quadrantes, extrapolação de canal | É o protocolo que diz como ler o experimento sem tirar conclusões indevidas. |
| `src/02_pipeline_gemini_multimodal_crm.py`, função `apply_prescriptive_uplift_policy` | as regras em código | Mostra a Seção 4.1 aplicada a um cliente, com o motivo de cada decisão. |

**Sequência de raciocínio:**

1. **Usar o experimento, e não o modelo de churn.** O modelo diz quem tende a sair. Ele não diz o que acontece se a pessoa for contatada. Só a comparação entre sorteados que receberam mensagem e sorteados do grupo controle (sem mensagem) mede o efeito. *Uplift* é essa diferença: taxa de saída no controle menos taxa de saída no tratamento. Positivo significa que o contato ajudou.
2. **Manter todos os sorteados, inclusive quem não abriu nem clicou (intenção de tratar).** Por quê: abrir e clicar acontecem depois do envio. Filtrar por clique compara pessoas diferentes e desfaz o sorteio.
3. **Usar o mesmo desfecho para os quatro grupos:** saída efetiva ou renovação desligada em 30/09/2026. Por quê: a mesma régua para todos. Incluir a renovação desligada captura quem já decidiu sair, mesmo que ainda esteja pagando.
4. **Calcular o efeito por plano (Tabela 4.1).** Por quê: o mensal teve reajuste em março e reage a preço. No mensal, os três tratamentos reduziram a saída. No anual, o cupom em massa piorou o resultado (−3,09 p.p.).
5. **Dividir pelo uso em julho (Tabela 4.2).** Por quê julho: é anterior ao sorteio, então não foi afetado pela campanha. Usar setembro misturaria o efeito da própria mensagem com o perfil do cliente.
6. **Ler os quatro quadrantes de Siegel.** Persuadível sai sem contato e fica com contato. Garantido fica de qualquer forma. Perdido sai de qualquer forma. *Sleeping Dog* fica se deixado em paz e sai se contatado. Com 0 treinos, os três tratamentos pioraram a saída (+6,09 a +9,16 p.p.): é o padrão de *Sleeping Dog*. Com 1 a 4 treinos, todos melhoraram: Persuadíveis. Com 5 ou mais, o Desafio melhora a custo zero e o cupom só gastaria margem.
7. **Transformar o achado em regras fixas (Seção 4.1).** Bloquear 0 treinos com renovação ligada; vedar cupom para quem treina 5 ou mais vezes; CS para fricção técnica ou anual de alto valor; WhatsApp ordenado por retorno; e-mail e push para o restante. Por quê regras fixas: são auditáveis, e o redator de IA da Peça 5 não decide nada.

**Armadilhas comuns:**

* **Medir sucesso pelo clique.** O cupom tem o maior clique (16,45% no mensal), mas clique não é retenção. A Ação 4 explora essa diferença.
* **Tratar o quadrante como fato individual.** Ninguém é observado com e sem contato ao mesmo tempo. Os quadrantes são estimativas por grupo, e a regra trata faixas, não pessoas.
* **Ignorar a janela.** Sessenta dias depois de 10/08 seria 09/10, mas os dados terminam em 30/09. O desfecho cobre cerca de sete semanas. Declare isso no slide.
* **Extrapolar o canal sem aviso.** O experimento usou push + e-mail. WhatsApp e CS não foram testados. O Slide 6 trata isso como risco, com grupo de controle (*holdout*, parcela que não recebe contato e serve de comparação) de 10%.
* **Confiar em diferenças pequenas em grupos pequenos.** Cada célula da Tabela 4.2 tem cerca de um quarto da faixa. Diferenças como +1,31 p.p. (Conteúdo nos Garantidos) podem ser acaso. O protocolo pede intervalo de confiança, que os artefatos não trazem. Peça ao agente para calcular antes de afirmar.
* **Confundir os dois grupos de inativos.** Os 2.685 do experimento tinham 0 treinos em julho. Os 995 da base atual têm 0 treinos em setembro e renovação ligada. A regra transporta o aprendizado de um grupo para o outro, e isso é uma premissa.
* **Inverter o sinal.** Neste playbook, positivo é retenção ganha e "pior" é aumento da saída. Use a mesma convenção em todas as tabelas.

**Como conferir sozinho:**

* Plano mensal: 1.440 + 1.420 + 1.456 + 1.463 = 5.779; com o anual: 5.779 + 8.341 = 14.120.
* Faixas de julho: 2.685 + 5.241 + 6.194 = 14.120.
* Grupos do sorteio (documento de estratégia, seção 2.1): 3.579 + 3.515 + 3.472 + 3.554 = 14.120. Tamanhos próximos são sinal de sorteio saudável.
* Uplift = controle − tratamento: 17,99 − 10,63 = 7,36 p.p.; 51,86 − 61,02 = −9,16 p.p. (dano).
* Redução relativa citada no Slide 4: 7,36 ÷ 17,99 ≈ 41%.
* Peça ao agente do BigQuery a distribuição de plano e de canal de cobrança por grupo. Se um grupo tiver muito mais anuais que os outros, parte do efeito pode ser do plano.

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `campanha_ago26`, `assinaturas` e `uso_mensal`

* **Prompt para o agente do BigQuery:**
  ```text
  Precisamos gerar as duas tabelas oficiais do Slide 4 sobre o experimento controlado de 10/08/2026 (tabela campanha_ago26 com 14.120 sorteados):
  1. Tabela 4.1 (Efeito Causal por Plano — Mensal vs Anual): cruze campanha_ago26 com assinaturas pelo user_id. Para o Plano Mensal (5.779 sorteados) e para o Plano Anual (8.341 sorteados), mostre por grupo (controle, cupom, desafio, conteudo): total de sorteados, taxa de clique (clicou = TRUE), churn efetivo até o corte (status_atual != 'ativa') e taxa combinada de saída + renovação desligada (status_atual != 'ativa' ou renovacao_automatica = 'nao'), calculando o Uplift em pontos percentuais contra o grupo Controle.
  2. Tabela 4.2 (Prova Empírica dos Sleeping Dogs vs Persuadíveis por Uso Prévio em Julho/2026): cruze campanha_ago26 com assinaturas e com uso_mensal no mes = '2026-07' (pré-campanha, coluna atividades; sem linha conta como 0). Separe os 14.120 sorteados em 3 faixas de treino em julho:
     - '0 treinos no mês' (N = 2.685 — Sleeping Dogs)
     - '1 a 4 treinos no mês' (N = 5.241 — Persuadíveis)
     - '>= 5 treinos no mês' (N = 6.194 — Garantidos)
     Mostre a taxa de saída/desligamento de cada faixa nos grupos Controle, Desafio, Cupom e Conteúdo.
  ```

---

### Ação 2: Conferir o resultado
* **Tabela 4.1 (No Plano Mensal):**
  * `Controle` (`1.440`): `14,58%` churn efetivo | `17,99%` saída + desligamento.
  * `Cupom` (`1.420`): **`8,94%` churn efetivo | `10,63%` saída + desligamento (`+7,36 p.p.` de Uplift)**.
  * `Desafio` (`1.456`): **`11,13%` churn efetivo | `12,98%` saída + desligamento (`+5,01 p.p.` de Uplift a custo R$ 0)**.
  * `Conteúdo` (`1.463`): `13,53%` churn efetivo | `15,79%` saída + desligamento (`+2,20 p.p.`).
* **Tabela 4.2 (Por Uso em Julho/2026 — A Prova dos 4 Quadrantes de Siegel):**
  * **`0` treinos (`N = 2.685` — *Sleeping Dogs*):** `51,86%` no Controle vs. **`61,02%` no Desafio (`+9,16 p.p.` pior)**, **`57,95%` no Cupom (`+6,09 p.p.` pior)** e **`60,39%` no Conteúdo (`+8,53 p.p.` pior)**.
  * **`1 a 4` treinos (`N = 5.241` — *Persuadíveis*):** Caiu de `25,19%` (Controle) para **`20,37%` no Desafio (`+4,82 p.p.` ganho)** e **`21,45%` no Cupom (`+3,74 p.p.` ganho)**.
  * **`≥ 5` treinos (`N = 6.194` — *Garantidos*):** Caiu de `14,38%` para **`9,70%` no Desafio (`+4,68 p.p.` ganho a custo R$ 0)**.

---

### Ação 3: Escrever o Slide 4 e a Seção 4.1 com o agente de código

Antes do agente, escreva com suas palavras a frase que resume o experimento e as 5 regras de contato, uma linha cada, citando o número da Tabela 4.2 que justifica cada regra.

**Estrutura do slide e da seção:**

| Item | Slide 4 — Prova causal | Tech Seção 4.1 — Regra de contato |
| :--- | :--- | :--- |
| **Título (frase de conclusão)** | O que o experimento provou. Exemplo de forma: "Contatar quem não treinou aumentou a saída; contatar os oscilantes reduziu". | O que a regra faz antes de qualquer mensagem ser escrita. |
| **O número que importa** | +9,16 p.p. de saída a mais nos inativos que receberam Desafio; +7,36 p.p. de retenção com cupom no mensal. | As capacidades que a regra respeita: 300 CS e 1.500 WhatsApps. |
| **Tabela de apoio** | Tabela 4.1 (por plano) e Tabela 4.2 (por uso em julho), com controle como referência. | As 5 regras, cada uma com condição de entrada, ação, canal, oferta e a evidência do experimento. |
| **Ressalvas** | Janela de cerca de sete semanas; canal testado foi push + e-mail; sem intervalos de confiança. | Premissa de transportar o resultado de julho para a base de setembro. |
| **Decisão pedida ao Conselho** | Aprovar silêncio para os *Sleeping Dogs* e a proibição de cupom para os Garantidos. | (Técnica) Aprovar que o redator de IA só recebe clientes já autorizados pela regra. |

```text
Estou construindo os meus entregáveis da Semana 10 (A2) na minha pasta `membros/nome_membro_1/semana_10_A2/` (troque pelo nome da minha pasta). Edite APENAS arquivos dentro dessa pasta. Não altere `artefatos_negocios/`, `artefatos_tecnologia/` nem qualquer outro lugar do repositório.

Resultado que obtive no BigQuery no Passo 04 (Tabela 4.1 por plano e Tabela 4.2 por faixa de uso em julho, experimento de 10/08/2026):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Minha frase-resumo do experimento e as minhas 5 regras de contato:
"""
[COLE AQUI O SEU RASCUNHO]
"""

Trabalhe em quatro etapas e pare ao final de cada uma para eu confirmar:
1. EXPLIQUE DE VOLTA: em linguagem de negócio, diga o que as minhas duas tabelas mostram, calcule o uplift de cada tratamento contra o controle (controle menos tratamento, positivo = retenção ganha) e diga quais diferenças são grandes o bastante para sustentar uma regra e quais podem ser acaso. Se possível, calcule um intervalo de confiança aproximado para as diferenças da Tabela 4.2. Confira se as minhas 5 regras decorrem dos números.
2. REDIJA NA MINHA PASTA: escreva o Slide 4 (Tabelas 4.1 e 4.2, ressalvas e decisão pedida) no meu `ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e a Seção 4.1 (as 5 regras, cada uma com a evidência correspondente) no meu `ARTEFATO_TECH_SEMANA10_A2.md`. Compare as minhas regras com a função `apply_prescriptive_uplift_policy` em `src/02_pipeline_gemini_multimodal_crm.py` e me avise se houver diferença de lógica. Indique a fonte de cada número.
3. COMPARE NO FINAL: só agora leia o Slide 4 de `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e a Seção 4.1 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md` e liste as diferenças: números divergentes, regras ou ressalvas que faltam no meu e pontos em que o meu está mais claro. Não copie trechos do artefato oficial; eu decido o que ajustar.
4. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_10_A2/`, nunca `git add .`). Faça o commit no padrão do `03_GUIA_GIT.md`, seção 6: no título, `docs(membros):` seguido do que foi feito neste passo 04 do A2; na descrição, um tópico para cada alteração feita nos arquivos (um ou mais). Não coloque o meu nome na mensagem: o Git já registra o autor. Me mostre a mensagem antes de commitar e depois o hash. Em seguida rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (clicar significa ficar?):**
   ```text
   Na tabela campanha_ago26 cruzada com assinaturas, compare a taxa de clique (clicou = TRUE) com a taxa real de retenção (status_atual = 'ativa' e renovacao_automatica = 'sim') nos grupos Cupom e Desafio. Por que olhar apenas para a taxa de clique da campanha enganaria a diretoria de marketing?
   ```
2. **No agente do repositório ou no NotebookLM (os 4 quadrantes de Siegel):**
   ```text
   Leia o arquivo `00_comece_por_aqui/01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md` e os resultados do Passo 04. Me explique com exemplos práticos da Vitaliza a diferença entre Persuadíveis, Garantidos, Perdidos e Sleeping Dogs, e como essa matriz resolve o conflito entre quem quer contatar todos os clientes de risco alto (Patrícia, Head de CS, no Caminho A, e Marcelo, Head de Produto, no Caminho B) e a CFO Rita Fontes, que exige retorno comprovado dentro de R$ 40.000/mês.
   ```

---

## PASSO 05 — Peças 4 e 5 (Objetivos 7 e 8): Alocação do Orçamento de R$ 40k (`300 CS` + `1.500 WA`), Lucro Líquido (`+R$ 207,8k`), Copywriter CRM e Contingência

### O que este passo ensina
No último passo do módulo, você conecta a decisão matemática ao mundo real das operações de Growth e CRM:
1. **Otimização sob Restrições Físicas e Financeiras (Objetivo 7):** Temos no máximo **300 atendimentos humanos de CS** (R$ 18/un = R$ 5.400), **1.500 mensagens de WhatsApp** (R$ 0,40/un = R$ 600), E-mail (R$ 0,01) e Push (R$ 0,00), e a soma de tudo (incluindo os descontos de R$ 35,91 no mensal e R$ 25,00 no anual + R$ 420 de tokens de IA) não pode passar de **R$ 40.000/mês**. Nossa regra gasta **R$ 26.441,90/mês** e gera **+R$ 207.840,10 de Lucro Líquido Incremental**.
2. **Copywriting Generativo com Briefing Fechado (Objetivo 8):** O modelo de linguagem (Gemini) **nunca decide se o cliente ganha desconto**. Quem decide o canal e a oferta é a regra determinística da Peça 4. O Gemini recebe um briefing fechado com o contexto do cliente (a meta que ele escreveu no `onboarding.csv`, a modalidade favorita) e a oferta exata autorizada, e redige a mensagem individual sem poder inventar promoções.

---

### Raciocínio do passo

**Pergunta de negócio:** com R$ 40.000/mês, 1.500 WhatsApps e 300 atendimentos de CS, qual alocação gera o maior lucro incremental, quanto ele vale e o que pode dar errado? Rita Fontes (CFO) exige retorno comprovado dentro desses limites. Patrícia (Head de CS) opera os 300 atendimentos. Diego Almeida (CTO) responde pela operação do redator de IA. O Conselho aprova ou não o desembolso. Da resposta depende o plano de novembro e dezembro: quanto gastar, em quem, por qual canal, com qual oferta e com quais travas.

**Onde olhar e por quê:**

| Fonte | O que usar | Por que é necessária |
| :--- | :--- | :--- |
| `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md`, seção 4 | custo de cada canal, tetos, ofertas permitidas, taxas, custo de servir (R$ 4,20/mês), CAC (R$ 118) | São as regras econômicas do case. Toda linha do Slide 5 depende delas. |
| Tabelas 4.1 e 4.2 do Passo 04 | uplift por oferta e por faixa de uso | Dizem quantos clientes cada ação deve salvar. |
| Slide 2 e A1 | tamanho de cada público: 5.391 oscilantes, 7.049 engajados (4.089 + 2.960), 995 *Sleeping Dogs*, 1.318 inertes com renovação desligada | São os volumes que a alocação distribui. |
| Tabelas `usuarios`, `assinaturas`, `uso_mensal`, `onboarding`, `feed_posts` | plano, canal, treinos, meta declarada, último post | Formam o contexto permitido do briefing de cada mensagem. |
| `src/02_pipeline_gemini_multimodal_crm.py`, função `generate_and_validate_crm_message` | briefing, termos proibidos, limite de 420 caracteres, template de reserva | Mostra como o redator é contido: oferta só a autorizada, sem mencionar score, com template se a validação falhar. |
| `00_comece_por_aqui/01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md`, seções 6, 7, 9 e 10 | fórmula de valor incremental, restrições, briefing fechado, riscos e gatilhos | É o método que o Slide 5 e o Slide 6 aplicam. |

**Sequência de raciocínio:**

1. **Listar as restrições antes de alocar.** Orçamento de R$ 40.000/mês (canais, descontos e IA juntos), 1.500 WhatsApps, 300 CS, push no máximo 1 por semana. Por quê: uma ação lucrativa isolada pode não caber quando disputa o mesmo recurso.
2. **Estimar o valor de cada público e ação.** Valor = uplift × receita líquida retida − custo de canal − custo de oferta. Por quê alocar por lucro incremental e não por risco: o cliente de maior risco pode ser Perdido ou *Sleeping Dog*. O dinheiro rende onde o contato muda o resultado e o cliente vale mais do que o custo de mantê-lo.
3. **Alocar primeiro o recurso mais caro e escasso.** Os 300 atendimentos de CS (R$ 18 cada) vão para casos que exigem uma pessoa: fricção técnica ou plano anual de alto valor. Por quê: é onde uma conversa resolve o que uma mensagem não resolve.
4. **Dividir os 1.500 WhatsApps por tipo de dor.** 750 com cupom para o mensal sensível a preço (maior uplift, +7,36 p.p., mas com desconto) e 750 com Desafio (uplift de +5,01 p.p., custo de oferta zero). Por quê: equilibra retenção e margem.
5. **Cobrir o restante com e-mail e push.** Custo quase zero e sem teto de volume. Por quê: os demais Persuadíveis ainda respondem ao contato, mas não justificam o custo do WhatsApp.
6. **Proteger margem e evitar dano.** Garantidos recebem só Desafio ou comunidade, sem cupom. *Sleeping Dogs* não recebem nada. Por quê: cupom para quem ficaria de qualquer forma é desconto perdido; contato com inativos aumenta a saída (Passo 04).
7. **Somar custos e conferir o teto.** Desconto entra só para quem aceita a oferta (cerca de 450 aceites × R$ 35,91 no mensal; cerca de 150 × R$ 25 no anual). Por quê: quem recebe e não aceita não gera custo de desconto.
8. **Calcular o retorno.** Clientes salvos = volume × uplift. Lucro incremental = receita retida − desembolso. ROI = lucro ÷ desembolso. Por quê: é a conta que Rita Fontes vai refazer.
9. **Escrever riscos com gatilho e ação (Slide 6).** Cada risco precisa de um indicador mensurável e de uma resposta automática. *Kill-switch* é o bloqueio automático que interrompe o envio quando o gatilho dispara.
10. **Montar o briefing fechado do redator.** A regra decide canal e oferta; o modelo de linguagem só redige; o validador recusa oferta não autorizada e usa o template homologado se a mensagem falhar.

**Armadilhas comuns:**

* **Alocar por risco.** A cota iria para os inertes, justamente onde o contato causa dano.
* **Somar o CAC evitado (R$ 43.778) ao lucro.** É outra forma de expressar o mesmo valor (371 clientes × R$ 118). Somar seria contar duas vezes.
* **Aplicar o uplift de push + e-mail ao WhatsApp e ao CS como se tivesse sido medido.** O uplift de 14% do CS é uma estimativa; esse canal não foi testado. Escreva "estimado" e mantenha o *holdout* de 10%.
* **Apresentar receita retida como receita realizada.** É projeção e precisa de horizonte declarado (a coluna do Slide 5 indica "Ciclo 6m / Anual").
* **Deixar o modelo de linguagem escolher a oferta** ou mencionar o score de risco. O script bloqueia termos como "score de churn", "risco de sair" e "sleeping dog".
* **Expor dado sensível na mensagem.** O guia de IA pede personalização proporcional. Mencionar lesão ou saúde exige cuidado; prefira oferecer opções (treino adaptado, pausa) em vez de diagnosticar.
* **Publicar dados pessoais.** A tabela `usuarios` traz e-mail, cidade e data de nascimento. No artefato, identifique o cliente só pelo `user_id`, como o artefato oficial faz.

**Como conferir sozinho:**

* Canais e IA: R$ 5.400 (300 CS) + R$ 600 (1.500 WhatsApps) + R$ 112,40 (e-mail e push: R$ 41,91 + R$ 70,49) + R$ 420 (IA) = R$ 6.532,40.
* Descontos: 450 × R$ 35,91 = R$ 16.159,50; 150 × R$ 25 = R$ 3.750; total R$ 19.909,50.
* Desembolso: R$ 6.532,40 + R$ 19.909,50 = R$ 26.441,90, abaixo de R$ 40.000; folga de R$ 13.558,10.
* Capacidades: 750 + 750 = 1.500 WhatsApps; 300 CS.
* Clientes salvos por linha (volume × uplift): 300 × 14% ≈ 42; 750 × 7,36% ≈ 55; 750 × 5,01% ≈ 38; 4.191 × 3,5% ≈ 146; mais 90 Garantidos preservados = 371.
* Receita retida: R$ 49.450 + R$ 30.899 + R$ 21.348 + R$ 82.023 + R$ 50.562 = R$ 234.282; menos R$ 26.441,90 = R$ 207.840,10.
* *Sleeping Dogs* protegidos: 995 × 8,53% (efeito do Conteúdo nos inativos) ≈ 85, que é o número do Slide 5. Confirme com o grupo como foram calculados os R$ 15.800/mês preservados nessa linha.
* **ROI:** lucro ÷ desembolso = R$ 207.840,10 ÷ R$ 26.441,90 ≈ 7,86, ou seja, +786%. Uma versão anterior do Slide 5 mostrava +686% por erro de conta; confira sempre o ROI refazendo a divisão.
* **Volume: some a coluna da Matriz 5.1.** As linhas 1 a 6 somam 14.035 (300 + 750 + 750 + 4.191 + 7.049 + 995), enquanto a linha consolidada mostra 14.753. A diferença é de 718 clientes. Uma leitura coerente com os números: a linha 4 inclui 600 dos 1.318 inertes com renovação desligada (janela das lojas), e os outros 718 não recebem ação. Confirme com o grupo e escreva isso no slide.
* **Receita por cliente salvo.** Divida a receita retida de cada linha pelos clientes salvos e compare com o que um cliente paga no horizonte declarado (por exemplo, R$ 33,92/mês líquidos no mensal pelas lojas, menos R$ 4,20 de custo de servir). Se o valor por cliente salvo for maior do que esse teto, o horizonte usado precisa ser explicado no slide.
* Mensagem do Exemplo A: R$ 39,90 × 0,70 = R$ 27,93. A oferta do texto deve ser igual à oferta autorizada, e o texto deve caber em 420 caracteres.

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `assinaturas`, `uso_mensal`, `usuarios`, `onboarding`, `tickets_suporte` e `feed_posts`

* **Prompt para o agente do BigQuery:**
  ```text
  Para fecharmos o Slide 5 (Alocação de Orçamento R$ 40.000/mês e Lucro Líquido) e a Seção 4.2 (Redator Generativo de CRM), consulte os 14.753 pagantes ativos em 30/09/2026:
  1. Mostre a divisão exata dos 14.753 pagantes ativos nos públicos da nossa Matriz Prescritiva de Alocação:
     - Persuadíveis (1 a 4 atividades em uso_mensal, mes = '2026-09' = 5.391 clientes): sendo 300 no Time de CS (R$ 18/un = R$ 5.400), 750 no WhatsApp com Cupom 30% off 3 meses (R$ 0,40/un + descontos R$ 16.159,50), 750 no WhatsApp com Desafio 6 Semanas (R$ 0,40/un, desconto R$ 0) e o restante em E-mail + Push (R$ 0,01/un)
     - Garantidos (>= 5 atividades = 7.049 clientes): Push Semanal + E-mail com Desafio 6 Semanas (R$ 70,49, proibido cupom)
     - Sleeping Dogs (0 atividades com renovacao_automatica = 'sim' = 995 clientes): Silêncio Absoluto (R$ 0, evitando +9,16 p.p. de churn induzido).
  2. Extraia também o perfil real do assinante user_id = 'u_2722f848' (e de mais 2 assinantes persuadíveis de 1 a 4 treinos) juntando usuarios, assinaturas, uso_mensal, onboarding (objetivo_texto) e feed_posts (texto) para gerarmos os exemplos de mensagens personalizadas com briefing fechado. Não traga e-mail.
  ```

---

### Ação 2: Conferir o resultado
* **Custo de Canais + IA:** `R$ 6.532,40` (`R$ 5.400` de 300 CS + `R$ 600` de 1.500 WhatsApps + `R$ 112,40` E-mail/Push + `R$ 420` Tokens LLM).
* **Custo de Descontos Concedidos:** `R$ 19.909,50` (`R$ 3.750` anual + `R$ 16.159,50` mensal).
* **Desembolso Mensal Total:** **`R$ 26.441,90 / mês`** (respeitando com folga o teto de **`R$ 40.000,00 / mês`**).
* **Retorno Financeiro (Objetivo 7):** `~371` saídas evitadas/mês + `85` *Sleeping Dogs* protegidos = **`R$ 234.282,00`** de receita preservada $\rightarrow$ **Lucro Líquido Incremental de `+R$ 207.840,10` (ROI de `+786%`)**.

---

### Ação 3: Fechar os dois artefatos da Semana 10 com o agente de código

Antes do agente, monte você mesmo a conta do Slide 5 numa folha ou planilha: cada público, volume, canal, oferta, custo e clientes salvos. Faça as conferências do bloco "Como conferir sozinho" e anote o que não fechou. Para o Slide 6, escreva um risco por linha com o gatilho em número. Para a Seção 4.2, escolha os dois perfis da sua consulta e escreva o briefing de cada um antes de pedir a mensagem.

**Estrutura dos slides e da seção:**

| Item | Slide 5 — Alocação e lucro | Slide 6 — Riscos e contingência | Tech Seção 4.2 — Redator de CRM |
| :--- | :--- | :--- | :--- |
| **Título (frase de conclusão)** | Quanto se gasta, quanto se ganha, dentro de qual teto. | Quais riscos existem e como são contidos automaticamente. | Como a mensagem é gerada sem que a IA decida a oferta. |
| **O número que importa** | R$ 26.441,90/mês de desembolso e o lucro incremental estimado (com o ROI que o grupo confirmar). | O gatilho de cada risco (por exemplo, desligamento de renovação acima de 1,5% em 48h após envio). | Oferta autorizada e limite de 420 caracteres por mensagem. |
| **Tabela de apoio** | Matriz por público: volume, canal, oferta, custo de canal, desconto, salvos, receita retida; linha de consolidado. | Risco, impacto, gatilho, ação de contingência. | Para cada exemplo: contexto de entrada, oferta autorizada, mensagem gerada, resultado da validação. |
| **Ressalvas** | Valores estimados; uplift de WhatsApp e CS não testado; horizonte da receita retida declarado. | O que fica fora do controle (adesão real ao cupom, efeito no WhatsApp). | Mensagem nova não foi testada em experimento; retenção causada pelo texto exige teste próprio. |
| **Decisão pedida ao Conselho** | Aprovar o desembolso mensal para novembro e dezembro. | Aprovar as travas (*kill-switch* de inatividade, trava de orçamento, *holdout*). | (Técnica) Aprovar o validador e o template de reserva como condição de envio. |

```text
Estou fechando os meus entregáveis da Semana 10 (A2) na minha pasta `membros/nome_membro_1/semana_10_A2/` (troque pelo nome da minha pasta). Edite APENAS arquivos dentro dessa pasta. Não altere `artefatos_negocios/`, `artefatos_tecnologia/` nem qualquer outro lugar do repositório.

Resultado que obtive no BigQuery no Passo 05 (divisão dos públicos e perfis reais para o redator):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Minha conta do Slide 5, meus riscos do Slide 6 e meus dois briefings, com o que não fechou nas conferências:
"""
[COLE AQUI O SEU RASCUNHO]
"""

Trabalhe em quatro etapas e pare ao final de cada uma para eu confirmar:
1. EXPLIQUE DE VOLTA: refaça a minha conta com as regras da seção 4 de `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md` e diga, linha por linha, se custo, desconto e clientes salvos estão certos. Confira: soma dos custos menor ou igual a R$ 40.000; 1.500 WhatsApps; 300 CS; soma dos volumes contra 14.753; ROI = lucro ÷ desembolso. Explique por que a alocação segue o lucro incremental e não o risco, e me diga se algum risco do meu Slide 6 está sem gatilho mensurável.
2. REDIJA NA MINHA PASTA: escreva o Slide 5 (matriz, consolidado, ressalvas e decisão pedida) e o Slide 6 (riscos, gatilhos e contingências) no meu `ARTEFATO_NEGOCIOS_SEMANA10_A2.md`, e a Seção 4.2 (dois exemplos com briefing fechado, mensagem e validação) no meu `ARTEFATO_TECH_SEMANA10_A2.md`. Use a função `generate_and_validate_crm_message` de `src/02_pipeline_gemini_multimodal_crm.py` para checar cada mensagem: oferta igual à autorizada, nenhum termo proibido, até 420 caracteres. Não publique nome real de cliente além do que já consta no artefato oficial. Indique a fonte de cada número.
3. COMPARE NO FINAL: só agora leia os Slides 5 e 6 de `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e a Seção 4.2 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`. Liste as diferenças: números divergentes (inclusive ROI e soma dos volumes), riscos ou ressalvas que faltam no meu e pontos em que o meu está mais claro. Não copie trechos do artefato oficial; eu decido o que ajustar. Por fim, revise os meus dois arquivos de `semana_10_A2/` e diga se algum número aparece diferente entre eles.
4. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_10_A2/`, nunca `git add .`). Faça o commit no padrão do `03_GUIA_GIT.md`, seção 6: no título, `docs(membros):` seguido do que foi feito neste passo 05 do A2; na descrição, um tópico para cada alteração feita nos arquivos (um ou mais). Não coloque o meu nome na mensagem: o Git já registra o autor. Me mostre a mensagem antes de commitar e depois o hash. Em seguida rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (mensagens personalizadas):**
   ```text
   Escolha 3 clientes reais da tabela assinaturas que estejam no plano mensal, tenham entre 1 e 3 atividades em setembro (uso_mensal, mes = '2026-09') e tenham objetivo_texto preenchido na tabela onboarding. Mostre o user_id deles, a meta que escreveram no onboarding e escreva uma sugestão de mensagem curta e empática de WhatsApp oferecendo o Desafio de 6 Semanas conectado ao objetivo de cada um.
   ```
2. **No agente do repositório ou no NotebookLM (perguntas do Conselho):**
   ```text
   Leia o documento `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e o guia `00_comece_por_aqui/01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md`. Simule comigo 3 perguntas difíceis que a CFO Rita Fontes e o CTO Diego Almeida fariam na apresentação final ao Conselho sobre o nosso plano de R$ 26.441,90/mês e me mostre como responder cada uma usando os números que encontramos nos dados.
   ```

---

## Fechamento da Semana 10

Ao final dos cinco passos, você tem dois arquivos na sua pasta. Antes de salvar, revise a qualidade, prepare a apresentação e só então envie ao GitHub.

### 1. Checklist de qualidade dos dois artefatos

**Números**

- [ ] Os números que aparecem nos dois arquivos são idênticos: 14.753 pagantes; 70,22% nas lojas; 995 *Sleeping Dogs*; PR-AUC 0,5986 e ganho de +2,72 p.p.; R$ 280/mês de extração e R$ 420/mês de IA no orçamento; +9,16 p.p. de dano nos inativos; R$ 26.441,90/mês de desembolso; lucro incremental e ROI.
- [ ] Os números são coerentes com a A1: os 4 segmentos têm os mesmos tamanhos de `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` e do seu próprio A1 (4.089, 2.960, 5.391, 2.313), e os inertes se dividem em 1.318 e 995.
- [ ] Todas as somas do bloco "Como conferir sozinho" de cada passo fecham.
- [ ] O ROI confere com lucro ÷ desembolso (+786%), e a diferença entre a soma dos volumes da Matriz 5.1 e 14.753 está explicada no slide.

**Rastreabilidade**

- [ ] Cada afirmação tem origem identificável: uma consulta que você rodou no BigQuery, um script em `src/`, um relatório em `relatorios/` ou um documento do case. Uma nota de fonte abaixo de cada tabela resolve isso.
- [ ] Projeções estão marcadas como estimativas: clientes salvos, receita retida, lucro, ROI, uplift de WhatsApp e de CS.
- [ ] As limitações estão escritas: janela de cerca de sete semanas no experimento; canal testado foi push + e-mail; ablação com texto e pixels juntos; modo de execução do script; ausência de intervalos de confiança.

**Riscos**

- [ ] O Slide 6 tem cada risco com gatilho mensurável e ação de contingência.
- [ ] O *kill-switch* de inatividade está descrito com a regra exata: `dias_ativos = 0` nos últimos 21 dias e renovação ligada bloqueiam o envio.
- [ ] A trava de orçamento (descontos acumulados de R$ 28.000 até o dia 20) e o *holdout* de 10% estão no texto.

**Escrita**

- [ ] Cada título é uma frase de conclusão.
- [ ] Cada slide termina com a decisão pedida ao Conselho.
- [ ] Todo termo técnico é explicado na primeira vez que aparece.

**Governança**

- [ ] Nada fora da sua pasta em `membros/` foi editado (confira no item 3 abaixo).
- [ ] Não há dado pessoal além do necessário.

### 2. Preparar a apresentação ao Conselho

**2.1 A história em seis frases.** Leia em sequência. Se uma frase não decorre da anterior, falta um elo no deck.

1. **Slide 1:** a Vitaliza já tem 2.250 assinantes (15,25%) com saída contratada, e o churn subiu de 5,6% para 6,6% às vésperas da Série B e da chegada do Strava Premium.
2. **Slide 2:** o risco evitável se concentra nos 5.391 oscilantes, 70,22% da base cancela fora do alcance do site e 995 inativos continuam pagando por inércia.
3. **Slide 3:** o Caminho A não alcança quem paga pelas lojas e o Caminho B sem filtro acorda os inativos, então recomendamos o score preditivo combinado a um filtro causal.
4. **Slide 4:** o experimento de 10/08 mostrou que contatar quem não treinou aumenta a saída em até 9,16 p.p. e que contatar os oscilantes a reduz.
5. **Slide 5:** com R$ 26.441,90/mês, dentro do teto de R$ 40.000, a alocação por lucro incremental gera lucro estimado de R$ 207.840,10.
6. **Slide 6:** os riscos principais têm gatilhos e respostas automáticas, com *kill-switch* para inativos, trava de orçamento para cupons e *holdout* para medir o efeito real.

**2.2 As cinco perguntas mais difíceis.** Prepare a resposta de cada uma com o número na mão.

| # | Pergunta provável | Quem tende a perguntar | Onde está a resposta | Como responder |
| :-: | :--- | :--- | :--- | :--- |
| 1 | "Como vocês sabem que o contato causa a retenção, e não que esses clientes já ficariam?" | Conselho, Rita Fontes | Tabela `campanha_ago26`; Tabelas 4.1 e 4.2; documento de estratégia, seção 4 | O sorteio criou grupos comparáveis (tamanhos entre 3.472 e 3.579). A análise mantém todos os sorteados, inclusive quem não clicou. A diferença contra o controle é o efeito. |
| 2 | "O teste foi por push e e-mail. Por que o WhatsApp e o CS teriam o mesmo efeito?" | Rita Fontes, Patrícia | Slide 6, risco 3; documento de estratégia, seção 5.3 | Não sabemos ainda. Por isso há *holdout* de 10% nos envios de novembro e recalibração na semana 3. O uplift de CS está marcado como estimativa. |
| 3 | "De onde vem o lucro e em qual horizonte?" | Rita Fontes | Matriz 5.1; resumo do case, seção 4 | Mostre a conta: volume × uplift = salvos; receita retida menos desembolso = lucro. Declare o horizonte e apresente o ROI que o grupo confirmou. |
| 4 | "Vale pagar IA para ler textos e imagens?" | Diego Almeida, Rita Fontes | Tech Seção 2.3; `relatorios/simulacao_gemini_crm.json` | PR-AUC sobe de 0,5714 para 0,5986 por R$ 280/mês; mapas de calor por contagem de pixels custam R$ 0. Diga a limitação: texto e imagem foram medidos juntos. |
| 5 | "Se deixarmos 995 clientes em silêncio, não estamos desistindo deles?" | Patrícia, Marcelo | Tabela 4.2, linha de 0 treinos; Slide 2 | Os três tratamentos aumentaram a saída nesse grupo (+6,09 a +9,16 p.p.). Eles pagam cerca de R$ 24,0 mil/mês. O silêncio preserva essa receita; o *kill-switch* garante que ninguém os acione por engano. |

Para ensaiar, use o prompt 2 da Ação 4 do Passo 05 e peça ao agente que faça também estas cinco perguntas, uma de cada vez, avaliando a sua resposta.

### 3. Salvar no GitHub

Cada passo já termina com um commit (última etapa do prompt da Ação 3), então o histórico da sua branch mostra o seu avanço passo a passo. No fechamento, confira se sobrou algo sem commit e envie. O passo a passo completo (branch, commit, push e pull request) está no [`03_GUIA_GIT.md`](./03_GUIA_GIT.md).

```bash
git status                                         # só devem aparecer arquivos da sua pasta em membros/
git add membros/<sua_pasta>/semana_10_A2/          # nunca git add . nem git add -A
git commit -m "docs(membros): revisa os artefatos do A2 no fechamento" -m "- <um tópico por alteração>"
git push origin membros/<seu_nome>                 # envia a sua branch, não a develop
```

Depois do push, abra o pull request da sua branch para a `develop` no GitHub. Se aparecer arquivo fora da sua pasta no `git status`, não o inclua no commit e veja a seção "Quando algo dá errado" do guia.
