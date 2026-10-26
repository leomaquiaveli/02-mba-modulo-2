# 🎙️ Transcrição Oficial — Síntese Executiva do Case Vitaliza (Módulo 2)

> **Equipe de Projetos MBA Inteli — Módulo 2**  
> **Duração Estimada de Leitura/Áudio:** 5 minutos  
> **Arquivo:** `documentos/midia_e_audios/TRANSCRICAO_AUDIO_SINTESE_EXECUTIVA.md`

---

## 🎙️ Transcrição Completa em Texto

Visão geral do diagnóstico estratégico, da modelagem analítica e da arquitetura de decisão estruturada para a Vitaliza.

### 1. O Problema Central e a Decisão de Negócio
A empresa estudada no Módulo 2 é a **Vitaliza**, um aplicativo brasileiro de corrida e treinos por assinatura — combinando registro de atividades com GPS, treinos guiados em vídeo e rede social — que encerrou o corte oficial de 30 de setembro de 2026 com **14.753 assinantes pagantes ativos**, distribuídos entre o plano mensal (R$ 39,90) e o plano anual (R$ 299,90).

O desafio central reside na deterioração da retenção ao longo de 2026: o cancelamento mensal médio avançou de **5,6% ao mês em 2025 para 6,6% ao mês em 2026**, atingindo um pico crítico de **8,1% em abril de 2026**, imediatamente após o reajuste do plano mensal de R$ 34,90 para R$ 39,90 em março. Simultaneamente, o concorrente Strava anunciou o lançamento de modelos preditivos individuais de desengajamento no Brasil, exigindo que a Vitaliza defenda seus indicadores de retenção antes da captação de sua rodada Série B.

A **decisão central** que o projeto responde é: **em quais assinantes investir para preservar a retenção, por qual canal, com qual oferta e para quais perfis manter a abstenção de contato**, respeitando o teto orçamentário de **R$ 40.000 por mês** e as capacidades operacionais de **1.500 mensagens de WhatsApp** e **300 atendimentos humanos de Customer Success** por mês.

---

### 2. O Dilema dos Executivos e os Dois Fatores Críticos de Negócio
Na diretoria da Vitaliza, a nova VP de Crescimento, **Camila Ferraz**, encontra os líderes divididos entre duas apostas:
* De um lado, a Head de CS (**Patrícia**) defende o **Caminho A (Win-Back Reativo)**: apresentar uma oferta de desconto quando o cliente clica no botão "Cancelar".
* Do outro lado, o Head de Produto (**Marcelo**) defende o **Caminho B (Engagement Forecasting)**: criar um modelo preditivo para acionar quem está reduzindo a frequência de treino semanas antes do cancelamento, enquanto o CTO (**Diego**) alerta para a fragmentação das bases de dados e a CFO (**Rita**) exige comprovação quantitativa de retorno financeiro.

Quando analisamos os dados reais da Vitaliza, identificamos **dois fatores críticos de negócio** que demonstram que nenhum dos dois caminhos se sustenta isoladamente:

1. **Primeiro Fator Crítico (A Assimetria de Canal de 70% no Caminho A):**  
   Sete em cada dez assinantes pagantes (**70,22% da base**) contratam via **App Store ou Google Play**. Quando decidem encerrar a assinatura, desativam a renovação automática diretamente nas configurações do iPhone ou do Android, fora do aplicativo da Vitaliza. Eles não passam pela tela de cancelamento do site. Portanto, uma ação puramente reativa no clique de cancelamento é **invisível para 70% dos clientes**.
2. **Segundo Fator Crítico (O Risco dos *Sleeping Dogs* e a Erosão de Margem no Caminho B):**  
   Se treinarmos um modelo preditivo e dispararmos ofertas indistintamente para todos os assinantes com "risco alto", incorremos em duas perdas financeiras diretas: primeiro, acionamos os chamados ***Sleeping Dogs* (clientes "Não Perturbe")** — pessoas inativas que mantêm a assinatura por inércia e que, ao receberem uma comunicação da Vitaliza, recordam a cobrança recorrente e cancelam imediatamente. Segundo, corroemos a margem concedendo desconto de R$ 35,91 para os clientes **Garantidos** (que renovariam organicamente) ou alocando atendimento humano de R$ 18,00 nos **Perdidos** (que cancelarão independentemente do estímulo). Por essa razão, o investimento deve ser direcionado estritamente aos clientes **Persuadíveis** — aqueles que sairiam na ausência de ação, mas permanecem quando abordados com a oferta adequada.

