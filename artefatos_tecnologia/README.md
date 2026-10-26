# 💻 Artefatos Oficiais de Tecnologia & Ciência de Dados — Módulo 2 (Case Vitaliza)

> **Módulo 2:** Inteligência de Mercado e Modelagem Preditiva para Crescimento — MBA Inteli  
> **Entregas Oficiais:** Semana 5 (`A1 — 13/11/2026`) · Previsão 60d (`08/12/2026`) · Semana 10 (`A2 — 18/12/2026`)  
> **Tema:** Engenharia Analítica Point-in-Time, Clusterização Comportamental, Classificação Supervisionada (60 dias), Extração Multimodal (Gemini + Pixels) e Redator de CRM com Briefing Fechado  

---

## 📂 1. Estrutura desta Pasta e Scripts Associados

Esta pasta centraliza os entregáveis oficiais da **Trilha de Tecnologia e Ciência de Dados** do grupo para submissão na plataforma Adalove:

```text
artefatos_tecnologia/
├── README.md                                            <-- Este guia técnico e índice de execução
├── semana_5_A1/
│   ├── README.md                                        <-- Guia rápido da entrega técnica da Semana 5
│   └── ARTEFATO_TECH_SEMANA5_A1.md                      <-- Pipeline Data Room, Clusterização & Baseline Logístico
└── semana_10_A2/
    ├── README.md                                        <-- Guia rápido da entrega técnica da Semana 10 + Gemini
    └── ARTEFATO_TECH_SEMANA10_A2.md                     <-- Modelos 60d, Ablação Multimodal & Redator Generativo
```

---

## 🎯 2. Síntese dos Entregáveis Técnicos

* **[`semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md`](./semana_5_A1/ARTEFATO_TECH_SEMANA5_A1.md)** ([Guia Semana 5](./semana_5_A1/README.md)): Pipeline de saneamento e integração do Data Room (`user_id`), tratamento das 7 anomalias estruturais, reconstrução histórica de assinaturas (`UTC` $\rightarrow$ `America/Sao_Paulo`), engenharia de variáveis sobre `atividades.parquet` (`1.254.475` treinos), clusterização não-supervisionada de assinantes sem vazamento de churn e baseline de **Regressão Logística** (`ROC-AUC = 0,7522`, `Lift@10% = 2,55x`).
* **[`semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md`](./semana_10_A2/ARTEFATO_TECH_SEMANA10_A2.md)** ([Guia Semana 10](./semana_10_A2/README.md)): Modelos supervisionados de predição de churn em 60 dias (**Regressão Logística, Árvore de Decisão, Bagging/Random Forest e Gradient Boosting Multimodal** com `ROC-AUC = 0,7858` e `PR-AUC = 0,5986`), extração multimodal com IA Generativa e Visão (`onboarding`, `suporte`, `feed`, `heatmaps_90d/` com ganho de `+2,72 p.p.` em PR-AUC), árvore prescritiva de decisão de CRM e motor generativo de redação personalizada de mensagens.

---

## 🚀 3. Como Executar os Scripts Reproduzíveis Localmente

Na raiz do repositório:

1. **Auditoria completa do Data Room (Peça 1 — Semana 5):**
   ```bash
   uv run --with duckdb --with pytz \
     python src/01_auditoria_data_room.py \
     --json relatorios/auditoria_exhibits.json
   ```

2. **Simulação do Pipeline Multimodal Gemini + Regra Prescritiva + Redator CRM (Peças 2, 4 e 5 — Semana 10):**
   ```bash
   uv run --with duckdb --with pillow \
     python src/02_pipeline_gemini_multimodal_crm.py \
     --json relatorios/simulacao_gemini_crm.json
   ```
