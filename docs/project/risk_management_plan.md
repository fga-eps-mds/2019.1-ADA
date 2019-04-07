# Plano de Gerenciamento de Riscos

| **Data** | **Versão** | **Descrição** | **Autor** |
| --- | --- | --- | --- |
| 04/04/2019 | 1.0 | Criação da primeira versão do documento | Ateldy Brasil |

## 1. Introdução

O plano de gerenciamento dos riscos fornece informações sobre papéis e responsabilidades relativas aos riscos, indica como as atividades do gerenciamento dos riscos são incluídas nos orçamento e cronograma, e descreve as categorias de risco que podem ser expressas como uma estrutura analítica dos riscos.

## 2. Objetivo

O objetivo do Plano de Gerenciamento de Riscos é documentar os riscos associados ao projeto e as ações a serem tomadas para que eles sejam mitigados ou contingenciada.

## 3. Estrutura Analítica dos Riscos

Uma forma comum para estruturar categorias dos riscos usa a estrutura analítica dos riscos (EAR), uma representação hierárquica de possíveis fontes de riscos. Uma EAR ajuda a equipe do projeto a considerar toda a gama de fontes das quais podem surgir cada risco do projeto. Isso pode ser útil para identificar os riscos ou para categorizá-los.

![Estrutura Analítica dos Riscos deste projeto.](../assets/img/project/risks/EAR.jpg)

