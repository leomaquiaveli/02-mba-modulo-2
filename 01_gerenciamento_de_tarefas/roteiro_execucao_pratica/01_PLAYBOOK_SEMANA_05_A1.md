# Playbook 1 — Semana 5 (A1)

> **Projeto:** MBA Inteli Módulo 2 — Case Vitaliza (1º Movimento: ENTENDER — Entrega `13/11/2026`)  
> **Ambiente de Dados:** Google BigQuery ([`thermal-origin-470820-e7.vitaliza_inteli_modulo_2`](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2))  
> **Objetivo:** conduzir qualquer integrante do grupo, mesmo sem experiência em programação ou SQL, na **construção completa dos seus próprios entregáveis de Negócios e Tecnologia da Semana 5**, aprendendo na prática como explorar bancos de dados em nuvem, auditar bases sujas, testar hipóteses, criar segmentações comportamentais, entender um modelo de previsão de churn e operar um agente de código (**Claude Code / Codex / VS Code**).
>
> **Seus arquivos (na sua pasta em `membros/`):**
> * Negócios A1: `membros/nome_membro_1/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md`
> * Tecnologia A1: `membros/nome_membro_1/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`
>
> **Artefatos oficiais do grupo (só para a comparação no fim de cada passo; não peça ao agente para lê-los antes disso):**
> * [`artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md`](../../artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md)
> * [`artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`](../../artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md)

---

## O que cada passo produz

| Passo | O que você aprende | O que constrói no `ARTEFATO_NEGOCIOS_SEMANA5_A1.md` | O que constrói no `ARTEFATO_TECH_SEMANA5_A1.md` |
| :--- | :--- | :--- | :--- |
| **Passo 01** | Reconciliação de população pagante, cálculo de *Take Rate* / MRR Líquido e detecção de *Churn Diferido* (`renovacao_automatica = 'nao'`). | **Seção 1 & 1.1:** Resumo Executivo, Tabela de Composição (`14.753` pagantes), Assimetria de Lojas (`70,22%`), MRR Líquido (`R$ 409.941/mês`) e Estoque de Saída Contratada (`2.250`). | **Seção 1:** Arquitetura do Pipeline de Engenharia e Reconciliação (`14.813` ativas − `60` cortesias = `14.753` pagantes). |
| **Passo 02** | Auditoria de Qualidade de Dados (*Data Hygiene*): prevenção de *Data Leakage* pós-corte, normalização de fuso horário `UTC ("Z")` vs. `BRT` e padronização de vocabulário em 1,25M de linhas. | **Seção 5.2 (Parte 1):** Limitações Metodológicas e Anomalias Temporais/Categóricas do Pacote Bruto. | **Seção 2 Completa:** Tabela das **7 Anomalias Estruturais** documentadas com volume exato e regra de tratamento. |
| **Passo 03** | Análise Exploratória Diagnóstica (EDA): como confrontar as hipóteses da diretoria com dados reais e separar correlação bivariada de causalidade. | **Seção 2 Completa & Seção 5.2 (Parte 2):** Diagnóstico da Subida do Churn em 2026 (`5,6% ➔ 6,6%`, pico `8,1%` em abril) testando as **5 Hipóteses (`H1` a `H5`)**. | **Seção 1 (Complemento EDA):** Validação estatística das hipóteses diagnósticas do Objetivo 2. |
| **Passo 04** | Clusterização Comportamental sem vazamento de alvo, construção de **Personas com Dados** (vs. personas inventadas) e cálculo de **Receita em Risco** (`Cluster 4A` vs `4B`). | **Seção 3 (Pilar 01):** Os 4 Segmentos Estratégicos;<br>**Seção 4 (Pilar 02):** As 4 Personas de Dados;<br>**Seção 5.1 (Pilar 03):** Valor em Risco Mensal/Anualizado (`4A` [`1.318`] vs `4B` [`995` *Sleeping Dogs*]). | **Seção 3 Completa:** Protocolo Anti-Leakage e Tabela dos 4 Clusters Comportamentais com Centróides (`treinos/mês`, `minutos/mês`) e Taxa de Renovação Desligada *a posteriori*. |
| **Passo 05** | Engenharia de Variáveis Temporais (`M-1` vs `M-2`, `delta_treinos`), validação *Out-of-Time* e avaliação de **Regressão Logística** (`ROC-AUC`, `PR-AUC`, `Brier Score` e `Lift@10%`). | Revisão de coerência final entre os números de Negócios e Tecnologia. | **Seção 4 Completa:** Conjunto de Variáveis (`X`) sem *Data Leakage* e Métricas do Baseline de **Regressão Logística** (`ROC-AUC = 0,7522`, `PR-AUC = 0,5079`, `Brier = 0,1504`, `Lift@10% = 2,55x`). |

---

## PASSO 01 — Fotografia Reconciliada da Base (`14.753`), Lojas (`70,22%`), MRR Líquido (`R$ 409.941`) e Saída Contratada (`2.250`)

### O que este passo ensina
Em qualquer projeto real de Ciência de Dados e Negócios, o erro mais comum é fazer um `COUNT(*)` simples na tabela de clientes ativos sem verificar:
1. **Quem realmente paga:** Muitas empresas misturam contas de teste, funcionários e influenciadores (`plano_atual = 'cortesia'`) junto com clientes pagantes. Se você não excluir essas contas antes de calcular o churn ou a receita média, todos os denominadores do projeto ficam errados.
2. **Receita Bruta vs. Receita Líquida (*Take Rate*):** Um cliente mensal que paga R$ 39,90 na App Store deixa 15% para a Apple (sobram R$ 33,92 para a Vitaliza), enquanto no Pix pelo site a taxa é de apenas 0,99% (sobram R$ 39,50).
3. **Churn Diferido (*Já Contratado*):** No modelo de assinatura (especialmente anual), o cliente entra nas configurações do iPhone/Android hoje e **desliga a renovação automática (`renovacao_automatica = 'nao'`)**, mas continua com `status_atual = 'ativa'` até o fim do período já pago. Descobrir quantos ativos já desligaram a renovação revela a perda que já está contratada e ainda não aparece no churn.

---

### Raciocínio do passo

**Pergunta de negócio:** quantos clientes pagam hoje, quanto eles deixam de fato no caixa da Vitaliza por mês e quanto dessa receita já tem saída decidida? Quem pergunta é Camila Ferraz, VP de Crescimento e Retenção. Ela precisa levar ao Conselho um número de base que ninguém conteste. A mesma resposta serve a Rita Fontes (CFO): o teto de R$ 40.000/mês só pode ser julgado quando comparado com a receita líquida em jogo. E ela testa a proposta de Patrícia (Head de CS), o Caminho A, uma oferta de retenção na tela "Cancelar" do site: se a maior parte da base paga pelas lojas, essa tela não alcança a maioria.

**Onde olhar e por quê:**

| Fonte | Campo ou regra | Por que é necessário |
| :--- | :--- | :--- |
| Tabela `assinaturas` | `status_atual` | Separa quem está ativo de quem já expirou ou foi reembolsado. |
| Tabela `assinaturas` | `plano_atual` | Separa `mensal`, `anual` e `cortesia`. Cortesia não paga e sai da conta. |
| Tabela `assinaturas` | `canal_cobranca` | Define a taxa retida por loja ou meio de pagamento e mostra onde a Vitaliza consegue agir no cancelamento. |
| Tabela `assinaturas` | `renovacao_automatica` | Mostra quem já desligou a renovação e vai sair ao fim do período pago. |
| `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md`, seção 4 | Preços e taxas | Define R$ 39,90/mês, R$ 299,90/ano e as taxas de 15% (lojas), 3,5% (cartão no site) e 0,99% (Pix no site). |
| `00_comece_por_aqui/05_DOSSIE_DICIONARIO_DE_DADOS_M2.md`, seção 3 | Domínio dos campos | Confirma que `cortesia` usa o canal `interno` e que `assinaturas` é um retrato da situação em `01/10/2026`, sem histórico. |

**Sequência de raciocínio:**
1. **Contar as assinaturas ativas (`14.813`).** Por quê: é o universo de quem tem acesso pago ou gratuito ao produto na data de corte.
2. **Retirar as `60` cortesias.** Por quê: quem não paga não gera receita e não cancela no sentido financeiro. Se ficar na base, aumenta o denominador de todas as taxas e reduz a receita média por cliente.
3. **Fixar a população pagante em `14.753`.** Por quê: todos os passos seguintes, nos dois artefatos, usam esse mesmo denominador. Se cada integrante usar um número diferente, as taxas deixam de ser comparáveis.
4. **Abrir a base por plano e canal.** Por quê: o preço depende do plano e a taxa depende do canal. A combinação dos dois define quanto cada cliente deixa de receita líquida.
5. **Mensalizar o plano anual (R$ 299,90 ÷ 12 ≈ R$ 24,99/mês).** Por quê: para somar mensal e anual na mesma unidade. É uma equivalência contábil; o cliente anual paga uma vez por ano.
6. **Aplicar a taxa do canal (receita líquida = preço × (1 − taxa)).** Por quê: o *take rate* (parcela que a loja ou o meio de pagamento retém) faz a receita bruta superestimar o que entra no caixa.
7. **Somar a receita líquida mensalizada (R$ 409.941/mês).** Por quê: é a base de comparação para o valor em risco que será calculado no Passo 04.
8. **Contar quem tem renovação desligada (`2.250`, `15,25%`).** Por quê: esses clientes ainda aparecem como ativos, mas já decidiram sair. É churn diferido: a perda está contratada e só aparece na série de churn quando o período pago termina.
9. **Calcular a participação das lojas (`70,22%`).** Por quê: é o dado que limita o Caminho A. Nas lojas, o cliente desliga a renovação nas configurações do celular, fora do alcance da Vitaliza.

**Armadilhas comuns:**
- **Contar todas as linhas de `assinaturas`.** A tabela tem uma linha por cliente (`32.643`), com a situação em `01/10/2026`, inclusive de quem já saiu. Sinal: um total muito acima de `14.813`.
- **Esquecer as cortesias.** No arquivo, as 60 cortesias estão com renovação desligada. Se ficarem na conta, o total de ativos e a contagem de saída contratada sobem juntos. Sinal: total de `14.813` em vez de `14.753`.
- **Filtro de renovação que não encontra nada.** `renovacao_automatica` é texto, com os valores `'sim'` e `'nao'`. Se o agente do BigQuery filtrar por `0` ou `false`, a contagem de renovação desligada vem zerada. Sinal: zero clientes com renovação desligada.
- **Somar preço anual com mensal sem mensalizar.** Sinal: a receita do plano anual aparece muito maior que a do mensal.
- **Usar uma taxa média única para todos os canais.** Sinal: receita total diferente do gabarito mesmo com as contagens corretas.
- **Arredondamento.** O artefato oficial arredondou a receita unitária para centavos antes de multiplicar (ex.: 39,90 × 0,85 = 33,915, arredondado para R$ 33,92). Se o agente só arredondar no final, a sua receita por linha pode diferir do gabarito em alguns reais. Isso é esperado; declare a regra de arredondamento que você usou.
- **Tratar os `2.250` como churn já ocorrido.** Eles ainda pagam até o fim do período. No plano anual, a saída pode demorar meses.

