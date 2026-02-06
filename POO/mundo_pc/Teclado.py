from POO.mundo_pc.Dispositivo_entrada import Dispositivo_entrada


class Teclado(Dispositivo_entrada):
    contador_teclados =0
    id_teclado =0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados +=1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    #get
    @property
    def id_teclado(self):
        return self._id_teclado

    def __str__(self):
        return f'ID: {self._id_teclado}, Marca: {self.marca}, Tipo de entrada: {self.tipo_entrada}'


#principal
if __name__ == '__main__':
    teclado1= Teclado('machenike', 'usb')
    print(teclado1)
