# **Documento de Visão**

## **Histórico de Revisão**

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
| 28/03/2019 | 2.0     | Revisão da formatação do documento de visão                     | Lucas Fellipe, Guilherme Mendes, João Vitor

## 1. Introdução

### 1.1 Propósito

<p style="text-align:justify">&emsp;&emsp;A finalidade desse documento é informar ao leitor a respeito do ChatOps Ada. Para isso, serão apresentados diversos aspectos relacionados a esse <i>software</i> de forma a expressar claramente a visão dele.</p>

### 1.2 Escopo

<p style="text-align:justify">&emsp;&emsp;O ChatOps Ada é um <i>Software</i> gerenciador de serviços que apoia-se em plataformas de controle de versionamento de <i>software</i> baseada em Git. Ele é simples e fácil de usar. Ada atua em qualquer chat (conversa) no Telegram e por meio dele é possível fazer ações imperativas e receptivas, como, por exemplo, criar novas <i>Issues</i> e receber notificações de diversos tipos.</p>

<p style="text-align:justify">&emsp;&emsp;Ada é mais que um gerenciador de serviços, ele é um facilitador e é uma ferramenta auxiliadora no processo de desenvolvimento de tarefas relacionadas ao ambiente de desenvolvimento baseado em Git. O ChatOps Ada é dotado de múltiplas ferramentas, que estão apresentadas adiante neste documento. Alguns exemplos são : notificar <i>Issues</i>; informar versões do serviço; colocar o serviço de volta ao ar; notificar integrações contínuas etc.</p>

<p style="text-align:justify">&emsp;&emsp;Ada foi desenvolvido por 9 estudantes de Engenharia de Software da Universidade de Brasília em um período aproximado de 4 meses e é voltado a desenvolvedores, principalmente, mas não somente.</p>

### 1.3 Definições, acrônimos e abreviações

| **Sigla** | **Definição**                                                                                            |
| --------- | -------------------------------------------------------------------------------------------------------- |
| Ada    | O nome do ChatOps                                                                                        |
| ChatOps   | <i>Software</i> que conduz uma conversa de forma a automatizar/integrar processos e serviços                  |
| EPS       | Equipe de Engenharia de Produto de <i>Software</i>                                                            |
| FGA       | Faculdade do Gama                                                                                        |
| Git       | Sistema de controle de versões                                                                           |
| Git       | Git é um sistema de controle de versões distribuído, usado principalmente no desenvolvimento de software |
| MDS       | Equipe de Métodos de Desenvolvimento de <i>Software</i>                                                       |
| Telegram  | Aplicativo de mensagens instantâneas                                                                     |
| TI        | Tecnologia da Informação                                                                                 |
| UnB       | Universidade de Brasília                                                                                 |
| FGA       | Faculdade do Gama                                                                                        |

### 1.4 Referências

- IBM Knowledge Center - Documento de Visão: A estrutura de tópicos do documento de visão. Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ\_4.0.6/com.ibm.rational.rrm.help.doc/topics/r\_vision\_doc.html. Acesso em 21 de mar. de 2019;

- Disponível em: https://github.com/fga-eps-mds/2018.2-Lino/blob/master/docs/documento-de-visao.md. Acesso em 22 de mar. de 2019;
- Disponível em: https://github.com/fga-eps-mds/2018.2-Kalkuli/blob/master/docs/DocumentoDeVisao.md. Acesso em 22 de mar. de 2019;
- Disponível em: https://github.com/fga-eps-mds/2018.1-Dr-Down/blob/develop/docs/mds/VISION\_DOCUMENT.md. Acesso em 22 de mar. de 2019;

### 1.5 Visão Geral

<p style="text-align:justify">&emsp;&emsp;Esse é um documento informativo sobre o ChatOps Ada que está organizado no formato de tópicos e subtópicos sequenciais numerados. A ordem desses tópicos começa em 1 e termina em 9, sendo eles : introdução; posicionamento; descrições dos envolvidos e dos usuários; visão geral do produto; recursos do produto; restrições; faixas de qualidade; precedência e prioridade; outros requisitos do produto.</p>

