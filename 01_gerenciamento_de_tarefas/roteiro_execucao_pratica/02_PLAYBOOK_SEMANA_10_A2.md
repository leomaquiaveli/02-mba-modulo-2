# Playbook 2 — Semana 10 (A2)

> **Projeto:** MBA Inteli Módulo 2 — Case Vitaliza (2º Movimento: AGIR — Submissão 60d `08/12`, Revelação `10/12`, Entrega Final `18/12/2026`)  
> **Ambiente de Dados:** Google BigQuery ([`thermal-origin-470820-e7.vitaliza_inteli_modulo_2`](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2))  
> **Objetivo:** conduzir qualquer integrante do grupo na **construção completa dos seus próprios entregáveis de Negócios (6 Slides do Conselho) e de Tecnologia da Semana 10**, aprendendo na prática como funcionam a **Extração Multimodal com IA Generativa (Texto + Imagens de Mapas de Calor)**, o **Teste de Ablação**, a **Comparação de 4 Algoritmos Supervisionados (Logística, Árvores, Random Forest e Gradient Boosting)**, a **Modelagem Causal de Uplift (Siegel)**, a **Alocação Financeira de Orçamento (Profit Analytics)** e o **Redator Generativo de CRM com Briefing Fechado**.
>
> **Seus arquivos (na sua pasta em `membros/`):**
> * 📊 Negócios A2 (Os 6 Slides do Conselho): `membros/nome_membro_1/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md`
> * 💻 Tecnologia A2 (Multimodal, 4 Modelos 60d, Uplift & Copywriter): `membros/nome_membro_1/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`
>
> **Gabaritos Oficiais do Grupo (apenas para leitura/referência do seu Agente):**
> * [`artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md`](../../artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md)
> * [`artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`](../../artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md)

---

## O que cada passo produz

| Passo | Habilidade Técnica & de Negócio Desenvolvida | O Que Constrói no Seu `ARTEFATO_NEGOCIOS_SEMANA10_A2.md` (6 Slides do Conselho) | O Que Constrói no Seu `ARTEFATO_TECH_SEMANA10_A2.md` (Seções 1 a 4) |
| :--- | :--- | :--- | :--- |
| **Passo 01** | Narrativa Executiva C-Level (Série B) e Avaliação de Arquitetura de Produto (*Win-Back* vs. *Forecasting* vs. *Uplift* frente ao Strava). | **Slide 1:** Diagnóstico do Problema e Série B;<br>**Slide 2:** Os 4 Perfis e os 2 Fatos Vitais (`70,22%` Lojas e `995` *Sleeping Dogs*);<br>**Slide 3:** Caminho A vs. Caminho B vs. Nossa Arquitetura Prescritiva. | **Seção 1:** Arquitetura Ponta a Ponta das 5 Peças na Semana 10 (Diagrama Mermaid integrando Tabelas, Textos, Heatmaps, 4 Modelos e Motor de Uplift/CRM). |
| **Passo 02** | Engenharia de IA Generativa & Visão: Extração com Schema JSON tipado, Contagem de Pixels por Cor vs. VLM em `25.473` PNGs, *Tokenomics* e **Teste de Ablação**. | Insumos de personalização e custo de IA (`R$ 420/mês` no orçamento global). | **Seção 2 Completa (Peça 2 / Obj. 5):** Contratos JSON de Extração, Comparação Pixels (R$ 0) vs. VLM em `heatmaps_90d/` e **Teste de Ablação** (`PR-AUC 0,5714 ➔ 0,5986`, `+2,72 p.p.`). |
| **Passo 03** | Ciência de Dados Supervisionada: comparação *Out-of-Time* entre modelos lineares e ensembles de árvores (**Logística, Árvore, Bagging/RF e Boosting**). | Base preditiva que alimenta a priorização de risco nos Slides 3 e 4. | **Seção 3 Completa (Peça 3 / Obj. 4):** Tabela comparativa das **4 Famílias Supervisionadas (60d)** (`ROC-AUC = 0,7858`, `PR-AUC = 0,5986`, `Lift@10% = 2,96x`). |
| **Passo 04** | Inferência Causal e **Uplift Modeling (Eric Siegel)**: análise de Teste A/B controlado (`campanha_ago26.csv`), isolando *Persuadíveis* e provando os *Sleeping Dogs*. | **Slide 4 Completo:** Prova Causal do Experimento de `10/08/2026` (`14.120` sorteados) — **Tabela 4.1** (Por Plano) e **Tabela 4.2** (Prova Empírica dos *Sleeping Dogs* `+9,16 p.p.` de churn induzido!). | **Seção 4.1 (Peça 4 / Obj. 6):** Algoritmo da Regra Prescritiva de Contato em 5 Regras determinísticas. |
| **Passo 05** | *Profit-Driven Analytics* (Verbeke et al.) e GenAI com Guardrails: alocação ótima de **R$ 40k/mês** (`300 CS` + `1.500 WA`), DRE de **Lucro Líquido (`+R$ 207,8k`)** e **Copywriting com Briefing Fechado**. | **Slide 5 Completo:** Matriz Prescritiva de Alocação Mensal e ROI (`+686%`);<br>**Slide 6 Completo:** Matriz de Riscos, Gatilhos (*Kill-Switch*) e Contingência. | **Seção 4.2 Completa (Peça 5 / Obj. 8):** Exemplos Reais de Saída do Redator Generativo com Briefing Fechado (Exemplos A e B). |

---