**Como conferir sozinho:**
- `14.753` + `60` = `14.813`.
- Anual `8.478` + Mensal `6.275` = `14.753`; `57,47%` + `42,53%` somam 100.
- Lojas `10.359` + Site `4.394` = `14.753`. App Store = `3.047` + `2.348` = `5.395`; Google Play = `2.928` + `2.036` = `4.964`.
- Receita: R$ 187.732 + R$ 222.209 = R$ 409.941.
- Saída contratada: `2.082` + `168` = `2.250`; `2.250` ÷ `14.753` ≈ `15,25%`.
- Recalcule uma linha à mão: mensal na App Store = R$ 33,92 × `2.348` ≈ R$ 79.644, valor que aparece na tabela 1.1 do artefato oficial.

---

### Ação 1: Consultar no agente do BigQuery
Abra a tabela **`assinaturas`** no [nosso Dataset do BigQuery](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sthermal-origin-470820-e7!2svitaliza_inteli_modulo_2):

* **Prompt para o agente do BigQuery:**
  ```text
  Na tabela assinaturas, filtre apenas os registros com status_atual igual a 'ativa'.
  1. Primeiro, mostre quantas assinaturas ativas pertencem ao plano_atual = 'cortesia' (canal_cobranca = 'interno') e quantas são assinaturas pagantes reais (planos 'anual' e 'mensal').
  2. Depois, considerando apenas os 14.753 assinantes pagantes ativos (excluindo cortesia), monte uma tabela detalhada agrupada por plano_atual e canal_cobranca contendo:
  - Assinantes Ativos (N)
  - % da Base Pagante (sobre 14.753)
  - Quantos já desligaram a renovação automática (renovacao_automatica = 'nao') e o percentual (%)
  - Preço Bruto (anual = R$ 299,90/ano ou R$ 24,991667/mês; mensal = R$ 39,90/mês)
  - Taxa do Canal (app_store e google_play = 15%; web_cartao = 3,5%; web_pix = 0,99%)
  - Receita Líquida Unitária Mensal e Receita Líquida Mensalizada Total de cada linha.
  Inclua os subtotais do Plano Anual, do Plano Mensal e o Total Geral dos 14.753 pagantes.
  ```

---

### Ação 2: Conferir o resultado
* **Reconciliação:** `14.813` ativas = **`14.753` pagantes ativos** + **`60` cortesias**.
* **Subtotal Anual:** **`8.478` assinantes (`57,47%`)** $\rightarrow$ `app_store` (`3.047`), `google_play` (`2.928`), `web_cartao` (`1.803`), `web_pix` (`700`) $\rightarrow$ Receita Líquida Mensalizada = **`R$ 187.732,00 / mês`**.
* **Subtotal Mensal:** **`6.275` assinantes (`42,53%`)** $\rightarrow$ `app_store` (`2.348`), `google_play` (`2.036`), `web_cartao` (`1.191`), `web_pix` (`700`) $\rightarrow$ Receita Líquida Mensalizada = **`R$ 222.209,00 / mês`**.
* **Total Geral Pagantes:** **`14.753` (`100%`)**, sendo **70,22% (`10.359`) nas Lojas** e **29,78% (`4.394`) no Site**, com Receita Líquida Total de **`R$ 409.941,00 / mês`**.
* **Alerta de Saída Contratada:** **`2.250` pagantes ativos (`15,25%`)** já desligaram a renovação automática (`2.082` no anual e `168` no mensal).

---

### Ação 3: Escrever a seção com o agente de código
Nesta ação você escreve a seção a partir do seu próprio resultado. O agente ajuda a explicar, redigir e revisar. O artefato oficial do grupo entra só no final, para comparação.

**Antes de abrir o agente:** escreva em até três frases o que o resultado mostra e o que ele muda para a Vitaliza. Formato sugerido: "A base pagante é de tantos clientes. A maior parte paga por tal canal, o que significa tal limite para a retenção. Já existem tantos clientes com saída decidida."

**Estrutura da seção:**
- **Negócios, Seção 1 (Resumo Executivo):** um parágrafo de três a cinco frases. Deve trazer a população (`14.753` pagantes, `60` cortesias excluídas), a evolução do churn informada no enunciado (5,6% em 2025, 6,6% em 2026, pico de 8,1% em abril) e uma frase que resuma o problema.
- **Negócios, Seção 1.1 (Composição da base):** tabela plano × canal com as colunas assinantes, % da base, preço bruto, taxa do canal, receita líquida unitária e receita líquida mensalizada. Subtotal do anual, subtotal do mensal e linha de total com a divisão lojas/site.
- **Callout de alerta:** os `2.250` clientes (`15,25%`) com renovação desligada, abertos em anual e mensal, e uma frase sobre o que isso significa: perda já decidida que ainda não apareceu na série de churn.
- **Tecnologia, Seção 1 (Pipeline):** diagrama em quatro camadas (ingestão das 13 fontes, saneamento, tabela analítica por assinante, modelos) e a reconciliação `14.813 − 60 = 14.753` escrita como regra de filtro.
- **Mensagem para o leitor:** a base pagante é menor do que o total de ativos, está concentrada nas lojas e já contém uma saída contratada relevante.

**Prompt para o Agente de Código:**

```text
Estou construindo os meus entregáveis da Semana 5 na minha pasta `membros/nome_membro_1/semana_5_A1/` (ou na minha pasta personalizada em `membros/`). Edite apenas arquivos dentro dessa pasta. Não altere nada em `artefatos_negocios/` nem em `artefatos_tecnologia/`.

Rodei o Passo 01 no BigQuery e obtive este resultado:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Minha leitura do resultado, em minhas palavras:
"""
[COLE AQUI AS SUAS TRÊS FRASES]
"""

Faça nesta ordem e pare ao final de cada etapa para eu confirmar:
1. Explique de volta o resultado: o que cada número significa, de qual tabela, coluna e filtro ele vem, e se a minha leitura está correta. Confira se os subtotais somam o total e se os percentuais somam 100. Aponte qualquer número que não feche.
2. Redija no meu `ARTEFATO_NEGOCIOS_SEMANA5_A1.md` a Seção 1 (resumo executivo de três a cinco frases) e a Seção 1.1 (tabela plano × canal com subtotais e total, mais um callout sobre os clientes com renovação desligada). Use apenas os números do meu resultado e indique abaixo da tabela a fonte e o filtro usados.
3. Redija no meu `ARTEFATO_TECH_SEMANA5_A1.md` a Seção 1: um diagrama Mermaid do pipeline em quatro camadas (ingestão das 13 fontes, saneamento, tabela analítica, modelos) e a regra de reconciliação das ativas em pagantes e cortesias.
4. Só depois, leia `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` e `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md` e liste em uma tabela as diferenças entre o meu rascunho e o oficial: números divergentes (com a causa provável), itens que faltam no meu e afirmações do oficial que não têm fonte indicada. Não copie texto do oficial para o meu arquivo. Se eu quiser incorporar algo, eu peço.
5. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_5_A1/`, nunca `git add .`), faça o commit com a mensagem `docs(membros): passo 01 do A1 de <meu_nome>` e me mostre o hash. Depois rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

**Depois do agente:** confira cada número do rascunho contra a sua saída do BigQuery. Se um número seu divergir do oficial, descubra a causa antes de trocar (filtro, arredondamento ou nome de coluna). A decisão sobre o que ajustar é sua.

---

### Ação 4: Prompts extras
Prompts opcionais para aprofundar o passo, no agente do BigQuery ou no agente do repositório (Claude Code, Codex ou NotebookLM):

1. **No Agente do BigQuery (Descobrindo o "Paradoxo do Início" nos Novatos):**
   ```text
   Dentro dos 14.753 pagantes ativos da tabela assinaturas, calcule o tempo de casa em meses de cada cliente até '2026-09-30' (usando a coluna inicio). Compare a taxa de renovação desligada (renovacao_automatica = 'nao') entre: (a) Novatos de até 1 mês de casa, (b) Clientes de 2 a 5 meses e (c) Veteranos de 6 meses ou mais. Onde está concentrado o maior risco inicial?
   ```
2. **No agente do repositório ou no NotebookLM (o Passo 01 contra o Caminho A):**
   ```text
   Leia o documento `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md` e o resultado que acabei de encontrar no Passo 01 (70,22% da base nas lojas App Store/Google Play e 2.250 clientes que já desligaram a renovação automática). Me explique por que essa fotografia da base derruba o argumento de criar apenas uma tela de desconto no botão "Cancelar" do site e quais perguntas um conselheiro faria para o CEO da Vitaliza.
   ```

---

## PASSO 02 — Auditoria das 7 Anomalias Estruturais do Data Room (*Data Hygiene*)

### O que este passo ensina
Bases de dados reais nunca vêm prontas para Machine Learning. Os professores inseriram **7 armadilhas reais de engenharia de dados** no pacote dos Exhibits para testar se a equipe audita os arquivos antes de modelar:
* Se você usar registros com data de **outubro/2026 ou 2027** em um corte de `30/09/2026`, você comete **Vazamento Temporal (*Data Leakage*)**.
* Se você não converter os eventos das lojas terminados em `"Z"` (`UTC`) para o fuso de Brasília (`UTC-3`), todo evento ocorrido entre 21h e 23h59 do dia `30/09` cai no mês de outubro.
* Se você não padronizar `android`/`Android` ou `corrida`/`run`, qualquer agrupamento ou gráfico divide a mesma categoria ao meio.

---

### Raciocínio do passo

**Pergunta de negócio:** os dados são confiáveis o bastante para sustentar números que vão ao Conselho, e que regras de limpeza todos os números do grupo precisam seguir? Quem pergunta é Diego Almeida (CTO), que alertou a diretoria para o esforço de engenharia sobre 13 fontes desconectadas e com fusos distintos. Dessa resposta depende a decisão sobre quanto trabalho de preparação de dados vem antes de qualquer score preditivo (o Caminho B). Para Camila Ferraz, o passo define as limitações: o que a análise não permite afirmar.

**Onde olhar e por quê:**