---

### 3. O Que Temos Que Construir? (As 5 Peças do Sistema)
Para resolver essa equação, vamos construir um sistema integrado de **5 peças** sobre os 13 arquivos do Data Room:
1. **Peça 1 (Dados):** Limpar e integrar as tabelas e logs pelo `user_id`, corrigindo fusos horários entre as lojas e o site, separando as 60 contas de cortesia dos 14.753 pagantes reais e reconstruindo quem estava ativo em cada mês.
2. **Peça 2 (Extração com IA Generativa e Visão):** Usar LLMs e Visão Computacional para ler os textos abertos de onboarding, suporte e rede social, além das 25 mil imagens de mapas de calor das rotas de treino, transformando tudo em colunas estruturadas na tabela e medindo se o ganho preditivo paga o custo dos tokens.
3. **Peça 3 (Segmentação e Previsão de Churn em 60 Dias):** Rodar Clusterização para criar Personas reais baseadas em comportamento de uso (sem usar a variável de churn) e treinar modelos supervisionados (Regressão Logística, Árvores de Decisão, Bagging e Boosting) para prever a chance de cada assinante sair nos 60 dias seguintes ao corte, até 29 de novembro de 2026.
4. **Peça 4 (Decisão Prescritiva e Uplift):** Analisar o experimento A/B real que a Vitaliza fez em 10 de agosto de 2026 com 14.120 clientes (divididos entre Desafio, Cupom, Conteúdo e Controle) para medir o efeito causal de cada ação e alocar os 1.500 WhatsApps, 300 atendimentos de CS e ofertas dentro dos R$ 40.000 mensais, maximizando o lucro líquido em reais.
5. **Peça 5 (Mensagem Personalizada):** Usar a IA Generativa como redatora final para escrever a mensagem individualizada de cada assinante selecionado, respeitando a persona, o canal e a oferta definida pela regra.

---

### 4. O Que Entregamos na Semana 5 (A1) e na Semana 10 (A2)?

O módulo tem duas entregas oficiais que dividem o trabalho em **Entender (Semana 5)** e **Agir (Semana 10)**:

* **Na Semana 5 (Artefato 1 — Entrega em 13 de novembro — Movimento ENTENDER):**
  * **Em Negócios:** Entregamos o **Customer Segmentation Analysis Report**, contendo o diagnóstico das causas da subida do churn em 2026, a descrição de 3 a 4 clusters comportamentais transformados em Personas de dados, o cálculo da Receita em Risco por segmento, a matriz de priorização de quem merece intervenção imediata versus monitoramento e as limitações dos dados.
  * **Em Tecnologia:** Entregamos o pipeline auditado do Data Room, a reconstrução histórica da base ativa, a engenharia de variáveis sobre o arquivo Parquet de 1,25 milhão de treinos, o modelo de Clusterização Não-Supervisionada e o modelo baseline de Regressão Logística.

* **Na Semana 10 (Artefato 2 — Previsão em 8 de dezembro e Entrega Final em 18 de dezembro — Movimento AGIR):**
  * **Em Negócios:** Entregamos o **Board Recommendation Deck (Plano de Inteligência de Retenção em 6 Slides Executivos)**, simulando a apresentação de Camila ao Conselho: diagnóstico final, quem cancela, comparação financeira entre Caminho A e Caminho B frente ao Strava, a política prescritiva de Uplift baseada no experimento de agosto, o plano de ação de 10 semanas com o ROI líquido dentro dos R$ 40.000 mensais e o plano de contingência contra *Sleeping Dogs*.
  * **Em Tecnologia:** Entregamos a comparação completa dos modelos supervisionados de churn de 60 dias (Regressão Logística, Árvores, Bagging e Boosting), o pipeline de extração multimodal de texto e imagem validado contra amostra humana e o motor generativo que redige as mensagens personalizadas de retenção.
