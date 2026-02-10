from functools import  reduce

print('*'*5,'lambda','*'*5)
'''
La función lambda en Python crea pequeñas funciones anónimas (sin nombre) de una sola línea de expresión,
diseñadas para tareas breves, simples y desechables. Se definen rápidamente usando la palabra clave lambda,
pueden recibir múltiples parámetros pero solo ejecutan una expresión, devolviendo el resultado automáticamente. 
'''

# Lambda para elevar al cuadrado
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Resultado: 25



print()
print('*'*5,'map','*'*5)
'''
a función
map() combinada con lambda en Python aplica una operación pequeña y anónima (lambda) a cada elemento de un iterable (como una lista o tupla) sin necesidad de un bucle for explícito.
Devuelve un iterador (objeto map) con los resultados transformados de manera eficiente. 
'''

numeros = [1,2,3,4,5]

#obtener el cuadrado de cada numero

cuadrados = list(map(lambda x:x**2,numeros))
print(cuadrados)

print()
print('*'*5,'filter','*'*5)

'''
La función
filter() junto con lambda en Python se utiliza para extraer elementos de un iterable (como una lista o tupla) que cumplen una condición específica,
devolviendo solo aquellos para los cuales la función lambda evalúa como True. Es una forma concisa y funcional de filtrar datos sin necesidad de usar bucles for explícitos. 
'''
# Usando lambda con filter() para obtener números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Resultado: [2, 4, 6]


print()
print('*'*5,'reduce','*'*5)
'''
La función reduce() en Python, combinada con una expresión lambda (importada desde functools), aplica una operación de forma acumulativa a los elementos de una lista, reduciéndolos a un solo valor.
Toma dos argumentos: una función que define la operación (generalmente lambda x, y: ...) y un iterable, procesándolo de izquierda a derecha. 
'''

suma_Acomulativa = reduce(lambda x,y: x+y, numeros)
print(suma_Acomulativa)



print()
print('*'*5,'sorted','*'*5)
'''
La función sorted() en Python, combinada con lambda en el parámetro key, permite ordenar iterables (listas, tuplas, diccionarios)
basándose en un criterio personalizado y específico en lugar del orden predeterminado.
La función lambda actúa como una regla de transformación rápida para cada elemento antes de compararlos. 
'''

nums = [3, 1, 4, 2]
desc = sorted(nums, reverse = True) # [4, 3, 2, 1]
print(desc)

