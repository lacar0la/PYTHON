# Regular expressions

Tambien se conocen con regex o regexp, son esencialmente una consulta de busqueda de texto que se expresa mediante un patrón de cadena. Cuando se ejecuta una busqueda en un fragmento de texto concreto, todo lo que coincida con un patrón de expresión regular especificado se devuelve como resultado de la busqueda. Las expresiones regulares permiten responder preguntas como:

- Cuales son todas las palabras de cuatro letras en un archivo
- Cuantos tipos de error diferente hay en este registro de errores.

En otras palabras las expresiones regulares permiten realizar una busqueda de texto entre strings buscando un patrón especifico.

Conocer las expresiones regulares ayuda a realizar procesamiento de texto.

Para usar las expresiones regulares en python es posible por ejemplo importar el modulo RE y usar la función search para encontrar las expresiones regulares dentro del string

```jsx
import re
log = "july 31 07:51:48 mycomputer bad_process[12345]: ERROR performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex,log)
print(result[1])
12345
```

## reserved characters

A dot matches every character (something like a comodin)

```jsx
grep l.rts
a**lerts**
b**lurts**
f**lirts**
```

Con el simbolo ^ es posible revisar si la busqueda se encuentra al inicio de la palabra, y $ para revisar si la busqueda está al final de una linea.

```jsx
grep ^fruit
**fruit**
**fruit**'s
**fruit**cake
**fruit**ion
```

Esta expresión regular permite revisar un texto y encontrar las palabras que estoy buscando- Atención, devuelve:
indices donde fue encontrado y el tipo de similitud

```jsx
print(re.search(r"___". text)

```

## Wildcards and character classes

Usar un punto en una expresión regular puede servir como “comodín” pues el punto puede ser reemplazado por cualquier caracter. Que sucede si deseamos tener una revisión mucho mas estricta, por ejemplo realizar una revisión de los caracteres validos en un string, buscar por ejemplo si un CSV inicia con una vocal. 

Es posible restringir los comodines a un rango de caracteres, para ello se usan otro tipo de expresiones regulares que se llaman CHARACTER CLASSES, estas son escritas dentro de parentesis cuadrados que nos permiten listar los caracteres que deseamos encontrar.(la información se escribe dentro de los parentesis)

Así mismo dentro de los paretesis cuadrados podemos definir el rango de caracteres usados en el dash. Por ejemplo podemos usar de “a” a “z” minusculas, que permita revisar si exise algún match que coincida.

> *Recuerda que la idea es que estos sean comodines pero mucho mas restringidos*
> 

```c
print(re.search(r"[a-z]way", "the end of the highway"))
<re.March object; span(18,22), match = "hway">
```

Tambien es posible por ejemplo usar el circunflejo para evaluar cuando un caracter no se encuentra dentro de un arreglo

```c
print(re.search(r"[^a-zA-Z]way", "This is a sentence with spaces"))
<re.March object; span(4,4), match = "' '" >
El primer match es un escpacio porque se encuentra fuera del rango que le dimos a la expresión
```

## Operador “o”

Entre las expresiones regulares tambien tenemos el operador “o” que nos permite buscar una coincidencia o la otra, de la siguiente manera.

```c
print(re.search(r"cat|dog", "I like cats."))
<re.March object; span(7,10), match = 'cat'> 
print(re.search(r"cat|dog", "I like dogs."))
<re.March object; span(7,10), match = 'dog'> 
print(re.search(r"cat|dog", "I like dogs and cats."))
<re.March object; span(7,10), match = 'dog'> 
```

Cuando usamos el operador “o” y el texto contiene ambos elementos de busqueda, la respuesta corresponderá unicamente a la primera aparición de una de las palabras, 

## Findall()

Si queremos ver las coincidencias entonces lo recomendable es trabajar con la función findall(), sin embargo recuerda que este operador solamente te mostrará si la palabra aparece, no indica el numero de ocurrencias, posiciones, etc.