| Fonte | Campo | Por que é necessário |
| :--- | :--- | :--- |
| `usuarios`, `feed_posts`, `amizades` | `data_cadastro`, `data_hora` e `desde` (data da relação) | Encontrar registros com data posterior a `30/09/2026`. |
| `eventos_assinatura` | `data_hora`, `canal_cobranca` | Os eventos das lojas chegam em UTC (horário universal, terminado em `"Z"` no CSV); os do site, em horário de Brasília. No BigQuery a coluna virou TIMESTAMP e o `"Z"` não aparece, então as lojas são identificadas pelo canal. |
| `atividades` | `inicio` | Achar treinos feitos na noite de 30/09 que aparecem como 01/10 em UTC. |
| `usuarios` | `sistema` | Verificar grafias diferentes do mesmo sistema operacional. |
| `atividades` | `tipo` (modalidade do treino) | Verificar a mesma modalidade escrita em português e em inglês. |
| `usuarios` | `relogio_conectado` | Ausência de relógio está gravada como o texto `nenhum`, e não como campo vazio. |
| `assinaturas` × `eventos_assinatura` | situação atual × histórico de eventos | `assinaturas` guarda só a situação em `01/10/2026`; o histórico está nos eventos. |
| `00_comece_por_aqui/05_DOSSIE_DICIONARIO_DE_DADOS_M2.md`, seção 2 | Cinco cuidados antes de integrar | Define a regra de fuso, o estado sobrescrito e a proibição de dados pós-corte. |
| `artefatos_tecnologia/semana_5_A1/README.md` | Script `src/01_auditoria_data_room.py` e `relatorios/auditoria_exhibits.json` | Mostra como o grupo reproduziu a auditoria fora do BigQuery. |

**Sequência de raciocínio:**
1. **Fixar a data de corte: `30/09/2026 23:59:59`, horário de Brasília.** Por quê: tudo o que acontece depois é futuro em relação à decisão. Usar esses registros é vazamento de dados (*data leakage*: usar informação que não existiria no momento da decisão).
2. **Contar os registros pós-corte em cada tabela com data.** Por quê: mostra o tamanho do problema (`119`, `122` e `273`) e prova que o filtro é necessário.
3. **Converter os horários `"Z"` para `America/Sao_Paulo` antes de atribuir o mês.** Por quê: um evento às 22h de 30/09 em Brasília é gravado como 01h de 01/10 em UTC. Sem conversão, ele muda de mês e distorce a série mensal de churn.
4. **Padronizar categorias (minúsculas, sem espaços, português e inglês unificados).** Por quê: sem isso, qualquer agrupamento divide a mesma categoria em duas ou três linhas.
5. **Tratar `nenhum` como ausência de relógio.** Por quê: um teste do tipo "campo preenchido" contaria todo mundo como dono de relógio.
6. **Usar `eventos_assinatura` para cortes passados.** Por quê: para saber quem estava ativo em `31/07/2026`, a situação de `01/10/2026` não serve.
7. **Registrar cada anomalia com volume e regra.** Por quê: outra pessoa precisa conseguir repetir a limpeza e chegar aos mesmos números.

**Armadilhas comuns:**
- **Filtrar por data em timestamps UTC sem converter.** Sinal: contagens que mudam por poucas unidades perto da virada do mês.
- **Comparar texto sem padronizar maiúsculas.** Sinal: duas ou três linhas para o mesmo sistema operacional.
- **Unificar `IOS` e esquecer `iOS`.** Sinal: a soma de iOS não chega a `29.797`.
- **Usar `IS NOT NULL` para relógio.** Sinal: quase toda a base aparece com relógio.
- **Aplicar o filtro de data só em uma tabela.** A regra vale para todas as tabelas antes de qualquer agregação.
- **Agente do BigQuery usando coluna que não existe.** O agente também erra. Se aparecer erro de coluna inexistente, peça a ele para listar o esquema da tabela e refazer a consulta com os nomes reais, sem mudar a lógica.
- **Tratar anomalia como motivo para descartar a fonte.** As sete anomalias pedem uma regra de tratamento. A fonte continua útil.

**Como conferir sozinho:**
- Android: `28.027` + `7.124` = `35.151`. iOS: `20.854` + `7.463` + `1.480` = `29.797`. Somados: `64.948`, o total de linhas de `usuarios`.
- A soma das sete modalidades unificadas dá `1.254.475`, o total de treinos de `atividades`.
- Depois de aplicar o filtro de data, rode a contagem pós-corte de novo: o resultado deve ser zero.
- Os volumes pós-corte batem com os citados no caderno de hipóteses (`273` relações e `122` posts, em H-SOCIAL-01).

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `usuarios`, `feed_posts`, `amizades`, `eventos_assinatura` e `atividades`

* **Prompt para o agente do BigQuery:**
  ```text
  Faça uma auditoria técnica nas tabelas usuarios, feed_posts, amizades, eventos_assinatura e atividades para documentarmos as anomalias estruturais do Data Room:
  1. Registros pós-corte (> '2026-09-30'): quantos registros existem após 30/09/2026 em usuarios (data_cadastro), feed_posts (data_hora) e amizades (desde)?
  2. Fuso horário UTC vs Brasília: quantos eventos existem em eventos_assinatura vindos das lojas (canal_cobranca app_store ou google_play, gravados em UTC) e quantos treinos na tabela atividades (coluna inicio) caíram na primeira hora de '2026-10-01' em UTC mas aconteceram na noite de '2026-09-30' no horário de Brasília (America/Sao_Paulo)?
  3. Despadronização de Sistema Operacional em usuarios: mostre a contagem de cada grafia bruta na coluna sistema (android, Android, ios, iOS, IOS) e o total unificado para Android e iOS.
  4. Modalidades bilíngues na tabela atividades (1.254.475 treinos): mostre a contagem de cada valor bruto da coluna tipo (corrida, run, caminhada, walk, forca, strength, pedal, ride, funcional, yoga, hiit) e a soma unificando Português + Inglês.
  5. String 'nenhum' em relogio_conectado na tabela usuarios: mostre quantos usuários têm o texto 'nenhum' versus quantos possuem relógio conectado real.
  ```

---

### Ação 2: Conferir o resultado
1. **Cortesias misturadas às ativas:** `60` linhas em `assinaturas.csv`.
2. **Registros pós-corte (`> 30/09/2026`):** `119` usuários, `122` posts e `273` amizades.
3. **Mistura de Fusos (`UTC` vs. `BRT`):** Eventos das lojas em `"Z"` + `34` treinos na 1ª hora de `01/10 UTC` que ocorreram na noite de `30/09 BRT`.
4. **Sistema Operacional despadronizado (`64.948` linhas):** `android` (`28.027`) + `Android` (`7.124`) = **`35.151`**; `ios` (`20.854`) + `iOS` (`7.463`) + `IOS` (`1.480`) = **`29.797`**.
5. **Modalidades bilíngues em `atividades.parquet` (`1.254.475` treinos):** `corrida` (`223.818`) + `run` (`162.108`) = **`385.926`**; `caminhada` (`118.024`) + `walk` (`88.509`) = **`206.533`**; `forca` (`112.704`) + `strength` (`85.548`) = **`198.252`**; `pedal` (`53.740`) + `ride` (`40.765`) = **`94.505`**; `funcional` (`145.476`); `yoga` (`113.849`); `hiit` (`109.934`).
6. **String `'nenhum'` em `relogio_conectado`:** Exige filtro explícito `LOWER(relogio_conectado) != 'nenhum'`.
7. **Estado sobrescrito em `assinaturas.csv`:** Exige reconstrução via `eventos_assinatura.csv` para cortes históricos.

---

### Ação 3: Escrever a seção com o agente de código
Nesta ação você escreve a seção a partir do seu próprio resultado. O agente ajuda a explicar, redigir e revisar. O artefato oficial entra só no final, para comparação.

**Antes de abrir o agente:** para cada anomalia, escreva uma linha com o que ela estragaria se não fosse tratada. Exemplo: "Sem converter o fuso, eventos de 30/09 caem em outubro e a série mensal de churn fica errada."

**Estrutura da seção:**
- **Tecnologia, Seção 2 (Auditoria):** uma frase de abertura dizendo quantas anomalias foram encontradas e com que consulta ou script. Depois, uma tabela com quatro colunas: número, anomalia, volume afetado e regra de tratamento. A regra deve estar escrita como instrução que outra pessoa consiga executar (ex.: "converter timestamps terminados em `Z` para `America/Sao_Paulo`").
- **Negócios, Seção 5.2 (Limitações, parte 1):** lista numerada em linguagem de negócio. Cada item diz o que a anomalia impede de afirmar. Exemplo: as fontes têm coberturas de tempo diferentes; `assinaturas` não mostra o passado.
- **Mensagem para o leitor:** o grupo sabe onde o pacote de dados engana e como cada número foi protegido.

**Prompt para o Agente de Código:**

