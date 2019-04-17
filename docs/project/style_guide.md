# Folha de estilo

| **Data** | **Versão** | **Descrição** | **Autor(es)** |
| :---: | :---: | :---: | :---: |
| 01/04/2019 | 0.1 | Abertura do documento | João Vitor |
                                                                                            
## 1. Objetivo

Este documento tem como objetivo deixar explícito como o software ADA deve ser programado.


## 2. Como deve ser feito

A linguagem utilizada neste projeto é o Python com o framework Flask. Como uma boa prática de programação todos os métodos, marcadores, variáveis , classes, constantes, exceções, coleções, nomenclatura, sintaxe e os comentários devem seguir o idioma padrão da linguagem, neste caso o inglês.


## 3. Indentação e Espaçamento

O nível de recuo deve ser de apenas quatros espaços em vez do TAB. Esse é o padrão da linguagem Python. Cada linha deve possuir no máximo 79 caracteres e ao finalizar um método deve-se pular apenas uma linha para o início de outro método.


## 4. Sintaxe

### 4.1 Aspas de Strings
No python aspas simples e duplas são as mesmas coisas. Porém por padrão serão utilizadas aspas duplas em todas strings.

### 4.2 Espaços em brancos em expressões e condições
#### 4.2.1 Dentro de de parênteses, colchetes e chaves

##### Exemplo Bom:
```ruby
spam(ham[1], {eggs: 2})
```
##### Exemplo Ruim: 

```ruby
spam( ham[ 1 ], { eggs: 2 } )
```

#### 4.2.2 Entre uma vírgula e fechamento de parêntese

##### Exemplo Bom:
```ruby
foo = (0,)
```
##### Exemplo Ruim:
```ruby
bar = (0, )
```
#### 4.2.3 Imediatamente antes de vírgula, ponto vírgula e dois pontos

##### Exemplo Bom:
```ruby
if x == 4: print x, y; x, y = y, x
```
##### Exemplo Ruim:
```ruby
if x == 4 : print x , y ; x , y = y , x
```

#### 4.2.4 Imediatamente antes de abertura de parênteses que inicia lista de argumentos de uma chamada de função 

##### Exemplo Bom: 
```ruby
spam(1)
```
##### Exemplo Ruim:
```ruby
spam (1)
```
#### 4.2.5 Imediatamente antes da abertura de chaves que iniciam indexamento 

##### Exemplo Bom: 
```ruby
dct[‘key’] = lst[index]
```

##### Exemplo Ruim:
```ruby
dct [‘key’] = lst [index]
```
#### 4.2.6 Mais de um espaço em atribuições ou operações  

##### Exemplo Bom: 
```ruby
x = 1
long_variable = 3
```
##### Exemplo Ruim:
```ruby
x       = 1
long_variable      = 3
```

#### 4.2.7 Utilizar um espaço em branco para os seguintes operadores (=, +, -,  <, >, +=, -=, !=,  >=, <=, *, and, or, not in, is, is not) e sem espaço em branco quando o operador realizar uma conta como no exemplo abaixo

##### Exemplo Bom: 
```ruby
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
##### Exemplo Ruim:
```ruby
i=i+1
submitted+=1
x=x * 2-1
hypot2=x * x+y * y
c=(a + b)*(a - b)
```

#### 4.2.8 Não utilizar espaço em branco entre (=) quando indicado para atribuir palavra chave

##### Exemplo Bom: 
```ruby
def complex(real, img=0.0):
	return magic(r=real, i=imag)
```

##### Exemplo Ruim:
```ruby
def complex(real, img = 0.0):
	return magic(r = real, i = imag)
```
#### 4.2.9 Assinaturas de métodos devem seguir as mesmas regras de espaços para vírgulas 

##### Exemplo Bom: 
```ruby
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...
``` 

##### Exemplo Ruim:
```ruby
def munge(input:AnyStr): ...
def munge()->AnyStr: …
```

## 5. Padronização

#### 5.1 Flake8
Para a garantia de uma formatação padronizada do código, utilizaremos o plugin [Flake8](https://pypi.python.org/pypi/flake8). O Flake8 combina 3 ótimas ferramentas em um só pacote:
<ul> 
<li>Pep8 que verifica se o estilo do código respeita o padrão adotado pela comunidade descrito na Python Enhancement Proposal 8.</li>
<li>PyFlakes que analisa estaticamente seu código detectando inúmeros anti-patterns e erros lógicos como módulos importados que não são utilizados, uso de variáveis não declaradas, entre muitas outras coisas.</li>
<li>Codepaths que realiza a análise da complexidade ciclomática do código com base nas métricas de McCabe.</li>
</ul>
   
## 6. Importações 

#### 6.1 Importações sempre devem ser feitas em linhas separadas.
##### Exemplo Bom:
```ruby
import os
import sys
```
##### Exemplo Ruim:
```ruby
import os,sys
```

##### Sem problemas dessa forma:
```ruby
from subprocess import Popen, PIPE
```

## 7. Comentários

#### 7.1 Os comentários devem ser frases completas, e iniciadas com letras maiúsculas.

##### Exemplo Bom
```ruby
# I'm a long comment, you should've notice that my lenght is being
# Greater quickly.
```
##### Exemplo Ruim
```ruby
# i'm a long comment, you should've notice that my lenght is being
# greater quickly
```


#### 7.2 Os comentários deve ser escritos em inglês.

#### 7.3 Use comentários de bloco em vez de comentários de linha.

##### Exemplo Bom:
```ruby
"""
comment line
another comment line

"""
```

##### Exemplo Ruim:
```ruby
# Aaaaa.
# Comment line.
# Another comment line.
```

## 8. Nomenclatura

#### 8.1 Todas as variáveis do projeto devem ser em inglês.
#### 8.2 Os nomes das classes devem seguir o CamelCase.
#### 8.3 O snake_case devem ser utilizados como:
<ul>
<li>símbolos</li>
<li>métodos</li>
<li>variáveis</li>
<li>nomes de arquivos</li>
<li>nomes de diretórios</li>
</ul>

#### 8.4 Os nomes de pacotes e módulos devem ser curtos, todos com letras minúsculas. Os sublinhados podem ser usados no nome do módulo se melhorar a legibilidade.
#### 8.5 Os nomes das funções devem ser minúsculas, com palavras separadas por sublinhados, conforme necessário, para melhorar a legibilidade.


## 9. Referências
Disponível em <https://github.com/fga-eps-mds/2017.2-Classificacao-de-Risco-Pediatrico/wiki/Folha-de-Estilo> Acesso em 01 de Abril de 2019.<br />
Disponível em <https://www.python.org/dev/peps/pep-0008/> Acesso em 01 de Abril de 2019.











