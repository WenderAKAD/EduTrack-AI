#!/usr/bin/env python3
"""Gera docs/painel-status.html a partir dos arquivos do repositorio.

Fontes lidas:
  - README.md              (tabela de tarefas 01-16, status, PRs)
  - openspec/changes/*/tasks.md  (progresso da change ativa)
  - openspec/specs/         (specs permanentes)
  - openspec/changes/archive/    (changes arquivadas)
  - docs/tarefas/, docs/evidencias/, docs/pendencias-tecnicas.md
  - git (branch, ultimo commit, total de commits)

Uso:  python3 scripts/update_status_page.py
O hook .git/hooks/pre-commit executa este script a cada commit.
"""

from __future__ import annotations

import datetime as dt
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "painel-status.html"

TOTAL_TAREFAS = 16

# Fases do mapeamento do curso sobre as tarefas do README.
FASES = [
    ("Fase 1", "Fundacao: Git, VS Code e OpenSpec", list(range(1, 6))),
    ("Fase 2", "Design, Templates e FlutterFlow", [6, 7, 9]),
    ("Fase 3", "Planejamento: OpenSpec e AGENTS.md", [8, 10]),
    ("Fase 4", "Backend Xano (tabelas via XanoScript)", [11]),
    ("Fase 5", "Logica e integracao Python", [12]),
    ("Fase 6", "APIs REST e aplicacao completa", list(range(13, 17))),
]

# Tarefas ainda fora da tabela do README (a 13 aparece em docs/tarefas/tarefa12.md).
TAREFAS_FUTURAS = {
    13: ("Expor o calculo de progresso via API REST", "Aguardando"),
    14: ("A definir", "Aguardando"),
    15: ("A definir", "Aguardando"),
    16: ("A definir", "Aguardando"),
}


def git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(ROOT), *args],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return ""


def ler_tarefas_readme() -> dict[int, dict]:
    tarefas: dict[int, dict] = {}
    texto = (ROOT / "README.md").read_text(encoding="utf-8")
    for linha in texto.splitlines():
        m = re.match(r"^\|\s*(\d{2})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", linha)
        if not m:
            continue
        num = int(m.group(1))
        status = m.group(3)
        tarefas[num] = {
            "titulo": m.group(2),
            "status": status,
            "pr": m.group(4),
            "detalhe": f"docs/tarefas/tarefa{num:02d}.md",
        }
    for num, (titulo, status) in TAREFAS_FUTURAS.items():
        tarefas.setdefault(num, {"titulo": titulo, "status": status, "pr": "—", "detalhe": ""})
    return tarefas


def peso_status(status: str) -> float:
    s = status.lower()
    if "conclu" in s:
        return 1.0
    if "parcial" in s:
        return 0.5
    return 0.0


def classe_status(status: str) -> str:
    s = status.lower()
    if "conclu" in s:
        return "ok"
    if "parcial" in s:
        return "parcial"
    return "pendente"


def ler_changes_ativas() -> list[dict]:
    changes = []
    base = ROOT / "openspec" / "changes"
    for pasta in sorted(base.iterdir()) if base.exists() else []:
        if not pasta.is_dir() or pasta.name == "archive":
            continue
        tasks = pasta / "tasks.md"
        if not tasks.exists():
            continue
        blocos, atual = [], None
        for linha in tasks.read_text(encoding="utf-8").splitlines():
            cab = re.match(r"^##\s+\d+\.\s+(.+)$", linha)
            if cab:
                atual = {"titulo": cab.group(1).strip(), "feitas": 0, "total": 0, "itens": []}
                blocos.append(atual)
                continue
            box = re.match(r"^-\s+\[( |x)\]\s+(.+)$", linha)
            if box and atual is not None:
                atual["total"] += 1
                feita = box.group(1) == "x"
                atual["feitas"] += int(feita)
                atual["itens"].append({"texto": box.group(2).strip(), "feita": feita})
        blocos = [b for b in blocos if b["total"] > 0]
        feitas = sum(b["feitas"] for b in blocos)
        total = sum(b["total"] for b in blocos)
        changes.append({"id": pasta.name, "blocos": blocos, "feitas": feitas, "total": total})
    return changes


