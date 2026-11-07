# 📘 Playbook 1 — Aprendizado Prático e Construção Guiada da Semana 5 (A1)

> **Projeto:** MBA Inteli Módulo 2 — Case Vitaliza (1º Movimento: ENTENDER — Entrega `13/11/2026`)  
> **Ambiente de Dados:** Google BigQuery ([`thermal-origin-470820-e7.vitaliza_inteli_modulo_2`](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2))  
> **Propósito deste Playbook:** Guiar qualquer integrante do grupo (mesmo sem nenhuma base prévia de programação ou SQL) na **construção completa dos seus próprios entregáveis de Negócios e Tecnologia da Semana 5**, aprendendo na prática como explorar bancos de dados em nuvem, auditar bases sujas, testar hipóteses estatísticas, criar segmentações comportamentais, usar Machine Learning no BigQuery e operar um Agente de Código (**Claude Code / Codex / VS Code**).
>
> **Seus Arquivos de Construção (no seu workspace isolado sem conflito de Git):**
> * 📊 Negócios A1: `membros/nome_membro_1/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md`
> * 💻 Tecnologia A1: `membros/nome_membro_1/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`
>
> **Gabaritos Oficiais do Grupo (apenas para leitura/referência do seu Agente):**
> * [`artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md`](../../artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md)
> * [`artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`](../../artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md)

---

## 🗺️ Mapa de Coerência 1:1 — O Que Você Aprende e Constrói em Cada Passo

| Passo | Habilidade Técnica & de Negócio Desenvolvida | O Que Constrói no Seu `ARTEFATO_NEGOCIOS_SEMANA5_A1.md` | O Que Constrói no Seu `ARTEFATO_TECH_SEMANA5_A1.md` |
| :--- | :--- | :--- | :--- |
| **Passo 01** | Reconciliação de população pagante, cálculo de *Take Rate* / MRR Líquido e detecção de *Churn Diferido* (`renovacao_automatica = 0`). | **Seção 1 & 1.1:** Resumo Executivo, Tabela de Composição (`14.753` pagantes), Assimetria de Lojas (`70,22%`), MRR Líquido (`R$ 409.941/mês`) e Estoque de Saída Contratada (`2.250`). | **Seção 1:** Arquitetura do Pipeline de Engenharia e Reconciliação (`14.813` ativas − `60` cortesias = `14.753` pagantes). |
| **Passo 02** | Auditoria de Qualidade de Dados (*Data Hygiene*): prevenção de *Data Leakage* pós-corte, normalização de fuso horário `UTC ("Z")` vs. `BRT` e padronização de vocabulário em 1,25M de linhas. | **Seção 5.2 (Parte 1):** Limitações Metodológicas e Anomalias Temporais/Categóricas do Pacote Bruto. | **Seção 2 Completa:** Tabela das **7 Anomalias Estruturais** documentadas com volume exato e regra de tratamento. |
| **Passo 03** | Análise Exploratória Diagnóstica (EDA): como confrontar hipóteses executivas com dados reais e separar correlação bivariada de causalidade. | **Seção 2 Completa & Seção 5.2 (Parte 2):** Diagnóstico da Subida do Churn em 2026 (`5,6% ➔ 6,6%`, pico `8,1%` em abril) testando as **5 Hipóteses (`H1` a `H5`)**. | **Seção 1 (Complemento EDA):** Validação estatística das hipóteses diagnósticas do Objetivo 2. |
| **Passo 04** | Clusterização Comportamental sem vazamento de alvo, construção de **Personas com Dados** (vs. personas inventadas) e cálculo de **Receita em Risco** (`Cluster 4A` vs `4B`). | **Seção 3 (Pilar 01):** Os 4 Segmentos Estratégicos;<br>**Seção 4 (Pilar 02):** As 4 Personas de Dados;<br>**Seção 5.1 (Pilar 03):** Valor em Risco Mensal/Anualizado (`4A` [`1.318`] vs `4B` [`995` *Sleeping Dogs*]). | **Seção 3 Completa:** Protocolo Anti-Leakage e Tabela dos 4 Clusters Comportamentais com Centróides (`treinos/mês`, `minutos/mês`) e Taxa de Renovação Desligada *a posteriori*. |
| **Passo 05** | Engenharia de Variáveis Temporais (`M-1` vs `M-2`, `delta_treinos`), validação *Out-of-Time* e avaliação de **Regressão Logística** (`ROC-AUC`, `PR-AUC`, `Brier Score` e `Lift@10%`). | Revisão de coerência final entre os números de Negócios e Tecnologia. | **Seção 4 Completa:** Conjunto de Variáveis (`X`) sem *Data Leakage* e Métricas do Baseline de **Regressão Logística** (`ROC-AUC = 0,7522`, `PR-AUC = 0,5079`, `Brier = 0,1504`, `Lift@10% = 2,55x`). |

---

## 🟢 PASSO 01 — Fotografia Reconciliada da Base (`14.753`), Lojas (`70,22%`), MRR Líquido (`R$ 409.941`) e Saída Contratada (`2.250`)

### 🧠 O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
Em qualquer projeto real de Ciência de Dados e Negócios, o erro mais comum é fazer um `COUNT(*)` simples na tabela de clientes ativos sem verificar:
1. **Quem realmente paga:** Muitas empresas misturam contas de teste, funcionários e influenciadores (`plano_atual = 'cortesia'`) junto com clientes pagantes. Se você não excluir essas contas antes de calcular o churn ou a receita média, todos os denominadores do projeto ficam errados.
2. **Receita Bruta vs. Receita Líquida (*Take Rate*):** Um cliente mensal que paga R$ 39,90 na App Store deixa 15% para a Apple (sobram R$ 33,92 para a Vitaliza), enquanto no Pix pelo site a taxa é de apenas 0,99% (sobram R$ 39,50).
3. **Churn Diferido (*Já Contratado*):** No modelo de assinatura (especialmente anual), o cliente entra nas configurações do iPhone/Android hoje e **desliga a renovação automática (`renovacao_automatica = 0`)**, mas continua com `status_atual = 'ativa'` até o fim do período já pago. Descobrir quantos ativos já desligaram a renovação revela a "perda invisível" que já está contratada!

