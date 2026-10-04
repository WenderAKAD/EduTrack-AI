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
| Nome do grupo | **Xano Backend** |
| Base URL | `https://x8ki-letl-twmt.n7.xano.io/api:<API_ID>` |
| Instância | `x8ki-letl-twmt` (Free Instance) |
| Workspace | Wender's Workspace (id `148813`) |
| Branch no Xano | `v1` (Live branch) |
| Token | Access Token **VS Code** — Metadata API & MCP Server |
| Escopos | Database, API Groups, Functions, Content |

**Como obter a Base URL:** no Xano, abrir a API criada na Tarefa 04 e copiar a
*Base URL* exibida no topo do editor.

**Teste de conexão:** abrir a URL no navegador. A resposta esperada é um erro
JSON — isso confirma que a conexão está funcionando.

---

## 4. Integração com o Figma (opcional / experimental)

| Campo | Valor |
|---|---|
| Figma Personal Access Token | *a colar* |
| Referências de design | `docs/pesquisa/referencias.md` (lista os 4 templates gratuitos escolhidos) |

**Observação:** a importação automática do Figma para o FlutterFlow é
experimental e frequentemente falha. A abordagem adotada é usar o Figma como
**referência visual** e montar os componentes manualmente no FlutterFlow com os
widgets `Column`, `Row` e `Container`.

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

## 6. Checklist dos critérios de avaliação

| # | Critério | Print de evidência | Status |
|---|---|---|---|
| 1 | Projeto criado com nome correto no FlutterFlow | `flutterflow-projeto.png` | ✅ |
| 2 | Cores e fontes personalizadas no Theme Settings | `flutterflow-theme.png` | ☐ |
| 3 | Grupo de API configurado com a URL correta do Xano | `flutterflow-api-group.png` | ☐ |
| 4 | Registro do progresso no README do projeto via Git | `flutterflow-git-readme.png` | ☐ |
| 5 | Importação do Figma (opcional) | `flutterflow-figma.png` | ☐ |

---

## 7. Referências

- Documentação das Tarefas 01 a 07: `README.md`
- Referências de design: `docs/pesquisa/referencias.md`
- Mockup do tema: [`tema-referencia.html`](tema-referencia.html) / [`img/tema-referencia-vermelho.png`](img/tema-referencia-vermelho.png)
