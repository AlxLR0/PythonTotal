print('*'*5,'leer archivo','*'*5)

nombre_archivo = 'mi_archivo.txt'

#leer un archivo usando el metodo readlines
with open(nombre_archivo, 'r') as archivo:
    #leer lineas de archivo
    print(archivo.readlines())


#leer todo el contenido con read
with open(nombre_archivo, 'r') as archivo:
    #leer lineas de archivo
    print(archivo.read())