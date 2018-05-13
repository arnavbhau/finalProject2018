'''' 
this code was made by arnav bhau

for the side scrolling background, i used a tutorial from https://www.youtube.com/watch?v=US3HSusUBeI
i also used mr. cozort's code a reference for some parts
i got the background image from http://www.mariouniverse.com/maps/ds/nsmb 
'''

# importing libraries
import time, sys, pygame
from pygame.locals import *
from pygame.sprite import Sprite
from player import Player
from settings import Settings
import gameFunctions as gf

# a basic setup function to start the game up so it can function 
def setup():
    #initialize pygame, settings, and screen object
    # this uses the settings function to make the settings for this screen
    marioSettings = Settings()
    # globalizes the variable screen so that it functions throughout the program and not just locally
    global screen
    # sets the dimensions of the screen to the dimensions outlined in the settings function
    screen = pygame.display.set_mode((marioSettings.screenWidth, marioSettings.screenHeight))
    #initialize pygame with the screen
    pygame.init()
    # sets the window display caption at the top
    pygame.display.set_caption("My Super Mario Bros Game!")

# making the background and defining some variables for the program running
#makes the background, an image online - i got the image from http://www.mariouniverse.com/maps/ds/nsmb 
background = pygame.image.load("finalProject/assets/images/marioplain.png")
# makes width and keyvar variables
width = 600
keyvar = 0
# makes a clock for fps rate
clock = pygame.time.Clock()
#makes a group and adds mario to it - mario is the only sprite, but this eases the draw function later on
all_sprites = pygame.sprite.Group()
# sets mario as an instance of the player class
mario = Player()
all_sprites.add(mario)

#getting the sound running
# music from https://www.youtube.com/watch?v=D0eD2ioPOqo
pygame.mixer.init()
pygame.mixer.music.load("finalProject/assets/sounds/themesong.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# the game loop
while True:
    # actually runs the setup function from above
    setup()
    # makes the fps rate for the clock equal to 30
    clock.tick(30)
    # if the user presses x then the window is exited out of - the functions in gameFunctions.py
    gf.check_events()
    # makes the screen move continuously via blitting - this was probably my biggest challenge
    # the convert function allows the background to fit the window
    background = background.convert()
    # uses the modulus operator - this divides x by the width of the background and returns the remainder
    # thus, relx can only be the values between 0 and the screen
    relx = keyvar % background.get_rect().width
    # now when we deduct the background width we get the x coordinate needed for blitting
    screen.blit(background, [relx - background.get_rect().width, 0])
    # this attaches another background image to the end of the first image for continuous blitting75
    if relx < width:
        screen.blit(background, [relx, 0])
    keyvar -= 1
    # loads the character on the screen
    all_sprites.update()
    all_sprites.draw(screen)
    # updates the screen
    pygame.display.flip()