```text
Estou construindo os meus entregáveis da Semana 5 na minha pasta `membros/nome_membro_1/semana_5_A1/` (ou na minha pasta personalizada em `membros/`). Edite apenas arquivos dentro dessa pasta. Não altere nada em `artefatos_negocios/` nem em `artefatos_tecnologia/`.

Rodei o Passo 02 no BigQuery e obtive estes números de anomalias do Data Room:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Minha leitura, uma linha por anomalia:
"""
[COLE AQUI AS SUAS LINHAS]
"""

Faça nesta ordem e pare ao final de cada etapa para eu confirmar:
1. Explique de volta o que cada anomalia é, em qual tabela e coluna ela aparece e que erro de decisão ela causaria. Diga se a minha leitura está correta. Confira se as somas das grafias de sistema operacional e das modalidades batem com os totais das tabelas.
2. Redija a Seção 2 do meu `ARTEFATO_TECH_SEMANA5_A1.md`: uma frase de abertura e uma tabela com número, anomalia, volume afetado e regra de tratamento executável.
3. Redija a parte 1 da Seção 5.2 (Limitações) do meu `ARTEFATO_NEGOCIOS_SEMANA5_A1.md`: lista numerada dizendo, em linguagem de negócio, o que cada problema dos dados impede de afirmar.
4. Só depois, leia a Seção 2 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md` e a Seção 5.2 de `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` e liste em uma tabela as diferenças entre o meu rascunho e o oficial: volumes divergentes, anomalias que faltam no meu e regras que no oficial não estão escritas de forma executável. Não copie texto do oficial para o meu arquivo.
5. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_5_A1/`, nunca `git add .`), faça o commit com a mensagem `docs(membros): passo 02 do A1 de <meu_nome>` e me mostre o hash. Depois rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

**Depois do agente:** confira se cada volume do rascunho aparece na sua saída do BigQuery. Se você não conseguiu medir uma anomalia (por exemplo, a contagem de eventos em UTC), escreva isso na seção em vez de copiar o número de outro lugar.

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (qual modalidade engaja mais):**
   ```text
   Na tabela atividades, coluna tipo (unificando corrida com run, caminhada com walk, forca com strength e pedal com ride), mostre o ranking das modalidades mais praticadas na Vitaliza com total de treinos, média de duracao_min e quantos usuários únicos praticam cada uma.
   ```
2. **No agente do repositório ou no NotebookLM (o impacto das anomalias no negócio):**
   ```text
   Leia o documento `00_comece_por_aqui/05_DOSSIE_EXHIBITS_M2.md` e o `00_comece_por_aqui/05_DOSSIE_DICIONARIO_DE_DADOS_M2.md`. Me explique, sem termos técnicos, que erro de decisão a diretoria da Vitaliza cometeria se analisasse os arquivos brutos sem filtrar as 60 cortesias, sem corrigir o fuso horário das lojas e sem separar a palavra 'nenhum' na coluna de relógio conectado.
   ```

---

## PASSO 03 — Diagnóstico da Subida do Churn em 2026: Testando as 5 Hipóteses (`H1` a `H5`)

### O que este passo ensina
Na reunião da diretoria da Vitaliza (descrita no Enunciado), cada diretor tinha um palpite sobre por que o churn subiu de **5,6% (2025) para 6,6% (2026)**: uns culpavam o aumento de preço de março, outros culpavam a falta de engajamento ou falhas técnicas.
Aqui você aprende o **teste estruturado de hipóteses (`Dado vs. Hipótese + Limite Metodológico`)**: para cada hipótese, buscamos a prova nos dados, mas também declaramos o que o dado **não** prova sozinho (ex.: `pesquisa_saida.csv` mostra 41% de reclamação de preço, mas só existe no site e sofre de viés de autosseleção).

---

### Raciocínio do passo

**Pergunta de negócio:** por que o churn mensal subiu de 5,6% para 6,6% e chegou a 8,1% em abril de 2026? Quem pergunta é a diretoria dividida. Patrícia (Head de CS) defende o Caminho A, a oferta no botão "Cancelar" do site. Marcelo (Head de Produto) defende o Caminho B, um score preditivo de queda de engajamento. Rita Fontes (CFO) quer retorno comprovado dentro do orçamento. Camila Ferraz precisa saber qual explicação os dados sustentam, porque cada causa pede uma ação diferente: preço pede oferta, canal define onde é possível agir, hábito pede ação antes do cancelamento, fricção pede correção operacional e não desconto.

**Onde olhar e por quê:**

| Hipótese | Fonte e campo | Por que é necessário | Regra no documento do case |
| :--- | :--- | :--- | :--- |
| **H1 (preço)** | `pesquisa_saida.motivo_principal`; `eventos_assinatura` (`evento`, `data_hora`, `plano`) | Motivo declarado de quem cancela e série mensal de saídas por plano. | Reajuste de R$ 34,90 para R$ 39,90 em `01/03/2026` (`01_RESUMO_EXECUTIVO_DO_CASE.md`). |
| **H2 (canal)** | `assinaturas.canal_cobranca` (resultado do Passo 01) | Mostra quantos clientes cancelam fora do alcance da Vitaliza. | Nas lojas, a Vitaliza recebe só notificações (`01_RESUMO_EXECUTIVO_DO_CASE.md`, seção 2). |
| **H3 (hábito)** | `uso_mensal` (`atividades` no `mes = '2026-09'`) + `assinaturas.renovacao_automatica` | Compara a intenção de saída entre faixas de frequência. | População de `14.753` pagantes (`06_CADERNO_DE_HIPOTESES_ANALITICAS.md`, seção 1). |
| **H4 (rede e relógio)** | `amizades`; `usuarios.relogio_conectado`; `atividades.treino_com` | Mede vínculo social e produto conectado. | Filtrar relações pós-corte (H-SOCIAL-01 no caderno). |
| **H5 (fricção)** | `tickets_suporte` (`status`, `aberto_em`); `pagamentos` (`status = 'recusado'`) | Separa problema técnico e falha de cobrança de decisão voluntária. | Status do ticket é o da exportação (H-SUPPORT-01 no caderno). |

**Sequência de raciocínio:**
1. **Escrever cada hipótese como frase testável, com população, exposição e desfecho.** Por quê: "o preço subiu" não se testa. "A saída dos mensais subiu depois de 01/03/2026 mais do que a dos anuais" se testa.
2. **Definir o desfecho antes de olhar os dados.** O churn mensal do enunciado é saídas no mês ÷ ativos no início do mês (abril: `1.154` ÷ `14.237` ≈ 8,1%). No retrato de 30/09, o sinal de saída é a renovação desligada. Por quê: sem uma definição única, cada hipótese mede uma coisa diferente.
3. **Para cada hipótese, comparar grupos.** Alto uso contra baixo uso, loja contra site, mensal contra anual. Por quê: uma taxa só significa algo quando comparada a outra.
4. **Para cada evidência, escrever o que ela não prova.** Por quê: o cruzamento de duas variáveis mostra associação, não causa. Quem treina pouco pode desligar a renovação por um terceiro motivo, como mudança de rotina.
5. **Classificar o papel de cada hipótese.** H1 como gatilho, H2 como restrição estrutural, H3 como principal preditor, H4 como barreira de saída, H5 como alavanca operacional. Por quê: cada papel leva a uma ação diferente.
6. **Ligar o resultado às duas apostas.** H2 limita o Caminho A. H3 sustenta a lógica do Caminho B, porque a queda de uso aparece antes da saída. Por quê: é essa ligação que a diretoria precisa para decidir.

**Armadilhas comuns:**
- **Tomar os `41,06%` de "preço" como motivo de toda a base.** A pesquisa existe desde `01/06/2026`, só para quem cancela no site, e é voluntária. O dicionário também registra que `289` das `643` respostas vêm de clientes que ainda estavam ativos em 30/09.
- **Comparar mensal e anual sem considerar o calendário.** O anual só renova a cada 12 meses. Ele pode parecer mais fiel apenas porque teve menos ocasiões de sair.
- **Misturar duas contagens de saída.** O dicionário distingue os `3.389` fins de assinatura de junho a setembro das `3.362` perdas da série mensal. A série conta só quem estava ativo no início do mês.
- **Ler H3 como causa.** A relação pode ter o sentido inverso: quem já decidiu sair para de treinar.
- **Ignorar o confundimento em H4** (quando um terceiro fator explica as duas coisas). No Data Room, ter relógio está ligado à faixa de treino: `8,00%` de quem treina 5 ou mais vezes tem relógio, contra `71,53%` de quem treina 1 a 4 vezes. Comparar relógio sem separar por faixa de treino mistura os dois efeitos.
- **Contar linhas de `pagamentos` como clientes.** Cada linha é uma tentativa de cobrança; o mesmo cliente pode ter várias recusas.

**Como conferir sozinho:**
- Os percentuais da pesquisa de saída somam 100; `264` ÷ `643` ≈ `41,06%`.
- Tickets: `65,97%` + `22,18%` + `11,85%` somam 100, e `22,18%` + `11,85%` = `34,03%` pendentes.
- As três faixas de treino somam `14.753`. A faixa de 5 ou mais treinos tem `7.049` pessoas (`113` com renovação desligada); a de 1 a 4, `5.391` (`819`); a de zero, `2.313` (`1.318`). Esses números reaparecem no Passo 04. Se não baterem, a junção com `uso_mensal` está diferente.
- `113` + `819` + `1.318` = `2.250`, o mesmo total de saída contratada do Passo 01.

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `eventos_assinatura`, `assinaturas`, `pesquisa_saida`, `uso_mensal`, `amizades`, `pagamentos` e `tickets_suporte`

* **Prompt para o agente do BigQuery:**
  ```text
  Precisamos testar as 5 hipóteses de negócio para explicar por que o churn mensal subiu de 5,6% (2025) para 6,6% (2026, com pico de 8,1% em abril):
  - H1 (Reajuste do Mensal em 01/03/2026 para R$ 39,90): na tabela pesquisa_saida (643 respostas), quantas e qual o % citam 'preco' como motivo_principal? E na evolução de eventos_assinatura, como se comportaram as saídas em abril de 2026?
  - H2 (Assimetria de Canal - Lojas): qual o % dos 14.753 pagantes ativos que pagam por app_store ou google_play, onde a tela de cancelamento do site não alcança?
  - H3 (Queda de Frequência de Treino): cruzando os 14.753 pagantes ativos de assinaturas com uso_mensal (mes = '2026-09', coluna atividades = treinos no mês; quem não tem linha conta como 0), qual é a taxa de renovação desligada (renovacao_automatica = 'nao') para quem treinou >= 5 vezes no mês, para quem treinou de 1 a 4 vezes e para quem teve 0 treinos?
  - H4 (Rede Social e Relógio Conectado): qual o total de vínculos em amizades (coluna desde até 30/09/2026) e qual a diferença na taxa de renovação desligada entre quem possui relógio conectado (usuarios.relogio_conectado = 'garmin' ou 'apple_watch') versus quem tem 'nenhum'?
  - H5 (Churn Involuntário e Suporte Técnico): na tabela tickets_suporte (4.422 chamados, coluna aberto_em até 30/09/2026), qual o % de tickets com status 'resolvido', 'aberto' e 'sem_resposta'? E na tabela pagamentos, quantas cobranças têm status 'recusado'?
  ```

---

### Ação 2: Conferir o resultado
* **H1 (Preço/Reajuste):** Pico de **8,1% em abril/2026** (`1.154` saídas); na `pesquisa_saida.csv`, **`preco` = `41,06%` (`264` de `643` respostas)**.
* **H2 (Assimetria Lojas):** **`70,22%` (`10.359`)** nas lojas (`app_store` + `google_play`).
* **H3 (Frequência):** `≥5` treinos = apenas **`1,60%`** de renovação desligada; `1 a 4` treinos = **`15,19%`**; `0` treinos = **`56,98%`**.
* **H4 (Social/Relógio):** `113.207` relações até 30/09/2026 (`113.480` no arquivo). `38,20%` dos pagantes têm relógio, com `15,49%` de renovação desligada, contra `15,10%` sem relógio: não há efeito protetor. Número de amigos também não separa o risco (`11,55%` com 0 amigos, `16,61%` com 1 a 5, `11,15%` com 6 ou mais). Treinar acompanhado ao menos uma vez: `12,55%` contra `15,59%`.
* **H5 (Suporte/Pagamentos):** Dos `4.422` tickets, **`65,97%` resolvidos**, **`22,18%` abertos** e **`11,85%` sem resposta** (`34,03%` pendentes).

---

### Ação 3: Escrever a seção com o agente de código
Nesta ação você escreve a seção a partir do seu próprio resultado. O agente ajuda a explicar, redigir e revisar. O artefato oficial entra só no final, para comparação.

**Antes de abrir o agente:** para cada hipótese, escreva duas linhas. A primeira diz o que o dado mostra. A segunda diz o que o dado não prova.

**Estrutura da seção:**
- **Negócios, Seção 2 (Diagnóstico):** uma frase de abertura com a evolução do churn (5,6%, 6,6% e pico de 8,1% em abril). Depois, uma tabela com três colunas: hipótese; evidência (número, tabela e população); conclusão com o limite metodológico. Cada linha termina com o papel da hipótese: gatilho, restrição, preditor, barreira ou alavanca.
- **Parágrafo de fechamento:** o que o diagnóstico muda na decisão. Ligue H2 ao alcance do Caminho A e H3 à lógica do Caminho B.
- **Negócios, Seção 5.2 (Limitações, parte 2):** a pesquisa de saída cobre só o site e é voluntária; cruzamentos bivariados não provam causa.
- **Tecnologia, Seção 1 (complemento opcional):** uma lista curta com a consulta, a população e a janela usadas em cada hipótese. O artefato oficial de Tecnologia não tem um bloco separado de EDA (análise exploratória); se você incluir, mantenha só o que permite repetir o teste.
- **Mensagem para o leitor:** o reajuste de março coincide com o pico de abril, e a frequência de treino é o fator que mais separa quem fica de quem sai.

**Prompt para o Agente de Código:**

```text
Estou construindo os meus entregáveis da Semana 5 na minha pasta `membros/nome_membro_1/semana_5_A1/` (ou na minha pasta personalizada em `membros/`). Edite apenas arquivos dentro dessa pasta. Não altere nada em `artefatos_negocios/` nem em `artefatos_tecnologia/`.

