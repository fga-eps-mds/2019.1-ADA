| Data       | Versão | Descrição            | Autor             |
|:----------:|:------:|:--------------------:|:-----------------:|
| 24/03/2019 | 1.0 | Criação do documento e resumo da entrevista  | Vitor Gomes|

# Reunião/Entrevista com cliente
A reunião foi realizada no dia 20 de março com clientes, equipe de EPS inteira, um integrante da equipe de MDS (Lucas Fellipe) e possíveis interessados (integrantes do laboratório LAPPIS).

Durante a reunião, foram levantados os seguintes problemas que poderiam ser solucionados a partir do ChatOps.

## Problema chave:
* Gerenciamento de tarefas

## Subproblemas:
* Dificuldade verificar a manutenção do serviço online
* Dificuldade em criar e comentar issues através do celular

## Outros pontos apontados
### Funcionalidades
* Criar um PR através do ChatOps seria inviável
* Seria interessante poder comentários nas issues, já que o acesso ao git por um celular é mais complicado
* Funcionalidades semelhantes ao Rancher seriam interessantes, como para vigiar os serviços e avisar quando estes caíssem
* É interessante pesquisar GitLab vs Travis para encontrar como fazer para funcionalidades similares ao rancher
* Gerenciar issues do próprio repositório
* Avisar quando for criada build
* Qual a versão da release
* Lista de issues fechadas
* Se cair trazer uma versão antiga pegar ultima build estável e colocar em produção
* Alertas
* Utilização do GitLab CI pode ser interessante ao projeto

### Questões relacionadas ao projeto
* Seria interessante pegar dois projetos diferentes e tentar descobrir como faríamos com duas organizações diferentes utilizando o ChatOps
* Colocar watch nas issues através do bot seria uma possível funcionalidade interessante, mas que não é uma prioridade
* Webinars no canal de Youtube do LAPPIS podem auxiliar no projeto [Fazendo seu chatbot inteligente com RASA e Rocket.Chat - YouTube](https://www.youtube.com/watch?v=5fbdIwsGrQ4&list=PLo2mbJ5niURawJ9wJ_FX62N0VzneV3nyV)
* Tecnicamente, o ChatOps é a união de 3 bots vigiando o pipeline inteiro, olhando por exemplo, GitHub e Heroku

### Links úteis
* [GitHub - lappis-unb/chatops: A chatbot using opsdroid to make chatops](https://github.com/lappis-unb/chatops)
* [GitHub - lappis-unb/rasa-ptbr-boilerplate: Um baseline para criar um FAQ chatbot usando Rasa, Rocket.chat, elastic search](https://github.com/lappis-unb/rasa-ptbr-boilerplate)
* [GitHub - exAspArk/awesome-chatops: A collection of awesome things about ChatOps – managing operations through a chat](https://github.com/exAspArk/awesome-chatops)

## Visão Geral de Funcionalidades
* Criar issue
* Notificação issues, pr
* Notificação integração contínua (em que ponto quebrou)
* Notificação fora do ar
* Através do chatbot colocar o serviço no ar
* Qual a versão da release
* Lista de issues

> O áudio da reunião pode ser encontrado em: [Entrevista 20 de março.m4a - Google Drive](https://drive.google.com/open?id=1vdwdlQoV2qdzM-E6D2wCQgr-YbryumlM)