---

### 🔹 Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
Abra a tabela **`assinaturas`** no [nosso Dataset do BigQuery](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2):

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Na tabela assinaturas, filtre apenas os registros com status_atual igual a 'ativa'.
  1. Primeiro, mostre quantas assinaturas ativas pertencem ao plano_atual = 'cortesia' (canal_cobranca = 'interno') e quantas são assinaturas pagantes reais (planos 'anual' e 'mensal').
  2. Depois, considerando apenas os 14.753 assinantes pagantes ativos (excluindo cortesia), monte uma tabela detalhada agrupada por plano_atual e canal_cobranca contendo:
  - Assinantes Ativos (N)
  - % da Base Pagante (sobre 14.753)
  - Quantos já desligaram a renovacao_automatica (igual a 0 ou false) e o percentual (%)
  - Preço Bruto (anual = R$ 299,90/ano ou R$ 24,991667/mês; mensal = R$ 39,90/mês)
  - Taxa do Canal (app_store e google_play = 15%; web_cartao = 3,5%; web_pix = 0,99%)
  - Receita Líquida Unitária Mensal e Receita Líquida Mensalizada Total de cada linha.
  Inclua os subtotais do Plano Anual, do Plano Mensal e o Total Geral dos 14.753 pagantes.
  ```

* **💻 Query SQL Equivalente (Para você rodar no Editor e aprender como o SQL calcula):**
  ```sql
  -- 1. Reconciliação: 14.813 ativas = 14.753 pagantes + 60 cortesias
  SELECT
    plano_atual,
    canal_cobranca,
    COUNT(*) AS total_ativas,
    COUNTIF(CAST(renovacao_automatica AS STRING) IN ('0', 'false', 'False')) AS renovacao_desligada
  FROM `vitaliza_inteli_modulo_2.assinaturas`
  WHERE status_atual = 'ativa'
  GROUP BY 1, 2
  ORDER BY plano_atual, total_ativas DESC;

  -- 2. Tabela completa da Seção 1.1 (14.753 pagantes ativos)
  WITH base AS (
    SELECT
      plano_atual,
      canal_cobranca,
      COUNT(*) AS assinantes_ativos,
      COUNTIF(CAST(renovacao_automatica AS STRING) IN ('0', 'false', 'False')) AS renovacao_desligada,
      CASE WHEN plano_atual = 'mensal' THEN 39.90 ELSE 299.90 / 12.0 END AS preco_mensal_bruto,
      CASE
        WHEN canal_cobranca IN ('app_store', 'google_play') THEN 0.15
        WHEN canal_cobranca = 'web_cartao' THEN 0.035
        WHEN canal_cobranca = 'web_pix' THEN 0.0099
        ELSE 0.0
      END AS taxa_canal
    FROM `vitaliza_inteli_modulo_2.assinaturas`
    WHERE status_atual = 'ativa' AND plano_atual IN ('mensal', 'anual')
    GROUP BY 1, 2
  )
  SELECT
    plano_atual,
    canal_cobranca,
    assinantes_ativos,
    ROUND(assinantes_ativos * 100.0 / SUM(assinantes_ativos) OVER(), 2) AS pct_base_pagante,
    renovacao_desligada,
    ROUND(taxa_canal * 100, 2) AS taxa_canal_pct,
    ROUND(preco_mensal_bruto * (1 - taxa_canal), 2) AS receita_liquida_unitaria_mes,
    ROUND(assinantes_ativos * preco_mensal_bruto * (1 - taxa_canal), 0) AS receita_liquida_mensalizada
  FROM base
  ORDER BY plano_atual, assinantes_ativos DESC;
  ```
  > **🔎 Entenda o SQL acima em 30 segundos:**  
  > * `WHERE status_atual = 'ativa' AND plano_atual IN ('mensal', 'anual')`: É o filtro que barra as 60 cortesias e as contas canceladas.  
  > * `COUNTIF(...)`: Conta apenas as linhas que atendem à condição (quem está com `renovacao_automatica = 0`).  
  > * `SUM(assinantes_ativos) OVER()`: É uma *Window Function* do SQL que soma o total geral (`14.753`) sem perder o agrupamento de cada linha, permitindo calcular a porcentagem exata de cada canal!

---

### 🔹 Ação 2: Conferir o Output na Tela (Gabarito Oficial)
* **Reconciliação:** `14.813` ativas = **`14.753` pagantes ativos** + **`60` cortesias**.
* **Subtotal Anual:** **`8.478` assinantes (`57,47%`)** $\rightarrow$ `app_store` (`3.047`), `google_play` (`2.928`), `web_cartao` (`1.803`), `web_pix` (`700`) $\rightarrow$ Receita Líquida Mensalizada = **`R$ 187.732,00 / mês`**.
* **Subtotal Mensal:** **`6.275` assinantes (`42,53%`)** $\rightarrow$ `app_store` (`2.348`), `google_play` (`2.036`), `web_cartao` (`1.191`), `web_pix` (`700`) $\rightarrow$ Receita Líquida Mensalizada = **`R$ 222.209,00 / mês`**.
* **Total Geral Pagantes:** **`14.753` (`100%`)**, sendo **70,22% (`10.359`) nas Lojas** e **29,78% (`4.394`) no Site**, com Receita Líquida Total de **`R$ 409.941,00 / mês`**.
* **Alerta de Saída Contratada:** **`2.250` pagantes ativos (`15,25%`)** já desligaram a renovação automática (`2.082` no anual e `168` no mensal).

---

### 🔹 Ação 3: Montar a Seção no Seu Agente de Código (Claude Code / Codex / VS Code)
Copie a resposta que o Agente do BigQuery gerou e envie este comando ao seu Agente de Código:

```text
Estou construindo os meus entregáveis da Semana 5 na minha pasta individual `membros/nome_membro_1/semana_5_A1/` (ou na minha pasta personalizada em `membros/`).
Consulte como referência de estrutura e formatação os arquivos oficiais `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` e `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`, mas NÃO altere os arquivos da raiz — edite APENAS os arquivos dentro da minha pasta em `membros/`.

