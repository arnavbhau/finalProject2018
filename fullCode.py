# this code was made by arnav bhau

# for the side scrolling background, i used a tutorial from https://www.youtube.com/watch?v=US3HSusUBeI
# i also used mr. cozort's code a reference for some parts
# i got the background image from http://www.mariouniverse.com/maps/ds/nsmb

# importing libraries
import random, math, time, sys
import pygame
from pygame.locals import *
from player import Player
from settings import Settings
from pygame.sprite import Sprite

# the run game function 
def setup():
    #initialize pygame, settings, and screen object
    # this uses the settings function to make the settings for this screen
    marioSettings = Settings()
    global screen
    screen = pygame.display.set_mode((marioSettings.screenWidth, marioSettings.screenHeight))
    #initialize
    pygame.init()
    pygame.display.set_caption("Super Mario Bros!")

# making the character group and the background
background = pygame.image.load("finalProject/assets/images/marioplain.png")
# allSpritesList = pygame.sprite.Group()

# defining some variables for the program running
width = 600
x = 0
while True:
    setup()

    # makes the screen move continuously via blitting
    background = background.convert()
    relx = x % background.get_rect().width
    screen.blit(background, [relx - background.get_rect().width, 0])
    if relx < width:
        screen.blit(background, [relx, 0])
    x -= 1

    # loads the characters on the screen
    mario = Player(screen)
    mario.blitme()

    # updates the screen
    pygame.display.flip()

    # to quit the game if the user clicks on the x button
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()