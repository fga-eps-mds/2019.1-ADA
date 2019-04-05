# Backlog do Produto

| **Data** | **Versão** | **Descrição** | **Autor** |
| --- | --- | --- | --- |
| 04/04/2019 | 1.0 | Construção do Backlog | Vítor Gomes |

Todos as features e histórias de usuário são apresentados em sua ordem de priorização.

## Épicos

- E1 Comunicação com o usuário
- E2 Gerenciamento do pipeline de produção
- E3 Relatórios de produção

## Features

| **Épico** | **Feature** | **Descrição** |
| --- | --- | --- |
| E1 | F2 | Conexão com Telegram |
| E2 | F4 | Informações de integração contínua |
| E3 | F9 | Produção relatórios de integração contínua |
| E2 | F5 | Informações de deploy |
| E2 | F6 | Gerenciar issues |
| E1 | F1 | Fluxo de conversas |
| E2 | F7 | Gerenciamento de Pull Requests |
| E3 | F8 | Produção de relatórios do GitHub |

> A feature E2F3 Informações de release foi retirada do escopo do produto para o contexto do projeto.

## Histórias de Usuário

| **Épico** | **Feature** | **História de Usuário** | **Descrição** |
| --- | --- | --- | --- |
| E1 | F1 | DS05 | Eu, como desenvolvedor, desejo criar um protótipo da Ada, para compreender melhor suas interações e interface. |
| E1 | F2 | DS01 | Eu, como desenvolvedor, desejo que todo o ambiente de desenvolvimento da Ada esteja uniformizado para padronizar o desenvolvimento. |
| E1 | F2 | DS11 | Eu, como desenvolvedor, desejo conectar o Rasa ao Telegram para que a Ada possa conversar com o usuário. |
| E2 | F4 | DS03 | Eu, como desenvolvedor, desejo que todo o ambiente de desenvolvimento do Monitoramento da integração contínua para padronizar o desenvolvimento. |
| E1 | F2 | DS02 | Eu, como desenvolvedor, desejo criar um banco de dados que guarde informações do Telegram para conseguir comunicação estável com a Ada. |
| E1 | F2 | US26 | Eu, como usuário, desejo me cadastrar com a Ada a partir do GitLab para receber notificações e gerenciar aplicações. |
| E2 | F4 | US07 | Eu, como usuário, desejo ser notificado sobre o resultado de builds para saber o estado de integração contínua. |
| E2 | F4 | US10 | Eu, como usuário, desejo saber quais os passos da build para me manter informado do processo. |
| E2 | F4 | US09 | Eu, como usuário, desejo saber o estágio da build para saber o andamento do processo. |
| E1 | F1 | US04 | Eu, como usuário, desejo ser cumprimentado pela Ada para iniciar uma conversa. |
| E2 | F4 | US08 | Eu, como usuário, desejo reiniciar uma build na ferramenta de integração contínua para confirmar o erro da build anterior. |
| E3 | F9 | US30 | Eu, como usuário, desejo receber um relatório sobre um número de informações do repositório no GitLab para analisar meu repositório mais detalhadamente. |
| E3 | F9 | US31 | Eu, como usuário, desejo agendar o recebimento de relatórios do GitLab para organizar a análise detalhada do repositório. |
| E1 | F2 | US06 | Eu, como usuário, desejo me cadastrar com a Ada a partir do GitHub para receber notificações e gerenciar aplicações. |
| E2 | F6 | US16 | Eu, como usuário, desejo que a Ada crie uma issue para mim para reportar algo aos mantenedores do repositório de maneira mais fácil. |
| E2 | F6 | US19 | Eu, como usuário, desejo ser informado caso a issue esteja atribuída para mim para que eu tenha conhecimento dela. |
| E2 | F6 | US17 | Eu, como usuário, desejo que a Ada faça um comentário na issue por mim para entrar em contato com os mantenedores do repositório de maneira mais fácil. |
| E2 | F6 | US18 | Eu, como usuário, desejo que a Ada feche uma issue para mim para encerrar uma conversa com os mantenedores do repositório de maneira mais fácil. |
| E1 | F1 | US12 | Eu, como usuário, desejo saber todas atividades que a Ada consegue fazer para saber o que posso demandar dela. |
| E1 | F1 | US14 | Eu, como usuário, desejo ser notificado quando a Ada demorar a recuperar informações para saber o status da minha requisição. |
| E2 | F7 | US25 | Eu, como usuário, desejo que a Ada me informe quando um pull request criado por ou atribuído a mim receber uma revisão para que eu possa fazer as alterações necessárias. |
| E1 | F1 | US13 | Eu, como usuário, desejo saber quando a Ada não reconhecer o que falo para repetir o comando reformulado. |
| E1 | F2 | US27 | Eu, como usuário, desejo me cadastrar com a Ada a partir do Amazon para receber notificações e gerenciar aplicações. |
| E2 | F5 | US23 | Eu, como usuário, desejo que a Ada me informe acerca do estado da aplicação para que eu esteja atualizado sobre a manutenção do serviço no ar. |
| E2 | F5 | US24 | Eu, como usuário, desejo que a Ada configure no pipeline de deploy a última versão estável do repositório para recolocar o serviço no ar. |
| E2 | F6 | US20 | Eu, como usuário, desejo que a Ada me informe os responsáveis pela issue que eu informar para auxiliar no gerenciamento de atividades. |
| E1 | F1 | US15 | Eu, como usuário, desejo saber a história da Ada para conhecê-la. |
| E3 | F8 | US28 | Eu, como usuário, desejo receber um relatório sobre um número de informações do repositório no GitHub para analisar meu repositório mais detalhadamente. |
| E3 | F8 | US29 | Eu, como usuário, desejo agendar o recebimento de relatórios do GitHub para organizar a análise detalhada do repositório. |

> As seguintes histórias foram retiradas do escopo do produto no contexto do projeto:
> - E2F7US21 Eu, como usuário, desejo que a Ada me informe os pull requests abertos para que eu saiba quais mudanças estão esperando por revisão.
> - E2F3US22 Eu, como usuário, desejo que a Ada me informe acerca da última release do repositório cadastrado para inteirar-me das últimas atualizações do projeto.
