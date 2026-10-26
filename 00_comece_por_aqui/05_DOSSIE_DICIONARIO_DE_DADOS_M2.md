# 🗄️ Dossiê do Dicionário de Dados — Fontes, Campos & Integração

> **Módulo 2:** IA e Dados para Negócios — Case Vitaliza  
> **Equipe:** Projetos MBA Inteli  
> **Foco deste documento:** Catálogo comentado das 13 fontes do Data Room

[🔰 Comece por Aqui](./README.md) / Dicionário de dados

🎯 **Finalidade:** localizar os campos do data room e entender como cada fonte pode ser usada. Este guia comenta o [dicionário oficial](<../documentos/enunciado_e_guias/Vitaliza - Dicionário de dados.pdf>); inconsistências observadas nos arquivos estão no [dossiê da auditoria](./05_DOSSIE_EXHIBITS_M2.md).

**Referência temporal:** exportação em 01/10/2026 e corte declarado em 30/09/2026. As contagens descrevem os arquivos; a existência de registros pós-corte exige filtros explícitos.

---

## 🧭 1. Escolha a fonte pela pergunta

| Pergunta | Fontes principais | Granularidade que exige cuidado |
| :--- | :--- | :--- |
| Quem é a pessoa e como chegou? | usuários e onboarding | conta e resposta inicial |
| Quem estava ativo em uma data? | assinaturas e eventos de assinatura | episódio de assinatura e evento |
| O que foi cobrado e recuperado? | pagamentos | tentativa de cobrança |
| Como o produto foi usado? | uso mensal e atividades | pessoa-mês e treino |
| Existe vínculo social? | amizades e feed | relação direcionada e post |
| Que fricção foi relatada? | tickets e pesquisa de saída | chamado e resposta voluntária |
| O contato mudou retenção? | campanha e eventos | pessoa sorteada e desfecho posterior |
| O que as rotas acrescentam? | heatmaps | pessoa-data, com janela de 90 dias |

O catálogo reúne 13 fontes lógicas: 11 CSVs, um Parquet e a coleção de imagens. A coleção de heatmaps chega em dois pacotes, um para cada data. As seções do PDF começam na visão geral e chegam à seção 14; isso não significa 14 bases independentes.

`user_id` é a chave da conta e liga grande parte das fontes. Em amizades, a ligação acontece por `seguidor_id` e `seguido_id`. A chave primária de uma assinatura, post ou ticket continua sendo a chave do registro correspondente. Agregue fontes de múltiplas linhas por pessoa antes de formar a base analítica.

**Como consultar:** leia os cuidados da seção 2, localize a fonte na seção 3 e use o [guia de reconstrução](./02_trilha_ciencia_de_dados_e_ml/01_SANEAMENTO_E_RECONSTRUCAO_HISTORICA.md) para transformar os campos em regras de preparação.

---

## ⚠️ 2. Cinco cuidados antes de integrar as fontes

1. **`assinaturas.csv` NÃO é histórico (Sobrescrita de Estado):**

   O sistema de assinaturas guarda apenas a situação atual de cada assinatura em `01/10/2026`. Para reconstruir quem estava ativo no início de cada mês ou na data de corte (`30/09/2026`), a fonte obrigatória é **`eventos_assinatura.csv`** (para eventos desde `01/07/2024`, complementado por `assinaturas.csv` para inícios anteriores).
2. **Diferença de Fuso Horário em `eventos_assinatura.csv`:**

   Os webhooks da App Store e Google Play chegam em **UTC (terminados em `"Z"`)**, enquanto os eventos do site da Vitaliza são gravados em **Horário de Brasília (`America/Sao_Paulo`, UTC-3)**. Na virada do último dia do mês (ex.: `30/09/2026` entre 21h e 23h59 BRT), não converter o fuso desloca o evento para o mês seguinte!
3. **Assinaturas Concluídas no Mesmo Mês vs. Série de Churn Mensal:**

   Os **3.389 fins de assinatura** de junho a setembro de 2026 e as **3.362 perdas da série mensal** medem coisas diferentes: a métrica oficial de churn mensal conta apenas quem estava **ativo no início do mês**, deixando de fora assinaturas que começaram e terminaram dentro do mesmo mês.
4. **Viés de Seleção e Ativos Pós-Corte em `pesquisa_saida.csv`:**

   A pesquisa existe apenas desde `01/06/2026` e somente para quem cancela pelo site (30% da base). Das 643 respostas (de 641 contas), **289 são de assinantes que cancelaram pelo site mas seguiam ativos em `30/09/2026`** porque o período já pago terminava depois da data de corte.