Rodei o Passo 03 no BigQuery testando as 5 hipóteses da subida do churn em 2026:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Minha leitura, duas linhas por hipótese (o que mostra / o que não prova):
"""
[COLE AQUI AS SUAS LINHAS]
"""

Faça nesta ordem e pare ao final de cada etapa para eu confirmar:
1. Explique de volta cada hipótese: qual comparação foi feita, qual população, qual número responde e o que esse número não prova. Diga se a minha leitura está correta. Confira se os percentuais de cada distribuição somam 100 e se as faixas de treino somam 14.753.
2. Redija a Seção 2 do meu `ARTEFATO_NEGOCIOS_SEMANA5_A1.md`: frase de abertura, tabela das 5 hipóteses (hipótese / evidência com número, tabela e população / conclusão com limite e papel da hipótese) e um parágrafo de fechamento ligando H2 ao Caminho A e H3 ao Caminho B. Marque como hipótese tudo o que não for medido.
3. Acrescente na Seção 5.2 do mesmo arquivo as limitações da pesquisa de saída e da leitura causal dos cruzamentos.
4. Só depois, leia a Seção 2 de `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` e liste em uma tabela as diferenças entre o meu rascunho e o oficial: números divergentes, hipóteses com conclusão diferente, evidências do oficial que eu não medi (como o resultado da campanha de agosto) e afirmações do oficial sem número. Não copie texto do oficial para o meu arquivo.
5. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_5_A1/`, nunca `git add .`), faça o commit com a mensagem `docs(membros): passo 03 do A1 de <meu_nome>` e me mostre o hash. Depois rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

**Depois do agente:** se o oficial cita uma evidência que você não mediu, você tem duas opções: rodar a consulta e incluir o número com a fonte, ou deixar de fora. Não inclua números sem consulta.

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (o "gêmeo demográfico" da Aula 3 de Negócios):**
   ```text
   Cruze usuarios, assinaturas e uso_mensal (mes = '2026-09'). Filtre apenas clientes com a mesma faixa de idade (26 a 30 anos, calculada por data_nascimento) e o mesmo sexo. Agora compare a taxa de renovação desligada (renovacao_automatica = 'nao') de quem fez 8 ou mais atividades no mês contra quem fez apenas 1. O que isso mostra sobre segmentar por idade versus segmentar por comportamento?
   ```
2. **No agente do repositório ou no NotebookLM (as Aulas 1 e 3 aplicadas ao case):**
   ```text
   Leia o arquivo `00_comece_por_aqui/06_CADERNO_DE_HIPOTESES_ANALITICAS.md` e o `00_comece_por_aqui/03_GUIA_AULA_01_NEGOCIOS_E_TECNOLOGIA.md`. Com base nos números que encontramos nas 5 hipóteses (H1 a H5), me ajude a construir um argumento mostrando por que o aumento de preço de março foi o gatilho, mas a falta de hábito (< 5 treinos/mês) é a causa raiz do cancelamento.
   ```

---

## PASSO 04 — Os 4 Segmentos Estratégicos (Pilar 01), Personas de Dados (Pilar 02) e Receita em Risco com `4A` vs. `4B` (Pilar 03)

### O que este passo ensina
Este passo cobre os **3 Pilares Obrigatórios da Entrega A1 de Negócios** e o **Objetivo 3 de Tecnologia**:
1. **Regra de Ouro da Clusterização (Sem Vazamento):** Você nunca coloca a coluna `churn` / `renovacao_automatica` dentro das variáveis que formam os grupos. Os grupos são formados exclusivamente pelo **comportamento no produto** (quantas vezes treina, quantos minutos, se treina ao ar livre com GPS ou em casa por vídeo). Só depois que os 4 grupos estão prontos é que olhamos a taxa de saída de cada um.
2. **Os 5 Critérios de Kotler (Aula 3):** Todo segmento precisa ser *Mensurável, Substancial, Diferenciável, Acessível e Acionável*.
3. **A Divisão Crítica do Cluster 4 (`4A` vs. `4B`):** Entre os `2.313` inativos (`0` treinos em setembro), `1.318` (`4A`) já desligaram a renovação automática, mas **`995` (`4B`) ainda estão com a renovação ligada pagando R$ 23.983/mês por esquecimento**. Esses `995` são os **Sleeping Dogs**: se você mandar um WhatsApp dizendo *"Sentimos sua falta!"*, você lembra o cliente de que ele está pagando sem usar, e ele tende a cancelar.

---

### Raciocínio do passo

**Pergunta de negócio:** em quais assinantes a Vitaliza deve investir e quais deve deixar sem contato? É a decisão central do case, formulada para Camila Ferraz: escolher dentro do teto de R$ 40.000/mês, com no máximo 1.500 mensagens de WhatsApp e 300 atendimentos de CS por mês. Rita Fontes (CFO) precisa saber quanto dinheiro está em risco em cada grupo. Marcelo (Head de Produto) precisa saber que ação de produto cabe a cada grupo. Patrícia (Head de CS) precisa saber onde usar os 300 atendimentos.

**Onde olhar e por quê:**

| Fonte | Campo | Por que é necessário |
| :--- | :--- | :--- |
| `uso_mensal` (`mes = '2026-09'`) | `atividades` (treinos no mês), `atividades_ar_livre`, `minutos`, `dias_ativos`, `sessoes_app` | Comportamento recente de uso, que forma os grupos. |
| `usuarios` | `relogio_conectado` | Produto conectado, uma das variáveis de entrada do protocolo da Seção 3.1 de Tecnologia. |
| `amizades` | relações até o corte | Grau social, outra variável de entrada do mesmo protocolo. |
| `assinaturas` | `plano_atual`, `canal_cobranca` | Receita líquida de cada cliente, com as regras do Passo 01. |
| `assinaturas` | `renovacao_automatica` | Usada só depois de formar os grupos, para descrever o risco e dividir o Cluster 4. |
| Resultado da campanha de `10/08/2026` (`campanha_ago26`), citado na Seção 5.1 do artefato oficial | churn dos inativos com e sem contato (`51,86%` contra `61,02%`) | É a evidência que sustenta o rótulo *Sleeping Dog* (cliente que cancela quando é lembrado da cobrança). |
| `00_comece_por_aqui/04_contexto_extra/01_VISAO_DETALHADA_SEMANA5_VS_SEMANA10.md`, seção 2.1 | Os 3 pilares e as boas práticas | Exige 3 a 4 clusters por comportamento, nomes com intenção estratégica e uma variável comprovada para cada atributo de persona. |
| `00_comece_por_aqui/01_trilha_negocios_e_crm/01_DIAGNOSTICO_ESTRATEGICO_A1_SEMANA5.md`, seção 7 | Modelo de persona e matriz impacto × acionabilidade | Lista os campos obrigatórios de cada persona. |

**Sequência de raciocínio:**
1. **Escolher variáveis de comportamento anteriores ao corte.** Por quê: o segmento precisa descrever o que o cliente faz. É isso que produto e CRM conseguem influenciar.
2. **Deixar a variável de saída fora da formação dos grupos.** Por quê: se a renovação desligada entra no cálculo, os grupos separam o churn por construção, e a taxa observada depois deixa de ser evidência. Isso é vazamento de alvo.
3. **Formar os grupos e declarar o método.** O prompt deste passo usa regras de corte: 5 ou mais treinos no mês (hábito estabelecido, pouco mais de um treino por semana), 1 a 4 (hábito instável) e zero (sem uso). Dentro do grupo de 5 ou mais, separa quem faz metade ou mais dos treinos ao ar livre. A Seção 3.1 do artefato de Tecnologia descreve uma clusterização com sete variáveis padronizadas (`StandardScaler`, que coloca todas na mesma escala). Por quê: o leitor precisa saber se os grupos vieram de regra ou de algoritmo. Escreva na seção o método que você de fato executou.
4. **Ler os centróides.** Centróide é a média de cada variável dentro do grupo, na unidade original (treinos/mês, minutos/mês). Por quê: é o que permite descrever o grupo em linguagem de negócio.
5. **Qualificar cada grupo:** tamanho, % da base e receita líquida. Por quê: o Pilar 01 pede essas medidas, e elas respondem aos critérios de Kotler "mensurável" e "substancial".
6. **Só então cruzar com a renovação desligada.** Por quê: é a validação de negócio. Grupos formados apenas por comportamento que mostram taxas tão diferentes (`1,61%` contra `56,98%`) indicam que a segmentação separa risco.
7. **Dividir o Cluster 4 em 4A e 4B pela renovação.** Por quê: aqui a variável de saída serve para decidir a ação, não para formar o grupo. Por isso não há vazamento. O 4A (`1.318`) já decidiu sair. O 4B (`995`) ainda paga com renovação ligada. As ações são opostas: no 4A, tentar reverter antes do fim do período; no 4B, não fazer contato.
8. **Calcular o valor em risco.** Valor em risco mensal = soma da receita líquida mensal dos clientes com renovação desligada no grupo. Anualizado = mensal × 12. No 4B, o risco é condicional: a receita só se perde se o grupo for acordado por contato. Por quê: Rita Fontes compara esses valores com o orçamento de R$ 40.000/mês.
9. **Montar a matriz impacto × acionabilidade.** Impacto é a receita em risco. Acionabilidade é a existência de canal, oferta e janela para agir. Por quê: é essa matriz que ordena a fila de testes do A2.

**Persona de dados versus persona inventada:**
- **Persona inventada** começa por uma pessoa imaginada ("Ana, 32 anos, executiva, gosta de yoga") e depois procura dados que a confirmem. Idade, profissão e gostos aparecem sem fonte, muitas vezes em variáveis que a segmentação nem usou.
- **Persona de dados** começa pelo grupo medido. O nome descreve o comportamento que diferencia o grupo. Cada frase aponta para uma coluna e um número. A persona termina com a ação de negócio que se propõe para ela. Se uma frase não tem número por trás, ela é retirada ou marcada como hipótese.

**Do centróide à persona, em quatro passos:**
1. **Comparar o centróide com a média da base.** A média da base é `6,6` treinos/mês. O que diferencia o grupo é o que fica muito acima ou muito abaixo dessa média.
2. **Dar o nome pelo comportamento dominante.** "Corredor Conectado de Parque" vem de 5 ou mais treinos no mês, com metade ou mais ao ar livre. Evite nomes que atribuem efeito não medido. O documento de diagnóstico A1 adverte que rótulos como "persuadível" ou "sleeping dog" exigem evidência específica. No artefato do grupo, o rótulo *Sleeping Dog* se apoia no resultado da campanha de agosto. Cite essa evidência quando usar o rótulo.
3. **Anexar os números:** N, % da base, treinos e minutos médios, taxa de renovação desligada observada depois, receita líquida mensal.
4. **Escrever o motivo provável de saída como hipótese marcada e a ação com canal e custo.**

Exemplo com o Cluster 3:
- Centróide: `2,2` treinos e `99,3` minutos por mês, bem abaixo da média de `6,6` treinos. Leitura: treina, mas sem regularidade.
- Nome: "Entusiasta Oscilante".
- Números: `5.391` clientes (`36,54%`), `15,19%` com renovação desligada, R$ 151.968/mês de receita líquida e R$ 19.303/mês em risco direto.
- Motivo provável (hipótese): sensibilidade ao preço depois do reajuste, somada à quebra de hábito.
- Ação: primeiro público dos testes de CRM do A2. Como o grupo é maior que a cota de 1.500 WhatsApps, será preciso priorizar dentro dele.

**Armadilhas comuns:**
- **Usar a renovação desligada para formar os grupos.** Sinal: um grupo com taxa de saída próxima de zero e outro próximo do total, com separação perfeita demais.
- **Escolher os pontos de corte olhando a taxa de saída.** Se o corte de 5 treinos foi escolhido porque a taxa muda ali, a separação observada depois fica otimista. Justifique o corte por critério de produto ou declare isso como limitação.
- **Usar `JOIN` em vez de `LEFT JOIN` com `uso_mensal`.** Cliente sem linha em setembro precisa entrar com zero treinos. Sinal: o Cluster 4 encolhe e o total não chega a `14.753`.
- **Nomes genéricos** ("Cluster 0") ou que prometem efeito sem evidência.
- **Atributo de persona sem número.** Uma versão anterior do artefato oficial descrevia o Cluster 1 como usuário de relógio Garmin ou Apple Watch. A consulta mostrou que só `8,46%` do grupo tem relógio. Toda frase de persona precisa de uma consulta por trás; se você não rodar, retire a frase.
- **Escrever o motivo de saída como fato.** Ele é hipótese até ser testado.
- **Tratar o 4B como perda certa.** É um risco condicional ao contato.
- **Anualizar sem declarar a premissa.** Multiplicar por 12 supõe que o cliente ficaria 12 meses. No anual com renovação desligada, a perda só acontece no fim do ciclo.

**Como conferir sozinho:**
- `4.089` + `2.960` + `5.391` + `2.313` = `14.753`.
- Receita: R$ 117.682 + R$ 86.795 + R$ 151.968 + R$ 53.496 = R$ 409.941, o mesmo total do Passo 01.
- Cluster 4: `1.318` + `995` = `2.313`; R$ 29.513 + R$ 23.983 = R$ 53.496.
- Renovação desligada: `113` (Clusters 1 e 2) + `819` (Cluster 3) + `1.318` (4A) = `2.250`, o mesmo total do Passo 01.
- Anualização (mensal × 12; diferenças de poucos reais vêm dos centavos): R$ 19.303 → R$ 231.640; R$ 29.513 → R$ 354.151; R$ 23.983 → R$ 287.792.
- Média dos centróides ponderada pelo tamanho de cada grupo: `6,6` treinos e `293,8` minutos por mês, que deve ser a linha de total da sua tabela.
- Para verificar atributos de persona, peça ao agente do BigQuery: "Para cada um dos 4 clusters deste passo, mostre o % com relógio conectado (excluindo `nenhum`), a média de amigos até 30/09/2026 e a distribuição por plano e canal."

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `assinaturas` + `uso_mensal` + `usuarios`

* **Prompt para o agente do BigQuery:**
  ```text
  Cruze os 14.753 pagantes ativos da tabela assinaturas (status_atual = 'ativa' e plano_atual IN ('mensal', 'anual')) com a tabela uso_mensal (mes = '2026-09', usando LEFT JOIN: quem não tem linha conta com 0 atividades) e com a tabela usuarios pelo user_id.
  1. Primeiro, agrupe os 14.753 pagantes nos 4 Clusters Comportamentais (sem usar a variável de saída na definição dos grupos):
     - Cluster 1 (Atletas Sociais de Rua & GPS): atividades >= 5 e atividades_ar_livre >= (atividades / 2)
     - Cluster 2 (Praticantes Regulares Indoor & Vídeo): atividades >= 5 e atividades_ar_livre < (atividades / 2)
     - Cluster 3 (Entusiastas Oscilantes / Em Risco): atividades entre 1 e 4
     - Cluster 4 (Pagantes Inertes / 0 treinos): atividades = 0 (ou sem registro em set/26)
     Mostre para cada Cluster: tamanho (N), % da base, média de atividades, média de minutos, % com renovação desligada (renovacao_automatica = 'nao', observada a posteriori) e Receita Líquida Mensal Total (com os preços e taxas do Passo 01).
  2. Depois, para montarmos a Matriz de Valor em Risco (Pilar 03), divida o Cluster 4 (2.313 inativos) em dois subgrupos:
     - Cluster 4A (Inertes que JÁ desligaram a renovação automática = 1.318 clientes)
     - Cluster 4B (Inertes que ainda estão com renovação automática LIGADA pagando por esquecimento = 995 Sleeping Dogs)
     Mostre a Receita Líquida Mensal e Anualizada (12x) em risco de cada grupo.
  ```

---

### Ação 2: Conferir o resultado
* **Cluster 1 (`4.089` | `27,72%`):** `12,4` treinos/mês, `615,4` min, **`1,61%`** renovação desligada, Receita Líquida = **`R$ 117.682 / mês`**.
* **Cluster 2 (`2.960` | `20,06%`):** `11,9` treinos/mês, `433,5` min, **`1,59%`** renovação desligada, Receita Líquida = **`R$ 86.795 / mês`**.
* **Cluster 3 (`5.391` | `36,54%`):** `2,2` treinos/mês, `99,3` min, **`15,19%` (`819` clientes)** renovação desligada, Receita Líquida = **`R$ 151.968 / mês`** (Receita em risco direto = **`R$ 19.303/mês` ou `R$ 231.640/ano`**).
* **Cluster 4 (`2.313` | `15,68%`):** `0,0` treinos/mês, **`56,98%`** renovação desligada, Receita Líquida = **`R$ 53.496 / mês`**, dividido em:
  * **Cluster 4A (`1.318` com renovação desligada):** **`R$ 29.513/mês` (`R$ 354.151/ano`)**;
  * **Cluster 4B (`995` *Sleeping Dogs* com renovação ligada):** **`R$ 23.983/mês` (`R$ 287.792/ano`)**.

---

### Ação 3: Escrever as seções com o agente de código
Nesta ação você escreve as seções a partir do seu próprio resultado. O agente ajuda a explicar, redigir e revisar. O artefato oficial entra só no final, para comparação.

**Antes de abrir o agente:** para cada cluster, escreva quatro linhas: o comportamento que o diferencia (com o número do centróide), o nome que você daria, o motivo provável de saída (marcado como hipótese) e a ação que você proporia.

**Estrutura da seção:**
- **Negócios, Seção 3 (Pilar 01, segmentação):** um parágrafo de método com a população, as variáveis usadas, a regra ou o algoritmo, e a frase "a variável de saída não entrou na formação dos grupos". Depois, um diagrama ou lista dos 4 segmentos e a tabela consolidada: N, % da base, treinos/mês, minutos/mês, % de renovação desligada observada depois, receita líquida mensal e papel no CRM, com linha de total.
- **Negócios, Seção 4 (Pilar 02, personas):** uma tabela com uma coluna por persona e linhas para nome (pelo comportamento), quem é e o que faz no produto (com números), motivo provável de saída (marcado como hipótese), custo da perda e ação proposta. Cada atributo precisa de uma variável medida por trás.
- **Negócios, Seção 5.1 (Pilar 03, valor em risco):** tabela com Cluster 3, Cluster 4A, Cluster 4B e Clusters 1 e 2. Colunas: N, receita líquida mensal, taxa de renovação desligada, receita mensal em risco, receita anualizada e prioridade (impacto × acionabilidade). Uma nota abaixo da tabela com a premissa da anualização. Um callout sobre o 4B: o risco só se materializa se o grupo for contatado, e a evidência vem da campanha de agosto.
- **Tecnologia, Seção 3:** 3.1 com o protocolo contra vazamento (variáveis de entrada, padronização, exclusão do alvo) e a tabela de centróides dos 4 clusters, com a taxa de renovação desligada marcada como "observada depois".
- **Mensagem para o leitor:** a maior receita recuperável está no Cluster 3. Os Clusters 1 e 2 não precisam de desconto. O 4B deve ficar sem contato.

**Prompt para o Agente de Código:**

```text
Estou construindo os meus entregáveis da Semana 5 na minha pasta `membros/nome_membro_1/semana_5_A1/` (ou na minha pasta personalizada em `membros/`). Edite apenas arquivos dentro dessa pasta. Não altere nada em `artefatos_negocios/` nem em `artefatos_tecnologia/`.

