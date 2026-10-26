# 🧪 Caderno de Hipóteses Analíticas — Perguntas, Testes & Evidências

> **Módulo 2:** IA e Dados para Negócios — Case Vitaliza  
> **Equipe:** Projetos MBA Inteli  
> **Foco deste documento:** Registro das hipóteses e critérios de validação

[🔰 Comece por Aqui](./README.md) / Caderno de hipóteses

> Documento de trabalho para transformar opiniões em testes reproduzíveis.
>
> Uma hipótese só avança para conclusão quando há definição de população, variável, método, métrica e evidência. Antes disso, permanece como hipótese.

---

## 🧭 Como usar o caderno

1. Escolha uma pergunta que possa alterar uma decisão da Vitaliza.
2. Identifique a hipótese pelo ID existente e complete o contrato do teste.
3. Associe responsável, tarefa e análise reproduzível antes da execução.
4. Registre resultado, incerteza e interpretação após a revisão.

**Estado dos registros abaixo:** hipóteses propostas, ainda sem testes concluídos neste caderno. Contagens da auditoria são evidência inicial, não confirmação dos mecanismos investigados.

Os itens classificados como prioritários são uma proposta de organização. A equipe deve ajustar a ordem conforme dependências, cobertura e esforço real.

---

## 📐 1. Contrato analítico comum

- **Corte de features:** 30/09/2026.
- **Horizonte de previsão:** 60 dias após cada corte; no corte final, até 29/11/2026. Rótulos de treino e avaliação exigem janelas históricas completas.
- **Unidade principal:** `user_id` pagante e ativo no corte.
- **População de referência:** 14.753 pagantes, excluindo 60 cortesias; coortes com elegibilidade adicional devem explicitar sua própria contagem.
- **Chave de integração:** `user_id`.
- **Regra de vazamento:** nenhuma feature pode observar fato posterior ao corte de seu exemplo. No experimento, atributos de ajuste e segmentação precisam anteceder o sorteio de 10/08.
- **Separação temporal:** validação fora do tempo; nunca embaralhar o futuro no treino.
- **Resultado de negócio:** lucro líquido incremental, não apenas acurácia.

O experimento usa sua população sorteada e uma janela de desfecho completamente observada; não herda automaticamente a coorte nem os 60 dias da previsão final.

---

## 📝 2. Registro padrão de hipótese

Cada hipótese deve ser registrada com estes campos:

| Campo | Conteúdo obrigatório |
|---|---|
| ID | identificador estável, como `H-PRICE-01` |
| Pergunta de negócio | decisão que a hipótese pode alterar |
| Mecanismo esperado | por que o efeito faria sentido |
| População | quem entra e quem fica de fora |
| Exposição | variável ou evento investigado |
| Desfecho | churn, renovação, clique, uplift ou lucro |
| Janela | período da exposição e do desfecho |
| Fontes | arquivos e colunas usados |
| Método | comparação, teste, modelo ou desenho causal |
| Confundidores | fatores que podem explicar o mesmo efeito |
| Critério | evidência que confirma, enfraquece ou derruba a hipótese |
| Limitações | o que o teste não consegue provar |
| Acompanhamento | responsável, tarefa associada, status e referência ao código/resultado |

---

## 🔍 3. Hipóteses prioritárias

<a id="h-price-01--reajuste-do-plano-mensal"></a>

### 3.1 H-PRICE-01 — reajuste do plano mensal

**Pergunta:** o aumento de R$ 34,90 para R$ 39,90 em 01/03/2026 elevou a saída dos assinantes mensais?

- Fontes: `eventos_assinatura.csv`, `assinaturas.csv`, `pagamentos.csv`, `uso_mensal.csv`.
- Comparação: mensal vs. anual antes e depois de março, com controle por coorte, canal, tempo de casa e engajamento.
- Evidência inicial: preço aparece em 41,06% das 643 pesquisas de saída.
- Risco: a pesquisa é voluntária e restrita ao site; não representa as lojas.
- Critério: aumento diferencial e persistente do churn mensal, com intervalo de confiança e análise de sensibilidade.

<a id="h-engagement-01--queda-recente-de-uso"></a>

### 3.2 H-ENGAGEMENT-01 — queda recente de uso

**Pergunta:** redução de frequência de treino e abertura do app antecede o churn?

- Fontes: `uso_mensal.csv`, `atividades.parquet`, `eventos_assinatura.csv`.
- Features: recência, frequência, minutos, dias ativos, sessões, tendência de 30/60/90 dias e dias desde o último treino.
- Risco: atividade em 01/10 pode refletir fuso; aplicar corte em BRT.
- Critério: ganho fora do tempo sobre um baseline cadastral e calibração preservada.

<a id="h-channel-01--canal-de-cobrança-e-capacidade-de-intervenção"></a>

### 3.3 H-CHANNEL-01 — canal de cobrança e capacidade de intervenção

**Pergunta:** loja e site apresentam riscos e janelas de retenção diferentes?

- Fontes: `assinaturas.csv`, `eventos_assinatura.csv`, `pagamentos.csv`.
- Evidência de contexto: 70,22% dos pagantes ativos usam App Store ou Google Play.
- Método: curvas de sobrevivência e taxa de saída por plano, canal e tempo de casa.
- Risco: canal se associa a sistema operacional e perfil de aquisição.
- Critério: diferença consistente depois de controlar fatores observáveis.