5. **Prevenção de *Data Leakage* (Vazamento de Futuro):**

   Nenhum dado com carimbo de tempo posterior a `30/09/2026` (ou eventos que revelam o desfecho futuro) pode entrar nas variáveis explicativas do modelo de previsão de 60 dias (que prevê a saída até `29/11/2026`).

---

## 📚 3. Catálogo das 13 fontes e seus campos

### Seção 02 — Cadastro de Contas (`usuarios.csv`)

* **Forma:** Tabela | **Granularidade:** 1 linha por conta | **Volume:** `64.948 linhas`
* **Descrição:** Contém todas as contas criadas desde setembro de 2020 (grátis e pagas). Campos digitados pelo usuário não possuem validação de formulário.
* **Colunas:**
  * `user_id`: Identificador único da conta (chave primária de ligação).
  * `email`: E-mail de cadastro.
  * `data_cadastro`: Data e hora do cadastro.
  * `data_nascimento`: Informada pelo usuário.
  * `sexo`: Informado pelo usuário.
  * `cidade`, `uf`: Informados pelo usuário em texto livre (sujeito a variações de grafia/maiúsculas).
  * `cep_prefixo`: 3 primeiros dígitos do CEP.
  * `canal_aquisicao`: Canal atribuído pelo marketing no momento do cadastro (orgânico, influenciadores, anúncios, indicação, parcerias corporativas).
  * `sistema`: Sistema operacional do celular (`iOS` / `Android`).
  * `versao_app`: Última versão do aplicativo vista.
  * `relogio_conectado`: Relógio conectado à conta, se houver (`Garmin`, `Apple Watch`; a auditoria local encontrou `nenhum` para ausência).

---

### Seção 03 — Assinaturas (`assinaturas.csv`)

* **Forma:** Tabela | **Granularidade:** 1 linha por assinatura | **Volume:** `32.643 linhas` (Retrato de `01/10/2026`)
* **Descrição:** Cada vez que uma conta passa a pagar, nasce um `assinatura_id`. A mesma conta (`user_id`) pode ter mais de uma assinatura ao longo do tempo (assina, cancela e retorna meses depois).
* **Colunas:**
  * `assinatura_id`: Identificador único da assinatura.
  * `user_id`: Conta associada.
  * `plano_atual`: `mensal` ou `anual` no escopo pagante; a auditoria também encontrou `cortesia`.
  * `canal_cobranca`: `app_store`, `google_play`, `web_cartao` ou `web_pix` no escopo pagante; cortesias usam `interno`.
  * `inicio`: Data da primeira cobrança.
  * `status_atual`: Situação em `01/10/2026`.
  * `renovacao_automatica`: Situação em `01/10/2026`.
  * `data_fim`: Quando a assinatura terminou, se terminou.
  * `motivo_fim`: Motivo registrado no fim, se houver.

---

### Seção 04 — Rede de Seguidores (`amizades.csv`)

* **Forma:** Tabela | **Granularidade:** 1 relação de seguir por linha | **Volume:** `113.480 linhas`
* **Descrição:** Grafo direcionado de seguidores (mão única: se Ana segue Bruno e Bruno segue Ana, existem duas linhas). Permite calcular grau de entrada (seguidores), grau de saída (seguindo) e reciprocidade.
* **Colunas:**
  * `seguidor_id`: `user_id` de quem segue.
  * `seguido_id`: `user_id` de quem é seguido.
  * `desde`: Data em que passou a seguir.

---

### Seção 05 — Campanha de Agosto de 2026 (`campanha_ago26.csv`)

* **Forma:** Tabela | **Granularidade:** 1 linha por assinante sorteado | **Volume:** `14.120 linhas`
* **Descrição:** Único experimento controlado randomizado (RCT / Teste A/B) da Vitaliza, disparado em `10/08/2026` para toda a base pagante daquele dia, dividida em 4 grupos de tamanho semelhante.
* **Colunas:**
  * `user_id`: Conta sorteada.
  * `grupo`: `controle` (não recebeu mensagem), `desafio`, `cupom` ou `conteudo`.
  * `enviado_em`: Data/hora de envio.
  * `canal`: `push+email`.
  * `titulo_mensagem`: Título da comunicação enviada:
    * Desafio: *"Novo desafio de 6 semanas montado para você"*
    * Cupom: *"Oferta para voltar a treinar"*
    * Conteúdo: *"Seu plano de treino personalizado está pronto"*
  * `oferta`: Oferta do grupo cupom: `30pct_3_meses` (mensal) ou `1_mes_gratis` (anual).
  * `abriu_push`, `abriu_email`, `clicou`: Indicadores de engajamento com a mensagem.

