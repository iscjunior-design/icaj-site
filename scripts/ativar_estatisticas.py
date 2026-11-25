#!/usr/bin/env python3
"""Ativa ou remove o Cloudflare Web Analytics no index.html.

Uso:
  python3 scripts/ativar_estatisticas.py TOKEN     # ativa (ou troca o token)
  python3 scripts/ativar_estatisticas.py --remover # desativa

O token fica visível no código da página (é público por natureza) e
não é senha. O script também ajusta a política de segurança (CSP) para
permitir somente o script e o envio de dados da Cloudflare.
"""
import pathlib
import re
import sys

ARQ = pathlib.Path(__file__).resolve().parent.parent / "index.html"
INI, FIM = "<!-- estatisticas:inicio -->", "<!-- estatisticas:fim -->"
SCRIPT_HOST = "https://static.cloudflareinsights.com"
DADOS_HOST = "https://cloudflareinsights.com"


def ajustar_csp(html: str, ativar: bool) -> str:
    m = re.search(r'(http-equiv="Content-Security-Policy"\s+content=")([^"]*)(")', html)
    if not m:
        sys.exit("CSP não encontrada no index.html")
    diretivas = [d.strip() for d in m.group(2).split(";") if d.strip()]
    novas = []
    for d in diretivas:
        nome, *valores = d.split()
        valores = [v for v in valores if v not in (SCRIPT_HOST, DADOS_HOST)]
        if nome == "script-src" and ativar:
            valores.append(SCRIPT_HOST)
        if nome == "connect-src":
            valores = [v for v in valores if v != "'none'"]
            if ativar:
                valores.append(DADOS_HOST)
            if not valores:
                valores = ["'none'"]
        novas.append(" ".join([nome] + valores))
    return html[: m.start(2)] + "; ".join(novas) + html[m.end(2):]


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    html = ARQ.read_text(encoding="utf-8")
    html = re.sub(r"\n?\s*" + re.escape(INI) + r".*?" + re.escape(FIM), "", html, flags=re.S)
    ativar = sys.argv[1] != "--remover"
    if ativar:
        token = sys.argv[1].strip()
        if not re.fullmatch(r"[0-9a-fA-F]{32}", token):
            sys.exit("Token inválido: deve ter 32 caracteres (0-9, a-f).")
        trecho = (
            f"  {INI}\n"
            f"  <script defer src=\"{SCRIPT_HOST}/beacon.min.js\" "
            f"data-cf-beacon='{{\"token\": \"{token}\"}}'></script>\n"
            f"  {FIM}\n"
        )
        if html.count("</body>") != 1:
            sys.exit("</body> não encontrado uma única vez")
        html = html.replace("</body>", trecho + "</body>")
    html = ajustar_csp(html, ativar)
    ARQ.write_text(html, encoding="utf-8")
    print("Estatísticas " + ("ativadas." if ativar else "removidas."))


if __name__ == "__main__":
    main()
