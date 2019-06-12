## intent:action_start
- [/start](command)
- [start](command)

## intent:set_pipeline
- me mostra o pipeline do repositorio por favor
- pipeline repositorio por favor
- pipeline do meu projeto ada
- me mostra o pipe
- qual o resultado do pipeline
- pode me mostrar o resultado do pipeline
- qual foi a  situação final do pipeline
- o pipeline deu certo
- pipeline por favor
- tem alguma build em andamento
- há alguma build
- tem build em progresso
- quais build estão acontecendo
- qual o estágio da build
- onde está a build
- quero saber o estágio da build
- a build está em qual estágio
- me fala a build
- me diz o estágio da build
- ada, qual o estágio da build
- diz o andamento da build
- fala pra mim se tem build em progresso
- me diz o estágio da build, ada
- como está a build
- a build está terminando?
- a build tá começando?
- a build parou?
- quantas builds tem
- quantas builds eu tenho?
- em qual job a build se encontra?
- qual o job da build atual
- tem job em andamento?
- qual a job atual
- quantas builds eu tenho?
- minhas builds
- mostre a build
- builds recentes
- quais são as builds
- diga-me as builds
- as builds, me mostra ai
- git build
- quais as builds
- me mostra a build mais recente
- me mostra o resultado do pipeline
- resultado da pipeline
- resultados das pipelines
- resultados das builds
- saber pipeline
- Ada, me mostra o resultado do pipeline

## intent:action_set_repository_gitlab
- labrepo: [gitlab-runner](repository_gitlab)
- labrepo: [quests](repository_gitlab)
- labrepo: [abcde12345](repository_gitlab)
- labrepo: [owner/repo](repository_gitlab)
- labrepo: [adabot/ada](repository_gitlab)
- labrepo: [adabot/ada-gitlab](repository_gitlab)
- labrepo: [gitlab-org/gitlab-runner](repository_gitlab)
- labrepo: [terrakok/gitlab-client](repository_gitlab)
- labrepo: [gitlab-org/gitaly](repository_gitlab)
- labrepo: [trabalho1](repository_gitlab)
- labrepo: [2019.1-MDS](repository_gitlab)

## intent:action_set_repository_github
- hubrepo: [uri-online-judge](repository_github)
- hubrepo: [gitlab_user](repository_github)
- hubrepo: [gitlab-runner](repository_github)
- o nome do repositório do github é [adabot](repository_github)
- hubrepo: [lucasfcm9](repository_github)
- hubrepo: [caiovf13](repository_github)

## intent:action_get_report
- me manda o relatório do projeto
- relatório, por favor
- ada, me manda o relatório
- me mostra o relatório
- cadê o relatório
- me mostra o relatorio, ada
- Ada, me mostra o relatório
- relatório, por favor
- me mostra o relatório, ada
- me mostra o relatorio, ada
- relatório

## intent:start_create_issue
- quero criar uma nova issue
- cria uma nova issue
- pode criar uma issue nova
- cria uma issue
- tem como criar uma issue pra mim
- Cria uma issue para mim, Ada

## intent:issue_name
- Titulo: [abc](issue_name)
- Título: [2019a](issue_name)
- titulo: [abc](issue_name)
- titulo: [2019a](issue_name)
- Título: [122345](issue_name)
- Titulo: [HEHEHEHE](issue_name)
- titulo: [US26-Ada](issue_name)
- titulo: [Eu como Usuário](issue_name)
- título: [#135 ABC](issue_name)

## intent:create_issue
- Descrição: [Quero criar um banco capaz de guardar informações](issue_body)
- descrição: [teste](issue_body)
- descrição: [Criterios de aceitação](issue_body)
- Descrição: [Tasks 1, 2, 3, 4, 5](issue_body)
- descricao: [1 salvar dados](issue_body)

## intent:comment_issue
- Comentar #[1](issue_number) : Quero criar um banco capaz de guardar informações
- comentar #[3](issue_number) : Nessa historia foi realiza as seguintes funcionalidades
- Comentar #[23](issue_number) : Criterios de aceitação
- Comentar #[456](issue_number) : teste teste teste
- Comentar #[7891](issue_number) : Tasks 1, 2, 3, 4, 5
- Comentar #[12345](issue_number) : 1 salvar dados 

## intent:rerun_pipeline
- quero reiniciar a pipeline

## intent:action_get_report_github
- me manda o relatório do github, ada
- me manda o relatorio do github
- me manda o relatório do github
- me mostra o relatório do github, ada
- Ada, me mostra o relatório do github

## intent:get_url_domain
- [https://fga-eps-mds.github.io/2019.1-ADA](url_name)
- [http://fga-eps-mds.github.io/2019.1-ADA](url_name)
- [https://fga-eps-mds.github.io/](url_name)
- [https://123.com.br](url_name)
- [www.example.com](url_name)
- [www.example.com/example](url_name)
- [www.example.com/example/1234](url_name)
- [https://123.com](url_name)

## intent:action_get_domain
- cadastra meu dominio
- cadastra meu domínio
- fica de olha na minha url
- fica de olho no meu site
- fica de olho no meu dominio
- fica de olho no meu domínio
- fica de olho no meu deploy
- monitora ai meu site
- monitora ai meu dominio
- monitora ai meu domínio
- monitora ai meu deploy

## intent:action_get_issues_of_contributor
- Quero saber quais são as issues do [caiovferas](contributor_name) 
- Quero saber quais sao as issues de [guilhermemender](contributor_name) 
- Quero saber quais sao as issues de [Gudimender](contributor_name)
- Quais são as issues do [João_vvdsad](contributor_name)
- Quais são as issues do [ana](contributor_name)
- Quais são as issues do [CARLOS](contributor_name)
- Quais são as issues do [mariop](contributor_name)
- Quais são as issues do [jose](contributor_name) 
- Quais são as issues do [caio](contributor_name)
- Quais são as issues do [CARLA](contributor_name) 
- Quais são as issues do [igor](contributor_name)
- Quais são as issues do [erick](contributor_name) 
- quais são as issues de [Vitor](contributor_name)
- me fala as issues do [Fulano](contributor_name)

## intent:find_project_collaborators
- quem são os colaboradores do meu projeto ?
- quem está colaborando pro meu projeto ?
- com quem eu trabalho no projeto
- me fala quem mais trabalha no mesmo projeto que eu
- Ada, quem, além de mim, está no mesmo projeto que eu
- com quem estou trabalhando ?
- quem mais trabalha comigo no projeto ?
- quem contribui pro meu projeto ?
- Quem está no mesmo projeto que eu ?
- diz ai os colaboradores do meu projeto
- sou só eu, ou tem mais gente trabalhando no meu projeto ?
- Sou so eu, ou tem mais gente trabalhando no mesmo projeto que eu
- encontra quem mais ta no projeto comigo
- me diz quem ta trabalhando comigo
- me manda os colaboradores
- manda os contribuidores
- quem esta contribuindo para o projeto ?

##intent:action_change_github_repository
- Desejo alterar meu repositório do github
- Quero mudar meu repositório do github
- quero recadastrar meu repositório github
- recadastra meu repositório do github
- muda meu repositório do github
- quero me cadastrar em um novo repositório do github
- Quero me cadastrar em um novo repositório do github
- me cadastra em um novo repositório do gihub
- Me cadastra em um novo repositório do gihub por favor
- Poderia me cadastrar em um novo repositório no github?