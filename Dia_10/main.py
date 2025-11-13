import pygame
import random

#inicializar pygame
pygame.init()

#crear la pantalla
pantalla = pygame.display.set_mode((800,600))#configurar el tamaño de la pantalla

#titulo, icono y fondo
pygame.display.set_caption('Invasion Espacial')#titulo
icono= pygame.image.load('ovni.png')#preparar el icono
pygame.display.set_icon(icono)#insertar icono en la ventana
fondo = pygame.image.load('Fondo.jpg')

#jugador
img_jugador= pygame.image.load('cohete.png')#preparar png del cohete
jugador_x = 368 #coordenadas x,y inicializadas en la posición de partida
jugador_y = 500
jugador_x_cambio = 0 #esto se encarga de guardar la posición cuando cambie en el loop

#enemigo
img_enemigo = pygame.image.load('enemigo.png')
enemigo_x = random.randint(0,736) #se establece una longitud aleatoria donde puede aparecer el enemigo
enemigo_y = random.randint(50,200) #al igual que una altura
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50

#bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500 #se posiciona de inicio a la misma altura que la nave
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False #esto ya que la bala no se tiene que ver hasta que el jugador dispare

#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))#blit arroja datos a pantalla pasándole la img y una tuple con las posiciones de x,y

#funcion enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y))

#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True #cuando el jugador dispare el estado de la bala cambia a visible
    pantalla.blit(img_bala, (x+16,y+10)) #se le asignan más cantidad al valor original para que se vea mejor como sale la bala

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
                disparar_bala(jugador_x,bala_y) #jugador_x para que dispare desde la posición en la que se encuentra la neva
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
    enemigo_x += enemigo_x_cambio

    # mantener enemigo en bordes
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.4 #en este caso en lugar de detener al enemigo este cambiará su camino hacia el otro lado
        enemigo_y += enemigo_y_cambio #y después bajara en su posición en el eje
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.4
        enemigo_y += enemigo_y_cambio

    #movimiento bala
    if bala_visible: #si el valor de la bala es TRUE
        disparar_bala(jugador_x,bala_y) #jugador_x para que dispare desde la posición en la que se encuentra la neva
        bala_y -= bala_y_cambio


    jugador(jugador_x,jugador_y) #se le pasan las variables a la función jugador
    enemigo(enemigo_x,enemigo_y)

    #actualizar
    pygame.display.update()#se encarga de actualizar la pantalla con los elementos seleccionados

#todo: intentar hacer que los enemigos conforme van bajando aumenten la velocidad
