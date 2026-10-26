# 🎓 Guia Integrado da Aula 1 — Negócios, Dados & Tecnologia

> **Módulo 2:** IA e Dados para Negócios — Case Vitaliza  
> **Equipe:** Projetos MBA Inteli  
> **Foco deste documento:** Conceitos da aula aplicados ao case Vitaliza

[🔰 Comece por Aqui](./README.md) / Guia integrado da Aula 1

> Síntese integrada dos materiais `MBA_IA_Dados_Aula1_Fabio.pdf` (60 páginas) e `trilha-tech-mba-aula-1_compressed.pdf` (71 páginas).
>
> Este guia não substitui os slides. Ele organiza os conceitos da aula e os conecta ao case Vitaliza e aos entregáveis do módulo.

---

## 🧭 Como usar este guia

| Seu objetivo | Concentre a leitura em | Aplicação no projeto |
| :--- | :--- | :--- |
| Formular uma análise | seções 2 a 5 | pergunta de negócio, CREATE e ciclo CRISP-DM |
| Preparar dados | seções 6 e 7 | população, janela, fontes e disponibilidade |
| Entender os modelos | seções 8 a 10 | diferença entre previsão, geração e segmentação |
| Planejar sua contribuição | seção 11 | contratos iniciais e caderno de hipóteses |

**Materiais de referência:** [slides de Negócios](../documentos/MBA_IA_Dados_Aula1_Fabio.pdf) e [slides de Tecnologia](../documentos/trilha-tech-mba-aula-1_compressed.pdf). As aplicações práticas abaixo são orientações de estudo, não resultados executados pela equipe.

---

## 🎯 1. O problema do módulo

A Vitaliza quer responder quatro perguntas que parecem simples, mas exigem métodos diferentes:

1. Por que o churn mensal passou de 5,6% em 2025 para 6,6% entre janeiro e setembro de 2026?
2. Qual assinante ativo em 30/09/2026 tende a sair nos 60 dias seguintes?
3. Quem deve receber contato, por qual canal e com qual oferta?
4. Quanto a ação gera de retorno líquido depois de canais, descontos e IA?

A resposta não nasce de um único modelo. O módulo percorre um ciclo: formular a decisão, entender os dados, preparar uma base coerente, modelar, avaliar e transformar o resultado em uma ação de negócio.

---

## 🧠 2. A principal mudança de mentalidade

Os materiais de negócios e tecnologia convergem em um ponto: IA pode acelerar a produção de hipóteses e análises, mas não transfere a responsabilidade pela decisão.

- Um argumento plausível não é evidência.
- Correlação não prova causa.
- Um score de risco não define sozinho quem deve ser contatado.
- Um modelo sempre simplifica a realidade e sempre erra.
- O grupo precisa registrar premissas, cortes temporais, métricas e critérios de aceitação.

A pergunta correta não é “o que a IA respondeu?”. A pergunta correta é “que evidência confirma ou derruba esta hipótese?”.

---

## 📝 3. Framework CREATE para formular pedidos de análise

A trilha de negócios apresenta o framework CREATE como estrutura de contexto para IA:

| Elemento | Pergunta de controle | Aplicação no case Vitaliza |
|---|---|---|
| **C — Context** | Qual decisão, cenário e restrição importam? | Reduzir churn com orçamento de R$ 40 mil/mês e limites de 1.500 WhatsApps e 300 contatos de CS. |
| **R — Role** | Que papel ou perspectiva a IA deve assumir? | Cientista de dados, head de CRM, CFO ou responsável por Customer Success. |
| **E — Examples** | Há exemplos do formato e do nível de rigor esperados? | Tabela de hipóteses, plano de teste, definição de métrica e limiar de decisão. |
| **A — Action** | Qual tarefa concreta deve ser executada? | Formular hipóteses, propor variáveis, desenhar validação ou revisar riscos de viés. |
| **T — Type of output** | Qual formato a resposta deve seguir? | Matriz com hipótese, evidência, fonte, método, critério de aceitação e risco. |
| **E — Extras** | Quais limites ou detalhes adicionais valem? | Não usar dados posteriores ao corte; separar associação de causalidade; explicitar custo. |

