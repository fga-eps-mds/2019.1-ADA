#

# Documento de Visão

## Histórico de Revisão

| Data       | Versão | Divisão                                                                                                                           | Autor                                                      |
| ---------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 21/03/2019 | 0.1    | Abertura do documento                                                                                                             | MDS (todos)                                                |
| 21/03/2019 | 0.2    | Tópico 1 - Introdução                                                                                                             | Erick Giffoni, João Pedro                                  |
| 21/03/2019 | 0.3    | Tópico 2 - Posicionamento                                                                                                         | Erick Giffoni, João Pedro                                  |
| 21/03/2019 | 0.4    | Tópico 3 - Descrições dos Envolvidos e dos Usuários                                                                               | Guilherme Mendes, Lucas Fellipe                            |
| 21/03/2019 | 0.5    | Tópico 4 - Visão Geral do Produto                                                                                                 | Guilherme Mendes, Lucas Fellipe                            |
| 21/03/2019 | 0.6    | Tópico 5 - Recursos do Produto                                                                                                    | Guilherme Mendes, Lucas Fellipe, João Pedro, Erick Giffoni |
| 21/03/2019 | 0.7    | Tópico 6 - Restrições                                                                                                             | Guilherme Mendes, Lucas Fellipe, João Pedro, Erick Giffoni |
| 22/03/2019 | 0.8    | Tópico 7 - Outros requisitos do Produto                                                                                           | Caio Fernandes                                             |
| 22/03/2019 | 0.9    | Complementação do subtópico 2.3                                                                                                   | Erick Giffoni                                              |
| 23/03/2019 | 1.0    | Adição da tabela no subtópico 2.3                                                                                                 | Erick Giffoni                                              |
| 25/03/2019 | 1.1    | Revisão do Tópico 3 - Descrição dos Envolvidos e dos Usuários                                                                     | Guilherme Mendes                                           |
| 25/03/2019 | 1.2    | Revisão do documento, correção de especificidade do termo &quot;GitLab&quot; e adição do Tópico 3.7                               | Caio Fernandes                                             |
| 25/03/2019 | 1.3    | Revisão e formatação do documento. Complementação dos subtópicos : 4.3 Suposições e Dependências; 4.5 Licenciamento e Instalação. | Erick Giffoni                                              |
| 25/03/2019 | 1.4    | Revisão e complementação do subtópico: 4.1 (Perspectiva do produto)                                                               | Lucas Fellipe                                              |
| 25/03/2019 | 1.5    | Revisão do documento em geral e pequenas mudanças no tópico 5 (Recursos dos produtos)                                             | João Pedro                                                 |
| 26/03/2019 | 1.6    | Revisão do subtópico 1.4 (Referências)                                                                                            | Guilherme Mendes                                           |
| 27/03/2019 | 1.7    | Complementação do subtópico 2.2 Descrição do problema                                                                             | Guilherme Mendes, Caio Fernandes                           |

## 1. Introdução

1.1 Propósito

A finalidade desse documento é informar ao leitor a respeito do ChatOps \$nome. Para isso, serão apresentados diversos aspectos relacionados a esse _software_ de forma a expressar claramente a visão dele.

1.2 Escopo

O ChatOps $nome é um _software_ gerenciador de serviços que apoia-se em plataformas de controle de versionamento de softwares baseada em Git. Ele é simples e fácil de usar. $nome atua em qualquer chat (conversa) no Telegram e por meio dele é possível fazer ações imperativas e receptivas, como, por exemplo, criar novas issues e receber notificações de diversos tipos..

$nome é mais que um gerenciador de serviços, ele é um facilitador e é uma ferramenta auxiliadora no processo de desenvolvimento de tarefas relacionadas ao ambiente de desenvolvimento baseado em Git. O ChatOps $nome é dotado de múltiplas ferramentas, que estão apresentadas adiante neste documento. Alguns exemplos são : notificar issues; informar versões do serviço; colocar o serviço de volta ao ar; notificar integrações contínuas etc.

