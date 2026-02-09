from POO.mundo_pc.Dispositivo_entrada import Dispositivo_entrada


class Raton(Dispositivo_entrada):
    contador_ratones = 0
    id_raton = 0

    def __init__(self,marca, tipo_entrada):
        Raton.contador_ratones +=1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada) #heredar atributos de la clase padre

    @property
    def id_raton(self):
        return self._id_raton

    def __str__(self):
        return f'Raton: [ID: {self._id_raton}, Marca: {self.marca}, Tipo de entrada: {self.tipo_entrada}]'


#codigo principal
if __name__ == '__main__':
    raton1= Raton('hp', 'usb')
    print(raton1)