```c
print(re.findall(r"cat|dog", "i like both dogs and cats"))
['dog', 'cat']

```

## Multiples ocurrencias

Para la busqueda de multiples ocurrencias, es posible usar expresiones que incluyen un punto seguido por una asterisco, esto significa que coincide con cualquier caracter repetido tantas veces como sea posible incluyendo el cero.  

El asterisco toma tantos caracteres como sea posible, en programación a este tipo de comportamiento se le conoce como codicioso. 

Como se aclaró anteriormente, la implementación de expresiones regulares no siempre es la misma, los calificadores de repetición hacen la diferencia, algunas implementaciones pueden usar un solo calificador como se ha presentado en los ejemplos previos. En python pueden encontrarse implementaciones que incluyen 2 calificadores de repetición adicionales como el signo de suma y la marca de pregunta que puede ayudarnos a construir expresiones mucho mas complejas. El simbolo de suma permite revisar las courrencias del caracter que viene antes.

```c
print(re.search(r"o+l+", "goldfish"))
<re.March object; span(1,5), match = 'ol'> 

print(re.search(r"o+l+", "woolly"))
<re.March object; span(1,5), match = 'ooll'>

print(re.search(r"o+l+", "boil"))
None
```

Si no se logra asegurar el mismo patrón, la respuesta de la busqueda retornará un None, como en el ultimo ejemplo.

The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work.

```c
import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*a", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
```

El simbolo de pregunta es otro multiplicador, esto significa cero o una aparición del caracter anterior

```c
print(re.search(r"p?each", "To each their own"))
<re.March object; span(3,7), match = 'each'> 

print(re.search(r"p?each", "I like peaches"))
<re.March object; span(7,12), match = 'peach'>
```

Si quisieramos revisar que un numero tiene exactamente.2 digitos podremos revisarlo mediante el operador:

- `{m}` Especifica que exactamente *m* copias de la RE anterior deben coincidir; menos coincidencias hacen que la RE entera no coincida. Por ejemplo, `a{6}` coincidirá exactamente con seis caracteres `'a'`, pero no con cinco.
- `{m,n}` Hace que el RE resultante coincida de *m* a *n* repeticiones del RE precedente, tratando de coincidir con el mayor número de repeticiones posible. Por ejemplo, `a{3,5}` coincidirá de 3 a 5 caracteres `'a'`. Omitiendo *m* se especifica un límite inferior de cero, y omitiendo *n* se especifica un límite superior infinito. Por ejemplo, `a{4,}b` coincidirá con `'aaaab'` o mil caracteres `'a'` seguidos de una `'b'`, pero no `'aaab'`. La coma no puede ser omitida o el modificador se confundiría con la forma descrita anteriormente.
- `{m,n}?` Causes the resulting RE to match from *m* to *n* repetitions of the preceding RE, attempting to match as *few* repetitions as possible. This is the non-greedy version of the previous quantifier. For example, on the 6-character string `'aaaaaa'`, `a{3,5}` will match 5 `'a'` characters, while `a{3,5}?` will only match 3 characters.

## Escaping characters

Que sucede si deseamos realizar una busqueda especial donde queremos saber si un texto contiene “.” . Los caracteres de escape son aquellos que cuando se añaden a una busqueda permiten restringirla y hacerla literal de modo que limitan el campo de acción de los caractes especiales.

Añadir un backslash es una forma de escapar de los caracteres especiales. Pero, este no es el unico uso que tienen los backslash en python, por ejemplo podemos contar:

- \n para una nueva linea
- \t para tabulación
- \w en caso de que tenga coincidencia con cualquier caracter alfanumerico
- \d para digitos
- \s para coincidencias con espacios, lineas o saltos de linea.
- `\b`Coincide con la cadena vacía, pero sólo al principio o al final de una palabra. Una palabra se define como una secuencia de caracteres de palabras. Notar que formalmente, `\b` se define como el límite entre un carácter `\w` y un carácter `\W` (o viceversa), o entre `\w` y el principio/fin de la cadena. Esto significa que `r'\bfoo\b'` coincide con `'foo'`, `'foo.'`, `'(foo)'`, `'bar foo baz'` pero no `'foobar'` o `'foo3'`.

