import pygame as pg
from pygame.locals import *
import sys
from main import *
from info_menu import *


WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Menu():
    def __init__(self):

        pg.font.init()

        self.screen = pg.display.set_mode((800,600))
        self.display = pg.display.set_caption ('Spaceships')
        self.background_image = pg.image.load('resources/images/fondo.png').convert()
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 32)


        self.opciones = [

            ('· Historia del juego', historia_juego),
            ('· Instrucciones', instrucciones),
            ('· Jugar ', iniciar_juego),
            ('· Ranking ', ranking),
            ('· Creditos', creditos),
            ('· Salir', salir)
        ]
           
        
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False
           

    def update(self):        
        # opcion elejida
        tecla_pulsada = pg.key.get_pressed()

        if not self.mantiene_pulsado:
            if tecla_pulsada[K_UP]:
                self.seleccionado -= 1
            elif tecla_pulsada[K_DOWN]:
                self.seleccionado += 1
            elif tecla_pulsada[K_RETURN]:

                opcion_menu, funcion = self.opciones[self.seleccionado]
                print('{}'.format(opcion_menu))
                funcion()

        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

       
        self.mantiene_pulsado = tecla_pulsada[K_UP] or tecla_pulsada[K_DOWN] or tecla_pulsada[K_RETURN]

    def mensaje_opciones(self, pantalla):

        total = self.total
        indice = 0
        self.altura_opcion = 60
        x = 100
        y = 140

        for (opcion_menu, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = RED
            else:
                color = WHITE

            texto_pantalla = self.font.render(opcion_menu, 1, color)
            posicion_pantalla = (x,y + self.altura_opcion * indice)
            indice += 1
            self.screen.blit(texto_pantalla, posicion_pantalla)


    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:               
                salir()


    def mainloop_menu(self):
        while True:

            self.handleEvents()

            self.screen.blit(self.background_image, (0, 0))
            self.update()
            self.mensaje_opciones(self.screen)
            

            pg.display.flip()
            pg.time.delay(10)


def historia_juego():
    info_menu = info_Menu()
    info_menu.historia_juego()

    
def iniciar_juego():
    game = Game()
    game.mainloop_juego()

def instrucciones():
    info_menu = info_Menu()
    info_menu.instrucciones()

def ranking():
    print('ranking ')


def creditos():
    info_menu = info_Menu()
    info_menu.creditos()

def salir():
    print('Hasta Pronto!!')
    pg.quit()
    sys.exit()


if __name__ == '__main__':
    menu = Menu()
    menu.mainloop_menu()

