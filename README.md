# Site — icaj.com.br

Site institucional de **Isaias Carlos de Azevedo Júnior**, Advogado, OAB/MG 244.358. O site está publicado em **https://icaj.com.br** pelo GitHub Pages.

## Arquivos

| Arquivo | Função |
|---|---|
| `index.html` | O site: página única com estilos e script embutidos (inclui QR Code, salvar contato e formulário) |
| `404.html` | Página mostrada quando alguém acessa um endereço inexistente |
| `fonts/` | Fontes do site (Source Serif 4 e Source Sans 3), servidas daqui, sem depender do Google |
| `assets/` | Logotipos em vetor: `logo-azul.svg`, `logo-branco.svg` e `monograma.svg` (sigla). Use-os em qualquer material |
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

- **E-mail:** o site não exibe e-mail; as mensagens do formulário chegam ao e-mail cadastrado no Web3Forms. Para voltar a exibir um endereço, preencha a linha `<meta name="contato-email" content="">` perto do início do `index.html` (o site o espalha para o contato, o rodapé, o QR Code e o "Salvar contato"), sem rodar nenhum script.
- **Telefone/WhatsApp:** aparece nos links `wa.me` do `index.html`, na variável `PHONE` do script (depois rode o `atualizar_csp.py`) e no bloco `application/ld+json`.
- Atualize também o cartão impresso.

## Formulário de contato (Web3Forms)

As mensagens do formulário chegam por e-mail pelo serviço Web3Forms (plano gratuito, 250 envios por mês), na conta criada com o e-mail de contato.

- A chave fica no atributo `data-w3f-key` da tag `<form id="contactForm">` no `index.html`. Ela é pública; trocar a chave não exige rodar nenhum script.
- A política de segurança (CSP) libera apenas `https://api.web3forms.com` para o envio.
- O serviço só aceita envios feitos do navegador dos visitantes; testes a partir de servidores são recusados.
- Se as mensagens caírem no lixo eletrônico, marque-as como "não é lixo eletrônico".

## Estatísticas de visitas (Cloudflare Web Analytics)

Gratuito, sem cookies e sem coleta de dados pessoais (dispensa aviso de cookies).

- Ativar ou trocar o token: `python3 scripts/ativar_estatisticas.py TOKEN`
- Desativar: `python3 scripts/ativar_estatisticas.py --remover`

O script insere o código da Cloudflare antes de `</body>` e ajusta a política de
segurança (CSP) só para `static.cloudflareinsights.com` e `cloudflareinsights.com`.
O token aparece no código da página e não é senha. Os números ficam em
dash.cloudflare.com → Analytics & Logs → Web Analytics.

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
- não menciona cargo, emprego ou função, atual ou anterior (Código de Ética, art. 44, §2º);
- não usa expressões persuasivas, de autoengrandecimento ou de comparação, nem anuncia especialidade sem título (Provimento 205/2021, art. 3º);
- mantém tom informativo e sóbrio.

Revise esses pontos antes de qualquer mudança de texto.

---

© 2026 Isaias Carlos de Azevedo Júnior. Todos os direitos reservados.
