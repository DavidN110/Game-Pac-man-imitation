import pygame
from vglobales import *
def imprimir_letras():
    t1 = fuente.render('SCORE',True, WHITE)
    screen.blit(t1,(560,190))

    t2 = fuente2.render('David Pinzon',True, WHITE)
    screen.blit(t2,(10,380))

    t3 = fuente2.render('David Nagles',True, WHITE)
    screen.blit(t3,(10,400))

    name_game = fuente.render('CIRCE',True,RED)
    screen.blit(name_game,(10,190))
    
