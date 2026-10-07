# Guia de Execução no Windows — Tarefa 09

Roteiro para montar as três páginas e os assets do EduTrack AI no FlutterFlow, a
partir de uma máquina Windows 11.

---

## Por que o Windows

O MacBook Pro 2016 usado no desenvolvimento não abre nenhum dos dois IDEs web:

| Ferramenta | Bloqueio no Mac |
|---|---|---|
| **FlutterFlow** | Não usa WebGL, mas é um IDE web pesado e a CPU (Intel Core `m-5Y31` a 0,90 GHz, dual-core) não sustenta o carregamento. |

> O **Figma deixou de ser usado** (decisão registrada na spec `design-assets`):
> o arquivo do projeto nunca existiu e nenhuma máquina disponível o abre. A
> fonte de design é o mockup `flutterflow/tema-referencia.html` — `assets/` já
> contém os nove ícones a partir dele, sem depender do Figma. Este guia usa o
> HTML apenas como referência visual.

Nada disso é problema do projeto — é limite de hardware. A execução acontece
inteiramente no Windows, por acesso remoto. O que volta para o repositório são
os arquivos de `assets/` e os prints de evidência.

---

## Passo 1 — Gerar os nove arquivos SVG no Windows

Os ícones já existem no repositório. Este passo os materializa como arquivos
`.svg` na máquina Windows, sem depender de Git, de arrastar-e-soltar ou de
sincronização de área de transferência — o conteúdo trafega como texto
(base64), que qualquer forma de acesso remoto preserva.

**1.1.** `Win + X` → **Terminal** ou **PowerShell**. Se abrir o Terminal do
Windows, use a aba **PowerShell**.

**1.2.** Cole a linha abaixo inteira, com `Ctrl+V`, e aperte `Enter`. É uma linha
só e longa de propósito: PowerShell falha ao colar scripts multilinha.

```powershell
$d="$env:USERPROFILE\edu\icons";New-Item -ItemType Directory -Force -Path $d|Out-Null;$f=@{"home.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNSAyMXYtOGExIDEgMCAwIDAtMS0xaC00YTEgMSAwIDAgMC0xIDF2OCIvPjxwYXRoIGQ9Ik0zIDEwYTIgMiAwIDAgMSAuNzA5LTEuNTI4bDctNWEyIDIgMCAwIDEgMi41ODIgMGw3IDVBMiAyIDAgMCAxIDIxIDEwdjlhMiAyIDAgMCAxLTIgMkg1YTIgMiAwIDAgMS0yLTJ6Ii8+PC9zdmc+";"subjects.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMiA3djE0Ii8+PHBhdGggZD0iTTMgMThhMSAxIDAgMCAxLTEtMVY0YTEgMSAwIDAgMSAxLTFoNWE0IDQgMCAwIDEgNCA0IDQgNCAwIDAgMSA0LTRoNWExIDEgMCAwIDEgMSAxdjEzYTEgMSAwIDAgMS0xIDFoLTZhMyAzIDAgMCAwLTMgMyAzIDMgMCAwIDAtMy0zeiIvPjwvc3ZnPg==";"tasks.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Im0zIDE3IDIgMiA0LTQiLz48cGF0aCBkPSJtMyA3IDIgMiA0LTQiLz48cGF0aCBkPSJNMTMgNmg4Ii8+PHBhdGggZD0iTTEzIDEyaDgiLz48cGF0aCBkPSJNMTMgMThoOCIvPjwvc3ZnPg==";"add-subject.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik00IDQuNUEyLjUgMi41IDAgMCAxIDYuNSAySDE5YTEgMSAwIDAgMSAxIDF2MThhMSAxIDAgMCAxLTEgMUg2LjVBMi41IDIuNSAwIDAgMSA0IDE5LjV6Ii8+PHBhdGggZD0iTTEyIDcuNXY2Ii8+PHBhdGggZD0iTTkgMTAuNWg2Ii8+PC9zdmc+";"add-task.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjEwIi8+PHBhdGggZD0iTTggMTJoOCIvPjxwYXRoIGQ9Ik0xMiA4djgiLz48L3N2Zz4=";"check.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0yMCA2IDkgMTdsLTUtNSIvPjwvc3ZnPg==";"clock.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjEwIi8+PHBhdGggZD0iTTEyIDZ2Nmw0IDIiLz48L3N2Zz4=";"empty-subjects.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0yMiAxMmgtNmwtMiAzaC00bC0yLTNIMiIvPjxwYXRoIGQ9Ik01LjQ1IDUuMTEgMiAxMnY2YTIgMiAwIDAgMCAyIDJoMTZhMiAyIDAgMCAwIDItMnYtNmwtMy40NS02Ljg5QTIgMiAwIDAgMCAxNi43NiA0SDcuMjRhMiAyIDAgMCAwLTEuNzkgMS4xMXoiLz48L3N2Zz4=";"empty-tasks.svg"="PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxyZWN0IHdpZHRoPSI4IiBoZWlnaHQ9IjQiIHg9IjgiIHk9IjIiIHJ4PSIxIi8+PHBhdGggZD0iTTE2IDRoMmEyIDIgMCAwIDEgMiAydjE0YTIgMiAwIDAgMS0yIDJINmEyIDIgMCAwIDEtMi0yVjZhMiAyIDAgMCAxIDItMmgyIi8+PHBhdGggZD0iTTggMTFoLjAxIi8+PHBhdGggZD0iTTggMTZoLjAxIi8+PHBhdGggZD0iTTEyIDExaDQiLz48cGF0aCBkPSJNMTIgMTZoNCIvPjwvc3ZnPg=="};foreach($k in $f.Keys){[System.IO.File]::WriteAllBytes((Join-Path $d $k),[Convert]::FromBase64String($f[$k]))};Write-Host "--- arquivos criados ---";Get-ChildItem $d|Select-Object Name,Length
```

