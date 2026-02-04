#conjuntos
'''
Un set en Python es una colección desordenada de elementos únicos (no permite duplicados) e inmutables,
similar a un conjunto matemático, ideal para operaciones de pertenencia y eliminación de duplicados,
 creada con {} o set() y que soporta agregar/quitar elementos pero no acceder por índice como listas.
'''
print('*'*5,'SETS','*'*5)

mi_set = {1,2,3,4,5,5}
print(mi_set)

#agregar nuevo elemento
mi_set.add(6)
mi_set.add(7)

#eliminar un elemento
mi_set.remove(4)

print()
print('*'*5,'Operaciones con SETS','*'*5)
a={1,2,3}
b={3,4,5}

union = a | b
print(f'Union a|b: {union}')

inserseccion = a & b
print(f'inserseccion a&b: {inserseccion}')

diferencia = a - b
print(f'diferencia a-b: {diferencia}')


print()
print('*'*5,'Agregar un nuevo numero','*'*5)
nuevo_numero= int(input('Ingresa un nuevo numero: '))

if nuevo_numero in mi_set:
    print('este elemento ya existe')
else:
    mi_set.add(nuevo_numero)
    print('se añadio elemento a la lista')
print(mi_set)