---

### Seção 06 — Eventos de Assinatura (`eventos_assinatura.csv`)

* **Forma:** Log de eventos | **Granularidade:** 1 evento por linha | **Volume:** `275.565 linhas` (desde `01/07/2024`)
* **Descrição:** Histórico imutável de acontecimentos do ciclo de vida de cada assinatura. Fonte primária para reconstruir estados na cobertura observada, complementando episódios anteriores quando necessário.
* **Colunas:**
  * `user_id`: Conta associada.
  * `data_hora`: Carimbo de tempo do recebimento (Lojas em `UTC "Z"`; Site em `Horário de Brasília`).
  * `evento`: Valores possíveis:
    * `trial_iniciado`, `trial_expirado`
    * `assinatura_iniciada`, `renovacao`
    * `renovacao_automatica_desligada`, `renovacao_automatica_religada`
    * `periodo_carencia`, `assinatura_expirada`
    * `cancelamento_web`, `reembolso`, `chargeback`
  * `plano`: Plano no momento do evento.
  * `canal_cobranca`: Canal de cobrança.
  * `detalhe`: Informação adicional (nem sempre preenchida).

---

### Seção 07 — Pagamentos (`pagamentos.csv`)

* **Forma:** Log de eventos | **Granularidade:** 1 tentativa de cobrança por linha | **Volume:** `165.548 linhas`
* **Descrição:** Registra o fluxo financeiro real, incluindo reajuste de preço em `01/03/2026`, descontos aplicados, retentativas após recusa de cartão (`tentativa`) e estornos/chargebacks. Permite separar churn voluntário de churn involuntário (inadimplência técnica).
* **Colunas:**
  * `pagamento_id`: Identificador da cobrança.
  * `user_id`: Conta associada.
  * `data_hora`: Quando a cobrança foi processada.
  * `valor`: Valor cobrado em R$.
  * `metodo`: `app_store`, `google_play`, `cartao` ou `pix_automatico`.
  * `status`: `aprovado`, `recusado`, `estornado` ou `chargeback`.
  * `tentativa`: Número sequencial da tentativa de cobrança.

---

### Seção 08 — Uso Mensal (`uso_mensal.csv`)

* **Forma:** Log de eventos | **Granularidade:** 1 linha por usuário e mês | **Volume:** `591.662 linhas` (jan/2025 a set/2026)
* **Descrição:** Tabela consolidada mensalmente pelo BI para os painéis de engajamento.
* **Colunas:**
  * `user_id`: Conta associada.
  * `mes`: Competência no formato `AAAA-MM`.
  * `atividades`: Total de treinos registrados no mês.
  * `atividades_ar_livre`: Soma de treinos de corrida, caminhada e pedal.
  * `atividades_video`: Soma de treinos guiados em vídeo (funcional, força, yoga).
  * `minutos`: Total de minutos de treino no mês.
  * `dias_ativos`: Quantidade de dias com pelo menos um treino.
  * `sessoes_app`: Quantidade de aberturas do aplicativo no mês.

---

### Seção 09 — Treinos Detalhados (`atividades.parquet`)

* **Forma:** Log de eventos (Parquet) | **Granularidade:** 1 treino por linha | **Volume:** `1.254.475 linhas` (`01/01/2026` a `30/09/2026`)
* **Descrição:** Registro granular de cada treino em 2026. Permite detectar pausas intra-mês (ex.: 15 dias parado), evolução de ritmo, uso de relógio e treinos acompanhados (`treino_com`). Deve ser lido com `pandas`, `polars` ou `duckdb`.
* **Colunas:**
  * `atividade_id`: Identificador do treino.
  * `user_id`: Conta associada.
  * `inicio`: Data e hora de início do treino.
  * `tipo`: Modalidade do treino.
  * `duracao_min`: Duração em minutos.
  * `distancia_km`: Distância percorrida em km (quando há GPS).
  * `ritmo_min_km`: Pace em minutos por km (quando há GPS).
  * `fc_media`: Frequência cardíaca média (quando sincronizado via relógio).
  * `origem`: `app`, `garmin` ou `apple_health`.
  * `gps_ok`: Indicador se o GPS registrou o percurso corretamente.
  * `treino_com`: `user_id` de outra conta marcada como companhia no treino, se houver.

---

### Seção 10 — Questionário de Entrada (`onboarding.csv`)

