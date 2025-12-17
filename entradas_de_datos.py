#para convertir tipos de datos
from random import randint

#variable str a int
numero_string= "50"

total = int(numero_string)
print(type(total))

#str a float
total_float = float(numero_string)
print(type(total_float))

#float a str
numero= 10.9
total_cadena = str(numero)
print(type(total_cadena))


#bool() = es el mecanismo de python para determinar la existencia o el vacio de un dato
"""
FALSY :                     Truty:
representan nada o vacio    cualquier cosa que existe
0 (cero int/float)          1,-5,3.14 (no cero)
"" (str vacio)              "hola", " " (no vacio/espacios)
[] (lista vacia)            [0] (listas con datos)
none (ausencia de valor)    True

Numeros
print(bool(0))  False
print(bool(45)) True

Cadenas
print(bool("")) False
print(bool(" ")) True
"""

#se tiene que castear (convertir un tipo de dato a otro) los inputs del usuario ya que siempre seran str

numero = input("escribe un numero: ")
print(f"RESULTADO SIN CASTEAR { type(numero)}")
numero = int(numero)
print(f"RESULTADO CASTEADO INT() { type(numero)} 👈 esto ya se puede utilizar en funciones matematicas")

"""
otra forma para no escribir tanto codigo:

numero_2= int(input("escribe un numero: "))
print(numero_2+3)
"""

#EJERCICIO 1

nombre_empleado = input("Nombre del empleado: ")
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe = input('es jefe de depto? (si/no): ')

#convertir a un tipo bool la variable de es_jefa
es_jefe = es_jefe.lower() == 'si'

print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}') #:.2f para tener dos puntos decimales por ejemplo 25.36
print(f'Es jefe: {es_jefe}')



print('**Generador de id**')
nombre = input('Escribe tu nombre: ')
apellido = input('Escribe tu apellido: ')
anio_nacimiento= input('Escribe tu año de nacimiento (yyyy): ')

#normalizar datos
#Strip() es para quitar espacios al inicio y final de la cadena
nombre_normalizado = nombre.strip().upper()[0:2] #se crea el substring para partir el nombre (fulano = FU)
apellido_normalizado= apellido.strip().upper()[0:2]#lo mismo aca
anio_normalizado = anio_nacimiento.strip()[2:]#aqui se recuperan o se parten los dos ultimos digitos del año 1995 -> (95)

#generar valor aleatorio

aleatorio = randint(1001,9999)

#generar id unico
id_unico=f'{nombre_normalizado}{apellido_normalizado}{anio_normalizado}'

print(f'{nombre} {apellido} tu id es: {id_unico}')

