# Entendendo o case Vitaliza

**Responsável pelas notas:** Ricardo Terzian
**Data:** 09/11/2026
**Referência temporal dos dados:** 30/09/2026
**Objetivo:** explicar o problema e orientar o trabalho do MBA em linguagem simples.

## 1. O que é a Vitaliza?

A Vitaliza é um aplicativo brasileiro fictício para quem pratica atividades físicas. O produto combina três experiências:

- Registro de corrida, caminhada e pedal com GPS.
- Aulas em vídeo, como funcional, força e yoga.
- Rede social para acompanhar pessoas e compartilhar treinos e publicações.

O aplicativo também conecta relógios Garmin e Apple Watch. O modelo é freemium: existem contas gratuitas e assinaturas Premium. Por isso, número de contas cadastradas e número de assinantes pagantes são medidas diferentes.

O plano mensal custa R$ 39,90 desde março de 2026; antes custava R$ 34,90. O plano anual tem preço de referência de R$ 299,90. Esses valores são regras do case, não preços de um serviço real.

## 2. Qual é o problema?

A empresa está perdendo assinantes com mais frequência. Segundo o resumo executivo do projeto, o churn mensal médio passou de **5,6% em 2025 para 6,6% entre janeiro e setembro de 2026**, com pico de **8,1% em abril de 2026**.

Churn é a saída de assinantes. Na série mensal do case, a taxa compara as perdas de assinaturas que estavam ativas no início do mês com a quantidade de assinaturas ativas nesse início de mês. É preciso manter o mesmo denominador ao comparar períodos.

A pergunta não se limita a identificar quem pode sair. A decisão central é:

> Em quais assinantes vale a pena investir para aumentar a retenção e o resultado financeiro, respeitando o orçamento e a capacidade de atendimento?

A referência de população é de **14.753 pagantes ativos em 30/09/2026**, conforme os materiais do projeto. Essa referência precisa ser reconciliada pelos dados históricos na execução analítica.

## 3. O que a equipe precisa descobrir?

O trabalho se organiza em quatro perguntas:

1. **Quem sai?** Identificar diferenças entre assinantes, como plano, tempo de relacionamento e comportamento de uso.
2. **Por que sai?** Investigar hipóteses, como preço, queda de uso ou problemas no serviço, sem tratar associação como prova de causa.
3. **Quem responde a uma ação?** Avaliar quem tem maior chance de permanecer por causa do contato ou da oferta.
4. **Em quem agir?** Escolher ações cujo benefício esperado compense seus custos e respeite os limites operacionais.

Por exemplo, observar menos treinos entre quem cancela pode ser útil para previsão, mas não prova que aumentar os treinos evitaria o cancelamento. Da mesma forma, o reajuste de março é uma hipótese a investigar, não uma causa já demonstrada.

## 4. Por que prever cancelamento não basta?

Um modelo de risco estima a probabilidade de saída. Já uma análise de **uplift** estima a diferença que uma intervenção pode produzir em comparação com não intervir.

Imagine dois assinantes com alto risco: um permanece após uma ação adequada; o outro cancela mesmo recebendo desconto. Contatar ambos pode consumir orçamento sem o mesmo retorno.

Também há quem renovaria sem incentivo e quem pode ser levado a cancelar ao receber um lembrete sobre a assinatura. Portanto, oferecer desconto ou contato para todos não é uma política automaticamente vantajosa.

O case disponibiliza uma campanha experimental de agosto de 2026 para estudar o efeito das ações. É necessário conferir o desenho do experimento, os grupos e as janelas de acompanhamento antes de estimar esse efeito.

## 5. Quais são as restrições?

| Recurso | Limite mensal informado no projeto |
|---|---:|
| Orçamento de retenção | R$ 40.000 |
| Mensagens de WhatsApp | 1.500 |
| Atendimentos de Customer Success (CS) | 300 |

O orçamento considera custos dos canais, descontos e uso de IA generativa. O objetivo econômico deve considerar o ganho incremental líquido: o que a ação acrescenta em relação a não agir, descontados os custos relevantes.

Os materiais do projeto apontam que aproximadamente 70% dos pagantes ativos contratam pelas lojas de aplicativos. Nesses canais, desligar a renovação pode ocorrer fora do site da Vitaliza. Uma intervenção apenas na tela de cancelamento do site tem cobertura limitada.

## 6. Quais dados ajudam a responder?

