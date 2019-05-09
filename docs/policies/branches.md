# Política de Branches

| Data       | Versão | Descrição            | Autor             |
|:----------:|:------:|:--------------------:|:-----------------:|
| 21/03/2019 | 0.1 | Criação do documento com template inicial  | João Vitor, Bruno Dantas, Ateldy Brasil e Vitor Gomes|

As braches devem seguir o seguinte padrão:

* O nome da branch deve ser abstraído do nome da história de usuário a qual se refere.

<b>Exemplo:</b>

```
CriarLogin
```

* O nome da branch deve possuir um 'tag' que é o número da história de usuário a qual se refere.

<b>Exemplo:</b>

```
3CriarLogin
```

* A branch deverá possuir o padrão CamelCase ```x-NomeDaBranch ```, em que o 'x' é o número da história de usuário.

<b>Exemplo:</b>

```
3-CriarLogin
```

* Caso a branch não esteja associada a alguma história de usuário, não é necessario a adição da 'tag'.

<b>Exemplo:</b>

```
RefatorarLogin
```