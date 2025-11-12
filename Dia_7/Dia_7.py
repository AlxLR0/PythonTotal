#creacion de clases
class Pajaro:# nombre en MAYUS para respetar sintaxis
    #atributos de clase esta tipo de atributos van a ser igual para todos los objs
    alas=True

    """
    __init__
    en Python es un método especial que se ejecuta automáticamente al crear un nuevo objeto (instancia) de una clase.
    Se utiliza para inicializar los atributos del objeto
    permitiendo establecer un estado inicial y personalizar las propiedades de cada instancia cuando se crea
    """
    def __init__(self,color): #metodo constructor
        #en otros lenguajes es igual a this.color = color donde self.color es el atributo y lo que esta en el parentesis y despues del signo de = es el parametro
        self.color = color

    #metodos personalizados(metodos de instancia) (metodos de toda la vida)
    #estos acceden y modifican atributos del obj,acceden a otros metodos y modifican el estado de la clase
    def piar(self): #self dentro de estos metodos que estan en las clases siempre es obligatorio ponerlo para que haga referencia a todos los parametros que contenga
        print('pio pio y soy {} prros'.format(self.color))#para mandar llamar otras variables o tributos de la clase

    def volar(self,metros):
        print(f'el pajarte volor {metros} metros')

    #metodos de clase
    @classmethod
    def poner_huevos(cls,cantidad): #no esta relacionado a las instancias si no a las clases mismas podemos ejecutar este metodo sin tener que crear un obj (llamarlo directamente Pajaro.poner_huevos)
        print(f'puso {cantidad} huevos')
        cls.alas= False #tambien pueden modificar atributos

    @staticmethod #es un método que pertenece a una clase pero no está vinculado a ninguna instancia de la clase ni a la propia clase, lo que significa que no recibe self ni cls como primer argumento.
    def mirar():
        print('ayam guachin yu prro (.)(.)')


#creacion de instancias
mi_pajaro=Pajaro('verde') #obj de la clase pajaro

#seleccionar atriburos
print(mi_pajaro.color)

eltuiter= Pajaro('azul')
eltuiter.piar() #mandar llamar a los metodos personalizados
eltuiter.volar(5) #metodo que pide perametro

#mandando llamar un metodo de clase
Pajaro.poner_huevos(58)

#mandando llamar un metodo estatico
Pajaro.mirar()


#herencia
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('nacio')

    def hablar(self):
        print('habla')

class Bird(Animal): #lo que esta entre parentesis marca a cual clase le esta heredando

    def __init__(self, edad,color,altura_vuelo):
        super().__init__(edad,color) #esto sirve para heredar los atributos que tengan en comun con la clase padre
        self.altura_vuelo = altura_vuelo

    def hablar(self):#se reescribe el metodo hablar con las propias caracteristicas de al clase padre
        print('pio')
    def volar(self, metros):
        print(f'vuela {metros} metros')

pajarraco=Bird(2,'verde',60) #le pasamos los parametros que exige la clase padre
pajarraco.nacer() #como se puede ver esta instancia de bird ya tiene acceso a las propiedades de la clase padre ANIMAL


#herencia multiple
class Padre:
    def hablar(self):
        print('hola')

class Madre:
    def reir(self):
        print('lol')
    def hablar(self):
        print('adios')

"""para que una clase pueda heredar de multiples clases basta con 'pasarlas como parametro' tomando en cuenta que...
   en caso de que tengan atributos similares (en esta caso hablar) se tomara en cuenta primero el atriburo que se pase primero de izquierda a derecha
   Hijo(Padre,Madre) si se quiere que primero tome en cuenta lo de la madre seria Hijo(Madre, Padre)
 """
class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mai_granson=Nieto()
mai_granson.hablar() #y asi el nieto puede tener atributos de los nietos

print()
#polimorfismo = muchas formas
"""
Muchos formas: La palabra viene de "poli" (muchos) y "morfo" (forma).
Un mensaje, varias respuestas: Diferentes objetos reaccionan de forma única a una misma llamada a método.
Flexibilidad: Permite escribir código que funciona con objetos de distintas clases sin tener que saber exactamente qué clase es en el momento de escribir el código. Por ejemplo, una lista de Forma puede contener Círculo y Cuadrado, y al llamar a dibujar() en cada uno, se ejecutará la versión específica de cada figura. 

Ejemplo práctico

    Una clase base Animal con un método hacerSonido().
    Clases hijas como Perro y Gato que heredan de Animal.
    Ambas clases hijas sobrescriben el método hacerSonido():
        La clase Perro tiene la implementación ladra().
        La clase Gato tiene la implementación maúlla().
"""
class Vaca:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre+"dice muuuuuuuu prros")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre+"dice beeeeeeeee prros")


vaca1=Vaca('lola')
oveja1=Oveja('ASODJ')

vaca1.hablar()
oveja1.hablar()

animales = [vaca1,oveja1]
for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()
animal_habla(vaca1)

print()
#metodos especiales
"""
Los métodos especiales en Python, también conocidos como métodos mágicos o "dunder" (double underscore),
son funciones definidas por el usuario que se distinguen por tener doble guion bajo al principio y al final de su nombre (ej. __init__, __str__).
 Permiten personalizar el comportamiento de una clase, haciendo que sus objetos interactúen con los operadores y funciones integradas del lenguaje,
como la creación, la comparación y la impresión

Ejemplos comunes

    __init__(self, ...): El constructor de la clase. Se ejecuta automáticamente al crear un nuevo objeto y se usa para inicializar sus atributos.
    __str__(self): Devuelve una representación en cadena de texto legible para el usuario. Se usa cuando llamas a print() sobre un objeto.
    __len__(self): Permite que un objeto devuelva su tamaño. Se utiliza con la función len().
    __eq__(self, other): Define el comportamiento del operador de igualdad ==. Se utiliza para comparar si dos objetos son iguales.
    __add__(self, other): Define el comportamiento del operador de suma +.
    __del__(self): Funciona como un destructor, ejecutándose justo antes de que un objeto sea eliminado de la memoria.
"""

class CD:
    def __init__(self,autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    def __str__(self): #para armar unos string
        return f"Album {self.titulo} de {self.autor}"
    def __len__(self):
        return self.canciones
mi_cd=CD('pin floi', 'de gual', 8000)
print(mi_cd)
