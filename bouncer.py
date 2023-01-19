import pygame as pg

GREY=(222,222,222)
BLACK=(0,0,0)

class Bouncer(pg.sprite.Sprite):
    
    def __init__(self,width,height):
        super().__init__()
        self.image=pg.Surface((width,height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pg.draw.rect(self.image,GREY,[0,0,width,height])
        self.rect=self.image.get_rect()

    def moveUp(self,pixels):
        self.rect.y-=pixels
        if self.rect.y<0:
            self.rect.y=60

    def moveDown(self,pixels):
        self.rect.y+=pixels
        if self.rect.y>600:
            self.rect.y=540
