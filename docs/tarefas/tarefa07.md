# Tarefa 07 – Configuração Inicial no FlutterFlow

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code
Módulo: 1 – Introdução ao Spec-Driven Development

Início da interface (frontend) do EduTrack AI no FlutterFlow, conectada ao
backend Xano e com o Design System definido.

---

1. O QUE FOI FEITO

- Projeto "EduTrack AI" criado no FlutterFlow a partir de um template em
  branco (Blank Project), com a configuração inicial de Firebase pulada
  conforme o enunciado — o backend principal do projeto é o Xano.
- Design System definido no Theme Settings, com paleta e tipografia
  registradas em flutterflow/REGISTRO-CONFIGURACAO.md.
- API Group "Xano Backend" criado em Settings & Integrations > API Calls,
  apontando para a Base URL da API do workspace no Xano.
- Configuração inicial documentada em flutterflow/REGISTRO-CONFIGURACAO.md,
  incluindo o mockup de referência do tema.

---

2. ENTREGÁVEIS

- [x] Screenshot da tela inicial do projeto no FlutterFlow.
      Arquivo: DMAtividades/7ATIVIDADE/flutterflow-projeto.png
- [x] Screenshot da configuração do "API Group" com a URL do Xano.
      Arquivo: DMAtividades/7ATIVIDADE/ApiXanoFlutterflow.png
- [x] Link do repositório GitHub com o README atualizado (este arquivo).
      https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est
      (Pull Request #4 mergeado: chore/flutterflow-setup -> main)

---

3. CRITÉRIOS DE AVALIAÇÃO

[✅] Projeto criado com nome correto no FlutterFlow.
Confirmação: projeto "EduTrack AI" criado a partir de Blank Project, com a
configuração inicial de Firebase pulada conforme o enunciado. Print em
DMAtividades/7ATIVIDADE/flutterflow-projeto.png.

[✅] Cores e fontes personalizadas no Theme Settings.
Confirmação: paleta vermelha em duas variantes (claro e dark + neon) e
tipografia Inter + JetBrains Mono aplicadas no Theme Settings. Prints em
DMAtividades/7ATIVIDADE/TemaCoresFlutterflow.png e
DMAtividades/7ATIVIDADE/TemaFonteFlutterflow.png. Mockup de referência
versionado em flutterflow/img/tema-referencia-vermelho.png e ficha completa
em flutterflow/REGISTRO-CONFIGURACAO.md.

[✅] Grupo de API configurado com a URL correta do Xano.
Confirmação: API Group "Xano Backend" no FlutterFlow apontando para
https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC. Print em
DMAtividades/7ATIVIDADE/ApiXanoFlutterflow.png. A API foi criada no Xano como
AutenticacaoEduTrackIAEst, com o endpoint GET /status validado em HTTP 200
(ver apis/autenticacao_edutrack_ia_est/).

[✅] Registro do progresso realizado no README do projeto via Git.
Confirmação: branch 'chore/flutterflow-setup' criada, 5 commits pushados e
Pull Request #4 aberto e mergeado na main (merge a5b05a5). A seção desta
tarefa está no README da branch main, junto de flutterflow/ e da API do
Xano.

---

4. OBSERVAÇÕES TÉCNICAS

- O FlutterFlow é uma ferramenta baseada em navegador: não há artefatos de
  build local para commitar. O versionamento do projeto acontece no
  repositório Git, onde a configuração é registrada em markdown.
- A paleta adotada parte das referências gratuitas levantadas na Tarefa 06 e
  foi consolidada em duas variantes — tema claro e tema dark com acento neon —
  mantendo o mesmo vermelho de marca (#E10600) como cor primária.
- No tema claro o vermelho neon (#FF1E3C) não é usado em texto: sobre fundo
  branco ele perde contraste. Nesse caso entra #C1121F, que é o mesmo
  vermelho com contraste acessível. O neon fica restrito a preenchimentos e
  brilhos, no limite de 5-10% da tela.
- A importação automática do Figma para o FlutterFlow é experimental e
  frequentemente falha. A abordagem é usar o Figma como referência visual e
  montar os componentes manualmente com Column, Row e Container.
  (A partir da Tarefa 09 a fonte de design passou a ser o mockup
  `flutterflow/tema-referencia.html` — ver Tarefa 09.)
- Base URL da API: no Xano, abrir a API criada na Tarefa 04 e copiar a Base URL
  exibida no topo do editor. O formato é
  https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC.

---

5. PRÓXIMO PASSO

Tarefa 08 — uso do OpenSpec para planejar as mudanças do projeto.

---
