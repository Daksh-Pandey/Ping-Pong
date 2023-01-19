import pygame as pg
from random import randint

ORANGE=(255,140,0)
BLACK=(0,0,0)


class Ball(pg.sprite.Sprite):
    
    def __init__(self,width,height):
        super().__init__()
        self.image=pg.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pg.draw.ellipse(self.image, ORANGE, [0,0,width,height])
        self.velocity=[randint(-4,4),randint(-4,4)]
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]

    def bounce(self):
        self.velocity[0]=-self.velocity[0]
        self.velocity[1]=randint(-4,4)
