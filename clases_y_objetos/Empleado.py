class Empleado:
    contador_empleados =0

    def __init__(self, nombre, departamento):
        self._nombre=nombre
        self._departamento=departamento
        Empleado.contador_empleados += 1

    # get
    @property
    def nombre(self):
        return self._nombre

    #set
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self,departamento):
         self._departamento = departamento

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados