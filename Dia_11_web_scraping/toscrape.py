import bs4
import requests

url_base= 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1,11):#sacar los primeros enlaces del sitio web
    print(url_base.format(n))#se le pasa n para remplazarlo en las llaves {} de url_base

resultado = requests.get(url_base.format(1))
sopa = bs4.BeautifulSoup(resultado.text,'lxml')

print()
libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)