## PASSO 01 — Diagnóstico para o Board (Slides 1 e 2) e Comparação Estratégica Caminho A vs. B (Slide 3 + Arquitetura Tech Seção 1)

### O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
Na Semana 10, você não está apresentando um relatório acadêmico: você está no papel da **Camila Ferraz (Head de Dados e IA)** diante do **Conselho de Administração da Vitaliza**, que precisa decidir onde investir para defender o valuation da **Série B** após o anúncio do **Strava Premium** no Brasil.
Existem duas propostas rivais na mesa da diretoria:
* **Caminho A (*Win-Back Reativo* — "O Bombeiro"):** Colocar uma oferta automática quando o cliente clica em *"Cancelar"* no site. **Por que falha sozinho?** Porque **70,22% da base (`10.359` clientes)** assina via App Store ou Google Play e cancela nas configurações do celular, sem nunca passar pelo site da Vitaliza!
* **Caminho B Puro (*Engagement Forecasting* — "O Detector de Fumaça"):** Calcular um score diário de risco de churn e disparar mensagens para todo mundo com risco alto. **Por que é perigoso sozinho?** Porque existem **`995` clientes inativos (`0` treinos) que ainda estão com a renovação ligada pagando `R$ 27,6 mil/mês` por esquecimento (*Sleeping Dogs*)**. Se o Caminho B mandar um alerta para eles, eles se lembram da assinatura e cancelam!
* **Nossa Recomendação (Arquitetura Prescritiva de Uplift):** Une a capacidade preditiva do Caminho B com o **Filtro Causal de Uplift (Siegel)**, agindo nos **Persuadíveis** e mantendo silêncio absoluto nos **Sleeping Dogs**.

---

### Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `assinaturas`, `uso_mensal` e `usuarios`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Para abrirmos a apresentação ao Conselho de Administração da Vitaliza (Slides 1, 2 e 3 da Semana 10), consolide sobre os 14.753 pagantes ativos em 30/09/2026 (cruzando assinaturas e uso_mensal em '2026-09'):
  1. Qual é a Receita Líquida Mensal total e Anualizada (12x) da base pagante, e quantos assinantes (N e %) já desligaram a renovacao_automatica no plano anual e no plano mensal?
  2. Mostre a tabela resumida dos 4 segmentos comportamentais (1. Atletas Sociais de Rua & GPS; 2. Praticantes Regulares Vídeo; 3. Entusiastas Oscilantes 1-4 treinos; 4. Pagantes Inertes 0 treinos) com Volume (N e %), Treinos/Mês e % Renovação Desligada.
  3. Destaque os 2 Fatos Vitais que inviabilizam o Caminho A puro (Win-Back apenas no botão cancelar do site): (a) quantos pagantes (N e %) estão na App Store e Google Play, e (b) quantos inativos com 0 treinos ainda estão com a renovacao_automatica ligada pagando por inércia (Sleeping Dogs) e qual a receita mensal deles.
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  WITH base AS (
    SELECT
      a.user_id,
      a.plano_atual,
      a.canal_cobranca,
      CAST(a.renovacao_automatica AS STRING) IN ('0', 'false', 'False') AS desligou_renovacao,
      COALESCE(um.treinos_mes, 0) AS treinos_mes,
      (CASE WHEN a.plano_atual = 'mensal' THEN 39.90 ELSE 299.90 / 12.0 END) *
      (1.0 - CASE
        WHEN a.canal_cobranca IN ('app_store', 'google_play') THEN 0.15
        WHEN a.canal_cobranca = 'web_cartao' THEN 0.035
        WHEN a.canal_cobranca = 'web_pix' THEN 0.0099
        ELSE 0.0
      END) AS mrr_liquido
    FROM `vitaliza_inteli_modulo_2.assinaturas` a
    LEFT JOIN `vitaliza_inteli_modulo_2.uso_mensal` um ON a.user_id = um.user_id AND um.ano_mes = '2026-09'
    WHERE a.status_atual = 'ativa' AND a.plano_atual IN ('mensal', 'anual')
  )
  SELECT
    COUNT(*) AS total_pagantes_ativos,
    ROUND(SUM(mrr_liquido), 0) AS mrr_liquido_mensal_rs,
    COUNTIF(desligou_renovacao) AS total_ja_desligaram_renovacao,
    COUNTIF(canal_cobranca IN ('app_store', 'google_play')) AS pagantes_lojas_n,
    ROUND(COUNTIF(canal_cobranca IN ('app_store', 'google_play')) * 100.0 / COUNT(*), 2) AS pagantes_lojas_pct,
    COUNTIF(treinos_mes = 0 AND NOT desligou_renovacao) AS sleeping_dogs_n,
    ROUND(SUM(CASE WHEN treinos_mes = 0 AND NOT desligou_renovacao THEN mrr_liquido ELSE 0 END), 0) AS sleeping_dogs_mrr_liquido_rs
  FROM base;
  ```

---

### Ação 2: Conferir o Output na Tela (Gabarito)
* **Estoque de Perda Contratada:** `14.753` pagantes ativos (`R$ 409.941/mês` ou `R$ 4,92 milhões/ano`), com **`2.250` (`15,25%`)** já com renovação desligada (`2.082` no anual e `168` no mensal).
* **Fato Vital 1 (Cegueira das Lojas):** **`10.359` pagantes (`70,22%`)** estão na App Store ou Google Play (o Caminho A só enxerga os `29,78%` do site).
* **Fato Vital 2 (*Sleeping Dogs*):** **`995` inativos (`0` treinos)** ainda estão com renovação ligada pagando **`R$ 27,6 mil/mês`** por esquecimento.

---

### Ação 3: Montar os Slides 1, 2 e 3 + Arquitetura Tech no Seu Agente de Código
```text
Estou construindo os meus entregáveis da Semana 10 (A2) na minha pasta individual `membros/nome_membro_1/semana_10_A2/` (ou na minha pasta personalizada em `membros/`).
Consulte como referência os arquivos oficiais `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`, mas NÃO altere os arquivos da raiz — edite APENAS os arquivos dentro da minha pasta em `membros/`.