### 💡 Exemplo aplicado

```text
Contexto: a Vitaliza registrou churn médio de 6,6% em 2026 contra 5,6% em 2025.
Papel: atue como cientista de dados responsável por uma análise auditável.
Exemplos: trate preço, canal, coorte, engajamento e falhas técnicas como hipóteses separadas.
Ação: produza um plano de investigação, sem afirmar causalidade antes dos testes.
Formato: tabela com hipótese, datasets, variáveis, método, métrica, risco de viés e evidência esperada.
Extras: use apenas dados disponíveis até 30/09/2026 e sinalize qualquer dado pós-corte.
```

O CREATE melhora o pedido. Ele não valida a resposta. A validação continua dependendo dos dados e do método.

---

## 📊 4. Os quatro tipos de análise

| Tipo | Pergunta | Exemplo Vitaliza | Resultado esperado |
|---|---|---|---|
| **Descritiva** | O que aconteceu? | Quantos pagantes estavam ativos no corte? Como o churn variou por mês? | Métricas reconciliadas e séries históricas. |
| **Diagnóstica** | Por que pode ter acontecido? | O reajuste do plano mensal coincide com aumento de saídas? | Hipóteses testadas, sem confundir associação com causalidade. |
| **Preditiva** | O que provavelmente acontecerá? | Qual a chance de cada assinante sair em 60 dias? | Probabilidade calibrada e ranking de risco. |
| **Prescritiva** | O que devemos fazer? | Quem contatar, com qual oferta e dentro de qual limite? | Política de decisão com custo, capacidade e retorno esperado. |

O trabalho de ciência de dados começa quando uma decisão de negócio vira uma pergunta mensurável. Ele não termina quando o modelo produz um score; termina quando o resultado pode ser avaliado e usado com segurança.

---

## 🔄 5. CRISP-DM como ciclo de trabalho

A trilha de tecnologia usa o CRISP-DM para organizar o módulo:

1. **Entendimento do negócio** — qual decisão precisa melhorar e como o sucesso será medido.
2. **Entendimento dos dados** — que fontes existem, como foram geradas e quais limitações carregam.
3. **Preparação dos dados** — integração, limpeza, definição de coorte, janela temporal e variáveis.
4. **Modelagem** — clusterização, regressão logística, árvores, bagging, boosting e uplift.
5. **Avaliação** — desempenho estatístico, calibração, lucro e adequação ao uso real.
6. **Implantação** — política de CRM, monitoramento, feedback e revisão periódica.

O ciclo não é uma escada linear. Uma inconsistência encontrada na avaliação pode obrigar a equipe a revisar a preparação dos dados ou até a pergunta de negócio.

---

## 🕒 6. O contrato temporal do case

O recorte final do enunciado considera pagantes ativos em 30/09/2026 e saída nos 60 dias seguintes, até 29/11/2026. Para transformá-lo em um protocolo implementável, registre:

| Elemento | Definição a conferir e implementar |
| :--- | :--- |
| População | pagantes ativos; se houver exclusão por renovação desligada, explicar a ponte para a coorte elegível |
| Evento de saída | distinguir desligamento de renovação e término efetivo; declarar a regra adotada |
| Casos especiais | carência, reativação, reembolso, falha de pagamento e chargeback |
| Features | informação conhecida no corte específico de cada exemplo |
| Rótulo | evento posterior ao corte dentro de uma janela completamente observada |

Os 14.753 pagantes são referência do case, não garantia do tamanho de toda coorte de previsão. Regras de elegibilidade adicionais podem alterar o denominador.

Sem observação até novembro, a base de setembro não oferece o desfecho completo do corte final. Treino e avaliação usam cortes históricos com horizonte observado. Esse contrato precisa estar documentado e implementado; definições diferentes geram problemas de previsão diferentes.

---

## 🗄️ 7. Três formas de dados

