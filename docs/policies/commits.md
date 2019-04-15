# Política de Commits

| Data       | Versão | Descrição            | Autor             |
|:----------:|:------:|:--------------------:|:-----------------:|
| 20/03/2019 | 0.1 | Criação do documento com template inicial  | João Vitor, Bruno Dantas, Ateldy Brasil e Vitor Gomes|

 Os commits devem seguir o seguinte padrão:

* Devem ser escritos em inglês na forma infinitiva, e ainda conter uma breve decrição.

<b>Exemplo: <b>

```
Create a new document.
```

* A issue em questão deve ser citada no commit, para isso, basta adicionar 
``` #<numero_da_issue>. ```

<b>Exemplo: <b>

```
#5 Create a new document.
```

<b>Observação: </b> Por padrão, o caracter # define uma linha de comentário no arquivo da mensagem do commit. Para resolver este problema, use o commando:

```
git config --local core.commentChar '!'
```

* Para que ambos envolvidos no commit sejam incluidos como contribuintes no gráfico de commits do GitHub, basta incluir a instrução ```Co-authored-by:``` na mensagem:

<b>Exemplo: <b>

```
#5 Create a new document.

Co-authored-by: Bruno Oliveira Dantas <oliveiradantas96@gmail.com>
Co-authored-by: Ateldy Brasil <ateldybfilho@gmail.com>
```

* Para commits que encerram a resolução de uma issue, deve-se iniciar a mensagem do commit com Fix ```#<numero_da_issue> <mensagem>```, para que a issue seja encerrada automaticamente quando mesclada na ```master```.

<b>Exemplo: <b>

```
Fix #5 Create a new document.
```

* Para commits que incluem uma pequena mudança em uma issue que já teve sua resolução encerrada, deve-se iniciar a mensagem do commit com HOTFIX ```#<numero_da_issue> <mensagem>```

<b>Exemplo: <b>

```
HOTFIX #5 Add new anwser.
```