Acabei de rodar o Passo 01 no BigQuery e obtive esta resposta:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Com base nessa resposta:
1. No meu arquivo `ARTEFATO_NEGOCIOS_SEMANA10_A2.md`, preencha completos:
   - Slide 1 (Diagnóstico do Problema: Sangria de Receita e o Dilema da Série B);
   - Slide 2 (O Que os Dados Dizem Sobre Quem Cancela: Tabela dos 4 Perfis e os 2 Fatos Vitais);
   - Slide 3 (Tabela Comparativa Caminho A Win-Back vs. Caminho B Puro Engagement Forecasting vs. Nossa Recomendação de Arquitetura Prescritiva de Uplift frente ao Strava).
2. No meu arquivo `ARTEFATO_TECH_SEMANA10_A2.md`, preencha a Seção 1 com o diagrama Mermaid da Arquitetura Ponta a Ponta das 5 Peças na Semana 10.
```

---

### Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Quem São os *Sleeping Dogs* por Plano e Canal?):**
   ```text
   Dentro dos 995 assinantes ativos que tiveram 0 treinos em setembro ('2026-09') mas ainda estão com a renovacao_automatica ligada (os nossos Sleeping Dogs), quantos são do plano anual e quantos são do plano mensal? E qual é a distribuição deles entre App Store, Google Play e Site?
   ```
2. **No Seu Agente do Repositório / NotebookLM (Debatendo Caminho A vs. Caminho B vs. Strava):**
   ```text
   Leia o arquivo `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md` e o Slide 3 de `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md`. Me ajude a montar um argumento executivo de 2 minutos explicando para o Conselho por que o lançamento do Strava Premium no Brasil obriga a Vitaliza a ir além do Win-Back reativo (Caminho A), mas por que o Caminho B puro sem filtro de Uplift daria prejuízo.
   ```

---

## PASSO 02 — Peça 2 (Objetivo 5): Extração Multimodal de Texto e Imagem (`heatmaps_90d/`), Tokenomics e Teste de Ablação

### O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
O Objetivo 5 do case faz uma pergunta muito prática de engenharia de IA: **"Processar textos livres (`onboarding`, `tickets_suporte`, `feed_posts`) e `25.473` imagens de mapas de calor (`heatmaps_90d/`) melhora a previsão de churn o suficiente para pagar o custo dos tokens?"**
Aqui você aprende 3 conceitos modernos de IA Generativa aplicada a Ciência de Dados:
1. **Extração com Schema JSON Fixo (*Structured Outputs*):** Em vez de pedir um resumo aberto ao Gemini, exigimos que ele devolva um JSON tipado com variáveis booleanas e categóricas (`motivacao_onboarding`, `suporte_falha_tecnica_gps`, `feed_mencao_lesao_ou_dor`) que entram direto como colunas na tabela de Machine Learning!
2. **Sistematização Determinística em Imagens (Pixels vs. VLM):** Como os `25.473` mapas de calor de `heatmaps_90d/` usam cores fixas (`verde` = parque, `azul` = água, `areia` = praia, `amarelo` = avenida), contar a proporção de pixels por cor via Python (`Pillow`/`NumPy`) extrai o ambiente de treino e a variação de intensidade (`30/09` vs `31/07`) a **custo R$ 0,00 de API**!
3. **Teste de Ablação (*Ablation Study*):** É o experimento onde treinamos exatamente o mesmo algoritmo (**Gradient Boosting**) duas vezes: primeiro **sem** as colunas de texto/imagem (**Modelo A: `PR-AUC = 0,5714`**) e depois **com** as colunas de texto/imagem (**Modelo B: `PR-AUC = 0,5986`**), provando um ganho real de **`+2,72 p.p.`** por apenas **R$ 280/mês** no lote de 14.753 ativos!

---

### Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `onboarding`, `tickets_suporte` e `feed_posts`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Para a Peça 2 (Objetivo 5 — Extração Multimodal de Texto e Imagem), consulte as bases de texto até '2026-09-30':
  1. Mostre o volume de registros válidos até 30/09/2026 em onboarding, tickets_suporte e feed_posts.
  2. Em tickets_suporte, quantos chamados mencionam falha de GPS/sincronização ou intenção de cancelamento/preço, e quantos estão 'aberto' ou 'sem_resposta'?
  3. Em feed_posts, mostre 5 exemplos reais de posts de usuários que mencionam dor, lesão, pausa ou desânimo nos treinos.
  4. Cruze esses sinais com a tabela assinaturas e mostre como os usuários com ticket pendente ou menção negativa têm maior taxa de saída/desligamento de renovação.
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  -- 1. Volume de textos válidos até o corte de 30/09/2026
  SELECT 'onboarding_ate_corte' AS fonte, COUNT(*) AS registros FROM `vitaliza_inteli_modulo_2.onboarding` WHERE DATE(data_onboarding) <= '2026-09-30'
  UNION ALL
  SELECT 'tickets_suporte_ate_corte', COUNT(*) FROM `vitaliza_inteli_modulo_2.tickets_suporte` WHERE DATE(TIMESTAMP(data_abertura)) <= '2026-09-30'
  UNION ALL
  SELECT 'feed_posts_ate_corte', COUNT(*) FROM `vitaliza_inteli_modulo_2.feed_posts` WHERE TIMESTAMP(data_hora) <= '2026-09-30 23:59:59';

  -- 2. Exemplos de menções a lesão, dor ou pausa no feed_posts
  SELECT user_id, data_hora, texto_post, likes
  FROM `vitaliza_inteli_modulo_2.feed_posts`
  WHERE TIMESTAMP(data_hora) <= '2026-09-30 23:59:59'
    AND REGEXP_CONTAINS(LOWER(texto_post), r'(lesão|lesao|dor|machuquei|ombro|joelho|parado|volto)')
  LIMIT 10;
  ```

