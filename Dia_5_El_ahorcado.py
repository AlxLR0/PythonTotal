#Métodos, Ayuda y Documentación
from operator import truediv

from Dia_3_Analizador_de_texto import mein_lista

dic= {'c1':1, 'c2':2}
dic.popitem()
#funciones
def saludo():
    print('hola')

#funcion con return
def suma(num1,num2):
    return num1 + num2
r = suma(10,20) #guardar en una variable

def potencia (base,exponente):
    resultado = base**exponente
    return resultado

"""
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para suministrarle como argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.
"""

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra
palabras_lista = "python"

invertir_palabra(palabras_lista)

#funciones dinamicas

def checar_3_cifras(lista):

    lista_nueva=[]

    for n in lista:
        if n in range(100,1000): #checar si un numero_string esta dentro del rango de 100 a 999
            lista_nueva.append(n)
           #return True si algún argumento es de 3 cifras regresa true
        else:
            pass  #caso contrario lo deja pasar
    return lista_nueva
   # return False #al completar las vueltas regresara el false si es necesario

res= checar_3_cifras([555,959,600])

"""
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
"""
lista_numeros = [1, 50, 500, 5000, 750, 600]

def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma

"""
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
"""
lista_numeros= [1,50,502,5000,755,600,33,61]

def cantidad_pares(lista_numeros):
    cantidad = 0
    for n in lista_numeros:
        if n % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad


#interaccion entre numeros
from random import *
#lista inicial
palitos=['-','--','---','----']

#mezcla
def mezclar(lista):
    shuffle(lista)#shuffle sirve para mezclar elementos aleatorios
    return lista

#pedir intento
def probar_suerte():
    intento=''

    while intento not in ['1','2','3','4']: #se crea un loop donde si el numero_string del intento no esta del 1 al 4 sele pide que agregue uno valido
        intento = input("Elige un numero_string del 1 al 4: ") #se hace con strings ya que sea lo que sea el interprete lo tomara como un string

    return int(intento)#ya después de castea a int para manipular los datos como integers


#comprobar intento
def checar_intento(lista,intento):
    if lista[intento -1]=='-':
        print('perdiste')
    else:
        print('te salvaste')
    print(f'te toco {lista[intento-1]}')

#mandar llamar todo
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
checar_intento(palitos_mezclados,seleccion)



"""
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

    La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

    Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

    "La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

    "La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
"""
def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


"""
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

    Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

    Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
"""

lista_numeros = [1, 2, 15, 7, 2, 8]

import random


def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado


def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista


#*args argumentos indefinidos args=arguments
#es una funcion a la cual se le permiten x cantidad de argunentos

def sumita(*args): #para que permita que se le puedan pasar x cantidad de argumentos a la funcion
    total = 0
    #forma 1 de sumar para estos casos tambien sirve para multiplicar etc.
    #for arg in args:
    #    total+=arg
    #return total

    #forma 2 y mas simple para sumar en estos casos
    return sum(args)

print(sumita(100,500,400))


"""
Práctica sobre Argumentos Indefinidos (*args) 1

Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.


Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
"""


def suma_cuadrados(*args):
    total = 0

    for arg in args:
        total += arg ** 2
    return total


suma_cuadrados(1, 2, 3)

"""
Práctica sobre Argumentos Indefinidos (*args) 2

Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
"""
def suma_absolutos(*args):
    total = 0
    for argumento in args:
        total += abs(argumento) #abs es para sacar el valor absoluto de los numeros (El valor absoluto es la distancia de un número a cero en la recta numérica, por lo que siempre es un número no negativo (positivo o cero))
    return total
"""
Práctica sobre Argumentos Indefinidos (*args) 3

Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
"""

def numeros_persona(nombre,*args):
    total= sum(args)
    return f"{nombre}, la suma de tus números es {total}"

#**kwargs esto es keyboard args que ayuda con los argumentos de los diccionaros en una funcion, se le pueden pasar clave y valor a una funcion para trabajar con ella
def sumonona(**kwargs):
    #print(type(**kwargs))
    total=0
    for clave,valor in kwargs.items():
        print(f"{clave}={valor}")
        total+=valor
    return total
print(sumonona(x=3,y=5,z=1))

print()
"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio.
"""

def devolver_distintos(n1,n2,n3):
    numeros=[n1,n2,n3]
    total=n1+n2+n3
    if total>15:
        return f"los numeros son {n1}, {n2}, {n3}\nla suma es {total}\nel numero_string maximo es {max(n1, n2, n3)}"
    elif total<10:
        return  f"los numeros son {n1}, {n2}, {n3}\nla suma es {total}\nel numero_string minimo es {min(n1,n2,n3)}"
    elif total>=10 and total<=15:
        numeros.sort()
        return f"los numeros son {n1}, {n2}, {n3}\nla suma es {total}\nel numero_string intermedio es {numeros[1]}"



devolver_distintos(5,6,7)
print(devolver_distintos(5, 6, 7))


print()

"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
"""

def palabra(palabra):
    palabra_lista=list(palabra)
    eliminar_repetidos= set(palabra_lista)
    numeros_ordenados = sorted(eliminar_repetidos)
    return numeros_ordenados

print(palabra('entretenido'))

print()
"""
proyecto dia 5 el ahorcado
"""
print("---El Ahorcado----")
vidas = 6 #cantidad de vidas
palabra_oculta = '' #aqui se guardara la palabra ya oculta
palabras_lista = ["python", "manzana", "perro", "gato", "hola", "bichis"] #lista de palabras disponibles
palabra_secreta=choice(palabras_lista)#aqui guardamos la seleccion del elemento al azar con choice
palabra_secreta = palabra_secreta.lower()#convertir a mins

print(palabra_secreta)
palabra_oculta= "_" * len(palabra_secreta) # guardar en la variable la multiplicacion de un guion por cada elemento de la palabra usando len
print(palabra_oculta)

print(f"La palabra tiene {len(palabra_secreta)} letras.")

letra = input("Elige una letra: ") #pedir letra
letra = letra.lower()
#len(letra) == 1 se asegura de que el jugador haya puesto una sola letra, no una palabra o una tecla vacía. y .isalpha() devuelve True si todos los caracteres en la cadena son letras (a–z o A–Z) y no contiene números, espacios ni símbolos.
if len(letra) == 1 and letra.isalpha():

    if letra in palabra_secreta:

        palabra_oculta = list("_" * len(palabra_secreta))
        for i in palabra_oculta:
            #palabra_oculta[i] = letra
            pass
        print("hell yeah baby tu letra esta en la palabra oculta")
    else:
        print("nop, intenta de nuevo")
else:
    print("nop, intenta de nuevo")



"""
otra fakin solucion
"""
palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palbra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra!!!")

    return True


palabra, letras_unicas = elegir_palbra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado
#pedir letra

#validar letra

#checar letra

#ver si gano



