# EduTrack AI

Projeto da disciplina Innovation Lab – Faculdade Impacta  
Aluno: Wender Araújo Santos
Data Início: 2026

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
