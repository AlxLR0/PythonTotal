print('*'*5,'decoradores','*'*5)
'''
Los decoradores en Python son funciones especiales que envuelven y modifican el comportamiento de otras funciones 
o métodos sin cambiar su código original. Actúan como una "capa extra" —identificable por la arroba @— para añadir 
funcionalidad (como logs, medir tiempo o autenticación) de forma reutilizable y limpia. 
'''

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('antes')
        resultado = funcion(*args, **kwargs) #llamamos a nuestra funcion
        print('despues')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'hola {nombre}')

saludar('fulano')

print()
def mi_decorador(funcion):
    def envoltura():
        print("Antes de ejecutar la función.")
        funcion()
        print("Después de ejecutar la función.")
    return envoltura

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
# Resultado:
# Antes de ejecutar la función.
# ¡Hola!
# Después de ejecutar la función.