Rodei o Passo 04 no BigQuery e obtive a tabela dos 4 clusters e a abertura do valor em risco (incluindo 4A e 4B):
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

Minha leitura, quatro linhas por cluster (comportamento com número / nome / motivo provável de saída como hipótese / ação proposta):
"""
[COLE AQUI AS SUAS LINHAS]
"""

Faça nesta ordem e pare ao final de cada etapa para eu confirmar:
1. Explique de volta o resultado: como os grupos foram formados, por que a renovação desligada não entrou na formação, o que cada centróide diz e por que a divisão 4A/4B não é vazamento. Confira se os tamanhos somam 14.753, se a receita soma o total do Passo 01 e se as renovações desligadas somam 2.250. Diga se a minha leitura e os meus nomes estão sustentados pelos números.
2. Redija no meu `ARTEFATO_NEGOCIOS_SEMANA5_A1.md` a Seção 3 (método, diagrama e tabela consolidada com total), a Seção 4 (personas de dados: cada atributo com o número e a coluna correspondente, motivo de saída marcado como hipótese, ação proposta) e a Seção 5.1 (valor em risco mensal e anualizado, prioridade, nota sobre a premissa da anualização e callout sobre o 4B). Se alguma frase de persona não tiver número no meu resultado, deixe-a marcada como [A VERIFICAR] em vez de inventar.
3. Redija no meu `ARTEFATO_TECH_SEMANA5_A1.md` a Seção 3: protocolo contra vazamento e tabela de centróides. Escreva qual método eu executei (regras de corte ou algoritmo de clusterização).
4. Só depois, leia as Seções 3, 4 e 5.1 de `artefatos_negocios/semana_5_A1/ARTEFATO_NEGOCIOS_SEMANA5_A1.md` e a Seção 3 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`. Liste em uma tabela as diferenças entre o meu rascunho e o oficial: números divergentes, atributos de persona do oficial que não têm número na consulta, diferenças de método e de nome. Não copie texto do oficial para o meu arquivo.
5. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_5_A1/`, nunca `git add .`), faça o commit com a mensagem `docs(membros): passo 04 do A1 de <meu_nome>` e me mostre o hash. Depois rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

