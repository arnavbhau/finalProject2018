#importing the libraries for the game functions
import pygame, sys
from pygame.locals import *

# a check events function that's sole purpose is to determine if the user clicks on the x out of the window button
# amd if that happens, exits out of the window
def check_events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
