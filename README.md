# EduTrack AI

Projeto da disciplina Innovation Lab – Faculdade Impacta  
Aluno: Wender Araújo Santos
Data Início: 2026

## Tecnologias Utilizadas

- Git & GitHub
- VS Code
- Node.js
- OpenSpec
- Xano

Tarefa 02 – Instalação do VS Code, Node.js e Configuração de IA

Aluno: Wender Araujo Santos
E-mail institucional: wender.araujo@aluno.impacta.edu.br
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code

---

1. ENTREGÁVEIS ANEXADOS

a) Print do VS Code com a pasta do projeto aberta no Explorer:

- Pasta: EduTrack-IA-Wender-Est
- Arquivo visível: README.md

b) Print do terminal interno do VS Code mostrando:

- node --version → v22.23.3
- npm --version → 10.9.9

---

2. CRITÉRIOS DE AVALIAÇÃO

[✅] VS Code instalado e abrindo a pasta do projeto.
Confirmação: Pasta "EduTrack-IA-Wender-Est" (repositório clonado
na Tarefa 01) está aberta no VS Code com o README.md visível no
painel Explorer.

[✅] Node.js (LTS) instalado e versão verificada no terminal.
Confirmação: node v22.23.3 / npm 10.9.9 (versão LTS).

[⚠️] Extensão Gemini Code Assist instalada e autenticada com e-mail
@aluno.faculdadeimpacta.edu.br.
Observação: O login direto da extensão Gemini Code Assist no VS
Code não concluiu a autenticação no meu ambiente (macOS Ventura
13.7.8, Intel, Homebrew com conflitos recorrentes).

    Conforme orientação do professor, a IA foi configurada e
    autenticada via **Antigravity** usando a conta institucional
    wender.araujo@aluno.impacta.edu.br. O chat do Antigravity está
    ativo, logado e respondendo comandos, conforme evidenciado nos
    prints anexos.

[✅] Extensão XanoScript instalada.
Confirmação: XanoScript v0.5.12 instalada no VS Code.

---

3. OBSERVAÇÕES TÉCNICAS

- Ambiente: MacBook Retina 12" Early 2015, macOS Ventura 13.7.8,
  Intel Core M, 8 GB RAM.
- O Homebrew apresenta status "Tier 3" neste sistema, com problemas
  recorrentes de lock em /usr/local/Cellar/pkgconf. Por isso, o
  Node.js foi instalado via instalador oficial .pkg do site
  nodejs.org (versão LTS).
- A autenticação da IA foi feita via Antigravity conforme orientação
  do professor, pois o login direto no VS Code não concluiu.

---

4. ENTREGÁVEIS VISUAIS

1. Print: VS Code com pasta EduTrack-IA-Wender-Est no Explorer
   - terminal mostrando node --version v22.23.3.

1. Print: Extensão XanoScript instalada no VS Code.

1. Print: Chat do Antigravity respondendo (evidência de IA
   autenticada).

---

---

Tarefa 03 – Instalação e Inicialização do OpenSpec

Aluno: Wender Araujo Santos
E-mail institucional: wender.araujo@aluno.impacta.edu.br
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code

---

1. ENTREGÁVEIS ANEXADOS

a) Print do terminal interno do VS Code mostrando:

- openspec --version → 1.13.2

b) Print do Explorer do VS Code mostrando a estrutura criada:

- Pasta openspec/ contendo: project.md, AGENTS.md, config.yaml, specs/ e changes/
- Arquivo AGENTS.md na raiz do projeto

c) Print do histórico de commits no GitHub mostrando:

- Commit "feat: inicialização do OpenSpec no projeto"

---

2. CRITÉRIOS DE AVALIAÇÃO

[✅] CLI OpenSpec instalada e versão verificada.
Confirmação: OpenSpec CLI v1.13.2 instalada globalmente e vinculada em /usr/local/bin.

[✅] Comando openspec init executado com sucesso (estrutura criada).
Confirmação: Estrutura padrão criada (openspec/ com project.md, AGENTS.md, config.yaml,
pastas specs/ e changes/archive/ com .gitkeep, e AGENTS.md na raiz).

[✅] Integração com assistente de IA configurada.
Confirmação: OpenSpec configurado com suporte ao Antigravity (.agents/workflows/)
e mantendo stubs compatíveis com Gemini CLI/Code Assist (.gemini/).

[✅] Mudanças commitadas e enviadas ao GitHub.
Confirmação: Commit realizado com mensagem padronizada e publicado no repositório.

---

3. OBSERVAÇÕES TÉCNICAS