### 📋 7.1 Tabelas

Arquivos como `usuarios.csv`, `assinaturas.csv`, `amizades.csv` e `campanha_ago26.csv` já chegam em linhas e colunas. Mesmo assim, exigem auditoria de chaves, categorias, duplicidades e validade temporal.

### ⏱️ 7.2 Logs de eventos

`eventos_assinatura.csv`, `pagamentos.csv`, `uso_mensal.csv` e `atividades.parquet` registram acontecimentos. Antes de alimentar um modelo, precisam ser resumidos por pessoa e por janela de tempo.

Exemplos de variáveis:

- treinos nos últimos 7, 30 e 90 dias;
- dias desde o último treino;
- queda de frequência entre janelas;
- cobranças recusadas e número de tentativas;
- tempo entre desligar a renovação e expirar;
- seguidores, conexões e treinos acompanhados.

### 🖼️ 7.3 Texto e imagem

`onboarding.csv`, `pesquisa_saida.csv`, `feed_posts.csv`, `tickets_suporte.csv` e `heatmaps_90d/` precisam de uma etapa adicional de extração.

A IA generativa pode transformar conteúdo livre em colunas, desde que o grupo defina antes:

- schema de saída;
- valores permitidos;
- amostra de validação humana;
- métrica de acerto;
- custo por registro;
- política para respostas inválidas ou incertas.

---

## 🤖 8. IA preditiva e IA generativa têm papéis diferentes

- **IA preditiva:** recebe variáveis e estima uma classe ou probabilidade, como `score_churn_60d`.
- **IA generativa:** recebe um pedido e produz texto, imagem, código ou campos estruturados.

No módulo, a previsão de churn é o núcleo. A IA generativa atua como ferramenta de apoio para extrair variáveis de conteúdo não estruturado e, no final, redigir mensagens de CRM. Ela não substitui a avaliação estatística.

---

## 🧠 9. Paradigmas de aprendizado usados no módulo

### 🎯 Supervisionado

O algoritmo aprende com exemplos que incluem a resposta. Aplicações previstas:

- regressão logística;
- árvore de decisão;
- bagging e Random Forest;
- boosting.

### 🧩 Não supervisionado

O algoritmo procura grupos sem receber a resposta de churn. Aplicação prevista:

- clusterização de assinantes em segmentos interpretáveis.

A variável de churn não pode entrar na construção dos clusters. Ela pode ser usada depois para descrever como os segmentos se comportam.

---

## 🔎 10. Um exemplo integrado da aula

Os slides acompanham um mesmo assinante por tabelas, eventos, texto e imagem. Apenas as tabelas podem sugerir risco baixo. O feed, o onboarding, a queda recente de uso e o mapa de calor acrescentam contexto que pode alterar a leitura.

Essa narrativa ensina duas coisas:

1. a chave `user_id` conecta as fontes, mas não resolve diferenças de tempo e granularidade;
2. mais dados não significam automaticamente melhor decisão. Cada nova fonte precisa demonstrar ganho e justificar seu custo.

---

## 📦 11. Entregáveis derivados da Aula 1

A equipe deve sair da primeira aula com estes contratos documentados:

- pergunta de decisão e métrica de sucesso;
- população, corte e definição de saída;
- inventário das fontes e suas granularidades;
- caderno de hipóteses;
- riscos de viés, vazamento e qualidade;
- plano de validação para extrações com IA;
- critérios que separam resultado exploratório de evidência aceita.

O [Caderno de Hipóteses Analíticas](./06_CADERNO_DE_HIPOTESES_ANALITICAS.md) transforma esses pontos em tarefas executáveis. O [Dossiê dos Exhibits](./05_DOSSIE_EXHIBITS_M2.md) registra o que foi verificado diretamente nos arquivos.

👉 **Continue:** [🗺️ Mapa das Trilhas](./02_MAPA_DAS_TRILHAS.md) · [A1 e A2](./04_contexto_extra/01_VISAO_DETALHADA_SEMANA5_VS_SEMANA10.md).
