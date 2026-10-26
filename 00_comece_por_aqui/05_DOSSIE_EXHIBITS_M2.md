# 🔍 Dossiê dos Exhibits M2 — Auditoria, Reconciliação & Qualidade

> **Módulo 2:** IA e Dados para Negócios — Case Vitaliza  
> **Equipe:** Projetos MBA Inteli  
> **Foco deste documento:** Achados da auditoria local do Data Room

[🔰 Comece por Aqui](./README.md) / Exhibits auditados

> Auditoria empírica dos arquivos em `documentos/exhibits-m2/`.
>
> Data da auditoria: 24/10/2026. Os números abaixo foram calculados diretamente nos CSVs e no Parquet; não são apenas transcrições do enunciado.

---

## ⚡ Leitura rápida da auditoria

| Achado | Implicação prática |
| :--- | :--- |
| 14.813 ativas = 14.753 pagantes + 60 cortesias | a população pagante precisa excluir cortesias |
| Registros com data posterior a 30/09 | a descrição do pacote não substitui filtro temporal |
| Categorias inconsistentes e valor monetário como texto | a preparação deve converter e validar explicitamente |
| Retrato atual da assinatura | histórico precisa ser reconstruído pelos eventos |
| Heatmaps com volumes esperados | inventário não é avaliação visual completa das imagens |

**Evidência de execução:** [relatório JSON](../relatorios/auditoria_exhibits.json) e [script de auditoria](../src/01_auditoria_data_room.py). O status registrado é `passed_with_warnings`; isso não significa que a base esteja pronta para modelar.

Para reproduzir na raiz do projeto, com os dados locais presentes:

```bash
uv run --with duckdb --with pytz \
  python src/01_auditoria_data_room.py \
  --json relatorios/auditoria_exhibits.json
```

---

## 🔒 1. Escopo e regra de publicação

O pacote entregue contém 11 arquivos CSV, um arquivo Parquet, dois pacotes de mapas de calor e o ZIP original. O material bruto soma centenas de megabytes e inclui campos como e-mail e textos livres, ainda que o case seja fictício.

Por esse motivo:

- dados brutos permanecem locais e ignorados pelo Git;
- o repositório publica documentação, código, schemas, testes e resultados agregados;
- nenhuma amostra publicada deve expor e-mail, texto individual ou identificador completo;
- relatórios devem registrar consulta, corte temporal e regra de agregação.

---

## 🗄️ 2. Inventário verificado

| Fonte | Linhas verificadas | Granularidade | Uso principal |
|---|---:|---|---|
| `usuarios.csv` | 64.948 | uma conta | cadastro, aquisição, dispositivo e relógio |
| `assinaturas.csv` | 32.643 | uma assinatura | retrato do ciclo atual da assinatura |
| `amizades.csv` | 113.480 | uma relação direcionada | rede social e conexões |
| `campanha_ago26.csv` | 14.120 | um participante sorteado | experimento de retenção |
| `eventos_assinatura.csv` | 275.565 | um evento | reconstrução temporal da assinatura |
| `pagamentos.csv` | 165.548 | uma tentativa de cobrança | receita, recusa, estorno e chargeback |
| `uso_mensal.csv` | 591.662 | usuário-mês | comportamento mensal agregado |
| `atividades.parquet` | 1.254.475 | um treino | comportamento granular em 2026 |
| `onboarding.csv` | 63.929 | uma resposta inicial | intenção declarada e perfil |
| `pesquisa_saida.csv` | 643 | uma resposta de saída | motivo declarado por parte dos cancelamentos web |
| `feed_posts.csv` | 119.309 | um post | texto social e engajamento |
| `tickets_suporte.csv` | 4.422 | um ticket | problemas, categoria e resolução |
| `heatmaps_2026-07-31.zip` | 12.426 imagens esperadas | usuário-data | padrão espacial de treino |
| `heatmaps_2026-09-30.zip` | 13.047 imagens esperadas | usuário-data | padrão espacial de treino |

As chaves primárias testadas em usuários, assinaturas, campanha, pagamentos, onboarding, pesquisa de saída, posts, tickets e atividades não apresentaram duplicidade.

---

## ⚖️ 3. Reconciliação da base ativa

`assinaturas.csv` contém 14.813 assinaturas com `status_atual = ativa`:

- 14.753 assinaturas pagantes (`mensal` ou `anual`);
- 60 cortesias (`plano_atual = cortesia`, canal `interno`).

Isso explica por que uma contagem ingênua de “ativas” não coincide com o número oficial de pagantes do case.

### 3.1 Distribuição dos 14.753 pagantes

| Dimensão | Categoria | Quantidade | Participação |
|---|---|---:|---:|
| Plano | anual | 8.478 | 57,47% |
| Plano | mensal | 6.275 | 42,53% |
| Canal | App Store | 5.395 | 36,57% |
| Canal | Google Play | 4.964 | 33,65% |
| Canal | cartão no site | 2.994 | 20,29% |
| Canal | Pix no site | 1.400 | 9,49% |

As lojas representam 70,22% da base pagante ativa. A assimetria de cancelamento fora do app é, portanto, uma restrição estrutural, não um detalhe de interface.

---

## 🧪 4. Campanha de agosto

A campanha está bem distribuída entre quatro grupos:

| Grupo | Pessoas | Abriu push | Abriu e-mail | Clicou |
|---|---:|---:|---:|---:|
| conteúdo | 3.554 | 32,05% | 17,98% | 14,91% |
| controle | 3.579 | 0,00% | 0,00% | 0,00% |
| cupom | 3.472 | 31,60% | 18,98% | 16,45% |
| desafio | 3.515 | 30,61% | 18,38% | 14,31% |

