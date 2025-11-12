import re
import os
import time
import datetime
from pathlib import Path
import math

# -------------------------
# Inicio del script
# -------------------------
# Guardamos el tiempo de inicio para luego calcular cuánto tardó la búsqueda
inicio = time.time()

# Ruta donde vamos a buscar los archivos
ruta = 'C:\\Users\\alexl\\Desktop\\Tareas\\practicar\\PythonTotal\\Dia_9\\Mi_Gran_Directorio'

# Patrón regex que buscamos dentro de los archivos
# En este caso: letra 'N', tres caracteres NO dígito, un guion, y 5 dígitos.
# Ejemplo que coincide: "Nabc-12345"
patron = r'N\D{3}-\d{5}'

# Fecha de hoy (para mostrar en el informe)
hoy = datetime.date.today()

# Listas donde guardamos resultados
numeros_encontrados = []    # almacenará los números/series hallados por el patrón
archivos_encontrados = []   # almacenará los nombres de los archivos donde se encontró

# -------------------------
# Función: buscar_numero
# -------------------------
def buscar_numero(archivo, patron):
    """
    Abre el archivo cuyo path se le pasa en 'archivo', lee todo su texto
    y busca la primera coincidencia del 'patron' regex.
    Si encuentra algo devuelve el objeto Match (re.search), si no devuelve cadena vacía.
    NOTA: la función abre el archivo con open() sin usar 'with' (no modificamos esto para mantener la funcionalidad original).
    """
    este_archivo = open(archivo, 'r')      # abrir el archivo en modo lectura
    texto = este_archivo.read()            # leer todo el contenido como string
    if re.search(patron, texto):           # buscar el patrón dentro del texto
        return re.search(patron, texto)    # devuelve el primer match (objeto Match)
    else:
        return ''                          # si no hay coincidencia devuelve cadena vacía

# -------------------------
# Función: crear_lista
# -------------------------
def crear_lista():
    """
    Recorre recursivamente la estructura de carpetas en 'ruta' (usando os.walk).
    Para cada archivo que encuentre, llama a buscar_numero() para ver si contiene el patrón.
    Si encuentra una coincidencia:
      - añade el texto del grupo (resultado.group()) a numeros_encontrados
      - añade el nombre del archivo (con formato Title) a archivos_encontrados
    """
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            # Construimos la ruta completa al archivo con Path(carpeta, a)
            resultado = buscar_numero(Path(carpeta, a), patron)
            if resultado != '':
                # Guardamos la cadena del match (por ejemplo "Nabc-12345")
                numeros_encontrados.append((resultado.group()))
                # Guardamos el nombre del archivo (title case para presentación)
                archivos_encontrados.append(a.title())

# -------------------------
# Función: mostrar_todo
# -------------------------
def mostrar_todo():
    """
    Muestra en pantalla un pequeño informe con:
      - fecha de búsqueda
      - tabla de Archivo <tab> Nro. Serie (los resultados encontrados)
      - cantidad total de números encontrados
      - duración en segundos (redondeada hacia arriba)
    """
    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t--------')
    # Recorremos la lista de archivos encontrados y mostramos el número correspondiente
    for a in archivos_encontrados:
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados {len(numeros_encontrados)}')
    # Calculamos cuanto tiempo tomó la búsqueda usando el tiempo de inicio guardado arriba
    fin = time.time()
    duracion = fin - inicio
    # Mostramos la duración redondeando hacia arriba con math.ceil
    print(f'duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

# -------------------------
# Ejecución del flujo
# -------------------------
# 1) Construir las listas (buscar coincidencias en todos los archivos)
crear_lista()
# 2) Mostrar un informe con los resultados
mostrar_todo()
