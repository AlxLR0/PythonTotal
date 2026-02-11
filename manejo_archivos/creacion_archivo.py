print('*'*5,'crear un archivo','*'*5)
nombre_archivo = 'mi_archivo.txt'

#abrir el archivo en modo escritura ('w')
archivo = open(nombre_archivo, 'w') #se abre / crea archivo
archivo.write('hola mundo') #se escribe

archivo.close() # se cierra

print(f'se creo el archivo: {nombre_archivo}')