<a id="h-social-01--vínculo-social-protege-retenção"></a>

### 3.4 H-SOCIAL-01 — vínculo social protege retenção

**Pergunta:** seguidores, pessoas seguidas e treino acompanhado reduzem a chance de saída?

- Fontes: `amizades.csv`, `atividades.parquet`, `feed_posts.csv`.
- Features: grau de entrada, grau de saída, reciprocidade, treino com companhia, frequência de posts e curtidas.
- Risco: há 273 relações e 122 posts posteriores ao corte; filtrar timestamps.
- Critério: efeito estável em validação temporal e análise por nível de engajamento.

<a id="h-support-01--fricção-técnica-e-cobrança"></a>

### 3.5 H-SUPPORT-01 — fricção técnica e cobrança

**Pergunta:** tickets técnicos, tickets sem resposta e cobranças recusadas antecedem o churn?

- Fontes: `tickets_suporte.csv`, `pagamentos.csv`, `eventos_assinatura.csv`.
- Evidência inicial: 34,03% dos tickets estavam abertos ou sem resposta na exportação.
- Features: tickets nos últimos 30/90 dias, categoria, tempo de resolução, recusa, retentativa e período de carência.
- Risco: status atual pode ter sido atualizado depois da janela analisada.
- Critério: associação temporal anterior ao desfecho e melhoria útil de recall/lift.

<a id="h-campaign-01--efeito-incremental-da-campanha"></a>

### 3.6 H-CAMPAIGN-01 — efeito incremental da campanha

**Pergunta:** desafio, cupom ou conteúdo reduziram a saída comparados ao controle?

- Fontes: `campanha_ago26.csv` e `eventos_assinatura.csv`.
- Desenho: comparação por intenção de tratar entre os grupos sorteados.
- Evidência inicial: cupom teve 16,45% de clique, o maior resultado bruto; clique não é retenção.
- Critério: diferença de churn com intervalo de confiança e tradução em receita líquida.
- Extensão: estimar heterogeneidade de efeito somente depois de validar o efeito médio.

<a id="h-multimodal-01--valor-incremental-de-texto-e-imagem"></a>

### 3.7 H-MULTIMODAL-01 — valor incremental de texto e imagem

**Pergunta:** variáveis extraídas por IA melhoram a decisão o suficiente para pagar o custo?

- Fontes: onboarding, feed, suporte, pesquisa de saída e heatmaps.
- Gate 1: schema fixo e amostra humana rotulada.
- Gate 2: qualidade da extração por campo.
- Gate 3: ganho preditivo fora do tempo.
- Gate 4: lucro incremental líquido do custo de inferência.
- Critério: ganho estatístico e financeiro; se um deles falhar, a fonte não entra em produção.

---

## 📊 4. Matriz de priorização

| Hipótese | Valor de negócio | Risco metodológico | Custo de teste | Ordem |
|---|---|---|---|---:|
| Definição da coorte e label | máximo | alto | médio | 1 |
| Queda de engajamento | alto | médio | médio | 2 |
| Reajuste de preço | alto | alto | médio | 3 |
| Canal de cobrança | alto | médio | baixo | 4 |
| Suporte e cobrança | médio/alto | médio | médio | 5 |
| Campanha e uplift | máximo | alto | médio | 6 |
| Rede social | médio | médio | médio | 7 |
| Texto e imagem | incerto | alto | alto | 8 |

---

## ✅ 5. Gate de evidência

Uma análise não pode ser descrita como conclusão se faltar qualquer item:

- consulta ou código reproduzível;
- população e datas explícitas;
- tratamento de valores ausentes e categorias;
- métrica com incerteza;
- comparação com baseline;
- verificação de vazamento temporal;
- interpretação de negócio;
- limitação registrada.

---

## 🧠 6. Template CREATE para revisar uma hipótese

```text
Contexto: [decisão, população, corte e restrições].
Papel: revise como cientista de dados responsável por validação temporal e impacto financeiro.
Exemplos: separe hipótese, evidência observada, método e limitação.
Ação: critique o plano e proponha o menor teste capaz de derrubar a hipótese.
Formato: tabela com risco, correção, métrica e critério de aceite.
Extras: não trate correlação como causalidade e não use dados após 30/09/2026.
```

---

## 📦 7. Saída esperada por hipótese

Cada teste deve gerar:

1. notebook ou script reproduzível;
2. tabela agregada sem dados pessoais;
3. gráfico com população e período no título;
4. decisão: `confirmada provisoriamente`, `enfraquecida`, `derrubada` ou `inconclusiva`;
5. próximo teste e risco residual.

“Confirmada provisoriamente” deve ser lido como compatibilidade com a evidência sob o método adotado. Não transforma associação observacional em causa. Registre tamanho de efeito e incerteza, inclusive quando o resultado for inconclusivo.

🔗 **Integração:** [Diagnóstico A1](./01_trilha_negocios_e_crm/01_DIAGNOSTICO_ESTRATEGICO_A1_SEMANA5.md) · [Experimento e retorno A2](./01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md).
