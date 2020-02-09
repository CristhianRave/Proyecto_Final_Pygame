import pygame as pg
from pygame.locals import *
import sys
from entities import *
from random import randint

FPS = 60

class Game:
    clock = pg.time.Clock()

    def __init__(self):
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption ('Spaceships')
        self.background_image = pg.image.load('resources/images/fondo.png').convert()

        self.player = Nave()
        self.asteroide = Asteroide()

        self.allSprites = pg.sprite.Group()
        self.asteroidesGroup = pg.sprite.Group()

        self.allSprites.add(self.player)
        self.asteroidesGroup.add(self.asteroide)

        self.asteroides_en_pantalla = 20
        self.new_asteroide = FPS//2
        self.crear_asteroid = FPS*6

 
    def crear_asteroides(self, dt):       
        self.new_asteroide += dt
        if  self.new_asteroide >= self.crear_asteroid:
            self.asteroide = Asteroide(randint(780, 840), randint(-10, 550))
            self.asteroide.speed = (randint(1, 3))
            self.asteroidesGroup.add(self.asteroide)
            self.new_asteroide = 0  # Se reinicia a cero para que  los obstaculos no salgan de golpe

    def gameOver(self):
        pg.quit()
        sys.exit()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.gameOver()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.player.go_up()

                if event.key == K_DOWN:
                    self.player.go_down()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.player.go_up()
        if keys_pressed[K_DOWN]:
            self.player.go_down()

    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)
            self.handleEvents()
            
            self.player.comprobar_colision(self.asteroidesGroup)
                

            if self.player.vidas == 0:
                self.gameOver()

            self.screen.blit( self.background_image, (0,0))
        
            cant_asteroides_creados = len(self.asteroidesGroup)
            if cant_asteroides_creados < self.asteroides_en_pantalla:
                self.crear_asteroides(dt)

            self.allSprites.update(dt)
            self.asteroidesGroup.update(dt)

            self.allSprites.draw(self.screen)
            self.asteroidesGroup.draw(self.screen)




            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.mainloop()