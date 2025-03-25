#==================================import-libraies==========================#
import pygame
from pygame.locals import *
import sys

#==================================import-objects==========================#
from objects.objects import *
from objects.obsticals import *

#==================================import-levels==========================#
from levels.levels import *
from levels.mianScreen import *

#==================================config==================================#
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FRAMES_PER_SECOND = 60

#==================================basic_initlaition=======================#
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
game_state = "start_start"

#==================================variables===============================#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#==================================sounds==================================#
colect_sfx = pygame.mixer.Sound("assets\sounds\collect.wav")

#==================================objects=================================#
ball = Ball(WINDOW_WIDTH, WINDOW_HEIGHT)
coin = Coin(WINDOW_WIDTH, WINDOW_HEIGHT)

#==================================main_loop===============================#
while True:
    dt = clock.tick(FRAMES_PER_SECOND) / 1000.0 #ads down time

    for event in pygame.event.get(): # makes you be able to close the game
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    if game_state == "start_start":
        game_state = mainScreen(window, clock, BLACK, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, game_state)
    elif game_state == "level1":
        game_state = level1(window, clock, ball, coin, colect_sfx, BLACK, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, font, dt,Platform,Wall)
    

 