<p style="text-align:justify">&emsp;&emsp;O documento de visão têm por objetivo representar de forma explicativa todas as informações sobre o projeto, para que os membros e os interessados do projeto sejam capazes de entender melhor do que se trata e ter noção de todas as funcionalidades, as restrições, os fatores de qualidade entre outros que serão descritos subsequentemente.</p>

## 2. Posicionamento

### 2.1 Oportunidade de negócios

<p style="text-align:justify">&emsp;&emsp;Muitos desenvolvedores de <i>Software</i>, estudantes e profissionais da área de TI utilizam plataformas baseadas em Git para gerenciar seus serviços e aplicações. Essas plataformas são robustas e possuem diversas facilidades. Entretanto, é fácil perder-se em meio a tantos comentários, commits, versões do produto ou serviço, visto que tais plataformas são, por vezes, um pouco complicadas de se lidar.</p>

<p style="text-align:justify">&emsp;&emsp;Nesse sentido, o ChatOps Ada impulsiona-se nos ambientes online para gerenciar serviços de forma automatizada, simples e rápida, por meio de chats interativos e não interativos na plataforma Telegram.</p>

### 2.2 Descrição do problema

|           |      **5W2H**                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **O que?**        | ChatOps voltado para controle de repositórios remotos.                                                                                                                                           |
| **Quem?**         | Estudantes de Engenharia de Software da Universidade de Brasília                                                                                                                                 |
| **Onde?**         | Universidade de Brasília, FGA                                                                                                                                                                    |
| **Quando?**       | No primeiro semestre de 2019.                                                                                                                                                                    |
| **Por quê?**      | Para melhorar a integração de times de desenvolvedores com a ferramenta Git, automatizando processos e trazendo informações de maneira a facilitar e a otimizar o desenvolvimento do <i>Software</i>. |
| **Como?**         | Por meio do desenvolvimento de um ChatOps que utiliza processamento de linguagem natural para controlar ambientes de gerenciamento de <i>Software</i> baseados em git.                                |
| **Quanto custa?** | ~ R\$ 300.000,00.                                                                                                                                                                                |


|           |  Informações do Produto   |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **O problema de**                | Falta de uma ferramenta que automatize todo o pipeline de integração de software      juntamente com um gerenciador de repositório de software baseado em Git por meio de um ChatOps.                                                                        |
| **Afeta**                     | Desenvolvedores.            |
| **Cujo impacto é**        | Facilitar o desenvolvimento de software.                         |
| **Uma boa solução seria**     | O uso prático do ChatOps, como uma ferramenta de comunicação em tempo real para facilitar o gerenciamento de repositórios Git, melhorando a rastreabilidade das modificações feitas nos projetos. |


### 2.3 Instrução de posição do produto

<p style="text-align:justify">&emsp;&emsp;Ada é voltado para quaisquer profissionais e estudantes que utilizam plataformas baseadas em Git para gerenciar repositórios remotos e controle de versões, uma vez que há a necessidade de automatizar esses processos. O Ada é um ChatOps de controle e de gerenciamento de atividades cuja motivação é utilizar linguagem natural para melhorar processos produtivos. Diferente do GitHub bot, nosso produto possui mais funcionalidades, como criar novas <i>Issues</i> e colocar o serviço no ar.</p>

A seguir, tabela que explica o dito acima:

|            |    Instrução de posição do produto    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Para                | Quaisquer profissionais e estudantes que utilizem plataformas baseadas em Git para gerenciar repositórios remotos e controle de versoões.                                                                               |
| Que                     | Têm a necessidade de automatizar esses processos.            |
| Ada é        | Um ChatOps de controle e de gerenciamento de atividades.                         |
| Que     | Utiliza linguagem natural para melhorar processos produtivos. |
| Diferente do             | GitHub bot.                                                                                                      |
| Nosso produto | Atua em plataformas baseadas em Git e possui mais funcionalidades, como criar novas <i>Issues</i> e colocar o serviço no ar.

