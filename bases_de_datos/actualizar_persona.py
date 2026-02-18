import mysql.connector



personas_bd = mysql.connector.connect(
    host='',
    port=0,  # Puerto Docker
    user='',
    password='',
    database=''  # TablePlus
)

#ejecutar la sentencia UPDATE
try:
    cursor = personas_bd.cursor()
    sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
    valores = ('carl', 'jhonson', 29, 3) #nombre, apellido, edad, id
    cursor.execute(sentencia_sql,valores)
    personas_bd.commit() #guardar los cambios en la bd
    print(f'Se actualizaron los datos {valores} en la bd')
    cursor.close()
    personas_bd.close()
except mysql.connector.Error as err:
    print(f"❌ Error de MySQL: {err}")