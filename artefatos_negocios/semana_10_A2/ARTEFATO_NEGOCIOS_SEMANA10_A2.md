# Artefato 2 de Negócios (Semana 10 — A2): Board Recommendation Deck — Plano de Inteligência de Retenção

> **Módulo 2:** Inteligência de Mercado e Modelagem Preditiva para Crescimento (Inteli MBA)  
> **Business Case:** Vitaliza — Predição de Churn, Extração Multimodal, Uplift & Decisão Prescritiva de CRM  
> **Marcos Oficiais:** Submissão Previsão 60d (`08/12/2026`) · Revelação (`10/12/2026`) · Entrega Final A2 (`18/12/2026`)  
> **Escopo:** Objetivos 5, 6, 7 e 8 + Os 6 Slides/Blocos Executivos para o Conselho de Administração da Vitaliza  
> **Equipe de Trabalho:** Equipe de Projetos MBA Inteli  
> **Arquivo:** `ARTEFATO_NEGOCIOS_SEMANA10_A2.md`  

> **📌 Nota de Governança da Equipe (Baseline Inicial):**  
> *Este documento estrutura a recomendação executiva ao Conselho da Vitaliza em formato de **6 Blocos/Slides Executivos**, fundamentada nos resultados empíricos do experimento controlado de agosto (`campanha_ago26.csv`) e nas regras financeiras da Seção 03 do case. Serve como **Baseline Inicial (Ponto de Partida)** para revisão, refinamento e coautoria de toda a equipe.*

---

## 📊 Slide 1 — Diagnóstico do Problema: Sangria de Receita e o Dilema da Série B

* **O Cenário Crítico:** A taxa média de churn mensal da Vitaliza subiu de **5,6% em 2025 para 6,6% em 2026 (jan–set)**, com pico de **8,1% em abril de 2026** (`1.154` assinaturas perdidas em um único mês após o reajuste do plano mensal de R$ 34,90 para R$ 39,90 em `01/03/2026`).
* **O Estoque de Perda Já Contratada no Corte (`30/09/2026`):** Entre os **`14.753` assinantes pagantes ativos** (receita líquida mensalizada de **R$ 409.941/mês** ou **R$ 4,92 milhões/ano**), **`2.250` assinantes (`15,25%`) já desligaram a renovação automática** (`2.082` no plano anual e `168` no plano mensal) e deixarão de pagar assim que o ciclo vigente expirar.
* **Por Que as Visões Isoladas da Diretoria Falharam:**
  * A equipe operava sem sistema estruturado de retenção, guiada por vieses de confirmação onde cada área culpava um fator isolado (preço, falta de personalização, marketing ou ausência de abordagem no cancelamento).

---

## 🔍 Slide 2 — O Que os Dados Dizem Sobre Quem Cancela (Os 4 Perfis e os 2 Fatos Vitais)

A segmentação comportamental dos `14.753` pagantes ativos e a auditoria do Data Room revelam que o cancelamento não é uniforme — ele se concentra onde o hábito de treino cai abaixo de 5 sessões mensais e expõe **dois fatos vitais de negócio**:

| Segmento Comportamental (`30/09/2026`) | Volume (`N` e `%`) | Treinos / Mês | % Renovação Desligada | Diagnóstico Comportamental e de Canal |
| :--- | ---: | ---: | ---: | :--- |
| **1. Atletas Sociais de Rua & GPS** | `4.089` (`27,72%`) | `12,4` | **`1,61%`** | Fidelizados pelo GPS, relógio (`Garmin`/`Apple Watch`) e rede de amigos (`amizades.csv`). |
| **2. Praticantes Regulares Vídeo** | `2.960` (`20,06%`) | `11,9` | **`1,59%`** | Hábito consolidado em aulas guiadas em casa (funcional, força, yoga). |
| **3. Entusiastas Oscilantes (Em Risco)**| `5.391` (`36,54%`) | `2,2` | **`15,19%`** | **O coração do churn evitável:** Frustrados com metas não cumpridas, falhas de app ou sensíveis aos R$ 39,90/mês. |
| **4. Pagantes Inertes (*Sleeping Dogs*)**| `2.313` (`15,68%`) | `0,0` | **`56,98%`** | Abandonaram o uso: `1.318` já cancelaram a renovação e `995` continuam pagando apenas por esquecimento/inércia. |

1. **Fato Vital 1 — Cegueira de 70,22% nas Lojas:** `10.359` pagantes (`70,22%`) assinam via **App Store (`36,57%`) ou Google Play (`33,65%`)** e cancelam nas configurações do celular, fora do app da Vitaliza. Qualquer ação restrita à tela de cancelamento do site ignora 7 em cada 10 clientes.
2. **Fato Vital 2 — O Perigo Real dos *Sleeping Dogs*:** Existem `995` clientes inativos que ainda estão com a renovação automática ligada pagando por inércia (**R$ 27,6 mil/mês**). Acioná-los sem filtro lembra-os da cobrança e dispara o cancelamento imediato.

