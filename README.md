# ADA

## Sobre o Projeto   

<p align="justify"> &emsp;&emsp;
  O projeto ADA tem como objetivo facilitar o gerenciamento de tarefas dentro de um projeto de desenvolvimento de software, sobretudo aquelas relacionadas ao papel de DevOps. A partir de um acesso rápido a informações através do bot no Telegram e possibilidade de realização de algumas tarefas através dele, diminui-se o esforço e tempo necessários para manter o projeto em organizado e em funcionamento.</p>

### Requisitos de Alto Nível
* Interação através de linguagem natural para uma melhor usabilidade;
* Fluxos de conversas objetivos e práticos;
* Gerenciamento de issues e pull requests;
* Captura de informações sobre a release;
* Captura de informações sobre integração contínua do repositório;
* Captura de informações sobre deploy contínuo do repositório;
* Gerenciamento do pipeline de produção.

## Contribuindo

### Guia de Contribuição

Para contribuir com o projeto, temos um [Guia de Contribuição Inicial](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CONTRIBUTING.md).

### Políticas

As políticas de _[branches](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/branches)_, _[commits](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/commits)_, _[pull requests](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/pull_request)_ e _[issues](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/issues)_ se encontram [aqui](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/policies).

### Código de Conduta

O código de conduta para contribuição está disponível [aqui](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CODE_OF_CONDUCT.md)

### Desenvolvimento

#### Subindo o chatbot no mensageiro

Para executar a Ada utilizando o Telegram, siga os seguintes comandos:

* Instale o ngrok utilizando as instruções do [link](https://ngrok.com/download).

* No terminal, execute o ngrok na porta 5001:

```sh
./ngrok http 5001
```

* Faça a exportação das seguintes variáveis de ambiente:

```sh
- export ACCESS_TOKEN='TELEGRAM_ACCESS_TOKEN'
- export BOT_NAME='BOT_NAME'
- export WEBHOOK_URL='WEBHOOK_URL'
``` 

Faça as instalações dos seguintes programas:

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/#install-compose)

Usando o Docker

* Execute o comando para inicializar o container em seu computador:

```sh
docker-compose -f docker-compose-dev.yml up --build
```

#### Subindo o chatbot no Terminal

Para executar a Ada localmente utilizando o Terminal, siga os comandos:

* Execute o comando para criar a imagem do container:

```sh
docker-compose -f docker-compose-dev.yml up --build
```

* Execute o Docker:

```sh
docker exec -it container_id bash
```

* Rode os comandos para o treinamento do bot:

```sh
python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml
```
Após os comando é possível realizar diálogos com o bot e visualizar os logs do Rasa.

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