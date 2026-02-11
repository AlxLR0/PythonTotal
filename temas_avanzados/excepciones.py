print('*'*5,'excepciones','*'*5)

'''
Las excepciones en Python son errores que ocurren mientras el programa se está ejecutando, interrumpiendo su flujo normal.
A diferencia de los errores de sintaxis, el código está bien escrito, pero algo inesperado sucede (ej. dividir por cero, archivo no encontrado).
Se manejan con try y except para evitar que el programa se detenga.
'''

try:
    resultado = 10 / 0
    if resultado == 0:
        raise Exception('el denominador es 0 mi brooooo') #Lanzar o generar un error (excepción) de forma manual y explícita en tu código. Funciona como una alerta para detener el flujo normal cuando ocurre algo inesperado o inválido, permitiendo personalizar el mensaje de error y el tipo de excepción que se lanza.
except ZeroDivisionError:
    print("No puedes dividir por cero.") # Esto evita que el programa rompa
except TypeError:
    print("No puedes dividir cadenas.")
else:
    print('no hay ningún error')
finally:
    print('fin')