Acabei de rodar o Passo 01 no BigQuery e obtive esta resposta:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Com base nessa resposta:
1. Preencha a Seção 1 e a Seção 1.1 do meu arquivo `ARTEFATO_NEGOCIOS_SEMANA5_A1.md` com o resumo executivo, a tabela completa aberta por plano e canal (com subtotais Anual R$ 187.732, Mensal R$ 222.209 e Total R$ 409.941/mês) e o callout de alerta sobre os 2.250 assinantes (15,25%) que já desligaram a renovação automática.
2. Preencha a Seção 1 do meu arquivo `ARTEFATO_TECH_SEMANA5_A1.md` com o diagrama Mermaid da arquitetura do pipeline de engenharia das 13 fontes e a reconciliação das 14.813 ativas em 14.753 pagantes + 60 cortesias.
```

---

### 💡 Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
Quer aprofundar seu entendimento neste Passo 01 sem precisar mexer em código? Use estes prompts para conversar com o **Agente do BigQuery** ou com o seu **Agente do Repositório (Claude Code / Codex / NotebookLM)**:

1. **No Agente do BigQuery (Descobrindo o "Paradoxo do Início" nos Novatos):**
   ```text
   Dentro dos 14.753 pagantes ativos da tabela assinaturas, calcule o tempo de casa em meses de cada cliente até '2026-09-30' (usando data_inicio). Compare a taxa de renovacao_automatica desligada entre: (a) Novatos de até 1 mês de casa, (b) Clientes de 2 a 5 meses e (c) Veteranos de 6 meses ou mais. Onde está concentrado o maior risco inicial?
   ```
2. **No Seu Agente do Repositório / NotebookLM (Debatendo Estratégia como um Executivo):**
   ```text
   Leia o documento `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md` e o resultado que acabei de encontrar no Passo 01 (70,22% da base nas lojas App Store/Google Play e 2.250 clientes que já desligaram a renovação automática). Me explique por que essa fotografia da base derruba o argumento de criar apenas uma tela de desconto no botão "Cancelar" do site e quais perguntas um conselheiro faria para o CEO da Vitaliza.
   ```

---

## 🟢 PASSO 02 — Auditoria das 7 Anomalias Estruturais do Data Room (*Data Hygiene*)

### 🧠 O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
Bases de dados reais nunca vêm prontas para Machine Learning. Os professores inseriram **7 armadilhas reais de engenharia de dados** no pacote dos Exhibits para testar se a equipe audita os arquivos antes de modelar:
* Se você usar registros com data de **outubro/2026 ou 2027** em um corte de `30/09/2026`, você comete **Vazamento Temporal (*Data Leakage*)**.
* Se você não converter os eventos das lojas terminados em `"Z"` (`UTC`) para o fuso de Brasília (`UTC-3`), todo evento ocorrido entre 21h e 23h59 do dia `30/09` cai no mês de outubro!
* Se você não padronizar `android`/`Android` ou `corrida`/`run`, qualquer agrupamento ou gráfico divide a mesma categoria ao meio.

---

### 🔹 Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas utilizadas no BigQuery:** `usuarios`, `feed_posts`, `amizades`, `eventos_assinatura` e `atividades`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Faça uma auditoria técnica nas tabelas usuarios, feed_posts, amizades, eventos_assinatura e atividades para documentarmos as anomalias estruturais do Data Room:
  1. Registros pós-corte (> '2026-09-30'): quantos registros existem após 30/09/2026 em usuarios (data_cadastro), feed_posts (data_hora) e amizades (data_amizade)?
  2. Fuso horário UTC vs Brasília: quantos eventos existem em eventos_assinatura terminados em 'Z' (UTC das lojas) e quantos treinos na tabela atividades caíram na primeira hora de '2026-10-01' em UTC mas aconteceram na noite de '2026-09-30' no horário de Brasília (America/Sao_Paulo)?
  3. Despadronização de Sistema Operacional em usuarios: mostre a contagem de cada grafia bruta na coluna sistema (android, Android, ios, iOS, IOS) e o total unificado para Android e iOS.
  4. Modalidades bilíngues na tabela atividades (1.254.475 treinos): mostre a contagem de cada modalidade bruta (corrida, run, caminhada, walk, forca, strength, pedal, ride, funcional, yoga, hiit) e a soma unificando Português + Inglês.
  5. String 'nenhum' em relogio_conectado na tabela usuarios: mostre quantos usuários têm o texto 'nenhum' versus quantos possuem relógio conectado real.
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  -- 1. Registros posteriores ao corte de 30/09/2026
  SELECT 'usuarios_pos_corte' AS anomalia, COUNT(*) AS qtd FROM `vitaliza_inteli_modulo_2.usuarios` WHERE DATE(data_cadastro) > '2026-09-30'
  UNION ALL
  SELECT 'feed_posts_pos_corte', COUNT(*) FROM `vitaliza_inteli_modulo_2.feed_posts` WHERE TIMESTAMP(data_hora) > '2026-09-30 23:59:59'
  UNION ALL
  SELECT 'amizades_pos_corte', COUNT(*) FROM `vitaliza_inteli_modulo_2.amizades` WHERE DATE(data_amizade) > '2026-09-30';

  -- 2. Despadronização de Sistema Operacional em usuarios.csv
  SELECT
    sistema AS grafia_bruto,
    LOWER(TRIM(sistema)) AS sistema_unificado,
    COUNT(*) AS qtd_linhas
  FROM `vitaliza_inteli_modulo_2.usuarios`
  GROUP BY 1, 2
  ORDER BY sistema_unificado, qtd_linhas DESC;

  -- 3. Modalidades bilíngues (PT/EN) em atividades.parquet (1.254.475 treinos)
  SELECT
    modalidade AS modalidade_bruta,
    CASE
      WHEN modalidade IN ('corrida', 'run') THEN 'corrida + run'
      WHEN modalidade IN ('caminhada', 'walk') THEN 'caminhada + walk'
      WHEN modalidade IN ('forca', 'strength') THEN 'forca + strength'
      WHEN modalidade IN ('pedal', 'ride') THEN 'pedal + ride'
      ELSE modalidade
    END AS modalidade_unificada,
    COUNT(*) AS qtd_treinos
  FROM `vitaliza_inteli_modulo_2.atividades`
  GROUP BY 1, 2
  ORDER BY modalidade_unificada, qtd_treinos DESC;
  ```

