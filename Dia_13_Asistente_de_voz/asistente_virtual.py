import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar voz t devolver audio como texto
def transformar_audio_en_texto():
    #almacenar recognizer en variable
    r=sr.Recognizer()

    #configurar microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print('ya puedes hablar :)')
        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio,language="es-mx")

            #prueba de que pudo entrar
            print('Dijiste: '+pedido)
            #devolver pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print('Ups, no entendí')

            #devolver error
            return "sigo esperando"

        #en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print('Ups, no hay servicio')

            # devolver error
            return "sigo esperando"

        #error inesperado:
        except:
            # prueba de que no comprendio el audio
            print('Ups, algo salio mal :(')

            # devolver error
            return "sigo esperando"


#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #encender el motor de pyttsx3
    engine= pyttsx3.init()

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#informar el dia de la semana
def pedir_dia():

    #crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombres de días
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    #decir dia de la semana
    hablar(f'hoy es {calendario[dia_semana]}')

#informar que hora es
def pedir_hora():
    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora= f'Son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    #hablar
    hablar(hora)

#def funcion de saludo inicial
def saludo_inicial():
    #variable con datos de hota
    hora=datetime.datetime.now()
    if hora.hour <6 or hora.hour>20:
        momento='Buenas noches'
    elif 6<= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    #decir saludo
    hablar(f'Hola {momento}, soy tu asistente virtual. ¿En que te puedo ayudar?')

#funcion central del asistente
def pedir_cosas():
    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    while comenzar:
       #activar micro y guardar el pedido en string
       pedido = transformar_audio_en_texto().lower()

       if 'abrir youtube' in pedido:
            hablar('Abriendo Youtube')
            webbrowser.open('https://www.youtube.com/')
            continue
       elif 'abrir navegador' in pedido:
           hablar('Estoy en eso')
           webbrowser.open('https://www.google.com/')
           continue
       elif 'qué día es hoy' in pedido:
           pedir_dia()
           continue
       elif 'qué hora es' in pedido:
           pedir_hora()
           continue
       elif 'busca en wikipedia' in pedido:
           hablar('Buscando en wikipedia')
           pedido = pedido.replace('busca en wikipedia','')
           wikipedia.set_lang('es')
           resultado = wikipedia.summary(pedido, sentences=1 )
           hablar('Wikipedia dice lo siguiente.')
           hablar(resultado)
           continue
       elif 'busca en internet' in pedido:
           hablar('estoy en eso')
           pedido = pedido.replace('busca en internet', '')
           pywhatkit.search(pedido)
           hablar('esto es lo que he encontrado.')
           continue
       elif 'reproducir' in pedido:
           hablar('comenzando a reproducir')
           pywhatkit.playonyt(pedido)

           continue
       elif 'cuéntame un chiste' in pedido:
           hablar(pyjokes.get_joke('es'))
           continue
       elif 'precio de las acciones' in pedido:
           accion = pedido.split('de')[-1].strip()
           cartera = {'apple':'APPL',
                      'amazon':'AMZN',
                      'goggle':'GOOGL'}
           try:
               accion_buscada = cartera[accion]
               accion_buscada = yf.Ticker(accion_buscada)
               precio_actual = accion_buscada.info['regularMarketPrice']
               hablar(f'El precio de {accion} es de {precio_actual}')
               continue
           except:
               print('ups, algo salio mal')
               continue
       elif 'apagate':
           hablar('Adios')
           break

pedir_cosas()
#saludo_inicial()
#pedir_hora()

#pedir_dia()

# ---- LLAMADA A LA FUNCIÓN ----
#transformar_audio_en_texto()

#hablar('hola a todos')

'''
#miras voces disponibles en el sistema
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)
'''