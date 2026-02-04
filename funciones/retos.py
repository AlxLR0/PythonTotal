import math
print()
print('*'*5,'Calcular la potencia de un número con recursividad','*'*5)

def potencia_numero(base,exponente):
    #a**b=a*a**(b-1)
    #caso base
    if exponente == 0:
        return 1
    else: #caso recursivo
        return base * potencia_numero(base,exponente-1)


print(potencia_numero(2,3))


print()
print('*'*5,'sistema inventario','*'*5)

#inventario del almacen
inventario =[
    {'id':1, 'nombre':'camisa', 'precio': 55.99, 'cantidad':50},
    {'id':2, 'nombre':'pantalon', 'precio': 100.99, 'cantidad':30},
    {'id':3, 'nombre':'zapatos', 'precio': 78.99, 'cantidad':50},
]

#funcion para mostar el inventario
def mostrar_inventario():
    print('inventario almacen')
    for producto in inventario:
        print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")}, Precio {producto.get("precio")}, cantidad: {producto.get("cantidad")}')

def agregar_producto():
    print('Agregar nuevo producto')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre':nombre, 'precio':precio, 'cantidad':cantidad}
    inventario.append(nuevo_producto)

    print('producto agregado al inventario 🎉')

def buscar_producto_id():
    print('Buscar producto id')
    id_buscar = int(input('ingresa el id a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('Informacion del producto')
            print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")}, precio: {producto.get("precio")},cantidad: {producto.get("cantidad")}')
            return
    print('Producto no encontrado')


#programa principal
if __name__ == '__main__':
    while True:
        print(f'''
        1. mostrar inventario
        2. agregar a inventario
        3. buscar por id
        4. salir
        
    ''')
        opc= int(input('proporciona una opcion: '))
        if opc == 1:
            mostrar_inventario()
        elif opc == 2:
            agregar_producto()
        elif opc == 3:
            buscar_producto_id()
        elif opc == 4:
            print('fin....')
            break
        else:
            print('opcion invalida, intentalo de nuevo')