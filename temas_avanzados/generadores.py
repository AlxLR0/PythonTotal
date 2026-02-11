print('*'*5,'generadores','*'*5)
'''
Los generadores en Python son funciones especiales que devuelven secuencias de valores uno por uno (al vuelo)
en lugar de todos a la vez, usando yield en lugar de return`. Esto ahorra memoria al no almacenar listas grandes,
ya que pausan su ejecución y recuerdan su estado interno hasta la siguiente llamada.


Características principales:

    Eficiencia de memoria: Ideal para manejar conjuntos de datos inmensos o infinitos sin saturar la RAM.
    Evaluación perezosa (Lazy evaluation): Solo calculan el siguiente valor cuando se solicita (next()), no antes.
    Sintaxis yield: Cuando una función llega a yield, devuelve el valor y pausa la ejecución. La próxima vez que se llama, continúa justo después del yield.
    Uso: Se suelen recorrer con bucles for o la función next()
'''
def contador(maximo):
    n = 1
    while n <= maximo:
        yield n  # Pausa aquí y devuelve n
        n += 1

# Uso
for numero in contador(3):
    print(numero) # Imprime 1, 2, 3


print('*'*5,'expresiones generadoras','*'*5)

'''
Las expresiones generadoras en Python son una forma compacta y eficiente de crear secuencias de datos sin ocupar mucha memoria,
parecidas a las comprensiones de lista pero usando paréntesis () en lugar de corchetes []. Generan elementos uno por uno (evaluación perezosa)
en lugar de crear la lista completa en la memoria, siendo ideales para grandes conjuntos de datos. 
'''

generador = (x**2 for x in range(10))