O cupom teve o maior clique bruto. Isso não prova maior retenção. Para medir efeito incremental, é necessário cruzar os grupos com a definição de saída e comparar cada tratamento ao controle, preservando o sorteio original.

---

## 🔎 5. Evidências iniciais úteis

### 5.1 Pesquisa de saída

Entre 643 respostas:

| Motivo | Respostas | Participação |
|---|---:|---:|
| preço | 264 | 41,06% |
| outro | 223 | 34,68% |
| não uso | 81 | 12,60% |
| outro app | 34 | 5,29% |
| problema técnico | 27 | 4,20% |
| saúde | 14 | 2,18% |

Preço é o motivo mais selecionado, mas a pesquisa cobre apenas parte dos cancelamentos do site e depende de resposta voluntária. Ela gera hipótese; não representa todos os assinantes.

### 5.2 Suporte

Dos 4.422 tickets:

- 65,97% estavam resolvidos;
- 22,18% permaneciam abertos;
- 11,85% estavam sem resposta.

As maiores categorias registradas são técnico (961), cancelamento (913), conta (757), cobrança (651), conteúdo (588) e dúvida geral (552). O texto do cliente pode revelar diferenças entre o problema real e a categoria escolhida pelo atendente.

### 5.3 Atividades

O Parquet contém 1.254.475 treinos de 36.551 usuários. As origens são:

- app: 881.706;
- Garmin: 207.954;
- Apple Health: 164.815.

Há categorias equivalentes em idiomas diferentes, como `corrida`/`run`, `caminhada`/`walk`, `forca`/`strength` e `pedal`/`ride`. Elas precisam ser normalizadas antes de qualquer perfil comportamental.

---

## ⚠️ 6. Achados de qualidade que mudam a análise

### 6.1 Registros posteriores ao corte

Embora o corte oficial seja 30/09/2026, a auditoria encontrou:

- 119 cadastros posteriores ao corte, chegando até 04/04/2027;
- 122 posts de 120 usuários entre 01/10 e 07/10/2026;
- 273 relações de amizade entre 01/10 e 09/10/2026;
- 34 atividades entre 00:00 e 00:59 de 01/10/2026.

Os 34 treinos podem refletir conversão de fuso. Os demais registros mostram que filtrar pelo nome do arquivo ou confiar apenas na descrição do PDF não basta. Toda feature deve aplicar o corte no timestamp.

### 6.2 Categorias inconsistentes

Em `usuarios.csv`, o sistema operacional aparece como `android`, `Android`, `ios`, `iOS` e `IOS`. Em atividades, as modalidades misturam português e inglês. A preparação dos dados deve manter a coluna original e criar uma coluna normalizada auditável.

### 6.3 Valor monetário lido como texto

`pagamentos.csv` usa representação que fez o leitor automático inferir `valor` como texto. O pipeline deve converter explicitamente o separador decimal e falhar quando houver valor inválido, em vez de substituir silenciosamente.

### 6.4 Campo de relógio usa categoria explícita

`relogio_conectado` não usa nulo para ausência; usa a categoria `nenhum`. A distribuição é:

- nenhum: 40.159;
- Garmin: 13.403;
- Apple Watch: 11.386.

Uma checagem baseada apenas em `IS NOT NULL` classificaria incorretamente 100% das contas como conectadas a relógio.

### 6.5 Retrato não é histórico

`assinaturas.csv` representa o estado na exportação. A reconstrução de uma data anterior deve usar `eventos_assinatura.csv`. O arquivo de assinaturas serve para reconciliação, não para reescrever o passado.

---

## 📐 7. Contratos mínimos antes da modelagem

### 7.1 Coorte

Definir em código quais assinaturas compõem a população no corte e provar que o resultado reconcilia 14.753 pagantes, excluindo cortesias.

### 7.2 Label

Formalizar quais eventos contam como saída nos 60 dias após cada corte. Para 30/09, o horizonte termina em 29/11/2026; sem dados até essa data, não há rótulo final observado. Definir como serão tratados:

- renovação automática desligada;
- assinatura expirada;
- cancelamento web;
- falha de pagamento e período de carência;
- reembolso;
- chargeback.

### 7.3 Tempo

Converter timestamps para uma referência comum, preservar o valor original e testar eventos na virada do dia e do mês.

### 7.4 Privacidade

Usar identificadores pseudonimizados em amostras e nunca publicar e-mails ou textos individuais.

### 7.5 Evidência

Todo indicador deve trazer:

- fonte;
- consulta ou função que o gerou;
- população;
- período;
- regra de exclusão;
- data da execução.

---

## 🧭 8. Próxima etapa analítica

A ordem segura é:

1. executar auditoria reprodutível;
2. reconciliar população e label;
3. corrigir corte temporal e categorias;
4. produzir baseline descritivo;
5. testar hipóteses diagnósticas;
6. criar clusterização sem usar churn;
7. treinar baseline supervisionado com validação temporal;
8. integrar os modelos à estimativa de uplift e à avaliação de lucro.

O protocolo do experimento de agosto pode avançar em paralelo após definir população, desfecho e janela completa; ele não depende de um modelo de churn treinado.

O arquivo [`src/01_auditoria_data_room.py`](../src/01_auditoria_data_room.py) implementa o primeiro gate. O [Caderno de Hipóteses](./06_CADERNO_DE_HIPOTESES_ANALITICAS.md) organiza os testes seguintes.

👉 **Continue:** [Dicionário comentado](./05_DOSSIE_DICIONARIO_DE_DADOS_M2.md) · [Guia de reconstrução](./02_trilha_ciencia_de_dados_e_ml/01_SANEAMENTO_E_RECONSTRUCAO_HISTORICA.md).
