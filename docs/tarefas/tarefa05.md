# Tarefa 05 – Exercícios Básicos de Git (Branches e Pull Requests)

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
E-mail institucional: wender.araujo@aluno.impacta.edu.br
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code

---

1. ENTREGÁVEIS ANEXADOS

a) Link do Pull Request fechado (Merged) no GitHub:

- PR #1: https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est/pull/1
  (branch feat/melhoria-readme → main, status "Merged")

b) Print do histórico de commits da branch main no GitHub:

- Commit de merge exibido no histórico: "Merge pull request #1 from
  wenderaraujo-creator/feat/melhoria-readme" (9cb5d79)

c) Print do README.md atualizado:

- Seção "## Tecnologias Utilizadas" com as 5 ferramentas: Git & GitHub,
  VS Code, Node.js, OpenSpec e Xano.

---

2. CRITÉRIOS DE AVALIAÇÃO

[✅] Branch criada com nomenclatura correta (feat/...).
Confirmação: Branch 'feat/melhoria-readme' criada a partir da main.

[✅] Commit message segue o padrão.
Confirmação: Commit 'docs: adiciona seção de tecnologias no README'
(4bde5a9), no padrão Conventional Commits.

[✅] Alterações realizadas e commitadas apenas na branch secundária (não na main).
Confirmação: A seção "Tecnologias Utilizadas" foi adicionada e commitada
somente na branch 'feat/melhoria-readme' e integrada à main via Pull Request.

[✅] README.md foi alterado com a seção "Tecnologias Utilizadas" incluindo as 5 ferramentas.
Confirmação: Seção criada com Git & GitHub, VS Code, Node.js, OpenSpec e Xano.

[✅] Pull Request aberto no GitHub com título e descrição adequados.
Confirmação: PR #1 aberto comparando 'feat/melhoria-readme' com a 'main',
com título proveniente da mensagem de commit e descrição do escopo.

[✅] Pull Request foi mergeado com sucesso (status "Merged").
Confirmação: PR #1 mergeado; commit de merge 9cb5d79 na main
("Merge pull request #1 from wenderaraujo-creator/feat/melhoria-readme").

[✅] Branch local foi deletada após o merge (git branch -d feat/melhoria-readme).
Confirmação: branch local 'feat/melhoria-readme' deletada após o merge; a
branch remota e o Pull Request permanecem disponíveis no GitHub.

[✅] Branch main local foi atualizada após o merge (git pull origin main).
Confirmação: executados 'git checkout main' e 'git pull origin main' após o
merge; a main local está sincronizada com origin/main.

---

3. OBSERVAÇÕES TÉCNICAS

- Fluxo adotado: criar branch → alterar arquivo → git add → git commit →
  git push → abrir PR → merge na main. É o fluxo profissional com branches,
  Pull Requests e merge.
- A branch foi publicada com vínculo remoto (upstream) via
  'git push -u origin feat/melhoria-readme', permitindo que os envios
  seguintes usem apenas 'git push'.
- As mensagens de commit seguem o padrão Conventional Commits (docs:, feat:),
  mantendo o histórico do projeto consistente.
- O repositório registrou dois Pull Requests: o PR #1 (seção Tecnologias
  Utilizadas) e um PR #2 posterior de documentação da própria Tarefa 05;
  ambos constam como "Merged" na main.

---

Data de entrega: 6 de outubro de 2026
Aluno: Wender Araujo Santos

---
