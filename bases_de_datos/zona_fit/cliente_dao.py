'''
El patrón DAO (Data Access Object) en Python es una técnica de diseño que separa la lógica de negocio de la persistencia de datos.
Actúa como una interfaz intermedia que encapsula las operaciones CRUD (crear, leer, actualizar, borrar) en una base de datos,
ocultando la complejidad del SQL. Esto facilita la mantenibilidad, pruebas y el cambio de motor de base de datos sin afectar el código funciona
'''
from bases_de_datos.zona_fit.conexion import Conexion
from cliente import Cliente

class ClienteDao:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre,apellido,membresia) VALUES (%s,%s,%s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            #mapeo de clase-tabla cliente
            clientes=[]
            for registro in registros:
                cliente=Cliente(registro[0],registro[1],registro[2],registro[3])

                clientes.append(cliente)
            return clientes

        except Exception as e:
            print(f'ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def insertar(cls, cliente):
        conexion = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores=(cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR,valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'ocurrio un error al insertar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'ocurrio un error al actualizar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)



if __name__ == '__main__':

    #insertar cliente
    # cliente1= Cliente(nombre='tony', apellido='cipriani',membresia=300)
    # clientes_insertados = ClienteDao.insertar(cliente1)
    # print(f'clientes insertados: {clientes_insertados}')

    #actualizar cliente
    cliente_actualizar=Cliente(3,'tony','cipriani', 400)
    clientes_actuaizados = ClienteDao.actualizar(cliente_actualizar)
    print(f'clientes actualizados: {clientes_actuaizados}')

    #selecionar clientes
    clientes = ClienteDao.seleccionar()
    for cliente in clientes:
        print(cliente)