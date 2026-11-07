# 00 · Guia Mestre de Aprendizado Prático & Setup de Ambiente — Case Vitaliza (Módulo 2)

> **Propósito deste Guia:** Este não é um manual de divisão burocrática de tarefas. O objetivo aqui é que **cada integrante do grupo (independentemente da sua área de origem)** consiga percorrer **100% da jornada técnica e estratégica de ponta a ponta**, aprendendo na prática a operar Bancos de Dados em Nuvem (**Google BigQuery**), **SQL Analítico**, **Machine Learning Supervisionado e Não-Supervisionado**, **Extração Multimodal com IA Generativa (Gemini)** e **Engenharia Assistida por Agentes de Código (Claude Code / Codex / VS Code)** até construir, com as próprias mãos, os seus próprios entregáveis completos da **Semana 5 (A1)** e da **Semana 10 (A2)**.

---

## 🎯 1. A Filosofia do Nosso Método: Aprender Fazendo de Ponta a Ponta

No modelo tradicional de trabalhos em grupo, cada pessoa faz apenas a parte que já sabe (quem é de negócios escreve texto, quem é de tecnologia roda código) e ninguém desenvolve habilidades novas. **Neste Módulo 2, invertemos essa lógica:**

1. **O Gabarito Oficial já está pronto e garantido (`artefatos_negocios/` e `artefatos_tecnologia/`):**
   * Os 4 entregáveis oficiais do módulo já estão construídos, auditados e salvos na raiz do repositório como **Ponto de Chegada / Referência Executiva**. Isso tira 100% da pressão de prazo das costas do grupo.
2. **A Jornada Individual de Construção (`membros/nome_membro_1/`):**
   * Com o resultado final garantido, cada integrante usa os nossos **2 Playbooks de Aprendizado Prático** para **reconstruir toda a solução passo a passo dentro da sua própria pasta individual (`membros/`)**:
   * Você vai conversar com as 13 bases de dados no **BigQuery**, rodar consultas SQL reais, inspecionar scripts Python, interagir com o seu **Agente de Código** e ver nascer, seção por seção, os seus próprios documentos de Negócios e Tecnologia.

```mermaid
flowchart TD
    subgraph Oficial ["1. REFERÊNCIA OFICIAL DO GRUPO (RAIZ DO REPOSITÓRIO — PROTEGIDA)"]
        RefA1["artefatos_negocios/semana_5_A1/<br/>artefatos_tecnologia/semana_5_A1/"]
        RefA2["artefatos_negocios/semana_10_A2/<br/>artefatos_tecnologia/semana_10_A2/"]
    end

    subgraph Ciclo ["2. SEU CICLO PRÁTICO DE APRENDIZADO (PASSO A PASSO NOS PLAYBOOKS)"]
        BQ["A. Google BigQuery (Agente + SQL)<br/>Explorar as 13 tabelas reais do Data Room"]
        Code["B. Agente de Código (Claude Code / Codex / VS Code)<br/>Validar hipóteses, rodar Python/ML e redigir análises"]
        Deep["C. Aprofundamento Técnico & Negócios<br/>Testar prompts extras, gráficos e cenários"]
        BQ --> Code --> Deep
    end

    subgraph MeuWorkspace ["3. SEU WORKSPACE INDIVIDUAL (ZERO CONFLITO DE GIT)"]
        MyA1["membros/nome_membro_1/semana_5_A1/<br/>• ARTEFATO_NEGOCIOS_SEMANA5_A1.md<br/>• ARTEFATO_TECH_SEMANA5_A1.md"]
        MyA2["membros/nome_membro_1/semana_10_A2/<br/>• ARTEFATO_NEGOCIOS_SEMANA10_A2.md<br/>• ARTEFATO_TECH_SEMANA10_A2.md"]
    end

    Oficial -. "Serve como Gabarito / Padrão de Qualidade" .-> Code
    Ciclo --> MeuWorkspace
```

---

## 🛠️ 2. O Ecossistema de Ferramentas (O Que Vamos Aprender a Usar)

Ao seguir este roteiro, você desenvolverá fluência prática em **4 ferramentas fundamentais de IA e Dados**:

