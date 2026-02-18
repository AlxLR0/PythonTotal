from bases_de_datos.zona_fit.cliente_dao import ClienteDao
from bases_de_datos.zona_fit.cliente import Cliente

print('--- ZONA FIT ---')
opcion = None

while opcion != 5:
    print(f'''MENU:
    1. Listar clientes
    2. Agregar cliente
    3. Modificar Cliente
    4. Eliminar cliente
    5. Salir

''')
    opcion = int(input('ingresa una opcion: '))

    if opcion == 1: #listar clientes
        clientes = ClienteDao.seleccionar()
        print('\n***LISTADO CLIENTES***')
        for cliente in clientes:
            print(cliente)
        print()

    elif opcion == 2: #agregar cliente
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = input('Escribe la membresia: ')
        cliente = Cliente(nombre= nombre_var, apellido= apellido_var, membresia=membresia_var)

        clientes_insertados = ClienteDao.insertar(cliente)
        print(f'Cliente/s insertados: {clientes_insertados}')

    elif opcion == 3: #modificar cliente
        id_cliente_var = int(input('Escribe el id del cliente a modificar: '))
        nombre_var = input('Escribe el nombre a modificar: ')
        apellido_var = input('Escribe el apellido a modificar: ')
        membresia_var = input('Escribe la membresia: ')
        cliente = Cliente(id_cliente_var, nombre_var,apellido_var, membresia_var)

        clientes_actualizados = ClienteDao.actualizar(cliente)
        print(f'Cliente/s actualizados: {clientes_actualizados}')

    elif opcion == 4 :
        id_cliente_var = int(input('Escribe el id del cliente a modificar: '))
        cliente = Cliente(id=id_cliente_var)

        clientes_eliminados = ClienteDao.eliminar(cliente)
        print(f'Cliente/s eliminados: {clientes_eliminados}')
    else:
        print('BYE BYE')