**1.3.** Confirme que a tabela tem **nove linhas**, cada `Length` entre 130 e 500
bytes.

**1.4.** `explorer $env:USERPROFILE\edu\icons` abre a pasta.

---

## Passo 2 — Referência visual

O Figma não é usado neste projeto (decisão em `openspec/changes/add-figma-assets-and-navigation/specs/design-assets/spec.md`). O mockup é a referência de design:

**2.1.** Abra `flutterflow/tema-referencia.html` num navegador. Ele é a fonte
editável do design — paleta, tipografia, cards e a barra de navegação.

**2.2.** Confira que a seção Dashboard do mockup organiza os elementos em grupos
por função: um grupo para o card de disciplina, um para o card de tarefa e um
para a barra de navegação. Nenhum elemento deve ficar solto fora de grupo —
se estiver, agrupe com `Ctrl+G` na página referente.

**2.3.** Os nove ícones de `assets/icons/` já são a saída do design — não há
exportação a fazer. Use a tabela de `../assets/README.md` para conferir que cada
ícone tem contraparte no mockup.

> Não use o arquivo "EduTrack Orbit AI — Design System". Ele pertence ao
> projeto antigo em Streamlit, é outro código e outro design. O motivo está
> registrado em `assets/README.md`.

---

## Passo 3 — FlutterFlow

**3.1.** `https://app.flutterflow.io` → projeto **EduTrack AI**.

**3.2.** Crie as três páginas com os nomes exatos: `HomePage`, `SubjectsPage`,
`TasksPage`.

**3.3.** Cada página com título visível:

| Página | Título | Conteúdo |
|---|---|---|
| `HomePage` | EduTrack AI | um card de visão geral |
| `SubjectsPage` | Disciplinas | lista de `Container` com borda arredondada, cada um com nome, professor e carga horária |
| `TasksPage` | Tarefas | `ListView` com ao menos um item (título, data, estado) |

**3.4.** Componente `NavBar` em `Column`, no rodapé: três itens — Home →
`HomePage`, Disciplinas → `SubjectsPage`, Tarefas → `TasksPage`. Cada item com a
action **Navigate to Page** apontando para a página correspondente. Item da
página atual em `Primary Color`, os demais em `#7B6A67`.

**3.5.** Suba os nove ícones em **Media Assets**, com a opção de tintura marcada
para que sigam a cor do tema.

**3.6.** Confira as três páginas em **largura de celular** e em **preview de
navegador**.

---

## Passo 4 — Evidência

Quatro prints, em `DMAtividades/9ATIVIDADE/`:

| Arquivo | Conteúdo |
|---|---|
| `flutterflow-home.png` | `HomePage` |
| `flutterflow-subjects.png` | `SubjectsPage` |
| `flutterflow-tasks.png` | `TasksPage` |
| `flutterflow-navbar.png` | a `NavBar` com os três itens |
| `assets-vscode.png` | a pasta `assets/` aberta no VS Code |

---

## Problemas conhecidos

**O FlutterFlow não carrega.** Permite pop-ups e área de transferência de
`app.flutterflow.io` nas configurações do navegador antes de desconsiderar.

**O ícone aparece vermelho sólido no Media Assets.** Não é o vetor — é a
miniatura gerada pelo upload. Abra o asset e confira o traçado real.

**O SVG sobe com `stroke="#1A1312"` fixo.** Esperado se o editor de SVG
materializou a cor; trocar por `currentColor` no arquivo de `assets/icons/`