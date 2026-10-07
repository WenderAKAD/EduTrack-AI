# Tasks

## 1. Assets do Design System

- [ ] 1.1 Abrir `flutterflow/tema-referencia.html` e verificar que os elementos da tela Dashboard estão agrupados por função (grupo do card de disciplina, grupo do card de tarefa, grupo da barra de navegação) — verificar no HTML que não há elemento solto fora de grupo
- [ ] 1.2 Conferir que os ícones em `assets/icons/` estão em **SVG** e têm contraparte no mockup `tema-referencia.html` — verificar que nenhum arquivo tem extensão `.png`, `.jpg` ou `.webp`
- [ ] 1.3 Exportar as imagens raster em PNG para `assets/images/` — verificar que a pasta existe e não está vazia sem motivo
- [x] 1.4 Renomear os arquivos exportados para `kebab-case` descritivo, com base na função e não na cor (ex: `add-task.svg`, e não `red-circle.svg`) — verificar com `ls assets/icons assets/images` que nenhum nome tem espaço, acento ou caractere maiúsculo
- [x] 1.5 Confirmar que cada SVG é recolorível, ou seja, sem `fill` fixo que impeça o FlutterFlow de aplicar a cor do Design System — abrir cada `.svg` em editor de texto e procurar por `fill="#`
- [x] 1.6 Escrever `assets/README.md` registrando a origem de cada asset (elemento do mockup `tema-referencia.html`), o formato e onde ele é usado no FlutterFlow — verificar que todo arquivo em `assets/icons/` e `assets/images/` aparece na tabela

## 2. Estrutura no repositório

- [x] 2.1 Criar a branch `style/assets-figma` a partir da `main` — verificar com `git branch --show-current`
- [x] 2.2 Garantir que `assets/icons/` e `assets/images/` existam e contenham `.gitkeep` — verificar com `git ls-files assets/` que as pastas aparecem no índice
- [x] 2.3 versionar os assets com `git add assets/` e um commit no formato `style: adiciona assets originais do Design System e estrutura de pastas` — verificar que nenhum `.png` ou `.svg` ficou de fora com `git status`

## 3. Páginas no FlutterFlow

- [ ] 3.1 Abrir o projeto EduTrack AI no FlutterFlow e criar a página `HomePage` com título visível — verificar na lista de páginas do projeto
- [ ] 3.2 Criar a página `SubjectsPage` com título visível e um `Container` de bordas arredondadas com pelo menos um `Text` dentro, seguindo o card do mockup — verificar que o container não está vazio
- [ ] 3.3 Criar a página `TasksPage` com título visível e uma `ListView` com pelo menos um item — verificar que a lista renderiza conteúdo
- [ ] 3.4 Adicionar o componente **NavBar** com três itens, um por página, e atribuir a action **Navigate to Page** de cada item para a sua própria página — verificar que nenhum item está sem action
- [ ] 3.5 Tornar o item da página atual visualmente distinto dos demais, com `#E10600` no tema claro e `#FF1E3C` no dark — verificar navegando entre as três páginas
- [ ] 3.6 Fazer upload dos assets de `assets/` em **Media Assets** — verificar que os arquivos aparecem na biblioteca do FlutterFlow
- [ ] 3.7 Verificar as três páginas nas duas larguras, celular e navegador — confirmar que a NavBar fica visível e que não há barra de rolagem horizontal
- [ ] 3.8 Confirmar que nenhuma das três páginas chama a API Group "Xano Backend" — verificar em cada página que a lista de API Calls está vazia

## 4. Registro e entrega

- [x] 4.1 Atualizar `flutterflow/REGISTRO-CONFIGURACAO.md` com a seção de navegação e a tabela de assets, seguindo o padrão de registro da Tarefa 07
- [ ] 4.2 Gerar o link de visualização do projeto no FlutterFlow pelo botão **Share**, ou registrar que ele não está disponível e usar screenshots no lugar
- [ ] 4.3 Capturar os prints de evidência: as 3 páginas no FlutterFlow, a NavBar e a pasta `assets/` no VS Code
- [x] 4.4 Documentar a Tarefa 09 no `README.md` com o mesmo padrão de 5 seções das tarefas anteriores, incluindo a seção "Próximo passo"
- [x] 4.5 Rodar `openspec validate add-figma-assets-and-navigation --strict` e confirmar que a change é válida
- [ ] 4.6 Arquivar a change com `openspec archive add-figma-assets-and-navigation --yes` e confirmar que `openspec/specs/design-assets/spec.md` e `openspec/specs/app-navigation/spec.md` foram gerados — verificar com `openspec validate --specs --strict`
- [x] 4.7 Abrir o Pull Request de `style/assets-figma` para `main`, mergear e registrar a URL no README — PR #6 (https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est/pull/6) e PR #5 da Tarefa 08

---

## 5. Estado de execução

A change está **parcialmente executada**. As tasks 3.1 a 3.8, 4.2, 4.3, 4.6 e 4.7
dependem do FlutterFlow, que não abre na máquina de desenvolvimento — o Chrome 154
bloqueia a GPU de 2015 (`WebGL: Disabled`) e o FlutterFlow não carrega no Core
`m-5Y31` de 0,90 GHz. A execução está planejada para Windows 11, com o roteiro em
`docs/guia-execucao-windows.md`.

### O Figma foi substituído pelo mockup (Opção A)

O enunciado pedia exportar do arquivo do Figma da Tarefa 06, mas esse arquivo
nunca existiu e nenhuma máquina disponível roda o Figma. A spec `design-assets`
foi revisada: todo asset agora provém do Design System da Tarefa 07, materializado
em `flutterflow/tema-referencia.html`, que passa a ser a fonte editável de
design. As tasks 3.1 a 3.8 continuam dependendo do FlutterFlow, mas nenhuma
depende mais do Figma.

### Divergência em relação ao enunciado

**O arquivo do Figma citado na tarefa 09 não existe.** A tarefa diz "abra o
arquivo do Figma que você duplicou na Tarefa 06"; a Tarefa 06 entregou um
arquivo de referências com quatro templates do Figma Community e não duplicou
nada. Existe um arquivo "EduTrack Orbit AI — Design System"
(`i6BKRzp9HGlhyubcz6xhJ1`), mas ele pertence a um projeto distinto e
abandonado — uma aplicação Python/Streamlit com histórico Git próprio — e não
foi usado, para não misturar dois projetos numa entrega.

Consequência: como não há de onde exportar, os nove ícones foram **sourced** do
Design System da Tarefa 07 e conferidos contra o mockup `tema-referencia.html`,
versionados como base de trabalho. `assets/README.md` registra a origem e a
decisão que substitui o Figma. As tasks 1.1 e 1.2 que citavam exportação foram
reescritas para verificação contra o mockup.

### Task 1.3 sem objeto

`assets/images/` permanece vazia. O Design System da Tarefa 07 é vetorial e não
contém fotografia, ilustração ou textura que rendam um PNG. Não foi gerado
placeholder para preencher a pasta — um rasterizado sem uso é escopo não pedido.
A task fica aberta até que o mockup permita avaliar se há algo a exportar.