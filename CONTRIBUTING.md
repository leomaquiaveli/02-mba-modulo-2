# Guia de contribuição

## Antes de começar

1. Leia o [README principal](./README.md).
2. Escolha uma tarefa em [`01_gerenciamento_de_tarefas/`](./01_gerenciamento_de_tarefas/).
3. Confirme a fonte oficial e a data de corte.
4. Abra uma branch curta e descritiva.

Exemplos:

```bash
git switch -c docs/aula-01
git switch -c feat/auditoria-coorte
git switch -c analysis/hipotese-preco
```

## O que pode entrar no Git

- Markdown e diagramas Mermaid;
- scripts e notebooks sem dados pessoais embutidos;
- schemas e contratos;
- testes;
- gráficos e tabelas agregadas;
- relatórios de auditoria sem registros individuais.

## O que não pode entrar

- CSVs e Parquet brutos;
- ZIPs dos heatmaps;
- e-mails, textos de clientes ou identificadores completos;
- credenciais, tokens e arquivos `.env`;
- resultados inventados ou ainda não executados.

## Padrão de análise

Toda entrega analítica deve declarar:

- pergunta de negócio;
- população e período;
- arquivos e colunas usados;
- tratamento de tempo, ausentes e categorias;
- método e baseline;
- métrica e incerteza;
- resultado;
- limitação;
- comando para reprodução.

## Commits

Prefira um commit por mudança coerente.

```text
docs(aula-01): integrar CREATE e CRISP-DM ao case Vitaliza
feat(auditoria): validar coorte ativa e registros pós-corte
analysis(churn): testar hipótese de reajuste do plano mensal
```

Evite mensagens como `update`, `ajustes`, `final` ou `coisas novas`.

## Pull request

A descrição deve responder:

1. O que mudou?
2. Por que mudou?
3. Como foi validado?
4. Que arquivos ou dados não foram incluídos?
5. Existe decisão pendente da equipe?

## Checklist

- [ ] Links locais verificados.
- [ ] Nenhum dado bruto entrou no diff.
- [ ] Nenhum segredo entrou no diff ou no remote.
- [ ] Datas e população estão explícitas.
- [ ] Números têm fonte ou consulta.
- [ ] Código foi executado no ambiente documentado.
- [ ] Limitações foram registradas.