\$nome foi desenvolvido por 9 estudantes de Engenharia de Software da Universidade de Brasília em um período aproximado de 4 meses e é voltado a desenvolvedores, principalmente, mas não somente.

1.3 Definições, acrônimos e abreviações

| **Sigla** | **Definição**                                                                                            |
| --------- | -------------------------------------------------------------------------------------------------------- |
| \$nome    | O nome do ChatOps                                                                                        |
| ChatOps   | _Software_ que conduz uma conversa de forma a automatizar/integrar processos e serviços                  |
| EPS       | Equipe de Engenharia de Produto de _Software_                                                            |
| FGA       | Faculdade do Gama                                                                                        |
| Git       | Sistema de controle de versões                                                                           |
| Git       | Git é um sistema de controle de versões distribuído, usado principalmente no desenvolvimento de software |
| MDS       | Equipe de Métodos de Desenvolvimento de _Software_                                                       |
| Telegram  | Aplicativo de mensagens instantâneas                                                                     |
| TI        | Tecnologia da Informação                                                                                 |
| UnB       | Universidade de Brasília                                                                                 |
| FGA       | Faculdade do Gama                                                                                        |

1.4 Referências

- IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ\_4.0.6/com.ibm.rational.rrm.help.doc/topics/r\_vision\_doc.html. Acesso em 21 de mar. de 2019;

- Disponível em: https://github.com/fga-eps-mds/2018.2-Lino/blob/master/docs/documento-de-visao.md. Acesso em 22 de mar. de 2019;
- Disponível em: https://github.com/fga-eps-mds/2018.2-Kalkuli/blob/master/docs/DocumentoDeVisao.md. Acesso em 22 de mar. de 2019;
- Disponível em: https://github.com/fga-eps-mds/2018.1-Dr-Down/blob/develop/docs/mds/VISION\_DOCUMENT.md. Acesso em 22 de mar. de 2019;

  1.5 Visão Geral

Esse é um documento informativo sobre o ChatOps \$nome que está organizado no formato de tópicos e subtópicos sequenciais numerados. A ordem desses tópicos começa em 1 e termina em 9, sendo eles : introdução; posicionamento; descrições dos envolvidos e dos usuários; visão geral do produto; recursos do produto; restrições; faixas de qualidade; precedência e prioridade; outros requisitos do produto.

O documento de visão têm por objetivo representar de forma explicativa todas as informações sobre o projeto, para que os membros e os interessados do projeto sejam capazes de entender melhor do que se trata e ter noção de todas as funcionalidades, as restrições, os fatores de qualidade entre outros que serão descritos subsequentemente.

## 2. Posicionamento

2.1 Oportunidade de negócios

Muitos desenvolvedores de _software_, estudantes e profissionais da área de TI utilizam plataformas baseadas em Git para gerenciar seus serviços e aplicações. Essas plataformas são robustas e possuem diversas facilidades. Entretanto, é fácil perder-se em meio a tantos comentários, commits, versões do produto ou serviço, visto que tais plataformas são, por vezes, um pouco complicadas de se lidar.

Nesse sentido, o ChatOps \$nome impulsiona-se nos ambientes online para gerenciar serviços de forma automatizada, simples e rápida, por meio de chats interativos e não interativos na plataforma Telegram.

2.2 Descrição do problema

| **5W2H**          |                                                                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **O que?**        | ChatOps voltado para controle de repositórios remotos.                                                                                                                                           |
| **Quem?**         | Estudantes de Engenharia de Software da Universidade de Brasília                                                                                                                                 |
| **Onde?**         | Universidade de Brasília, FGA                                                                                                                                                                    |
| **Quando?**       | No primeiro semestre de 2019.                                                                                                                                                                    |
| **Por que?**      | Para melhorar a integração de times de desenvolvedores com a ferramenta Git, automatizando processos e trazendo informações de maneira a facilitar e a otimizar o desenvolvimento do _software_. |
| **Como?**         | Por meio do desenvolvimento de um ChatOps que utiliza processamento de linguagem natural para controlar ambientes de gerenciamento de _software_ baseados em git.                                |
| **Quanto custa?** | ~ R\$ 300.000,00.                                                                                                                                                                                |

