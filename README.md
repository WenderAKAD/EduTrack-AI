# EduTrack AI

Assistente educacional para acompanhar **disciplinas**, **tarefas** e
**progresso acadêmico**. O backend fica no **Xano**, o frontend em
**Flutter/FlutterFlow** e o planejamento com **OpenSpec** (Spec-Driven
Development).

| Informação | Valor |
|---|---|
| Disciplina | Innovation Lab: Desenvolvimento Avançado No/Low Code |
| Aluno | Wender Araújo Santos |
| E-mail institucional | wender.araujo@aluno.impacta.edu.br |
| Instituição | Faculdade Impacta |
| Repositório | [EduTrack-IA-Wender-Est](https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est) |
| Espelho (portfólio) | [WenderAKAD/EduTrack-AI](https://github.com/WenderAKAD/EduTrack-AI) |

## Tecnologias

- Git & GitHub
- VS Code
- Node.js / npm
- OpenSpec
- Xano / XanoScript
- Antigravity (IA)
- Flutter

## Tarefas

Progresso: **11 de 16 tarefas** concluídas (Tarefas 01 a 11). O detalhe de cada
tarefa — entregáveis, critérios e observações — fica em `docs/tarefas/`.

| # | Tarefa | Status | PR | Detalhe |
|---|--------|--------|----|---------|
| 01 | Primeiro Contato com Git e GitHub | Concluída | — | [tarefa01](docs/tarefas/tarefa01.md) |
| 02 | VS Code, Node.js e Configuração de IA | Concluída | — | [tarefa02](docs/tarefas/tarefa02.md) |
| 03 | Instalação e Inicialização do OpenSpec | Concluída | — | [tarefa03](docs/tarefas/tarefa03.md) |
| 04 | Primeiro Pull/Push com XanoScript | Concluída | — | [tarefa04](docs/tarefas/tarefa04.md) |
| 05 | Exercícios Básicos de Git (Branches e PRs) | Concluída | #1, #2 | [tarefa05](docs/tarefas/tarefa05.md) |
| 06 | Exploração de Templates Gratuitos | Concluída | #3 | [tarefa06](docs/tarefas/tarefa06.md) |
| 07 | Configuração Inicial no FlutterFlow | Concluída | #4 | [tarefa07](docs/tarefas/tarefa07.md) |
| 08 | Uso do OpenSpec para Planejar Mudanças | Concluída | #5 | [tarefa08](docs/tarefas/tarefa08.md) |
| 09 | Navegação e Assets do Design System | Parcial | #6, #7 | [tarefa09](docs/tarefas/tarefa09.md) |
| 10 | Configuração Avançada do AGENTS.md | Concluída | #8 | [tarefa10](docs/tarefas/tarefa10.md) |
| 11 | Adicionar Tabela Tarefas via XanoScript | Concluída | #9 | [tarefa11](docs/tarefas/tarefa11.md) |

## Estrutura do repositório

- `AGENTS.md` — regras do projeto para as IAs.
- `openspec/` — especificações e mudanças planejadas (Spec-Driven Development).
- `apis/`, `tables/`, `functions/`, `addons/` — backend Xano (XanoScript).
- `flutterflow/`, `lib/`, `assets/` — frontend.
- `docs/` — documentação; `docs/tarefas/` (detalhe por tarefa) e `docs/evidencias/`.

## Observações de transparência

- **Tarefa 02** — a IA foi configurada via **Antigravity** (conta institucional),
  pois o login da extensão Gemini Code Assist não concluiu no VS Code.
- **Tarefa 07** — a importação automática do Figma não foi usada; os componentes
  foram montados manualmente a partir do mockup de referência.
- **Tarefa 09** — o FlutterFlow não foi construído por limitação de hardware
  (CPU/GPU da máquina). As páginas foram montadas em **Flutter local** (PR #7) e
  a fonte de design passou a ser o mockup, não o Figma. Aguarda confirmação do
  professor.
- Os **endpoints de API** de `subjects` e `user` no Xano ficam para a próxima
  etapa do módulo.

## Pendências Técnicas

Itens conhecidos e adiados de propósito. O detalhe de cada um está em
[`docs/pendencias-tecnicas.md`](docs/pendencias-tecnicas.md).

1. Limpeza dos objetos de template do workspace Xano (194 objetos que não são do
   projeto).
2. Cache local do Xano CLI desatualizado (`.xano/branches/v1/objects.json`).
3. `addons/109599_user.xs` corrompido — origem da falsa impressão de que a
   tabela `user` já existia no Xano.
4. Extensão `xano.xanoscript` descontinuada — o fluxo atual usa o Xano CLI.
5. `tables/user.xs` não é byte-idêntico ao servidor (campo `user_id`).

---

Aluno: Wender Araujo Santos · Faculdade Impacta · 2026
