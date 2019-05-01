# Plano de Medição

| **Data** | **Versão** | **Descrição** | **Autor** |
| --- | --- | --- | --- |
| 17/04/2019 | 1.0 | Criação da primeira versão do documento | Ateldy Brasil |

## 1. Objetivo

O projeto em desenvolvimento necessita de melhoria constante, tanto no processo, quanto no produto. Para realizar o acompanhamento, a equipe precisa definir estratégias que sejam objetivas para facilitar na identificação de impedimentos. Nesse contexto, o processo de medição é uma forma de captura de dados para que a equipe possa diagnosticar problemas e o Scrum Master possa mitigar e conter riscos e tomar decisões rápidas para assegurar o desenvolvimento do projeto.

Para a análise de esforço de cada tarefa ou história de usuário, foi estimado um _ponto_ seguindo a metodologia _scrum_. Esse ponto é importante para a análise em métricas e ferramentas utilizadas. 

## 2. Indicadores da Qualidade do Processo

### 2.1. Burndown da Sprint
A ferramenta _Burndown da Sprint_ é uma representação gráfica que mostra a quantidade restante de trabalho do Backlog da Sprint, ao longo dos dias de duração da Sprint. Neste projeto o  esforço estimado está em _pontos_.

Para o auxílio da coleta desta métrica, é usado a ferramenta ZenHub rastrear o Burndown da equipe, sprint a sprint.


### 2.2. Burndown de Riscos
A ferramenta _Burndown de Riscos_ é uma representação gráfica que  organiza e apresenta a soma dos valores de avaliação dos riscos. Ele possui uma escala de 0 a 25 para cada risco acontecer, de acordo com a tabela de avaliação presente no Plano de Gerenciamento de Riscos. 

Para cada Sprint, os riscos podem cair de acordo com a mitigação e contenção e a avaliação pode ser alterada, gerando um declínio no gráfico.

### 2.3. Velocity

É uma métrica que demonstra a produtividade da equipe por sprint. É calculado através do somatório das estimativas originais (pontos planejados) de todos os trabalhos aceitos naquela sprint (pontos queimados). Para o auxílio da coleta desta métrica, é usado a ferramenta ZenHub rastrear a velocidade da equipe, sprint a sprint.

### 2.4. Work Capacity

A métrica Work Capacity (capacidade de trabalho) é definida como a soma de todo o esforço relatado durante o Sprint. Em cada _daily meeting_ o Scrum Master é responsável por coletar a estimativa de esforço diário de cada membro na unidade de _pontos_. Ao final da Sprint, a Work Capacity total do time é comparada à soma total de pontos planejadas. Quando mais similares, significa que a estimativa foi bem feita e não houve esforço em excesso para concluir tarefas.

A Capacidade de Trabalho foi usada no início do projeto para definir o nosso _ponto_ e estimar melhor a pontuação de cada história de usuário e tarefas.

A Work Capacity pode, em raras ocasiões, cair abaixo da Velocity. Isso ocorre porque a Velocity é calculada com base nas estimativas originais do trabalho, enquanto a Work Capacity é calculada com base na soma do trabalho real relatado. Neste cenário de inversão raro, indica que a equipe tem superestimado a complexidade do trabalho solicitado.

### 2.5. Targeted Value Increase (TVI+)
A métrica de _Targeted Value Increase (TVI+)_ é calculada da seguinte maneira:

> Velocity da Sprint Atual ÷ Velocity da Sprint Original (Sprint 0)

Essa métrica demonstra o quão maior/menor é a entrega de pontos em relação a sprint original(sprint 0).

### 2.6. Quadro de Conhecimento 
É uma ferramenta que evolui a cada sprint, e propicia a visualização da evolução técnica da equipe, e possíveis pontos de risco com tecnologias adotadas. 

|Nível|Pontos|
|-----|---|
|alto |  3|
|médio|	2|
|baixo|	1|
|nenhum|	0|

## 3. Referências

Downey, Scott, e Jeff Sutherland. **“Scrum Metrics for Hyperproductive Teams: How They Fly like Fighter Aircraft”**. In 2013 46th Hawaii International Conference on System Sciences, 4870–78. Wailea, HI, USA: IEEE, 2013. https://doi.org/10.1109/HICSS.2013.471.
