import pygame as pg
from pygame.locals import *


class Planeta(pg.sprite.Sprite):  
    clock = pg.time.Clock()
    FPS = 60  
    imgs_planeta = ('luna.png')

    def __init__(self, x = 800, y = 0,  speed = 1):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.speed = speed
 
        self.image = pg.image.load('resources/images/{}'.format(self.imgs_planeta)).convert_alpha()
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
        self.animation_time = self.FPS//2 
        self.current_time = 0

    def update(self, dt):
        self.current_time += dt      
        if self.current_time > self.animation_time: 
            self.current_time = 0
            self.rect.x -= 1
        if self.rect.x == 600:
            self.rect.x += 1
            self.speed = 0


RED = (255, 0, 0)
class Nave_rotate(pg.sprite.Sprite):  
    clock = pg.time.Clock()
    FPS = 60  
    imgs_nave = ('nave.png')

    def __init__(self, x = 0, y = 270,  speed = 1):
        pg.font.init()
        pg.sprite.Sprite.__init__(self)
        self.fonty = pg.font.Font('resources/fonts/PressStart.ttf', 52)
  
        self.screen = pg.display.set_mode((800,600))

        self.x = x
        self.y = y
        self.speed = speed
 
        self.image = pg.image.load('resources/images/{}'.format(self.imgs_nave)).convert_alpha()
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
        self.animation_time = self.FPS//2 
        self.current_time = 0
        self.angulo = 0


    def muestra_texto(self):
        self.ganaste = self.fonty.render('Ganaste', True, RED)
        self.screen.blit(self.ganaste,(200,250))

    def rotar (self):
        self.imagen = pg.transform.rotate(self.image, self.angulo)
        if self.rect.x > 400:
            self.angulo += 1 
        if self.angulo > 180:
            self.angulo = 180
        
        self.screen.blit(self.imagen, self.rect)

    def update(self, dt):
        self.current_time += dt 
        self.rect.x += 1  
        self.rotar()

        if self.current_time > self.animation_time: 
            self.current_time = 0      
        
        if self.rect.x == 650:          
            self.rect.x -= 1
            self.speed = 0            
            self.muestra_texto()
        