| Ferramenta | O Que É na Prática (Sem Jargão) | Como Usamos no Case Vitaliza | Link / Onde Acessar |
| :--- | :--- | :--- | :--- |
| **1. Google BigQuery + Agente Gemini** | Um "Super Excel em Nuvem" do Google que armazena as 13 tabelas do case (incluindo `atividades.parquet` com 1,25 milhão de treinos) e permite conversar com os dados em linguagem natural ou rodar SQL em segundos. | Para auditar os dados, limpar pegadinhas, calcular churn, segmentar clientes e analisar o experimento A/B de agosto sem travar o computador. | [**Abrir Dataset `vitaliza_inteli_modulo_2` no BigQuery**](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2) |
| **2. Agente de Código (`Claude Code`, `Codex`, `Cursor` ou `VS Code`)** | Um assistente que lê todas as pastas e documentos do nosso repositório, conversa com você sobre o case e preenche os seus relatórios. | Para transformar as respostas do BigQuery nas seções estruturadas dos seus artefatos dentro de `membros/` e debater os documentos das trilhas de estudo. | No seu computador (Desktop App ou VS Code). |
| **3. NotebookLM do Case** | Caderno de IA alimentado exclusivamente com os PDFs oficiais (Enunciado, Dicionário de Dados e Slides das Aulas) e dossiês do projeto. | Para tirar dúvidas conceituais sobre regras do case, preços, taxas de canal e teoria das aulas (Siegel, Kotler, CRISP-DM). | [**Abrir Caderno Oficial no NotebookLM**](https://notebook.google.com/notebook/7201a470-3cf5-42e0-b859-7036086280ac) |
| **4. Git & GitHub (`main` e `develop`)** | Sistema de controle de versão onde o repositório do grupo vive na nuvem. | Para você aprender na prática a clonar o projeto, puxar atualizações (`git pull`), salvar seus artefatos na sua pasta individual (`git commit`) e compartilhar na branch `develop` (`git push` / `git merge`). | [**Repositório `02-mba-modulo-2` no GitHub**](https://github.com/leomaquiaveli/02-mba-modulo-2) |

---

## 👥 3. Como Funciona a Estrutura da Pasta `membros/` (Zero Conflito de Git)

Se 5 pessoas editarem ao mesmo tempo o arquivo `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md`, quando a segunda pessoa tentar subir para o GitHub vai ocorrer **conflito de merge** (porque dois computadores mexeram na mesma linha do mesmo arquivo).

Para que **todo mundo possa construir os 4 artefatos completos do início ao fim** sem nunca travar em conflito de Git, cada integrante trabalha na sua própria subpasta dentro de [`membros/`](../../membros/):

```text
membros/
├── 00_geral/                                      <-- Anotações e arquivos compartilhados
├── nome_membro_1/                                 <-- Pasta-modelo pronta (você duplica com seu nome!)
│   ├── README.md                                  <-- Seu painel de controle individual
│   ├── semana_5_A1/
│   │   ├── ARTEFATO_NEGOCIOS_SEMANA5_A1.md        <-- Seu relatório de Negócios A1 (construído no Playbook 1)
│   │   └── ARTEFATO_TECH_SEMANA5_A1.md            <-- Seu relatório de Tecnologia A1 (construído no Playbook 1)
│   └── semana_10_A2/
│       ├── ARTEFATO_NEGOCIOS_SEMANA10_A2.md       <-- Sua apresentação ao Board A2 (construída no Playbook 2)
│       └── ARTEFATO_TECH_SEMANA10_A2.md           <-- Seu relatório de Tecnologia A2 (construído no Playbook 2)
└── nome_membro_2/                                 <-- Pasta isolada de outro integrante
```

### Passo Inicial no Seu Agente de Código (Faça Isso Antes do Passo 01):
Abra o projeto no seu **Claude Code / Codex / VS Code** e mande este primeiro comando para preparar o seu espaço pessoal:

```text
Quero iniciar minha jornada prática no repositório da Vitaliza.
1. Verifique se estou na branch `develop` (e faça `git pull origin develop` para garantir que tenho a versão mais recente).
2. Duplique a pasta-modelo `membros/nome_membro_1/` criando uma nova pasta chamada `membros/<coloque_seu_identificador_aqui>/` (mantendo a subpasta `semana_5_A1/` e `semana_10_A2/` lá dentro).
3. Me confirme a árvore de arquivos criada na minha pasta individual e me diga que estamos prontos para o Passo 01 do Playbook 1.
```

---

## 🗄️ 4. Como Usar o Google BigQuery no Dia a Dia (Três Formas de Interagir)

Ao abrir o nosso dataset [**`vitaliza_inteli_modulo_2` no BigQuery**](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2), você verá no painel esquerdo todas as **13 tabelas** do case (`amizades`, `assinaturas`, `atividades`, `campanha_ago26`, `eventos_assinatura`, `feed_posts`, `gym_churn_us`, `onboarding`, `pagamentos`, `pesquisa_saida`, `tickets_suporte`, `uso_mensal`, `usuarios`).

Você pode explorar essas tabelas de **3 formas diferentes** em cada Passo dos Playbooks:

1. **Forma 1 — Pelo Agente Conversacional (`Conversations` / `Ask a question`):**
   * Clique em uma tabela (ex.: `assinaturas`) ou clique em **`Conversations`** no menu esquerdo para selecionar **várias tabelas ao mesmo tempo** (ex.: `assinaturas` + `uso_mensal` + `usuarios`).
   * Cole o **💬 Prompt para o Agente do BigQuery** do Playbook: o próprio Agente gera a consulta interna, calcula a tabela e desenha o gráfico na tela!
2. **Forma 2 — Pelo `Data canvases` (Cruzamento Visual + Gráficos):**
   * Clique em **`Data canvases`** no menu esquerdo, adicione duas ou mais tabelas na tela, clique em **Join** (unindo por `user_id` ou `assinatura_id`) e peça análises ou gráficos comparativos na caixa de prompt.
3. **Forma 3 — Pelo Editor SQL (`Queries`):**
   * Em todos os Passos dos Playbooks deixamos também a **💻 Query SQL Completa**. Mesmo que você use o Agente Conversacional, recomendamos colar e rodar a Query SQL no editor para **aprender a ler como o SQL filtra datas (`WHERE`), agrupa (`GROUP BY`), cruza tabelas (`JOIN`) e cria faixas (`CASE WHEN`)**.

---

## 📅 5. Roteiro de Estudo e Construção (10 Passos em 2 Playbooks)

Você pode avançar no seu ritmo (por exemplo, **1 Passo por dia** em ~25 minutos, ou fazer uma imersão no fim de semana). Cada Passo tem começo, meio e fim e deixa uma seção inteira do seu entregável pronta:

### 📘 Fase 1: Construindo os Entregáveis da Semana 5 (A1)
👉 **Abra o arquivo:** [**`01_PLAYBOOK_SEMANA_05_A1.md`**](./01_PLAYBOOK_SEMANA_05_A1.md)

| Passo | O Que Você Vai Aprender a Fazer | Quais Tabelas Você Vai Dominar | O Que Fica Pronto na Sua Pasta `semana_5_A1/` |
| :--- | :--- | :--- | :--- |
| **Passo 01** | Reconciliar uma base de assinaturas, isolar contas não-pagantes (`cortesia`), calcular Receita Líquida (MRR) descontando *take rate* e medir churn contratado (`renovacao_automatica = 0`). | `assinaturas` (`32.643` linhas) | **Negócios A1:** Seção 1 e 1.1<br>**Tech A1:** Seção 1 |
| **Passo 02** | Fazer auditoria de *Data Quality*: detectar vazamento temporal pós-corte (`> 30/09/2026`), converter fuso horário `UTC ("Z")` para Brasília (`BRT`), padronizar strings (`android`/`iOS`) e unificar vocabulário PT/EN em 1,25 milhão de linhas. | `usuarios`, `eventos_assinatura`, `atividades`, `feed_posts`, `amizades` | **Tech A1:** Seção 2 (As 7 Anomalias)<br>**Negócios A1:** Seção 5.2 (Limitações) |
| **Passo 03** | Conduzir uma Análise Exploratória Diagnóstica (EDA) testando 5 hipóteses de negócio (`H1` Reajuste de preço, `H2` Canal Loja vs Site, `H3` Frequência de treino, `H4` Rede social/Smartwatch e `H5` Falha de pagamento/Suporte). | `eventos_assinatura`, `pesquisa_saida`, `uso_mensal`, `amizades`, `pagamentos`, `tickets_suporte` | **Negócios A1:** Seção 2 Completa (Matriz `H1` a `H5`) |
| **Passo 04** | Criar uma Segmentação Comportamental sem *Data Leakage* (4 Clusters), traduzir clusters em **Personas Baseadas em Dados** e calcular a **Matriz de Receita em Risco** separando inativos que já cancelaram (`4A`) dos *Sleeping Dogs* (`4B`). | `assinaturas` + `uso_mensal` + `usuarios` | **Negócios A1:** Seções 3, 4 e 5.1<br>**Tech A1:** Seção 3 Completa |
| **Passo 05** | Construir uma visão consolidada de variáveis de risco (`M-1` vs `M-2`, `delta_treinos`) e entender como funciona o modelo baseline de **Regressão Logística** (`ROC-AUC`, `PR-AUC`, `Brier Score` e `Lift@10%`). | Todas as fontes tabulares unificadas por `user_id` no BigQuery | **Tech A1:** Seção 4 Completa *(Fechamento 100% da Semana 5!)* |

---

### 📙 Fase 2: Construindo os Entregáveis da Semana 10 (A2)
👉 **Abra o arquivo:** [**`02_PLAYBOOK_SEMANA_10_A2.md`**](./02_PLAYBOOK_SEMANA_10_A2.md)

| Passo | O Que Você Vai Aprender a Fazer | Quais Tabelas / Scripts Você Vai Dominar | O Que Fica Pronto na Sua Pasta `semana_10_A2/` |
| :--- | :--- | :--- | :--- |
| **Passo 01** | Estruturar uma defesa executiva para Conselho de Administração (Série B) e comparar arquiteturas de produto (*Win-Back Reativo* vs. *Engagement Forecasting* vs. *Política Prescritiva de Uplift* frente ao Strava). | `assinaturas`, `uso_mensal`, `usuarios` | **Negócios A2:** Slides 1, 2 e 3<br>**Tech A2:** Seção 1 |
| **Passo 02** | Extrair variáveis estruturadas de textos livres (`onboarding`, `suporte`, `feed`), entender a análise dos `25.473` mapas de calor (`heatmaps_90d/`), calcular o custo de IA e analisar o **Teste de Ablação**. | `onboarding`, `tickets_suporte`, `feed_posts` no BigQuery + Dossiê Multimodal | **Tech A2:** Seção 2 Completa (Subseções 2.1, 2.2 e 2.3) |
| **Passo 03** | Comparar 4 famílias de algoritmos supervisionados para predição em 60 dias (**Regressão Logística, Árvore de Decisão, Random Forest e Gradient Boosting Multimodal**) e extrair regras não-lineares de risco. | Feature Store Completa (Tabular + Multimodal) | **Tech A2:** Seção 3 Completa |
| **Passo 04** | Analisar um **Experimento Controlado A/B (`campanha_ago26.csv`)**, calcular **Uplift (Efeito Causal Heterogêneo)** por plano e por engajamento prévio e provar matematicamente os **4 Quadrantes de Siegel** (*Persuadíveis*, *Garantidos*, *Perdidos* e *Sleeping Dogs*). | `campanha_ago26` + `assinaturas` + `uso_mensal` (mês `2026-07`) | **Negócios A2:** Slide 4 Completo (Tabelas 4.1 e 4.2)<br>**Tech A2:** Seção 4.1 (Árvore de Decisão em 5 Regras) |
| **Passo 05** | Otimizar um orçamento real de CRM (**R$ 40.000/mês**, **300 CS**, **1.500 WhatsApps**), calcular a DRE de **Lucro Líquido Incremental (`+R$ 207.840,10`)**, desenhar travas de contingência (*Kill-Switch*) e gerar mensagens personalizadas de CRM com **Briefing Fechado**. | Base Ativa no BigQuery + Documentos da Trilha 1 e 3 | **Negócios A2:** Slides 5 e 6<br>**Tech A2:** Seção 4.2 *(Fechamento 100% da Semana 10!)* |

---

## 🔄 6. Guia Rápido de Git para Salvar e Sincronizar Seu Aprendizado

Sempre que você quiser atualizar seu computador com as novidades da branch `develop` ou salvar o que construiu na sua pasta em `membros/`, você pode pedir direto para o seu **Agente de Código** ou rodar estes comandos:

1. **Para trazer a branch `develop` (onde estão estes Playbooks) para o seu computador:**
   ```bash
   git fetch origin
   git checkout develop
   git pull origin develop
   ```
2. **Se você estiver na `main` e quiser puxar (fazer o merge) do que está na `develop`:**
   ```bash
   git checkout main
   git pull origin develop
   ```
3. **Para salvar os artefatos que você construiu na sua pasta `membros/`:**
   ```bash
   git add membros/
   git commit -m "feat(membros): avanca na construcao dos artefatos praticos"
   git pull --rebase origin develop
   git push origin develop
   ```
