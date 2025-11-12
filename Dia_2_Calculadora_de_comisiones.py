#variables


num1 = 7.5

num2 = 2.5

resultado = num1 + num2
#imprimir tipo de datos
print(type(resultado))

#convertir tipos de datos
print(num1)
print(type(num1))

convertir= int(num1)
print(convertir)
print(type(convertir))

#formatear cadenas
x = 6
y= 2
z= 7

print("mis numero son {} y {}".format(x,y))
print(f"mis numero son {x} y {y}")

#operadores

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

print(f"{z} dividido al piso de {y} es igual a {z//y}") #dividir al piso es quitando los residuos dando un numero entero
print(f"{z} modulo de {y} es igual {z%y}") #para sacar el modulo
print(f"{x} elevado a la {y} es igual a {x**y}") # potencia
print(f"raiz de {x} es igual a {x**0.5}") #raiz

#redondeo
a= 9.6666
b= round(a,1)

print(b)


#programa final

nombre= input("ingresa tu nombre")
ventas = input("ingresa tus ventas")
convertir_venta = float(ventas) * 13 / 100
res = round(convertir_venta,2)
print(f"{nombre} y la comosion es de {res}")



