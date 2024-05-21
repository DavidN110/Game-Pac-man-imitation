from vglobales import *
def points(score):
    point = fuente.render('$'+str(score),True,RED)
    screen.blit(point,(560,390))
    