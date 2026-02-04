'''

Los diccionarios en Python son estructuras de datos que almacenan pares ordenados de
clave-valor (key:value), permitiendo un acceso rápido a los elementos sin usar índices numéricos.
 Son mutables, dinámicos, no permiten claves duplicadas y se definen con llaves {},
 siendo ideales para modelar información estructurada o "listas asociativas"
'''
print('*'*5,'Diccionarios','*'*5)

persona = {'nombre':'fulanito', 'edad':25, 'ciudad':'peluche'}

#acceder a la data
print(f'Nombre: {persona["nombre"]}')
#otra forma de acceder
print(f'Edad: {persona.get("edad")}')

#modificar data
persona['edad']=26
print(persona)

#añadir info
persona['profession'] = 'ingeniero'
print(persona)

#eliminar elemento
del persona['ciudad']

#eliminar por llave
persona.pop('profession')

print(persona)

print()
#iterar los elelemtos del dict

for llave, valor in persona.items():
    print(f'Llave {llave} valor {valor}')

print()
#obtener valores
for valor in persona.values():
    print(f'-valor {valor}')


#combinar listar y diccionarios
personas = [{'nombre':'fulano', 'edad':800}, {'nombre':'sutano', 'edad': 800}]