| **O problema de**         | Falta de uma ferramenta que automatize todo o pipeline de integração de software juntamente com um gerenciador de repositório de software baseado em Git por meio de um ChatOps.                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Afeta**                 | Desenvolvedores                                                                                                                                                                                  |
| **Cujo impacto é**        | Facilitar o desenvolvimento de software.                                                                                                                                                         |
| **Uma boa solução seria** | O uso prático do ChatOps, como uma ferramenta de comunicação em tempo real para facilitar o gerenciamento de repositórios Git, melhorando a rastreabilidade das modificações feitas nos projetos |

2.3 Instrução de posição do produto

$nome é voltado para quaisquer profissionais e estudantes que utilizam plataformas baseadas em Git para gerenciar repositórios remotos e controle de versões, uma vez que há a necessidade de automatizar esses processos. O $nome é um ChatOps de controle e de gerenciamento de atividades cuja motivação é utilizar linguagem natural para melhorar processos produtivos. Diferente do GitHub bot, nosso produto possui mais funcionalidades, como criar novas issues e colocar o serviço no ar.

A seguir, tabela que explica o dito acima:

| Para          | Quaisquer profissionais e estudantes que utilizem plataformas baseadas em Git para gerenciar repositórios remotos e controle de versões |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Que           | Têm a necessidade de automatizar esses processos                                                                                        |
| \$nome é      | Um ChatOps de controle e de gerenciamento de atividades                                                                                 |
| Que           | Utiliza linguagem natural para melhorar processos produtivos.                                                                           |
| Diferente do  | GitHub bot                                                                                                                              |
| Nosso produto | Atua em plataformas baseadas em Git e possui mais funcionalidades, como criar novas issues e colocar o serviço no ar.                   |

## 3. Descrição dos Envolvidos e dos Usuários

3.1 Resumo dos Envolvidos

| **Nome**                                      | **Descrição**                                                                                      | **Responsabilidades**                                                                                   |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Equipe de Desenvolvimento de _Software_       | Estudantes da disciplina de Métodos de Desenvolvimento de _Software_, da Universidade de Brasília. | Desenvolver e implementar o _Software_ descrito no documento.                                           |
| Equipe de Engenharia de Produto de _Software_ | Estudantes da disciplina de Engenharia de Produto de _Software_, da Universidade de Brasília.      | Gestão da Equipe de Desenvolvimento, garantindo a viabilidade do produto por meio de entregas contínuas |
| Equipe de orientação                          | Professores e monitores das disciplinas de EPS e MDS.                                              | Auxiliar a equipe durante o desenvolvimento do _Software_.                                              |

3.2 Resumo dos Usuários

| **Nome**                  | **O que representa?**                                                                                 | **Função**                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Equipe de desenvolvedores | Equipes que utilizam plataformas de hospedagem de código-fonte (GitHub, GitLab, etc...).              | Criação de projetos comerciais e pessoais. |
| Equipe de estudantes      | Estudantes que cursam a área de TI em universidades que precisam organizar e gerenciar seus projetos. | Criação de projetos comerciais e pessoais. |

3.3 Ambiente dos Usuários

Os usuários poderão realizar a interação com o ChatOps \$nome a partir do Telegram e de plataformas baseadas em Git, sempre que quiserem realizar commits, pull requests, criar issues, comentar em issues, voltar para releases mais estáveis, entre outras funcionalidades.

3.4 Perfis do Envolvidos

3.4.1 Equipe de Desenvolvimento de _Software_

