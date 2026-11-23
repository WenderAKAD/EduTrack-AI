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


def xano_send_verification_code(base_url, email):
    body = json.dumps({"email": email.strip().lower()}).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/auth/send-verification-code",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, json.load(response)
    except urllib.error.HTTPError as err:
        try:
            err_data = json.loads(err.read().decode("utf-8"))
            msg = err_data.get("message") or err_data.get("error") or f"Erro {err.code}"
        except Exception:
            msg = f"Erro {err.code}: {err.reason}"
        return False, msg
    except Exception as exc:
        return False, str(exc)


def xano_signup(base_url, name, email, password, verification_code):
    body = json.dumps(
        {
            "name": name.strip(),
            "email": email.strip().lower(),
            "password": password,
            "verification_code": verification_code.strip(),
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/auth/signup",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, json.load(response)
    except urllib.error.HTTPError as err:
        try:
            err_data = json.loads(err.read().decode("utf-8"))
            msg = err_data.get("message") or err_data.get("error") or f"Erro {err.code}"
        except Exception:
            msg = f"Erro {err.code}: {err.reason}"
        return False, msg
    except Exception as exc:
        return False, str(exc)


def xano_login(base_url, email, password):
    body = json.dumps({"email": email.strip().lower(), "password": password}).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/auth/login",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return True, json.load(response)
    except urllib.error.HTTPError as err:
        try:
            err_data = json.loads(err.read().decode("utf-8"))
            msg = err_data.get("message") or err_data.get("error") or "Credenciais inválidas no Xano."
        except Exception:
            msg = f"Erro {err.code}: {err.reason}"
        return False, msg
    except Exception as exc:
        return False, str(exc)


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

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

THEME = {
    "bg": "#FFFFFF",
    "surface": "#F7F4F3",
    "border": "#EADFDC",
    "text": "#1A1312",
    "muted": "#7B6A67",
    "heading": "#8B0012",
    "primary": "#C1121F",
    "sidebar": "#8B0012",
    "sidebar_text": "#FFFFFF",
    "sidebar_button_bg": "#FFFFFF",
    "sidebar_button_text": "#8B0012",
} if not st.session_state.dark_mode else {
    "bg": "#0A0A0A",
    "surface": "#16181C",
    "border": "#2A2D33",
    "text": "#F2F3F5",
    "muted": "#9AA0A6",
    "heading": "#FF1E3C",
    "primary": "#FF1E3C",
    "sidebar": "#101215",
    "sidebar_text": "#F2F3F5",
    "sidebar_button_bg": "#E10600",
    "sidebar_button_text": "#FFFFFF",
}

st.markdown(
    f"""
<style>
  [data-testid="stAppViewContainer"] {{ background: {THEME["bg"]}; }}
  [data-testid="stSidebar"] {{ background: {THEME["sidebar"]}; }}
  [data-testid="stSidebar"] * {{ color: {THEME["sidebar_text"]} !important; }}
  [data-testid="stSidebar"] button {{ background-color: {THEME["sidebar_button_bg"]} !important; color: {THEME["sidebar_button_text"]} !important; }}
  [data-testid="stSidebarCollapseButton"] button,
  [data-testid="stExpandSidebarButton"] button {{ background: transparent !important; border: none !important; font-size: 0 !important; }}
  [data-testid="stSidebarCollapseButton"] button::after {{ content: "«"; font-size: 22px; color: {THEME["sidebar_text"]}; }}
  [data-testid="stExpandSidebarButton"] button::after {{ content: "»"; font-size: 22px; color: {THEME["muted"]}; }}
  h1, h2, h3, h4 {{ color: {THEME["heading"]} !important; }}
  label, [data-testid="stWidgetLabel"] p {{ color: {THEME["text"]} !important; font-weight: 600; }}
  input, textarea, select {{ color: {THEME["text"]} !important; background-color: {THEME["bg"]} !important; border: 1px solid {THEME["heading"]} !important; border-radius: 8px !important; }}
  [data-testid="stTextInput"] > div,
  [data-testid="stNumberInput"] > div,
  [data-testid="stDateInput"] > div,
  [data-testid="stSelectbox"] > div {{ border-radius: 8px !important; }}
  input::placeholder, textarea::placeholder {{ color: {THEME["muted"]} !important; }}
  [data-testid="stTabs"] [role="tab"] {{ color: {THEME["text"]} !important; font-weight: 600; border-radius: 8px 8px 0 0 !important; }}
  [data-testid="stTabs"] [aria-selected="true"] {{ color: {THEME["heading"]} !important; border-color: {THEME["primary"]} !important; }}
  div[data-testid="stMetricValue"] {{ color: {THEME["primary"]} !important; }}
  div[data-testid="stFormSubmitButton"] button,
  div[data-testid="stButton"] button {{ background-color: {THEME["primary"]} !important; color: #FFFFFF !important; border: 1px solid {THEME["heading"]} !important; border-radius: 8px !important; }}
  [data-testid="stContainer"] {{ background-color: {THEME["surface"]} !important; border: 1px solid {THEME["border"]} !important; border-radius: 12px !important; overflow: hidden; }}
  div[data-testid="stAlert"] {{ color: {THEME["text"]} !important; border-radius: 8px !important; }}
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

@st.cache_resource
def get_password_tab_component():
    return st.components.v2.component(
        "edutrack_password_tab_fix",
        js=PASSWORD_TAB_JS,
    )


fix_password_tabs = get_password_tab_component()
fix_password_tabs(key="edutrack_password_tab_fix", height=0)

LOGIN_SUGGEST_JS = """
export default function(component) {
  const KEY = 'edutrack_saved_logins';

  const read = () => {
    try {
      const value = JSON.parse(localStorage.getItem(KEY) || '[]');
      return Array.isArray(value) ? value : [];
    } catch (error) {
      return [];
    }
  };

  const write = (values) => localStorage.setItem(KEY, JSON.stringify(values));

  if (component.data && component.data.save) {
    const values = read();
    if (!values.includes(component.data.save)) {
      values.push(component.data.save);
      write(values.slice(-10));
    }
    component.setTriggerValue('saved', component.data.save);
  }

  let observer = window.__edutrackLoginObserver;

  const apply = () => {
    if (observer) observer.disconnect();

    const values = read();
    let datalist = document.getElementById('edutrack-login-emails');
    if (!datalist) {
      datalist = document.createElement('datalist');
      datalist.id = 'edutrack-login-emails';
      document.body.appendChild(datalist);
    }
    datalist.innerHTML = '';
    values.forEach((value) => {
      const option = document.createElement('option');
      option.value = value;
      datalist.appendChild(option);
    });

    document.querySelectorAll('input[type="text"]').forEach((input) => {
      const form = input.closest('[data-testid="stForm"]');
      if (!form) return;
      const passwords = form.querySelectorAll('input[type="password"]');
      if (passwords.length !== 1) return;
      input.setAttribute('list', 'edutrack-login-emails');
      input.setAttribute('autocomplete', 'off');
    });

    document.querySelectorAll('input[type="password"]').forEach((input) => {
      input.setAttribute('autocomplete', 'new-password');
      input.setAttribute('data-lpignore', 'true');
      input.setAttribute('data-1p-ignore', 'true');
    });

    if (observer) observer.observe(document.body, { childList: true, subtree: true });
  };

  apply();
  if (!observer) {
    observer = new MutationObserver(apply);
    window.__edutrackLoginObserver = observer;
    observer.observe(document.body, { childList: true, subtree: true });
  }
}
"""

def clear_pending_saved_login():
    st.session_state.pending_saved_login = ""


@st.cache_resource
def get_login_suggestions_component():
    return st.components.v2.component(
        "edutrack_login_suggestions",
        js=LOGIN_SUGGEST_JS,
    )


login_suggestions = get_login_suggestions_component()
login_suggestions(
    data={"save": st.session_state.get("pending_saved_login", "")},
    on_saved_change=clear_pending_saved_login,
    key="edutrack_login_suggestions",
    height=0,
)

if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "username" not in st.session_state:
    st.session_state.username = ""
if "pending_saved_login" not in st.session_state:
    st.session_state.pending_saved_login = ""

st.sidebar.title("EduTrack AI")
st.sidebar.caption("Gestão acadêmica · uso local")
st.sidebar.toggle("Modo escuro", key="dark_mode")

if st.session_state.user_id is None:
    st.title("Acesso ao EduTrack AI")
    st.caption("Crie sua conta com verificação por e-mail ou entre para cadastrar disciplinas e tarefas no Xano.")
    login_tab, register_tab = st.tabs(["Entrar", "Criar conta (com verificação por e-mail)"])

    with login_tab:
        with st.form("login_form"):
            login_username = st.text_input("E-mail ou Usuário")
            login_password = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar"):
                # Tenta autenticar no backend Xano primeiro
                ok, res = xano_login(BASE_URL, login_username, login_password)
                if ok and isinstance(res, dict) and "authToken" in res:
                    st.session_state.auth_token = res["authToken"]
                    # Sincroniza conta no cache SQLite local para compatibilidade
                    local_acc = find_user(login_username)
                    if not local_acc:
                        uid = create_user(login_username, login_password)
                    else:
                        uid = local_acc["id"]
                    st.session_state.user_id = uid
                    st.session_state.username = login_username.strip().lower()
                    st.session_state.pending_saved_login = login_username.strip().lower()
                    st.rerun()
                else:
                    # Fallback local se o Xano ainda não foi atualizado ou offline
                    account = find_user(login_username)
                    if account and verify_password(login_password, account["password_hash"]):
                        st.session_state.user_id = account["id"]
                        st.session_state.username = account["username"]
                        st.session_state.pending_saved_login = account["username"]
                        st.rerun()
                    else:
                        err_msg = res if not ok else "Usuário ou senha inválidos."
                        st.error(f"Falha no login: {err_msg}")

    with register_tab:
        st.markdown("#### 1. Verificação de E-mail")
        email_col1, email_col2 = st.columns([3, 1])
        with email_col1:
            verify_email = st.text_input("E-mail para cadastro", key="reg_email_input")
        with email_col2:
            st.write("")
            st.write("")
            send_code_btn = st.button("Enviar código", key="btn_send_code")

        if send_code_btn:
            if "@" not in verify_email or "." not in verify_email:
                st.error("Informe um e-mail válido para receber o código.")
            else:
                ok, res = xano_send_verification_code(BASE_URL, verify_email)
                if ok:
                    st.session_state.verify_email_sent = verify_email.strip().lower()
                    code_info = f" (Código gerado: **{res.get('code')}**)" if isinstance(res, dict) and res.get("code") else ""
                    st.success(f"Código de verificação enviado para {verify_email}!{code_info}")
                else:
                    dev_code = str(secrets.randbelow(900000) + 100000)
                    st.session_state.dev_verification_code = dev_code
                    st.session_state.verify_email_sent = verify_email.strip().lower()
                    st.info(f"Modo Dev/Simulação (Xano pendente de push): Código gerado: **{dev_code}**")

        st.markdown("#### 2. Dados da Conta e Confirmação do Código")
        with st.form("register_form"):
            new_name = st.text_input("Nome completo")
            new_code = st.text_input("Código de verificação (6 dígitos)")
            new_password = st.text_input("Nova senha (mínimo 8 caracteres)", type="password")
            confirm_password = st.text_input("Confirmar senha", type="password")

            if st.form_submit_button("Cadastrar no Xano"):
                target_email = st.session_state.get("verify_email_sent") or verify_email.strip().lower()
                if not target_email or "@" not in target_email:
                    st.error("Informe o e-mail e clique em 'Enviar código' primeiro.")
                elif len(new_code.strip()) != 6:
                    st.error("O código de verificação deve ter exatamente 6 dígitos.")
                elif len(new_name.strip()) < 2:
                    st.error("Informe seu nome completo.")
                elif len(new_password) < 8:
                    st.error("A senha deve ter pelo menos 8 caracteres (requisito do Xano).")
                elif new_password != confirm_password:
                    st.error("As senhas não conferem.")
                else:
                    ok, res = xano_signup(BASE_URL, new_name, target_email, new_password, new_code)
                    if ok and isinstance(res, dict) and "authToken" in res:
                        st.session_state.auth_token = res["authToken"]
                        local_id = create_user(target_email, new_password)
                        st.session_state.pending_saved_login = target_email
                        st.success("Conta criada e verificada com sucesso no Xano! Faça login na aba Entrar.")
                    else:
                        dev_code = st.session_state.get("dev_verification_code")
                        if dev_code and new_code.strip() == dev_code:
                            local_id = create_user(target_email, new_password)
                            st.session_state.pending_saved_login = target_email
                            st.success("Conta criada com código verificado! (Lembre-se de rodar xano workspace push para habilitar no Xano remoto).")
                        else:
                            st.error(f"Erro na criação da conta: {res}")
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
<div style="background:{THEME["sidebar"]};color:{THEME["sidebar_text"]};padding:32px;border-radius:16px;margin-bottom:24px;">
  <h1 style="color:{THEME["sidebar_text"]};margin:10px 0 8px;">Bem-vindo, {safe_username}!</h1>
  <p style="color:{THEME["sidebar_text"]};margin:0;max-width:720px;">Sua conta foi criada com sucesso. A partir de agora, seus dados ficam salvos neste dispositivo e você pode começar a organizar seus estudos.</p>
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
