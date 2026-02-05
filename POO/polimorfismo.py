'''
El polimorfismo es la
capacidad que tienen objetos de distintas clases de responder al mismo comando o método de formas diferentes.

Una superclase Animal tiene un método hacerSonido(). Si tienes subclases Perro y Gato, al llamar a hacerSonido(),
 el perro ladra y el gato maúlla, aunque el comando enviado fue el mismo.
'''
from POO.herencia.herencia import animal1


class Animal:
    def hacer_sonido(self):
        print('hacer un sonido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Ladra')

class Gato(Animal):
    def hacer_sonido(self):
        print('maulla')


print('clase padre: Animal')
animal1 = Animal()
animal1.hacer_sonido()

print('\nclase hija: perro')
perro1= Perro()
perro1.hacer_sonido()

print('\nclase hija: gato')
gato1=Gato()
gato1.hacer_sonido()