[Clique aqui para visualizar a imagem em um maior tamanho](https://raw.githubusercontent.com/fga-eps-mds/2019.1-ADA/gh-pages/docs/img/risks/EAR.jpg)

### 3.1. Risco Técnico

| **Tipo** | **Descrição** |
| --- | --- |
| Requisitos | Riscos pela falta de mapeamento e elicitação de requisitos |
| Tecnologias | Riscos gerados pela tecnologia usada |
| Complexidade | Riscos gerados pela falta de conhecimento, como equipe de desenvolvimento não se adaptar a tecnologia escolhida |
| Qualidade | Riscos decorrentes da qualidade do produto final |

### 3.2. Risco de Gerenciamento

| **Tipo** | **Descrição** |
| --- | --- |
| Estimativa | Riscos que podem afetar o tempo de produção do projeto |
| Controle | Riscos relacionados ao controle de atividades |
| Planejamento | Riscos relacionados ao planejamento de confecção do projeto |
| Comunicação | Riscos relacionados às atividades e meio de comunicação, como falta de comunicação da equipe |

### 3.3. Risco Organizacional

| **Tipo** | **Descrição** |
| --- | --- |
| Recursos | Riscos gerados pela falta de material humano e/ou tecnológico, como perda ou defeitos em equipamentos ou membros que abandonam o projeto. |
| Priorização | Riscos gerados pela má escolha de histórias na Sprint |
| Dependências | Riscos que podem afetar a evolução do projeto |

### 3.4. Risco Externo

| **Tipo** | **Descrição** |
| --- | --- |
| Cliente | Riscos gerados pelo cliente em relação ao produto, como mudanças no escopo devido a um pedido do cliente |
| Greve na UnB | Risco gerado pela paralisação de atividades na UnB |

## 4. Identificação dos Riscos

| **ID** | **Se** | **por conta** | **o impacto será** | **Categoria EAR** |
| --- | --- | --- | --- | --- |
| RN01 | o projeto não atender os requisitos | do levantamento de requisitos falho e falta de validação constante | atraso na entrega do produto e necessidade de redefinição dos requisitos | Requisitos |
| RN02 | a tecnologia usada apresentar problemas | do seu proprietário | atraso na entrega do produto e necessidade de troca de tecnologia equivalente | Tecnologias |
| RN03 | O arquiteto não conseguir planejar e garantir a execução da arquitetura | da falta de conhecimento das tecnologias do projeto | dificuldade na organização e atraso no desenvolvimento | Complexidade |
| RN04 | Equipe de desenvolvimento não se adapta a tecnologia escolhida | da falta de conhecimento das tecnologias do projeto | produto não será entregue | Complexidade |
| RN05 | Houverem dificuldades em realizar os testes | da falta de conhecimento | atraso na entrega das histórias planejadas | Complexidade |
| RN06 | O DevOps não conseguir automatizar o deploy e a integração contínua | de falta de conhecimento | atraso na entrega do produto em ambiente de produção | Complexidade |
| RN07 | O DevOps não conseguir automatizar o deploy e a integração contínua | de indefinição da Arquitetura do projeto | atraso na entrega do produto em ambiente de produção | Complexidade |
| RN08 | o produto final estiver em baixa qualidade | da equipe de desenvolvimento | refazer todo o produto | Qualidade |
| RN09 | as atividades não forem concretizadas no prazo | da falta de integração da equipe de desenvolvimento | atraso na baseline do projeto | Estimativa/Dependência |
| RN10 | Houver histórias de usuário mal definidas | de falta elicitação de requisitos de forma adequada | atraso na entrega do produto e necessidade de redefinição das histórias | Estimativa |
| RN11 | Houver Sprint mal planejada | de histórias mal planejadas | atraso na entrega do produto, dificuldade na compreensão das histórias e necessidade de replanejamento | Estimativa/Priorização |
| RN12 | Houver mudança no escopo | da falha no planejamento | Atraso ou projeto não ser concluído a tempo | Planejamento |
| RN13 | Houver falta de comunicação na equipe | da não utilização dos meios de comunicação definidos | dificuldade no gerenciamento da equipe por parte do Scrum Master e falta de alinhamento da equipe | Comunicação |
| RN14 | Houver problemas na comunicação da equipe | do número de membros | dificuldade no gerenciamento da equipe por parte do Scrum Master e falta de alinhamento da equipe | Comunicação |
| RN15 | Membros da equipe abandonarem o projeto | da desmotivação | sobrecarga entre os membros restantes | Recursos |
| RN16 | se houver perda ou defeitos em equipamentos | mal uso | atraso na entrega do projeto | Recursos |
| RN17 | Houver o cancelamento do projeto | de falta de interesse do cliente | interrupção do projeto | Cliente |
| RN18 | A qualidade do software não corresponder às expectativas do cliente | Má implementação | Descontentamento do Cliente e possibilidade de cancelamento do projeto | Cliente/Qualidade |
| RN19 | houver greve na UnB | de orientações de assembleias do corpo docente ou estudantil | interrupção do projeto | Greve na UnB |

## 5. Interpretação

| **ID** | **Impacto** | **Probabilidade** | **Avaliação** | **Contingência** | **Mitigação** |
| --- | --- | --- | --- | --- | --- |
| RN01 | Crítico | Muito Alta | 25 | Revalidar todo os requisitos com o Product Owner e com o cliente | Realizar constantes reuniões entre os membros da equipe, com o cliente e pesquisas necessárias para obtenção de conhecimento e compreensão sobre o escopo do projeto |
| RN02 | Crítico | Baixa | 10 | Trocar para uma tecnologia equivalente | Escolher uma tecnologia com suporte |
| RN03 | Crítico | Alta | 16 | Realizar a mudança na Arquitetura do projeto buscando outras tecnologias capazes de solucionar os problemas ocorridos | Buscar conhecimento com outros alunos, professores, pessoas de fora da comunidade universitária, novas pesquisas e/ou cogitar a mudança de tecnologias |
| RN04 | Grande | Alta | 16 | Indicar treinamentos para a equipe de desenvolvimento sobre a tecnologia escolhida | Estabelecer treinamentos constantes sobre a tecnologia escolhida |
| RN05 | Crítico | Alta | 20 | Indicar treinamentos para a equipe de desenvolvimento sobre testes | Estabelecer treinamentos constantes sobre testes |
| RN06 | Grande | Alta | 16 | Procurar ajuda de alunos, professores, pessoas de fora do ambiente universitário e aumentar a carga de estudos | Realização de pesquisas constantes e consultoria com outros alunos, professores e pessoas de fora do ambiente universitário |
| RN07 | Grande | Alta | 16 | Procurar ajuda de alunos, professores, pessoas de fora do ambiente universitário e aumentar a carga de estudos, por parte do Arquiteto | Realização de pesquisas constantes e consultoria com outros alunos, professores e pessoas de fora do ambiente universitário, por parte do Arquiteto |
| RN08 | Crítico | Muito Alta | 25 | Realizar refatoração de código, testes e validação com o cliente | Realizar treinamentos de todas as tecnologias utilizadas, garantir a realização de testes, boas práticas de programação e validação com o cliente |
| RN09 | Crítico | Muito alta | 25 | Realizar a entrega na próxima Sprint como dívida técnica e, talvez, realocá-la para uma dupla com mais facilidade com a tecnologia | Planejar as atividades e dividi-las nas sprints com base nos pesos e dificuldade definida no planning poker |
| RN10 | Grande | Muito alta | 20 | Realizar um replanejamento das histórias para que entrem em conformidade com os requisitos | Realizar constantes reuniões entre os membros da equipe, com o cliente e pesquisas necessárias para obtenção de conhecimento e compreensão sobre o escopo do projeto |
| RN11 | Grande | Alta | 16 | Realizar replanejamento da sprint utilizando a priorização do backlog do produto | Montar o backlog da sprint utilizando a priorização do backlog do produto |
| RN12 | Crítico | Baixa | 10 | Redefinir o quanto antes as mudanças de escopo | Manter sempre a comunicação com o cliente |
| RN13 | Crítico | Alta | 20 | Reafirmar a necessidade de um alto grau de comunicação e promover as mudanças necessárias, desde realização de daily meetings mais objetivas a mudanças de ferramentas para comunicação | Criando o Plano de comunicação em que a equipe demonstre comum acordo |
| RN14 | Crítico | Alta | 20 | Reafirmar a necessidade de um alto grau de comunicação e promover as mudanças necessárias, desde realização de daily meetings mais objetivas a mudanças de ferramentas para comunicação | Criando o Plano de comunicação em que a equipe demonstre comum acordo |
| RN15 | Grande | Muito alta | 20 | Realocar as tarefas entre os membros presentes | Conversar com a equipe a fim de reafirmar a importância do projeto para que a equipe o priorize |
| RN16 | Grande | Média | 12 | Realocar as tarefas entre os membros com equipamentos que funcionam | Incentivar a manutenção recorrente de equipamentos |
| RN17 | Crítico | Muito Baixa | 5 | Oferecer a melhor possibilidade de produto para o cliente | Manter comunicação constante com o cliente |
| RN18 | Crítico | Muito Alta | 25 | Realizar refatoração de código, testes e validação com o cliente | Realizar treinamentos de todas as tecnologias utilizadas, garantir a realização de testes, boas práticas de programação e validação com o cliente |
| RN19 | Crítico | Média | 15 | Aceitar o risco | - |

### 5.1. Tabela de Probabilidade

| **Probabilidade** | **Intervalo** | **Peso** |
| --- | --- | --- |
| Muito Baixa |  menor que 10% | 1 |
| Baixa | de 10% a 25% | 2 |
| Média | de 25% a 50% | 3 |
| Alta | de 50% a 75% | 4 |
| Muito Alta | maior que 75% | 5 |

### 5.2. Tabela de Impacto

| **Impacto** | **Descrição** | **Peso** |
| --- | --- | --- |
| Insignificante | Impacto insignificante para o andamento do projeto | 1 |
| Pequeno | Impacto com pouca influência no andamento do projeto | 2 |
| Moderado | Impacto notável para o andamento do projeto | 3 |
| Grande | Impacto grave para o andamento do projeto | 4 |
| Crítico | Impacto crítico para o andamento do projeto | 5 |

### 5.3. Avaliação dos Riscos

A avaliação dos riscos é feita multiplicando o peso da probabilidade pelo peso do impacto.

| **Impacto/Probabilidade** | **Muito Baixa** | **Baixa** | **Média** | **Alta** | **Muito alta** |
| --- | --- | --- | --- | --- | --- |
| **Insignificante** | **1** | **2** | **3** | **4** | **5** |
| **Pequeno** | **2** | **4** | **6** | **8** | **10** |
| **Moderado** | **3** | **6** | **9** | **12** | **15** |
| **Grande** | **4** | **8** | **12** | **16** | **20** |
| **Crítico** | **5** | **10** | **15** | **20** | **25** |

## 6. Referências

PMI (2017), **UM GUIA DO CONHECIMENTO EM GERENCIAMENTO DE PROJETOS (GUIA PMBOK®)**, 6ª Ed.

BARCELOS, Filipe; ARAUJO Igor; NAVES, Lucas; LIMA, Shermam. **NaturalSearch - Plano de Gerenciamento de Riscos. Disponível em:** https://fga-eps-mds.github.io/2018.2-NaturalSearch/docs/Plano\_de\_Risco.html

VILARINS, Augusto; FRANÇA, Emanoel; SOARES, Ingrid. **GamesBI - Riscos.** Disponível em: https://fga-eps-mds.github.io/2018.2-GamesBI/viabilidade/riscos.html