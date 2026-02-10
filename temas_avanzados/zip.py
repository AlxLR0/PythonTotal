print('*'*5,'ZIP','*'*5)

'''
La función
zip() en Python es una herramienta incorporada que toma múltiples iterables (como listas, tuplas o cadenas)
y los combina en un solo iterador de tuplas. Empareja el primer elemento de cada iterable, luego el segundo,
y así sucesivamente,siendo ideal para procesar datos relacionados en paralelo o crear diccionarios. 
'''

nombres = ["Ana", "Bob"]
edades = [25, 30]
ciudades = ["tangamandapio","ajijic de la montaña"]
for nombre, edad,ciudad in zip(nombres, edades,ciudades):
    print(nombre, edad,ciudad) # Resultado: Ana 25, Bob 30
