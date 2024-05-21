from vglobales import *

def paredes():
    global paredes1
    global paredes2
    global paredes3
    global paredes4

    A = 2.5
    B = 697.5
    C = 150
    D = 450
    E = 250
    F = 575
    G = 550
    paredes1 = [0,0,A,A,B,B,A,B,A,B,A,B,A,B,C,G,C,G,290,410,290,290,380,75,625,0,650,220,480,220,480,300,300,300,350,350,350,220,480,220,480,75,430,220,480,C,G,C,G]
    paredes2 = [A,B,0,700,0,700,C,C,D,D,E,E,350,350,C,C,350,350,350,350,350,E,E,75,75,F,F,75,75,C,C,75,D,F,75,D,F,350,350,F,F,638,638,513,513,513,513,513,513]
    paredes3 = [700,700,A,A,B,B,C,G,C,G,C,G,C,G,C,G,C,G,290,410,410,320,410,C,G,50,700,220,480,270,430,400,400,400,350,350,350,220,480,220,480,270,625,275,425,75,625,C,G]
    paredes4 = [A,B,C,D,C,D,C,C,D,D,E,E,350,350,E,E,D,D,E,E,350,E,E,75,75,F,F,E,E,C,C,75,D,F,C,513,638,D,D,638,638,638,638,513,513,513,513,F,F]
    for i in range(0,49):
        pygame.draw.line(screen,BLUE,(paredes1[i],paredes2[i]),(paredes3[i],paredes4[i]),GROSOR)