import hashlib
import html
import json
import os
import secrets
import sqlite3
import urllib.parse
import urllib.request
from contextlib import contextmanager
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st

from scripts.calculate_progress import calculate_progress, calculate_subject_progress
from scripts.search_overdue_subjects import handle, is_overdue_task

DB_PATH = Path(__file__).with_name("edutrack.db")
BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC"


@contextmanager
def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with db() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS subject (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                teacher TEXT NOT NULL,
                hours INTEGER NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS academic_task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                due_date TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
                FOREIGN KEY (subject_id) REFERENCES subject(id) ON DELETE CASCADE
            );
            """
        )
        columns = [row["name"] for row in conn.execute("PRAGMA table_info(user)")]
        if "welcome_seen" not in columns:
            conn.execute("ALTER TABLE user ADD COLUMN welcome_seen INTEGER NOT NULL DEFAULT 0")


def hash_password(password, salt=None):
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), bytes.fromhex(salt), 200_000
    ).hex()
    return f"{salt}${digest}"


def verify_password(password, stored):
    salt, expected = stored.split("$", 1)
    actual = hash_password(password, salt).split("$", 1)[1]
    return secrets.compare_digest(actual, expected)


def find_user(username):
    with db() as conn:
        return conn.execute(
            "SELECT * FROM user WHERE username = ?", (username.strip().lower(),)
        ).fetchone()


def create_user(username, password):
    with db() as conn:
        try:
            cursor = conn.execute(
                "INSERT INTO user (username, password_hash) VALUES (?, ?)",
                (username.strip().lower(), hash_password(password)),
            )
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None


def get_welcome_seen(user_id):
    with db() as conn:
        row = conn.execute(
            "SELECT welcome_seen FROM user WHERE id = ?", (user_id,)
        ).fetchone()
    return bool(row["welcome_seen"]) if row else True


def mark_welcome_seen(user_id):
    with db() as conn:
        conn.execute("UPDATE user SET welcome_seen = 1 WHERE id = ?", (user_id,))


def list_subjects(user_id):
    with db() as conn:
        rows = conn.execute(
            "SELECT * FROM subject WHERE user_id = ? ORDER BY name", (user_id,)
        ).fetchall()
    return [dict(row) for row in rows]


def list_tasks(user_id):
    with db() as conn:
        rows = conn.execute(
            "SELECT * FROM academic_task WHERE user_id = ? ORDER BY due_date",
            (user_id,),
        ).fetchall()
    return [dict(row) for row in rows]


def add_subject(user_id, name, teacher, hours):
    with db() as conn:
        conn.execute(
            "INSERT INTO subject (user_id, name, teacher, hours) VALUES (?, ?, ?, ?)",
            (user_id, name.strip(), teacher.strip(), hours),
        )


def add_task(user_id, subject_id, title, status, due_date):
    due_value = due_date.isoformat() if hasattr(due_date, "isoformat") else str(due_date)
    with db() as conn:
        conn.execute(
            "INSERT INTO academic_task (user_id, subject_id, title, status, due_date) "
            "VALUES (?, ?, ?, ?, ?)",
            (user_id, subject_id, title.strip(), status, due_value),
        )


def set_task_status(user_id, task_id, status):
    with db() as conn:
        conn.execute(
            "UPDATE academic_task SET status = ? WHERE id = ? AND user_id = ?",
            (status, task_id, user_id),
        )


def delete_task(user_id, task_id):
    with db() as conn:
        conn.execute(
            "DELETE FROM academic_task WHERE id = ? AND user_id = ?",
            (task_id, user_id),
        )


def delete_subject(user_id, subject_id):
    with db() as conn:
        conn.execute(
            "DELETE FROM subject WHERE id = ? AND user_id = ?",
            (subject_id, user_id),
        )


def secret(name):
    try:
        return st.secrets.get(name, "") or ""
    except Exception:
        return ""


def xano_login(base_url, email, password):
    body = json.dumps({"email": email, "password": password}).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/auth/login",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.load(response)


def xano_search(base_url, token, query, overdue):
    params = []
    if query:
        params.append(f"q={urllib.parse.quote(query)}")
    if overdue:
        params.append("overdue=true")
    url = f"{base_url}/subjects/search"
    if params:
        url += "?" + "&".join(params)
    request = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {token}"}
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.load(response)


def spec_rows():
    rows = []
    for path in sorted(Path("openspec/specs").glob("*/spec.md")):
        text = path.read_text(encoding="utf-8")
        rows.append(
            {
                "spec": path.parent.name,
                "requirements": text.count("### Requirement:"),
                "scenarios": text.count("#### Scenario:"),
            }
        )
    return rows


init_db()

st.set_page_config(
    page_title="EduTrack AI", page_icon=None, layout="wide", initial_sidebar_state="expanded"
)

st.markdown(
    """
