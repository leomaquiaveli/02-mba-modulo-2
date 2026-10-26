# 🛠️ Guia de Contribuição & Boas Práticas de Commit

> **Módulo 2:** IA e Dados para Negócios — Case Vitaliza  
> **Equipe:** Projetos MBA Inteli  
> **Foco deste documento:** Colaboração com e sem terminal

[🔰 Comece por Aqui](../README.md) / [Navegação para iniciantes](./00_COMO_NAVEGAR_NO_GITHUB.md) / Contribuição

🎯 **Objetivo:** permitir que cada pessoa proponha mudanças claras, revisáveis e fáceis de integrar. Isso vale para uma correção de texto, uma hipótese de negócio ou um novo script.

---

## 📂 1. Escolha o lugar da contribuição

| Tipo de contribuição | Destino |
| :--- | :--- |
| Explicação para orientar o grupo | guia correspondente em `00_comece_por_aqui/` |
| Hipótese ou plano de teste | [caderno analítico](../06_CADERNO_DE_HIPOTESES_ANALITICAS.md) |
| Rascunho ou nota pessoal | [espaço de membros](../../membros/00_geral/README.md) |
| Código de preparação ou análise | `src/`, com orientação de reprodução |
| Resultado pronto para entrega | artefato de negócios ou tecnologia, após revisão |
| Divisão e acompanhamento de tarefas | [matriz de execução](../../01_gerenciamento_de_tarefas/MATRIZ_DE_TAREFAS_E_ESPECIFICACOES.md) |

Combine a tarefa com a equipe para evitar duas pessoas alterando a mesma seção ao mesmo tempo.

---

## 📝 2. Prepare uma mudança que outra pessoa consiga revisar

Antes de enviar, registre:

- **Problema:** o que faltava ou estava incorreto?
- **Mudança:** que conteúdo, regra ou resultado foi incluído?
- **Evidência:** qual fonte ou execução sustenta a alteração?
- **Validação:** como a mudança foi conferida?
- **Limitação:** o que ainda depende de análise ou decisão?

Para números e gráficos, acrescente população, período, fonte e método. Se o resultado não foi calculado, escreva que é uma hipótese ou exemplo ilustrativo.

---

## 🌐 3. Fluxo pelo navegador

1. Abra o documento e use a opção de edição disponível para sua conta.
2. Faça uma alteração com escopo claro e confira a prévia de formatação.
3. Ao registrar a mudança, dê preferência a uma **nova branch** para permitir revisão.
4. Crie a proposta de alteração, ou **pull request**, descrevendo problema, mudança e validação.
5. Peça a revisão conforme a organização do grupo e incorpore os ajustes combinados.

Se sua conta não tiver permissão de escrita, as opções podem envolver uma cópia do repositório, chamada fork. Confirme o fluxo usado pela equipe antes de trabalhar em uma cópia que ninguém acompanha.

Para adicionar arquivos, use o envio de arquivos do repositório na pasta adequada e siga o mesmo processo de proposta e revisão. Revise o conteúdo do arquivo antes de enviá-lo; um notebook pode conter dados nas células de saída.

---

## 💻 4. Fluxo pelo terminal

Exemplo para um repositório **já publicado**, com `origin` configurado e branch principal chamada `main`. O repositório local ainda depende dessa configuração; não execute o exemplo sem conferir sua situação.

```bash
# Confira a branch e as mudanças locais antes de atualizar.
git status
git remote -v

# Com a árvore de trabalho limpa, atualize a principal.
git switch main
git pull --ff-only origin main

# Abra uma branch específica para a contribuição.
git switch -c docs/hipoteses-engajamento

# Depois de editar, confira e adicione apenas os arquivos necessários.
git diff --check
git diff -- 00_comece_por_aqui/06_CADERNO_DE_HIPOTESES_ANALITICAS.md
git add 00_comece_por_aqui/06_CADERNO_DE_HIPOTESES_ANALITICAS.md
git commit -m "docs: detalha teste da hipotese de engajamento"
git push -u origin docs/hipoteses-engajamento
```

Depois, abra um pull request para revisão. Se houver mudanças locais pendentes, resolva sua organização antes de trocar de branch; não descarte trabalho para seguir o exemplo.

---

## 🏷️ 5. Escreva mensagens de commit úteis

| Tipo | Exemplo |
| :--- | :--- |
| Documentação | `docs: esclarece denominador do churn mensal` |
| Funcionalidade | `feat(dados): reconstrói estado da assinatura por corte` |
| Correção | `fix(dados): interpreta categoria nenhum no campo de relógio` |

Uma mudança deve reunir arquivos que pertencem ao mesmo objetivo. Mensagens como “ajuste final” ou “update” dificultam entender o histórico.

---

## 🔒 6. Confira o conteúdo que vai compartilhar

Mantenha arquivos brutos, identificadores individuais, e-mails, textos pessoais e chaves de API fora da publicação. O `.gitignore` ajuda no fluxo local, mas não substitui a revisão de arquivos enviados pelo navegador nem remove arquivos já rastreados.

Não coloque dados individuais em notas, capturas, exemplos ou saídas de notebooks. Para ilustrar uma explicação, use um exemplo explicitamente fictício ou um agregado que não exponha registros.

---

## ✅ 7. Checklist de revisão

- [ ] A contribuição está na pasta correspondente e vinculada à tarefa.
- [ ] Links, títulos e tabelas foram conferidos na prévia.
- [ ] Fonte, população e período acompanham os números.
- [ ] Hipótese e resultado estão diferenciados.
- [ ] Dados brutos e credenciais não fazem parte da proposta.
- [ ] Outra pessoa consegue explicar o que mudou e como foi validado.

📚 **Referência do grupo:** [CONTRIBUTING.md](../../CONTRIBUTING.md).

↩️ **Voltar:** [🗺️ Mapa das Trilhas](../02_MAPA_DAS_TRILHAS.md).
