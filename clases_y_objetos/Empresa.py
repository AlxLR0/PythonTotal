from clases_y_objetos.Empleado import Empleado


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados=[]

    def contratar_empleado(self, nombre, departemento):
        empleado = Empleado(nombre, departemento)
        self.empleados.append(empleado)

    def obtener_numero_empleados_departamento(self, departemento):
        contador_empleados =0
        for empleado in self.empleados:
            if empleado._departamento == departemento:
                contador_empleados += 1

        return  contador_empleados


print('sistema empleados')

#instancia empresa
empresa1 = Empresa('monsters inc.')

#contratar empleados
empresa1.contratar_empleado('fulanito','ventas')
empresa1.contratar_empleado('sutanito', 'IT')
empresa1.contratar_empleado('perenganito','ventas')

#obtener el total de objetos de tipo empleado
print(f'total de empleados: {Empleado.obtener_total_empleados()}')

#empleados en ventas
print(f'total de empleados en ventas: {empresa1.obtener_numero_empleados_departamento("ventas")}')

