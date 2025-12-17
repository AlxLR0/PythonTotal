#operadores de comparacion
"""
= asignación
== comparación
!= diferencia
<> mayor y menor
"""

#operadores logicos
"""
and a= 4<5 and 5>6
or  a= 10==10 or 3==3
not a= not 'a' == 'a'
"""

#control de flujo
"""
if = if condición:
        print(variable)
elif= elif otra_condición:
        print(variable_B)
else= else:
        print(variable_C)
"""
#loops

#for
lista = ['a','b','c']
for letra in lista:
    numero_letra = lista.index(letra)+1
    print(f"Letra {numero_letra}: {letra}")
nombres = ['fulano','sutano','mangano']

for nombre in nombres:
    if nombre.startswith('s'): #startswith es pra saber que string inicia con la letra indicada
        print(nombre)

numerotes=[1,2,3,4,5,6,7,8,9]
mein_valor=0
for numero in numerotes:
    mein_valor = mein_valor + numero
print(mein_valor)

#while
"""
while una_condición:
        #codigo
else:
        #otro_codigo
"""
monedas = 5
while monedas>0:
    print(f"Tengo {monedas} monedas")
    monedas-=1
else:
    print("fin")

while monedas ==10:
    pass #esto es para dejar pasar el codigo para revolverlo mas tarde

nombrexD= input("tu neim: ")

for letra in nombrexD:
    if letra == 'r':
        break #rompe la ejecucion del codigo
    print(letra)

#rango range
            #el primer parametro es desde donde inicia y el segundo hasta donde osea que imprime del 1 al 4 y un 3ro puede ser cuantos saltos da el conteo  range(1,5,2)
for numero in range(1,5):
    print(numero)

#otro ejemplo
#aqui casteamos el rango a una lista con list para que se pueda almacenar en una lista correctamente
lista = list(range(1,101))

#enumerate/enumeradaor
lista=['a','b','c']

for indice,item in enumerate(lista):
    print(indice,item)

#convertir a tupla con enumerate
mis_tuples = list(enumerate(lista))

"""
Práctica Enumerador 2

Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices .
"""
palabre ="Python"
lista_indices= list(enumerate(palabre))
print(lista_indices)

#zip esta cosa sirve para juntar tuplas
nombre = ['juan','pablo','ana']
edad= [26,27,29]
ciudades=['gotham','metropolis', 'san ajijic de la pitaya']
combinacion=list(zip(nombre,edad,ciudades)) #para poder ver este resultado en pantalla hay que castear o convertir a una lista
print(combinacion)

for nombre,edad,ciudades in combinacion:
    print(f"{nombre} tiene {edad} años y es de {ciudades}")

#min y max sirve para saber los valores minimos y maximos en por ejemplo una lista
min=min(58,59,6,45,8) #en este caso el minimo es 6
max=max(58,59,6,45,8)# y el maximo es 59

#tambien funciona con alfabeticos
ejemplo_nombres=['benito','camelo','sango','loteo']

#print(min(ejemplo_nombres))

"""
Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:
"""
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

#rango = max(lista_numeros) - min(lista_numeros)

"""
Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre
"""

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
#edad_minima= min(diccionario_edades.values())
#ultimo_nombre = max(diccionario_edades.keys())

#random
from random import *

aleatorio = randint(1,50)#elige un numero_string aleatorio entre el 1 al 50
aleatorio_decimal = uniform(1,5)#este tira aletatorios pero con decimal ejem: 1.00111 esto se puede redondear con round round(uniform(1,5),1) recordar que el ultimo numero_string (es este caso el 1) es la cantidad de decimales a mostrar
aleatorio_total= random() # este elige entre 0 y 1 con algun decimal (tambien se le puede aplicar un round)
colores = ['rojo','verde','azul']
aleatorio_seleccion=choice(colores)#Esta cosa es parecido a los otros pero aca puede elegir un elemento de alguna listra, tupla etc.
pokar=list(range(5,50,5))
shuffle(pokar) #este lo que hace es mezclar los elementos de una lista, tupla etc. a como le de la gana
print(f"el numero_string aleatorio es: {aleatorio}")


#conprencion de listas

palabrona= 'python'
listilla= [letra for letra in palabrona] #aqui lo que estamos haciendo es meter directamente el for a la lista para que haga su chamba y ahorras unas cuantas lineas de codigo sin perder legibilidad
                                        #en lugar de tener la lista vacia y luego el for aparte y usar el metodo apend para llenar la lista por cada letra

#otro ejemplo con numeros en un rango de 0 a 20 saltando de 2 en 2
listilla2=[n for n in range(0,21,2)]
#tambien se pueden hacer cuentas aca se divide cada numero_string entre 2
listilla2a=[n/2 for n in range(0,21,2)]
#tambien se le pueden añadir condicionales en este caso se almacena si el numero_string multiplicado por 2 es mayor a 10
listilla2b=[n for n in range(0,21,2) if n*2>10]
#si se quiere añadir un else ahi ya cambia la cosa aca va al inicio el if/else y en este caso si no cumple la funcion se guardara la palabra nel
listilla2b=[n if n*2>10 else 'nel' for n in range(0,21,2) ]


pies=[10,20,30]
metrobooming=[p/3.281 for p in pies]

#match esta cosa es como el switch

serie = "n1"
match serie:
    case "n1":
        print('a')
    case "n2":
        print('b')
    case _: #Esto es como un default
        print('no hay nada')

#proyecto dia 4 adivina el numero_string

#preguntar nombre del usuario

#num_jugador=int(num_jugador)
#print(type(num_jugador))
intentos = 0
num_jugador=0
#print(type(intentos))
numero_Aleatorio= randint(1,100)

while intentos < 8:
    num_jugador = int(input("Ingresa un numero_string: "))
    intentos+=1
    if num_jugador not in range(1,101):
        print("Numero fuera de rango (1-100)")
    elif num_jugador<numero_Aleatorio:
        print(f"El numero_string secreto es las alto")
    elif num_jugador>numero_Aleatorio:
        print(f"El numero_string secreto es las bajo")
    else:
        print(f"respuesta es correcta\ntu numero_string: {num_jugador}\nnumero_string secreto:{numero_Aleatorio}\nintentos totales: {intentos}")
        break

if num_jugador != numero_Aleatorio:
    print(f"se agotaron los intentos. El numero_string era {numero_Aleatorio}")

