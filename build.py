#!/usr/bin/env python3
"""Gera index.html e README.md a partir de resume.yaml (fonte única de verdade)."""
import html
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML é necessário: pip install pyyaml")

ROOT = Path(__file__).parent
DATA = yaml.safe_load((ROOT / "resume.yaml").read_text(encoding="utf-8"))
CSS = (ROOT / "assets" / "style.css").read_text(encoding="utf-8").rstrip("\n")

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{NAME}} — {{SUBTITLE}}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style>
__CSS__
  </style>
</head>"""

REPO_DOCS = """## Project Structure & PDF Generation

This repository uses a structured directory layout for managing resume versions tailored to different companies and roles.

### Project Layout
- [_base/](_base/) — Baseline LaTeX CVs in Portuguese ([Patrick_Serrano_CV_2026.tex](_base/Patrick_Serrano_CV_2026.tex)) and English ([Patrick_Serrano_CV_EN_2026.tex](_base/Patrick_Serrano_CV_EN_2026.tex)).
- [in-progress/](in-progress/) — Active applications and interview preparation materials (e.g. Arco Educação, Stone, Buzzlabs).
- [todo/](todo/) — Drafts, JD analyses, and target CV files for potential/upcoming candidacies (e.g. Brasil Paralelo, OLX, Globo).
- [archived/](archived/) — Older, unmaintained resume versions.

### Source of Truth
- [resume.yaml](resume.yaml) is the single source of truth for the web version ([index.html](index.html)) and [README.md](README.md).
- Regenerate them with:
  ```bash
  python3 build.py
  ```
- Check that the web source (`resume.yaml`) and the LaTeX sources (`_base/*.tex`) list the same experience entries:
  ```bash
  python3 consistency.py
  ```
  Both checks run in CI (job `check-generated`) and fail the build if the sources drift.

### How to Compile PDFs Locally
Because compiling LaTeX requires a large set of TeX packages and engines, you can compile any `.tex` file locally using Docker without needing to install TeX Live on your host system:

1. **Navigate** to the directory containing the `.tex` file you want to compile:
   ```bash
   cd todo/brasilparalelo
   ```
2. **Run the compiler** inside the `ghcr.io/xu-cheng/texlive-full` Docker container:
   ```bash
   docker run --rm -v "$(pwd)":/workdir -w /workdir ghcr.io/xu-cheng/texlive-full pdflatex Patrick_Serrano_CV_BrasilParalelo_2026.tex
   ```
   This compiles the `.tex` file and produces the output `.pdf` file in the same directory.

