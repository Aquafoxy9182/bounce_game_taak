import pygame
from pygame.locals import * 
import os 

def mainScreen(window, clock, BLACK, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND,game_state):
    
    background = pygame.image.load(os.path.join("Project Bounce","assets","img","beautiful-color-ui-gradients-backgrounds-sexy-blue.png"))
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    backgroundStars = pygame.image.load(os.path.join("Project Bounce","assets","ui","Background_2.png"))
    backgroundStars = pygame.transform.scale(backgroundStars, (WINDOW_WIDTH, WINDOW_HEIGHT))

    startButton = pygame.image.load(os.path.join("Project Bounce","assets","ui","StartButton.png"))
    startButton = pygame.transform.scale(startButton, (300, 100))

    settingButton = pygame.image.load(os.path.join("Project Bounce","assets","ui","Settings.png"))
    settingButton = pygame.transform.scale(settingButton, (80, 80))


    startButtonRect = startButton.get_rect()
    startButtonRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    settingButtonRect = settingButton.get_rect()
    settingButtonRect.center = (WINDOW_WIDTH-100, 10)
    settingButtonRect = settingButtonRect.inflate(80, 80)
  
    running = True
    while running:
        window.blit(background, (0, 0))  # Draw background
        window.blit(backgroundStars, (0, 0)) # Draw background stars
        window.blit(startButton, startButtonRect.topleft)  # Draw the button
        window.blit(settingButton, settingButtonRect.center) # draw settings button
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:  # Only check position when the mouse is clicked
                if startButtonRect.collidepoint(event.pos):  
                    game_state = "level1"
                    return game_state
                elif settingButtonRect.collidepoint(event.pos):  
                    print("Settings button clicked")
        # Update screen  
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)