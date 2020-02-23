import pygame as pg
from pygame.locals import *


class Planeta(pg.sprite.Sprite):  
    clock = pg.time.Clock()
    FPS = 60  
    imgs_planeta = ('planeta.png')

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
WHITE = (255, 255, 255)
GREEN = (30, 186, 22)

class Nave_rotate(pg.sprite.Sprite):  

    FPS = 60  
    imgs_nave = ('nave.png')

    def __init__(self, x = 0, y = 270,  speed = 1):

        pg.font.init()
        pg.sprite.Sprite.__init__(self)
        self.fonty = pg.font.Font('resources/fonts/PressStart.ttf', 52)
        self.font = pg.font.Font('resources/fonts/PressStart.ttf', 22)
  
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
        self.ganaste = self.fonty.render('Ganaste!!', True, RED)
        self.ganaste1 = self.font.render('Preciona "Space" para guardar', True, GREEN)
        self.ganaste2 = self.font.render('puntaje y volver al Menu.', True, GREEN)
        self.screen.blit(self.ganaste,(180, 150))
        self.screen.blit(self.ganaste1,(100, 400))
        self.screen.blit(self.ganaste2,(120, 450))
 

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
        