---

### Ação 2: Conferir o Output e a Tabela do Teste de Ablação
* **Volumes até o corte:** `onboarding` (`63.929`), `tickets_suporte` (`4.422`), `feed_posts` (`119.309`) e `heatmaps_90d/` (`12.426` PNGs em `31/07` + `13.047` PNGs em `30/09`).
* **Resultado do Teste de Ablação (Gradient Boosting 150 árvores):**
  * **Modelo A (Somente Tabelas e Logs):** `ROC-AUC = 0,7798` | `PR-AUC = 0,5714` | `Brier = 0,1352` | Custo = `R$ 0,00`.
  * **Modelo B (Tabelas + Features Extraídas de Texto/Suporte/Feed + Pixels):** **`ROC-AUC = 0,7858`** | **`PR-AUC = 0,5986` (`+2,72 p.p.`)** | **`Brier = 0,1330`** | Custo = **`R$ 280,00 / mês`**.

---

### Ação 3: Montar a Seção 2 no Seu Agente de Código (Claude Code / Codex / VS Code)
```text
Acabei de rodar o Passo 02 no BigQuery analisando as fontes de texto livre (onboarding, suporte e feed):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência a Seção 2 completa do arquivo oficial `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`, preencha a Seção 2 (Subseções 2.1, 2.2 e 2.3) do meu arquivo `ARTEFATO_TECH_SEMANA10_A2.md` na minha pasta em `membros/` documentando:
- O Schema JSON fixo de extração multimodal (`extracao_texto` e `extracao_heatmap_90d`);
- A comparação técnica e financeira entre Contagem de Pixels por Cor (R$ 0,00) e VLM nos 25.473 PNGs de `heatmaps_90d/`;
- A tabela do Teste de Ablação comprovando o ganho de +2,72 p.p. em PR-AUC (0,5714 para 0,5986) por R$ 280/mês.
```

---

### Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Lendo o Que os Clientes Escrevem Antes de Sair):**
   ```text
   Cruze assinaturas (clientes com renovacao_automatica desligada) com tickets_suporte e feed_posts. Mostre 5 histórias reais de clientes que desligaram a renovação, exibindo o que eles postaram no feed e o que reclamaram no suporte antes de decidir sair.
   ```
2. **No Seu Agente do Repositório / NotebookLM (Entendendo como a IA Analisa Textos e Mapas de Calor):**
   ```text
   Leia o guia `00_comece_por_aqui/03_trilha_ia_generativa_e_multimodal/README.md` e o relatório já pronto em `relatorios/simulacao_gemini_crm.json`. Me explique em linguagem de negócios como os textos do suporte/onboarding e os mapas de calor ajudam a descobrir o motivo real pelo qual o cliente está parando de treinar, e por que gastar R$ 280/mês com essa leitura de IA se paga com folga.
   ```

---

## PASSO 03 — Peça 3 (Objetivo 4): Comparação das 4 Famílias de Modelos Supervisionados em 60 Dias

### O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
No Objetivo 4 completo, o case pede para comparar **4 famílias clássicas de Machine Learning Supervisionado**:
1. **Regressão Logística (Linear):** Soma pesos lineares para cada variável. É fácil de explicar, mas não captura sozinha quando **duas coisas combinadas** explodem o risco (ex.: ser do *Plano Mensal* **E** cair para *1 treino* **E** ter *ticket sem resposta*).
2. **Árvore de Decisão (`max_depth=5`):** Cria regras do tipo `SE treinos < 3 E plano = mensal ENTÃO risco = alto`. Concentra muito bem o topo 10% (`Lift = 2,97x`), mas uma árvore sozinha é instável.
3. **Bagging / Random Forest (`200` árvores em paralelo):** Treina 200 árvores independentes sorteando amostras e tira a média, reduzindo a variância (`ROC-AUC = 0,7850`).
4. **Gradient Boosting + Multimodal (`150` árvores sequenciais):** Cada nova árvore foca em corrigir os erros das árvores anteriores. Combinado com as variáveis extraídas de texto e heatmaps, é o nosso **Modelo Campeão (`ROC-AUC = 0,7858` | `PR-AUC = 0,5986`)**.

---

### Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `assinaturas`, `uso_mensal` e `tickets_suporte`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Para o Objetivo 4 (Classificação Supervisionada de Churn em 60 dias), extraia no BigQuery as regras de negócio não-lineares que diferenciam uma Árvore de Decisão / Gradient Boosting de uma Regressão Logística simples:
  Cruze assinaturas (14.753 pagantes ativos) com uso_mensal ('2026-09') e tickets_suporte. Compare a taxa de desligamento de renovação combinando simultaneamente: Plano (mensal vs anual) x Faixa de Treinos (0, 1-4, 5+) x Presença de Ticket Pendente no Suporte. Mostre como a interação entre essas variáveis concentra o risco no topo 10% da base (cota de 1.500 WhatsApps).
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  WITH suporte AS (
    SELECT user_id, MAX(CASE WHEN status_ticket IN ('aberto', 'sem_resposta') THEN 1 ELSE 0 END) AS ticket_pendente
    FROM `vitaliza_inteli_modulo_2.tickets_suporte`
    WHERE DATE(TIMESTAMP(data_abertura)) <= '2026-09-30'
    GROUP BY 1
  )
  SELECT
    a.plano_atual,
    CASE
      WHEN COALESCE(um.treinos_mes, 0) = 0 THEN '0_treinos'
      WHEN COALESCE(um.treinos_mes, 0) BETWEEN 1 AND 4 THEN '1_a_4_treinos'
      ELSE '5+_treinos'
    END AS faixa_treinos,
    COALESCE(s.ticket_pendente, 0) AS ticket_pendente,
    COUNT(*) AS n_clientes,
    ROUND(AVG(CASE WHEN CAST(a.renovacao_automatica AS STRING) IN ('0', 'false', 'False') THEN 100.0 ELSE 0.0 END), 2) AS pct_saida_desligamento
  FROM `vitaliza_inteli_modulo_2.assinaturas` a
  LEFT JOIN `vitaliza_inteli_modulo_2.uso_mensal` um ON a.user_id = um.user_id AND um.ano_mes = '2026-09'
  LEFT JOIN suporte s ON a.user_id = s.user_id
  WHERE a.status_atual = 'ativa' AND a.plano_atual IN ('mensal', 'anual')
  GROUP BY 1, 2, 3
  ORDER BY pct_saida_desligamento DESC;
  ```

---

### Ação 2: Conferir as Métricas Auditadas das 4 Famílias Supervisionadas
| Família Supervisionada | ROC-AUC | PR-AUC | Brier Score | Lift @ Topo 10% (`1.500` WA) | Papel |
| :--- | ---: | ---: | ---: | ---: | :--- |
| **1. Regressão Logística (Baseline)** | `0,7522` | `0,5079` | `0,1504` | `2,55x` | Referência linear interpretável. |
| **2. Árvore de Decisão (`max_depth=5`)** | `0,7691` | `0,5420` | `0,1372` | **`2,97x`** | Regras de negócio transparentes. |
| **3. Bagging / Random Forest (`200` árvores)** | `0,7850` | `0,5839` | `0,1333` | `2,93x` | Redução de variância em dados tabulares. |
| **4. Gradient Boosting + Multimodal (`150` árvores)** | **`0,7858`** | **`0,5986`** | **`0,1330`** | **`2,96x`** | **Modelo Campeão** em precisão/recall e lucro líquido. |

---

### Ação 3: Montar a Seção 3 no Seu Agente de Código (Claude Code / Codex / VS Code)
```text
Acabei de rodar o Passo 03 no BigQuery verificando as interações não-lineares de risco:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência a Seção 3 do arquivo oficial `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`, preencha a Seção 3 completa do meu arquivo `ARTEFATO_TECH_SEMANA10_A2.md` na minha pasta em `membros/` apresentando a tabela comparativa das 4 famílias supervisionadas (Regressão Logística, Árvore de Decisão, Bagging/Random Forest e Gradient Boosting + Multimodal) com ROC-AUC, PR-AUC, Brier Score e Lift@10%.
```

---

### Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Encontrando o Perfil de Maior Risco da Base Inteira):**
   ```text
   Cruze assinaturas (14.753 pagantes ativos) com uso_mensal ('2026-09'), pagamentos e tickets_suporte. Quais combinações de plano_atual, faixa de treino e problemas de pagamento/suporte têm mais de 40% de renovacao_automatica desligada?
   ```
2. **No Seu Agente do Repositório / NotebookLM (Traduzindo os 4 Algoritmos para Linguagem Executiva):**
   ```text
   Leia o guia `00_comece_por_aqui/02_trilha_ciencia_de_dados_e_ml/02_CLUSTERIZACAO_E_CHURN_SUPERVISIONADO.md` e a Seção 3 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`. Me explique sem jargão matemático a diferença prática entre Regressão Logística, Árvore de Decisão, Random Forest e Gradient Boosting, e por que usamos o critério de lucro líquido em reais (e não só AUC) para escolher o modelo vencedor.
   ```

---

## PASSO 04 — Peça 4 (Objetivo 6): O Experimento de `10/08/2026` (`campanha_ago26`) e a Prova dos *Sleeping Dogs* vs. *Persuadíveis*

