from vglobales import *
from jugador import *
from puntos import *
import pygame

def comida(Lista_comidax:list,Lista_comiday:list,SCORE:int,imagen_jugador):
    for i in range(0,len(Lista_comidax)-1):
        com = pygame.Rect(Lista_comidax[i],Lista_comiday[i],5,5)
        if imagen_jugador.colliderect(com):
            SCORE+=1
            points(SCORE) 
            Lista_comidax[i] = 800
            Lista_comiday[i] = 800
        else:
            points(SCORE) 
            comidas.append(pygame.draw.circle(screen,WHITE,(Lista_comidax[i],Lista_comiday[i]),5))
    return SCORE,Lista_comidax,Lista_comiday
 