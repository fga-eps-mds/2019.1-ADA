# Gitflow

| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
|28/03/2019|1.0|Criação da versão inicial do gitflow | João Vitor |
|06/04/2019|2.0|Criação da versão inicial do gitflow | João Vitor |

## 1. Visão Geral

Foi idealizado um _Gitflow_ (fluxo de trabalho) automatizado visando entregas de funcionalidade mais rápidas e de mais qualidade.

O fluxo de trabalho contará com 3 estágios de verificação até o envio do serviço para o ambiente de produção. Os estágios de **teste**, **build** e **deploy**.

## 2. Workflow

Quando iniciado o desenvolvimento de uma funcionalidade deve-se primeiro iniciar o docker. E depois do ambiente rodando corretamente, deve-se criar uma _branch_ seguindo a [política de branches](/docs/policies/branches.md).

Após a criação da _branch_, os _commits_ devem ser feitos de acordo com a [política de commits](/docs/policies/commits.md). Ao realizar o _push_ de um _commit_ para a sua _branch_ correspondente no [repositório do projeto](https://github.com/fga-eps-mds/2019.1-Grupo-3), irá ser utilizada a ferramenta de continuous integration, gitlabCI por meio de um espelhamento das contribuições para o gitlab. Nesse momento é testado o primeiro estágio do _deploy_, descrito pela ferramenta do gitlab chamado gitlabCI, _test_.

Após a finalização da funcionalidade, um Pull Request deve ser aberto, de acordo com a [política de Pull Requests](/docs/policies/pull_request.md), da _branch_ em que se foi feito o trabalho para a branch de homologação, devel. **Importante** - Um _Pull Request_ só será aceito caso o estágio de _teste_ estiver passado pelo gitlabCI.

Ao _Pull Request_ ser aceito para a branch de homologação, ele passa por todos os estágios(teste, build e deploy) e se todos esses estiverem funcionando corretamente, passa pelo estágio de _deploy_ para o ambiente de homologação.

Após a realização dos testes em ambiente de homologação na _branch_ devel e a validação de um usuário real, é aberto um _pull request_ para a branch master.

A _branch_ master é o ambiente de produção. Local em que todas alterações devem estar funcionando corretamente. Porém caso ocorra algo que não foi localizado em alguma das etapas anteriores, todos os estágios de _teste_, _build_ e _deploy_ são rodados novamente.

## 3. Tecnologias

### Docker
  O docker terá duas funcionalidades principais: padronização e isolamento do ambiente.

  Para a padronização do ambiente de desenvolvimento, servirá para o ambiente ser exatamente o mesmo independentemente de Sistema Operacional(SO), visto que dentro da equipe existe uma grande diversidade desses. Mitigando o risco de erros não previstos por conta dessa diferença de SO's.

### DockerHub
  O DockerHub é uma ferramenta que servirá como _registry_. O que é basicamente um repositório de imagens de Docker.

  Ao decorrer do projeto serão geradas imagens de docker e essas serão enviadas ao repositório no DockerHub. Sendo facilmente utilizadas por todos os serviços do produto..

### Github
  É uma ferramenta de controle de versão adotada mundialmente. Através dela é possível que diversas pessoas possam contribuir simultaneamente no mesmo projeto.

  Assim, fizemos o versionamento do código será realizado via Github e adaptado de acordo com os padrões de Software Livre.

### Gitlab-CI
  O gitlab será utilizado para a automatização do _pipeline_ de entrega contínua das funcionalidades a serem desenvolvidas.