### O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
Este é o ponto alto da teoria de **Uplift Modeling (Eric Siegel)**:
* Prever que alguém tem **alto risco de sair** não significa que mandar uma mensagem vai salvar essa pessoa!
* Em `10/08/2026`, a Vitaliza sorteou **`14.120` pagantes** em 4 grupos (`controle`, `desafio`, `cupom`, `conteudo`). Quando cruzamos esse experimento no BigQuery com a frequência de treino no mês anterior ao sorteio (**julho/2026**), descobrimos **a prova matemática dos 4 Quadrantes de Siegel**:
  1. **Nos Inativos (`0` treinos em julho — `N = 2.685`):** Quem ficou no **Controle (sem receber mensagem)** teve **`51,86%`** de saída/desligamento. Mas quem recebeu **Desafio subiu para `61,02%` (`+9,16 p.p.` a mais de cancelamento!)**, quem recebeu **Conteúdo subiu para `60,39%` (`+8,53 p.p.` pior)** e quem recebeu **Cupom subiu para `57,95%` (`+6,09 p.p.` pior)**! Ou seja: **mandar mensagem para quem tem 0 treinos acorda o *Sleeping Dog* e faz a Vitaliza perder dinheiro!**
  2. **Nos Oscilantes (`1 a 4` treinos em julho — `N = 5.241`):** O tratamento reduz a saída de `25,19%` (Controle) para **`20,37%` no Desafio (`+4,82 p.p.` de retenção ganha!)** e **`21,45%` no Cupom (`+3,74 p.p.` ganho)** — e no plano mensal o **Cupom reduz a saída de `17,99%` para `10,63%` (`+7,36 p.p.` de Uplift!)**. Esses são os verdadeiros **Persuadíveis**!

---

### Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `campanha_ago26`, `assinaturas` e `uso_mensal`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Precisamos gerar as duas tabelas oficiais do Slide 4 sobre o experimento controlado de 10/08/2026 (tabela campanha_ago26 com 14.120 sorteados):
  1. Tabela 4.1 (Efeito Causal por Plano — Mensal vs Anual): cruze campanha_ago26 com assinaturas pelo user_id. Para o Plano Mensal (5.779 sorteados) e para o Plano Anual (8.341 sorteados), mostre por grupo (controle, cupom, desafio, conteudo): total de sorteados, taxa de clique (%), churn efetivo até o corte (status_atual != 'ativa') e taxa combinada de saída + renovação desligada, calculando o Uplift em pontos percentuais contra o grupo Controle.
  2. Tabela 4.2 (Prova Empírica dos Sleeping Dogs vs Persuadíveis por Uso Prévio em Julho/2026): cruze campanha_ago26 com assinaturas e com uso_mensal no mês '2026-07' (pré-campanha). Separe os 14.120 sorteados em 3 faixas de treino em julho:
     - '0 treinos no mês' (N = 2.685 — Sleeping Dogs)
     - '1 a 4 treinos no mês' (N = 5.241 — Persuadíveis)
     - '>= 5 treinos no mês' (N = 6.194 — Garantidos)
     Mostre a taxa de saída/desligamento de cada faixa nos grupos Controle, Desafio, Cupom e Conteúdo!
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  -- 1. Tabela 4.1: Efeito causal por plano (Mensal vs Anual)
  SELECT
    a.plano_atual,
    c.grupo,
    COUNT(*) AS assinantes_sorteados,
    ROUND(AVG(CAST(c.clicou AS FLOAT64)) * 100, 2) AS taxa_clique_pct,
    ROUND(AVG(CASE WHEN a.status_atual != 'ativa' THEN 100.0 ELSE 0.0 END), 2) AS churn_efetivo_pct,
    ROUND(AVG(CASE WHEN a.status_atual != 'ativa' OR CAST(a.renovacao_automatica AS STRING) IN ('0', 'false', 'False') THEN 100.0 ELSE 0.0 END), 2) AS saida_mais_renov_desligada_pct
  FROM `vitaliza_inteli_modulo_2.campanha_ago26` c
  JOIN `vitaliza_inteli_modulo_2.assinaturas` a ON c.user_id = a.user_id
  GROUP BY 1, 2
  ORDER BY 1, saida_mais_renov_desligada_pct ASC;

  -- 2. Tabela 4.2: Prova dos Sleeping Dogs vs Persuadíveis (corte por uso em julho/2026)
  WITH uso_julho AS (
    SELECT user_id, treinos_mes
    FROM `vitaliza_inteli_modulo_2.uso_mensal`
    WHERE ano_mes = '2026-07'
  )
  SELECT
    CASE
      WHEN COALESCE(u.treinos_mes, 0) = 0 THEN '1. 0 treinos em jul/26 (Sleeping Dogs)'
      WHEN u.treinos_mes BETWEEN 1 AND 4 THEN '2. 1 a 4 treinos em jul/26 (Persuadiveis)'
      ELSE '3. >= 5 treinos em jul/26 (Garantidos)'
    END AS faixa_engajamento_julho,
    c.grupo,
    COUNT(*) AS n_sorteados,
    ROUND(AVG(CASE WHEN a.status_atual != 'ativa' OR CAST(a.renovacao_automatica AS STRING) IN ('0', 'false', 'False') THEN 100.0 ELSE 0.0 END), 2) AS pct_saida_ou_desligamento
  FROM `vitaliza_inteli_modulo_2.campanha_ago26` c
  JOIN `vitaliza_inteli_modulo_2.assinaturas` a ON c.user_id = a.user_id
  LEFT JOIN uso_julho u ON c.user_id = u.user_id
  GROUP BY 1, 2
  ORDER BY 1, 2;
  ```

---

### Ação 2: Conferir o Output na Tela (Gabarito Slide 4)
* **Tabela 4.1 (No Plano Mensal):**
  * `Controle` (`1.440`): `14,58%` churn efetivo | `17,99%` saída + desligamento.
  * `Cupom` (`1.420`): **`8,94%` churn efetivo | `10,63%` saída + desligamento (`+7,36 p.p.` de Uplift!)**.
  * `Desafio` (`1.456`): **`11,13%` churn efetivo | `12,98%` saída + desligamento (`+5,01 p.p.` de Uplift a custo R$ 0!)**.
  * `Conteúdo` (`1.463`): `13,53%` churn efetivo | `15,79%` saída + desligamento (`+2,20 p.p.`).
* **Tabela 4.2 (Por Uso em Julho/2026 — A Prova dos 4 Quadrantes de Siegel):**
  * **`0` treinos (`N = 2.685` — *Sleeping Dogs*):** `51,86%` no Controle vs. **`61,02%` no Desafio (`+9,16 p.p.` pior!)**, **`57,95%` no Cupom (`+6,09 p.p.` pior)** e **`60,39%` no Conteúdo (`+8,53 p.p.` pior)**!
  * **`1 a 4` treinos (`N = 5.241` — *Persuadíveis*):** Caiu de `25,19%` (Controle) para **`20,37%` no Desafio (`+4,82 p.p.` ganho)** e **`21,45%` no Cupom (`+3,74 p.p.` ganho)**.
  * **`≥ 5` treinos (`N = 6.194` — *Garantidos*):** Caiu de `14,38%` para **`9,70%` no Desafio (`+4,68 p.p.` ganho a custo R$ 0)**.

---

### Ação 3: Montar o Slide 4 e a Seção 4.1 no Seu Agente de Código
```text
Acabei de rodar o Passo 04 no BigQuery e obtive as duas tabelas causais do experimento de 10/08/2026 (Tabela 4.1 por Plano e Tabela 4.2 por Faixa de Uso em Julho):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência o Slide 4 de `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e a Seção 4.1 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`:
1. Preencha o Slide 4 completo (Tabelas 4.1 e 4.2) do meu arquivo `ARTEFATO_NEGOCIOS_SEMANA10_A2.md` na minha pasta em `membros/`;
2. Preencha a Seção 4.1 (Algoritmo da Regra Prescritiva de Contato em 5 regras determinísticas) do meu arquivo `ARTEFATO_TECH_SEMANA10_A2.md`.
```

---

### Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Clicar na Mensagem Significa Ficar na Vitaliza?):**
   ```text
   Na tabela campanha_ago26 cruzada com assinaturas, compare a taxa de clique (clicou = 1) com a taxa real de retenção nos grupos Cupom e Desafio. Por que olhar apenas para a taxa de clique da campanha enganaria a diretoria de marketing?
   ```
2. **No Seu Agente do Repositório / NotebookLM (Dominando os 4 Quadrantes de Siegel):**
   ```text
   Leia o arquivo `00_comece_por_aqui/01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md` e os resultados do Passo 04. Me explique com exemplos práticos da Vitaliza a diferença entre Persuadíveis, Garantidos, Perdidos e Sleeping Dogs, e como essa matriz resolve o conflito entre a CMO (que queria dar cupom para todos) e o CFO (que queria cortar custo).
   ```

---

## PASSO 05 — Peças 4 e 5 (Objetivos 7 e 8): Alocação do Orçamento de R$ 40k (`300 CS` + `1.500 WA`), Lucro Líquido (`+R$ 207,8k`), Copywriter CRM e Contingência

### O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
No último passo do módulo, você conecta a decisão matemática ao mundo real das operações de Growth e CRM:
1. **Otimização sob Restrições Físicas e Financeiras (Objetivo 7):** Temos no máximo **300 atendimentos humanos de CS** (R$ 18/un = R$ 5.400), **1.500 mensagens de WhatsApp** (R$ 0,40/un = R$ 600), E-mail (R$ 0,01) e Push (R$ 0,00), e a soma de tudo (incluindo os descontos de R$ 35,91 no mensal e R$ 25,00 no anual + R$ 420 de tokens de IA) não pode passar de **R$ 40.000/mês**. Nossa regra gasta **R$ 26.441,90/mês** e gera **+R$ 207.840,10 de Lucro Líquido Incremental**!
2. **Copywriting Generativo com Briefing Fechado (Objetivo 8):** O modelo de linguagem (Gemini) **nunca decide se o cliente ganha desconto**. Quem decide o canal e a oferta é a regra determinística da Peça 4. O Gemini recebe um briefing fechado com o nome real do cliente, a meta que ele escreveu no `onboarding.csv`, a modalidade favorita e a oferta exata autorizada, redigindo a mensagem individual sem risco de alucinar promoções!

---

### Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `assinaturas`, `uso_mensal`, `usuarios`, `onboarding`, `tickets_suporte` e `feed_posts`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Para fecharmos o Slide 5 (Alocação de Orçamento R$ 40.000/mês e Lucro Líquido) e a Seção 4.2 (Redator Generativo de CRM), consulte os 14.753 pagantes ativos em 30/09/2026:
  1. Mostre a divisão exata dos 14.753 pagantes ativos nos públicos da nossa Matriz Prescritiva de Alocação:
     - Persuadíveis (1 a 4 treinos em set/26 = 5.391 clientes): sendo 300 no Time de CS (R$ 18/un = R$ 5.400), 750 no WhatsApp com Cupom 30% off 3 meses (R$ 0,40/un + descontos R$ 16.159,50), 750 no WhatsApp com Desafio 6 Semanas (R$ 0,40/un, desconto R$ 0) e o restante em E-mail + Push (R$ 0,01/un)
     - Garantidos (>= 5 treinos = 7.049 clientes): Push Semanal + E-mail com Desafio 6 Semanas (R$ 70,49, proibido cupom)
     - Sleeping Dogs (0 treinos com renovação ligada = 995 clientes): Silêncio Absoluto (R$ 0, evitando +9,16 p.p. de churn induzido).
  2. Extraia também o perfil real do assinante user_id = 'u_2722f848' (e de mais 2 assinantes persuadíveis de 1 a 4 treinos) juntando usuarios, assinaturas, uso_mensal, onboarding e feed_posts para gerarmos os exemplos reais de mensagens personalizadas com briefing fechado!
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  -- Extrair contexto real dos clientes para o Redator Generativo de CRM (Objetivo 8)
  SELECT
    a.user_id,
    u.nome,
    a.plano_atual,
    a.canal_cobranca,
    um.treinos_mes AS treinos_set26,
    ob.texto_onboarding,
    fp.texto_post AS ultimo_post_feed
  FROM `vitaliza_inteli_modulo_2.assinaturas` a
  JOIN `vitaliza_inteli_modulo_2.usuarios` u ON a.user_id = u.user_id
  LEFT JOIN `vitaliza_inteli_modulo_2.uso_mensal` um ON a.user_id = um.user_id AND um.ano_mes = '2026-09'
  LEFT JOIN `vitaliza_inteli_modulo_2.onboarding` ob ON a.user_id = ob.user_id
  LEFT JOIN `vitaliza_inteli_modulo_2.feed_posts` fp ON a.user_id = fp.user_id
  WHERE a.user_id = 'u_2722f848'
     OR (a.status_atual = 'ativa' AND a.plano_atual = 'mensal' AND um.treinos_mes BETWEEN 1 AND 3)
  LIMIT 5;
  ```

