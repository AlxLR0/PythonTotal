#index
mi_txt= "hola k hace"
res= mi_txt[3] #saber en que contiene el indice 0
print(res)
res2=mi_txt.index("k") # en que indice se encuentra la letra k
print(res2)
res2=mi_txt.index("a",4,11)#que encuentre la letra a despues del indice 4 y antes del 11
print(res2)
res3=mi_txt.rindex("a")#encuentra en reversa
print(res3)

#substrings
textonon= "ABCDEFGHI"
# extraer desde la posicion numero_string dos hasta la numero_string 5 (sin incluir el final) dando como resultado CDE
fragmento=textonon[2:5]
print(fragmento)

# extraer desde la posicion numero_string dos hasta la numero_string 7 saltando de 2 en 2 dando como resultado CEG
fragmento2=textonon[2:7:2]
print(fragmento2)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])


#metodos string
resultadon = frase.upper()#todo a mayususculas
print(resultadon)
resultadon = frase.lower()#todo en minusculas
print(resultadon)
resultadon = frase.split()#crea una lista por cada una de las palabras en el texto
print(resultadon)
var1= "hola"
var2= "mundo"
x= "-".join([var1,var2])#une el contenido
print(x)
resultadon = frase.find("s")#encuentra el contenido de la letra seleccionada
print(resultadon)
resultadon = frase.replace("Nunca","Siempre")#remplazar texto o contenido
print(resultadon)

#propiedades de string
neim ="""hola 
mundo """ #escribir en un bloque
print(neim)
print(len(neim))

#lista puede contener cualquier elemento y se pueden modificar
mein_lista=['a','b','d','c']
mein_lista[0]="alfa"#modificar un elemento de una lista
mein_lista.append('e')#añadir un elemento al final
mein_lista.pop(1)#eliminar un elemento en este caso con el indice 1 (la b) si no se pone nada eliminara el ultimo elemento de la lista
mein_lista.sort()#ordena la lista
mein_lista.reverse()#lista en reversa
print(mein_lista)

#diccionarios
my_dic={'c1':'val1', 'c2':'val2'}
resultadote= my_dic['c1']
print(resultadote)

my_dic2={'c1':'val1', 'c2':[1,2,3], 'c3':{'si':100,'s2':200}}
print(my_dic2['c2'][1])#imprimir lo que contiene la llave c2 índice 1 (resultado será 2)

my_dic3={'c1':['a','b','c'], 'c2':['d','e','f']}
letra=my_dic3['c2'][1]
print(letra.upper())#extraer la letra e y hacerla mayúscula

my_dic3["pais"]='hola' #añadir elemento al dictionary
print(my_dic3)

print(my_dic3.keys())#conocer las llaves que contiene un diccionario}

#tuplas
mi_tupla=(1,2,3,4,1)
print(mi_tupla)
print(mi_tupla.count(1))#cuantas veces hay el numero_string 1 en la tupla
print(mi_tupla.index(2))#consultar el index 2
a,b,c,d,e=mi_tupla #almacenar cada valor de la tupla a diferentes variables ejem: a=1 b=2 c=3...
converti_tupla= list(mi_tupla)#convertir tupla a lista

#sets
mi_set= set([1,2,3,4,5])#un set normalito
mi_set.add(6)#añadir elementos a un set
s2={7,8} #otra forma de crear sets
s2.remove(8)#eliminar un elemento del set
s3= mi_set.union(s2) #union de sets

print(s3)


#proyecto dia 3

texto = input("ingresa texto: ")
texto=texto.lower()
letras=[]
letras.append(input("ingresa letra 1: ").lower())
letras.append(input("ingresa letra 2: ").lower())
letras.append(input("ingresa letra 3: ").lower())


#cuantas letras hay en total
print("\n")
print("cantidad de letras")
cantidad1=texto.count(letras[0])
cantidad2=texto.count(letras[1])
cantidad3=texto.count(letras[2])

print(f"{letras[0]} aparece {cantidad1} veces")
print(f"{letras[1]} aparece {cantidad2} veces")
print(f"{letras[2]} aparece {cantidad3} veces")

#cuantas palabras hay en total
print("\n")
print("cantidad de palabras")
palabras=texto.split()
print(f"hay {len(palabras)} palabras en total")

#primera y ultima letra
print("\n")
print("primera y ultima letra")
print(f"primera letra: {texto[0]}")
print(f"ultima letra: {texto[-1]}")

#texto en reversa
print("\n")
print("texto en reversa")
palabras.reverse()
txt_invertido=' '.join(palabras)

print(f"la frase en reversa es: {txt_invertido}")


#aparece python en la palabra
print("\n")
print("python en la palabra")
py= 'python' in texto
print(f"{py} la palabra python aparece en la frase {texto}")