## 3. Descrição dos Envolvidos e dos Usuários

### 3.1 Resumo dos Envolvidos

| **Nome**                                      | **Descrição**                                                                                      | **Responsabilidades**                                                                                   |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Equipe de Desenvolvimento de <i>Software</i>       | Estudantes da disciplina de Métodos de Desenvolvimento de <i>Software</i>, da Universidade de Brasília. | Desenvolver e implementar o <i>Software</i> descrito no documento.                                           |
| Equipe de Engenharia de Produto de <i>Software</i> | Estudantes da disciplina de Engenharia de Produto de <i>Software</i>, da Universidade de Brasília.      | Gestão da Equipe de Desenvolvimento, garantindo a viabilidade do produto por meio de entregas contínuas |
| Equipe de orientação                          | Professores e monitores das disciplinas de EPS e MDS.                                              | Auxiliar a equipe durante o desenvolvimento do <i>Software</i>.                                              |

### 3.2 Resumo dos Usuários

| **Nome**                  | **O que representa?**                                                                                 | **Função**                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| Equipe de desenvolvedores | Equipes que utilizam plataformas de hospedagem de código-fonte (GitHub, GitLab, etc...).              | Criação de projetos comerciais e pessoais. |
| Equipe de estudantes      | Estudantes que cursam a área de TI em universidades que precisam organizar e gerenciar seus projetos. | Criação de projetos comerciais e pessoais. |

### 3.3 Ambiente dos Usuários

Os usuários poderão realizar a interação com o ChatOps Ada a partir do Telegram e de plataformas baseadas em Git, sempre que quiserem realizar commits, <i>Pull Requests</i>, criar <i>Issues</i>, comentar em <i>Issues</i>, voltar para <i>Releases</i> mais estáveis, entre outras funcionalidades.

### 3.4 Perfis do Envolvidos

#### 3.4.1 Equipe de Desenvolvimento de <i>Software</i>

| Representantes           | Caio Vinicius Fernandes de Araújo, Erick Giffoni Felicíssimo, Guilherme Mendes Pereira, João Pedro José Santos da Silva Guedes, Lucas Fellipe Carvalho Moreira |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Descrição                | Desenvolvimento do <i>Software</i>.                                                                                                                                 |
| Tipo                     | Estudantes de Métodos de Desenvolvimento de <i>Software</i> da Universidade de Brasília - UnB/Gama - FGA, curso Engenharia de <i>Software</i>.                           |
| Responsabilidades        | Desenvolver, implementar e testar o <i>Software</i>.                                                                                                                |
| Critérios de Sucesso     | Finalizar o <i>Software</i> com todas as funcionalidades no prazo estipulado.                                                                                       |
| Envolvimento             | Alto.                                                                                                                                                          |
| Comentários ou Problemas | Inexperiência da equipe com a linguagem de programação utilizada para desenvolver o <i>Software</i>.                                                                |

#### 3.4.2 Equipe de Engenharia de Produto de <i>Software</i>

| Representantes           | Ateldy Borges Brasil Filho, Bruno Oliveira Dantas, João Vitor Ramos de Souza, Vitor Gomes de Menezes       |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Descrição                | Gerenciamento do <i>Software</i>.                                                                               |
| Tipo                     | Estudantes de Engenharia de Produto de <i>Software</i> da Universidade de Brasília - UnB/Gama - FGA.            |
| Responsabilidades        | Realizar a gestão, monitorar e orientar a equipe de Desenvolvimento de <i>Software</i>.                         |
| Critérios de Sucesso     | Permanecer com os prazos estipulados sem atraso, e controlar a qualidade do <i>Software</i> em desenvolvimento. |
| Envolvimento             | Alto.                                                                                                      |
| Comentários ou Problemas | Inexperiência com tecnologias e gestão.                                                                    |

#### 3.4.3 Equipe de Orientação