<style>
  [data-testid="stAppViewContainer"] { background: #FFFFFF; }
  [data-testid="stSidebar"] { background: #8B0012; }
  [data-testid="stSidebar"] * { color: #FFFFFF !important; }
  [data-testid="stSidebar"] button { background-color: #FFFFFF !important; color: #8B0012 !important; }
  h1, h2, h3, h4 { color: #8B0012 !important; }
  label, [data-testid="stWidgetLabel"] p { color: #1A1312 !important; font-weight: 600; }
  input, textarea, select { color: #1A1312 !important; background-color: #FFFFFF !important; border: 1px solid #8B0012 !important; border-radius: 8px !important; }
  [data-testid="stTextInput"] > div,
  [data-testid="stNumberInput"] > div,
  [data-testid="stDateInput"] > div,
  [data-testid="stSelectbox"] > div { border-radius: 8px !important; }
  input::placeholder, textarea::placeholder { color: #7B6A67 !important; }
  [data-testid="stTabs"] [role="tab"] { color: #1A1312 !important; font-weight: 600; border-radius: 8px 8px 0 0 !important; }
  [data-testid="stTabs"] [aria-selected="true"] { color: #8B0012 !important; border-color: #C1121F !important; }
  div[data-testid="stMetricValue"] { color: #C1121F !important; }
  div[data-testid="stFormSubmitButton"] button,
  div[data-testid="stButton"] button { background-color: #C1121F !important; color: #FFFFFF !important; border: 1px solid #8B0012 !important; border-radius: 8px !important; }
  [data-testid="stContainer"] { border-radius: 12px !important; overflow: hidden; }
  div[data-testid="stAlert"] { color: #1A1312 !important; border-radius: 8px !important; }
</style>
""",
    unsafe_allow_html=True,
)

PASSWORD_TAB_JS = """
export default function(component) {
  if (window.__edutrackPasswordTabFix) return;
  window.__edutrackPasswordTabFix = true;

  const apply = () => {
    document.querySelectorAll('input[type="password"]').forEach((input) => {
      const wrapper = input.closest('[data-testid="stTextInput"]') || input.parentElement;
      if (!wrapper) return;
      wrapper.querySelectorAll('button').forEach((button) => {
        button.tabIndex = -1;
      });
    });
  };

  apply();
  const observer = new MutationObserver(apply);
  observer.observe(document.body, { childList: true, subtree: true });
}
"""

fix_password_tabs = st.components.v2.component(
    "edutrack_password_tab_fix",
    js=PASSWORD_TAB_JS,
)
fix_password_tabs(key="edutrack_password_tab_fix", height=0)

if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "username" not in st.session_state:
    st.session_state.username = ""

st.sidebar.title("EduTrack AI")
st.sidebar.caption("Gestão acadêmica · uso local")

if st.session_state.user_id is None:
    st.title("Acesso ao EduTrack AI")
    st.caption("Crie sua conta ou entre para cadastrar disciplinas, tarefas e acompanhar gráficos.")
    login_tab, register_tab = st.tabs(["Entrar", "Criar conta"])

    with login_tab:
        with st.form("login_form"):
            login_username = st.text_input("Usuário")
            login_password = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar"):
                account = find_user(login_username)
                if account and verify_password(login_password, account["password_hash"]):
                    st.session_state.user_id = account["id"]
                    st.session_state.username = account["username"]
                    st.rerun()
                else:
                    st.error("Usuário ou senha inválidos.")

    with register_tab:
        with st.form("register_form"):
            new_username = st.text_input("Novo usuário")
            new_password = st.text_input("Nova senha", type="password")
            confirm_password = st.text_input("Confirmar senha", type="password")
            if st.form_submit_button("Cadastrar"):
                if len(new_username.strip()) < 3:
                    st.error("Use pelo menos 3 caracteres no usuário.")
                elif len(new_password) < 6:
                    st.error("Use pelo menos 6 caracteres na senha.")
                elif new_password != confirm_password:
                    st.error("As senhas não conferem.")
                else:
                    new_id = create_user(new_username, new_password)
                    if new_id:
                        st.success("Conta criada. Faça login na aba Entrar.")
                    else:
                        st.error("Esse usuário já existe.")
    st.stop()

user_id = st.session_state.user_id
subjects = list_subjects(user_id)
tasks = list_tasks(user_id)
subject_names = {subject["id"]: subject["name"] for subject in subjects}

st.sidebar.write(f"Usuário: **{st.session_state.username}**")
st.sidebar.divider()
if st.sidebar.button("Sair"):
    st.session_state.user_id = None
    st.session_state.username = ""
    st.rerun()

if not get_welcome_seen(user_id):
    safe_username = html.escape(st.session_state.username)
    st.markdown(
        f"""
<div style="background:#8B0012;color:#FFFFFF;padding:32px;border-radius:16px;margin-bottom:24px;">
  <h1 style="color:#FFFFFF;margin:10px 0 8px;">Bem-vindo, {safe_username}!</h1>
  <p style="color:#FFFFFF;margin:0;max-width:720px;">Sua conta foi criada com sucesso. A partir de agora, seus dados ficam salvos neste dispositivo e você pode começar a organizar seus estudos.</p>
</div>
""",
        unsafe_allow_html=True,
    )
    st.subheader("Por onde começar")
    step_col_1, step_col_2, step_col_3 = st.columns(3)
    with step_col_1:
        st.markdown("**1. Disciplinas**")
        st.caption("Cadastre suas disciplinas, professor e carga horária.")
    with step_col_2:
        st.markdown("**2. Tarefas**")
        st.caption("Adicione tarefas, status e data de vencimento.")
    with step_col_3:
        st.markdown("**3. Gráficos**")
        st.caption("Acompanhe progresso, atrasos e tendências na Visão geral.")
    st.divider()
    if st.button("Começar a usar o EduTrack AI"):
        mark_welcome_seen(user_id)
        st.rerun()
    st.stop()

st.title("EduTrack AI")
st.caption("Seus dados, suas disciplinas, suas tarefas e seus indicadores.")

overdue = handle({"tasks": tasks, "subjects": subjects}, today=date.today())
completed = sum(1 for task in tasks if task["status"] == "completed")
percentage = calculate_progress(completed, len(tasks))["percentage"]

metric_col_1, metric_col_2, metric_col_3, metric_col_4 = st.columns(4)
metric_col_1.metric("Progresso geral", f"{percentage}%")
metric_col_2.metric("Disciplinas", len(subjects))
metric_col_3.metric("Tarefas", len(tasks))
metric_col_4.metric("Disciplinas em atraso", len(overdue["subjects"]))

overview_tab, subjects_tab, tasks_tab, specs_tab, xano_tab = st.tabs(
    ["Visão geral", "Disciplinas", "Tarefas", "OpenSpec", "Xano"]
)

with overview_tab:
    st.subheader("Indicadores")
    if tasks:
        status_counts = (
            pd.Series([task["status"] for task in tasks])
            .value_counts()
            .rename_axis("Status")
            .reset_index(name="Total")
        )
        st.bar_chart(status_counts.set_index("Status"))

        progress_rows = [
            {
                "Disciplina": subject["name"],
                "Progresso (%)": calculate_subject_progress(
                    [task for task in tasks if task["subject_id"] == subject["id"]]
                )["percentage"],
            }
            for subject in subjects
        ]
        if progress_rows:
            st.caption("Progresso por disciplina")
            st.bar_chart(pd.DataFrame(progress_rows).set_index("Disciplina"))

        timeline = pd.DataFrame(tasks).groupby("due_date").size().rename("Tarefas")
        st.caption("Tarefas por data de vencimento")
        st.line_chart(timeline)

        if overdue["subjects"]:
            overdue_rows = [
                {
                    "Disciplina": subject["name"],
                    "Vencidas": sum(
                        1
                        for task in tasks
                        if task["subject_id"] == subject["id"] and is_overdue_task(task)
                    ),
                }
                for subject in overdue["subjects"]
            ]
            st.caption("Disciplinas com tarefas vencidas")
            st.bar_chart(pd.DataFrame(overdue_rows).set_index("Disciplina"))
    else:
        st.info("Cadastre uma disciplina e uma tarefa para ver os gráficos.")

with subjects_tab:
    st.subheader("Nova disciplina")
    with st.form("subject_form"):
        subject_name = st.text_input("Nome da disciplina")
        subject_teacher = st.text_input("Professor(a)")
        subject_hours = st.number_input("Carga horária", min_value=1, max_value=200, value=4)
        if st.form_submit_button("Cadastrar disciplina"):
            if subject_name.strip() and subject_teacher.strip():
                add_subject(user_id, subject_name, subject_teacher, subject_hours)
                st.success("Disciplina cadastrada.")
                st.rerun()
            else:
                st.error("Preencha nome e professor.")

    st.subheader("Minhas disciplinas")
    if subjects:
        for subject in subjects:
            subject_tasks = [
                task for task in tasks if task["subject_id"] == subject["id"]
            ]
            percentage_subject = calculate_subject_progress(subject_tasks)["percentage"]
            with st.container(border=True):
                info_col, action_col = st.columns([4, 1])
                info_col.markdown(f"**{subject['name']}**")
                info_col.caption(
                    f"{subject['teacher']} · {subject['hours']}h · {percentage_subject}% concluído"
                )
                info_col.progress(percentage_subject / 100)
                if action_col.button("Excluir", key=f"delete-subject-{subject['id']}"):
                    delete_subject(user_id, subject["id"])
                    st.rerun()
    else:
        st.info("Nenhuma disciplina cadastrada.")

with tasks_tab:
    st.subheader("Nova tarefa")
    if subjects:
        with st.form("task_form"):
            selected_subject = st.selectbox(
                "Disciplina",
                options=[subject["id"] for subject in subjects],
                format_func=lambda subject_id: subject_names[subject_id],
            )
            task_title = st.text_input("Título da tarefa")
            task_status = st.selectbox("Status", options=["pending", "completed"])
            task_due_date = st.date_input("Vencimento", value=date.today())
            if st.form_submit_button("Cadastrar tarefa"):
                if task_title.strip():
                    add_task(
                        user_id,
                        selected_subject,
                        task_title,
                        task_status,
                        task_due_date,
                    )
                    st.success("Tarefa cadastrada.")
                    st.rerun()
                else:
                    st.error("Informe o título da tarefa.")
    else:
        st.warning("Cadastre uma disciplina antes de criar tarefas.")

    st.subheader("Minhas tarefas")
    if tasks:
        header_cols = st.columns([3, 2, 1, 1, 1, 1])
        header_cols[0].markdown("**Tarefa**")
        header_cols[1].markdown("**Disciplina**")
        header_cols[2].markdown("**Status**")
        header_cols[3].markdown("**Vencimento**")
        header_cols[4].markdown("**Atrasada**")
        header_cols[5].markdown("**Ações**")
        for task in tasks:
            cols = st.columns([3, 2, 1, 1, 1, 1])
            cols[0].write(task["title"])
            cols[1].write(subject_names.get(task["subject_id"], "—"))
            cols[2].write(task["status"])
            cols[3].write(task["due_date"])
            cols[4].write("sim" if is_overdue_task(task) else "não")
            action_label = "Concluir" if task["status"] == "pending" else "Reabrir"
            new_status = "completed" if task["status"] == "pending" else "pending"
            if cols[5].button(action_label, key=f"toggle-{task['id']}"):
                set_task_status(user_id, task["id"], new_status)
                st.rerun()
            if cols[5].button("Excluir", key=f"delete-task-{task['id']}"):
                delete_task(user_id, task["id"])
                st.rerun()
    else:
        st.info("Nenhuma tarefa cadastrada.")

with specs_tab:
    st.subheader("Especificações permanentes")
    st.dataframe(spec_rows(), hide_index=True)
    st.caption("Fonte: openspec/specs/*/spec.md")

with xano_tab:
    st.subheader("Integração Xano")
    st.info(
        "Este app usa SQLite local. Quando você fornecer token/credenciais, "
        "o adaptador Xano pode substituir a persistência sem mudar a interface."
    )
    st.text_input("Base URL", value=BASE_URL, disabled=True)
    st.code("POST /auth/login\nGET  /subjects/search?q=...&overdue=true", language="http")
    configured = bool(os.getenv("XANO_TOKEN") or secret("XANO_TOKEN"))
    st.write("Token configurado:", "sim" if configured else "não")

    with st.expander("Passo a passo detalhado no Xano"):
        st.markdown(
            "1. No Xano, abra o grupo **Autenticacao EduTrackIA Est** e rode "
            "`POST /auth/login` com `{\"email\":\"...\",\"password\":\"...\"}`.\n"
            "2. Copie o `authToken` da resposta sem mostrar em print.\n"
            "3. No Swagger, clique em **Authorize** e informe `Bearer <authToken>`.\n"
            "4. Execute `GET /subjects/search` com `q=Innovation`, depois com "
            "`overdue=true`, depois com ambos.\n"
            "5. Teste também sem token; deve retornar acesso negado.\n"
            "6. Salve os prints em `docs/evidencias/tarefa14/`."
        )
