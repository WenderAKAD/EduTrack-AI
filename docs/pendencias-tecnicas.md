# Pendências Técnicas

[← Voltar ao índice](../README.md#pendências-técnicas)

---

Itens que foram identificados e adiados de propósito, registrados aqui para
verificação posterior. Nenhum deles bloqueia as tarefas 01 a 08.

### 1. Limpeza dos objetos de template do Xano

O workspace *Wender's Workspace* (id `148813`, branch `v1`) contém 194 objetos
que **não pertencem ao EduTrack AI**:

| Tipo | Quantidade | Origem provável |
|---|---|---|
| api_endpoint | 176 | templates padrão do Xano |
| api_group | 10 | `event_logs`, `members_accounts`, `send_grid`, `authentication` |
| function | 5 | `sendgrid_*`, `getting_started_template/*` |
| tool | 1 | `search_xano_docs` |
| agent | 1 | `Xano Example Agent` |
| addon | 1 | `user` (ver item 3) |

Do EduTrack AI existem apenas `apis/autenticacao_edutrack_ia_est/` (Tarefa 07)
e, a partir da Tarefa 08, `tables/user.xs` e `tables/subjects.xs`.

**Como separar no dia a dia**, sem apagar nada no servidor:

```bash
xano workspace push \
  --include "tables/*.xs" \
  --include "apis/autenticacao_edutrack_ia_est/**"
```

**Para remover de fato** do workspace seria preciso `--sync --delete`, que apaga
os objetos também no servidor. **Não foi executado** — é destrutivo e exige
decisão consciente. Requer ainda um `xano workspace pull` antes, para atualizar
o cache local (ver item 2), sob risco de sobrescrever arquivos versionados.

### 2. Cache local do CLI desatualizado

O arquivo `.xano/branches/v1/objects.json` é de **28 de setembro de 2026**,
anterior à Tarefa 07. Consequência: o preview de push reporta
`CREATE api_group AutenticacaoEduTrackIAEst`, mas essa API já existe no
servidor (responde HTTP 200 em `/status`) — o cache é que está desatualizado.

**Atenção:** não rodar `xano workspace pull` antes de versionar os arquivos
atuais, sob risco de o pull sobrescrever ou apagar `tables/user.xs` e
`tables/subjects.xs`.

### 3. `addons/109599_user.xs` corrompido

O arquivo declara referências vazias:

```xs
int user_id? { table = "" }
db.query "" { ... }
```

Ele **não** é a definição de uma tabela — é um addon (bloco de lógica
reutilizável) quebrado. Foi ele que gerou a falsa impressão de que a tabela
`user` já existia no Xano. Substituído pela tabela real em `tables/user.xs`.

### 4. Extensão `xano.xanoscript` descontinuada

A extensão do VS Code que fazia o push nas Tarefas 04 a 07 foi descontinuada
pela Xano. O fluxo atual usa o **Xano CLI**:

| Componente | Versão | Papel |
|---|---|---|
| `@xano/cli` | 1.3.3 | push, pull, auth, metadata |
| `xano.xanoscript-language-server` | 0.3.3 | suporte a `.xs` no editor |

A extensão antiga foi mantida instalada apenas para não quebrar o
versionamento anterior, mas novos pushes devem usar o CLI.

### 5. `tables/user.xs` não é byte-idêntico ao servidor

A tabela `user` tem 8 campos no Xano. O `user_id` foi criado manualmente no
dashboard e é uma self-reference que o EduTrack AI não usa (o app é de conta
única, sem times nem multi-tenant).

O campo está declarado em `tables/user.xs`, mas **sem o atributo `methods`**
(ação referencial), que a documentação da Xano não descreve e que só existe no
servidor. Consequência: um dry-run sempre reporta `UPDATE_FIELD` em
`tables/user.xs`.

**Decisão:** manter o `user_id` declarado localmente e **não dar push nessa
tabela** novamente. Declarar o campo é o que impede o CLI de propor
`DROP_FIELD user_id`, que removeria o campo do servidor. O `UPDATE_FIELD`
restante é não destrutivo e a tabela está vazia.

Para eliminar a diferença seria preciso ler o valor de "On Delete" do campo no
dashboard e declará-lo localmente.

---

Data de entrega: 6 de outubro de 2026
Aluno: Wender Araujo Santos

---
