Dado que Python es la base para aprender MicroPython, es necesario seguir algún tutorial de los ofrecidos en línea para aquellos que no tienen conocimientos básicos de Python. Puedes encontrar muchos libros y materiales de aprendizaje relacionados con Python en línea, así que aquí simplemente daremos algunos materiales de aprendizaje rápido de Python 3 que pueden servir como diccionario de Python.

Documentación basada en:

<center>**Ponte al día con Python 3 en 10 minutos, por Louie Dinh, traducido por Geoff Liu**</center>

## <FONT COLOR=#007575>**Comentarios**</font>

~~~py
# Los comentarios de una sola línea comienzan con un símbolo de número (#)

""" Las cadenas de varias líneas se escriben entre comillas triples
    y también se utilizan habitualmente para comentar varias líneas
    de código.
"""
~~~

## <FONT COLOR=#007575>**Tipos de datos y operadores**</font>

~~~py
####################################################
## 1. Tipos de datos primitivos y operadores
####################################################

# entero
3  # => 3

# No hay nada inesperado en la aritmética
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20

""" Sin embargo, la división es una excepción y se convertirá
automáticamente a un número de coma flotante."""
35 / 5  # => 7.0
5 / 3  # => 1.6666666666666667

# El resultado de la división entera siempre se redondea hacia abajo
5 // 3     # => 1
5.0 // 3.0 # => 1.0 # Los números de coma flotante también son aceptables
-5 // 3  # => -2
-5.0 // 3.0 # => -2.0

# El resultado de una operación de coma flotante también es un número de coma flotante
3 * 2.0 # => 6.0

# módulo
7 % 3 # => 1

# x elevado a la potencia y
2**4 # => 16

# Utiliza paréntesis para establecer jerarquia de operaciones
1 + 3 * 2  # => 7
(1 + 3) * 2  # => 8

# Valores booleanos
True
False

# Utiliza 'not' para negar
not True  # => False
not False  # => True

# Operadores lógicos, ten en cuenta que tanto 'and' como 'or' se escriben en minúscula
True and False # => False
False or True # => True

# Los números enteros también pueden tratarse como valores booleanos
0 and 2 # => 0
-5 or 0 # => -5
0 == False # => True
2 == True # => False
1 == True # => True

# Utiliza == para comprobar la igualdad de una condición
1 == 1  # => True
2 == 1  # => False

# Utiliza el operador '!=' (distinto) para comprobar la desigualdad de una condición
1 != 1  # => False
2 != 1  # => True

# Comparar valores
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Comparar valores vinculados entre si
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# Las cadenas pueden encerrarse entre comillas simples o dobles
"Esto es una cadena"
'Esto también es una cadena'

# Para concatenar cadenas utiliza el signo más
"¡Hola " + "mundo!"  # => "¡Hola mundo!"

# Las cadenas se pueden tratar como listas de caracteres
"Esto es una cadena"[0]  # => 'E'

# Utiliza .format para dar formato a las cadenas
print("{} pueden ser {}".format("Las cadenas", "interpoladas")) 
# => Las cadenas pueden ser interpoladas

# Los parámetros pueden repetirse para ahorrar tiempo
print("{0} es ágil, {0} es rápido, {0} salta por encima del {1}".format("Pedro", "muro alto"))
# => Pedro es ágil, Pedro es rápido, Pedro salta por encima del muro alto

# Si no deseas enumerar los parámetros, puedes utilizar palabras clave
print("{nombre} quiere comer {comida}".format(nombre="Fede", comida="canelones"))
# => Fede quiere comer canelones

# None (Ninguno) es un objeto
None  # => None

# Al comparar con None, no utilices `==`; en su lugar, utiliza `is`. 
# El operador `is` se utiliza para determinar si dos variables apuntan al mismo objeto
"etc" is None  # => False
None is None  # => True

