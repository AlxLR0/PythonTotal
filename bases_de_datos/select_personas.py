import mysql.connector



personas_bd = mysql.connector.connect(
    host='',
    port=0,  # Puerto Docker
    user='',
    password='',
    database=''  # TablePlus
)

#ejecutar la sentencia select
cursor = personas_bd.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)

cursor.close()
personas_bd.close()
