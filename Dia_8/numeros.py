#generar numeros de los turnos
def numeros_perfumeria():
    for n in range(1,10000): #que genere numeros en un rango de 1 a 10000
        yield f'P - {n}' #y yield los imprimira 1 a 1 ([p-1] [p-2] ...) conforme se vaya llamando

def numeros_farmacia():
    for n in range(1,10000):
        yield f'F - {n}'

def numeros_cosmetica():
    for n in range(1,10000):
        yield f'C - {n}'

#guaradar las funciones en variables para que el programa se puede acordar
p=numeros_perfumeria()
f=numeros_farmacia()
c=numeros_cosmetica()


#crear decoradores para construir el ticket
def decorador(rubro):
    print('\n'+'*'*46)
    print('Su numero es: ')
    if rubro == 'P':
        print(next(p))#aqui con la funcion next impimimos el siguiente numero que contenga p que al mismo tiempo almacena el generador  numeros_perfumeria()
    elif rubro == 'F':
        print(next(f))#igual aqui
    else:
        print(next(c))#y pues aqui tambien pero con sus respetivos generadores
    print('Aguante bara que ya mero le damos su buena despachada ;)')
    print('*' * 46 +'\n')