# None (Ninguno), 0, cadenas vacías, listas vacías y diccionarios vacíos se consideran False.
# Todos los demás valores son verdaderos (True).
bool(0)  # => False
bool("")  # => False
bool([]) # => False
bool({}) # => False
~~~

## <FONT COLOR=#007575>**Variables y conjuntos de datos**</font>

~~~py
####################################################
## 2. Variables y conjuntos de datos
####################################################

# print es la función de impresión integrada
print("Soy Python. ¡Encantado de conocerte!") # => Soy Python. ¡Encantado de conocerte!

# # No es necesario declarar las variables antes de asignarlas
# La nomenclatura convencional de las variables utiliza letras minúsculas
# con guiones bajos para separar las palabras
alguna_variable = 5
alguna_variable  # => 5

# El acceso a una variable no inicializada generará una excepción.
# Consulta la sección de control de flujo para más información del manejo de excepciones
alguna_variable_desconocida # => Lanza NameError

# Almacenar secuencias utilizando listas
lista = []
# Al crear una lista, también puedes asignarle valores a sus elementos
otra_lista = [4, 5, 6]

# Añade elementos al final de una lista utilizando append
lista.append(1)    # ahora es lista[1]
lista.append(2)    # ahora es lista[1, 2]
lista.append(4)    # ahora es lista[1, 2, 4]
lista.append(3)    # ahora es lista[1, 2, 4, 3]
# Eliminar del final de la lista utilizando pop
lista.pop()        # => Elimina el, lista ahora es [1, 2, 4]
# Vuelve a colocar los 3 en su sitio
lista.append(3)    # ahora es lista[1, 2, 4, 3]

# El acceso a elementos de la lista se hace igual que en las matrices
lista[0]  # => 1
# Recuperar el último elemento
lista[-1]  # => 3

# El acceso fuera de límites dará lugar a un IndexError
lista[0]  # => Genera IndexError

# Operador de corte
lista[1:3]  # => [2, 4]
# Extracción desde el índice hasta el final
lista[2:]  # => [4, 3]
# Extracción desde el principio hasta el indice menos uno
lista[:3]  # => [1, 2, 4]
# Extrae uno cada dos
lista[::2]   # =>[1, 4]
# Invertir la lista
lista[::-1]   # => [3, 4, 2, 1]
# El corte se puede construir utilizando cualquier combinación de los tres parámetros
# lista[Inicio:Fin: Paso]

# Utiliza 'del' para eliminar cualquier elemento
del lista[2]   # ahora es lista[1, 2, 3]

# Las listas se pueden sumar
# Nota: Los valores de lista y otra_lista permanecen sin cambios
lista + otra_lista   # => [1, 2, 3, 4, 5, 6]

# Concatenar listas utilizando `extend`
lista.extend(otra_lista)   # ahora es lista[1, 2, 3, 4, 5, 6]

# Utiliza el operador 'in' para comprobar si una lista contiene un valor
1 in lista   # => True

# Utiliza 'len' para obtener la longitud de la lista
len(lista)   # => 6

# Las tuplas son colecciones inmutables
tupla = (1, 2, 3)
tupla[0]   # => 1
tupla[0] = 3  # Lanza TypeError


# La mayoria de operaciones de listas se aplican a las tuplas
len(tupla)   # => 3
tupla + (4, 5, 6)   # => (1, 2, 3, 4, 5, 6)
tupla[:2]   # => (1, 2)
2 in tupla   # => True

# Puedes extraer una tupla y asignar sus valores a variables
a, b, c = (1, 2, 3)     # Ahora a es 1, b es 2 y c es 3
# Se pueden omitir los paréntesis en las tuplas
d, e, f = 4, 5, 6
# Intercambiar los valores de dos variables es así de sencillo
e, d = d, e     # Ahora d es 5 y e es 4

# Diccionarios
diccionario_vacio = {}
# Diccionario inicializado
diccionario = {"uno": 1, "dos": 2, "tres": 3}
# Utiliza [] para recuperar valores
diccionario["uno"] # => 1

