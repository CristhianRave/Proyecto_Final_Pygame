import pygame as pg
from pygame.locals import *
import random
from random import choice, randint

FPS = 60


class Nave(pg.sprite.Sprite):
    img_nave = 'nave.png'
    speed = 5

    def __init__(self, x = 0, y = 270):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.image = pg.image.load('resources/images/{}'.format(self.img_nave)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = self.rect.w
        self.h = self.rect.h

    def go_up(self):
       self.rect.y = max(0, self.rect.y - self.speed)

    def go_down(self):
       self.rect.y = min(self.rect.y + self.speed, 600-self.w)



class Asteroide(pg.sprite.Sprite):
    
    imgs_asteroides =('asteroide_60.png', 'asteroide_200.png', 'satelite.png', 'saturno.png', 'astronauta.png')

    def __init__(self, x = randint(780, 800), y = randint(-10,550), w = 0, h = 0, speed = 5):
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
        if self.rect.x <= -170: 
            self.kill() 
            del self