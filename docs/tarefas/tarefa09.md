# Tarefa 09 – Integração Figma → FlutterFlow

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code
Módulo: 1 – Introdução ao Spec-Driven Development

Estrutura de navegação do frontend: três páginas, barra de navegação inferior e
os assets que as sustentam.

> **Nota sobre a ordem das tarefas.** A seção acima foi escrita antes de o
> enunciado da Tarefa 09 ser confirmado. O enunciado recebido é sobre Figma e
> FlutterFlow, não sobre endpoints de API; os endpoints de `subjects` e `user`
> ficam para a tarefa seguinte.

---

1. O QUE FOI FEITO

- Change `add-figma-assets-and-navigation` criada com os quatro artifacts do
  schema `spec-driven`: `proposal.md`, `specs/design-assets/spec.md`,
  `specs/app-navigation/spec.md`, `design.md` e `tasks.md`. São 11 requirements
  e 29 scenarios, cobrindo origem dos assets, geometria dos ícones, estrutura
  das três páginas, comportamento da NavBar e ausência de binding com o Xano.
- Nove ícones SVG criados em `assets/icons/` — `home`, `subjects`, `tasks`,
  `add-subject`, `add-task`, `check`, `clock`, `empty-subjects`, `empty-tasks`.
  Todos em grade 24×24 com `fill="none"`, `stroke="currentColor"` e
  `stroke-width="2"`, o que permite recolorir entre os dois temas da Tarefa 07
  sem duplicar arquivo.
- `assets/README.md` criado com a tabela de origem de cada ícone, a cor por tema
  e a fonte de design (mockup `tema-referencia.html`, sem Figma).
- `flutterflow/REGISTRO-CONFIGURACAO.md` recebeu a seção 6, que especifica os
  nomes exatos das três páginas, os três itens da NavBar com suas actions
  Navigate to Page e a regra de conferência nas duas larguras.
- `docs/guia-execucao-windows.md` criado com o roteiro completo de execução,
  incluindo o comando que materializa os nove SVG no Windows sem depender de
  arrastar arquivos ou sincronização de área de transferência.

---

2. ENTREGÁVEIS

- [ ] Link do projeto FlutterFlow com as três páginas, ou prints das páginas.
      *Pendente — depende do acesso à máquina Windows.*
- [ ] Print da pasta `assets/` no VS Code.
      *Pendente — depende do acesso à máquina Windows.*
- [x] Link do Pull Request da branch `style/assets-figma`.
      PR #6 merged — https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est/pull/6
- [x] Registro de configuração do frontend atualizado com a navegação.
      Arquivo: flutterflow/REGISTRO-CONFIGURACAO.md (seção 6)
- [x] Registro de origem dos assets.
      Arquivo: assets/README.md
- [x] Roteiro de execução documentado.
      Arquivo: docs/guia-execucao-windows.md

---

3. CRITÉRIOS DE AVALIAÇÃO

- [ ] Pelo menos 3 páginas criadas com título visível.
      Especificado, ainda não construído. Páginas: `HomePage`, `SubjectsPage`,
      `TasksPage`.
- [ ] Barra de navegação inferior presente, com pelo menos 3 itens, navigating
      para as páginas correspondentes.
      Especificado, ainda não construído. Três itens com action Navigate to
      Page.
- [ ] Assets provenientes do Design System e versionados.
      **Parcial.** Os nove SVGs estão versionados em `assets/icons/`, sourced do
      Design System da Tarefa 07 e conferidos contra o mockup — ver item 4. Não
      há exportação de Figma: a spec foi revisada (Opção A).
- [ ] Assets referenciados no projeto FlutterFlow.
      *Pendente.*
- [ ] Pull Request aberto com o histórico de commits.
      *Pendente.*
- [ ] README do repositório atualizado com o progresso.
      Este arquivo.

---

4. OBSERVAÇÕES TÉCNICAS

- **O Figma foi substituído pelo mockup como fonte de design.** O enunciado
  pedia exportar do arquivo do Figma "duplicado na Tarefa 06", mas esse arquivo
  nunca existiu e nenhuma máquina disponível roda o editor. A spec da change
  `design-assets` foi revisada: todo asset agora provém do Design System da
  Tarefa 07, materializado em `flutterflow/tema-referencia.html`, que é a nova
  fonte editável de referência. Nenhuma task da Tarefa 09 depende mais do Figma;
  só o FlutterFlow segue pendente, por bloqueio de hardware.

- **O arquivo do Figma citado no enunciado não existe.** A tarefa diz "abra o
  arquivo do Figma que você duplicou na Tarefa 06", mas a Tarefa 06 entregou um
  arquivo de referências com quatro templates do Figma Community e não duplicou
  arquivo nenhum. Não há o que abrir.

- **Existe um arquivo "EduTrack Orbit AI — Design System", e ele é de outro
  projeto.** O `file_key` `i6BKRzp9HGlhyubcz6xhJ1` aparece no histórico do
  navegador. Ele pertence a uma aplicação Python/Streamlit abandonada, com
  histórico Git próprio em `Documents/2 Semestre/Innovation Lab/EduTrack Orbit
  IA/`, stack diferente (Streamlit, ReportLab, Pandas) e nenhum vestígio de
  "Orbit" neste repositório. Importar dali misturaria dois projetos numa entrega
  só, então não foi usado.

- **Os nove ícones foram sourced do Design System, não exportados.** Como não há
  arquivo do Figma de onde exportar, os ícones foram construídos a partir do
  Design System já versionado na Tarefa 07 e conferidos contra o mockup
  `tema-referencia.html`. `assets/README.md` declara a origem por ícone e a
  decisão. Apresentá-los como exportação do Figma seria falso.

- **O hardware de desenvolvimento não abre o FlutterFlow.** O MacBook Pro 2016
  (Intel Core `m-5Y31` a 0,90 GHz, Intel HD Graphics 5300) não carrega o IDE —
  o Chrome 154 reporta `WebGL: Disabled` por causa da GPU de 2015 em blocklist, e
  o FlutterFlow, ainda que não use WebGL, não roda nessa CPU. A execução foi
  planejada para uma máquina Windows 11 por acesso remoto, e o roteiro está
  versionado. O Figma, que antes também bloqueava, saiu de cena por decisão de
  spec.

- **Nenhum dado é buscado da API.** As três páginas declaram que não chamam
  nenhum endpoint e exibem conteúdo estático de exemplo. Os endpoints de
  `subjects` e `user` ainda não existem, e ligar as telas a eles agora produziria
  erro de runtime. Isso está fixado como requirement na spec da change.

- **Nove ícones, nenhum a mais.** Ícones de functionality que o app ainda não
  tem — login, notificações, configurações, perfil — ficam de fora de propósito.
  A entrega é a navegação entre três telas, e um ícone sem tela correspondente
  é escopo não pedido.

---

5. PRÓXIMO PASSO

Executar `docs/guia-execucao-windows.md` na máquina Windows: conferir o mockup
`tema-referencia.html` como referência, montar as três páginas e a NavBar no
FlutterFlow usando os ícones já versionados em `assets/icons/`, tirar os prints
e abrir o Pull Request.

---

Data de entrega: 6 de outubro de 2026
Aluno: Wender Araujo Santos

---
