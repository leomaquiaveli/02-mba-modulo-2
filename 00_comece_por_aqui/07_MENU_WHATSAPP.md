# 📱 Menu de Navegação para WhatsApp — Compartilhe com a Equipe

> **Módulo 2:** IA e Dados para Negócios — Case Vitaliza  
> **Equipe:** Projetos MBA Inteli  
> **Foco deste documento:** Mensagens prontas para compartilhar os materiais

[🔰 Comece por Aqui](./README.md) / Menu de compartilhamento

> Repositório oficial da equipe no GitHub: **`https://github.com/leomaquiaveli/02-mba-modulo-2`**

---

## ⚡ Versão curta

```text
📚 MBA Inteli — Módulo 2 | Case Vitaliza

Pessoal, organizei um menu rápido para navegar no projeto:

🏠 Comece por aqui
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/00_comece_por_aqui

⚡ Resumo executivo do case
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md

🧭 Como navegar no GitHub sem experiência técnica
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/00_para_nao_tecnicos/00_COMO_NAVEGAR_NO_GITHUB.md

🗺️ Escolha sua trilha
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/02_MAPA_DAS_TRILHAS.md

🎓 Guia integrado da Aula 1
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/03_GUIA_AULA_01_NEGOCIOS_E_TECNOLOGIA.md

🗄️ Dossiê auditado dos Exhibits
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/05_DOSSIE_EXHIBITS_M2.md

🧪 Hipóteses e plano de análise
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/06_CADERNO_DE_HIPOTESES_ANALITICAS.md

📋 Divisão de tarefas
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/01_gerenciamento_de_tarefas/00_MAPA_GERAL_FRENTES_DE_ATUACAO.md

Se for seu primeiro acesso, comece pela visão geral e depois escolha uma trilha.
```

---

## 📚 Versão completa

```text
📚 MBA Inteli — Módulo 2
Case Vitaliza: churn, machine learning, uplift e IA generativa

Estruturei este índice para facilitar o acesso direto da equipe aos documentos do repositório no GitHub.

1️⃣ COMEÇAR AQUI

🏠 Página de entrada e roteiro de leitura
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/00_comece_por_aqui

⚡ Resumo executivo do case
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md

🧭 Mapa visual, trilhas e sequência de estudo
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/02_MAPA_DAS_TRILHAS.md

2️⃣ MATERIAL DA AULA E DADOS

🎓 Aula 1 integrada: negócios + tecnologia
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/03_GUIA_AULA_01_NEGOCIOS_E_TECNOLOGIA.md

🗄️ Auditoria real dos Exhibits
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/05_DOSSIE_EXHIBITS_M2.md

📖 Dicionário detalhado das 13 fontes
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/05_DOSSIE_DICIONARIO_DE_DADOS_M2.md

🧪 Caderno de hipóteses analíticas
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/06_CADERNO_DE_HIPOTESES_ANALITICAS.md

3️⃣ ESCOLHA SUA FRENTE

📊 Negócios, Growth, CRM e Uplift
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/00_comece_por_aqui/01_trilha_negocios_e_crm

📈 Ciência de Dados e Machine Learning
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/00_comece_por_aqui/02_trilha_ciencia_de_dados_e_ml

🤖 IA Generativa e Multimodal
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/00_comece_por_aqui/03_trilha_ia_generativa_e_multimodal

📋 Tarefas e divisão do grupo
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/01_gerenciamento_de_tarefas

4️⃣ ENTREGÁVEIS

📌 O que preparar para A1 e A2
https://github.com/leomaquiaveli/02-mba-modulo-2/blob/main/00_comece_por_aqui/04_contexto_extra/01_VISAO_DETALHADA_SEMANA5_VS_SEMANA10.md

📊 Artefatos de Negócios
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/artefatos_negocios

💻 Artefatos de Tecnologia
https://github.com/leomaquiaveli/02-mba-modulo-2/tree/main/artefatos_tecnologia

⚠️ Os dados brutos não ficam públicos. O GitHub contém documentação, código, testes e resultados agregados.
```

---

## 🛠️ Como finalizar o menu

Quando a URL pública existir, confirme também o nome da branch principal. Os exemplos usam `main`; ajuste os caminhos se a publicação usar outra branch. Substitua o placeholder em todo o arquivo:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('00_comece_por_aqui/07_MENU_WHATSAPP.md')
text = p.read_text(encoding='utf-8')
text = text.replace('<URL_DO_REPOSITORIO>', 'https://github.com/ORGANIZACAO/REPOSITORIO')
p.write_text(text, encoding='utf-8')
PY
```

Depois, abra pelo menos três links da mensagem em uma janela anônima. Assim você confirma que o repositório e os documentos estão públicos para quem receber o WhatsApp.
