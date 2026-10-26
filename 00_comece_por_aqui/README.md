# 🔰 Comece por Aqui — Guia de Entrada do Case Vitaliza

> **Módulo 2:** IA e Dados para Negócios — Case Vitaliza  
> **Equipe:** Projetos MBA Inteli  
> **Foco deste documento:** Roteiro de leitura e navegação por perfil

Como transformar dados de treino, assinaturas e relacionamento em uma decisão de retenção que gere retorno? Este é o fio condutor do projeto. Esta página organiza a leitura para que cada integrante entenda o problema, encontre sua contribuição e acompanhe a construção da solução.

> 🔰 **Primeiro acesso?** Leia o [resumo executivo](./01_RESUMO_EXECUTIVO_DO_CASE.md), escolha uma rota no [mapa das trilhas](./02_MAPA_DAS_TRILHAS.md) e consulte a [visão de A1 e A2](./04_contexto_extra/01_VISAO_DETALHADA_SEMANA5_VS_SEMANA10.md). Você terá o contexto necessário para começar a trabalhar.

---

## 🧭 Escolha seu ponto de partida

| O que você precisa agora | Comece por | Ao terminar, você deve conseguir… |
| :--- | :--- | :--- |
| Entender a Vitaliza e o desafio | [Resumo executivo do case](./01_RESUMO_EXECUTIVO_DO_CASE.md) | explicar o problema, as restrições e o resultado esperado |
| Encontrar sua área de contribuição | [🗺️ Mapa das Trilhas](./02_MAPA_DAS_TRILHAS.md) | escolher uma rota e entender suas dependências |
| Relacionar a aula ao projeto | [Guia integrado da Aula 1](./03_GUIA_AULA_01_NEGOCIOS_E_TECNOLOGIA.md) | conectar conceitos de negócios e tecnologia às decisões do case |
| Saber o que entra nas entregas | [Guia de A1 e A2](./04_contexto_extra/01_VISAO_DETALHADA_SEMANA5_VS_SEMANA10.md) | separar diagnóstico, baseline e solução integrada |
| Entender os arquivos disponíveis | [Dicionário de dados comentado](./05_DOSSIE_DICIONARIO_DE_DADOS_M2.md) | localizar campos, granularidade e cuidados de integração |
| Conhecer os achados da auditoria | [Dossiê dos Exhibits](./05_DOSSIE_EXHIBITS_M2.md) | distinguir o conteúdo previsto das inconsistências observadas |
| Transformar uma suspeita em análise | [Caderno de hipóteses](./06_CADERNO_DE_HIPOTESES_ANALITICAS.md) | registrar população, método, evidência e limitações |
| Compartilhar os acessos com a equipe | [Menu para WhatsApp](./07_MENU_WHATSAPP.md) | preparar uma mensagem com os caminhos principais |

---

## 🗺️ Um percurso comum, três trilhas de conhecimento

Todas as pessoas precisam conhecer a pergunta de negócio e as regras do case. Depois dessa leitura comum, o aprofundamento acontece em três trilhas complementares:

| Trilha | Pergunta que orienta o trabalho | Guias disponíveis |
| :--- | :--- | :--- |
| 📊 **01 · Negócios e CRM** | Por que perdemos assinantes e onde vale a pena investir em retenção? | [Visão da trilha](./01_trilha_negocios_e_crm/README.md) · [Análise dos 13 exhibits](./01_trilha_negocios_e_crm/03_ANALISE_EXHIBITS_M2.md) · [Diagnóstico A1](./01_trilha_negocios_e_crm/01_DIAGNOSTICO_ESTRATEGICO_A1_SEMANA5.md) · [Uplift e retorno A2](./01_trilha_negocios_e_crm/02_ESTRATEGIA_UPLIFT_E_ROI_A2_SEMANA10.md) |
| 💻 **02 · Ciência de Dados e ML** | Como construir uma base confiável, segmentar e prever saída? | [Visão da trilha](./02_trilha_ciencia_de_dados_e_ml/README.md) · [Reconstrução histórica](./02_trilha_ciencia_de_dados_e_ml/01_SANEAMENTO_E_RECONSTRUCAO_HISTORICA.md) · [Clusterização e previsão](./02_trilha_ciencia_de_dados_e_ml/02_CLUSTERIZACAO_E_CHURN_SUPERVISIONADO.md) |
| 🤖 **03 · IA Generativa e Multimodal** | Texto e imagem melhoram a decisão e a comunicação? | [Visão da trilha](./03_trilha_ia_generativa_e_multimodal/README.md) · [Extração e redação de CRM](./03_trilha_ia_generativa_e_multimodal/01_EXTRACAO_MULTIMODAL_E_COPYWRITING_CRM.md) · [Arquitetura e contratos](./03_trilha_ia_generativa_e_multimodal/02_ARQUITETURA_E_CONTRATOS_MULTIMODAIS.md) · [Avaliação e governança](./03_trilha_ia_generativa_e_multimodal/03_AVALIACAO_SEGURANCA_E_GOVERNANCA.md) |

**Gestão e qualidade atravessam as três trilhas.** Para assumir uma tarefa, consulte o [mapa das frentes](../01_gerenciamento_de_tarefas/00_MAPA_GERAL_FRENTES_DE_ATUACAO.md) e a [matriz de tarefas](../01_gerenciamento_de_tarefas/MATRIZ_DE_TAREFAS_E_ESPECIFICACOES.md). As trilhas organizam o conhecimento; as frentes organizam a execução.

---

## 🔍 Como ler os materiais com confiança

| Tipo de conteúdo | O que representa | Onde consultar |
| :--- | :--- | :--- |
| **Fonte oficial** | contexto, objetivos, premissas e definição dos arquivos | [Enunciado](<../documentos/enunciado_e_guias/Vitaliza - Enunciado do case.pdf>) e [dicionário original](<../documentos/enunciado_e_guias/Vitaliza - Dicionário de dados.pdf>) |
| **Evidência observada** | contagens e inconsistências já verificadas nos arquivos locais | [Dossiê de auditoria](./05_DOSSIE_EXHIBITS_M2.md) e [relatório JSON](../relatorios/auditoria_exhibits.json) |
| **Plano de trabalho** | método proposto, hipótese ou saída ainda a construir | guias das trilhas, [caderno](./06_CADERNO_DE_HIPOTESES_ANALITICAS.md) e documentos de entrega |
| **Resultado validado** | análise executada, reproduzível e revisada pela equipe | deverá ser incorporado aos artefatos com referência ao código e às métricas |

A auditoria inicial existe. Modelos, segmentos, uplift e retorno financeiro continuam sendo trabalho a desenvolver. As orientações destes guias não representam resultados já obtidos.

---

## 🤝 Primeira contribuição, mesmo sem experiência técnica

1. Leia [como navegar no repositório](./00_para_nao_tecnicos/00_COMO_NAVEGAR_NO_GITHUB.md).
2. Escolha uma pergunta da sua trilha e uma tarefa correspondente.
3. Registre sua contribuição com fonte, população e período; use [o guia de contribuição](./00_para_nao_tecnicos/01_GUIA_DE_CONTRIBUICAO_E_COMMITS.md) para enviá-la para revisão.
4. Relacione a contribuição ao artefato de negócios ou tecnologia que vai utilizá-la.

👉 **Próximo passo:** abra o [resumo executivo](./01_RESUMO_EXECUTIVO_DO_CASE.md). Para retornar à visão de todo o projeto, acesse o [README principal](../README.md).