# Utiliza 'keys' para obtener todas las claves
# Como las claves devuelven un objeto iterable, el resultado se envuelve en una lista aquí
# Nota: El orden de las claves del diccionario no está especificado; tu resultado puede diferir del siguiente
list(diccionario.keys())   # => ["tres", "dos", "uno"]

# Utiliza `values` para obtener todos los valores. Al igual que con `keys`, 
# los devuelve en una lista, y el orden puede variar
list(diccionario.values())   # => [3, 2, 1]

# Utiliza 'in' para comprobar si un diccionario contiene una clave
"uno" in diccionario   # => True
1 in diccionario   # => False

# El acceso a una clave inexistente dará lugar a un error KeyError.
diccionario["cuatro"]   # KeyError

# Utiliza 'get' para evitar KeyError
diccionario.get("uno")   # => 1
diccionario.get("cuatro")   # => None
# Cuando la clave no existe, el método get puede devolver un valor predeterminado
diccionario.get("uno", 4)   # => 1
diccionario.get("cuatro", 4)   # => 4

# El método `setdefault` solo inserta un nuevo valor cuando la clave no existe
diccionario.setdefault("cinco", 5)  # diccionario["cinco"] establecer como 5
diccionario.setdefault("cinco", 6)  # filled_dict["cinco"] todavia es 5

# Asignación de diccionario
diccionario.update({"cuatro":4}) # => {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4}
diccionario["cuatro"] = 4  # Otro método de asignación

# Eliminar con 'del'
del diccionario["uno"]  # Eliminar 'uno' de diccionario

# Usar 'set' para crear estructuras de datos
estructura = set()
# Se inicializan con una sintaxis similar a la de un diccionario
some_set = {1, 1, 2, 2, 3, 4}   # some_set ahora es {1, 2, 3, 4}

# Un conjunto puede asignarse a una variable
variable = some_set

# Añadir elementos al conjunto
variable.add(5)  # some_set ahora es {1, 2, 3, 4, 5}

# Operador & o intersección
other_set = {3, 4, 5, 6}
variable & other_set  # => {3, 4, 5}

# Operador | o unión
variable | other_set  # => {1, 2, 3, 4, 5, 6}

# Hacer el complemento
{1, 2, 3, 4} - {2, 3, 5}   # => {1, 4}

# Si el conjunto de pruebas contiene un elemento
2 in variable   # => True
10 in variable   # => False
~~~

## <FONT COLOR=#007575>**Control de flujo e iteradores**</font>

~~~py
####################################################
## 3. Control de flujo e iteradores
####################################################

# Primero, define una variable arbitrariamente
una_var = 5
# Esta es una instrucción if
# Ten en cuenta que la sangría es lo correcto en la sintaxis en Python
# Imprime como es el valor de 'una_var' respecto de 10
if una_var > 10:
    print("La variable es mayor que 10")
elif una_var < 10:    # La cláusula elif es opcional
    print("La variable es menor que 10")
else:                  # La cláusula `else` también es opcional
    print("La variable es igual a 10")

"""
Recorrer una lista con una instrucción de bucle 'for'
Imprimir:
    El perro es un mamífero.
    El gato es un mamífero.
    El rata es un mamífero.
"""
for animal in ["perro", "gato", "rata"]:
    print("{} es un mamifero".format(animal))

