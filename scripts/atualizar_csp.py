#!/usr/bin/env python3
"""Recalcula o hash do script do cartão e atualiza a política de segurança (CSP).

Uso (na pasta do repositório):  python3 scripts/atualizar_csp.py
Rode sempre que editar o trecho entre <script> e </script> do index.html;
sem isso, o navegador bloqueia o script e os botões param de funcionar.
"""
import base64, hashlib, pathlib, re, sys

arquivo = pathlib.Path(__file__).resolve().parent.parent / "index.html"
html = arquivo.read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
if len(scripts) != 1:
    sys.exit(f"Esperava 1 script executável em index.html, encontrei {len(scripts)}.")
novo = "sha256-" + base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode()
html2, n = re.subn(r"script-src 'sha256-[^']+'", f"script-src '{novo}'", html)
if n != 1:
    sys.exit("Não encontrei a diretiva script-src na política de segurança.")
if html2 == html:
    print("A política já estava atualizada.")
else:
    arquivo.write_text(html2, encoding="utf-8")
    print("Política de segurança atualizada:", novo)