| Representantes           | Bruna Nayara Moreira Lima, Carla Silva Rocha Aguiar                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Descrição                | Professoras da Universidade de Brasília, no Campus Faculdade Gama(FGA-UnB), professoras de Métodos de Desenvolvimento de <i>Software</i> e Engenharia de Produto de <i>Software</i>, respectivamente. |
| Tipo                     | Orientadoras e avaliadoras que darão auxílio no desenvolvimento do ChatOps Ada.                                                                                                          |
| Responsabilidades        | Avaliar a equipe de MDS e EPS e ajudá-los em eventuais dúvidas.                                                                                                                             |
| Critérios de Sucesso     | Testemunhar o sucesso da equipe de Desenvolvimento e ver o ChatOps funcionando perfeitamente.                                                                                               |
| Envolvimento             | Médio.                                                                                                                                                                                      |
| Comentários ou Problemas | --                                                                                                                                                                                          |

### 3.5 Perfis dos Usuários

| Representantes           | Desenvolvedores                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Descrição                | Desenvolvedores que utilizam plataformas de hospedagem de código-fonte Git.                                 |
| Tipo                     | Responsáveis pela programação, manutenção e desenvolvimento de software.                                    |
| Responsabilidades        | Interação com o ChatBot através do _Telegram_, a fim de receber notificações e gerenciar seus repositórios. |
| Critérios de Sucesso     | Usabilidade e praticidade.                                                                                  |
| Envolvimento             | Alto.                                                                                                       |
| Comentários ou Problemas | Não possuir cadastro no _Telegram_.                                                                         |

### 3.6 Principais Necessidades dos Usuários ou dos Envolvidos

| Necessidade                                                                           | Prioridade | Preocupações                                                  | Solução Atual                               | Soluções Propostas                                                                            |
| ------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Gerenciar e visualizar funcionalidades dos gerenciadores de repositórios de software. | Alta       | Integração com plataformas de hospedagem de código-fonte Git. | Acessar diretamente os repositórios via web | Por meio do ChatBot no _Telegram_ realizar alterações e receber notificações dos repositórios |

### 3.7 Alternativas e Concorrências

#### 3.7.1 Integram:Ferramenta de integração entre o Telegram e outros serviços como Trello, Gitlab e Bitbucket.

#### 3.7.2 GitHub Bot **:** Extensão para o Telegram que notifica sobre eventos, repositórios e comentários do GitHub.

## 4. Visão geral do Produto

### 4.1 Perspectiva do produto

<p style="text-align:justify">&emsp;&emsp;O produto, inicialmente, tem como objetivo fazer a gerência de serviços em uma plataforma de hospedagem de código-fonte. O produto tem como propósito facilitar a organização de tarefas em projetos. O nosso produto é baseado no ChatOps (ChatBots + DevOps), que é a prática do desenvolvimento e operação orientado por conversas. Esse sistema, visa, principalmente, viabilizar a relação entre usuário e máquina, fazendo com que as equipes possam automatizar tarefas e colaborar, trabalhando melhor, mais barato e mais rápido. Existem ferramentas, atualmente, para a realização do ChatOps, tais como, <i>Integram</i>, <i>GitHub Bot</i>, entre outros. O <i>Integram</i> é um ChatOps que visa ajudar equipes de operação e desenvolvimento a obterem resultados mais rápidos a partir da integração com o Telegram. O nosso produto possui diversas funcionalidades e se destaca em relação a outros produtos, como o <i>Integram</i>, pois, além de integrar conversas, notificar os usuários, ele realizará ações imperativas, como, realizar <i>commits</i>, realizar <i><i>Pull Requests</i></i>, realizar a criação de <i><i>Issues</i></i> e realizar o controle da versão mais estável da <i>Releases</i></p>

![chatops](../assets/img/project/chatops.png)

### 4.2 Funções do produto