def estado_execucao(change: dict) -> str:
    tasks = ROOT / "openspec" / "changes" / change["id"] / "tasks.md"
    texto = tasks.read_text(encoding="utf-8")
    m = re.search(r"##\s+5\.\s+Estado de execu[cç][aã]o\s*(.*?)(?=\n##\s|\Z)", texto, re.DOTALL)
    if not m:
        return ""
    parags = [p.strip().replace("\n", " ") for p in m.group(1).split("\n\n") if p.strip()]
    return " ".join(parags[:1])


def status_openspec() -> dict:
    specs = sorted(p.name for p in (ROOT / "openspec" / "specs").iterdir() if p.is_dir()) \
        if (ROOT / "openspec" / "specs").exists() else []
    arquivo = ROOT / "openspec" / "changes" / "archive"
    arquivadas = sorted(p.name for p in arquivo.iterdir() if p.is_dir()) if arquivo.exists() else []
    return {"specs": specs, "arquivadas": arquivadas}


def pendencias() -> list[str]:
    caminho = ROOT / "docs" / "pendencias-tecnicas.md"
    if not caminho.exists():
        return []
    itens = []
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\d+\.\s+(.+)$", linha.strip())
        if m:
            itens.append(m.group(1).rstrip("."))
    return itens


def declaracao_readme() -> tuple[int, int] | None:
    texto = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"(\d+)\s+de\s+(\d+)\s+tarefas[^.\n]*conclu", texto)
    return (int(m.group(1)), int(m.group(2))) if m else None


def ler_bloqueios() -> list[str]:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"## Observações de transparência(.*?)## ", readme, re.DOTALL)
    if not m:
        return []
    return [
        re.sub(r"\s+", " ", l.strip())[2:].strip()
        for l in m.group(1).splitlines()
        if l.strip().startswith("- **")
    ]


def resumo_evidencias() -> tuple[int, int]:
    tarefas = list((ROOT / "docs" / "tarefas").glob("tarefa*.md")) if (ROOT / "docs" / "tarefas").exists() else []
    evid = [p for p in (ROOT / "docs" / "evidencias").iterdir() if p.is_dir()] \
        if (ROOT / "docs" / "evidencias").exists() else []
    return len(tarefas), len(evid)


def pct(x: float) -> int:
    return round(x * 100)


HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EduTrack AI — Painel de Status</title>
<style>
  :root {{
    --vermelho: #E10600; --vermelho-esc: #FF1E3C; --fundo: #0f1420;
    --card: #171e2e; --card-2: #1d2639; --texto: #e8ecf5; --suave: #9aa7bf;
    --ok: #2ecc71; --parcial: #f1c40f; --pend: #6c7a94;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
         background:var(--fundo); color:var(--texto); line-height:1.5; }}
  .wrap {{ max-width: 1080px; margin: 0 auto; padding: 28px 20px 60px; }}
  header.hero {{ background: linear-gradient(135deg, #1a2236 0%, #241016 60%, #3a0d10 100%);
    border-bottom: 3px solid var(--vermelho); border-radius: 16px; padding: 30px 26px; margin-bottom: 22px; }}
  header.hero h1 {{ margin:0 0 6px; font-size: 1.9rem; letter-spacing:-.5px; }}
  header.hero p {{ margin:0; color:var(--suave); font-size:.95rem; }}
  .badge {{ display:inline-block; background:var(--vermelho); color:#fff; font-weight:700;
    padding:3px 10px; border-radius:999px; font-size:.8rem; margin-top:12px; }}
  .stats {{ display:grid; grid-template-columns: repeat(auto-fit,minmax(150px,1fr)); gap:12px; margin-bottom:26px; }}
  .stat {{ background:var(--card); border:1px solid #232d44; border-radius:12px; padding:14px 16px; }}
  .stat .n {{ font-size:1.7rem; font-weight:800; }}
  .stat .l {{ color:var(--suave); font-size:.78rem; text-transform:uppercase; letter-spacing:.6px; }}
  h2 {{ font-size:1.05rem; margin:30px 0 12px; text-transform:uppercase; letter-spacing:1px;
    color:#cfd8ea; border-left:4px solid var(--vermelho); padding-left:10px; }}
  .bar-geral {{ background:var(--card); border:1px solid #232d44; border-radius:14px; padding:18px 20px; }}
  .track {{ background:#0c111c; border-radius:999px; height:22px; overflow:hidden; }}
  .fill {{ height:100%; background:linear-gradient(90deg,var(--vermelho),var(--vermelho-esc));
    display:flex; align-items:center; justify-content:flex-end; color:#fff; font-size:.72rem; font-weight:700;
    padding-right:8px; transition:width .5s; }}
  .faixa {{ display:flex; justify-content:space-between; color:var(--suave); font-size:.78rem; margin-top:6px; }}
  .fase {{ background:var(--card); border:1px solid #232d44; border-radius:12px; padding:14px 16px; margin-bottom:10px; }}
  .fase .topo {{ display:flex; justify-content:space-between; align-items:center; gap:10px; }}
  .fase .nome {{ font-weight:700; font-size:.95rem; }}
  .fase .nome span {{ color:var(--suave); font-weight:400; }}
  .fase .mini {{ background:#0c111c; height:10px; border-radius:999px; margin-top:10px; overflow:hidden; }}
  .fase .mini i {{ display:block; height:100%; background:var(--vermelho); }}
  .chip {{ font-size:.7rem; font-weight:700; padding:2px 9px; border-radius:999px; white-space:nowrap; }}
  .chip.ok {{ background:rgba(46,204,113,.15); color:var(--ok); border:1px solid rgba(46,204,113,.4); }}
  .chip.parcial {{ background:rgba(241,196,15,.14); color:var(--parcial); border:1px solid rgba(241,196,15,.4); }}
  .chip.pendente {{ background:rgba(108,122,148,.16); color:var(--suave); border:1px solid #33405c; }}
  table {{ width:100%; border-collapse:collapse; background:var(--card); border-radius:12px; overflow:hidden;
    border:1px solid #232d44; font-size:.87rem; }}
  th, td {{ padding:9px 12px; text-align:left; border-bottom:1px solid #222c42; }}
  th {{ background:var(--card-2); font-size:.72rem; text-transform:uppercase; letter-spacing:.7px; color:var(--suave); }}
  tr:last-child td {{ border-bottom:none; }}
  td.num {{ font-weight:700; color:var(--suave); width:44px; }}
  a {{ color:var(--vermelho-esc); }}
  .bloco {{ background:var(--card); border:1px solid #232d44; border-radius:12px; padding:14px 16px; margin-bottom:10px; }}
  .bloco h3 {{ margin:0 0 8px; font-size:.95rem; display:flex; justify-content:space-between; gap:10px; }}
  .bloco ul {{ margin:6px 0 0; padding-left:0; list-style:none; }}
  .bloco li {{ padding:3px 0 3px 22px; position:relative; font-size:.85rem; color:#c6cfe2; }}
  .bloco li::before {{ position:absolute; left:0; top:3px; width:15px; height:15px; border-radius:4px;
    font-size:.7rem; display:flex; align-items:center; justify-content:center; font-weight:700; }}
  .bloco li.feita::before {{ content:"✓"; background:rgba(46,204,113,.18); color:var(--ok); border:1px solid var(--ok); }}
  .bloco li.aberta::before {{ content:"·"; background:#0c111c; color:var(--suave); border:1px solid #33405c; }}
  .lista {{ background:var(--card); border:1px solid #232d44; border-radius:12px; padding:8px 16px; margin:0; }}
  .lista li {{ padding:7px 0; border-bottom:1px solid #222c42; font-size:.87rem; color:#c6cfe2; }}
  .lista li:last-child {{ border-bottom:none; }}
  .tags {{ display:flex; flex-wrap:wrap; gap:8px; }}
  .tag {{ background:var(--card-2); border:1px solid #2b3757; color:#cfd8ea; font-size:.78rem;
    padding:5px 11px; border-radius:8px; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
  footer {{ margin-top:34px; color:var(--suave); font-size:.78rem; text-align:center; border-top:1px solid #222c42;
    padding-top:16px; }}
  .nota {{ background:var(--card); border-left:3px solid var(--parcial); border-radius:0 10px 10px 0;
    padding:12px 16px; color:#c6cfe2; font-size:.86rem; margin-top:10px; }}
</style>
</head>
<body>
<div class="wrap">

  <header class="hero">
    <h1>EduTrack AI — Painel de Status</h1>
    <p>Assistente educacional · Innovation Lab · Faculdade Impacta · Wender Araújo Santos</p>
    <span class="badge">Etapa: {etapa}</span>
  </header>

  <div class="stats">
    <div class="stat"><div class="n">{feitas}/{total}</div><div class="l">{lbl_tarefas}</div></div>
    <div class="stat"><div class="n">{geral_pct}%</div><div class="l">Progresso geral</div></div>
    <div class="stat"><div class="n">{n_specs}</div><div class="l">Specs permanentes</div></div>
    <div class="stat"><div class="n">{n_arquivadas}</div><div class="l">Changes arquivadas</div></div>
    <div class="stat"><div class="n">{n_changes}</div><div class="l">Change ativa</div></div>
    <div class="stat"><div class="n">{prs}</div><div class="l">Pull requests</div></div>
  </div>

  <div class="bar-geral">
    <div class="track"><div class="fill" style="width:{geral_pct}%">{geral_pct}%</div></div>
    <div class="faixa"><span>Tarefa 01</span><span>{etapa_legenda}</span><span>Tarefa 16</span></div>
    {nota_divergencia}
  </div>

  <h2>Fases do projeto</h2>
  {fases_html}

  <h2>Tarefas</h2>
  <table>
    <thead><tr><th>#</th><th>Tarefa</th><th>Status</th><th>PR</th></tr></thead>
    <tbody>{linhas_tabela}</tbody>
  </table>

  <h2>Change OpenSpec ativa</h2>
  {changes_html}

  <h2>Especificações permanentes</h2>
  <div class="tags">{spec_tags}</div>

  <h2>Bloqueios e transparência</h2>
  <ul class="lista">{bloqueios}</ul>

  <h2>Pendências técnicas</h2>
  <ul class="lista">{pendencias}</ul>

  <h2>Repositório</h2>
  <div class="bloco">
    <ul class="lista" style="border:none;background:transparent;padding:0">
      <li><strong>Branch:</strong> {branch} &nbsp;·&nbsp; <strong>Commits:</strong> {commits}</li>
      <li><strong>Último commit:</strong> {ultimo_commit}</li>
      <li><strong>Documentação:</strong> {n_tarefas_doc} guias em <code>docs/tarefas/</code> · {n_evid} pastas de evidência</li>
    </ul>
  </div>

  <footer>
    Gerado automaticamente por <code>scripts/update_status_page.py</code> em {agora}.<br>
    Este arquivo é recriado a cada commit (hook <code>pre-commit</code>) — não edite manualmente.
  </footer>
</div>
</body>
</html>
"""


def main() -> None:
    tarefas = ler_tarefas_readme()
    changes = ler_changes_ativas()
    oss = status_openspec()
    pend = pendencias()
    bloqueios_lista = ler_bloqueios()
    n_tarefas_doc, n_evid = resumo_evidencias()

    feitas = sum(1 for t in tarefas.values() if peso_status(t["status"]) == 1.0)
    total = max(TOTAL_TAREFAS, len(tarefas))
    pontos = sum(peso_status(t["status"]) for t in tarefas.values())
    geral_pct = pct(pontos / total)
    parcial = [n for n, t in tarefas.items() if classe_status(t["status"]) == "parcial"]
    etapa = (
        f"{feitas} de {total} tarefas concluídas"
        + (f" · Tarefa {parcial[0]:02d} parcial" if parcial else "")
        + (f" · {len(changes)} change ativa" if changes else " · sem changes ativas")
    )
    etapa_legenda = "APIs REST e app completo" if geral_pct < 100 else "Entrega final"

    decl = declaracao_readme()
    if decl and decl[0] != feitas and parcial:
        nota_divergencia = (
            f'<div class="nota"><strong>Nota de consistência:</strong> o texto do README declara '
            f'<strong>{decl[0]} de {decl[1]}</strong> tarefas concluídas, mas a própria tabela marca a '
            f'Tarefa {parcial[0]:02d} como <em>parcial</em>. Este painel usa a tabela: '
            f'{feitas} concluídas + {len(parcial)} '
            f'{"parcial" if len(parcial) == 1 else "parciais"} = {geral_pct}% do total.</div>'
        )
    else:
        nota_divergencia = ""

    lbl_tarefas = "Tarefas concluídas"
    if parcial:
        plural = "eis" if len(parcial) != 1 else ""
        lbl_tarefas = f"Tarefas concluídas · {len(parcial)} parcial{plural}"

    # Fases
    fases_html = []
    for cod, nome, nums in FASES:
        itens = [tarefas[n] for n in nums if n in tarefas]
        if not itens:
            continue
        p = sum(peso_status(t["status"]) for t in itens) / len(itens)
        todos_ok = all(peso_status(t["status"]) == 1.0 for t in itens)
        if todos_ok:
            chip = '<span class="chip ok">concluída</span>'
        elif p > 0:
            chip = '<span class="chip parcial">em andamento</span>'
        else:
            chip = '<span class="chip pendente">a iniciar</span>'
        nums_txt = ", ".join(f"{n:02d}" for n in nums)
        fases_html.append(
            f'<div class="fase"><div class="topo">'
            f'<div class="nome">{cod}: {nome} <span>· tarefas {nums_txt}</span></div>{chip}</div>'
            f'<div class="mini"><i style="width:{pct(p)}%"></i></div></div>'
        )
    fases_html = "\n".join(fases_html)

    # Tabela de tarefas
    linhas = []
    for n in sorted(tarefas):
        t = tarefas[n]
        cls = classe_status(t["status"])
        detalhe = (
            f'<a href="../{t["detalhe"]}">detalhe</a>' if t["detalhe"] and (ROOT / t["detalhe"]).exists() else "—"
        )
        linhas.append(
            f'<tr><td class="num">{n:02d}</td><td>{t["titulo"]}<br>'
            f'<span style="color:var(--suave);font-size:.76rem">{detalhe}</span></td>'
            f'<td><span class="chip {cls}">{t["status"].lower()}</span></td>'
            f'<td>{t["pr"]}</td></tr>'
        )
    linhas_tabela = "\n".join(linhas)

    # Changes ativas
    changes_html = []
    for ch in changes:
        c_pct = pct(ch["feitas"] / ch["total"]) if ch["total"] else 0
        blocos = []
        for b in ch["blocos"]:
            itens = "".join(
                f'<li class="{"feita" if i["feita"] else "aberta"}">{i["texto"]}</li>'
                for i in b["itens"]
            )
            blocos.append(
                f'<div class="bloco"><h3>{b["titulo"]}'
                f'<span class="chip {"ok" if b["feitas"] == b["total"] else "parcial"}">'
                f'{b["feitas"]}/{b["total"]}</span></h3><ul>{itens}</ul></div>'
            )
        nota = estado_execucao(ch)
        nota_html = f'<div class="nota"><strong>Estado de execução:</strong> {nota}</div>' if nota else ""
        changes_html.append(
            f'<div class="fase"><div class="topo"><div class="nome">{ch["id"]}</div>'
            f'<span class="chip {"ok" if c_pct == 100 else "parcial"}">{ch["feitas"]}/{ch["total"]} tasks · {c_pct}%</span></div>'
            f'<div class="mini"><i style="width:{c_pct}%"></i></div></div>'
            + "".join(blocos) + nota_html
        )
    changes_html = "\n".join(changes_html) or '<div class="nota">Nenhuma change ativa.</div>'

    spec_tags = "".join(f'<span class="tag">{s}</span>' for s in oss["specs"]) or "—"
    bloqueios_html = "".join(f"<li>{b}</li>" for b in bloqueios_lista) or "<li>—</li>"
    pend_html = "".join(f"<li>{p}</li>" for p in pend) or "<li>—</li>"

    branch = git("rev-parse", "--abbrev-ref", "HEAD") or "—"
    commits = git("rev-list", "--count", "HEAD") or "0"
    ultimo = git("log", "-1", "--format=%h · %ad · %s", "--date=short") or "—"
    prs = len({p.strip() for t in tarefas.values() for p in re.findall(r"#\d+", t["pr"])})

    html = HTML.format(
        etapa=etapa,
        lbl_tarefas=lbl_tarefas,
        nota_divergencia=nota_divergencia,
        feitas=feitas, total=total, geral_pct=geral_pct,
        n_specs=len(oss["specs"]), n_arquivadas=len(oss["arquivadas"]),
        n_changes=len(changes), prs=prs,
        etapa_legenda=etapa_legenda,
        fases_html=fases_html, linhas_tabela=linhas_tabela, changes_html=changes_html,
        spec_tags=spec_tags, bloqueios=bloqueios_html, pendencias=pend_html,
        branch=branch, commits=commits, ultimo_commit=ultimo,
        n_tarefas_doc=n_tarefas_doc, n_evid=n_evid,
        agora=dt.datetime.now().strftime("%d/%m/%Y %H:%M"),
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Painel gerado: {OUT.relative_to(ROOT)} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
