# Contributing guidelines

Thank you for taking the time to contribute! :tada:

## What should I know before I get started?

Please make sure to read our [READ_ME](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/README.md) in order to get to know more about our project, system requirements and how to build the system.

Make sure to read our [Code of conduct](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CODE_OF_CONDUCT.md) as well.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please refer to the list of open issues, someone may have already reported it.
When creating a bug report, please provide as much information as possible:

* Your title should be clear and descriptive
* Describe the steps to reproduce the bug
* Tell us what was expected and what happened that didn't go as such
* Include any images or screenshots that could help to identify the problem
* If the problem isn't related to any specific action, explain what you were doing at the time it happened
* Say which OS you are using
* Say which version of the system you encountered this bug

### Suggesting Enhancements

Before suggesting an enhancement, please refer to the list of open issues, someone may have already suggested it.
When suggesting an enhancement, please provide as much information as possible:

* Your title should be clear and descriptive
* Describe how the enhancement would work step by step and how it would take place
* Provide examples
* Include any images or screenshots that could help elucidate the enhancement
* Explain why the enhancement would be useful
* Say which OS you are using
* Say which version of the system you encountered this bug

### How do I run Ada?
#### First steps
##### Install Docker
Check the following links for information on how to install Docker according to your operational system.

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/#install-compose) (already included when installing Docker Desktop for MacOS)

#### Running Ada on Telegram
Follow these steps to run Ada on Telegram through a bot created by you.

##### Create a bot on Telegram
Chat with  [@BotFather on Telegram](https://t.me/BotFather) and create a test bot unique to you following its instructions.

##### Export bot variables
After choosing a name for your bot, @BotFather is gonna give a token that can be used to access Telegram’s API. Export both on a terminal as follows. Replace TELEGRAM_ACESS_TOKEN with the token given to you by the @BotFather and TELEGRAM_BOT_NAME with your bot’s name.

```sh
- export ACCESS_TOKEN='TELEGRAM_ACCESS_TOKEN'
- export BOT_NAME='TELEGRAM_BOT_NAME'
```

##### Install ngrok
Check this [link](https://ngrok.com/download) for information on how to install ngrok.

##### Run ngrok
Run ngrok on port 5001 as follows.

```sh
./ngrok http 5001
```

##### Export the Webhook’s URL and connect to Telegram

On the terminal ngrok is running, some information about the current session is shown. Copy the url on the field Forwarding, it is similar to the following one.

```sh
https://0x00000x.ngrok.io
```

Next, export it as follow, replacing it on NGROK_WEBHOOK_URL.

```sh
- export WEBHOOK_URL='NGROK_WEBHOOK_URL'
```

::Remember::: every time you run ngrok this url changes and must be exported again.

Afterwards, you must set this url on telegram. This is done by visiting an url specific to your bot. It is as follows. Do not forget to replace TELEGRAM_ACESS_TOKEN and NGROK_WEBHOOK_URL.

```sh
- http://api.telegram.org/botTELEGRAM_ACCESS_TOKEN/setWebhook?url=https://NGROK_WEBHOOK_URL/webhooks/telegram/webhook
```

To check that it worked successfully you can visit:

```sh
- https://api.telegram.org/botTELEGRAM_ACCESS_TOKEN/getWebhookInfo
```

##### Run Docker
```sh
docker-compose up --build
```

##### Chat with the bot
And everything’s ready to begin your conversation with the bot on telegram!

#### Running Ada on a Terminal
Follow these steps to run Ada locally using a terminal.

##### Run the following command to create the container image

```sh
docker-compose up --build
```

##### Run Docker
After creating the container image, in another terminal, type the following command to get your containers’ ids.

```sh
docker ps
```

Copy the CONTAINER_ID  of the image 20191-ada_ada and replace it on the following command.

```sh
docker exec -it container_id bash
```

After running this command, the container will be in execution. Something as follows is gonna appear on your terminal.
```sh
root@00x00xx00000:/ada#
```

Inside it, run the command to train the bot.

```sh
python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml
```

After running this command, it is possible to chat with the bot as well as check the logs from Rasa.

## Templates

In order to make any contribution, please refer to our templates:

* [Issue template](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/.github/ISSUE_TEMPLATE/issue-template.md)
* [Pull request template](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/pull_request_template.md)
* [Template for commits](https://github.com/fga-eps-mds/2019.1-ADA/)
