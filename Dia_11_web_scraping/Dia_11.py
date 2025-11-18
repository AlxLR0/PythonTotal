import bs4
import requests
#import lxml

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/buscas-trabajo-y-no-has-certificado-en.html')


#print(resultado.text)

sopa =bs4.BeautifulSoup(resultado.text,'lxml')

print(sopa.select('title'))
print(sopa.select('title')[0].getText())

parrafo = sopa.select('h2')[1].getText()

titulo = sopa.select('.post-title a')[0].getText() #extraer clases

imagenes = sopa.select('img')

print(len(sopa.select('h1')))

print(parrafo)
print(titulo)
for i in imagenes:
    print(imagenes)