---

### 🔹 Ação 2: Conferir o Output na Tela (Gabarito das 7 Anomalias)
1. **Cortesias misturadas às ativas:** `60` linhas em `assinaturas.csv`.
2. **Registros pós-corte (`> 30/09/2026`):** `119` usuários, `122` posts e `273` amizades.
3. **Mistura de Fusos (`UTC` vs. `BRT`):** Eventos das lojas em `"Z"` + `34` treinos na 1ª hora de `01/10 UTC` que ocorreram na noite de `30/09 BRT`.
4. **Sistema Operacional despadronizado (`64.948` linhas):** `android` (`28.027`) + `Android` (`7.124`) = **`35.151`**; `ios` (`20.854`) + `iOS` (`7.463`) + `IOS` (`1.480`) = **`29.797`**.
5. **Modalidades bilíngues em `atividades.parquet` (`1.254.475` treinos):** `corrida` (`223.818`) + `run` (`162.108`) = **`385.926`**; `caminhada` (`118.024`) + `walk` (`88.509`) = **`206.533`**; `forca` (`112.704`) + `strength` (`85.548`) = **`198.252`**; `pedal` (`53.740`) + `ride` (`40.765`) = **`94.505`**; `funcional` (`145.476`); `yoga` (`113.849`); `hiit` (`109.934`).
6. **String `'nenhum'` em `relogio_conectado`:** Exige filtro explícito `LOWER(relogio_conectado) != 'nenhum'`.
7. **Estado sobrescrito em `assinaturas.csv`:** Exige reconstrução via `eventos_assinatura.csv` para cortes históricos.

---

### 🔹 Ação 3: Montar a Seção no Seu Agente de Código (Claude Code / Codex / VS Code)
```text
Acabei de rodar o Passo 02 no BigQuery e obtive os números das anomalias estruturais do Data Room:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência a Seção 2 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md` e a Seção 5.2 de `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` (sem alterar os arquivos da raiz):
1. Preencha a Seção 2 do meu arquivo `ARTEFATO_TECH_SEMANA5_A1.md` na minha pasta em `membros/` com a tabela completa das 7 anomalias estruturais detectadas, o volume exato afetado e a regra de engenharia implementada.
2. Preencha a Seção 5.2 (Limitações Explícitas da Análise) do meu arquivo `ARTEFATO_NEGOCIOS_SEMANA5_A1.md`.
```

---

### 💡 Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Qual Modalidade de Treino MaisEngaja os Clientes?):**
   ```text
   Na tabela atividades (unificando corrida com run, caminhada com walk, forca com strength e pedal com ride), mostre o ranking das modalidades mais praticadas na Vitaliza com total de treinos, média de duração em minutos e quantos usuários únicos praticam cada uma.
   ```
2. **No Seu Agente do Repositório / NotebookLM (Entendendo o Impacto das "Pegadinhas" no Negócio):**
   ```text
   Leia o documento `00_comece_por_aqui/05_DOSSIE_EXHIBITS_M2.md` e o `00_comece_por_aqui/05_DOSSIE_DICIONARIO_DE_DADOS_M2.md`. Me explique de forma executiva (sem termos técnicos pesados) que erro de decisão a diretoria da Vitaliza cometeria se analisasse os arquivos brutos sem filtrar as 60 cortesias, sem corrigir o fuso horário das lojas e sem separar a palavra 'nenhum' na coluna de relógio conectado.
   ```

---

## 🟢 PASSO 03 — Diagnóstico da Subida do Churn em 2026: Testando as 5 Hipóteses (`H1` a `H5`)

### 🧠 O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
Na reunião da diretoria da Vitaliza (descrita no Enunciado), cada diretor tinha um palpite sobre por que o churn subiu de **5,6% (2025) para 6,6% (2026)**: uns culpavam o aumento de preço de março, outros culpavam a falta de engajamento ou falhas técnicas.
Aqui você aprende a técnica executiva de **Teste Estruturado de Hipóteses (`Dado vs. Hipótese + Limite Metodológico`)**: para cada hipótese, buscamos a prova nos dados, mas também declaramos o que o dado **não** prova sozinho (ex.: `pesquisa_saida.csv` mostra 41% de reclamação de preço, mas só existe no site e sofre de viés de autosseleção).

---

### 🔹 Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `eventos_assinatura`, `assinaturas`, `pesquisa_saida`, `uso_mensal`, `amizades`, `pagamentos` e `tickets_suporte`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Precisamos testar as 5 hipóteses de negócio para explicar por que o churn mensal subiu de 5,6% (2025) para 6,6% (2026, com pico de 8,1% em abril):
  - H1 (Reajuste do Mensal em 01/03/2026 para R$ 39,90): na tabela pesquisa_saida (643 respostas), quantas e qual o % citam 'preco' como motivo_principal? E na evolução de eventos_assinatura, como se comportaram as saídas em abril de 2026?
  - H2 (Assimetria de Canal - Lojas): qual o % dos 14.753 pagantes ativos que pagam por app_store ou google_play, onde a tela de cancelamento do site não alcança?
  - H3 (Queda de Frequência de Treino): cruzando os 14.753 pagantes ativos de assinaturas com uso_mensal em '2026-09', qual é a taxa de renovacao_automatica desligada (%) para quem treinou >= 5 vezes no mês, para quem treinou de 1 a 4 vezes e para quem teve 0 treinos?
  - H4 (Rede Social e Relógio Conectado): qual o total de vínculos em amizades (até 30/09/2026) e qual a diferença na taxa de renovação desligada entre quem possui relógio conectado (Garmin/Apple Watch) versus quem tem 'nenhum'?
  - H5 (Churn Involuntário e Suporte Técnico): na tabela tickets_suporte (4.422 chamados até 30/09/2026), qual o % de tickets com status 'resolvido', 'aberto' e 'sem_resposta'? E na tabela pagamentos, quantas cobranças foram recusadas?
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  -- H1: Motivos na pesquisa de saída (643 respostas)
  SELECT motivo_principal, COUNT(*) AS mencoes, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct
  FROM `vitaliza_inteli_modulo_2.pesquisa_saida`
  GROUP BY 1 ORDER BY mencoes DESC;

  -- H3 e H4: Taxa de renovação desligada por faixa de treino em set/2026 e posse de relógio
  SELECT
    CASE
      WHEN COALESCE(um.treinos_mes, 0) >= 5 THEN '1. 5+ treinos/mes'
      WHEN COALESCE(um.treinos_mes, 0) BETWEEN 1 AND 4 THEN '2. 1 a 4 treinos/mes'
      ELSE '3. 0 treinos/mes'
    END AS faixa_frequencia_set26,
    COUNT(*) AS pagantes_ativos,
    ROUND(AVG(CASE WHEN CAST(a.renovacao_automatica AS STRING) IN ('0', 'false', 'False') THEN 100.0 ELSE 0.0 END), 2) AS pct_renovacao_desligada,
    ROUND(AVG(CASE WHEN LOWER(u.relogio_conectado) NOT IN ('nenhum', '') THEN 100.0 ELSE 0.0 END), 2) AS pct_com_relogio
  FROM `vitaliza_inteli_modulo_2.assinaturas` a
  JOIN `vitaliza_inteli_modulo_2.usuarios` u ON a.user_id = u.user_id
  LEFT JOIN `vitaliza_inteli_modulo_2.uso_mensal` um ON a.user_id = um.user_id AND um.ano_mes = '2026-09'
  WHERE a.status_atual = 'ativa' AND a.plano_atual IN ('mensal', 'anual')
  GROUP BY 1 ORDER BY 1;

  -- H5: Status dos 4.422 chamados em tickets_suporte
  SELECT status_ticket, COUNT(*) AS qtd, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct
  FROM `vitaliza_inteli_modulo_2.tickets_suporte`
  WHERE DATE(TIMESTAMP(data_abertura)) <= '2026-09-30'
  GROUP BY 1 ORDER BY qtd DESC;
  ```