**Depois do agente:** resolva cada item marcado como [A VERIFICAR]. Rode a consulta de verificação sugerida em "Como conferir sozinho" ou retire a frase. Uma persona com menos atributos e todos medidos vale mais do que uma persona completa com atributos sem fonte.

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (casos reais dentro de cada persona):**
   ```text
   Cruze assinaturas, usuarios, uso_mensal e onboarding. Mostre o perfil real de 2 clientes do Cluster 1 (Atletas GPS) e de 2 clientes do Cluster 3 (Entusiastas Oscilantes de 1 a 4 treinos), trazendo o objetivo_texto que eles escreveram no onboarding e quantas atividades fizeram em julho, agosto e setembro (mes = '2026-07', '2026-08' e '2026-09').
   ```
2. **No agente do repositório ou no NotebookLM (os 4 segmentos pelos 5 critérios de Kotler):**
   ```text
   Leia o arquivo `00_comece_por_aqui/01_trilha_negocios_e_crm/01_DIAGNOSTICO_ESTRATEGICO_A1_SEMANA5.md` e avalie os nossos 4 segmentos (Atletas GPS, Praticantes Vídeo, Entusiastas Oscilantes e Pagantes Inertes) segundo os 5 critérios clássicos de segmentação vistos em aula (Mensurável, Substancial, Diferenciável, Acessível e Acionável). Qual ação concreta de produto ou CRM faz sentido para cada um?
   ```

---

## PASSO 05 — Feature Store Tabular (`M-1` vs. `M-2`) e Baseline Supervisionado de Regressão Logística (60 Dias)

### O que este passo ensina
Para prever quem vai sair nos próximos 60 dias (**Objetivo 4**), o modelo não pode olhar apenas para uma fotografia estática: ele precisa capturar **a velocidade da queda de hábito (`delta_treinos = treinos_m1 - treinos_m2`)**.
Além disso, você aprende as **4 métricas usadas para avaliar um classificador de churn**:
* **`ROC-AUC` (`0,7522` no nosso Baseline):** Capacidade global de ranquear um cliente que vai sair acima de um cliente que vai ficar (`0,50` = cara ou coroa; `1,00` = perfeito).
* **`PR-AUC` (`0,5079`):** Foco em precisão e cobertura na classe minoritária (quem realmente sai).
* **`Brier Score` (`0,1504`):** Mede se a probabilidade prevista (ex.: 30% de chance de sair) é calibrada com a realidade (quanto menor, melhor).
* **`Lift no Topo 10%` (`2,55x`):** Como só temos **1.500 mensagens de WhatsApp por mês** (~10% dos 14.753 ativos), o `Lift@10% = 2,55x` mostra que abordar o topo 10% do ranking do modelo encontra **2,55 vezes mais cancelamentos reais** do que escolher 1.500 clientes por sorteio.

---

### Raciocínio do passo

**Pergunta de negócio:** dá para saber, semanas antes, quem vai sair, com precisão suficiente para gastar os 1.500 WhatsApps do mês em quem importa? Quem pergunta é Marcelo (Head de Produto), que defende o Caminho B: um score preditivo de queda de engajamento. Rita Fontes (CFO) quer saber se a lista do modelo gera retorno dentro do orçamento. Diego Almeida (CTO) quer saber se o pipeline sustenta esse cálculo. O anúncio do Strava Premium, que lança modelos individuais de risco no Brasil, aumenta a pressão. Dessa resposta depende a decisão de investir em modelo preditivo e o critério para escolher quem recebe contato.

**Onde olhar e por quê:**

| Fonte | Campo ou variável | Por que é necessário |
| :--- | :--- | :--- |
| `uso_mensal` em dois meses seguidos antes do corte (M-1 e M-2) | treinos, minutos, dias ativos, sessões | Nível de uso e tendência recente (`delta_treinos`). |
| `assinaturas` | `plano_atual`, `canal_cobranca` | `is_mensal` (exposto ao reajuste) e `is_loja` (fora do alcance do site). |
| `usuarios` | `relogio_conectado` | `tem_relogio`, com o tratamento de `nenhum` do Passo 02. |
| `amizades`, `tickets_suporte`, `pagamentos` | registros até o corte | `n_amigos`, `n_tickets` e `n_recusas`. |
| `eventos_assinatura` | eventos de saída e de renovação desligada | Construir o alvo em cortes passados, já que `assinaturas` não guarda o histórico. |
| `00_comece_por_aqui/04_contexto_extra/01_VISAO_DETALHADA_SEMANA5_VS_SEMANA10.md`, seção 4, item 2 | Definição de saída | Saída é renovação desligada ou sem assinatura vigente ao fim da janela, incluindo falha de pagamento não recuperada, reembolso e chargeback. |
| `00_comece_por_aqui/06_CADERNO_DE_HIPOTESES_ANALITICAS.md`, seção 1 | Contrato analítico | Horizonte de 60 dias, validação fora do tempo, nenhuma variável posterior ao corte. |
| `00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md`, seção 4 | Cota de canais | 1.500 WhatsApps por mês, cerca de 10% da base pagante. |

**Sequência de raciocínio:**
1. **Definir o alvo.** Saída em 60 dias, com a definição da Visão Detalhada. Por quê: o modelo aprende o que for definido como saída. Uma definição diferente produz um modelo diferente.
2. **Escolher um corte histórico com os 60 dias já observados (`31/07/2026`).** Por quê: no corte de 30/09 ainda não se sabe quem vai sair até 29/11. Sem desfecho conhecido, não há como medir acerto.
3. **Calcular as variáveis só com dados até o corte.** No corte de 31/07, M-1 é julho e M-2 é junho. Por quê: qualquer dado posterior ao corte é vazamento e infla as métricas.
4. **Criar `delta_treinos = treinos_m1 − treinos_m2`.** Por quê: um único mês não distingue quem sempre treinou pouco de quem está caindo. A queda recente é o sinal que o Caminho B quer captar.
5. **Treinar a regressão logística.** É um modelo que estima a probabilidade de saída a partir de uma soma ponderada das variáveis. `StandardScaler` coloca as variáveis na mesma escala. `L2` é uma penalização que evita pesos extremos. Por quê: é simples, os pesos podem ser lidos, e serve de referência para os modelos da Semana 10.
6. **Validar fora do tempo.** O modelo é avaliado em um período posterior ao usado para treinar. Por quê: o uso real é prever o futuro. Misturar períodos no treino e no teste infla a métrica.
7. **Ler as métricas na ordem da decisão.** Primeiro o `Lift@10%`, porque a cota de 1.500 WhatsApps corresponde a cerca de 10% da base. Depois `ROC-AUC` (ordenação), `PR-AUC` (desempenho na classe de quem sai) e `Brier` (calibração da probabilidade).
8. **Ler os pesos e checar se o sinal faz sentido para o negócio.** Queda de treinos, plano mensal, recusas de pagamento e ausência de relógio aumentam o risco. Por quê: um peso com sinal contrário ao esperado indica erro de dado ou de variável.
9. **Usar a consulta do BigQuery como checagem descritiva.** Ela compara as médias das variáveis entre quem manteve e quem desligou a renovação, no retrato de 30/09. Por quê: confirma que os sinais existem na base atual, mas não treina nem avalia o modelo.

**Armadilhas comuns:**
- **Achar que a consulta reproduz `ROC-AUC = 0,7522`.** Ela não reproduz. Usa o retrato de 30/09 e só compara médias. As métricas vêm do modelo treinado no corte de 31/07. Este repositório não traz o código desse modelo. Registre na seção como as métricas foram obtidas.
- **Usar o retrato de 30/09 para treinar.** A renovação desligada em 30/09 e o uso de setembro são medidos no mesmo momento. A relação entre os dois mostra coincidência no tempo, não antecedência.
- **Usar `assinaturas` para saber quem estava ativo em 31/07.** A tabela mostra só a situação em 01/10/2026. Use `eventos_assinatura`.
- **Ignorar a campanha de agosto.** A janela de 60 dias depois de 31/07 contém a campanha de `10/08/2026`, enviada a toda a base pagante daquele dia. Parte dos clientes recebeu mensagem dentro da janela do alvo. Declare isso como limitação.
- **Ler `ROC-AUC = 0,75` como "acerta 75%".** A métrica é a probabilidade de o modelo dar nota maior a um cliente que sai do que a um que fica, escolhidos ao acaso.
- **Comparar `PR-AUC` com 0,5.** A referência de um modelo sem informação é a taxa de saída da base, e não 0,5.
- **Contar amizades de um lado só.** A relação tem `seguidor_id` e `seguido_id`. Contar só por `seguidor_id` mede "quantas pessoas o cliente segue". Declare qual lado você usou.
- **Ler peso como causa.** Um peso positivo indica associação com a saída, controlada pelas outras variáveis do modelo. Não prova que mudar a variável muda a saída.

**Como conferir sozinho:**
- Os dois grupos da consulta (alvo 0 e alvo 1) somam `14.753`. O grupo 1 tem `2.250` clientes, o mesmo número do Passo 01.
- A direção dos sinais confere com os pesos da Seção 4.2 do artefato de Tecnologia: média de treinos menor no grupo 1, percentual com relógio menor no grupo 1, recusas maiores no grupo 1.
- `1.500` ÷ `14.753` ≈ 10%. Por isso o topo 10% é a medida certa para a cota de WhatsApp.
- `Lift@10% = 2,55x` significa que a taxa de saída entre os 10% de maior risco é 2,55 vezes a taxa média da base.
- Faixas válidas: `ROC-AUC` entre 0,5 e 1; `Brier` entre 0 e 1, quanto menor melhor. Um valor fora dessas faixas indica erro de cálculo ou de transcrição.

---

### Ação 1: Consultar no agente do BigQuery
* **Tabelas no BigQuery:** `assinaturas`, `usuarios`, `uso_mensal`, `amizades`, `tickets_suporte` e `pagamentos`