---

## ⚔️ Slide 3 — As Duas Apostas na Mesa (Caminho A vs. Caminho B) e o Fator Strava

Avaliamos de forma estruturada as duas propostas debatidas pela liderança frente ao anúncio competitivo do **Strava Premium** no Brasil:

| Dimensão de Avaliação | 🔥 Caminho A: Win-Back Reativo ("O Bombeiro" — CS) | 📡 Caminho B Puro: Engagement Forecasting ("Detector de Fumaça" — Produto) | 🏆 Nossa Recomendação: Arquitetura Prescritiva de Uplift (Caminho B + Regra Causal) |
| :--- | :--- | :--- | :--- |
| **Mecanismo de Acionamento** | Oferta exibida apenas quando o usuário clica em *"Cancelar"* na web. | Score preditivo diário dispara intervenção para todos os usuários de "risco alto". | Combina **Score Preditivo 60d (ML + GenAI)** com **Filtro de Uplift (Siegel)** e janela de aviso das lojas. |
| **Cobertura da Base Pagante** | **Apenas 29,78% (Site).** É 100% cego para os **70,22% das lojas** e para quem sai sem clicar. | **100% da base** (alcança clientes de App Store e Google Play semanas antes do cancelamento). | **100% da base**, mas filtra cirurgicamente quem deve receber contato e quem deve ficar em silêncio. |
| **Risco Colateral Financeiro** | **Baixo risco de acordar inativos**, mas recupera fração mínima da sangria total. | **ALTO RISCO:** Acorda *Sleeping Dogs* (`+9,16 p.p.` de churn extra!) e queima cupom em *Garantidos*. | **Risco Mitigado:** Bloqueia contato em *Sleeping Dogs* (`0` treinos + renovação ligada) e veda cupom em *Garantidos*. |
| **Posicionamento vs. Strava** | **Defasado:** Chega ao mercado superado pela camada preditiva personalizada do Strava. | **Paridade Técnica:** Responde ao Strava com personalização preditiva baseada em dados reais de treino. | **Vantagem Competitiva Comprovada em P&L:** Une paridade tecnológica com otimização estrita de margem (ROI). |

---

## 🧪 Slide 4 — A Prova Causal: O Que o Experimento de 10/08/2026 (`campanha_ago26.csv`) Revelou

A Vitaliza sorteou aleatoriamente **`14.120` assinantes pagantes** em `10/08/2026` entre quatro grupos (`controle`, `desafio`, `cupom`, `conteudo`). Nossa auditoria inédita cruzando o sorteio com o status de retenção e o uso prévio em julho/2026 comprova matematicamente a teoria dos **4 Quadrantes de Siegel**:

### 📈 4.1. Efeito Causal por Plano de Assinatura (Mensal vs. Anual)

| Plano | Grupo do Sorteio (`10/08/2026`) | Assinantes Sorteados | Taxa de Clique (`clicou`) | Churn Efetivo até o Corte | Saída + Renovação Desligada | Uplift de Retenção Ativa vs. Controle | Diagnóstico Econômico do Tratamento |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| **Plano Mensal** | **1. Controle (Sem mensagem)** | `1.440` | `0,00%` | `14,58%` | `17,99%` | *Referência (0,00 p.p.)* | Churn mensal elevado pós-reajuste de R$ 39,90. |
| **Plano Mensal** | **2. Cupom (`30pct_3_meses`)** | `1.420` | `16,45%` | **`8,94%`** | **`10,63%`** | **`+ 7,36 p.p.` (Redução de 41% na saída!)** | **Altíssimo Uplift** para quem tem dor de preço/oscilação, mas custa R$ 35,91 por retido. |
| **Plano Mensal** | **3. Desafio (6 semanas)** | `1.456` | `14,31%` | **`11,13%`** | **`12,98%`** | **`+ 5,01 p.p.` (Custo de oferta R$ 0!)** | **Melhor relação custo-benefício** para reengajar sem abrir mão de receita! |
| **Plano Mensal** | **4. Conteúdo (Plano treino)** | `1.463` | `14,91%` | `13,53%` | `15,79%` | **`+ 2,20 p.p.` (Custo de oferta R$ 0)** | Efeito positivo moderado para usuários com dúvida de treino. |
| **Plano Anual** | **Controle vs. Tratamentos** | `8.341` | `~15,2%` | `6,07% a 7,21%` | `30,39% (Ctrl) vs 33,48% (Cupom)` | **Negativo no disparo cego (`-3,09 p.p.` no Cupom)** | Disparar cupom em massa no anual acordou inativos! No anual, a ação deve focar apenas nos oscilantes ativos. |

