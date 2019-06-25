![Ada_logo_horizontal](https://user-images.githubusercontent.com/22121504/56839465-006c8200-6859-11e9-8feb-ad76c573b844.png)

[![pipeline status](https://gitlab.com/adabot/ada/badges/master/pipeline.svg)](https://gitlab.com/adabot/ada/commits/master) [![Percentage of issues still open](http://isitmaintained.com/badge/open/fga-eps-mds/2019.1-ADA.svg)](http://isitmaintained.com/project/fga-eps-mds/2019.1-ADA "Percentage of issues still open") [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Maintainability](https://api.codeclimate.com/v1/badges/87b77c0a20222afea5d0/maintainability)](https://codeclimate.com/github/fga-eps-mds/2019.1-ADA/maintainability)

## Sobre a Ada  

<p align="justify"> &emsp;&emsp;
  A Ada é um chatbot com objetivo de facilitar a transformação full-stack e a integração entre equipes multidisciplinares em organizações envolvidas com desenvolvimento de software. Esse objetivo é concretizado por meio  de dois aspectos principais: comunicação fácil e em linguagem natural e monitoramento completo do pipeline de produção de softwares. Além de monitorar o pipeline, a Ada também permite a realização de uma série de atividades relacionadas ao gerenciamento da produção nas plataformas entregues. A Ada, em sua versão básica, inclui suporte para um pipeline GitHub com GitLab CI. Além disso, nessa versão a comunicação entre a Ada e o usuário ocorre através do Telegram. </p>

## Contribuindo

### Guia de Contribuição

Para contribuir com o projeto, temos um [Guia de Contribuição Inicial](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CONTRIBUTING.md).

### Políticas

As políticas de _[branches](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/branches)_, _[commits](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/commits)_, _[pull requests](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/pull_request)_ e _[issues](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/issues)_ se encontram [aqui](https://fga-eps-mds.github.io/2019.1-ADA/#/docs/policies/policies).

### Código de Conduta

O código de conduta para contribuição está disponível [aqui](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CODE_OF_CONDUCT.md).

### Desenvolvimento

#### Primeiros passos
##### Instale o Docker
Seguindo as instruções dos links a seguir, instale o docker conforme seu sistema operacional.

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/#install-compose) (já incluído na instalação do Docker Desktop para MacOS)

#### Subir a Ada no Telegram
Siga esses passos para executar a Ada utilizando o Telegram através de um bot criado por você.

##### Instale o ngrok
Utilizando as instruções do [link](https://ngrok.com/download), faça a instalação do ngrok.

##### Execute o ngrok
Conforme a seguir, execute o ngrok na porta 5001.

```sh
./ngrok http 5001
```

#### Exporte as variáveis de ambiente
Exporte as variáveis de ambiente conforme as instruções presentes nesse [documento](/env_vars.md).
 
<strong><em>Antes de seguir adiante. Importante:</strong></em> As variáveis de ambiente são necessárias para o correto funcionamento do bot, por isso não esqueça de exportá-las.


##### Execute o Docker
```sh
docker-compose up --build
```


##### Converse com o bot
E está tudo pronto pra conversar com o bot no telegram!

#### Subir a Ada no Terminal
Siga esses passos para executar a Ada localmente utilizando o Terminal.

##### Execute o comando a seguir para criar a imagem do container

```sh
docker-compose up --build
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


<p align="center"><b>Grupo 3</b></p>
<p align="center">Engenharia de Produto de <i>Software</i> (EPS) / Métodos de Desenvolvimento de <i>Software</i> (MDS)<br /><br />
<p align="center">2019</p>
<a href="https://fga.unb.br" target="_blank"><img width="230"src="https://4.bp.blogspot.com/-0aa6fAFnSnA/VzICtBQgciI/AAAAAAAARn4/SxVsQPFNeE0fxkCPVgMWbhd5qIEAYCMbwCLcB/s1600/unb-gama.png"></a>
</p>
