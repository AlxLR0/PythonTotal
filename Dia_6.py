#abrir archivos de texto
mi_archivo=open('prueba.txt') #selecionamos el archivo en este caso es prueba.txt que ademas esta en el mismo directorio que este proyecto
print(mi_archivo.read())#el metodo read es para que pueda leer el contenido del archivo y mostrarlo en consola
#print(mi_archivo.readline())#este metodo solo lee la primera linea del archivo
#print(mi_archivo.readline().rstrip())#rstrip es para que omita saltos de linea
#print(mi_archivo.readlines())#readlines crea una lista de cada una de las lineas del archivo
#tambien se puede hacer diferentes metodos
for linea in mi_archivo:
    print(f"aqui dice: {linea}")
mi_archivo.close()#se recomienda cerrarlo para que pueda ahorrar memoria


"""
Abre el archivo texto.txt e imprime únicamente la segunda línea.
"""

#archivo = open("texto.txt")
#lineas = archivo.readlines()
#print(lineas[1])

#archivo.close()
# Alternativa de solución admitida:
# lineas = archivo.readline()
# lineas = archivo.readline()
# print(lineas)


mi_archivo2=open('prueba1.txt','w')#la letra al final del nombre del archivo puede ser r=read (solo lectura) w=write (escritura cuidado con este que sobre escribe todo)
mi_archivo2.write('hola nuevo texto') # write permite excribir
#mi_archivo2.writelines(['hola', 'mundo']) #writelines perimite escribir una lista en ael archivo
#metodo alterno para writelines escriba todo con saltos de linea y no todo pegado
lista=['hola','mundo']
for palabra in lista:
    mi_archivo2.writelines(palabra+'\n')
mi_archivo2.close()

"""
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

a=open('mi_archivo.txt','w')
a.write("Nuevo texto")
a.close()

a=open('mi_archivo.txt','r')
print(a.read())

"""

"""
Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.


registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())
"""
from pathlib import Path, PureWindowsPath

carpetona = Path('/Users/alexl/Desktop/Tareas/practicar/PythonTotal/archivos') #elegimos la ruta del archivonon (este jala para todos los OS)
ruta_windows = PureWindowsPath(carpetona)#este en caso de querer transformar la ruta exclusiva a windows
archivonon = carpetona / 'prueba.txt'


if not archivonon.exists():
    print("Este archivonon no existe viejo ya pelaste gallo alv")
else:
    archivou = open(archivonon)
    print(archivou.read())

print()

#path
base = Path.home()#por si queremos una ruta absoluta
#si queremos pasar de una ruta relativa a una absoluta seria pasar la variable base al path --->  Path(base,"barcelona","sagrada_familia.txt")
guia = Path("barcelona","sagrada_familia.txt") #esto es igual a crear una carpera y archivo en la ruta ../barcelona/sagrada_familia.txt en una ruta relativa

print(guia)



#proyecto dia 6

