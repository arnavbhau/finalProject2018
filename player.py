import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Player(Sprite):
    def __init__(self, screen, velocity, maxJumpRange):
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("finalProject/assets/images/mariospriteEdit.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = (200,200)
        self.center = float(self.rect.centerx)
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange

    def setLocation(self):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True
    
    def keys(self):
        k = pygame.key.get_pressed()
        if k[K_LEFT]:
            self.xVelocity = -self.velocity
        if k[K_RIGHT]
        


    def update(self):
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)

## for moving, he has lines that ask if the keys down
## 