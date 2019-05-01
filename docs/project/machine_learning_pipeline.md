# Pipeline Rasa NLU

| **Data** | **Versão** | **Descrição** | **Autor** |
| --- | --- | --- | --- |
| 18/04/2019 | 1.0 | Escolha da pipeline rasa nlu | Bruno Dantas |

## Pipeline Rasa NLU

<p style="text-align:justify">&emsp;&emsp;No Rasa NLU, as mensagens recebidas são processadas por uma sequência de componentes. Esses componentes são executados um após o outro em um chamado pipeline de processamento. Existem componentes para extração de entidade, para classificação de intenção, pré-processamento e outros. Você pode adicionar seu próprio componente, por exemplo, para executar uma verificação ortográfica ou fazer uma análise de sentimento. </p>

<p style="text-align:justify">&emsp;&emsp;Cada componente processa a entrada e cria uma saída. A saída pode ser usada por qualquer componente que venha após esse componente no pipeline. Existem componentes que apenas produzem informações que são usadas por outros componentes no pipeline e há outros componentes que produzem saída de atributos que serão retornados após o processamento ter sido concluído. </p>

## Escolha

<p style="text-align:justify">&emsp;&emsp;O Rasa Nlu possui alguns tipos de pipeline que adequa-se a necessidade de cada projeto. São eles o "spacy_sklearn", "tensorflow_embedding", "mitie" e "mitie_sklearn", com exceção do "tensorflow_embedding" todos os outros possuem maiores limitações. O "spacy_sklearn" é recomendado para projetos que utilizam menos de 1000 exemplos de treinamento total. Já o mitie, o próprio site oficial do Rasa não recomenda sua utilização, pois o mesmo entrará em desuso nas próximas versões. </p>

<p style="text-align:justify">&emsp;&emsp;Dito isso a escolhe ideal é o <i>tensorflow_embedding</i>. </p>

## Tensorflow_embedding

```
language: "pt"

pipeline: "tensorflow_embedding"
```

<p style="text-align:justify">&emsp;&emsp;O <i>tensorflow_embedding</i> comporta mais de 1000 declarações rotuladas. Porém a sua maior vantagem é que seus vetores de palavra serão personalizados para seu domínio. Por exemplo, em geral, a palavra “equilíbrio” está intimamente relacionada à “simetria”, mas muito diferente da palavra “dinheiro”. Em um domínio bancário, "saldo" e "dinheiro" estão intimamente relacionados e você gostaria que seu modelo captasse isso. Esse pipeline não usa um modelo específico de idioma, porém é uma boa prática definir a configuração de linguagem do seu projeto.</p>

<p style="text-align:justify">&emsp;&emsp;Além disso, esse é o único modelo que pode realizar múltiplas intenções que as divide em vários rótulos.</p>


## Referências

- Choosing a Rasa NLU Pipeline. https://rasa.com/docs/nlu/choosing_pipeline/. Acesso em 16/05/2019 - 10:23h;