---

### 🔹 Ação 2: Conferir o Output na Tela (Gabarito `H1` a `H5`)
* **H1 (Preço/Reajuste):** Pico de **8,1% em abril/2026** (`1.154` saídas); na `pesquisa_saida.csv`, **`preco` = `41,06%` (`264` de `643` respostas)**.
* **H2 (Assimetria Lojas):** **`70,22%` (`10.359`)** nas lojas (`app_store` + `google_play`).
* **H3 (Frequência):** `≥5` treinos = apenas **`1,60%`** de renovação desligada; `1 a 4` treinos = **`15,19%`**; `0` treinos = **`56,98%`**!
* **H4 (Social/Relógio):** `113.480` relações em `amizades.csv` e ~40% com relógio conectado protegendo a retenção.
* **H5 (Suporte/Pagamentos):** Dos `4.422` tickets, **`65,97%` resolvidos**, **`22,18%` abertos** e **`11,85%` sem resposta** (`34,03%` pendentes!).

---

### 🔹 Ação 3: Montar a Seção no Seu Agente de Código (Claude Code / Codex / VS Code)
```text
Acabei de rodar o Passo 03 no BigQuery testando as 5 hipóteses da subida do churn em 2026:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência a Seção 2 de `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md`, preencha a Seção 2 completa do meu arquivo `ARTEFATO_NEGOCIOS_SEMANA5_A1.md` na minha pasta em `membros/` montando a matriz das 5 Hipóteses (H1 a H5) com a evidência empírica auditada, a conclusão diagnóstica e o limite metodológico de cada uma.
```

---

### 💡 Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Testando o Conceito de "Gêmeo Demográfico" da Aula 3 de Negócios):**
   ```text
   Cruze usuarios, assinaturas e uso_mensal ('2026-09'). Filtre apenas clientes com a mesma idade (entre 26 e 30 anos) e mesmo gênero. Agora compare a taxa de renovacao_automatica desligada de quem treina 8 ou mais vezes no mês contra quem treina apenas 1 vez no mês. O que isso mostra sobre segmentar por idade versus segmentar por comportamento?
   ```
2. **No Seu Agente do Repositório / NotebookLM (Conectando a Aula 1 e a Aula 3 com o Case):**
   ```text
   Leia o arquivo `00_comece_por_aqui/06_CADERNO_DE_HIPOTESES_ANALITICAS.md` e o `00_comece_por_aqui/03_GUIA_AULA_01_NEGOCIOS_E_TECNOLOGIA.md`. Com base nos números que encontramos nas 5 hipóteses (H1 a H5), me ajude a construir um argumento executivo mostrando por que o aumento de preço de março foi o gatilho, mas a falta de hábito (< 5 treinos/mês) é a causa raiz do cancelamento.
   ```

---

## 🟢 PASSO 04 — Os 4 Segmentos Estratégicos (Pilar 01), Personas de Dados (Pilar 02) e Receita em Risco com `4A` vs. `4B` (Pilar 03)

