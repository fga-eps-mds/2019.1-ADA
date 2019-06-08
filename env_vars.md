## Setando variáveis de ambiente

##### Crie um bot no Telegram
Converse com o [@BotFather do Telegram](https://t.me/BotFather) e crie um bot de teste unicamente seu seguindo as instruções dele.


##### Exporte as variáveis do seu bot
Após escolher um nome para seu bot, o @BotFather lhe dará um token para utilizar para acessar a API do Telegram. Exporte ambos no terminal como a seguir. Substitua o TELEGRAM_ACESS_TOKEN pelo token lhe enviado pelo @BotFather e TELEGRAM_BOT_NAME pelo nome do seu bot.

```sh
export ACCESS_TOKEN='TELEGRAM_ACCESS_TOKEN'
export BOT_NAME='TELEGRAM_BOT_NAME'
```

##### Execute o ngrok
Conforme a seguir, execute o ngrok na porta 5001.

```sh
./ngrok http 5001
```

##### Exporte a URL do Webhook e conecte ao Telegram

Enquanto o ngrok estiver em execução, ele apresentará uma série de informações da sessão atual. Copie a primeira url do campo Forwarding, ela será similar à seguinte.

```sh
https://0x00000x.ngrok.io
```

Em seguida, exporte-a como a seguir, substituindo-a em NGROK_WEBHOOK_URL.


```sh
export WEBHOOK_URL='NGROK_WEBHOOK_URL'
```

::Lembre-se::: sempre que executar o ngrok essa url deve ser exportada.

Depois, você deve configurar essa url na api do telegram. Isso deve ser feito visitando um link específico para seu bot. Ele é da maneira a seguir. Não se esqueça de substituir TELEGRAM_ACESS_TOKEN e NGROK_WEBHOOK_URL.

```sh
http://api.telegram.org/botTELEGRAM_ACCESS_TOKEN/setWebhook?url=https://NGROK_WEBHOOK_URL/webhooks/telegram/webhook
```

Para verificar que tudo funcionou corretamente:

```sh
https://api.telegram.org/botTELEGRAM_ACCESS_TOKEN/getWebhookInfo
```

##### Exporte a variável de ambiente do GitLab
Siga as instruções em [ADA-gitlab ReadMe](https://github.com/fga-eps-mds/2019.1-ADA-gitlab) e depois rode o comando para obter as ids dos contêineres.
```sh
docker ps
```

Exporte o nome da imagem referente ao serviço do GitLab, tal como:
```sh
export GITLAB_SERVICE_URL='http://20191-ada-gitlab_api_1:5000/'
```

##### Exporte a variável de ambiente do Github
Siga as instruções em [ADA-github ReadMe](https://github.com/fga-eps-mds/2019.1-ADA-github) e depois rode o comando para obter as ids dos contêineres.
```sh
docker ps
```

Exporte o nome da imagem referente ao serviço do GitHub, tal como:
```sh
export GITLAB_SERVICE_URL='http://20191-ada-github_api_1:5000/'
```

##### Crie um OAuth App no github
Crie um OAuth app no github para a Ada realizar autenticação junto aos usuários, seguindo os passos a seguir:
- No seu perfil do github clique em **Developer Settings** > **OAuth Apps** e selecione **New OAuth app**.
- No formulário de registro do app, escolha o nome do seu app e preencha os campos **Homepage URL** com as urls ```http://localhost:5015/user``` e ```http://localhost:5000/user/gitlab/authorize``` respectivamente.
- Ao clicar em **Register application** o github irá retornar os tokens _Client id_ e _Client secret_.

Agora seu app está pronto.

Para maiores informações clique nesse [link da documentação do github](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/).


##### Exporte as variáveis do seu app
Após cadastrar um app o github irá disponibilizar dois tokens. Para a execução da Ada é necessário a exportação do Client ID gerado na criação do APP, além dessa variável também é preciso de exportar a variável utilizada no Authorization callback URL do app. Exporte ambos no terminal como a seguir. Substitua o CLIENT_ID pelo token gerado pelo GitHub na criação do app e a variável GITHUB_SIGNUP_URL pode ser mantida como no exemplo, conforme explicado acima.

```sh
export CLIENT_ID_GITHUB='CLIENT_ID'
export GITHUB_SIGNUP_URL=http://localhost:5015/user/github/authorize
```

##### Crie uma Application no gitlab
Crie uma application no gitlab para a Ada realizar autenticação junto aos usuários, seguindo os passos a seguir:
- No seu perfil do gitlab clique em **Profile Settings** > **Applications** e selecione **New Application**.
- No formulário de registro da aplicação, escolha o nome da sua aplicação e preencha o campo **Redirect URI** com a url ```http://localhost:5000/user/gitlab/authorize```.
- Dentre os scopes disponíveis, selecione _api_ e _read_user_
- Ao clicar em **Save application** o gitlab irá retornar os tokens _Application id_ e _Secret_.

Agora sua application está pronta.

Para maiores informações clique nesse [link da documentação do gitlab](https://docs.gitlab.com/ee/integration/oauth_provider.html#adding-an-application-through-the-profile).


##### Exporte as variáveis do seu app
Após cadastrar um application o gitlab irá disponibilizar dois tokens. Para a execução da Ada é necessário a exportação do Application ID gerado na criação do App, além dessa variável também é preciso de exportar a variável utilizada no Authorization callback URL do app. Exporte ambos no terminal como a seguir. Substitua o APPLICATION_ID pelo token gerado pelo GitLab na criação do app e a variável GITLAB_SIGNUP_URL pode ser mantida como no exemplo, conforme explicado acima.

```sh
export CLIENT_ID_GITLAB='APPLICATION_ID'
export GITLAB_SIGNUP_URL=http://localhost:5000/user/gitlab/authorize
```