* **Forma:** Texto livre e categórico | **Granularidade:** 1 linha por conta | **Volume:** `63.929 linhas`
* **Descrição:** Respondido na criação da conta. Contém a intenção original declarada pelo usuário em suas próprias palavras.
* **Colunas:**
  * `onboarding_id`: Identificador da resposta.
  * `user_id`: Conta associada.
  * `respondido_em`: Data da resposta.
  * `objetivo_texto`: Resposta aberta opcional à pergunta *"Qual o seu objetivo com a Vitaliza?"* (ex.: *"quero perder uns 15kg"*, *"treinar junto com meu namorado"*).
  * `como_conheceu`: Resposta livre opcional.
  * `nivel`: Nível autodeclarado.
  * `dias_por_semana`: Meta pretendida de dias de treino por semana (texto livre).

---

### Seção 11 — Pesquisa de Saída (`pesquisa_saida.csv`)

* **Forma:** Texto livre e categórico | **Granularidade:** 1 resposta por linha | **Volume:** `643 linhas` (desde `01/06/2026`)
* **Descrição:** Exibida apenas para cancelamentos realizados no site da Vitaliza.
* **Colunas:**
  * `resposta_id`: Identificador da resposta.
  * `user_id`: Conta associada.
  * `respondido_em`: Data da resposta.
  * `motivo_principal`: `preco`, `nao_uso`, `problema_tecnico`, `outro_app`, `saude` ou `outro`.
  * `comentario`: Comentário aberto opcional.

---

### Seção 12 — Posts da Rede Social (`feed_posts.csv`)

* **Forma:** Texto livre | **Granularidade:** 1 post por linha | **Volume:** `119.309 linhas` (`01/07/2025` a `30/09/2026`)
* **Descrição:** Textos curtos publicados espontaneamente no feed após os treinos.
* **Colunas:**
  * `post_id`: Identificador da publicação.
  * `user_id`: Autor do post.
  * `data_hora`: Data/hora da publicação (usar apenas até a data de corte da análise).
  * `texto`: Conteúdo textual livre do post.
  * `curtidas`: Número de curtidas recebidas.

---

### Seção 13 — Chamados ao Suporte (`tickets_suporte.csv`)

* **Forma:** Texto livre e categórico | **Granularidade:** 1 chamado por linha | **Volume:** `4.422 linhas` (`01/07/2025` a `30/09/2026`)
* **Descrição:** Contém a primeira mensagem enviada pelo cliente (por chat, e-mail ou loja) e a classificação atribuída pelo atendente.
* **Colunas:**
  * `ticket_id`: Identificador do chamado.
  * `user_id`: Conta associada.
  * `aberto_em`: Data/hora de abertura.
  * `canal`: `chat`, `email` ou `loja`.
  * `texto_cliente`: Primeira mensagem livre escrita pelo cliente (ex.: *"corrida registrada com distância zerada"*).
  * `categoria_atendente`: Categoria escolhida pelo atendente.
  * `status`: `resolvido`, `aberto` ou `sem_resposta`.
  * `resolvido_em`: Data de resolução, quando aplicável.

---

### Seção 14 — Mapas de Calor das Rotas (`heatmaps_90d/`)

* **Forma:** Imagem (`PNG`) | **Granularidade:** 1 imagem `<user_id>.png` por assinante pagante ao ar livre e data | **Volume:** `12.426 imagens` em `2026-07-31/` e `13.047 imagens` em `2026-09-30/`
* **Descrição:** Mostra espacialmente onde e com qual intensidade o assinante treinou nos 90 dias anteriores a cada data.
* **Regras de Interpretação das Cores do Mapa Estilizado:**
  * **Verde:** Parque
  * **Azul:** Água
  * **Cor de Areia:** Praia
  * **Amarelo:** Avenida
  * **Traçado da Rota:** Quanto mais vezes a pessoa passou por um trecho, mais forte é a cor da rota.
  * **Métodos de Extração Sugeridos no Case:** Contagem determinística de pixels por cor vs. interpretação por modelo multimodal de visão.

---

## ✅ 4. Checklist de uso de uma fonte

- A chave e a granularidade estão definidas antes do cruzamento?
- A data representa ocorrência, recebimento, atualização ou fechamento?
- O campo realmente estava disponível no corte histórico?
- Ausência, zero e categoria explícita foram diferenciados?
- A integração preservou a quantidade esperada de pessoas?
- O cálculo aponta para fonte, janela, transformação e regra de exclusão?

Status atual, curtidas acumuladas e resolução de tickets exigem atenção adicional: o valor observado na exportação pode não representar o valor conhecido no passado.

👉 **Continue:** [Exhibits auditados](./05_DOSSIE_EXHIBITS_M2.md) · [Preparação e reconstrução histórica](./02_trilha_ciencia_de_dados_e_ml/01_SANEAMENTO_E_RECONSTRUCAO_HISTORICA.md).
