# Instruções para Agentes de IA - EduTrack AI

## Perfil do Projeto

Este é o projeto **EduTrack AI**, um app de gestão acadêmica.

- **Frontend:** FlutterFlow

- **Backend:** Xano (via XanoScript)

- **Metodologia:** Spec-Driven Development (OpenSpec)

- **IA Assistente:** Gemini Code Assist (Google Cloud)

## Customizações do EduTrack AI

### Nomenclatura Específica

1. **Língua:** Código e variáveis sempre em **INGLÊS**.

2. **Banco de Dados:** Use `snake_case` (ex: `subjects`, `user_id`).

3. **Proposals OpenSpec:** Use `kebab-case` (ex: `add-subjects-table`).

### Conhecimento do Schema

1. **Tabela de Autenticação:** a tabela `user` é criada pelo projeto em `tables/user.xs` (change `create-user-table`). Ela **não** vem pronta no Xano. Qualquer tabela que referencie o usuário logado depende dela existir antes — por isso `user` precisa ser enviado ao Xano em um push separado, antes das tabelas que a referenciam.

2. **Relacionamentos:** Sempre use `user_id` para vincular dados ao usuário logado.

### Regras de Segurança

1. Toda query ao banco DEVE filtrar por `user_id` do usuário autenticado.

### ⚠️ OBRIGATÓRIO: Consulte openspec/AGENTS.md

**ANTES de criar qualquer proposal ou `specs/spec.md`:**

**VOCÊ DEVE usar `read_file` para ler `openspec/AGENTS.md` COMPLETO.**

Este arquivo contém a estrutura obrigatória do `proposal.md` (## Why, ## What Changes, ## Impact) e os formatos de delta corretos.

### ⚠️ IMPORTANTE: Formato de `specs/spec.md` em changes/

**Arquivos `specs/spec.md` dentro de `openspec/changes/<id>/specs/spec.md` são DELTAS.**

Use:

- `## ADDED Requirements` (NÃO use apenas `## Requirements`)

- `## MODIFIED Requirements` (para alterações)

- `## REMOVED Requirements` (para remoções)

Exemplo correto para arquivo em changes/:
subjects Specification
Purpose
Define database structure for subjects.
ADDED Requirements    ← Use ADDED, não Requirements
Requirement: Create table
Sistema SHALL create subjects table.
Scenario: User creates subject
WHEN user creates subject
THEN system stores with user_id

### Escopo de Tarefas (CRÍTICO)

**O arquivo `tasks.md` deve conter APENAS as tarefas solicitadas pelo usuário.**

- Se o usuário pedir "criar tabela X", NÃO adicione automaticamente: API CRUD, testes, ou frontend.

- Se o usuário pedir "criar API para Y", NÃO adicione automaticamente: testes ou frontend.

- Adicione tarefas extras SOMENTE se explicitamente solicitado.

### Responsabilidade da IA

**SUA TAREFA TERMINA NA GERAÇÃO DOS ARQUIFOS.**

- ✅ Criar/editar arquivos (.xs, `specs/spec.md`, tasks.md)

- ✅ Marcar tasks completas em tasks.md

- ✅ Atualizar todos.md

- ❌ NÃO tente fazer push, sync ou deploy para Xano

- ❌ NÃO procure ou invoque ferramentas push_all_changes_to_xano

**O desenvolvedor é responsável por revisar e fazer push manualmente.**

⚠️ IMPORTANTE: Se seu arquivo AGENTS.md já tem um bloco <!-- OPENSPEC:START --> ... <!-- OPENSPEC:END -->, deixe-o intacto! Cole o conteúdo acima ANTES desse bloco.

<!-- OPENSPEC:START -->
# AGENTS.md

Instructions and project rules for AI agents working on EduTrack AI.
<!-- OPENSPEC:END -->
