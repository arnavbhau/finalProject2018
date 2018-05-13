# for making the player move, i used a tutorial from kids can code and chris bradfield --
# https://www.youtube.com/watch?v=nGufy7weyGY&index=3&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw

#importing the libraries for the player class
import pygame, math
from pygame.sprite import Sprite
from pygame.locals import *

#the actual player class for mario
class Player(pygame.sprite.Sprite):
    # initializes the class with some necessary variaables
    def __init__(self):
        # initializes the super class, Sprite from pygame
        pygame.sprite.Sprite.__init__(self)
        # loads the image of the player Mario which I edited and cropped to the edges on photoshop 
        self.image = pygame.image.load("finalProject/assets/images/mariospriteEdit.png")
        # gets the rect of the image
        self.rect = self.image.get_rect()
        # sets the initial position
        self.rect.center = (50, 304)

    # the update function for the player, the majority of what makes mario move
    def update(self):
        # sets self vx and vy variables in order to make changes to the self.rect.x and y variables
        # these are essentially "change in" x and y
        self.vx, self.vy = 0, 0
        # setting the function to detect if the user presses a key
        keystate = pygame.key.get_pressed()
        # if the user presses the up key
        if keystate[pygame.K_UP]:
            # the change in y is that it decreases by 5 - its a decrease because in the computer's grid
            # when we decrease the y coordinate, we're actually going up
            self.vy = -5
        # if the user presses the up key
        if keystate[pygame.K_DOWN]:
            # adds 5 to y, making it go down
            self.vy = 5
        # if the user presses the left and right keys - adjusts the change in x accordingly
        if keystate[pygame.K_LEFT]:
            self.vx = -10
        if keystate[pygame.K_RIGHT]:
            self.vx = 10
        # adds the changes to the original self.rect.x and y to update the changes on the screen
        self.rect.x += self.vx
        self.rect.y += self.vy
