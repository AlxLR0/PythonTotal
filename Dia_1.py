#print
a= 'mundo'
print('hola',a)

#variable privada
_private_name= 'alx'

#constante
PI= 3.1416
print(PI)

#short circuit
name = 'alejandro'
print(name and name.upper()) #esto sirve para imprimir el valor de la variable si es que existe o si no existe imprime el valor de la variable

#string
print('me encanta estudiar')
print("hola \"mundo\"") #esto es para que tome en cuenta las comillas dobles dentro de las comillas dobles o tratarlas como caracter especial
print("hola \nmundo") #para salto de linea dentro del mismo print
print("\t esto es un tabulador")#para tabular un texto
print('you can\'t give up')#para usar el \ para un caracter especial
print ('Línea 1\nLínea 2\nLínea 3\n')

print('A\tB\tC\nD\tE\tF\nG\tH\tI')

print('Barra Normal: /\nBarra Invertida: \\')

#input
#print('Tu nombre es: '+input('tu nombre:')+' '+input('tu apellido:'))
print('Tu Marca es: \n"'+input('Palabra 1:')+' '+input('Palabra 2: ')+'"')