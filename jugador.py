from vglobales import RED, pygame,screen,WHITE,fuente2,fuente
import sys
import time
game_Over = False
menos_vida = False
contador_vidas = 3

def verificador_posisicion (x,y,paso):
   a = 0
   b = 0
   while a == 0:
      if y == 20 or y == 650:
         a = 1
         if x <= 20:
            return 20,y
         elif x >= 640:
            return 640,y
         else:
            return x,y
      
      if y == 86 or y == 585:
         a = 1
         if x >= 20-3 and x <=170+3:
            if x <= 20:
               return 20,y
            elif x >= 170:
               return 170,y
            else:
               return x,y
         if x >= 240-3 and x <=296+3:
            if x <= 240:
               return 240,y
            elif x >= 296:
               return 296,y
            else:
               return x,y
         if x >= 372-3 and x <=420+3:
            if x <= 372:
               return 372,y
            elif x >= 420:
               return 420,y
            else:
               return x,y
         if x >= 490-3 and x <=640+3:
            if x <= 490:
               return 490,y
            elif x >= 640:
               return 640,y
            else:
               return x,y

      if (y == 179 or y == 383) and x >= 230-3 and x <= 440+3:
         a = 1
         if x <= 240:
            return 240,y
         elif x >= 430:
            return 430,y
         else:
            return x,y
      
      if y >= 270 and y <= 280 and (x >= 420-20 or x <= 240+20):
         a = 1
         if x <= 420 and x >= 420-20:
            return 420,y
         elif x >= 240 and x <= 240+20:
            return 240,y
         else:
            return x,y
      
      if y == 461:
         a = 1
         if x >= 20-3 and x <=296+3:
            if x <= 20:
               return 20,y
            elif x >= 296:
               return 296,y
            else:
               return x,y
         if x >= 372-3 and x <=640+3:
            if x <= 372:
               return 372,y
            elif x >= 640:
               return 640,y
            else:
               return x,y
      
      if y == 521:
         a = 1
         if x >= 20-3 and x <=90+3:
            if x <= 20:
               return 20,y
            elif x >= 90:
               return 90,y
            else:
               return x,y
         if x >= 170-3 and x <=490+3:
            if x <= 170:
               return 170,y
            elif x >= 490:
               return 490,y
            else:
               return x,y
         if x >= 570-3 and x <=640+3:
            if x <= 570:
               return 570,y
            elif x >= 640:
               return 640,y
            else:
               return x,y

      if x == 20 or x == 640:
         a = 1
         if y >= 20-3 and y <=86+3:
            if y <= 20:
               return x,20
            elif y >= 86 and y <= 86+10:
               return x,86
            else:
               return x,y
         if y >= 461-3 and y <=521+3:
            if y <= 461 and y >= 461-10:
               return x,461
            elif y >= 521 and y <= 521+10:
               return x,521
            else:
               return x,y
         if y >= 585-3 and y <=650+3:
            if y <= 585 and y >= 585-10:
               return x,585
            elif y >= 650:
               return x,650
            else:
               return x,y

      if (x == 90 or x == 570) and y >= 521-3 and y <= 585+3:
         a = 1
         if y <= 521:
            return x,521
         elif y >= 585:
            return x,585
         else:
            return x,y
      
      if x >= 240 and x <= 250 or x >= 420 and x <= 430:
         a = 1
         if y >= 20-3 and y <=86+10:
            if y <= 20:
               return x,20
            elif y >= 86 and y <= 86+10:
               return x,86
            else:
               return x,y
         if y >= 179-10 and y <=461+10:
            if y <= 179 and y >= 179-10:
               return x,179
            elif y >= 461 and y <= 461+10:
               return x,461
            else:
               return x,y
         if y >= 521-10 and y <=585+3:
            if y <= 521 and y >= 521-10:
               return x,521
            elif y >= 585:
               return x,585
            else:
               return x,y

      if x == 296 or x == 372:
         a = 1
         if y >= 86-3 and y <=179+10:
            if y <= 86:
               return x,86
            elif y >= 179 and y <= 179+10:
               return x,179
            else:
               return x,y
         if y >= 461-10 and y <=521+10:
            if y <= 461 and y >= 461-10:
               return x,461
            elif y >= 521 and y <= 521+10:
               return x,521
            else:
               return x,y
         if y >= 585-10 and y <=650+3:
            if y <= 585 and y >= 585-10:
               return x,585
            elif y >= 650:
               return x,650
            else:
               return x,y
      
      if x >= 160 and x <= 170 or x >= 490 and x <= 500:
         a = 1
         if y <= 20:
            return x,20
         elif y >= 585:
            return x,585
         else:
            return x,y

      if a == 0:
         if b == 0:
            x += paso
            b += 1
         elif b == 1:
            x -= paso
            y += paso
            b += 1
         elif b == 2:
            y -= paso
            x -= paso
            b += 1
         elif b == 3:
            x += paso
            y -= paso
   
   

def jugador(x, y,imagen_tigre1,imagen_tigre2,imagen_tigre3):
   global Pac
   global menos_vida
   global contador_vidas
   global f

   Pac = pygame.image.load("niña.jpg").convert()
   Pac.set_colorkey(WHITE)
   imagen_jugador = screen.blit(Pac,[x, y])
   if imagen_jugador.colliderect(imagen_tigre1) or imagen_jugador.colliderect(imagen_tigre2) or imagen_jugador.colliderect(imagen_tigre3):
      contador_vidas -= 1
      print(contador_vidas)
      
      time.sleep(3)
      menos_vida = True
   if contador_vidas == 0:
      global game_Over
      game_Over = True
   vida = fuente2.render('Vida: '+str(contador_vidas),True,RED)
   screen.blit(vida,(20,20))   
   return imagen_jugador

def Game_over():
   return game_Over

def Menos_vida():
   return menos_vida

def Reset_Menos_vida():
   global menos_vida
   menos_vida = False