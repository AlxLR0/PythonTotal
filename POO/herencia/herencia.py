class Animal:
    def comer(self):
        print('como muchas veces al dia')

    def dormir(self):
        print('duermo mucho 💤')



class Perro(Animal):
    def hacer_sonido(self):
        print('ladrar')

    #sobre escritura del metodo dormir: modificar el comportamiento de un metodo de la clase padre
    def dormir(self):
        print('duermo 15 hrs al dia 💤')



#programa principal
print('ejemplo de herencia')
print('clase padre, soy un animal')
animal1= Animal()
animal1.comer()
animal1.dormir() #se manda a llamar el metodo sobreescrito

print('\nClase hija, perro')
perro1=Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