Siempre debemos recordar que usar backslash para escapar de un caracter especial, debe entonces incluir un caracter especial. (Suena redundante, ¿no?, quizás si, pero nos evitará confusiones y la idea de asumir que si hay un backslash entonces en todas las ocasiones corresponderá a un escape)

*Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.*

```c
import re
def check_character_groups(text):
  result = re.search(r"\w\s+\w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
```

Esta pagina permite realizar analisis de expresiones y permite realizar un analisis de cada consulta.

[regex101: build, test, and debug regex](https://regex101.com/)

```c
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
```

Pattern es una expresion que permite revisar si la busque inicia con una letra, el resto puede variar entre letras o numeros y puede terminar de cualquier manera

*Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.*

```c
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z]*(\s[a-z]+)*[\.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
```

**^** asserts position at start of a line

**Match a single character present in the list below [A-Z]**

**A-Z** matches a single character in the range between A **(index 65)** and Z **(index 90)** (case sensitive)

**Match a single character present in the list below [a-z]**

* matches the previous token between **zero** and **unlimited** times, as many times as possible, giving back as needed (greedy)

**a-z** matches a single character in the range between a **(index 97)** and z **(index 122)** (case sensitive)

**1st Capturing Group (\s[a-z]+)***

*matches the previous token between **zero** and **unlimited** times, as many times as possible, giving back as needed (greedy)

> A repeated capturing group will only capture the last iteration. Put a capturing group around the repeated group to capture all iterations or use a non-capturing group instead if you're not interested in the data
> 

**\s** matches any whitespace character (equivalent to [\r\n\t\f\v ])

**Match a single character present in the list below [a-z]**

**+** matches the previous token between **one** and **unlimited** times, as many times as possible, giving back as needed (greedy)

**a-z** matches a single character in the range between a **(index 97)** and z **(index 122)** (case sensitive)

**Match a single character present in the list below [\.!\?]**

**\.** matches the character . with index **4610** (**2E16** or **568**) literally (case sensitive)

! matches the character ! with index **3310** (**2116** or **418**) literally (case sensitive)

**\?** matches the character ? with index **6310** (**3F16** or **778**) literally (case sensitive)

**$** asserts position at the end of a line

**Global pattern flags**

**g modifier:** **g**lobal. All matches (don't return after first match)

**m modifier:** **m**ulti line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)

[Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

[re — Regular expression operations](https://docs.python.org/3/library/re.html)

The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc.

```c
import re
def check_web_address(text):
  pattern = r"^\S+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
```

## Capturing groups

```c
import re
def capturing_groups (text):
  result = re.search(r"^(\w*), (\w*)$", text)

text = lovelace, Ada

print(result)
	<re.March object; span(0,13), match = 'Lovelace, Ada'> 

print(result.groups())
	('Lovelace', 'Ada')<- esto es una lista
print(result[1])
	Lovelace
print(result[2])
	Ada
```

## Función split() y función sub del modulo RE

Opera del mismo modo que la función split para strings, busca un caracter especial y realiza el split conforme el resultado

```c
import re
def split_function (text):
  result = re.split(r"[.?!]", text)

text = One sentence. Another one? and the last one!

print(result)
	["One sentence",'Another one', 'and the last one','']
```

Es posible realizar la captura tambien de los signos de puntuación para que aparezcan en el resultado del split, de la siguiente manera

```c
import re
def split_function (text):
  result = re.split(r"([.?!])", text)

text = One sentence. Another one? and the last one!

print(result)
	["One sentence",'.','Another one','?','and the last one','!','']
```

La función sub, realiza una busqueda y reemplaza información de acuerdo al criterio dado.
