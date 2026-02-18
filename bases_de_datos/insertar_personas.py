import mysql.connector



personas_bd = mysql.connector.connect(
    host='',
    port=0,  # Puerto Docker
    user='',
    password='',
    database=''  # TablePlus
)

#ejecutar la sentencia INSERT
try:
    cursor = personas_bd.cursor()
    sentencia_sql = 'INSERT INTO personas(nombre, apellido,edad) VALUES(%s,%s,%s)'
    valores = ('carl', 'jhonson', 30)
    cursor.execute(sentencia_sql,valores)
    personas_bd.commit() #guardar los cambios en la bd
    print(f'Se guardaron los datos {valores} en la bd')
    cursor.close()
    personas_bd.close()
except mysql.connector.Error as err:
    print(f"❌ Error de MySQL: {err}")