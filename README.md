# ObraQuote — site público de apresentação

Página do projeto piloto ObraQuote: https://obraquote.netlify.app/

Contato para demonstrações: contato.obraquote@gmail.com

## O que este repositório contém

- `public/index.html`, `public/styles.css` e `public/script.js`: página responsiva.
- `public/site-config.js`: e-mail comercial público.
- `public/assets/`: imagens e vídeo fictícios de demonstração.
- `netlify.toml`: publica somente o diretório `public/`, mantendo os arquivos de testes e configuração fora do site.
- `tests/` e `.github/workflows/site-check.yml`: testes automáticos antes de atualizar o site.

O formulário de interesse usa **Netlify Forms**: envia os dados diretamente pelo navegador, sem abrir um aplicativo de e-mail. A Netlify armazena as solicitações para consulta no painel. O link de e-mail permanece como alternativa.

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

Abra `http://localhost:8000`. Confira responsividade, imagens, vídeo e botão de contato. Após ativar Netlify Forms, envie uma solicitação de teste no site publicado e confirme que aparece no painel Forms. Para receber alertas por e-mail, configure uma notificação para contato.obraquote@gmail.com.

## Segurança e privacidade

A versão piloto do aplicativo não é uma loja e não calcula impostos legais oficiais nem conversão de câmbio. Este repositório é público, então todo arquivo commitado poderá ser visto por outras pessoas. Não inclua informações reais de clientes ou custos internos de obras.


## Receber pedidos de demonstração via Netlify Forms

1. Na Netlify, abra o projeto **obraquote** e entre em **Forms**.
2. Ative **Enable form detection** antes do próximo deploy, se ainda não estiver ativado.
3. Publique esta alteração no GitHub (`main`). A Netlify fará o deploy e registrará o formulário `piloto-obraquote`.
4. Em **Forms > Submission notifications**, crie uma notificação de e-mail para `contato.obraquote@gmail.com` e confirme o endereço, se solicitado.
5. No site público, preencha nome, e-mail, atividade e mensagem com dados seus de teste. Clique em **Solicitar demonstração gratuita**.
6. A página `/obrigado.html` deve aparecer; confira também a nova entrada em **Forms > Submissions** e o e-mail de notificação.

**Privacidade:** ao contrário da versão antiga, agora há coleta e armazenamento dos dados enviados. Revise periodicamente os envios no painel da Netlify e exclua os que não forem mais necessários. Os dados se destinam apenas ao retorno da equipe ObraQuote.

**Atenção:** sem habilitar a detecção no painel e sem configurar notificações, não é possível garantir o recebimento de pedidos nem os alertas por e-mail. Não divulgue até concluir o teste de ponta a ponta.
