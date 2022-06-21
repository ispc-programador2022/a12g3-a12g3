def ing2i():
    num1 = int( input("Ingrese un numero: "))
    num2 = int( input("Ingrese otro numero: "))
    return [num1,num2]

def ing2s():
    str1 = input("Ingrese una palabra: ")
    str2 = input("Ingrese otra palabras: ")
    return [str1, str2]

def presentacion():
    print("********************************")
    print("Calculadora ISPC TP Nro 1")
    print("********************************")

presentacion()
numeros = ing2i()
#palabras = ing2s()

from itertools import product
from suma import suma
print("La suma es: " + str( suma(numeros[0], numeros[1]) ))

from resta import resta
print("La resta es: " + str( resta(numeros[0], numeros[1]) ))

from producto import producto
print("El producto es: " + str( producto(numeros[0], numeros[1]) ))

from cociente import cociente
print("El cociente es: " + str( cociente(numeros[0], numeros[1]) ))

from modulo import modulo
print("El modulo es: " + str( modulo(numeros[0], numeros[1]) ))

from potencia import potencia
print("La potencia es: " + str( potencia(numeros[0], numeros[1]) ))

# Pido al usuario ingresar el 3er parametro y lo agrego a la lista numeros
numeros.append(int(input("Ingrese otro numero: ")))

from p1_producto import p1
print("El producto de los 2 primero más el 3er parámetro es: " + str( p1(numeros[0], numeros[1], numeros[2]) ))

from p1_suma import p1
print("La suma de los 2 primeros por el 3er parámetro es: " + str( p1(numeros[0], numeros[1], numeros[2]) ))

from p1_resta import p1
print("La resta de los 2 primeros por el 3er parámetro es: " + str( p1(numeros[0], numeros[1], numeros[2]) ))

from aleatorios50 import genrnd
lista_aleatoria_50 = genrnd()
print (lista_aleatoria_50)


# 13
# 14
# 15

# 16
from media_vector import media_vector
print("La media del vector aleatorio es: " + str(media_vector(lista_aleatoria_50)))

# 17
from mediana_vector import mediana_vector
print("La mediana del vector aleatorio es: " + str(mediana_vector(lista_aleatoria_50)))

# 18 Rango del vector

# 19 Varianza

# 20
from minimo_vector import minimo_vector
print("El valor minimo del vector aleatorio es: " + str(minimo_vector(lista_aleatoria_50)))

# 21
from maximo_vector import maximo_vector
print("El valor maximo del vector aleatorio es: " + str(maximo_vector(lista_aleatoria_50)))
