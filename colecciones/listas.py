print('*'*5,'LISTAS','*'*5)

mi_lista = [1,2,3,4,5]

print(f'{mi_lista}-> lista original ')

#largo de una lista
print(f'largo de la lista: {len(mi_lista)}')

#acceder a los elementos por indice
print(f'valor indice 4: {mi_lista[4]}')
print(f'valor ultimo indice: {mi_lista[-1]}')

#modificar elementos de una lista
mi_lista[1]=10
print(f'modificar el valor de lindice 1: {mi_lista[1]}')

#agregar nuevo elemento al final de la lista
mi_lista.append(6)
print(f'nuevo elemento: {mi_lista}')

#agregar nuevo elemento en un indice especifico de la lista
mi_lista.insert(2, 15)
print(f'nuevo elemento: {mi_lista}')

#eliminar elemento de una lista
mi_lista.remove(5)
print(f'5 elemento eliminado: {mi_lista}')

#eliminar por indice
mi_lista.pop(1)
print(f'{mi_lista} se removio el indice 1')

#eliminando con la palabra del
del mi_lista[2]
print(f'{mi_lista} se elimino el indice 2')

#obtener sub lista
sublista = mi_lista[1:3]# genera una sublista de lindice 1 al 2 no incluye a l3
print(f'sub lista {sublista}')

print()
print('*'*5,'ITERAR LISTAS','*'*5)
nombres =['funalo','sutano','magnano','aeiuo']

for nombre in nombres:
    print(nombre)

print()
print('*'*5,'Promedio Calificaciones','*'*5)
total_calificaciones = int(input('Proporciona el numero de calificaciones a evaluar: '))
calificaciones=[]

#iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion= float(input(f'calificacion[{indice+1}]: '))
    calificaciones.append(calificacion)

#imprimir las calificaciones proporcionadas
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

#caclular promedio
suma_calificaciones = sum(calificaciones)
promedio= suma_calificaciones / total_calificaciones
print(f'el promedio es {promedio:.2f}')


#nombres en orden alfabetico
print()
nombres.sort()
print(f'{nombres}')
