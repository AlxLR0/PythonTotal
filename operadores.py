#asignacion multiple
x,y=10,5 # x vale 10 y vale 5

#invertir valores
x,y = y,x #ahora x vale 5 y vale 10

#recibir multiples valores de entrada
nombre,apellido = input('ingresa tu nombre y apellido separandolos por una coma (fulanito, perez): ').split(',')#esto recibe multipler valores asignandolos a nombre y apellido y se usa split para cortar la coma y poder guardarlos
print(f'{nombre} - {apellido}')

#asignacion compuesto
contador = 0
contador += 1 # es igual a contador = contador + 1 esto tambien aplica a restas - multipicacion * division /

"""
comparacion🟢
5==5   👈true👉   3>5
5==6   👈false👉  6<3

5!=5   👈false👉  3>=5
5!=5   👈true👉   5>=5

Logicos🟢
a = false
b = true
print(a and b) false

a = false
b = true
print(a or b) true

a = false
print(not a) true

______________________
OR🟢
a    | b   | a or b
_____________________
false|false| false
false|true | true
true |false| ture
true |true | true
_____________________

NOT🟢
a    | not a
_____________________
false| true
true | false
_____________________

"""

print()

print('**descuentos vip**')
NO_PRODUCTOS_DESCUENTO= 10 #constante
cantidad_procuctos = int(input('cuantos productos compraste hoy: '))
tiene_membresia= input('tienes membresia (si/no): ').strip().lower()

elegible_descuento = (cantidad_procuctos >= NO_PRODUCTOS_DESCUENTO and tiene_membresia == 'si')
if elegible_descuento:
    print('tienes acceso al descuento vip')
else:
    print('no elegible aun')


"""
PRECEDENCIA DE OPERADORES

la precedencia de operadores determina el ordenen que ese evaluan las operaciones en una expresion
python aplica la siguiente tabla para asegurar que algunos operadores tengan mayor prioridad que otros durante la evaluacion se expresiones

1.- operador de parentesis ()
2.- exponente **
3.- unarios +x, -x
4.- multiplicacion, division, modulo *,/,//,%
5.- suma y resta +, -
6.- comparacion ==, !=, <,<=,>,>=
7.- operadores logicos not and y or
8.- operadores asignacion =,+=,-=,%=,//=,**=

res= 5 + 3 * 2 ** 2 = 17
res= (5 + 3) * 2 ** 2 = 32

"""