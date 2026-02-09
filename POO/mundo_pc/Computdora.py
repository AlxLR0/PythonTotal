class Computadora:
    contador_computadoras=0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def id_computadora(self):
        return  self._id_computadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return  self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'Nombre: {self._nombre} -> ID: {self.id_computadora}, Monitor: {self.monitor}, Teclado: {self.teclado}, Raton: {self.raton}'

if __name__ == '__main__':
    pc1 = Computadora('Gamer',15,'usb','usb')
    print(pc1)