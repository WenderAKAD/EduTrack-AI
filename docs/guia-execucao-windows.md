# Guia de Execução no Windows — Tarefa 09

Roteiro para montar as três páginas e os assets do EduTrack AI no FlutterFlow, a
partir de uma máquina Windows 11.

---

## Por que o Windows

O MacBook Pro 2016 usado no desenvolvimento não abre nenhum dos dois IDEs web:

| Ferramenta | Bloqueio no Mac |
|---|---|
| **Figma** | Exige Safari 17.4+; a máquina tem Safari 16.6 (macOS 13.7.8 não recebe versão mais nova). O Chrome 154 também recusa: `WebGL: Disabled`, porque a Intel HD Graphics 5300 de 2015 está na blocklist da GPU. |
| **FlutterFlow** | Não usa WebGL, mas é um IDE web pesado e a CPU (Intel Core `m-5Y31` a 0,90 GHz, dual-core) não sustenta o carregamento. |

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

## Passo 2 — Figma

**2.1.** Crie um arquivo novo em `figma.com` chamado **EduTrack AI — Design
System**.

> Não use o arquivo "EduTrack Orbit AI — Design System". Ele pertence ao
> projeto antigo em Streamlit, é outro código e outro design. O motivo está
> registrado em `assets/README.md`.

**2.2.** Na aba `Icons`, arraste os nove `.svg` do Explorer até o canvas — um de
cada vez, senão o Figma empilha todos no mesmo ponto. Organize num grid com
folga de 40px.

**2.3.** Renomeie cada vetor no painel **Design** para `home`, `subjects`,
`tasks`, `add-subject`, `add-task`, `check`, `clock`, `empty-subjects`,
`empty-tasks`.

**2.4.** Crie a variável de cor. No painel de variáveis (ícone de sliders, à
direita): `+ Create variable` → nome `icon/default` → tipo **Color** → valor
`1A1312`. Selecione os nove ícones e aplique a variável. É o que permite
recolorir entre os temas claro e dark.

**2.5.** Crie a aba `Dashboard` e monte a tela de referência seguindo
[`../flutterflow/tema-referencia.html`](../flutterflow/tema-referencia.html):
header, um card de disciplina, um card de tarefa e a barra de navegação com os
três ícones. Agrupe cada bloco com `Ctrl+G`.

**2.6.** Exporte: selecione o ícone → painel **Design** → seção **Export** → `+`
→ **SVG** → Exportar.

Anote o `node-id` de cada vetor (aparece na URL ao selecionar, ou em
*Copy link to selection*) para preencher a tabela de
[`../assets/README.md`](../assets/README.md).

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

**O SVG arrastado aparece vermelho sólido.** Não é o vetor — foi a miniatura do
Explorer. Arraste de novo.

**O export sai com `stroke="#000000"`.** Esperado: o Figma converte a variável
para o valor literal no export. Registrar como limitação em `assets/README.md`
ou trocar por `currentColor` à mão.

**O FlutterFlow não carrega.** Permite pop-ups e área de transferência de
`app.flutterflow.io` nas configurações do navegador antes de desconsiderar.

**O Figma não tem WebGL.** No Windows isso não deveria ocorrer; se ocorrer, teste
outro navegador.