from mysql.connector import pooling
from mysql.connector import Error

'''
Un pool de objetos, especialmente el pool de conexiones de bases de datos en Python, 
es un patrón de diseño que mantiene un conjunto preinicializado de conexiones activas. 
En lugar de crear y destruir una conexión por cada consulta, la aplicación "toma prestada"
una conexión existente y la devuelve al finalizar, mejorando drásticamente el rendimiento y la eficiencia. 
'''
class Conexion:
    host= '127.0.0.1'
    port = 3307  # Puerto Docker
    user= 'root'
    password= 'admin'
    database ='zona_fit_db'  # TablePlus
    pool_size = 5
    pool_name = 'zona_fit_pool'
    pool = None


    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.pool_name,
                    pool_size = cls.pool_size,
                    host = cls.host,
                    port = cls.port,
                    database = cls.database,
                    user = cls.user,
                    password = cls.password

                )
                return cls.pool
            except Error as e:
                print(f'ERROR EN POOL: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


#prueba de conexion
if __name__ == '__main__':
    #se crea el objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1=pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print('CONEXION LIBERADA')
