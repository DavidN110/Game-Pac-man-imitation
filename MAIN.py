import pygame, sys
from tigres import *
from comida import *
from paredes import *
from palabras import *
from jugador import *

SCORE=0

pygame.init()

def limites(variable):
    if variable > 700:
        return 0
    elif variable < 0:
        return 700
    else:
        return variable

while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -paso_personaje
            if event.key == pygame.K_RIGHT:
                speed_x = paso_personaje
            if event.key == pygame.K_UP:
                speed_y = -paso_personaje
            if event.key == pygame.K_DOWN:
                speed_y = paso_personaje

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0 

    if Menos_vida():
        cord_x = 20
        cord_y = 20

        cord_x_t1 = CENTROX-60
        cord_y_t1 = CENTROY-50

        cord_x_t2 = CENTROX-20
        cord_y_t2 = CENTROY-50

        cord_x_t3 = CENTROX+20
        cord_y_t3 = CENTROY-50

        Reset_Menos_vida()

    screen.fill(BLACK)
    cord_x += speed_x   
    cord_y += speed_y

    cord_x, cord_y = verificador_posisicion(cord_x,cord_y,paso_personaje)

    cord_x = limites(cord_x)
    cord_x_t1 = limites(cord_x_t1)
    cord_x_t2 = limites(cord_x_t2)
    cord_x_t3 = limites(cord_x_t3)

    cord_x_t1,cord_y_t1,dir1 = mov_tigres(cord_x_t1,cord_y_t1,dir1)
    cord_x_t2,cord_y_t2,dir2 = mov_tigres(cord_x_t2,cord_y_t2,dir2)
    cord_x_t3,cord_y_t3,dir3 = mov_tigres(cord_x_t3,cord_y_t3,dir3)

    paredes()
    imprimir_letras()
    SCORE = comida(Lista_comidax,Lista_comiday,SCORE,jugador(cord_x, cord_y,tigres(cord_x_t1, cord_y_t1),tigres(cord_x_t2, cord_y_t2),tigres(cord_x_t3, cord_y_t3)))[0]

    if SCORE==73:
        victoria = fuente3.render('Victory',True, RED)
        screen.blit(victoria,(100,250))

        victoria = fuente2.render('Si te gusto suscribete y dale like',True, RED)
        screen.blit(victoria,(230,380))
        pygame.display.flip() 
        time.sleep(10)
        sys.exit() 

    if Game_over(): 
      vida = fuente.render('GAME OVER',True,RED)
      screen.blit(vida,(250,300)) 
      pierde = fuente2.render('Intentalo en una proxima oportunidad',True, RED)
      screen.blit(pierde,(200,380))
      pygame.display.flip()
      time.sleep(10)
      sys.exit()

    pygame.display.flip()
    clock.tick(90)