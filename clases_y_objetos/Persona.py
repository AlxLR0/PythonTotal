#definicion de la clase

class Persona:

    #contructor
    def __init__(self, nombre, apellido):
        # crear atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''
        nombre: {self.nombre}
        apellido: {self.apellido}
        ''')

#creacion de objetos
if __name__ == '__main__':
    #creacion de primer objeto
    persona1=Persona('funalito','de tal')
    persona1.mostrar_persona()


class Aritmetica:

    def __init__(self,n1,n2):
        self._n1 = n1
        self._n2 = n2

    def sumar (self):
        resultado = self._n1 + self._n2
        print(f'la suma es: {resultado}')

    def restar (self):
        resultado = self._n1 - self._n2
        print(f'la resta es: {resultado}')

    def multiplicar (self):
        resultado = self._n1 * self._n2
        print(f'la multiplicacion es: {resultado}')

    def dividir (self):
        resultado = self._n1 / self._n2
        print(f'la division es: {resultado}')

    #get
    @property
    def operando1(self):
        return self._n1

    #set
    @operando1.setter
    def operando1(self,n1):
        self._n1 = n1

    @property
    def operando2(self):
        return self._n2

    @operando2.setter
    def operando2(self,n2):
        self._n2 = n2


if __name__ == '__main__':
    aritmetica = Aritmetica(5,7)
    print(f'n1: {aritmetica.operando1} n2: {aritmetica.operando2}')
    aritmetica.sumar()





'''
El encapsulamiento en Python
es un pilar de la programación orientada a objetos (POO) que agrupa datos (atributos) y métodos en una clase,
restringiendo el acceso directo a los componentes internos para evitar modificaciones accidentales

para proteger un dato en python solo basta con poner _ a los atribustos ppor ejemplo
self._nombre #atributo protegido
self.__nombre #atributo privado
'''

class Auto:
    def __init__(self, marca, modelo, color):
       ''' self.marca = marca #atributo publico
        self._modelo = modelo #atributo protegido
        self.__color = color #atributo privado
        '''

       self._marca = marca
       self._modelo = modelo
       self._color = color

    def get_marca(self):
        return self._marca

    def set_marca(self,marca):
        self._marca= marca

    @property #otra forma de definir el metodo get
    def modelo(self):
        return self._modelo

    @modelo.setter #otra forma de definir metodo set
    def modelo(self,modelo):
        self._modelo=modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color=color


    def conducir(self):
        print(f'marca {self._marca} modelo: {self._modelo} color{self._color}')

if __name__ == '__main__':
    pass