### 🚨 4.2. A Prova Empírica dos *Sleeping Dogs* vs. *Persuadíveis* (Corte por Uso em Julho/2026)

| Faixa de Engajamento Prévio (Julho/2026) | Quadrante de Siegel Identificado | Saída/Desligamento no **Controle** | Saída/Desligamento no **Desafio** | Saída/Desligamento no **Cupom** | Saída/Desligamento no **Conteúdo** | Regra Prescritiva Mandatória (Objetivo 6) |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **`0` treinos no mês (`N = 2.685` no teste)** | **Não Perturbe (*Sleeping Dogs*)** | **`51,86%`** | `61,02%` *(+9,16 p.p. pior!)* | `57,95%` *(+6,09 p.p. pior!)* | `60,39%` *(+8,53 p.p. pior!)* | **PROIBIDO CONTATAR** quem tem `0` treinos e renovação ligada! O contato lembra da assinatura e destrói retenção. |
| **`1 a 4` treinos no mês (`N = 5.241` no teste)**| **Persuadíveis (*Persuadables*)** | `25,19%` | **`20,37%` (`+4,82 p.p.` ganho!)** | **`21,45%` (`+3,74 p.p.` ganho!)** | **`21,61%` (`+3,58 p.p.` ganho!)** | **ALVO PRIORITÁRIO:** Atacar com *Desafio* (R$ 0) ou *Cupom* (para sensíveis a preço no mensal). |
| **`≥ 5` treinos no mês (`N = 6.194` no teste)** | **Garantidos (*Sure Things*)** | `14,38%` | **`9,70%` (`+4,68 p.p.` ganho!)** | `10,93%` *(Queima margem)* | `13,07%` *(+1,31 p.p. ganho)* | **VEDADO DAR CUPOM:** Engajar apenas com *Desafio de 6 semanas* ou *Conteúdo* (custo de oferta R$ 0,00) via Push/E-mail. |

---

## 💰 Slide 5 — Plano de Alocação Ótima (Orçamento R$ 40.000/mês) & Lucro Líquido Incremental

Para novembro e dezembro de 2026, alocamos os recursos respeitando rigorosamente os tetos físicos (**1.500 WhatsApps**, **300 atendimentos CS**) e financeiros (**R$ 40.000/mês** já incluindo canais, descontos e tokens de IA Generativa):

### 📋 5.1. Matriz Prescritiva de Alocação Mensal por Público-Alvo, Canal e Oferta

| Prioridade e Público Elegível (População Ativa `30/09/2026`) | Volume Alvo (`N`) | Canal Alocado | Oferta Prescrita | Custo de Canal | Custo de Descontos Estimado | Assinantes Salvos Incrementais (Uplift) | Receita Líquida Retida (Ciclo 6m / Anual) |
| :--- | ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| **1. Persuadíveis de Alto Valor com Fricção Técnica / Alto Risco**<br>*(1–4 treinos + ticket aberto/problema GPS ou Anual próximo à renovação)* | **`300`** *(100% do teto CS)* | **Time de CS** *(R$ 18,00/un)* | Resolução ativa + **Plano Personalizado** ou **1 mês grátis Anual** (R$ 25) | **R$ 5.400,00** | **R$ 3.750,00** *(~150 aceites anuais x R$ 25)* | **`~42` clientes salvos** *(Uplift estimado +14%)* | **R$ 49.450,00** |
| **2. Persuadíveis do Plano Mensal Sensíveis a Preço / Queda Aguda**<br>*(1–4 treinos no Mensal, score de risco alto, sem falha técnica)* | **`750`** *(50% do teto WA)* | **WhatsApp** *(R$ 0,40/un)* | **Cupom 30% off por 3 meses** *(R$ 35,91 no ciclo)* | **R$ 300,00** | **R$ 16.159,50** *(~450 aceites x R$ 35,91)* | **`~55` clientes salvos** *(Uplift real +7,36 p.p.)* | **R$ 30.899,00** *(líquido de custo de servir)* |
| **3. Persuadíveis Oscilantes com Meta de Performance/Saúde**<br>*(1–4 treinos identificadas no `onboarding.csv` e `heatmaps_90d`)* | **`750`** *(50% do teto WA)* | **WhatsApp** *(R$ 0,40/un)* | **Desafio 6 Semanas + Plano Personalizado** *(Custo oferta R$ 0)* | **R$ 300,00** | **R$ 0,00** | **`~38` clientes salvos** *(Uplift real +5,01 p.p.)* | **R$ 21.348,00** |
| **4. Restante dos Persuadíveis (1–4 treinos) + Janela Lojas (`renov=nao`)** | **`4.191`** | **E-mail + Push** *(R$ 0,01/un)* | **Desafio 6 Semanas** ou **Pausa de até 60 dias** *(Custo direto R$ 0)* | **R$ 41,91** | **R$ 0,00** | **`~146` clientes salvos** *(Uplift médio +3,5 p.p.)* | **R$ 82.023,00** |
| **5. Garantidos Engajados (`≥ 5` treinos — Clusters 1 e 2)** | **`7.049`** | **Push Semanal + E-mail** | **Desafio 6 Semanas / Comunidade** *(PROIBIDO CUPOM)* | **R$ 70,49** | **R$ 0,00** | **`~90` clientes preservados** *(Prevenção de queda)* | **R$ 50.562,00** |
| **6. Sleeping Dogs (`0` treinos com renovação ligada)** | **`995`** | **NENHUM (Silêncio)** | **Nenhuma ação** *(Evita +9,16 p.p. de churn induzido!)* | **R$ 0,00** | **R$ 0,00** | **`~85` cancelamentos evitados** *(por não acordar!)* | *(Preserva R$ 15.800/mês que seriam perdidos)* |
| **7. Processamento de IA Generativa & Visão (Peças 2 e 5)** | *Base elegível* | API LLM & Visão | Extração de texto/heatmaps + Redação das mensagens | **R$ 420,00** *(Tokens LLM)* | — | *Habilitador de precisão e personalização* | — |
| **CONSOLIDADO MENSAL DA POLÍTICA PRESCRITIVA** | **`14.753`** | **1.500 WA \| 300 CS \| E-mail/Push** | **Dentro do Teto de R$ 40k** | **R$ 6.532,40** *(Canais + IA)* | **R$ 19.909,50** *(Descontos)* | **`~371` saídas evitadas/mês** *(+85 Sleeping Dogs protegidos)* | **R$ 234.282,00** *(Valor Retido no Horizonte)* |

