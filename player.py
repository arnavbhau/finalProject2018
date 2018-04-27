# for making the player move, i used a tutorial from https://www.youtube.com/watch?v=AX8YU2hLBUg
#importing the libraries for the player class
import pygame
from pygame.sprite import Sprite
from pygame.locals import *

#the actual player class for mario
class Player(Sprite):
    def __init__(self, screen, velocity, maxJumpRange):
        # initializes the player class
        super(Player, self).__init__()
        self.screen = screen
        #this is the background image
        self.image = pygame.image.load("finalProject/assets/images/mariospriteEdit.png")
        # in order for python images to work and process
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # self.rect.centerx = (200, 200)
        self.center = float(self.rect.centerx)
        # sets the velocity and the maximum jump range for the player
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange
        # the new position
        self.new_pos = [(self.rect.centerx),(self.rect.centery)]
        

    # a set location method with basics
    def setLocation(self, x, y):
        # the x and y coordinates for the player
        self.x = x
        self.y = y
        # the velocity to move the player
        self.xVelocity = 0
        # for jumping and falling
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True

    # the keys function for the player to move with the keys
    def keys(self):
        # a key function in pygame
        k = pygame.key.get_pressed()

        # the left key, which makes the player set up to move left with a "negative" velocity
        if k[K_LEFT]:
            self.xVelocity = -self.velocity

        # the right key, which makes the player set up to move right with a positive velocity
        elif k[K_RIGHT]:
            self.xVelocity = self.velocity
        
        # if the player's not going to the left or right, then the x velocity is 0
        else:
            self.xVelocity = 0

        #if the up key is pressed, and the vehicle's not falling - then set to jumping
        if k[K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0

    # the move function which makes it so that the player can move as a result of the keys
    def move(self):
        # adds additional xvelocity to the x corrdinate to make it move to the next one
        self.x += self.xVelocity
        #checking teh x boundaries
        # if the player's jumping, the y now goes down to fall
        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            # if the jump counter equals than the maximum range via which the palyer can jump, he starts falling
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        # if he's falling then the y gets back to normal
        elif self.falling:
            if self.y <= 375 and self.y + self.velocity >= 375:
                self.y = 375
                self.falling = False
            # if not then add velocity to y
            else:
                self.y += self.velocity

    def update(self):
        # update laser based on mouse position changes
        # self.rect.x+=self.velx
        # self.rect.y+=self.vely
        # self.rot = pygame.transform.rotate(self.image, 360-self.angle*57.29)
        self.new_pos = [self.x, self.y]

        #part of the update function, after the first two functions occur to upate the player's location
    def blitme(self):
        # draw mario on screen
        self.screen.blit(self.image, self.new_pos)

    # actually runs the functions in one
    def do(self):
        self.keys()
        self.move()
        self.update()


    # def update(self):
    #     self.rect.centerx = self.center