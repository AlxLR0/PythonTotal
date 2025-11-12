# Proyecto: Cajero simple con POO
# Breve: Este programa define dos clases (Persona y Cliente). Cliente hereda de Persona
# y tiene métodos para depositar y retirar dinero. Luego pide al usuario crear un cliente
# y le permite realizar operaciones (depositar, retirar, mostrar datos, salir).

# -----------------------------
# Clase base: Persona
# -----------------------------
# Representa una persona con nombre y apellido.
# Solo guarda los datos personales básicos que usarán los clientes.
class Persona():
    def __init__(self, nombre, apellido):
        # Guarda el nombre y apellido de la persona (atributos de instancia).
        self.nombre = nombre
        self.apellido = apellido


# -----------------------------
# Clase derivada: Cliente
# -----------------------------
# Cliente hereda de Persona, porque un cliente es una persona con datos bancarios.
# Aparte del nombre y apellido (heredados), el cliente tiene número de cuenta y balance.
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        # Llamamos al constructor de la clase padre (Persona) para inicializar nombre/apellido.
        super().__init__(nombre, apellido)
        # Atributos propios de Cliente:
        self.numero_cuenta = numero_cuenta  # número de cuenta (puede ser string o int)
        self.balance = balance              # saldo actual (float o int)

    # Método para depositar dinero en la cuenta del cliente.
    # Recibe 'cantidad' y la suma al balance.
    # Actualmente devuelve un texto con el nuevo balance (puedes cambiar el retorno si prefieres True/False).
    def depositar(self, cantidad):
        # 'resultado' se usa aquí para devolver el balance resultante (suma simple).
        resultado = cantidad + self.balance
        self.balance += cantidad
        # Devolvemos un mensaje; en un diseño alternativo, podríamos devolver True y dejar el mensaje fuera.
        return f'se deposito: {resultado}'

    # Método para retirar dinero de la cuenta.
    # Si hay saldo suficiente, resta y confirma; si no, informa que no hay fondos.
    def retirar(self, cantidad):
        if self.balance >= cantidad:
            # Hay saldo suficiente: realizamos el retiro.
            self.balance -= cantidad
            return 'operacion exitosa'
        else:
            # No hay fondos suficientes: no modificamos balance y devolvemos mensaje de error.
            return 'no hay fondos suficientes'

    # Método especial: __str__
    # Permite que cuando hagamos print(cliente) se muestre información amigable del cliente.
    def __str__(self):
        return f'El usuario {self.nombre} {self.apellido} con numero de cuenta {self.numero_cuenta} tiene un balance de {self.balance}'


# -----------------------------
# Función: crear_cliente
# -----------------------------
# Pide al usuario los datos necesarios para crear un objeto Cliente y lo devuelve.
# Pasos:
#  1) Preguntar nombre/apellido/número de cuenta/balance inicial
#  2) Convertir los valores numéricos a int/float según corresponda
#  3) Crear la instancia Cliente y devolverla
def crear_cliente():
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    numero_cuenta = input('ingresa tu numero de cuenta: ')
    # Convertimos a int porque queremos un número; si prefieres mantenerlo como string,
    # puedes eliminar la conversión. Aquí la dejamos por claridad.
    try:
        numero_cuenta = int(numero_cuenta)
    except ValueError:
        # Si el usuario no mete un número válido, lo guardamos como string original.
        # (Esto evita que el programa rompa si ingresan algo extraño.)
        numero_cuenta = numero_cuenta

    balance_inicial = input("Balance inicial: ")
    # Convertimos el balance a float para poder manipular decimales.
    try:
        balance_inicial = float(balance_inicial)
    except ValueError:
        # Si la conversión falla, ponemos balance 0.0 por seguridad.
        print("Balance inválido, se inicializa a 0.0")
        balance_inicial = 0.0

    # Creamos el objeto Cliente con los datos ingresados y lo devolvemos.
    cliente = Cliente(nombre, apellido, numero_cuenta, balance_inicial)
    return cliente


# -----------------------------
# Función: inicio (loop principal)
# -----------------------------
# Orquesta la ejecución del programa:
#  1) Crea un cliente llamando a crear_cliente()
#  2) Entra en un bucle que muestra un menú (depositar, retirar, mostrar datos, salir)
#  3) Según la opción, llama a los métodos del cliente y muestra resultados
def inicio():
    # Crear cliente al inicio del programa
    cliente = crear_cliente()

    # Bucle principal: se repite hasta que el usuario elija salir.
    while True:
        print("\n¿Qué quieres hacer?")
        print("(d) Depositar")
        print("(r) Retirar")
        print("(m) Mostrar datos")
        print("(s) Salir")
        # Leemos la opción y normalizamos (minúsculas y sin espacios extra).
        opcion = input("Elige una opción: ").lower().strip()

        # Opción: depositar
        if opcion == 'd':
            # Pedimos monto a depositar (se asume entrada válida según consigna del curso)
            try:
                cantidad = float(input('Ingresa monto depositar: '))
            except ValueError:
                # Si el usuario mete algo que no es número, avisamos y volvemos al menú.
                print("Monto inválido. Usa números, por ejemplo: 100 o 50.5")
                continue

            # Llamamos al método depositar del objeto Cliente. Aquí el método devuelve un mensaje.
            resultado_deposito = cliente.depositar(cantidad)
            # Imprimimos confirmación y el nuevo balance (formateado con dos decimales).
            print(f"{resultado_deposito}. Balance actual: {cliente.balance:.2f}")

        # Opción: retirar
        elif opcion == 'r':
            try:
                cantidad = float(input('Ingresa monto a retirar: '))
            except ValueError:
                print("Monto inválido. Usa números, por ejemplo: 100 o 50.5")
                continue

            # Llamamos al método retirar; según su implementación devuelve texto indicando éxito o fallo.
            resultado = cliente.retirar(cantidad)
            if resultado == 'operacion exitosa':
                print(f"Retiro realizado. Balance actual: {cliente.balance:.2f}")
            else:
                # Aquí mostramos el motivo (por ejemplo: 'no hay fondos suficientes')
                print(f"No se pudo retirar: {resultado}. Balance actual: {cliente.balance:.2f}")

        # Opción: mostrar datos del cliente (usamos __str__)
        elif opcion == 'm':
            print(cliente)

        # Opción: salir del programa
        elif opcion == 's':
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break

        # Opción inválida
        else:
            print("Opción no válida. Intenta de nuevo.")


# -----------------------------
# Bloque de prueba / ejecución directa
# -----------------------------
# Aquí hay ejemplos para probar los métodos de la clase sin entrar en el menú.
# Puedes comentar (o borrar) estas pruebas cuando uses el programa normalmente.
c = Cliente("Ana", "Lopez", "123", 1000)
print(c.depositar(200))        # prueba depositar
print(c.__str__())             # mostrar datos
print(c.retirar(500))          # prueba retirar (éxito)
print(c.retirar(800))          # prueba retirar (falla por fondos)
print(c.__str__())             # mostrar datos finales

# Inicia el flujo interactivo con el usuario (menú)
inicio()
