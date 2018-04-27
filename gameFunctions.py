#importing the libraries for the player class
import pygame
from pygame.sprite import Sprite
from pygame.locals import *

def check_events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()