| Representantes           | Caio Vinicius Fernandes de Araújo, Erick Giffoni Felicíssimo, Guilherme Mendes Pereira, João Pedro José Santos da Silva Guedes, Lucas Fellipe Carvalho Moreira |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Descrição                | Desenvolvimento do _Software_.                                                                                                                                 |
| Tipo                     | Estudantes de Métodos de Desenvolvimento de _Software_ da Universidade de Brasília - UnB/Gama - FGA, curso Engenharia de _Software_.                           |
| Responsabilidades        | Desenvolver, implementar e testar o _software_.                                                                                                                |
| Critérios de Sucesso     | Finalizar o _software_ com todas as funcionalidades no prazo estipulado.                                                                                       |
| Envolvimento             | Alto.                                                                                                                                                          |
| Comentários ou Problemas | Inexperiência da equipe com a linguagem de programação utilizada para desenvolver o _software_.                                                                |

3.4.2 Equipe de Engenharia de Produto de _Software_

| Representantes           | Ateldy Borges Brasil Filho, Bruno Oliveira Dantas, João Vitor Ramos de Souza, Vitor Gomes de Menezes       |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Descrição                | Gerenciamento do _Software_.                                                                               |
| Tipo                     | Estudantes de Engenharia de Produto de _Software_ da Universidade de Brasília - UnB/Gama - FGA.            |
| Responsabilidades        | Realizar a gestão, monitorar e orientar a equipe de Desenvolvimento de _Software_.                         |
| Critérios de Sucesso     | Permanecer com os prazos estipulados sem atraso, e controlar a qualidade do _software_ em desenvolvimento. |
| Envolvimento             | Alto.                                                                                                      |
| Comentários ou Problemas | Inexperiência com tecnologias e gestão.                                                                    |

3.4.3 Equipe de Orientação

| Representantes           | Bruna Nayara Moreira Lima, Carla Silva Rocha Aguiar                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Descrição                | Professoras na Universidade de Brasília, no Campus Faculdade Gama(FGA-UnB), professoras de Métodos de Desenvolvimento de _Software_ e Engenharia de Produto de _Software_, respectivamente. |
| Tipo                     | Orientadoras e avaliadoras que darão auxílio no desenvolvimento do ChatOps \$nome.                                                                                                          |
| Responsabilidades        | Avaliar a equipe de MDS e EPS e ajudá-los em eventuais dúvidas.                                                                                                                             |
| Critérios de Sucesso     | Testemunhar o sucesso da equipe de Desenvolvimento e ver o ChatOps funcionando perfeitamente.                                                                                               |
| Envolvimento             | Médio.                                                                                                                                                                                      |
| Comentários ou Problemas | --                                                                                                                                                                                          |

3.5 Perfis dos Usuários

| Representantes           | Desenvolvedores                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Descrição                | Desenvolvedores que utilizam plataformas de hospedagem de código-fonte Git.                                 |
| Tipo                     | Responsáveis pela programação, manutenção e desenvolvimento de software.                                    |
| Responsabilidades        | Interação com o ChatBot através do _Telegram_, a fim de receber notificações e gerenciar seus repositórios. |
| Critérios de Sucesso     | Usabilidade e praticidade.                                                                                  |
| Envolvimento             | Alto.                                                                                                       |
| Comentários ou Problemas | Não possuir cadastro no _Telegram_.                                                                         |

3.6 Principais Necessidades dos Usuários ou dos Envolvidos

| Necessidade                                                                           | Prioridade | Preocupações                                                  | Solução Atual                               | Soluções Propostas                                                                            |
| ------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Gerenciar e visualizar funcionalidades dos gerenciadores de repositórios de software. | Alta       | Integração com plataformas de hospedagem de código-fonte Git. | Acessar diretamente os repositórios via web | Por meio do ChatBot no _Telegram_ realizar alterações e receber notificações dos repositórios |

3.7 Alternativas e Concorrências

3.7.1 Integram:Ferramenta de integração entre o Telegram e outros serviços como Trello, Gitlab e Bitbucket.

3.7.2 GitHub Bot **:** Extensão para o Telegram que notifica sobre eventos, repositórios e comentários do GitHub.

## 4. Visão geral do Produto

4.1 Perspectiva do produto

