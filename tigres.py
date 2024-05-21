from vglobales import pygame, screen, WHITE, CENTROX,paso_tigres
from jugador import verificador_posisicion
import random

def mov(tigx,tigy,dir):
    x = tigx
    y = tigy
    if dir == 1:
        x-=1
    elif dir == 2:
        x+=1
    elif dir == 3:
        y-=1
    elif dir == 4:    
        y+=1
    return x,y

def mov_tigres (tigx,tigy,dir):
    x = tigx
    y = tigy
    direccion = dir
    
    if y > 179 and y < 373 and x > 250 and x < 410:
        if x == CENTROX-20:
            direccion = 3
        elif x > CENTROX-20:
            direccion = 1
        elif x < CENTROX-20:
            direccion = 2
    elif x != verificador_posisicion(x,y,paso_tigres)[0] or y != verificador_posisicion(x,y,paso_tigres)[1]:
        x,y = verificador_posisicion(x,y,paso_tigres)
        direccion = random.randint(1,4)

  
    x,y = mov(x,y,direccion)

    return (x,y,direccion) 

def tigres (cord_x_t, cord_y_t):

    tigre1 = pygame.image.load("tigree.jpg").convert()
    tigre1.set_colorkey(WHITE)
    screen.blit(tigre1,[cord_x_t, cord_y_t])
    return pygame.Rect(cord_x_t, cord_y_t,40,40)