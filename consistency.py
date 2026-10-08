#!/usr/bin/env python3
"""Checa consistência entre as fontes do currículo.

Compara o conjunto de entradas de experiência de:
  - resume.yaml          (fonte da versão web: index.html / README.md)
  - _base/*.tex  (PT e EN)  (fonte dos PDFs LaTeX)

As entradas aparecem com nomes diferentes em cada idioma, então o casamento é
feito por um slug canônico por projeto. Se uma entrada existir em uma fonte e
faltar em outra, o script falha (exit 1) — evitando lacunas silenciosas
(ex.: a entrada Rohana que faltava na versão web).
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML é necessário: pip install pyyaml")

ROOT = Path(__file__).parent
PT = ROOT / "_base" / "Patrick_Serrano_CV_2026.tex"
EN = ROOT / "_base" / "Patrick_Serrano_CV_EN_2026.tex"

# Slug canônico por projeto: casa a entrada do resume.yaml com a dos .tex,
# independentemente do idioma do título. As chaves são específicas de propósito
# (evitar falsos positivos por substring, ex.: "Ark" dentro de "Marketplace").
CANON = [
    # (slug, rótulo, substrings que identificam a entrada em cada título)
    ("neotek", "NeoTek / AI Factory", ["NeoTek", "AI Factory"]),
    ("rohana", "Rohana / Daelaam", ["Rohana", "Daelaam"]),
    ("ark", "Ark Streams", ["Ark Streams", "Ark Engine"]),
    ("octopus", "Octopus Pay", ["Octopus Pay"]),
    ("zougue", "Zougue / MPMS", ["Zougue", "MPMS"]),
]


def slug_of(title: str) -> str | None:
    for slug, _label, keys in CANON:
        if any(k.lower() in title.lower() for k in keys):
            return slug
    return None


def web_entries() -> dict[str, str]:
    data = yaml.safe_load((ROOT / "resume.yaml").read_text(encoding="utf-8"))
    out = {}
    for e in data["experience"]:
        s = slug_of(e["title"])
        if s:
            out[s] = e["title"]
    return out


def tex_entries(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    # \cventry{date}{title}{...}...
    out = {}
    for m in re.finditer(r"\\cventry\{[^}]*\}\{([^}]*)\}", text):
        title = m.group(1)
        s = slug_of(title)
        if s:
            out[s] = title
    return out


def main() -> int:
    web = web_entries()
    pt = tex_entries(PT)
    en = tex_entries(EN)

    problems = []
    for slug, label, _keys in CANON:
        present = {
            "resume.yaml": slug in web,
            "_base PT": slug in pt,
            "_base EN": slug in en,
        }
        missing = [src for src, ok in present.items() if not ok]
        if missing:
            problems.append((label, missing))

    if problems:
        print("::error::Fontes do currículo divergentes.")
        print("\nEntradas de experiência presentes em uma fonte e ausentes em outra:\n")
        for label, missing in problems:
            print(f"  • {label}  →  ausente em: {', '.join(missing)}")
        print("\nAtualize resume.yaml e _base/*.tex para manter as fontes em sincronia.")
        return 1

    print("Fontes consistentes: resume.yaml, _base PT e _base EN têm as mesmas entradas.")
    for slug, label, _keys in CANON:
        print(f"  ✓ {label}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
