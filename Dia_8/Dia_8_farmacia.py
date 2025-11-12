import  numeros

def preguntar():
    print('guelcom tu farmaci paiton')
    while True:
        print('[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmeticos')
        try:
            mi_rubro = input('Elija una opcion: ').upper()
            ['P','F','C'].index(mi_rubro) #esto lo que hace es añadirle estas posibles opciones
        except:
            print('Opcion no valida')
        else:
            break
    numeros.decorador(mi_rubro) # le pasamos tooodo esto al decorador que ese encuentra en numeros.py para crear el ticket

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('Du yu guant anoder turno?\n[S]=SI [N]=NO: ').upper()
            ['S','N'].index(otro_turno)
        except:
            print('Opcion no valida')
        else:
            if otro_turno == 'N':
                print('chao prro')
                break

inicio()