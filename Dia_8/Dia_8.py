#manejo de errores

def suma():
    n1 = int(input('n1: '))
    n2 = int(input('n2: '))
    print(n1+n2)

try:
    #codigo que queremos probar
    suma()
except ValueError: #tambien se puede poner typeerror y cualquier otro tipo de errores a los cuales se quiere preparar al programa
    # codigo a ejecutar si hay error este caso al poner el tipo de error (valueError) va a verificar que si ocurre ese error va a mostrar ese print
    print('valiendo verija ese no es un numero')
except:
    #codigo a ejecutar si hay error este al estar solo va por defecto
    print('Algo no salio bien mi master chif')
else: #este es extra
    #codigo a ejecutar si no hay error
    print('Suma resuelta correctamente')
finally:
    #codigo que se va a ejecutar de todos modos
    print('bye bye')


def pedir_numero():
    while True:
        try:
            n= int(input('gimi a number:'))
        except:
            print('eso no es un numero')
        else:
            print(f'el numereishon is {n}')
            break
    print('.....')

pedir_numero()

#decoradores
def cambiar_letras(tipo):
    def mayuscula(txt):
        print(txt.upper())


    def minuscula(txt):
        print(txt.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula
op=cambiar_letras('may')

op('hola')


def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

@decorar_saludo
def mayus(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())
mayus('python')


#otra forma de decorar mayus=decorar_saludo(mayus)


#generadores
"""
Los generadores en Python
son un tipo especial de función que devuelve un iterador y produce valores uno por uno a medida que se necesitan, pausando su estado entre cada uno.
si estamos generando una lista de [1 a 1millon] en lugar de generar todo de golpe se va generando conforme de necesite
en lugar de usar return en las funciones aca se usas yield

def funcion():
    yield algo

"""

#comparando funcion tradicional con return y con el generador yield
def mi_funcion():
    lista=[]
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x*10

print(mi_funcion())
print(mi_generador())

g=mi_generador()
print(g) #conforme vamos mandando a llamar al generador se van generando los datos
print(g)