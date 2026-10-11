# Tarefa 04 – Primeiro Pull/Push com XanoScript

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
E-mail institucional: wender.araujo@aluno.impacta.edu.br
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code

---

1. ENTREGÁVEIS ANEXADOS

a) Print do VS Code com os arquivos .xs baixados:

- Explorer exibindo a árvore de arquivos baixados (apis, functions, addons, agents, tools)
- Arquivo 3823228_auth_login_POST.xs aberto exibindo comentário de teste

b) Print do terminal interno do VS Code mostrando:

- git push origin main concluído com sucesso

c) Link do repositório GitHub atualizado:

- https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est

---

2. CRITÉRIOS DE AVALIAÇÃO

[✅] Workspace Xano criado e Token gerado.
Confirmação: Workspace 'edutrack-ai' criado no Xano e Access Token 'VS Code'
gerado (Metadata API & MCP Server) com escopos de Database, API Groups,
Functions e Content.

[✅] Conexão bem-sucedida via extensão XanoScript no VS Code.
Confirmação: Login via 'XanoScript: Login to Xano' e workspace selecionado
com 'XanoScript: Select workspace'; branch 'v1 Live branch' reconhecida.

[✅] Arquivos .xs visíveis no repositório local.
Confirmação: 'XanoScript: Pull latest changes from Xano' trouxe as pastas
apis/ (186 .xs), functions/ (5), addons/ (1), agents/ (1) e tools/ (1),
além da configuração oculta em .xano/.

[✅] Commit e Push realizados no GitHub incluindo a pasta do Xano.
Confirmação: Commit 'feat: conexão com Xano e pull inicial do XanoScript'
(29e673a) publicado na branch main, totalizando 196 arquivos versionados.

---

3. OBSERVAÇÕES TÉCNICAS

- Para validar o fluxo nos dois sentidos (pull e push), foi adicionado o
  comentário "// Meu primeiro comentário via VS Code" no topo de
  apis/authentication/3823228_auth_login_POST.xs e enviado ao Xano com
  'XanoScript: Push Stage Changes to Xano'.
- Conforme a etapa 4.1 da tarefa, não há tabelas padrão versionadas: a pasta
  tables/ está vazia e não aparece no GitHub, pois o Git não rastreia pastas
  vazias. A tabela de autenticação padrão (user) está representada como
  addon em addons/109599_user.xs.
- A pasta oculta .xano/ armazena a configuração da conexão
  (.xano/config.json e .xano/branches/v1/objects.json) e foi versionada
  junto com o projeto.

---

Data de entrega: 6 de outubro de 2026
Aluno: Wender Araujo Santos

---
