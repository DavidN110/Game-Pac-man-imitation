import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

size = (700, 700)

CENTROX = 350
CENTROY = 350
GROSOR = 5

speed_x = 0
speed_y = 0
cord_x = 20
cord_y = 20

paso_personaje = 2
paso_tigres = 1

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

cord_x_t1 = CENTROX-60
cord_y_t1 = CENTROY-50

cord_x_t2 = CENTROX-20
cord_y_t2 = CENTROY-50

cord_x_t3 = CENTROX+20
cord_y_t3 = CENTROY-50

Pac = 0
tigre1 = 0
tigre1c = 0
tigre2 = 0
tigre2c = 0
tigre3 = 0
tigre3c = 0

comidas = []
No_comidas = []
pygame.font.init()
fuente = pygame.font.Font("fnt.ttf", 30)
fuente2 = pygame.font.Font("fnt.ttf", 12)
fuente3 = pygame.font.Font("fnt.ttf",100)


A=40
B=110
C=200
D=300
E=400
F=480
G=550
H=610
I=670

Lista_comidax=[
    40,110,180,250,320,390,460,530,600,670, #A
    40,110,180,250,320,390,460,530,600,670, #B
    190,270,350,430,510, #C
    30,110,190,270,430,510,590,670,750, #D
    190,270,350,430,510, #E
    30,110,190,270,430,510,590,670,750, #F
    38,116,194,272,350,428,506,584,662,740, #G
    38,116,194,272,428,506,584,662,740, #H
    40,110,180,250,320,390,460,530,600,670,740#I
    ]
Lista_comiday=[
    A,A,A,A,A,A,A,A,A,A,
    B,B,B,B,B,B,B,B,B,B,
    C,C,C,C,C,
    D,D,D,D,D,D,D,D,D,
    E,E,E,E,E,
    F,F,F,F,F,F,F,F,F,
    G,G,G,G,G,G,G,G,G,G,
    H,H,H,H,H,H,H,H,H,
    I,I,I,I,I,I,I,I,I,I
    ]

comidas = []

dir1 = 1
dir2 = 1
dir3 = 1