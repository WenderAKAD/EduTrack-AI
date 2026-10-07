# Registro de Configuração — FlutterFlow (Tarefa 07)

**Disciplina:** Innovation Lab: Desenvolvimento Avançado No/Low Code
**Módulo:** 1 – Introdução ao Spec-Driven Development
**Aluno:** Wender Araújo Santos
**E-mail institucional:** wender.araujo@aluno.impacta.edu.br
**Data de entrega:** 6 de outubro de 2026

Registro da configuração inicial do frontend do EduTrack AI no FlutterFlow,
conectado ao backend Xano.

---

## 1. Projeto

| Campo | Valor |
|---|---|
| Nome do projeto | **EduTrack AI** |
| Tipo | Blank Project (template em branco) |
| Firebase | Pulado nesta etapa — o backend principal é o **Xano** |
| Backend | Xano, via API Groups |

---

## 2. Design System — Theme Settings

### 2.1 Paleta aprovada

Identidade cromática única, declarada em duas variantes (mesmo vermelho,
duas leituras). Mockup de referência:
[`img/tema-referencia-vermelho.png`](img/tema-referencia-vermelho.png)
— fonte editável em [`tema-referencia.html`](tema-referencia.html).

#### Variante A — Tema Claro (padrão)

| Token | Valor | Uso |
|---|---|---|
| Primary Color | `#E10600` | Botões primários, CTAs |
| Secondary Color | `#8B0012` | Sidebar, cabeçalhos, estado pressionado |
| Accent / texto vermelho | `#C1121F` | Realces, links, tags — garante contraste AA |
| Background | `#F7F4F3` | Fundo da aplicação |
| Surface | `#FFFFFF` | Cards, modais, painéis |
| Border | `#EADFDC` | Bordas e divisores |
| Text principal | `#1A1312` | Títulos e corpo |
| Text secundário | `#7B6A67` | Legendas e labels |

#### Variante B — Tema Dark + Neon

| Token | Valor | Uso |
|---|---|---|
| Primary Color | `#E10600` | Botões primários, CTAs |
| Secondary Color | `#101215` | Sidebar |
| Accent (neon) | `#FF1E3C` | Destaques, glow, aba ativa |
| Hover / glow | `#FF4D5E` | Estado de hover |
| Background | `#0A0A0A` | Fundo da aplicação |
| Surface | `#16181C` | Cards, modais, painéis |
| Border | `#2A2D33` | Bordas e divisores |
| Text principal | `#F2F3F5` | Títulos e corpo |
| Text secundário | `#9AA0A6` | Legendas e labels |

**Regra de uso do neon:** o vermelho neon (`#FF1E3C`) é acento — limitar a
5–10% da tela (CTA, tags de atraso, foco). No tema claro ele **não** é usado em
texto, porque perde contraste sobre fundo branco; ali entra `#C1121F`.

### 2.2 Tipografia

| Token | Valor | Observação |
|---|---|---|
| Fonte de títulos | **Inter** (Bold / SemiBold) | Tipografia de dashboard |
| Fonte de corpo | **Inter** (Regular) | Leitura de listas e tabelas |
| Fonte mono | **JetBrains Mono** | Logs, datas, IDs e trechos de API |

**Justificativa:** a paleta baseia-se nas referências gratuitas levantadas na
Tarefa 06 (`docs/pesquisa/referencias.md`) e na paleta "Neon Red / Dark"
definida em conjunto, priorizando legibilidade em telas densas de
acompanhamento acadêmico.

---

## 3. Conexão com o Xano — API Group

| Campo | Valor |
|---|---|
| Nome do grupo no FlutterFlow | **Xano Backend** |
| Base URL | `https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC` |
| Endpoint de teste | `GET /status` |
| Instância | `x8ki-letl-twmt` (Free Instance) |
| Workspace | Wender's Workspace (id `148813`) |
| Branch no Xano | `v1` (Live branch) |
| Token | Access Token **VS Code** — Metadata API & MCP Server |
| Escopos | Database, API Groups, Functions, Content |

**API group no Xano:** `AutenticacaoEduTrackIAEst` — canonical `JBdUmIAC`
(atribuído pelo Xano). Pasta versionada: `apis/autenticacao_edutrack_ia_est/`.

**Teste de conexão:** usar a URL completa do endpoint `status`:

```
https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC/status
```

Resposta `200` confirmada em 4 de outubro de 2026:

```json
{
  "status": "ok",
  "app": "EduTrack AI",
  "modulo": "1 - Introducao ao Spec-Driven Development",
  "instance": "x8ki-letl-twmt",
  "timestamp": "now"
}
```

> **Nota:** o campo `timestamp` devolve a string literal `"now"`. Para gerar um
> epoch em ms é preciso `datetime_now()` — ajuste previsto para a Tarefa 08.

