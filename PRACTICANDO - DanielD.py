Residencial = "R"
Comercial = "C"
Industrial = "I"

KwhConsumidos = int(input("Introduzca la cantidad de kwh consumidos: "))
tipoinstalacion = input("Introduzca el tipo de instalacion: ")

if tipoinstalacion == "R":
    if KwhConsumidos >= 500:
        precio = 550
    else:
        precio = 850

if tipoinstalacion == "C":
    if KwhConsumidos >= 1000:
        precio = 1300
    else:
        precio = 2500

if tipoinstalacion == "I":
    if KwhConsumidos >= 5000:
        precio = 3800
    else:
        precio = 4200

if precio:
    print("Precio = ", precio)

  #  Programa
# Un programa es un conjunto de pasos lógicos escritos en un lenguaje de programación que nos permite realizar una tarea específica.

# Programacion
# La programación es el proceso de crear un conjunto de instrucciones que le dicen a una computadora como realizar algún tipo de tarea

# Lenguaje programacion
# Un lenguaje de programación, en palabras simples, es el conjunto de instrucciones a través del cual los humanos interactúan con las computadoras

# Bug o error de sotware
# es un problema en un programa de computador o sistema de software que desencadena un resultado indeseado

# Git
# Git es un sistema de control de versiones, un software que sirve básicamente para gestionar las versiones por las que va pasando el código de los proyectos.

# Github
# GitHub es un servicio basado en la nube que aloja un sistema de control de versiones (VCS) llamado Git

# Tipos de datos
# Los tipos de datos básicos de Python son los booleanos, los numéricos (enteros, punto flotante y complejos) y las cadenas de caracteres.

# Variable
# Una variable es una forma de identificar, de forma sencilla, un dato que se encuentra almacenado en la memoria del ordenador.

# Expresiones constantes:
# son las expresiones que solo tienen valores constantes.
# Expresiones aritméticas: una expresión aritmética es una combinación de valores numéricos, operadores y, a veces, paréntesis.


# Comentario
# Un comentario es una línea de texto no ejecutable, esto quiere decir que el compilador o intérprete no la tomará como una línea de código.
# Tabulacion
# Las tabulaciones pueden ir en conjunto con los saltos de línea o no. Cada tabulación, en Python equivale a pulsar la tecla "TABULADOR" de nuestro teclado.


# Cadenas de strings
# Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.

# Sentencia if
# Utilice la sentencia IF para determinar el flujo del programa en función de la evaluación de expresión. Si el valor de expresión es verdadero, se ejecutan las sentencias THEN. Si el valor de expresión es falso, se omiten las sentencias THEN y se ejecutan las sentencias ELSE.

# Sentencia for
# El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código.

# Sentencia while
# El bucle while es otra estructura de control de flujo, concretamente lo que hace es repetir un código mientras dure una determinada condición.

# Break
# la instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.

# Continue
# La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.


# Funciones definidas por el usuario
# En programación, una función es un grupo de instrucciones con un objetivo particular y que se ejecuta al ser llamada desde otra función o procedimiento. ...
# Las funciones pueden recibir datos desde afuera al ser llamadas a través de los parámetros y puede entregar un resultado.

# Variables locales
# En Python las variables locales son aquellas definidas dentro de una función. Solamente son accesibles desde la propia función y dejan de existir cuando esta termina su ejecución.

# Precondiciones
# Las precondiciones son las condiciones que deben cumplir los parámetros recibidos por una función.