---

### Ação 2: Conferir os Números Finais (Slide 5 e Seção 4.2)
* **Custo de Canais + IA:** `R$ 6.532,40` (`R$ 5.400` de 300 CS + `R$ 600` de 1.500 WhatsApps + `R$ 112,40` E-mail/Push + `R$ 420` Tokens LLM).
* **Custo de Descontos Concedidos:** `R$ 19.909,50` (`R$ 3.750` anual + `R$ 16.159,50` mensal).
* **Desembolso Mensal Total:** **`R$ 26.441,90 / mês`** (respeitando com folga o teto de **`R$ 40.000,00 / mês`**).
* **Retorno Financeiro (Objetivo 7):** `~371` saídas evitadas/mês + `85` *Sleeping Dogs* protegidos = **`R$ 234.282,00`** de receita preservada $\rightarrow$ **Lucro Líquido Incremental de `+R$ 207.840,10` (ROI de `+686%`)**.

---

### Ação 3: Fechar os Seus 2 Artefatos da Semana 10 no Agente de Código
```text
Acabei de rodar o Passo 05 no BigQuery consolidando a alocação financeira e os perfis reais para o Redator de CRM:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência os Slides 5 e 6 de `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e a Seção 4.2 de `artefatos_tecnologia/semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md` (sem alterar os arquivos da raiz):
1. No meu arquivo `ARTEFATO_NEGOCIOS_SEMANA10_A2.md` na minha pasta em `membros/`, preencha:
   - Slide 5 (Matriz Prescritiva de Alocação Mensal dentro do orçamento de R$ 40.000/mês, demonstrando o desembolso de R$ 26.441,90 e o Lucro Líquido Incremental de +R$ 207.840,10);
   - Slide 6 (Matriz de Riscos, Kill-Switch de Inatividade, Trava de Orçamento e Plano de Contingência).
2. No meu arquivo `ARTEFATO_TECH_SEMANA10_A2.md` na minha pasta em `membros/`, preencha a Seção 4.2 com os exemplos reais de mensagens geradas pelo Redator Generativo com Briefing Fechado (Exemplo A no mensal com cupom 30% e Exemplo B no anual com lesão leve e pausa/treino adaptado).
Revise os meus dois arquivos de `semana_10_A2/` para garantir que estão completos.
```

---

### Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Criando Mensagens Personalizadas Direto no Chat do BigQuery):**
   ```text
   Escolha 3 clientes reais da tabela assinaturas que estejam no plano mensal, tenham entre 1 e 3 treinos em setembro ('2026-09' na tabela uso_mensal) e tenham texto preenchido na tabela onboarding. Mostre o nome deles, a meta que escreveram no onboarding e escreva uma sugestão de mensagem curta e empática de WhatsApp oferecendo o Desafio de 6 Semanas conectado ao objetivo de cada um.
   ```
2. **No Seu Agente do Repositório / NotebookLM (Simulando a Sabatina do Conselho de Administração):**
   ```text
   Leia o documento `artefatos_negocios/semana_10_A2/ARTEFATO_NEGOCIOS_SEMANA10_A2.md` e o guia `00_comece_por_aqui/01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md`. Simule comigo 3 perguntas difíceis que o CFO (Tomás) e a CMO (Marina) fariam na apresentação final sobre o nosso plano de R$ 26.441,90/mês e me mostre como responder cada uma usando os números que encontramos nos dados.
   ```

---

## Como salvar seus artefatos no GitHub

Ao concluir os passos, envie este pedido ao seu Agente de Código (Claude Code / Codex / VS Code):

```text
Salve no GitHub apenas os arquivos construídos dentro da minha pasta em `membros/`:
1. Verifique no git status que nenhum arquivo fora da minha pasta em `membros/` foi modificado;
2. Faça um commit das minhas alterações e envie para a branch develop (`git pull --rebase origin develop && git push origin develop`).
```