> **Nota:** a Tarefa 04 apenas fez *pull* dos 10 API groups padrão que já
> vinham no workspace do Xano. Nenhuma tabela (`tables/`) foi criada até aqui —
> a tabela `user` existe apenas como *addon*. Por isso o endpoint `status` foi
> escrito sem depender de banco: ele valida a conexão e libera a Base URL para
> o FlutterFlow. Os endpoints de login e cadastro entram na Tarefa 08, junto com
> a tabela de usuários.

---

## 4. Fonte de design (mockup, sem Figma)

| Campo | Valor |
|---|---|
| Fonte editável de design | `tema-referencia.html` (paleta, tipografia, cards e NavBar) |
| Referências visuais | `docs/pesquisa/referencias.md` (lista os 4 templates gratuitos escolhidos) |

**Observação:** o Figma não é usado neste projeto — o arquivo citado na
Tarefa 09 nunca foi criado e nenhuma máquina disponível abre o editor. A fonte
de design é o mockup `tema-referencia.html`; os componentes são montados
manualmente no FlutterFlow com os widgets `Column`, `Row` e `Container`,
seguindo o mockup como referência visual.

---

## 5. Fluxo Git

Branch da tarefa:

```
chore/flutterflow-setup
```

Comandos:

```
git checkout -b chore/flutterflow-setup
git add README.md flutterflow/
git commit -m "chore: atualiza status do frontend no README"
git push -u origin chore/flutterflow-setup
```

---

## 6. Navegação e Assets (Tarefa 09)

Especificação da navegação adicionada na Tarefa 09. Registrada aqui porque o
FlutterFlow não produz artefato de build: o versionamento do projeto é este
documento mais os arquivos de `assets/`.

### 6.1 Páginas

Três páginas, com os nomes exatos abaixo — o nome da página é o alvo das
actions de navegação, e o action `Navigate to Page` o resolve pelo nome.

| Página | Conteúdo | Ícone na NavBar |
|---|---|---|
| `HomePage` | Título **EduTrack AI** + card de visão geral | `home.svg` |
| `SubjectsPage` | Título **Disciplinas** + lista de `Container` com borda arredondada, cada um com nome, professor e carga horária | `subjects.svg` |
| `TasksPage` | Título **Tarefas** + `ListView` com ao menos um item, cada um com título, data e estado | `tasks.svg` |

Todas as páginas declararem que **não chamam nenhuma API** e exibem apenas
conteúdo estático de exemplo. Os endpoints de `subjects` e `user` entram na
tarefa seguinte; ligar as telas a eles agora produziria erro de runtime em tela
vazia.

### 6.2 Barra de navegação

Componente `NavBar`, em `Column`, no rodapé da página. Três itens, nesta ordem:

| # | Rótulo | Destino | Ícone | Estado ativo |
|---|---|---|---|---|
| 1 | Home | `HomePage` | `home.svg` | `#E10600` |
| 2 | Disciplinas | `SubjectsPage` | `subjects.svg` | `#E10600` |
| 3 | Tarefas | `TasksPage` | `tasks.svg` | `#E10600` |

Cada item usa a action **Navigate to Page** apontando para a página da tabela.
O item da página atual fica com o preenchimento em `Primary Color`; os demais,
com `Text secundário` (`#7B6A67`).

### 6.3 Assets

Nove ícones SVG em [`../assets/icons/`](../assets/icons/), com o registro de
origem em [`../assets/README.md`](../assets/README.md). Todos usam
`stroke="currentColor"`, o que permite recolorir entre os dois temas sem
duplicar arquivo.

### 6.4 Largura

O FlutterFlow serve build de celular e preview de navegador a partir do mesmo
projeto, então cada página é conferida nas duas larguras. Um layout que só
funciona em uma delas não atende ao requisito.

---

## 7. Checklist dos critérios de avaliação

| # | Critério | Print de evidência | Status |
|---|---|---|---|
| 1 | Projeto criado com nome correto no FlutterFlow | `flutterflow-projeto.png` | ✅ |
| 2 | Cores e fontes personalizadas no Theme Settings | `flutterflow-theme.png` | ☐ |
| 3 | Grupo de API configurado com a URL correta do Xano | `flutterflow-api-group.png` | ☐ |
| 4 | Registro do progresso no README do projeto via Git | `flutterflow-git-readme.png` | ☐ |
| 5 | Importação do Figma (opcional) — **não se aplica** | `flutterflow-figma.png` | ⛔ |

---

## 8. Referências

- Documentação das Tarefas 01 a 07: `README.md`
- Referências de design: `docs/pesquisa/referencias.md`
- Mockup do tema: [`tema-referencia.html`](tema-referencia.html) / [`img/tema-referencia-vermelho.png`](img/tema-referencia-vermelho.png)
- Navegação e assets da Tarefa 09: seção 6 deste arquivo
- Registro de origem dos ícones: [`../assets/README.md`](../assets/README.md)
