import pygame as  pg
from pygame.locals import *
import sys


RED = (229, 9, 9)
WHITE = (255, 255, 255)


class info_Menu():

    def __init__(self):
        
        self.bucle_info = True

        pg.font.init()
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption ('The Quest')
        self.background_image = pg.image.load('resources/images/fondo8.jpg').convert()
        self.screen.blit(self.background_image, (0, 0))

        self.tamaño_titulo_pequeño = pg.font.Font('resources/fonts/PressStart.ttf', 26)
        self.tamaño_titulo = pg.font.Font('resources/fonts/PressStart.ttf', 32)
        self.tamaño_letra = pg.font.Font('resources/fonts/PressStart.ttf', 16)
     


    def historia_juego(self):

        self.texto1 = self.tamaño_titulo.render('Historia ', True, RED)
        self.texto2 = self.tamaño_letra.render('La búsqueda comienza en un planeta tierra  ', True, WHITE)
        self.texto3 = self.tamaño_letra.render('moribundo por el cambio climático. Partiremos  ', True, WHITE)
        self.texto4 = self.tamaño_letra.render('a la búsqueda de un planeta compatible con  ', True, WHITE)
        self.texto5 = self.tamaño_letra.render('vida humana para colonizarlo. Eres nuestra  ', True, WHITE)
        self.texto6 = self.tamaño_letra.render('ultima esperanza, que la fuerza te acompañe ', True, WHITE)
        self.texto7 = self.tamaño_letra.render('y cumple con tu mision!!', True, WHITE)
        self.texto8 = self.tamaño_letra.render('Menu pulsa "Escape"', True, RED)

        self.screen.blit(self.texto1, (50, 80))
        self.screen.blit(self.texto2, (50, 150))
        self.screen.blit(self.texto3, (50, 190))       
        self.screen.blit(self.texto4, (50, 230))     
        self.screen.blit(self.texto5, (50, 270))
        self.screen.blit(self.texto6, (50, 310))       
        self.screen.blit(self.texto7, (50, 350))    
        self.screen.blit(self.texto8, (50, 550))

        pg.display.flip()                
        self.mainloop_info()


    def instrucciones(self):

        self.texto1 = self.tamaño_titulo.render('Intrucciones', True, RED)
        self.texto2 = self.tamaño_letra.render('Utiliza las teclas arriba ↑ o abajo ↓ ', True, WHITE)
        self.texto3 = self.tamaño_letra.render('para desplazar la nave. ', True, WHITE)
        self.texto4 = self.tamaño_letra.render('Consta de 3 niveles los cuales iran', True, WHITE)
        self.texto5 = self.tamaño_letra.render('aumentando de dificultad por la', True, WHITE)
        self.texto6 = self.tamaño_letra.render('aceleracion de los obstaculos.', True, WHITE)
        self.texto7 = self.tamaño_letra.render('Menu pulsa "Escape"', True, RED)


        self.screen.blit(self.texto1, (50, 80))
        self.screen.blit(self.texto2, (50, 150))
        self.screen.blit(self.texto3, (50, 190))       
        self.screen.blit(self.texto4, (50, 250))     
        self.screen.blit(self.texto5, (50, 290))
        self.screen.blit(self.texto6, (50, 330))       
        self.screen.blit(self.texto7, (50, 550)) 
        

        pg.display.flip()                
        self.mainloop_info()
        
    def creditos(self):

        self.texto = self.tamaño_titulo_pequeño.render('Proyecto fin Bootcamp', True, RED)
        self.texto1 = self.tamaño_titulo_pequeño.render('Aprender a programar ', True, RED)
        self.texto2 = self.tamaño_titulo_pequeño.render('desde cero', True, RED)
        self.texto3 = self.tamaño_letra.render('Realizado en python, libreria pygame 1.9.6', True, WHITE)
        self.texto4 = self.tamaño_letra.render('Creado por: Cristhian David Rave Osorio', True, WHITE)
        
        self.texto5 = self.tamaño_letra.render('Fecha: 23-02-2020', True, WHITE)
        self.texto6 = self.tamaño_letra.render('Profesor: Ramón Maldonado', True, WHITE)
        self.texto7 = self.tamaño_letra.render('Menu pulsa "Escape"', True, RED)

        self.screen.blit(self.texto, (130, 80))
        self.screen.blit(self.texto1, (145, 120))
        self.screen.blit(self.texto2, (260, 160))
        self.screen.blit(self.texto3, (50, 300))       
        self.screen.blit(self.texto4, (50, 340))     
        self.screen.blit(self.texto5, (50, 380))
        self.screen.blit(self.texto6, (50, 420))       
        self.screen.blit(self.texto7, (50, 550))

        pg.display.flip()                
        self.mainloop_info()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.bucle_info = False

    def mainloop_info(self):

        while self.bucle_info:
            self.handleEvents()



