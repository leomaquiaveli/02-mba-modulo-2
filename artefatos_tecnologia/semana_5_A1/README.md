# Artefato de Tecnologia — Semana 5 (A1): Pipeline do Data Room, Clusterização & Baseline

> **Módulo 2:** Inteligência de Mercado e Modelagem Preditiva para Crescimento — MBA Inteli  
> **Entrega:** Semana 5 — `13/11/2026` (1º Movimento: ENTENDER — Avaliação Formativa)  
> **Tema:** Engenharia Analítica Point-in-Time (`DuckDB`), Saneamento das 13 Fontes, Clusterização Comportamental sem Vazamento de Churn e Baseline de Regressão Logística  

---

## 📂 1. Estrutura desta Pasta e Arquivos Relacionados

```text
semana_5_A1/
├── ARTEFATO_TECH_SEMANA5_A1.md            <-- Documento técnico completo oficial da Semana 5 (A1)
└── README.md                              <-- Este guia rápido de contexto e execução local

Arquivos de Código e Relatórios Associados (na raiz do repositório):
├── src/
│   └── 01_auditoria_data_room.py          <-- Script reproduzível de auditoria física e lógica das 13 fontes
└── relatorios/
    └── auditoria_exhibits.json            <-- Relatório JSON verificado (14.753 pagantes + 60 cortesias)
```

---

## 🚀 2. Como Executar e Reproduzir a Auditoria Localmente

Na raiz do repositório:

1. **Executar a auditoria completa no diretório canônico (`documentos/exhibits-m2/`):**
   ```bash
   uv run --with duckdb --with pytz \
     python src/01_auditoria_data_room.py \
     --json relatorios/auditoria_exhibits.json
   ```

2. **Conferir o relatório consolidado gerado:**
   O script valida a contagem exata dos 11 CSVs e do arquivo `atividades.parquet` (`1.254.475` linhas), testa unicidade de chaves primárias, reconcilia as `14.813` assinaturas ativas em **`14.753` pagantes ativos** e **`60` cortesias**, e mapeia os registros posteriores ao corte (`30/09/2026`).

---

## 🎯 3. Destaques Técnicos do Entregável A1

1. **Saneamento e Tratamento das 7 Anomalias Estruturais (Objetivo 1):**
   - Exclusão das `60` contas de cortesia interna (`plano_atual = 'cortesia'`);
   - Filtro temporal estrito (`<= 2026-09-30 23:59:59`) removendo `119` cadastros, `122` posts e `273` amizades pós-corte;
   - Normalização de fuso horário (`UTC "Z"` das lojas App Store / Google Play para `America/Sao_Paulo` em `eventos_assinatura.csv`);
   - Padronização de grafias de sistema operacional (`android`/`Android`, `ios`/`iOS`/`IOS`), vocabulário bilíngue de treinos (`corrida`/`run`, `caminhada`/`walk`, `forca`/`strength`, `pedal`/`ride`) e tratamento explícito da string `'nenhum'` em `relogio_conectado`.
2. **Clusterização Comportamental Sem Vazamento de Churn (Objetivo 3):**
   - Formação de **4 segmentos interpretáveis** (*Atletas Rua GPS [27,72%]*, *Praticantes Vídeo [20,06%]*, *Entusiastas Oscilantes 1–4 treinos [36,54%]* e *Pagantes Inertes 0 treinos [15,68%]*) utilizando apenas variáveis de uso e ecossistema, projetando a taxa de desligamento de renovação exclusivamente *a posteriori*.
3. **Baseline Supervisionado Out-of-Time (Objetivo 4 Inicial):**
   - Modelo de **Regressão Logística (`StandardScaler`, `L2`)** validado fora da amostra temporal, atingindo **`ROC-AUC = 0,7522`**, **`PR-AUC = 0,5079`**, **`Brier Score = 0,1504`** e **`Lift@10% = 2,55x`** na cota operacional de `1.500` mensagens de WhatsApp.
