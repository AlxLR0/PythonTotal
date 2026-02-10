print('*'*5,'split','*'*5)
'''
El método .split() en Python divide una cadena de texto (string) en una lista de subcadenas más pequeñas,
 utilizando un separador especificado. Por defecto, separa por espacios en blanco
(espacios, tabulaciones, saltos de línea). Es fundamental para el análisis de texto y manipulación de datos. 
'''

#dividir cadena
cadena = 'hola mundo'
palabras = cadena.split()
print(palabras)

cadena2 = 'hola a todos'
palabras2 = cadena2.split('t')
print(palabras2)

print('')
print('*'*5,'find','*'*5)
posicion = cadena.find('mundo')#devolver el valor de 5
print(posicion)

print('')
print('*'*5,'replace','*'*5)
nueva_cadena = cadena.replace('mundo', 'amigo')
print(nueva_cadena)



print('')
print('*'*5,'strip','*'*5)
'''
La función
.strip() en Python elimina caracteres iniciales y finales de una cadena, siendo su uso principal quitar espacios en blanco,
 tabulaciones (\t) y saltos de línea (\n) de ambos extremos.
Devuelve una nueva cadena sin modificar la original, siendo útil para la limpieza de datos. 
'''
cadena_espacios = ' hola mundo  '
cadena_limpia = cadena.strip()
print(cadena_limpia)
cadena_caracteres = '...hola mundo ...'
cadena_limpia2 = cadena_caracteres.strip('.')
print(cadena_limpia2)