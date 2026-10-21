# Evidências — Tarefa 13: APIs CRUD para Disciplinas

**Aluno:** Wender Araújo Santos  
**Disciplina:** Innovation Lab: Desenvolvimento Avançado No/Low Code  
**Módulo:** 2 – Ciclo de Mudança com IA, Python e XanoScript

## O que foi feito
- Change OpenSpec `api-crud-disciplinas` (proposal, design, specs delta, tasks) validada e arquivada
- 4 endpoints CRUD criados em `apis/autenticacao_edutrack_ia_est/` e enviados ao Xano
- Grupo API `Autenticacao EduTrackIA Est` (canonical `JBdUmIAC`) com Swagger ativado
- Segurança por `user_id` em todos os métodos (`auth = ""` + filtro/autorização por dono)
- Endpoints de autenticação `auth/signup` e `auth/login` adicionados para viabilizar teste

## Endpoints criados
| Método | Rota | Descrição |
|---|---|---|
| GET | `/subjects` | Lista disciplinas do usuário autenticado |
| POST | `/subjects` | Cria disciplina com `user_id` do token |
| PATCH | `/subjects/{subject_id}` | Atualiza disciplina do usuário (merge parcial, nega dono diferente) |
| DELETE | `/subjects/{subject_id}` | Remove disciplina do usuário (nega dono diferente) |

## Base URL
`https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC`

## Arquivos versionados
- `apis/autenticacao_edutrack_ia_est/subjects_GET.xs`
- `apis/autenticacao_edutrack_ia_est/subjects_POST.xs`
- `apis/autenticacao_edutrack_ia_est/subjects_subject_id_PATCH.xs`
- `apis/autenticacao_edutrack_ia_est/subjects_subject_id_DELETE.xs`
- `apis/autenticacao_edutrack_ia_est/auth_signup_POST.xs`
- `apis/autenticacao_edutrack_ia_est/auth_login_POST.xs`
- `openspec/changes/archive/2026-10-20-api-crud-disciplinas/*`
- `openspec/specs/subjects/spec.md` (atualizada)

## Teste via Swagger
Os endpoints estão no Swagger do grupo `Autenticacao EduTrackIA Est`. 
Para validação completa (isolamento por usuário), testar com dois logins distintos pelo Swagger/Run & Debug do Xano.

## Prints
- [swagger-lista-endpoints.png](swagger-lista-endpoints.png) – Lista de endpoints do grupo `Autenticacao EduTrackIA Est` no Xano
- [swagger-documentacao.png](swagger-documentacao.png) – Documentação Swagger mostrando os endpoints CRUD de `subjects`
