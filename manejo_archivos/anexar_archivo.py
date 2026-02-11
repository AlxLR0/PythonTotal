print('*'*5,'anexar archivo','*'*5)
nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    archivo.write('\n anexando info..\n')

print('se actualizo la info del archivo')