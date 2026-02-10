print('*'*5,'Comprensión de listas','*'*5)

'''
La comprensión de listas en Python es una
forma concisa y elegante de crear nuevas listas basadas en iterables existentes (listas, rangos, etc.) en una sola línea de código.
Sustituye los bucles for tradicionales por una sintaxis más rápida y legible: [expresión for elemento in iterable if condición]. 
'''

# Sin comprensión de listas (bucle for)
numeros = [1, 2, 3, 4]
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)

# Con comprensión de listas
cuadrados = [n ** 2 for n in numeros] # Resultado: [1, 4, 9, 16]

# Crear lista de pares
numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0] # Resultado: [2, 4, 6]

