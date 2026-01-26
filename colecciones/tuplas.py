print('*'*5,'TUPLAS','*'*5)
mi_tupla=(1,2,3,4,5)
tupla_un_elemento = 10, #👈 para que se le considere una tupla unitaria esta debe ir con una coma al final si o si
tupla_anidada=(1,2,3,4,5,(1,2,3))

print()
print('*'*5,'DESEMPAQUETADO DE TUPLAS (UNPACKING)','*'*5)
producto = ('p001', 'Camisa', 200)
id, descripcion, precio = producto[0], producto[1], producto[2]

print(f'ID: {id}\nDESCRIPCION: {descripcion}\nPRECIO: {precio}')

print()
print('*'*5,'Combinar listas y tuplas','*'*5)
productos = [
    ('p001', 'camisa', 2),
    ('p002', 'jeans', 3),
    ('p003', 'sudadera', 2),
]

precio_total = 0

print('Información de los productos:')
# Desempaquetamos directamente en la cabecera del for
for id_p, desc, precio in productos:
    print(f'ID: {id_p}\nDESCRIPCION: {desc}\nPRECIO: {precio}\n')
    precio_total += precio

print(f'Precio total: {precio_total}')