| Fonte | Como ajuda |
|---|---|
| `usuarios.csv` | Cadastro e características das contas. |
| `eventos_assinatura.csv` | Reconstrução da situação da assinatura em uma data. |
| `assinaturas.csv` | Retrato das assinaturas em 01/10/2026; exige cuidado para análise histórica. |
| `pagamentos.csv` | Cobranças e falhas de pagamento. |
| `uso_mensal.csv` e `atividades.parquet` | Uso do produto e comportamento de treino. |
| `amizades.csv` e `feed_posts.csv` | Relações de seguidores e publicações. |
| `onboarding.csv`, `pesquisa_saida.csv` e `tickets_suporte.csv` | Objetivos declarados, motivos de saída e problemas relatados. |
| `campanha_ago26.csv` | Comparação das intervenções da campanha experimental. |
| Imagens de heatmaps | Sinais visuais que podem ser transformados em variáveis e avaliados. |

Essas fontes não devem ser reunidas indiscriminadamente. Cada pergunta define quais arquivos, períodos e variáveis são necessários. Textos e imagens exigem extração e validação antes de entrar em um modelo.

## 7. Quais cuidados evitam conclusões erradas?

- **Respeitar o corte:** usar somente informações disponíveis até 30/09/2026 para a decisão nessa data. Resultados futuros podem servir como alvo de avaliação, nunca como variável explicativa disponível no passado.
- **Reconstruir o histórico:** `assinaturas.csv` é um retrato de 01/10/2026; usar os eventos para determinar a situação em datas anteriores.
- **Conferir fusos:** horários das lojas em UTC e registros do site em Brasília precisam de tratamento consistente.
- **Auditar a qualidade:** verificar datas futuras, categorias com grafias diferentes, ausentes, duplicações e chaves antes de calcular indicadores.
- **Separar populações:** conta gratuita, assinatura histórica, cortesia e pagante ativo não são a mesma coisa.
- **Reconhecer vieses:** a pesquisa de saída é opcional e ligada ao cancelamento pelo site; não representa automaticamente toda a base.
- **Separar risco de efeito:** um bom classificador de churn não demonstra que uma oferta funcionará.

## 8. O que precisa ser entregue?

| Etapa | Negócios | Tecnologia |
|---|---|---|
| **A1 — Semana 5: entender** | Diagnóstico, segmentação, personas e prioridades com limitações explícitas. | Preparação dos dados, análise exploratória, clusterização e modelo inicial de referência. |
| **A2 — Semana 10: agir** | Recomendação ao conselho, ações, retorno esperado, orçamento e riscos. | Comparação de modelos, avaliação temporal, uso validado de texto/imagem e apoio à decisão de CRM. |

O modelo inicial serve de referência para avaliar se soluções mais complexas realmente melhoram o resultado. Uma entrega consistente conecta o diagnóstico à escolha de quem contatar, por qual canal, com qual ação e por qual benefício esperado.

## 9. Como estas notas devem ser usadas?

Este documento é uma síntese de estudo, baseada nos materiais já presentes no repositório. Não executa uma nova análise, não recalcula indicadores e não apresenta uma política de retenção validada. Os números citados são referências do projeto e precisam manter vínculo com as fontes oficiais e com consultas reproduzíveis nas entregas analíticas.

Para Ricardo, um caminho prático é começar pela qualidade dos dados, confirmar a população e o corte, formular hipóteses e registrar cada conclusão com evidência e limitação. Depois, conectar essas conclusões aos artefatos de negócios e tecnologia.

## Fontes e próximos passos

- [Resumo executivo do case](../../00_comece_por_aqui/01_RESUMO_EXECUTIVO_DO_CASE.md): contexto, indicadores e restrições usados nesta síntese.
- [README do projeto](../../README.md): visão geral e estrutura dos artefatos.
- [Enunciado oficial](../../documentos/enunciado_e_guias/Vitaliza%20-%20Enunciado%20do%20case.pdf): referência para conferir as regras e requisitos.
- [Dicionário de dados](../../documentos/enunciado_e_guias/Vitaliza%20-%20Dicion%C3%A1rio%20de%20dados.pdf): referência para conferir o significado das colunas antes das análises.
- [Roteiro de execução prática](../../01_gerenciamento_de_tarefas/roteiro_execucao_pratica/00_VISAO_GERAL_E_FERRAMENTAS.md): organização da execução.
