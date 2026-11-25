# Cartão digital — icaj.com.br

Cartão de visitas digital de **Isaias Carlos de Azevedo Júnior**, Advogado, OAB/MG 244.358. O site está publicado em **https://icaj.com.br** pelo GitHub Pages.

## Arquivos

| Arquivo | Função |
|---|---|
| `index.html` | O cartão: página única com estilos e script embutidos |
| `404.html` | Página mostrada quando alguém acessa um endereço inexistente |
| `fonts/` | Fontes do site (Inter, Plus Jakarta Sans e IBM Plex Mono), servidas daqui, sem depender do Google |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` | Ícones da aba do navegador e da tela inicial do celular |
| `site.webmanifest` | Dados para "Adicionar à tela inicial" |
| `og-image.jpg` | Imagem que aparece ao compartilhar o link no WhatsApp e em redes sociais (1200 × 630) |
| `robots.txt`, `sitemap.xml` | Orientações para buscadores |
| `CNAME` | Domínio próprio `icaj.com.br`. **Não apague.** |
| `.nojekyll` | Faz o GitHub publicar os arquivos como estão |
| `scripts/atualizar_csp.py` | Recalcula a política de segurança depois de mudanças no script |

## Como editar

1. Abra o arquivo no GitHub, clique no ícone de lápis, faça a alteração e clique em **Commit changes**.
2. O site atualiza em cerca de 1 minuto, no mesmo endereço. O QR Code impresso continua valendo.

### Atenção ao editar o script

O `index.html` tem uma política de segurança (Content-Security-Policy) que só deixa rodar **exatamente** o script atual. Mudar textos, links e estilos fora do bloco `<script>…</script>` não exige nada. Se o bloco `<script>` for alterado, os botões param de funcionar até a política ser atualizada. Para atualizar, rode na pasta do repositório:

```
python3 scripts/atualizar_csp.py
```

e envie o `index.html` atualizado. O bloco `<script type="application/ld+json">`, com os dados para o Google, não é afetado.

### Ao mudar dados de contato

Atualize todos estes lugares, para que fiquem iguais:
- os botões e a barra de e-mail no `index.html`;
- os vCards `COMPACT_VCARD` e `FULL_VCARD` no script, e depois rode o `atualizar_csp.py`;
- o bloco `application/ld+json` no início do `index.html`;
- o cartão impresso.

## Configuração que não deve ser alterada

- **O repositório precisa ser público.** No plano gratuito, um repositório privado tira o site do ar.
- **GitHub, em Settings > Pages:** "Deploy from a branch", depois `main` e `/ (root)`. Domínio `icaj.com.br`, com **Enforce HTTPS** marcado.
- **DNS no Registro.br, modo avançado:**

| Tipo | Nome | Valor |
|---|---|---|
| A | icaj.com.br | 185.199.108.153 |
| A | icaj.com.br | 185.199.109.153 |
| A | icaj.com.br | 185.199.110.153 |
| A | icaj.com.br | 185.199.111.153 |
| CNAME | www.icaj.com.br | iscjunior-design.github.io |

- **Segurança:** mantenha a verificação em duas etapas ativa no GitHub e no Registro.br, e a renovação automática do domínio ligada. O domínio vence em 24/11/2027.

## Publicidade da advocacia

O conteúdo segue o Estatuto da OAB, o Código de Ética e Disciplina e o Provimento 205/2021:
- não divulga outra atividade em conjunto com a advocacia;
- não menciona cargo, emprego ou função;
- mantém tom informativo e sóbrio.

Revise esses pontos antes de qualquer mudança de texto.

---

© 2026 Isaias Carlos de Azevedo Júnior. Todos os direitos reservados.
