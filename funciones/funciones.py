print('*'*5,'Funciones','*'*5)

def sumar (a,b):
    return a+b


#prueba de la funcion sumar par que solo se ejecute aqui
if __name__ == '__main__':
    print(f'Prueba funcion sumar desde el modulo : {sumar(15,30)}')

#Regresar una tupla de valores desde una función en Python
def persona_mayus(nombre, apellido, edad):
    print(f'Funcion regresa varios valores en tupla')
    return (nombre.upper(), apellido.upper(), edad)

persona=persona_mayus('fulano', 'fulanoide', 666)
print(persona)

#unpacking de la tupla
nombre, apellido, edad = persona


#alcance de variables

#variable global
contador_global=0
def incrementar_contador():
    #variable local
    contador_local =0

    #para poder usar la variable global se tiene que usar la palabra reservada "global" al inicio, si no se tomara como una diferente
    global contador_global

print()
'''*args
*args en Python permite que una función acepte un número variable de argumentos posicionales, empaquetándolos en una tupla dentro de la función
'''
print('*'*5,'*args','*'*5)
def superheroe_superpoderes(super,nombre,*args):
    print(f'superjiro: {super} - {nombre}-{args}')

#llamar la funcion
superheroe_superpoderes('spiterman','piter', 'nada, dormir, y ya')

'''
Los
kwargs (keyword arguments) en Python son una sintaxis especial (**kwargs) que permite pasar un número variable de argumentos nombrados (clave-valor)
a una función. Recopilan estos argumentos en un diccionario,
lo que proporciona flexibilidad para manejar entradas de longitud variable y mejorar la reutilización del código
'''
print()
print('*'*5,'*kwargs','*'*5)

def new_hero(nombre, *args, **kwargs):
    print(f'hero: {nombre}-{args}- mas info: {kwargs}')

#llamar la funcion
new_hero('spiterman','instinto aracnido', edad=98 , empresa='marvel')


print()
print('*'*5,'par o inpar','*'*5)

def es_par(num):
    if num%2==0:
        return True
    else:
        return False

print(es_par(5))

print()
print('*'*5,'Funciones recursivas','*'*5)

#definir funcion recursiva
def funcion_recursiva(numero):
    #caso base
    if numero == 1:
        print(numero, end=' ')
    else: #caso recursivo
        funcion_recursiva(numero -1)
        print(numero, end=' ')

funcion_recursiva(5)


print()
print('*'*5,'Factorial de un número con recursividad ','*'*5)
#definir funcion

def factorial_recursiva(numero):
    #caso base, factorial 0! = 1,1!=1
    if numero == 0 or numero == 1:
        print(f'resultado factorial parcial {numero} es: 1')
        return 1
    else: #caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero-1)
        print(f'resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

factorial_recursiva(5)