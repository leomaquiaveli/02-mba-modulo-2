# Exhibits do Módulo 2 — uso local

Esta pasta contém o pacote bruto do Data Room Vitaliza, extraído localmente para auditoria e modelagem.

## Não publicar os arquivos brutos

Os CSVs, o Parquet, os ZIPs de heatmaps e o ZIP original devem permanecer fora do Git porque:

- o pacote original ultrapassa o limite normal de arquivo do GitHub;
- os dados têm e-mails, identificadores e textos livres;
- a análise deve publicar resultados agregados e código reproduzível, não registros individuais.

O `.gitignore` do repositório protege o conteúdo desta pasta e mantém apenas este README versionável.

## Conteúdo esperado

- 11 CSVs de tabelas, eventos e texto;
- `atividades.parquet`;
- `heatmaps/heatmaps_2026-07-31.zip`;
- `heatmaps/heatmaps_2026-09-30.zip`;
- ZIP original de entrega.

## Auditoria

Execute:

```bash
cd /home/admin/Projects/02-inteli-mba-modulo-02
uv run --with duckdb --with pytz python src/01_auditoria_data_room.py
```

O script valida presença, contagens, chaves, coorte ativa e registros posteriores ao corte.

Leia também:

- [`../../00_comece_por_aqui/05_DOSSIE_EXHIBITS_M2.md`](../../00_comece_por_aqui/05_DOSSIE_EXHIBITS_M2.md)
- [`../../00_comece_por_aqui/05_DOSSIE_DICIONARIO_DE_DADOS_M2.md`](../../00_comece_por_aqui/05_DOSSIE_DICIONARIO_DE_DADOS_M2.md)
