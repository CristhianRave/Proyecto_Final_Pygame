import pygame as pg
from pygame.locals import *
import random
from random import choice, randint


class Nave(pg.sprite.Sprite):
    img_nave = 'nave.png'
    speed = 5
    FPS = 60
    vidas = 5
    
    
    def __init__(self, x = 0, y = 270):
        pg.mixer.init()
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        
        self.nave_normal = pg.image.load('resources/images/{}'.format(self.img_nave)).convert_alpha()
        self.image = self.nave_normal
        pg.mixer.music.load('resources/sounds/Explo.wav')
        self.frames = []  
        self.explotar = False       
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w 
        self.h = self.rect.h
        self.index = 0
        self.how_many = 0
        self.animation_time = self.FPS*2 
        self.current_time = 0
        self.loadFrames()

    def go_up(self):
       self.rect.y = max(0, self.rect.y - self.speed)

    def go_down(self):
       self.rect.y = min(self.rect.y + self.speed, 535)

    def loadFrames(self): 
        self.w = 128
        self.h = 128
        self.sprite_sheet = pg.image.load('resources/images/bomb-sprite.png').convert_alpha()
        for fila in range(4):
            y = fila*self.h
            for columna in range (4):
                x = columna * self.w

                img_explo = pg.Surface((self.w, self.h), pg.SRCALPHA).convert_alpha()
                img_explo.blit(self.sprite_sheet, (0, 0), (x, y, self.w, self.h))
                self.frames.append(img_explo)
        self.how_many = len(self.frames)
        self.image = self.frames[self.index]
    

    def comprobar_colision(self,group):
        colisiones = pg.sprite.spritecollide(self,group,True)
        self.num_candidatos = len(colisiones)
        if self.num_candidatos > 0: 
            self.vidas -= 1   
            self.explotar = True
            pg.mixer.music.play()


    def update(self,dt):
    
        if not  self.explotar :
            self.image = self.nave_normal

        else:             
            self.current_time += dt

            if self.current_time > self.animation_time :   
                if self.index < self.how_many -1:                  
                    self.index += 1   
                else:
                    self.explotar = False
                    self.current_time = 0
                    self.index = 0
            self.image = self.frames[self.index-1] 


class Asteroide(pg.sprite.Sprite):    

    imgs_asteroides =('asteroide_60.png', 'satelite.png', 'saturno.png', 'astronauta.png')

    def __init__(self, x = randint(780, 800), y = randint(10,550), w = 0, h = 0, speed = 1):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed        
        
        self.asteroids = []     
        for img in self.imgs_asteroides:
            self.image = pg.image.load('resources/images/{}'.format(img)).convert_alpha()
            self.asteroids.append(self.image)
        self.image = (random.choice(self.asteroids))

        self.rect = self.image.get_rect()   
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h    

    def update(self, dt):
        self.rect.x -= self.speed
        if self.rect.x <= -self.rect.w:                      
            self.kill() 
            del self