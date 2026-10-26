# Artefato de Tecnologia — Semana 10 (A2): Modelos Supervisionados (60d), Extração Multimodal & Redator de CRM

> **Módulo 2:** Inteligência de Mercado e Modelagem Preditiva para Crescimento — MBA Inteli  
> **Entrega:** Semana 10 — `18/12/2026` (2º Movimento: AGIR — Avaliação Somativa Final)  
> **Tema:** Classificação Supervisionada de Churn em 60 Dias (`Logística`, `Árvores`, `Bagging`, `Boosting`), Extração Multimodal (`Google Gemini` + `Pixels Determinísticos`), Regra Prescritiva de Uplift (`Siegel`) e Redator de CRM com Briefing Fechado  

---

## 📂 1. Estrutura desta Pasta e Código de Execução

```text
semana_10_A2/
├── ARTEFATO_TECH_SEMANA10_A2.md           <-- Documento executivo e técnico completo oficial da Semana 10 (A2)
└── README.md                              <-- Este guia rápido de arquitetura e execução local

Arquivos de Código e Relatórios Associados (na raiz do repositório):
├── src/
│   ├── 01_auditoria_data_room.py          <-- Auditoria point-in-time das 13 fontes do Data Room
│   └── 02_pipeline_gemini_multimodal_crm.py <-- Pipeline end-to-end: Extração Gemini + Pixels + Uplift + Redator CRM
└── relatorios/
    ├── auditoria_exhibits.json            <-- Relatório auditado do Data Room
    └── simulacao_gemini_crm.json          <-- Saída estruturada e validada do pipeline multimodal + CRM
```

---

## 🚀 2. Como Executar o Protótipo Multimodal & CRM Localmente

Na raiz do repositório:

1. **Rodar a simulação completa (Peça 2 Extração + Peça 4 Decisão + Peça 5 Copywriter):**
   ```bash
   uv run --with duckdb --with pillow \
     python src/02_pipeline_gemini_multimodal_crm.py \
     --json relatorios/simulacao_gemini_crm.json
   ```

2. **Testar com a API oficial do Google Gemini (`gemini-2.5-flash`):**
   Se a variável de ambiente `GEMINI_API_KEY` estiver configurada, o script aciona a API oficial do Gemini com *Structured Outputs* (JSON Schema estrito). Caso não esteja definida no ambiente local, o script executa automaticamente o motor determinístico calibrado sobre os registros reais do Data Room, garantindo 100% de reprodutibilidade offline.
   ```bash
   GEMINI_API_KEY="sua_chave_aqui" uv run --with duckdb --with pillow \
     python src/02_pipeline_gemini_multimodal_crm.py \
     --json relatorios/simulacao_gemini_crm.json
   ```

---

## 🎯 3. Destaques Técnicos do Entregável A2

1. **Ablação Multimodal e Tokenomics (Peça 2 / Objetivo 5):**
   - Comparação direta entre **Contagem Determinística de Pixels por Cor** (`verde` = parque, `azul` = água, `areia` = praia, `amarelo` = avenida em `heatmaps_90d/`, a custo de API **R$ 0,00**) e extração estruturada via LLM com schema JSON sobre `onboarding.csv`, `tickets_suporte.csv` e `feed_posts.csv`.
   - Ganho de **`+2,72 p.p.` em PR-AUC** (`0,5714` $\rightarrow$ `0,5986`) e redução do Brier Score (`0,1352` $\rightarrow$ `0,1330`) a um custo estimado de **~R$ 280,00/mês** no lote ativo.
2. **Comparação Out-of-Time das 4 Famílias Supervisionadas (Peça 3 / Objetivo 4):**
   - Evolução consistente sem *Data Leakage*: **Regressão Logística** (`0,7522` ROC-AUC), **Árvore de Decisão** (`0,7691` ROC-AUC, `Lift@10% = 2,97x`), **Bagging / Random Forest** (`0,7850` ROC-AUC) e **Gradient Boosting Multimodal** (**`0,7858` ROC-AUC / `0,5986` PR-AUC**).
3. **Motor Prescritivo de Uplift + Copywriter com Briefing Fechado (Peças 4 e 5 / Objetivos 6, 7 e 8):**
   - Bloqueia automaticamente comunicações para ***Sleeping Dogs*** (`0` treinos/mês + renovação ligada, evitando `+6,09 a +9,16 p.p.` de churn induzido), veda cupons em ***Garantidos*** (`≥5` treinos/mês) e submete o rascunho de mensagem a um validador determinístico anti-alucinação antes da liberação para o CRM.
