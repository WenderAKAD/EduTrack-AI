# Assets Visuais — EduTrack AI

Registro de origem e uso dos assets da interface. Criado na Tarefa 09.

| Campo | Valor |
|---|---|
| **Tarefa** | 09 – Integração Figma → FlutterFlow |
| **Branch** | `style/assets-figma` |
| **Origem** | Design System da Tarefa 07 — ver [`../flutterflow/REGISTRO-CONFIGURACAO.md`](../flutterflow/REGISTRO-CONFIGURACAO.md) |
| **Formato** | SVG, viewBox `0 0 24 24` |
| **Traçado** | `fill="none"`, `stroke="currentColor"`, `stroke-width="2"` |

---

## 1. Ícones

Todos os ícones usam a mesma geometria de traçado (`stroke-width="2"`, pontas e
juntas arredondadas) e a mesma grade de 24×24, de modo que leiam como um conjunto
único na barra de navegação.

| Arquivo | Uso na interface | `node-id` no Figma |
|---|---|---|
| [`icons/home.svg`](icons/home.svg) | Item 1 da NavBar — Home | *pendente* |
| [`icons/subjects.svg`](icons/subjects.svg) | Item 2 da NavBar — Disciplinas | *pendente* |
| [`icons/tasks.svg`](icons/tasks.svg) | Item 3 da NavBar — Tarefas | *pendente* |
| [`icons/add-subject.svg`](icons/add-subject.svg) | Botão de adicionar disciplina | *pendente* |
| [`icons/add-task.svg`](icons/add-task.svg) | Botão de adicionar tarefa | *pendente* |
| [`icons/check.svg`](icons/check.svg) | Tarefa concluída | *pendente* |
| [`icons/clock.svg`](icons/clock.svg) | Tarefa pendente ou atrasada | *pendente* |
| [`icons/empty-subjects.svg`](icons/empty-subjects.svg) | Estado vazio da lista de disciplinas | *pendente* |
| [`icons/empty-tasks.svg`](icons/empty-tasks.svg) | Estado vazio da lista de tarefas | *pendente* |

Nove ícones, nenhum a mais. Ícones de functionality que o app ainda não tem
(login, notificações, configurações, perfil) ficam de fora de propósito: a
primeira entrega da interface é a navegação entre três telas, e um ícone sem
tela correspondente é escopo não pedido.

### Por que `currentColor`

O `stroke` é `currentColor`, e não um hex fixo. É o que permite ao FlutterFlow
recolorir o mesmo arquivo entre os dois temas já registrados na Tarefa 07:

| Tema | Cor do ícone |
|---|---|
| Claro | `#1A1312` (text principal) |
| Dark | `#F2F3F5` (text principal) |

Um SVG com `stroke="#1A1312"` escrito dentro ficaria ilegível no tema dark, e o
mesmo arquivo teria de ser duplicado em duas variantes. Com `currentColor`, o
FlutterFlow resolve a cor pelo tema ativo.

---

## 2. Estado da exportação do Figma

> **Estes nove arquivos ainda não foram exportados do Figma.** Eles foram
> **autoral** a partir do Design System registrado na Tarefa 07, e estão
> versionados como a base de trabalho.

Motivo: o arquivo do Figma para este projeto **ainda não existe**. A Tarefa 06
documentou quatro templates do Figma Community como referência visual
([`../docs/pesquisa/referencias.md`](../docs/pesquisa/referencias.md)) e não
duplicou nenhum arquivo. A instrução da Tarefa 09 — "abra o arquivo do Figma que
você duplicou na Tarefa 06" — aponta para um arquivo que nunca foi criado.

Existe um arquivo chamado **"EduTrack Orbit AI — Design System"**
(`file_key` `i6BKRzp9HGlhyubcz6xhJ1`), mas ele pertence a um **projeto
diferente e abandonado**: uma aplicação Python/Streamlit com histórico Git
próprio em `Documents/2 Semestre/Innovation Lab/EduTrack Orbit IA/`. Stack,
base de código e design distintos. Importar dali misturaria dois projetos numa
entrega só, então ele não foi usado.

### Pendência

Construir um arquivo do Figma dedicado ao EduTrack AI e reexportar os nove
ícones dali. O roteiro está em
[`../docs/guia-execucao-windows.md`](../docs/guia-execucao-windows.md). Quando
concluído, a coluna `node-id` desta tabela é preenchida com o identificador de
cada vetor e o status acima é alterado para exportado.

---

## 3. Como subir no FlutterFlow

Os nove arquivos vão em **Media Assets** (ícone de imagem, no canto superior
esquerdo do editor). No tema escuro, marcar a opção de tintura da imagem para que
o ícone acompanhe a cor do texto em vez de manter o preto original.

---

## 4. Licença

Os ícones seguem a geometria de traçado de um conjunto de ícones aberto
(24×24, `stroke-width="2"`, sem preenchimento), o mesmo padrão de bibliotecas
como Lucide e Feather. Ambos são MIT. Caso o arquivo do Figma passe a usar
ícones de uma biblioteca de terceiros, a licença de origem deve ser declarada
aqui antes do merge.