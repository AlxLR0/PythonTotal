print('*'*5,'abrir un archivo en modo exclusivo','*'*5)

nombre_archivo = 'mi_archivo.txt'

try:
    with open(nombre_archivo, 'x') as archivo: #con with se ejecutara y se cerrara el codigo dentro de el sin necesidad de usar .close()
        archivo.write('hola mundo')
    print('se creo el archivo')
except FileExistsError:
    print(f'el archivo {nombre_archivo} ya existe')