### 🧠 O Que Você Vai Aprender Neste Passo (O Coração da Nota da Semana 5!)
Este passo cobre os **3 Pilares Obrigatórios da Entrega A1 de Negócios** e o **Objetivo 3 de Tecnologia**:
1. **Regra de Ouro da Clusterização (Sem Vazamento):** Você nunca coloca a coluna `churn` / `renovacao_automatica` dentro das variáveis que formam os grupos. Os grupos são formados exclusivamente pelo **comportamento no produto** (quantas vezes treina, quantos minutos, se treina ao ar livre com GPS ou em casa por vídeo). Só depois que os 4 grupos estão prontos é que olhamos a taxa de saída de cada um!
2. **Os 5 Critérios de Kotler (Aula 3):** Todo segmento precisa ser *Mensurável, Substancial, Diferenciável, Acessível e Acionável*.
3. **A Divisão Crítica do Cluster 4 (`4A` vs. `4B`):** Entre os `2.313` inativos (`0` treinos em setembro), `1.318` (`4A`) já desligaram a renovação automática, mas **`995` (`4B`) ainda estão com a renovação ligada pagando R$ 27.607/mês por esquecimento**. Esses `995` são os **Sleeping Dogs**: se você mandar um WhatsApp dizendo *"Sentimos sua falta!"*, você lembra o cliente de que ele está pagando sem usar e ele cancela na hora!

---

### 🔹 Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `assinaturas` + `uso_mensal` + `usuarios`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Cruze os 14.753 pagantes ativos da tabela assinaturas (status_atual = 'ativa' e plano_atual IN ('mensal', 'anual')) com a tabela uso_mensal no mês '2026-09' e com a tabela usuarios pelo user_id.
  1. Primeiro, agrupe os 14.753 pagantes nos 4 Clusters Comportamentais (sem usar a variável de saída na definição dos grupos):
     - Cluster 1 (Atletas Sociais de Rua & GPS): treinos_mes >= 5 e atividades_ar_livre >= (treinos_mes / 2)
     - Cluster 2 (Praticantes Regulares Indoor & Vídeo): treinos_mes >= 5 e atividades_ar_livre < (treinos_mes / 2)
     - Cluster 3 (Entusiastas Oscilantes / Em Risco): treinos_mes entre 1 e 4
     - Cluster 4 (Pagantes Inertes / 0 treinos): treinos_mes = 0 (ou sem registro em set/26)
     Mostre para cada Cluster: tamanho (N), % da base, média de treinos_mes, média de minutos_mes, % de renovacao_automatica desligada (observada a posteriori) e Receita Líquida Mensal Total.
  2. Depois, para montarmos a Matriz de Valor em Risco (Pilar 03), divida o Cluster 4 (2.313 inativos) em dois subgrupos:
     - Cluster 4A (Inertes que JÁ desligaram a renovação automática = 1.318 clientes)
     - Cluster 4B (Inertes que ainda estão com renovação automática LIGADA pagando por esquecimento = 995 Sleeping Dogs)
     Mostre a Receita Líquida Mensal e Anualizada (12x) em risco de cada grupo.
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  WITH base_clusters AS (
    SELECT
      a.user_id,
      CAST(a.renovacao_automatica AS STRING) IN ('0', 'false', 'False') AS desligou_renovacao,
      COALESCE(um.treinos_mes, 0) AS treinos_mes,
      COALESCE(um.minutos_mes, 0) AS minutos_mes,
      (CASE WHEN a.plano_atual = 'mensal' THEN 39.90 ELSE 299.90 / 12.0 END) *
      (1.0 - CASE
        WHEN a.canal_cobranca IN ('app_store', 'google_play') THEN 0.15
        WHEN a.canal_cobranca = 'web_cartao' THEN 0.035
        WHEN a.canal_cobranca = 'web_pix' THEN 0.0099
        ELSE 0.0
      END) AS receita_liquida_mes,
      CASE
        WHEN COALESCE(um.treinos_mes, 0) >= 5 AND COALESCE(um.atividades_ar_livre, 0) >= COALESCE(um.treinos_mes, 0) / 2.0
          THEN '1. Atletas Sociais de Rua & GPS'
        WHEN COALESCE(um.treinos_mes, 0) >= 5
          THEN '2. Praticantes Regulares Indoor & Video'
        WHEN COALESCE(um.treinos_mes, 0) BETWEEN 1 AND 4
          THEN '3. Entusiastas Oscilantes (1-4 treinos)'
        ELSE '4. Pagantes Inertes (0 treinos)'
      END AS cluster_estrategico
    FROM `vitaliza_inteli_modulo_2.assinaturas` a
    LEFT JOIN `vitaliza_inteli_modulo_2.uso_mensal` um
      ON a.user_id = um.user_id AND um.ano_mes = '2026-09'
    WHERE a.status_atual = 'ativa' AND a.plano_atual IN ('mensal', 'anual')
  )
  SELECT
    cluster_estrategico,
    COUNT(*) AS tamanho_n,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct_da_base,
    ROUND(AVG(treinos_mes), 1) AS treinos_mes_medio,
    ROUND(AVG(minutos_mes), 1) AS minutos_mes_medio,
    COUNTIF(desligou_renovacao) AS qtd_renovacao_desligada,
    ROUND(AVG(CASE WHEN desligou_renovacao THEN 100.0 ELSE 0.0 END), 2) AS pct_renovacao_desligada,
    ROUND(SUM(receita_liquida_mes), 0) AS receita_liquida_mensal_total,
    ROUND(SUM(CASE WHEN desligou_renovacao THEN receita_liquida_mes ELSE 0.0 END), 0) AS receita_mensal_em_risco_direto
  FROM base_clusters
  GROUP BY 1
  ORDER BY 1;
  ```

---

### 🔹 Ação 2: Conferir o Output na Tela (Gabarito)
* **Cluster 1 (`4.089` | `27,72%`):** `12,4` treinos/mês, `615,4` min, **`1,61%`** renovação desligada, Receita Líquida = **`R$ 113.633 / mês`**.
* **Cluster 2 (`2.960` | `20,06%`):** `11,9` treinos/mês, `433,5` min, **`1,59%`** renovação desligada, Receita Líquida = **`R$ 82.258 / mês`**.
* **Cluster 3 (`5.391` | `36,54%`):** `2,2` treinos/mês, `99,3` min, **`15,19%` (`819` clientes)** renovação desligada, Receita Líquida = **`R$ 149.816 / mês`** (Receita em risco direto = **`R$ 22.757/mês` ou `R$ 273.084/ano`**).
* **Cluster 4 (`2.313` | `15,68%`):** `0,0` treinos/mês, **`56,98%`** renovação desligada, Receita Líquida = **`R$ 64.234 / mês`**, dividido em:
  * **Cluster 4A (`1.318` com renovação desligada):** **`R$ 36.627/mês` (`R$ 439.524/ano`)**;
  * **Cluster 4B (`995` *Sleeping Dogs* com renovação ligada):** **`R$ 27.607/mês` (`R$ 331.284/ano`)**.

---

### 🔹 Ação 3: Montar as Seções no Seu Agente de Código (Claude Code / Codex / VS Code)
```text
Acabei de rodar o Passo 04 no BigQuery e obtive a tabela oficial dos 4 Clusters e a abertura do Valor em Risco (incluindo Cluster 4A e 4B):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência as Seções 3, 4 e 5.1 de `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` e a Seção 3 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md` (sem alterar os arquivos da raiz):
1. No meu arquivo `ARTEFATO_NEGOCIOS_SEMANA5_A1.md` dentro da minha pasta em `membros/`, preencha:
   - Seção 3 (Pilar 01 — Segmentação Estratégica Comportamental, incluindo o diagrama Mermaid e a Tabela Consolidada dos 4 Segmentos);
   - Seção 4 (Pilar 02 — Criação das 4 Personas Baseadas em Dados com quem é, por que sai e custo da perda);
   - Seção 5.1 (Pilar 03 — Tabela de Cálculo do Valor em Risco Mensal e Anualizado separando Cluster 3, Cluster 4A, Cluster 4B Sleeping Dogs e Clusters 1/2).
2. No meu arquivo `ARTEFATO_TECH_SEMANA5_A1.md` dentro da minha pasta em `membros/`, preencha a Seção 3 completa (Protocolo de Prevenção de Vazamento e Tabela de Centróides dos 4 Clusters).
```

