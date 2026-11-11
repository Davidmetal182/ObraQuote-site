# ObraQuote — site público de apresentação

Página do projeto piloto ObraQuote: https://obraquote.netlify.app/

Contato para demonstrações: contato.obraquote@gmail.com

## O que este repositório contém

- `public/index.html`, `public/styles.css` e `public/script.js`: página responsiva.
- `public/site-config.js`: e-mail comercial público.
- `public/assets/`: imagens e vídeo fictícios de demonstração.
- `netlify.toml`: publica somente o diretório `public/`, mantendo os arquivos de testes e configuração fora do site.
- `tests/` e `.github/workflows/site-check.yml`: testes automáticos antes de atualizar o site.

O formulário **abre o programa de e-mail do visitante** com uma mensagem pronta (`mailto:`). Ele não envia mensagens sem a confirmação da pessoa nem armazena dados num servidor.

## Publicação inicial via GitHub (Windows / PowerShell)

O repositório público `Davidmetal182/ObraQuote-site` já foi criado, vazio. O aplicativo `Davidmetal182/ObraQuote` é separado e privado.

1. Baixe o ZIP preparado para o site e extraia-o em uma pasta dedicada, por exemplo `C:\Users\julio\Desktop\ObraQuote-site`.
2. Abra o PowerShell na pasta onde aparecem `public`, `tests`, `netlify.toml` e `README.md`.
3. Execute:

```powershell
git init -b main
python -m unittest discover -s tests -v
git add .
git commit -m "feat: site publico ObraQuote"
git remote add origin https://github.com/Davidmetal182/ObraQuote-site.git
git push -u origin main
```

Verifique em https://github.com/Davidmetal182/ObraQuote-site que os arquivos aparecem. **Nunca envie os arquivos do aplicativo privado, orçamentos de clientes, senhas, tokens ou `.env`.**

## Conectar o repositório ao projeto Netlify existente

Use o projeto já publicado `obraquote`; **não crie outro projeto Netlify**. No painel Netlify, encontre **Project configuration → Developer settings → Continuous deployment → Repository → Link repository**, escolha o GitHub e **apenas** `Davidmetal182/ObraQuote-site` na instalação do GitHub App, quando solicitado.

Se a Netlify apresentar a autorização OAuth antiga pedindo leitura e escrita em **todos** os repositórios, cancele e escolha a integração via GitHub App com acesso restrito; não é necessário autorizar o acesso indiscriminado aos projetos privados.

Ao configurar o deploy:

- Branch de produção: `main`.
- Build command: deixar vazio.
- Publish directory: `public` (também definido em `netlify.toml`).
- Projeto Netlify: `obraquote` existente.

Depois de vincular, faça um pequeno commit de texto e confirme no painel **Deploys** se o site foi atualizado.

## Verificação local

```powershell
python -m unittest discover -s tests -v
cd public
python -m http.server 8000
```

Abra `http://localhost:8000`. Confira responsividade, imagens, vídeo e botão de contato. Faça um envio de e-mail de teste para confirmar o recebimento.

## Segurança e privacidade

A versão piloto do aplicativo não é uma loja e não calcula impostos legais oficiais nem conversão de câmbio. Este repositório é público, então todo arquivo commitado poderá ser visto por outras pessoas. Não inclua informações reais de clientes ou custos internos de obras.