> **🏆 Fechamento Financeiro (Objetivo 7):**  
> * **Desembolso Total da Política Prescritiva:** **R$ 26.441,90 / mês** (bem abaixo do teto de **R$ 40.000,00 / mês**, mantendo **R$ 13.558,10** de margem de segurança para variações na taxa de adesão aos cupons).  
> * **Lucro Líquido Incremental Gerado (vs. Não Fazer Nada):** **`+ R$ 207.840,10`** no horizonte de retenção dos coortes salvos (ROI de **+686%** sobre o orçamento investido, equivalente a evitar **R$ 43.778,00** em CAC de reposição imediata a R$ 118/cliente).

---

## 🛡️ Slide 6 — Riscos, Limitações Reconhecidas & Plano de Contingência

| Risco / Incerteza Operacional | Impacto Potencial | Gatilho de Monitoramento (KPI) | Ação de Contingência Imediata |
| :--- | :--- | :--- | :--- |
| **1. Acordamento Acidental de *Sleeping Dogs*** | Aumento de +6 a +9 p.p. na taxa de cancelamento de inativos. | Taxa de desligamento de renovação nas 48h após envio de Push/WhatsApp > 1,5%. | **Kill-Switch de Inatividade:** Bloqueio automático na régua de CRM para qualquer `user_id` com `dias_ativos = 0` nos últimos 21 dias e `renovacao_automatica = 'sim'`. |
| **2. Canibalização de Margem por Excesso de Cupons** | Estouro do orçamento de R$ 40.000/mês caso a adesão ao cupom de R$ 35,91 supere a projeção. | Consumo acumulado de descontos atingir R$ 28.000 no dia 20 do mês. | **Trava de Orçamento:** Substituição automática da oferta de *Cupom 30% off* pelo *Desafio de 6 Semanas + Pausa de 60 dias* (custo direto R$ 0). |
| **3. Limite de Extrapolação de Canal (Push/E-mail $\rightarrow$ WhatsApp/CS)** | O experimento de 10/08 testou apenas `push+email`. O efeito no WhatsApp e no CS pode variar. | Acompanhamento semanal de grupo de controle pareado (*Holdout de 10%*) nos disparos de WhatsApp de novembro. | Recalibrar os pesos de alocação de canal na semana 3 de novembro com base na conversão incremental real do WhatsApp. |
| **4. Alucinação na Redação Generativa de Mensagens (Objetivo 8)** | Promessa de desconto indevido ou menção incorreta ao histórico do assinante. | Validação por schema estrito antes do disparo (100% das mensagens checadas contra a oferta autorizada). | Fallback determinístico para template homologado de CRM caso o validador detecte divergência. |