---

### 💡 Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Conhecendo Histórias Reais Dentro de Cada Persona):**
   ```text
   Cruze assinaturas, usuarios, uso_mensal ('2026-09') e onboarding. Mostre o perfil real de 2 clientes do Cluster 1 (Atletas GPS) e de 2 clientes do Cluster 3 (Entusiastas Oscilantes de 1 a 4 treinos), trazendo o texto_onboarding original que eles escreveram quando entraram na Vitaliza e quantos treinos fizeram em julho, agosto e setembro.
   ```
2. **No Seu Agente do Repositório / NotebookLM (Avaliando os 4 Segmentos pelos 5 Critérios de Kotler):**
   ```text
   Leia o arquivo `00_comece_por_aqui/01_trilha_negocios_e_crm/01_DIAGNOSTICO_ESTRATEGICO_A1_SEMANA5.md` e avalie os nossos 4 segmentos (Atletas GPS, Praticantes Vídeo, Entusiastas Oscilantes e Pagantes Inertes) segundo os 5 critérios clássicos de segmentação vistos em aula (Mensurável, Substancial, Diferenciável, Acessível e Acionável). Qual ação concreta de produto ou CRM faz sentido para cada um?
   ```

---

## 🟢 PASSO 05 — Feature Store Tabular (`M-1` vs. `M-2`) e Baseline Supervisionado de Regressão Logística (60 Dias)

### 🧠 O Que Você Vai Aprender Neste Passo (Por Que Isso Importa)
Para prever quem vai sair nos próximos 60 dias (**Objetivo 4**), o modelo não pode olhar apenas para uma fotografia estática: ele precisa capturar **a velocidade da queda de hábito (`delta_treinos = treinos_m1 - treinos_m2`)**.
Além disso, você aprende as **4 métricas que todo executivo e cientista de dados usa para avaliar um classificador de churn**:
* **`ROC-AUC` (`0,7522` no nosso Baseline):** Capacidade global de ranquear um cliente que vai sair acima de um cliente que vai ficar (`0,50` = cara ou coroa; `1,00` = perfeito).
* **`PR-AUC` (`0,5079`):** Foco em precisão e cobertura na classe minoritária (quem realmente sai).
* **`Brier Score` (`0,1504`):** Mede se a probabilidade prevista (ex.: 30% de chance de sair) é calibrada com a realidade (quanto menor, melhor).
* **`Lift no Topo 10%` (`2,55x`):** Como só temos **1.500 mensagens de WhatsApp por mês** (~10% dos 14.753 ativos), o `Lift@10% = 2,55x` mostra que abordar o topo 10% do ranking do modelo encontra **2,55 vezes mais cancelamentos reais** do que escolher 1.500 clientes por sorteio!

---

### 🔹 Ação 1: Executar no Google BigQuery (Agente Conversacional ou SQL)
* **Tabelas no BigQuery:** `assinaturas`, `usuarios`, `uso_mensal`, `amizades`, `tickets_suporte` e `pagamentos`

* **💬 Prompt Principal para colar no Agente do BigQuery:**
  ```text
  Para o Objetivo 4 Inicial (Seção 4 do Artefato de Tecnologia da Semana 5), monte a consulta da Feature Store Tabular sem Data Leakage para os 14.753 pagantes ativos, calculando as variáveis explicativas (X):
  - Contrato e canal: is_mensal (1 se mensal, 0 se anual) e is_loja (1 se app_store/google_play, 0 se site)
  - Engajamento longitudinal: treinos_m1, minutos_m1, dias_ativos_m1, sessoes_m1 (no mês M-1) e treinos_m2 (no mês M-2), além de delta_treinos = treinos_m1 - treinos_m2 (desaceleração recente de hábito)
  - Ecossistema e fricção: tem_relogio (Garmin/Apple Watch), n_amigos (em amizades), n_tickets (em tickets_suporte) e n_recusas (em pagamentos).
  Mostre a média de cada variável comparando o grupo que manteve a renovação automática ligada (target = 0) com o grupo que desligou a renovação (target = 1), comprovando os sinais que alimentam o nosso baseline de Regressão Logística.
  ```

