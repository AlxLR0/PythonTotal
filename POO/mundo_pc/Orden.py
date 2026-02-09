class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes +=1
        self.id_orden = Orden.contador_ordenes

        #recibir la lista de objetos de tipo computadora
        self.computadoras = computadoras

    def agregar_pc(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str +='\n'+ computadora.__str__()
        return f'''orden: {self.id_orden}
        Computadoras: {computadoras_str}'''

