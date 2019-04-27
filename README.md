# ADA

[![pipeline status](https://gitlab.com/adabot/ada/badges/devel/pipeline.svg)](https://gitlab.com/adabot/ada/commits/devel) [![Percentage of issues still open](http://isitmaintained.com/badge/open/fga-eps-mds/2019.1-ADA.svg)](http://isitmaintained.com/project/fga-eps-mds/2019.1-ADA "Percentage of issues still open") [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Sobre a Ada  

<p align="justify"> &emsp;&emsp;
  A Ada é um chatbot com objetivo de facilitar a transformação full-stack e a integração entre equipes multidisciplinares em organizações envolvidas com desenvolvimento de software. Isso é obtido através de dois aspectos principais: comunicação fácil e em linguagem natural e monitoramento completo do pipeline de produção de softwares. Além de monitorar o pipeline, a Ada também permite a realização de uma série de atividades relacionadas ao gerenciamento da produção nas plataformas entregues. Sua versão básica inclui suporte para um pipeline GitHub, GitLab CI e Amazon e comunicação através do Telegram. </p>

## Contribuindo

### Guia de Contribuição

Para contribuir com o projeto, temos um [Guia de Contribuição Inicial](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CONTRIBUTING.md).

### Políticas

As políticas de _[branches](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/branches)_, _[commits](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/commits)_, _[pull requests](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/pull_request)_ e _[issues](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/issues)_ se encontram [aqui](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/policies).

### Código de Conduta

O código de conduta para contribuição está disponível [aqui](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CODE_OF_CONDUCT.md)

### Desenvolvimento

#### Primeiros passos

#### Primeiros passos
##### Instale o Docker
Seguindo as instruções dos links a seguir, instale o docker conforme seu sistema operacional.

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/#install-compose) (já incluído na instalação do Docker Desktop para MacOS)

#### Subir a Ada no Telegram
Siga esses passos para executar a Ada utilizando o Telegram através de um bot criado por você.

##### Crie um bot no Telegram
Converse com o [@BotFather do Telegram](https://t.me/BotFather) e crie um bot de teste unicamente seu seguindo as instruções dele.


##### Exporte as variáveis do seu bot
Após escolher um nome para seu bot, o @BotFather lhe dará um token para utilizar para acessar a API do Telegram. Exporte ambos no terminal como a seguir. Substitua o TELEGRAM_ACESS_TOKEN pelo token lhe enviado pelo @BotFather e TELEGRAM_BOT_NAME pelo nome do seu bot.

```sh
- export ACCESS_TOKEN='TELEGRAM_ACCESS_TOKEN'
- export BOT_NAME='TELEGRAM_BOT_NAME'
```

##### Instale o ngrok
Utilizando as instruções do [link](https://ngrok.com/download), faça a instalação do ngrok.

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
- export WEBHOOK_URL='NGROK_WEBHOOK_URL'
```

::Lembre-se::: sempre que executar o ngrok essa url deve ser exportada.

Depois, você deve configurar essa url na api do telegram. Isso deve ser feito visitando um link específico para seu bot. Ele é da maneira a seguir. Não se esqueça de substituir TELEGRAM_ACESS_TOKEN e NGROK_WEBHOOK_URL.

```sh
- http://api.telegram.org/botTELEGRAM_ACCESS_TOKEN/setWebhook?url=https://NGROK_WEBHOOK_URL/webhooks/telegram/webhook
```

Para verifica que tudo funcionou corretamente:

```sh
- https://api.telegram.org/botTELEGRAM_ACCESS_TOKEN/getWebhookInfo
```

##### Execute o Docker
```sh
docker-compose -f docker-compose-dev.yml up --build
```

##### Converse com o bot
E está tudo pronto pra conversar com o bot no telegram!

#### Subir a Ada no Terminal
Siga esses passos para executar a Ada localmente utilizando o Terminal.

##### Execute o comando a seguir para criar a imagem do container

```sh
docker-compose -f docker-compose-dev.yml up --build
```

##### Execute o Docker
Após criar a imagem do container, em um outro terminal, digite o seguinte comando para obter a id de seus contêineres.

```sh
docker ps
```

Copie o CONTAINER_ID  da imagem 20191-ada_ada e substitui no comando a seguir.

```sh
docker exec -it container_id bash
```

Após rodar esse comando, o container estará em execução. Algo como a seguir aparecerá no terminal.
```sh
root@00x00xx00000:/ada#
```

Dentro dele, rode o comando para treinar o bot.

```sh
python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml
```

Após executar esse comando, é possível conversar com o bot bem como visualizar os logs do Rasa.


## Equipe

| Nome | Papel | GitHub | Email |
| --- | --- | --- | --- |
| Ateldy Borges Brasil Filho | Scrum Master | ateldyfilho | ateldybfilho@gmail.com |
| Bruno Oliveira Dantas | Arquiteto de Software | Brunooliveiradantas | oliveiradantas96@gmail.com |
| João Vitor Ramos de Souza | DevOps | joaovitor3 | joaovytor0@gmail.com |
| Vítor Gomes | Product Owner | vitorandos | torandoing@gmail.com |
| Caio Vinicius Fernandes de Araújo | Desenvolvedor | caiovfernandes | caiovf13@gmail.com |
| Erick Giffoni Felicíssimo | Desenvolvedor | ErickGiffoni | giffoni.erick@gmail.com |
| Guilherme Mendes Pereira | Desenvolvedor | guilherme-mendes | guimendesp12@gmail.com |
| João Pedro José Santos da Silva Guedes | Desenvolvedor | sudjoao | isudjoao@gmail.com |
| Lucas Fellipe Carvalho Moreira | Desenvolvedor | lucasfcm9 | lucasfcm9@gmail.com |

## Licença

[GPL](https://opensource.org/licenses/GPL-3.0)


<p align="center"><b>Grupo 3</b></p>
<p align="center">Engenharia de Produto de <i>Software</i> (EPS) / Métodos de Desenvolvimento de <i>Software</i> (MDS)<br /><br />
<p align="center">2019</p>
<a href="https://fga.unb.br" target="_blank"><img width="230"src="https://4.bp.blogspot.com/-0aa6fAFnSnA/VzICtBQgciI/AAAAAAAARn4/SxVsQPFNeE0fxkCPVgMWbhd5qIEAYCMbwCLcB/s1600/unb-gama.png"></a>
</p>