* **Prompt para o agente do BigQuery:**
  ```text
  Para o Objetivo 4 Inicial (Seção 4 do Artefato de Tecnologia da Semana 5), monte a consulta da Feature Store Tabular sem Data Leakage para os 14.753 pagantes ativos, calculando as variáveis explicativas (X):
  - Contrato e canal: is_mensal (1 se mensal, 0 se anual) e is_loja (1 se app_store/google_play, 0 se site)
  - Engajamento longitudinal, a partir de uso_mensal (colunas atividades, minutos, dias_ativos, sessoes_app): treinos_m1, minutos_m1, dias_ativos_m1, sessoes_m1 (mes = '2026-09', M-1) e treinos_m2 (mes = '2026-08', M-2), além de delta_treinos = treinos_m1 - treinos_m2 (desaceleração recente de hábito)
  - Ecossistema e fricção: tem_relogio (usuarios.relogio_conectado diferente de 'nenhum'), n_amigos (linhas em amizades com seguidor_id = cliente e desde até 30/09/2026), n_tickets (tickets_suporte com aberto_em até 30/09/2026) e n_recusas (pagamentos com status = 'recusado' e data_hora até 30/09/2026).
  Mostre a média de cada variável comparando o grupo que manteve a renovação automática ligada (renovacao_automatica = 'sim', target = 0) com o grupo que desligou (renovacao_automatica = 'nao', target = 1), comprovando os sinais que alimentam o nosso baseline de Regressão Logística.
  ```

---

### Ação 2: Conferir o resultado
* Desempenho fora da amostra do **Baseline de Regressão Logística (`StandardScaler`, `L2`)** validado no corte histórico `31/07/2026`:
  * **`ROC-AUC = 0,7522`** | **`PR-AUC = 0,5079`** | **`Brier Score = 0,1504`** | **`Lift no Topo 10% (1.500 WhatsApps) = 2,55x`**.

---

### Ação 3: Fechar os dois artefatos da Semana 5 com o agente de código
Nesta ação você escreve a seção a partir do seu próprio resultado e fecha a revisão dos dois artefatos. O agente ajuda a explicar, redigir e revisar. O artefato oficial entra só no final, para comparação.

**Antes de abrir o agente:** escreva em três frases, sem termos técnicos, o que o modelo faz, o que significa o `Lift@10% = 2,55x` para a cota de WhatsApp e qual é a principal limitação da validação.

**Estrutura da seção:**
- **Tecnologia, abertura da Seção 4 (contrato temporal):** um parágrafo com o corte (`31/07/2026`), a janela (60 dias seguintes), a definição do alvo e a população.
- **Tecnologia, Seção 4.1 (variáveis):** lista agrupada em contrato e canal, engajamento e tendência, ecossistema e fricção. Para cada variável, a definição e a tabela de origem.
- **Tecnologia, Seção 4.2 (desempenho):** tabela com `ROC-AUC`, `PR-AUC`, `Brier` e `Lift@10%`, seguida de uma frase por métrica em linguagem de negócio. Depois, um parágrafo sobre os pesos (sinal e leitura).
- **Limitações do baseline:** a campanha de agosto dentro da janela do alvo; a consulta do BigQuery não reproduz as métricas; a origem do código do modelo.
- **Negócios, revisão de coerência:** confira se os números citados no artefato de Negócios são os mesmos do artefato de Tecnologia.
- **Mensagem para o leitor:** um modelo simples já concentra 2,55 vezes mais saídas no topo da lista do que a escolha ao acaso. Isso justifica testar o Caminho B, desde que a lista seja combinada com o efeito medido do contato no A2.

**Prompt para o Agente de Código:**

```text
Estou construindo os meus entregáveis da Semana 5 na minha pasta `membros/nome_membro_1/semana_5_A1/` (ou na minha pasta personalizada em `membros/`). Edite apenas arquivos dentro dessa pasta. Não altere nada em `artefatos_negocios/` nem em `artefatos_tecnologia/`.

Rodei o Passo 05 no BigQuery comparando as variáveis entre quem manteve e quem desligou a renovação:
"""
[COLE AQUI A RESPOSTA QUE O AGENTE DO BIGQUERY GEROU]
"""

As métricas do baseline do grupo (corte de 31/07/2026, saída nos 60 dias seguintes) são: ROC-AUC = 0,7522, PR-AUC = 0,5079, Brier Score = 0,1504 e Lift@10% = 2,55x.

Minha leitura, em três frases:
"""
[COLE AQUI AS SUAS TRÊS FRASES]
"""

Faça nesta ordem e pare ao final de cada etapa para eu confirmar:
1. Explique de volta, sem termos técnicos: o que a minha consulta mostra e o que ela não mostra (ela não reproduz as métricas), o que cada métrica significa e por que o Lift@10% é a métrica mais ligada à cota de 1.500 WhatsApps. Confira se os grupos da consulta somam 14.753 e se a direção das médias faz sentido. Diga se a minha leitura está correta.
2. Redija a Seção 4 do meu `ARTEFATO_TECH_SEMANA5_A1.md`: contrato temporal, Seção 4.1 com cada variável (definição e tabela de origem), Seção 4.2 com a tabela de métricas e uma frase de negócio por métrica, parágrafo sobre os pesos e uma lista de limitações (incluindo a campanha de 10/08/2026 dentro da janela do alvo).
3. Revise os meus dois arquivos de `semana_5_A1/`: liste todo número que aparece nos dois e aponte qualquer divergência entre eles. Liste também afirmações sem fonte indicada.
4. Só depois, leia a Seção 4 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md` e liste em uma tabela as diferenças entre o meu rascunho e o oficial: variáveis, definições, leitura dos pesos e limitações que um tem e o outro não. Não copie texto do oficial para o meu arquivo.
5. COMMIT: quando eu aprovar o texto, confira se estou na branch `membros/<meu_nome>` (se não estiver, pare e me avise). Adicione só a minha pasta (`git add membros/<minha_pasta>/semana_5_A1/`, nunca `git add .`), faça o commit com a mensagem `docs(membros): passo 05 do A1 de <meu_nome>` e me mostre o hash. Depois rode `git push origin membros/<meu_nome>`; se o push for recusado por falta de permissão, me avise e siga sem ele. Nunca use `git push --force`.
```

**Depois do agente:** corrija as divergências entre os seus dois arquivos antes de qualquer outra coisa. Em seguida, passe pelo checklist da seção "Fechamento da Semana 5".

---

### Ação 4: Prompts extras
1. **No agente do BigQuery (clientes em queda brusca de uso):**
   ```text
   Cruze assinaturas com uso_mensal comparando agosto (mes = '2026-08') e setembro (mes = '2026-09'). Quantos pagantes ativos tinham 6 ou mais atividades em agosto e caíram para apenas 1 ou 2 em setembro? Qual é a taxa de renovação desligada (renovacao_automatica = 'nao') desse grupo?
   ```
2. **No agente do repositório ou no NotebookLM (o modelo sem matemática):**
   ```text
   Leia o arquivo `00_comece_por_aqui/02_trilha_ciencia_de_dados_e_ml/README.md` e a Seção 4 de `artefatos_tecnologia/semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`. Me explique como se eu estivesse apresentando para o CFO da Vitaliza o que significa o nosso modelo ter um Lift de 2,55x no topo 10% e por que isso economiza dinheiro na hora de disparar os 1.500 WhatsApps do mês.
   ```

---

## Fechamento da Semana 5

### Checklist de qualidade dos dois artefatos

Passe por cada item antes de considerar a entrega pronta.

**Coerência entre Negócios e Tecnologia**
- [ ] Os dois arquivos usam a mesma população: `14.753` pagantes ativos em `30/09/2026`, com as `60` cortesias excluídas.
- [ ] Os números que aparecem nos dois arquivos são idênticos: `14.753`, `70,22%`, `2.250` (`15,25%`), R$ 409.941/mês, tamanho e taxa de cada cluster e as métricas do baseline. Procure cada número nos dois arquivos com a busca do editor.
- [ ] Os nomes dos clusters e das personas são os mesmos nos dois arquivos.

**Rastreabilidade**
- [ ] Para cada número, você sabe dizer de qual consulta ou documento do case ele veio. Se não sabe, retire o número ou refaça a consulta.
- [ ] Subtotais e totais fecham: base por plano e canal (Passo 01), tamanhos e receita dos clusters (Passo 04), renovações desligadas somando `2.250`.
- [ ] Cada atributo de persona tem uma variável medida por trás. Os motivos de saída estão marcados como hipótese.
- [ ] O método de segmentação descrito é o que você de fato executou.

**Limitações declaradas**
- [ ] A pesquisa de saída cobre só cancelamentos no site e é voluntária.
- [ ] As fontes têm coberturas de tempo diferentes, e `assinaturas` mostra apenas a situação em `01/10/2026`.
- [ ] Os cruzamentos do diagnóstico mostram associação, não causa.
- [ ] O valor anualizado depende da premissa de multiplicar por 12.
- [ ] O baseline foi validado em uma janela que contém a campanha de `10/08/2026`.
- [ ] Nenhuma variável usa dado posterior a `30/09/2026`.

**Higiene do repositório**
- [ ] Nada fora da sua pasta foi editado. Rode `git status` e confira que só aparecem arquivos em `membros/<sua_pasta>/`. Se aparecer qualquer arquivo de `artefatos_negocios/` ou `artefatos_tecnologia/`, desfaça a alteração com `git restore <caminho_do_arquivo>`.

**Linguagem**
- [ ] Cada termo técnico é explicado na primeira vez em que aparece.

### Perguntas dos personagens do case

Peça ao seu agente para fazer o papel de um personagem do case e questionar o seu trabalho:

```text
Leia os meus dois arquivos em `membros/nome_membro_1/semana_5_A1/`. Faça o papel de Rita Fontes, CFO da Vitaliza, e me faça três perguntas difíceis sobre o A1, uma de cada vez. Espere a minha resposta antes da próxima pergunta. Ao final, diga quais respostas ficaram sem número ou sem fonte.
```

Repita o exercício com Patrícia (Head de CS) e com Marcelo (Head de Produto). Cada um vai questionar a parte que afeta a sua proposta.

### Salvar no GitHub

Cada passo já termina com um commit (última etapa do prompt da Ação 3), então o histórico da sua branch mostra o seu avanço passo a passo. No fechamento, confira se sobrou algo sem commit e envie. O passo a passo completo (branch, commit, push e pull request) está no [`03_GUIA_GIT.md`](./03_GUIA_GIT.md).

```bash
git status                                         # só devem aparecer arquivos da sua pasta em membros/
git add membros/<sua_pasta>/semana_5_A1/           # nunca git add . nem git add -A
git commit -m "docs(membros): constroi artefatos A1 da semana 5 de <seu_nome>"
git push origin membros/<seu_nome>                 # envia a sua branch, não a develop
```

Depois do push, abra o pull request da sua branch para a `develop` no GitHub.

---

**Próximo:** [**`02_PLAYBOOK_SEMANA_10_A2.md`**](./02_PLAYBOOK_SEMANA_10_A2.md).
