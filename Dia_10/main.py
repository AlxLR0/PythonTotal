import pygame
import random
import math
from pygame import  mixer

#inicializar pygame
pygame.init()

#crear la pantalla
pantalla = pygame.display.set_mode((800,600))#configurar el tamaño de la pantalla

#titulo, icono y fondo
pygame.display.set_caption('Invasion Espacial')#titulo
icono= pygame.image.load('ovni.png')#preparar el icono
pygame.display.set_icon(icono)#insertar icono en la ventana
fondo = pygame.image.load('Fondo.jpg')

#agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)#establecer volumen
mixer.music.play(-1)#-1 para que se repita de nuevo cuando termine la música

#jugador
img_jugador= pygame.image.load('cohete.png')#preparar png del cohete
jugador_x = 368 #coordenadas x,y inicializadas en la posición de partida
jugador_y = 500
jugador_x_cambio = 0 #esto se encarga de guardar la posición cuando cambie en el loop

#enemigo
img_enemigo = []
enemigo_x = [] #se establece una longitud aleatoria donde puede aparecer el enemigo
enemigo_y = [] #al igual que una altura
enemigo_x_cambio = [] #velocidad de movimiento
enemigo_y_cambio = []
cantidad_enemigos = 10

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736)) #se establece una longitud aleatoria donde puede aparecer el enemigo
    enemigo_y.append( random.randint(50,200)) #al igual que una altura
    enemigo_x_cambio.append(0.5) #velocidad de movimiento
    enemigo_y_cambio.append(50)

#bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500 #se posiciona de inicio a la misma altura que la nave
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False #esto ya que la bala no se tiene que ver hasta que el jugador dispare

#puntaje
puntaje= 0              #tipo de fuente y tamaño
fuente = pygame.font.Font('abduction2002.ttf',32)
texto_x= 10
texto_y = 10

#texto final del juego
fuente_final = pygame.font.Font('abduction2002.ttf', 64)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO!!",True, (255,0,0))
    pantalla.blit(mi_fuente_final,(60,200))


#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    text = fuente.render(f'Puntaje: {puntaje}', True,(255,255,255))
    pantalla.blit(text,(x,y))

#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))#blit arroja datos a pantalla pasándole la img y una tuple con las posiciones de x,y

#funcion enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene],(x,y))

#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True #cuando el jugador dispare el estado de la bala cambia a visible
    pantalla.blit(img_bala, (x+16,y+10)) #se le asignan más cantidad al valor original para que se vea mejor como sale la bala

#funcion detectar colisiones
def detectar_colisiones(x_1,y_1,x_2,y_2):
            #la raiz del resultado x1 menos x2 al cuadrado + el resultado de y1 menos y2
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1,2))
    if distancia < 27:
        return True
    else:
        return False

#loop del juego
se_ejecuta_pantalla = True
while se_ejecuta_pantalla: #esto hace que se ejecute la pantalla mientras el valor sea verdadero

    #RGB (si se necesita en lugar de una img de fondo)
    #pantalla.fill((27, 141, 255))  # se rellena la pantalla y se le pasa una tuple con colores rgb(27, 141, 255)

    #imagen de fondo
    pantalla.blit(fondo,(0,0))

    #iterar eventos
    for evento in pygame.event.get():

        #evento cerrar
        if evento.type == pygame.QUIT: #hasta que se pulse el btn X de la ventana (pygame.QUIT)
            se_ejecuta_pantalla = False #este pasa a ser falso y se cierra la pantalla

        #evento presionar teclas
        if evento.type == pygame.KEYDOWN: #controla los eventos cuando una tecla es presionada
            if evento.key == pygame.K_a:
                jugador_x_cambio = -0.7 #disminuye el valor en X haciendo que se mueva a la izquierda
                #print('izquierda')
            if evento.key == pygame.K_d:
                jugador_x_cambio = 0.7 #aumenta el valor en X haciendo que se mueva a la derecha
                #print('derecha')
            if evento.key == pygame.K_SPACE:
                sonido_bala= mixer.Sound('disparo.mp3')#cargar el sonido del disparo
                sonido_bala.set_volume(0.5)
                sonido_bala.play()

                #esto es igual a bala_visible == False
                if not bala_visible: #esto solo funciona en caso de que la bala no sea visible y no afecte al movimiento
                    bala_x = jugador_x #se usa bala_x para poder hacer independiente el movimiento de la bala con la del jugador y eta no siga el mismo movimiento
                    disparar_bala(bala_x,bala_y) #bala_X(jugador_x) para que dispare desde la posición en la que se encuentra la neva

        #evento soltar flechas
        if evento.type == pygame.KEYUP: #controla los eventos cuando se deja presionar la tecla
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                #print('tecla soltada')
                jugador_x_cambio = 0 #regresa el valor a 0 para dejar de producir movimiento

    #modificar ubicación del jugador
    jugador_x += jugador_x_cambio #establecer cambios con respecto al movimiento

    #mantener jugador en bordes
    if jugador_x <= 0: #si la posición queda en 0 (pixel 0 de la pantalla ) el jugador se detiene
        jugador_x =0
    elif jugador_x >= 736: # igual en la posición 736 ejes x
        jugador_x = 736

    #modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

        #fin del juego game ovaaaahhh
        if enemigo_y[e]>475: #si el enemigo llega a esta distancia el juego termina
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]
    # mantener enemigo en bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.4 #en este caso en lugar de detener al enemigo este cambiará su camino hacia el otro lado
            enemigo_y[e] += enemigo_y_cambio[e] #y después bajara en su posición en el eje
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.4
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        colision = detectar_colisiones(enemigo_x[e], enemigo_y[e], bala_x, bala_y)  # guarda y se le pasan los valores a la función detectar_colisiones
        if colision:  # en caso de existir una colision
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.set_volume(0.5)
            sonido_colision.play()
            bala_y = 500  # se restablece el valor de la bala
            bala_visible = False  # y la visibilidad pasa a ser False
            puntaje += 1
            #print(puntaje)

            enemigo_x[e] = random.randint(0, 736)  # se establece una longitud aleatoria donde puede aparecer el enemigo
            enemigo_y[e] = random.randint(50, 200)  # al igual que una altura

        enemigo(enemigo_x[e], enemigo_y[e], e)#se le pasan las variables a la función enemigo

    #movimiento bala
    if bala_y <= -64:#si la bala sale de la vista del jugador
        bala_y = 500 #se restablece su posición
        bala_visible = False #la bala deja de ser visible

    if bala_visible: #si el valor de la bala es TRUE
        disparar_bala(bala_x,bala_y) #bala_x( jugador_x) para que dispare desde la posición en la que se encuentra la neva
        bala_y -= bala_y_cambio


    jugador(jugador_x,jugador_y) #se le pasan las variables a la función jugador

    #mostrar el puntaje
    mostrar_puntaje(texto_x,texto_y)

    #actualizar
    pygame.display.update()#se encarga de actualizar la pantalla con los elementos seleccionados

#todo: intentar hacer que los enemigos conforme van bajando aumenten la velocidad

#https://www.1001freefonts.com