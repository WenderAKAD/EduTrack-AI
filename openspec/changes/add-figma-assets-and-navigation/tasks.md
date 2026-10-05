# Tasks

## 1. Assets do Figma

- [ ] 1.1 Abrir o arquivo do Figma do EduTrack AI e agrupar os elementos da tela Dashboard por função (grupo do card de disciplina, grupo do card de tarefa, grupo da barra de navegação) — verificar no canvas que não há elemento solto fora de grupo
- [ ] 1.2 Exportar os ícones em **SVG** — verificar que nenhum arquivo em `assets/icons/` tem extensão `.png`, `.jpg` ou `.webp`
- [ ] 1.3 Exportar as imagens raster em PNG para `assets/images/` — verificar que a pasta existe e não está vazia sem motivo
- [ ] 1.4 Renomear os arquivos exportados para `kebab-case` descritivo, com base na função e não na cor (ex: `add-task.svg`, e não `red-circle.svg`) — verificar com `ls assets/icons assets/images` que nenhum nome tem espaço, acento ou caractere maiúsculo
- [ ] 1.5 Confirmar que cada SVG é recolorível, ou seja, sem `fill` fixo que impeça o FlutterFlow de aplicar a cor do Design System — abrir cada `.svg` em editor de texto e procurar por `fill="#`
- [ ] 1.6 Escrever `assets/README.md` registrando a origem de cada asset (elemento do Figma), o formato e onde ele é usado no FlutterFlow — verificar que todo arquivo em `assets/icons/` e `assets/images/` aparece na tabela

## 2. Estrutura no repositório

- [ ] 2.1 Criar a branch `style/assets-figma` a partir da `main` — verificar com `git branch --show-current`
- [ ] 2.2 Garantir que `assets/icons/` e `assets/images/` existam e contenham `.gitkeep` — verificar com `git ls-files assets/` que as pastas aparecem no índice
- [ ] 2.3 versionar os assets com `git add assets/` e um commit no formato `style: adiciona assets originais do Figma e estrutura de pastas` — verificar que nenhum `.png` ou `.svg` ficou de fora com `git status`

## 3. Páginas no FlutterFlow

- [ ] 3.1 Abrir o projeto EduTrack AI no FlutterFlow e criar a página `HomePage` com título visível — verificar na lista de páginas do projeto
- [ ] 3.2 Criar a página `SubjectsPage` com título visível e um `Container` de bordas arredondadas com pelo menos um `Text` dentro, seguindo o card do Figma — verificar que o container não está vazio
- [ ] 3.3 Criar a página `TasksPage` com título visível e uma `ListView` com pelo menos um item — verificar que a lista renderiza conteúdo
- [ ] 3.4 Adicionar o componente **NavBar** com três itens, um por página, e atribuir a action **Navigate to Page** de cada item para a sua própria página — verificar que nenhum item está sem action
- [ ] 3.5 Tornar o item da página atual visualmente distinto dos demais, com `#E10600` no tema claro e `#FF1E3C` no dark — verificar navegando entre as três páginas
- [ ] 3.6 Fazer upload dos assets exportados do Figma em **Media Assets** — verificar que os arquivos aparecem na biblioteca do FlutterFlow
- [ ] 3.7 Verificar as três páginas nas duas larguras, celular e navegador — confirmar que a NavBar fica visível e que não há barra de rolagem horizontal
- [ ] 3.8 Confirmar que nenhuma das três páginas chama a API Group "Xano Backend" — verificar em cada página que a lista de API Calls está vazia

## 4. Registro e entrega

- [ ] 4.1 Atualizar `flutterflow/REGISTRO-CONFIGURACAO.md` com a seção de navegação e a tabela de assets, seguindo o padrão de registro da Tarefa 07
- [ ] 4.2 Gerar o link de visualização do projeto no FlutterFlow pelo botão **Share**, ou registrar que ele não está disponível e usar screenshots no lugar
- [ ] 4.3 Capturar os prints de evidência: as 3 páginas no FlutterFlow, a NavBar e a pasta `assets/` no VS Code
- [ ] 4.4 Documentar a Tarefa 09 no `README.md` com o mesmo padrão de 5 seções das tarefas anteriores, incluindo a seção "Próximo passo"
- [ ] 4.5 Rodar `openspec validate add-figma-assets-and-navigation --strict` e confirmar que a change é válida
- [ ] 4.6 Arquivar a change com `openspec archive add-figma-assets-and-navigation --yes` e confirmar que `openspec/specs/design-assets/spec.md` e `openspec/specs/app-navigation/spec.md` foram gerados — verificar com `openspec validate --specs --strict`
- [ ] 4.7 Abrir o Pull Request de `style/assets-figma` para `main` e registrar a URL no README