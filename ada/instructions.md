# Executando Ada localmente

* Instale o ngrok utilizando as instruções do [link](https://ngrok.com/download).

* No terminal, execute o ngrok na porta 5001:

```sh
./ngrok http 5001
```

* Faça a exportação das seguintes variáveis de ambiente:

```sh
export ACCESS_TOKEN="xxxxxxxxxx"
export BOT_NAME="xxxxx"
export WEBHOOK_URL="xxxxxxxx.ngrok.io/webhooks/telegram/webhook"
``` 

## Usando o Docker

* Execute os seguintes comandos:

```sh
docker-compose up --build
```