- A instalação global via npm apresentou erro de permissão (EACCES) em /usr/local/lib/node_modules.
- Como boa prática recomendada pelo npm, o prefixo global foi configurado em ~/.npm-global e criado um symlink em /usr/local/bin/openspec para reconhecimento imediato no terminal do sistema.
- A ferramenta foi inicializada suportando os fluxos nativos do Antigravity em conjunto com as especificações exigidas na rubrica da disciplina.

---

Data de entrega: 28 de setembro de 2026
Aluno: Wender Araujo Santos

---

Tarefa 04 – Primeiro Pull/Push com XanoScript

Aluno: Wender Araujo Santos
E-mail institucional: wender.araujo@aluno.impacta.edu.br
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code

---

1. ENTREGÁVEIS ANEXADOS

a) Print do VS Code com os arquivos .xs baixados:

- Explorer exibindo a árvore de arquivos baixados (apis, functions, addons)
- Arquivo 3823228_auth_login_POST.xs aberto exibindo comentário de teste

b) Print do terminal interno do VS Code mostrando:

- git push origin main concluído com sucesso

c) Link do repositório GitHub atualizado:

- https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est

---

2. CRITÉRIOS DE AVALIAÇÃO

[✅] Workspace Xano criado e Token gerado.
Confirmação: Conexão autenticada via extensão XanoScript no VS Code.

[✅] Conexão bem-sucedida via extensão XanoScript no VS Code.
Confirmação: Login no workspace e branch 'v1 Live branch' reconhecida.

[✅] Arquivos .xs visíveis no repositório local.
Confirmação: Executado 'Pull latest changes from Xano' trazendo os grupos
de API, funções e tabelas para o projeto.

[✅] Push e sincronização com o Xano.
Confirmação: Comentário inserido em arquivo .xs e sincronizado via 'Push Stage Changes'.

[✅] Commit e Push realizados no GitHub incluindo a pasta do Xano.
Confirmação: Commit 'feat: conexão com Xano e pull inicial do XanoScript'
publicado na branch main com 196 arquivos versionados.

---

Data de entrega: 28 de setembro de 2026
Aluno: Wender Araujo Santos

---

Tarefa 05 – Exercícios Básicos de Git

Aluno: Wender Araujo Santos
E-mail institucional: wender.araujo@aluno.impacta.edu.br
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code

---

1. ENTREGÁVEIS ANEXADOS

a) Print do terminal interno do VS Code mostrando o fluxo completo de Git:

- Criação da branch de trabalho: git switch -c feat/melhoria-readme
- Commit das alterações no README.md
- Publicação da branch com vínculo remoto:
  git push -u origin feat/melhoria-readme
- Confirmação do rastreamento: git branch -vv
  → feat/melhoria-readme [origin/feat/melhoria-readme]

b) Print da página do Pull Request no GitHub:

- PR comparando a branch feat/melhoria-readme com a main
- Aba "Files changed" exibindo o diff do README.md

c) Print do Pull Request já integrado:

- PR com o selo "Merged" e o commit de merge publicado na main

d) Link do repositório GitHub:

- https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est

---

2. CRITÉRIOS DE AVALIAÇÃO

[✅] Branch criada e publicada no repositório remoto.
Confirmação: Branch 'feat/melhoria-readme' enviada ao GitHub e configurada
para rastrear a branch remota (upstream) via 'git push -u'.

[✅] Pull Request aberto com as mudanças descritas.
Confirmação: PR aberto comparando 'feat/melhoria-readme' com a 'main',
com o diff do README.md visível na aba "Files changed".

[✅] Pull Request mesclado (merge) na branch principal.
Confirmação: Merge realizado na 'main' através do commit de merge do PR,
integrando as alterações e preservando o histórico das branches.

[✅] Histórico de commits padronizado.
Confirmação: Mensagens no padrão Conventional Commits (docs:, feat:),
facilitando a leitura do histórico do projeto.

---

3. OBSERVAÇÕES TÉCNICAS

- Fluxo adotado: criar branch → alterar arquivo → git add → git commit →
  git push → abrir PR → merge na main. É o fluxo profissional com
  branches, Pull Requests e merge.
- O vínculo entre a branch local e a remota (upstream) foi configurado com
  'git push -u origin <branch>', permitindo que os envios seguintes usem
  apenas 'git push'.
- As mensagens de commit seguem o padrão Conventional Commits (docs:, feat:),
  mantendo o histórico do projeto consistente.
- Antes de cada envio, o diff foi revisado com 'git diff' e o estado com
  'git status', evitando commitar arquivos indevidos (ex.: .DS_Store, já
  ignorado pelo .gitignore).

---

Data de entrega: 28 de setembro de 2026
Aluno: Wender Araujo Santos
