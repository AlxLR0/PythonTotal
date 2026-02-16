import mysql.connector



personas_bd = mysql.connector.connect(
    host= '127.0.0.1',
    port = 3307,  # Puerto Docker
    user= 'root',
    password= 'admin',
    database ='personas_db'  # TablePlus
)

#ejecutar la sentencia select
cursor = personas_bd.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)

cursor.close()
personas_bd.close()
