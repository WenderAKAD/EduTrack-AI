# Design

## Context

EduTrack AI uses Xano as its backend database. User registration currently allows any email without verification. To ensure high-quality authentication and valid student emails, we need an email verification step where a 6-digit code is issued and must be supplied during signup.

## Decisions

1. **Dedicated Verification Table (`email_verification`):**
   - Keeps `user` table clean and strictly focused on active accounts.
   - Stores `email`, `code`, `expires_at`, `verified`, and `created_at`.
   - Allows clean expiration cleanup and rate-limiting if needed.

2. **Endpoint Design:**
   - `POST /auth/send-verification-code`:
     - Input: `email`.
     - Checks if user already exists (`db.get user where email == $input.email`). If exists, throws `accessdenied`.
     - Generates 6-digit code (e.g. `100000 + random(899999)`).
     - Saves to `email_verification`.
     - Response: `{status: "ok", message: "Codigo de verificacao gerado com sucesso.", code: $code}` (returns code for local/dev and can trigger SendGrid function if configured).
   - `POST /auth/signup`:
     - Input: `name`, `email`, `password`, `verification_code`.
     - Precondition: queries `email_verification` where `email == $input.email && code == $input.verification_code && expires_at > now`.
     - If not found or expired, throws `accessdenied` ("Codigo de verificacao invalido ou expirado.").
     - Upon validation, executes `db.add user` and creates auth token.

3. **Frontend Integration (`app.py`):**
   - Web application connects directly to Xano API for authentication (`POST /auth/send-verification-code`, `POST /auth/signup`, `POST /auth/login`).
   - Two-step signup UI:
     1. User enters email -> clicks "Enviar Código".
     2. Code input appears alongside Name and Password -> clicks "Cadastrar".
     3. User account is immediately persisted in Xano!

## Risks / Trade-offs

- **Offline / Local test:** If external network to Xano is momentarily unavailable or SendGrid credentials are not configured in Xano workspace, the endpoint can return the verification code in the response payload for easy development and testing, ensuring the developer is never blocked.
