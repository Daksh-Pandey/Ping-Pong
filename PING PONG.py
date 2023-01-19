import pygame as pg
from bouncer import Bouncer
from ball import Ball

pg.init()
screen=pg.display.set_mode((800,600))
pg.display.set_caption('PING PONG')

bouncer1=Bouncer(10,60)
bouncer1.rect.x=20
bouncer1.rect.y=290

bouncer2=Bouncer(10,60)
bouncer2.rect.x=770
bouncer2.rect.y=290

ball=Ball(30,30)
ball.rect.x=380
ball.rect.y=290

all_sprites=pg.sprite.Group()
all_sprites.add(bouncer1)
all_sprites.add(bouncer2)
all_sprites.add(ball)

clock=pg.time.Clock()

GREY=(222,222,222)
BLACK=(0,0,0)
WHITE = (255,255,255)

score=0
play=True

while play:
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            play=False
    
    keys=pg.key.get_pressed()
    if keys[pg.K_w]:
        bouncer1.moveUp(10)
    elif keys[pg.K_s]:
        bouncer1.moveDown(10)
    if keys[pg.K_UP]:
        bouncer2.moveUp(10)
    elif keys[pg.K_DOWN]:
        bouncer2.moveDown(10)
        
    all_sprites.update()
    
    if ball.rect.y<=10 or ball.rect.y>=570:
        ball.velocity[1]=-ball.velocity[1]
    
    if pg.sprite.collide_mask(ball,bouncer1) or pg.sprite.collide_mask(ball,bouncer2):
        ball.bounce()
        score+=1

    if ball.rect.x<=-30 or ball.rect.x>=830:
        font=pg.font.Font(None,100)
        text=font.render('GAME OVER',1,WHITE)
        screen.blit(text,(200,200))
        pg.display.flip()
        pg.time.wait(3000)
        play=False

    font=pg.font.Font(None,35)
    text=font.render(f'Score: {score}',1,WHITE)
    screen.blit(text,(300,20))
    pg.display.flip()
    
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(60)
    
pg.quit()