### Automation with GitHub Actions
When you push changes on the `master` branch to GitHub, the configured Actions workflow (defined in [.github/workflows/build-cv.yml](.github/workflows/build-cv.yml)) automatically compiles the configured `.tex` resume files and uploads them as workflow build artifacts.
"""

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────


def esc(text: str) -> str:
    """Escapa HTML preservando as tags <strong> permitidas no YAML."""
    return (
        html.escape(text, quote=False)
        .replace("&lt;strong&gt;", "<strong>")
        .replace("&lt;/strong&gt;", "</strong>")
    )


def title_parts(entry) -> tuple[str, str]:
    """Divide 'Nome — Empresa' em (nome, empresa)."""
    if " — " in entry["title"]:
        name, company = entry["title"].split(" — ", 1)
        return name, company
    return entry["title"], ""


def md_bold(text: str) -> str:
    """Converte o markup <strong> do YAML em **negrito** de Markdown."""
    return text.replace("<strong>", "**").replace("</strong>", "**")


# ─────────────────────────────────────────────────────────────────────────────
# README.md
# ─────────────────────────────────────────────────────────────────────────────

def render_readme(d: dict) -> str:
    n, ln, gh, mail = d["name"], d["linkedin"], d["github"], d["email"]
    out = []
    out.append(f"> Web version: [{d['site'].replace('https://', '')}]({d['site']})\n")
    out.append("<div align=\"center\">\n")
    out.append(f"# {n}\n")
    out.append(f"**{d['subtitle']}**\n")
    out.append(
        f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-{ln}-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/{ln})"
    )
    out.append(
        f"[![GitHub](https://img.shields.io/badge/GitHub-{gh}-181717?style=flat&logo=github&logoColor=white)](https://github.com/{gh})"
    )
    out.append(
        f"[![Email](https://img.shields.io/badge/Email-{mail.replace('@', '%40')}-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:{mail})"
    )
    out.append("\n</div>\n\n---\n")
    out.append(f"> {d['summary']}\n\n---\n")

    # Technical Profile
    out.append("## Technical Profile\n")
    out.append("| Area | Technologies |")
    out.append("|---|---|")
    for s in d["skills"]:
        out.append(f"| **{s['area']}** | {s['items']} |")
    out.append("\n---\n")

    # Experience
    out.append("## Professional Experience\n")
    for e in d["experience"]:
        name, company = title_parts(e)
        heading = f"{name} — {company}" if company else name
        out.append(f"### {heading}")
        out.append(f"**{e['role']}** &nbsp;·&nbsp; {e['date']}\n")
        out.append(f"{md_bold(e['description'])}\n")
        for b in e["bullets"]:
            out.append(f"- {md_bold(b)}")
        out.append("")
        out.append(" ".join(f"`{t}`" for t in e["tags"]))
        out.append("\n---\n")

    # Earlier experience
    out.append("<details>")
    out.append("<summary><strong>Earlier Experience (2018 – 2019)</strong></summary>\n")
    out.append("<br>\n")
    for e in d["earlier"]:
        out.append(f"**{e['title']}** — {md_bold(e['description'])}\n")
        out.append(" ".join(f"`{t}`" for t in e["tags"]))
        out.append("")
    out.append("</details>\n\n---\n")

    # Education
    out.append("## Education\n")
    for ed in d["education"]:
        if "date" in ed:
            out.append(f"**{ed['main']}** — {ed['sub']} &nbsp;·&nbsp; {ed['date']}\n")
        else:
            out.append(f"**{ed['main']}** — {ed['sub']}\n")
    out.append("---\n")

    # Languages
    out.append("## Languages\n")
    out.append("| Language | Level |")
    out.append("|---|---|")
    for lg in d["languages"]:
        out.append(f"| {lg['language']} | {lg['level']} |")
    out.append("\n---\n")

    # Repo docs (estático)
    out.append(REPO_DOCS)
    return "\n".join(out) + "\n"


# ─────────────────────────────────────────────────────────────────────────────
# index.html
# ─────────────────────────────────────────────────────────────────────────────

def render_html(d: dict) -> str:
    n = esc(d["name"])
    head = (
        HTML_HEAD.replace("{{NAME}}", n)
        .replace("{{SUBTITLE}}", esc(d["subtitle"]))
        .replace("__CSS__", CSS)
    )

    body = []
    body.append("\n<body>\n<div class=\"container\">\n")
    # Header
    body.append("  <!-- ── Header ── -->")
    body.append("  <header>")
    body.append(f"    <h1>{n}</h1>")
    body.append(f"    <p class=\"subtitle\">{esc(d['subtitle'])}</p>")
    body.append("    <nav class=\"header-links\">")
    body.append(
        f"      <a href=\"https://linkedin.com/in/{d['linkedin']}\" target=\"_blank\" rel=\"noopener\">\n"
        "        <svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z\"/></svg>\n        LinkedIn\n      </a>"
    )
    body.append(
        f"      <a href=\"https://github.com/{d['github']}\" target=\"_blank\" rel=\"noopener\">\n"
        "        <svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z\"/></svg>\n        GitHub\n      </a>"
    )
    body.append(
        f"      <a href=\"mailto:{d['email']}\">\n"
        "        <svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M0 3v18h24v-18h-24zm21.518 2l-9.518 7.713-9.518-7.713h19.036zm-19.518 14v-11.817l10 8.104 10-8.104v11.817h-20z\"/></svg>\n        Email\n      </a>"
    )
    body.append("    </nav>\n  </header>\n")

    # Summary
    body.append("  <!-- ── Summary ── -->")
    body.append("  <blockquote>")
    body.append(f"    {esc(d['summary'])}")
    body.append("  </blockquote>\n")

    # Skills
    body.append("  <!-- ── Technical Profile ── -->")
    body.append("  <section>")
    body.append("    <h2>Technical Profile</h2>")
    body.append("    <table class=\"skills-table\">")
    for s in d["skills"]:
        body.append(f"      <tr><td>{esc(s['area'])}</td><td>{esc(s['items'])}</td></tr>")
    body.append("    </table>\n  </section>\n")

    # Experience
    body.append("  <!-- ── Experience ── -->")
    body.append("  <section>")
    body.append("    <h2>Professional Experience</h2>\n")
    for e in d["experience"]:
        body.append("    <div class=\"entry\">")
        body.append("      <div class=\"entry-header\">")
        body.append(f"        <div class=\"entry-title\">{esc(e['title'])}</div>")
        body.append(f"        <div class=\"entry-meta\">{esc(e['role'])} &nbsp;·&nbsp; {esc(e['date'])}</div>")
        body.append("      </div>")
        body.append(f"      <p class=\"entry-description\">{esc(e['description'])}</p>")
        body.append("      <ul>")
        for b in e["bullets"]:
            body.append(f"        <li>{esc(b)}</li>")
        body.append("      </ul>")
        body.append("      <div class=\"tags\">")
        for t in e["tags"]:
            body.append(f"        <span class=\"tag\">{esc(t)}</span>")
        body.append("      </div>")
        body.append("    </div>\n")

    # Earlier experience
    body.append("    <details>")
    body.append("      <summary>Earlier Experience (2018 – 2019)</summary>")
    body.append("      <div class=\"details-body\">")
    for e in d["earlier"]:
        body.append("        <div class=\"entry\">")
        body.append("          <div class=\"entry-header\">")
        body.append(f"            <div class=\"entry-title\">{esc(e['title'])}</div>")
        body.append("          </div>")
        body.append(f"          <p class=\"entry-description\">{esc(e['description'])}</p>")
        body.append("          <div class=\"tags\">")
        for t in e["tags"]:
            body.append(f"            <span class=\"tag\">{esc(t)}</span>")
        body.append("          </div>")
        body.append("        </div>")
    body.append("      </div>")
    body.append("    </details>")
    body.append("  </section>\n")

    # Education
    body.append("  <!-- ── Education ── -->")
    body.append("  <section>")
    body.append("    <h2>Education</h2>")
    for ed in d["education"]:
        body.append("    <div class=\"edu-item\">")
        body.append("      <div>")
        main = esc(ed["main"])
        if "(incomplete)" in main:
            main = main.replace(
                "(incomplete)",
                "<span style=\"color:var(--text-muted);font-weight:400\">(incomplete)</span>",
            )
        if "date" in ed:
            body.append(f"        <div class=\"edu-main\">{main}</div>")
            body.append(f"        <div class=\"edu-sub\">{esc(ed['sub'])}</div>")
            body.append("      </div>")
            body.append(f"      <div class=\"edu-date\">{esc(ed['date'])}</div>")
        else:
            body.append(f"        <div class=\"edu-main\">{main}</div>")
            body.append(f"        <div class=\"edu-sub\">{esc(ed['sub'])}</div>")
            body.append("      </div>")
        body.append("    </div>")
    body.append("  </section>\n")

    # Languages
    body.append("  <!-- ── Languages ── -->")
    body.append("  <section>")
    body.append("    <h2>Languages</h2>")
    body.append("    <table class=\"lang-table\">")
    for lg in d["languages"]:
        body.append(f"      <tr><td>{esc(lg['language'])}</td><td>{esc(lg['level'])}</td></tr>")
    body.append("    </table>")
    body.append("  </section>\n")

    # Footer
    body.append("  <!-- ── Footer ── -->")
    body.append("  <footer>")
    body.append(
        f"    Source on <a href=\"https://github.com/{d['github']}/resume\" target=\"_blank\" rel=\"noopener\">GitHub</a>"
    )
    body.append("  </footer>\n")
    body.append("</div>\n</body>\n</html>\n")

    return head + "\n".join(body)


def main():
    (ROOT / "README.md").write_text(render_readme(DATA), encoding="utf-8")
    (ROOT / "index.html").write_text(render_html(DATA), encoding="utf-8")
    print("Gerados: README.md, index.html")


if __name__ == "__main__":
    main()
