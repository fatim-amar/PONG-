from pygame import *
from random import *


window = display.set_mode((700,500))
display.set_caption("pong")
background = transform.scale(image.load("tenniss_court.jpg"),(700,500))
game = True

FPS = 60
clock = time.Clock()
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, images, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(images), (70, 70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
class Racket(GameSprite) :
    def Move(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 5 :
            self.rect.y += self.speed
            
Rack = Racket("racket.png", 4, 50, 50)








while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT :
            game = False
    Racket.reset()
    Racket.update()    
    
    display.update()