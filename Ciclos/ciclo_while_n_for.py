import random

from numpy.random import randint

print('*'*5,'While','*'*5)
contador=1
while contador <= 5:
    print(contador)
    contador+=1

print()
print('*'*5,'While suma acumulativa','*'*5)
MAX=5
numero=1
acumulador_suma=0
while numero<=MAX:
    #imprimir lo que se va a sumar
    print(f'(acumulador_suma+ numero) -> {acumulador_suma} + {numero}')
    acumulador_suma+=numero
    numero += 1

print(f'resultado suma acomulada: {acumulador_suma}')

print()
print('*'*5,'While menu','*'*5)
salir = False
while not salir:
    print(f'''MENU:
    1.-Crear cuenta
    2.-Eliminar cuenta
    3.-Salir''')
    opcion=int(input('escoje un opcion: '))

    if opcion == 1:
        print('creando cuenta..')
    elif opcion == 2:
        print('Eliminando cuenta..')
    elif opcion == 3:
        print('saliendo..')
        salir = True
    else:
        print('opcion invalida')

print()
print('*'*5, 'Numero secreto', '*'*5)

INTENTOS_MAXIMOS = 5
intentos = 0
numero_Secreto = randint(1, 50)
numero = None

while numero != numero_Secreto and intentos < INTENTOS_MAXIMOS:
    numero = int(input('Ingresa un numero (1-50): '))

    if numero < 1 or numero > 50:
        print('❌ El número debe estar entre 1 y 50')
        continue

    intentos += 1

    if numero < numero_Secreto:
        print('El NUMERO SECRETO ES MAYOR')
    elif numero > numero_Secreto:
        print('El NUMERO SECRETO ES MENOR')

if numero == numero_Secreto:
    print(f'🎉 Adivinaste el número secreto {numero_Secreto} en {intentos} intento(s)')
else:
    print(f'😢 Se agotaron tus intentos máximos ({INTENTOS_MAXIMOS})')


print()
print('*'*5,'Triangulo simetrico','*'*5)
numero_filas = int(input('Proporciona numero de filas: '))

#iterar sobre cada fila del trangulo
for fila in range(1, numero_filas+1):
    # Calcula los espacios en blanco necesarios para centrar el triángulo
    # En las primeras filas hay más espacios y van disminuyendo
    espacios_blanco = ' ' * (numero_filas - fila)

    # Calcula la cantidad de asteriscos por fila
    # Se usa la fórmula (2 * fila - 1) para que siempre sea un número impar
    # y así el triángulo quede simétrico
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{asteriscos}')



print()
print('*'*5,'For','*'*5)
cadenona='hola mundo'
for letra in cadenona:
    print(letra, end='-')