O produto, inicialmente, tem como objetivo fazer a gerência de serviços em uma plataforma de hospedagem de código-fonte. O produto tem como propósito facilitar a organização de tarefas em projetos. O nosso produto é baseado no ChatOps (ChatBots + DevOps), que é a prática do desenvolvimento e operação orientado por conversas. Esse sistema, visa, principalmente, viabilizar a relação entre usuário e máquina, fazendo com que as equipes possam automatizar tarefas e colaborar, trabalhando melhor, mais barato e mais rápido. Existem ferramentas, atualmente, para a realização do ChatOps, tais como, _Integram_, _GitHub Bot_, entre outros*.* O _Integram_ é um ChatOps que visa ajudar equipes de operação e desenvolvimento a obterem resultados mais rápidos a partir da integração com o Telegram. O nosso produto possui diversas funcionalidades e se destaca em relação a outros produtos, como o _Integram_, pois, além de integrar conversas, notificar os usuários, ele realizará ações imperativas, como, realizar _commits_, realizar _pull requests_, realizar a criação de _issues_ e realizar o controle da versão mais estável da Release.

4.2 Funções do produto

O ChatOps \$nome visa fazer o gerenciamento de serviços. Ele pode ser utilizado na plataforma de mensagens instantâneas Telegram e possui diversas funções, como receber notificações (_commits_, _pull requests_, comentários em _issues_, etc...) além de poder criar novas issues e fazer com que o usuário volte para a versão mais estável da Release.

4.3 Suposições e dependências

Para a devida utilização desse software, é necessário que o usuário atenda a algumas restrições, conforme o exposto no tópico 6.

4.4 Custo e precificação

Vide documento Termo de Abertura.

4.5 Licenciamento e instalação

4.5.1 Licenciamento

Ainda não foi definido.

4.5.2 Instalação

Ainda não foi feito um tutorial de instalação.

## 5. Recursos do Produto

5.1 Acesso a repositório de ferramentas Git

O usuário poderá conectar seu repositório do Git a partir do ChatOps \$nome.

5.2 Envio de notificações sobre mudanças no repositório

Caso haja alguma mudança dentro do repositório, como novas issues, novos commits, novos pull requests, serão enviados alertas aos usuários através do chat do telegram. Além disso, o _Software_ avisará quando o serviço estiver fora do ar.

5.3 Interação com o usuário por meio do Telegram

O usuário poderá mandar mensagens para o bot em linguagem natural(português coloquial) e a resposta recebida será interativa.

5.4 Informações instantâneas

Caso o usuário faça a requisição, o bot enviará informações específicas, tais como: versão da release; commits; issues, entre outros.

5.4 Criação de novas Issues

O(s) usuário(s) poderá(ão) criar novas Issues no seu repositório por meio do bot, além de comentar issues já existentes.

5.5 Gerenciamento de versões

Se o serviço da versão atual estiver indisponível ou com falhas, o usuário poderá fazer o pedido e o bot fará com que o serviço volte para a versão anterior.

## 6. Restrições

- Uso do Telegram;
- Acesso à Internet;
- Acesso a conta de alguma ferramentagerenciadora de repositório de software baseado em git;
- Controle de apenas 1 repositório por chat;
- O ChatOps deverá estar em funcionamento até o dia 25/06/2019;
- Compreender significamente o português;

## 7. Outros Requisitos do Produto

7.1 Requisitos do Sistema

O usuário deverá ter acesso ao serviço de mensagens instantâneas Telegram e também a um repositório em um ambiente de gerenciamento de _software_ baseado em git (Github ou GitLab). O sistema operacional é variável de acordo com o dispositivo de utilização, sendo o telegram disponível para: iOS, Android, Windows, MacOs, Linux e Web. Ferramentas baseadas em git estão disponíveis em aplicações Web.

7.2 Requisitos de Desempenho

O sistema será dimensionado para suprir a necessidade de uma aplicação acessível à grande maioria dos aparelhos. Basta o dispositivo ter acesso à aplicação Telegram. Sendo assim, o desempenho do aparelho será um fator de mínima importância para o acesso, porém de alta relevância para a obtenção de um melhor desempenho do ChatOps.