"""
range(number) devuelve una lista de números enteros desde 0 hasta el número dado, incluido este.
Imprimir:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
Bucle 'while'; hasta que la condición ya no se cumpla
Imprimir:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # abreviatura de x = x + 1

# Maneje de excepciones utilizando bloques try/except
try:
    # Generar una excepción utilizando 'raise'
    raise IndexError("Este es un error de índice")
except IndexError as e:
    pass    # pass es una operación nula. Los errores deben gestionarse aquí.
except (TypeError, NameError):
    pass    # Puedes gestionar diferentes tipos de errores simultáneamente
else:   # La cláusula else es opcional y debe seguir a todas las cláusulas except
    print("Todo correcto")   # Esta instrucción solo se ejecutará si el bloque try
                             # se completa sin errores.

# Python proporciona una abstracción fundamental conocida como iterable. 
# Un objeto iterable es aquel que puede tratarse como una secuencia.
# Por ejemplo, el objeto devuelto por la función 'range' anterior es iterable.

diccionario = {"uno": 1, "dos": 2, "tres": 3}
iterable = diccionario.keys()
print(iterable) # => dict_keys(['uno', 'dos', 'tres'])

# Los objetos iterables se pueden recorrer con bucles
for i in iterable:
    print(i)    # Imprimir uno, dos, tres en tres lineas

# Sin embargo, no se permite el acceso aleatorio.
iterable[1]  # Lanza TypeError

# Los objetos iterables se pueden utilizar para generar iteradores.
iterable = iter(iterable)

# Un iterador es un objeto que recuerda su posición.
# Utiliza __next__ para recuperar el siguiente elemento.
iterable.__next__()  # => 'uno'

# Las llamadas posteriores a __next__ recordarán la posición.
iterable.__next__()  # => 'dos'
iterable.__next__()  # => 'tres'

# Una vez que se han recuperado todos los elementos, se genera StopIteration.
iterable.__next__() # Genera StopIteration.

# Todo el contenido de un iterador se puede capturar en una sola llamada a la lista.
print(list(diccionario.keys()))  # => Devuelve ['uno', 'dos', 'tres'].
~~~

## <FONT COLOR=#007575>**Funciones**</font>

~~~py
####################################################
## 4. Funciones
####################################################

# Para definir una nueva función utiliza 'def'
def suma(x, y):
    print("x vale {} ; y vale {}".format(x, y))
    return x + y # 'return' devuelve el resultado
    
print("La suma es:", suma(5, 6))    # x vale 5 ; y vale 6
                                    # La suma es: 11

# Las funciones también se pueden invocar utilizando argumentos clave.
suma(y=6, x=5)   # Los argumentos clave se pueden utilizar en cualquier orden

# Podemos definir una función con argumentos variables.
def varargs(*args):
    return args

varargs(1, 2, 3)   # => (1, 2, 3)

# También podemos definir una función de argumento clave con argumentos variables.
def keyword_args(**kwargs):
    return kwargs

# Veamos cuál es el resultado:
keyword_args(big="foot", loch="ness")   # => {"big": "foot", "loch": "ness"}

# Estos dos parámetros variables pueden utilizarse indistintamente.
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
    
all_the_args(1, 2, a=3, b=4)    # El resultado de esta llamada a la función es: 
                                # (1, 2) 
                                # {"a": 3, "b": 4}

# Al llamar a funciones con argumentos variables, se puede hacer lo contrario de lo anterior:
# usar * para expandir listas y ** para expandir diccionarios.
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
    
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args, **kwargs)     # (1, 2, 3, 4)
                                  # {'a': 3, 'b': 4}
# Alternativas:
#all_the_args(*args)       # (1, 2, 3, 4)
                           # {}

#all_the_args(**kwargs)    # ()
                           # {'a': 3, 'b': 4}

# Ámbito de la función
x = 5

def setX(num):
    # La x en el ámbito local es distinta de la x en el ámbito global.
    x = num # => 43
    print (x) # => 43

def setGlobalX(num):
    global x
    print (x) # => 5
    x = num # Ahora se le está asignando un valor a la variable global x.
    print (x) # => 6

setX(43)
setGlobalX(6)

# Las funciones son elementos de primera clase en Python.
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# También hay funciones anónimas.
(lambda x: x > 2)(3)   # => True

# Funciones de orden superior integradas
map(add_10, [1, 2, 3])   # => [11, 12, 13]
filter(lambda x: x > 5, [3, 4, 5, 6, 7])   # => [6, 7]

# Las operaciones con listas pueden simplificar las operaciones de mapeo y filtrado.
# El valor de retorno es otra lista
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]   # => [6, 7]
~~~

## <FONT COLOR=#007575>**Clases**</font>

~~~py
####################################################
## 5. Clases
####################################################

# Definir una clase que herede de 'object'
class Human(object):

    # Atributo de clase, compartido por todas las instancias de esta clase.
    species = "Homo sapiens"

    # Método constructor, llamado cuando se inicializa una instancia. Observa los dos guiones
    # bajos que rodean el nombre, que indican que este atributo o método tiene un significado
    # especial para Python, aunque los usuarios pueden definir los suyos propios.
    # No debes emplear este formato al nombrar los tuyos propios.
    def __init__(self, name):
        # Asigna el argumento al atributo 'name' de la instancia.
        self.name = name

# Los métodos de instancia siempre toman 'self' como su primer parámetro, que hace referencia al propio objeto de instancia.
def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

# Los métodos de clase son compartidos por todas las instancias de esta clase.
# El primer argumento es el propio objeto de clase
@classmethod
    def get_species(cls):
        return cls.species

# Métodos estáticos. No se produce ningún enlace de instancia o clase durante la invocación.
@staticmethod
    def grunt():
        return "*grunt*"

# Construir una instancia
i = Human(name="Juan")
print(i.say("hola"))     # Imprime "Juan: hola"

j = Human("Rafael")
print(j.say("hola"))  # Imprime "Rafael: hola"

# Llamar a un método de una clase
i.get_species()   # => "Homo sapiens"

# Cambiar un atributo de clase
Human.species = "Homo neandertal"
i.get_species()   # => "Homo neandertal"
j.get_species()   # => "Homo neandertal"

# Llamadas a métodos estáticos
Human.grunt()   # => "*grunt*"
~~~

## <FONT COLOR=#007575>**Módulos**</font>

~~~py
####################################################
## 6. Módulos
####################################################

# Importación de módulos mediante 'import'
import math
print(math.sqrt(16))  # => 4.0

# Los valores individuales también se pueden importar desde el módulo
from math import ceil, floor
print(ceil(3.7))  # Redondeo hacia arriba => 4.0
print(floor(3.7))   # Redondeo hacia abajo => 3.0

# Permite importar todos los valores dentro de un módulo
# Advertencia: No se recomienda esta práctica
from math import *

# Abreviar los nombres de los módulos
import math as m
math.sqrt(16) == m.sqrt(16)   # => True

# Los módulos de Python son esencialmente archivos Python normales
# Puedes escribir los tuyos propios e importarlos
# el nombre del módulo es simplemente el nombre del archivo

# Puedes enumerar todos los valores dentro de un módulo de esta manera
import math
dir(math)
~~~

## <FONT COLOR=#007575>**Uso avanzado**</font>

~~~py
####################################################
## 7. Uso avanzado
####################################################

# Utiliza generadores (generators) para escribir cómodamente operaciones
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Los generadores solo calculan el siguiente valor cuando es necesario.
# Producen un único valor por bucle, en lugar de calcular todos los valores.
#
# El valor de retorno de rango también es un generador; de lo contrario, una lista
# de valores del 1 al 900000000 consumiría demasiado tiempo y memoria
#
# Si deseas usar una palabra clave de Python como nombre de variable,
# añada un guion bajo para distinguirla
range_ = range(1, 900000000)
# Detenerse cuando se encuentra un resultado >= 30
# Esto significa que `double_numbers` no generará números mayores que 30
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break

# Decoradores (decorators)
# En este ejemplo, beg decora say
# beg primero llama a say. Si say_please es verdadero, beg modifica la cadena devuelta
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Por favor! Soy pobre :(")
        return msg

    return wrapper

@beg
def say(say_please=False):
    msg = "Puedes comprarme una cerveza?"
    return msg, say_please

print(say())  # Puedes comprarme una cerveza?
print(say(say_please=True))  # Puedes comprarme una cerveza? Por favor! Soy pobre :(
~~~
