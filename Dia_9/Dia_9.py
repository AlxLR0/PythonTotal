from collections import Counter
import os
from datetime import *
import datetime
import math
import shutil
#import send2trash #este se instala desde el cmd pip install send2trash sirve para enviar archivos eliminados a la papelera


numeros = [1,1,5,5,7,7,8,8,9,9,9,9,6,3,2,1,4,8]
print(Counter(numeros)) #este modulo permite saber cuantas veces se repiten los numero en la lista numeros

frase="al pan pan y al vino vino"
print(Counter(frase.split()))#tambien para contar cuantas veces se repiten las palabras en una frase

serie = Counter([1,1,1,1,1,2,2,2,2,3,3,3,4,4,5])
print(serie.most_common()) #aqui ordena al mas comun se le puede pasar argumentos serie.most_common(1) para que nos pase al que mas veces se repite

archivo = open('curso.txt', 'w')
archivo.write('hola mundo')
archivo.close()

#shutil.move('curso.txt', 'C:\\users\\alexl\\Desktop') Re ubicar archivos en este caso al escritorios

#send2trash.send2trah('curso.txt') #para borrar archivos

ruta= 'C:\\Users\\alexl\\Desktop\\Tareas\\practicar\\PythonTotal'
for carpeta,subcarpeta, archivo in os.walk(ruta):
    print(f'en la carpeta: {carpeta}')
    print(f'las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('los archivos son:')
    for arc in archivo:
        print(f'\t{arc}')
    print('\n')


#modulo date time
mi_dia = datetime.date(2025,10,17)

print(mi_dia)
print(mi_dia.today())

#diferencias de tiempo
nacimiento = date(1995,3,5)
defuncion = date(2095,5,19)

vida = defuncion - nacimiento
print(vida.days)

print()
#math
resultado = math.floor(89.665) #hacer redondeo hacia abajo (89)
resultado2 = math.ceil(89.665) # redondeo hacia arriba (90)
pi=math.pi # esto da 3.1415... (pi)
res = math.log(25,5) # a que numero se expone el 5 para dar 25

print()
#modulo Re (resgular expression)
import re
txt = 'Si necesitas ayuda llama al (658)-558-9977 las 24 horas del dia'

patron='nada'
ayuda= 'ayuda'
busqueda = re.search(patron,txt) #buscar si existe la palabra nada en el txt principal
print(busqueda)
busqueda= re.findall(ayuda,txt) #que encuentre todas las veces que aparece la palabra ayuda en el txt principal

numero = 'llama al 564-525-6588 ya'

patronNums = r'\d\d\d-\d\d\d-\d\d\d\d' #tener listo un patron de 3 numeros 3 numeros y 4 numeros
            #esto tambien funciona si se coloca r'\d{3}-\d{3}-\d{4}'
resultadoNums= re.search(patronNums,numero)
print(resultadoNums)
print(resultadoNums.group())#tener como tal el resultado del numero 564-525-6588

clave = input("gimi la clave: ")
patronon= r'\d{1}\w{7}' #este patron dice que la clave sera de un numero y 7 digitos
chequear = re.search(patron,clave)
print(chequear)

"""
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta,
que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" 
(aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok",
 pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario 
 "La dirección de email es incorrecta" imprimiendo el mensaje.
"""


def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

"""
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación
 (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón.
 Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
"""
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar= re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

#Comprimir y Descomprimir Archivos desde Python
import zipfile

#para comprimir
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w') #preparar el archivo comprimido nombre y w de write

mi_zip.write('curso.txt') #el archivo que se va a comprimir
mi_zip.close()

#para descomprimir
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')#preparar el archivo comprimido nombre y r de read
zip_abierto.extractall() #para extraer tooooodo el contenido del archivo zip
