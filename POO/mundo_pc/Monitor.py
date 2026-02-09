class Monitor:
    contador_monitores =0

    def __init__(self, marca, pulgadas):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._pulgadas = pulgadas

    @property
    def id_monitor(self):
        return self._id_monitor

    # get
    @property
    def marca(self):
        return self._marca

    # set
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def pulgadas(self):
        return  self._pulgadas

    @pulgadas.setter
    def pulgadas(self, pulgadas):
        self._pulgadas = pulgadas

    def __str__(self):
        return f'ID: {self.id_monitor}, Marca: {self.marca}, Tipo de entrada: {self.pulgadas}'

if __name__ == '__main__':
    monitor1 = Monitor('hp',15)
    print(monitor1)