<p style="text-align:justify">&emsp;&emsp;O ChatOps Ada visa fazer o gerenciamento de serviços. Ele pode ser utilizado na plataforma de mensagens instantâneas Telegram e possui diversas funções, como receber notificações (<i>commits</i>, <i><i>Pull Requests</i></i>, comentários em <i><i>Issues</i></i>, etc...) além de poder criar novas <i>Issues</i> e fazer com que o usuário volte para a versão mais estável da <i>Releases</i></p>

### 4.3 Suposições e dependências

<p style="text-align:justify">&emsp;&emsp;Para a devida utilização desse software, é necessário que o usuário atenda a algumas restrições, conforme o exposto no tópico 6.</p>

### 4.4 Custo e precificação

Vide documento Termo de Abertura.

### 4.5 Licenciamento e instalação

### 4.5.1 Licenciamento

<p style="text-align:justify">&emsp;&emsp; O ChatOps Ada é desenvolvido sob a licença <a href="https://github.com/fga-eps-mds/2019.1-Grupo-3/blob/master/LICENSE">GPL 3.0.</a></p>

#### 4.5.2 Instalação

Ainda não foi feito um tutorial de instalação.

## 5. Recursos do Produto

### 5.1 Acesso a repositório de ferramentas Git

<p style="text-align:justify">&emsp;&emsp;O usuário poderá conectar seu repositório do Git a partir do ChatOps Ada.<p>

### 5.2 Envio de notificações sobre mudanças no repositório

<p style="text-align:justify">&emsp;&emsp;Caso haja alguma mudança dentro do repositório, como novas <i>Issues</i>, novos commits, novos <i>Pull Requests</i>, serão enviados alertas aos usuários através do chat do telegram. Além disso, o <i>Software</i> avisará quando o serviço estiver fora do ar.</p>

### 5.3 Interação com o usuário por meio do Telegram

<p style="text-align:justify">&emsp;&emsp;O usuário poderá mandar mensagens para o bot em linguagem natural(português coloquial) e a resposta recebida será interativa.</p>

### 5.4 Informações instantâneas

<p style="text-align:justify">&emsp;&emsp;Caso o usuário faça a requisição, o bot enviará informações específicas, tais como: versão da <i>Releases</i> commits; <i>Issues</i>, entre outros.</p>

### 5.4 Criação de novas <i>Issues</i>

<p style="text-align:justify">&emsp;&emsp;O(s) usuário(s) poderá(ão) criar novas <i>Issues</i> no seu repositório por meio do bot, além de comentar <i>Issues</i> já existentes.</p>

### 5.5 Gerenciamento de versões

<p style="text-align:justify">&emsp;&emsp;Se o serviço da versão atual estiver indisponível ou com falhas, o usuário poderá fazer o pedido e o bot fará com que o serviço volte para a versão anterior.</p>

## 6. Restrições

- Uso do Telegram;
- Acesso à Internet;
- Acesso a conta de alguma ferramentagerenciadora de repositório de software baseado em git;
- Controle de apenas 1 repositório por chat;
- O ChatOps deverá estar em funcionamento até o dia 25/06/2019;
- Compreender significamente o português;

## 7. Outros Requisitos do Produto

### 7.1 Requisitos do Sistema

<p style="text-align:justify">&emsp;&emsp;O usuário deverá ter acesso ao serviço de mensagens instantâneas Telegram e também a um repositório em um ambiente de gerenciamento de <i>Software</i> baseado em git (Github ou GitLab). O sistema operacional é variável de acordo com o dispositivo de utilização, sendo o telegram disponível para: iOS, Android, Windows, MacOs, Linux e Web. Ferramentas baseadas em git estão disponíveis em aplicações Web.</p>

### 7.2 Requisitos de Desempenho

<p style="text-align:justify">&emsp;&emsp;O sistema será dimensionado para suprir a necessidade de uma aplicação acessível à grande maioria dos aparelhos. Basta o dispositivo ter acesso à aplicação Telegram. Sendo assim, o desempenho do aparelho será um fator de mínima importância para o acesso, porém de alta relevância para a obtenção de um melhor desempenho do ChatOps.</p>
