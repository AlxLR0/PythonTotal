import mysql.connector



personas_bd = mysql.connector.connect(
    host= '',
    port = 0,  # Puerto Docker
    user= '',
    password= '',
    database =''  # TablePlus
)

#ejecutar la sentencia UPDATE
try:
    cursor = personas_bd.cursor()
    sentencia_sql = 'DELETE FROM personas WHERE id=%s'
    valores = (4,) # id a eliminar con una coma al final para que lo tome como una tupla
    cursor.execute(sentencia_sql,valores)
    personas_bd.commit() #guardar los cambios en la bd
    print(f'Se elimino los datos con el id {valores} en la bd')
    cursor.close()
    personas_bd.close()
except mysql.connector.Error as err:
    print(f"❌ Error de MySQL: {err}")