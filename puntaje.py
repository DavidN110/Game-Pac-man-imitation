import pygame
from vglobales import *
def imprimir_puntaje(score:str):
    t1 = fuente.render('SCORE',True, WHITE)
    screen.blit(t1,(560,190))