* **💻 Query SQL Equivalente:**
  ```sql
  WITH m1 AS (SELECT user_id, treinos_mes, minutos_mes, dias_ativos, sessoes_app FROM `vitaliza_inteli_modulo_2.uso_mensal` WHERE ano_mes = '2026-09'),
       m2 AS (SELECT user_id, treinos_mes FROM `vitaliza_inteli_modulo_2.uso_mensal` WHERE ano_mes = '2026-08'),
       am AS (SELECT user_id_1 AS user_id, COUNT(*) AS n_amigos FROM `vitaliza_inteli_modulo_2.amizades` WHERE DATE(data_amizade) <= '2026-09-30' GROUP BY 1),
       tk AS (SELECT user_id, COUNT(*) AS n_tickets FROM `vitaliza_inteli_modulo_2.tickets_suporte` WHERE DATE(TIMESTAMP(data_abertura)) <= '2026-09-30' GROUP BY 1),
       pg AS (SELECT user_id, COUNTIF(status_pagamento = 'recusado') AS n_recusas FROM `vitaliza_inteli_modulo_2.pagamentos` WHERE DATE(data_pagamento) <= '2026-09-30' GROUP BY 1),
       features AS (
         SELECT
           a.user_id,
           CASE WHEN CAST(a.renovacao_automatica AS STRING) IN ('0', 'false', 'False') THEN 1 ELSE 0 END AS target_saida,
           CASE WHEN a.plano_atual = 'mensal' THEN 1 ELSE 0 END AS is_mensal,
           CASE WHEN a.canal_cobranca IN ('app_store', 'google_play') THEN 1 ELSE 0 END AS is_loja,
           COALESCE(m1.treinos_mes, 0) AS treinos_m1,
           COALESCE(m2.treinos_mes, 0) AS treinos_m2,
           COALESCE(m1.treinos_mes, 0) - COALESCE(m2.treinos_mes, 0) AS delta_treinos,
           CASE WHEN LOWER(u.relogio_conectado) NOT IN ('nenhum', '') THEN 1 ELSE 0 END AS tem_relogio,
           COALESCE(am.n_amigos, 0) AS n_amigos,
           COALESCE(tk.n_tickets, 0) AS n_tickets,
           COALESCE(pg.n_recusas, 0) AS n_recusas
         FROM `vitaliza_inteli_modulo_2.assinaturas` a
         JOIN `vitaliza_inteli_modulo_2.usuarios` u ON a.user_id = u.user_id
         LEFT JOIN m1 ON a.user_id = m1.user_id
         LEFT JOIN m2 ON a.user_id = m2.user_id
         LEFT JOIN am ON a.user_id = am.user_id
         LEFT JOIN tk ON a.user_id = tk.user_id
         LEFT JOIN pg ON a.user_id = pg.user_id
         WHERE a.status_atual = 'ativa' AND a.plano_atual IN ('mensal', 'anual')
       )
  SELECT
    target_saida,
    COUNT(*) AS n_assinantes,
    ROUND(AVG(treinos_m1), 2) AS media_treinos_m1,
    ROUND(AVG(delta_treinos), 2) AS media_delta_treinos,
    ROUND(AVG(tem_relogio) * 100, 1) AS pct_com_relogio,
    ROUND(AVG(n_amigos), 2) AS media_amigos,
    ROUND(AVG(n_tickets), 2) AS media_tickets,
    ROUND(AVG(n_recusas), 2) AS media_recusas
  FROM features
  GROUP BY 1
  ORDER BY 1;
  ```

---

### 🔹 Ação 2: Conferir o Output e as Métricas do Baseline
* Desempenho fora da amostra do **Baseline de Regressão Logística (`StandardScaler`, `L2`)** validado no corte histórico `31/07/2026`:
  * **`ROC-AUC = 0,7522`** | **`PR-AUC = 0,5079`** | **`Brier Score = 0,1504`** | **`Lift no Topo 10% (1.500 WhatsApps) = 2,55x`**.

---

### 🔹 Ação 3: Fechar os Seus 2 Artefatos da Semana 5 no Agente de Código
```text
Acabei de rodar o Passo 05 no BigQuery validando as variáveis da Feature Store Tabular:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Consultando como referência a Seção 4 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`, preencha a Seção 4 completa do meu arquivo `ARTEFATO_TECH_SEMANA5_A1.md` na minha pasta em `membros/` documentando:
- O protocolo de validação Out-of-Time sem Data Leakage (corte histórico 31/07/2026 medindo saída nos 60 dias seguintes);
- O conjunto de variáveis explicativas (X);
- A tabela de desempenho fora da amostra da Regressão Logística (ROC-AUC = 0,7522, PR-AUC = 0,5079, Brier Score = 0,1504 e Lift@10% = 2,55x) e a interpretação dos pesos.
Por fim, revise os meus dois arquivos de `semana_5_A1/` para garantir que estão 100% completos!
```

---

### 💡 Ação 4 (Prompts Extras para Explorar Insights e Conversar com o Agente):
1. **No Agente do BigQuery (Encontrando os Clientes em Desaceleração Aguda):**
   ```text
   Cruze assinaturas com uso_mensal comparando agosto ('2026-08') e setembro ('2026-09'). Quantos pagantes ativos treinavam 6 ou mais vezes em agosto e caíram para apenas 1 ou 2 treinos em setembro? Qual é a taxa de renovação desligada desse grupo que sofreu queda brusca de ritmo?
   ```
2. **No Seu Agente do Repositório / NotebookLM (Entendendo o Modelo sem Matemática Pesada):**
   ```text
   Leia o arquivo `00_comece_por_aqui/02_trilha_ciencia_de_dados_e_ml/README.md` e a Seção 4 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`. Me explique como se eu estivesse apresentando para o CFO da Vitaliza o que significa o nosso modelo ter um Lift de 2,55x no topo 10% e por que isso economiza dinheiro na hora de disparar os 1.500 WhatsApps do mês.
   ```

🎉 **Parabéns! Você concluiu toda a jornada da Semana 5 (A1) e construiu os dois relatórios completos no seu workspace!** Agora siga para o [**`02_PLAYBOOK_SEMANA_10_A2.md`**](./02_PLAYBOOK_SEMANA_10_A2.md).
