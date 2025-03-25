import pygame
from pygame.locals import *
import sys

isSecond = 0
firstTime = True


def levelTimer(time, window, WINDOW_WIDTH, color, font, timebarBack):
    global isSecond, firstTime, prevtime

    if firstTime:
        print("hello")
        prevtime = time
        firstTime = False

    isSecond += 1

    if isSecond >= 60:
        isSecond = 0
        prevtime = prevtime - 1
        print(prevtime)
        
        if prevtime <= 0:
            print("Time is up")
            game_state = "game_over"
            return game_state


    centerx = WINDOW_WIDTH // 2
    centery = timebarBack.get_height() // 2
    width = timebarBack.get_width()
    height = timebarBack.get_height()

    timebarBackrec = timebarBack.get_rect(centerx=centerx, centery=centery, width=width, height=height)
    window.blit(timebarBack, timebarBackrec)

    time_text = font.render(str(prevtime), True, color)
    timeDisplay = window.blit(time_text, (WINDOW_WIDTH // 2 - time_text.get_width() // 2, 30))

    return timeDisplay, prevtime 


def level1(window, clock, ball, coin, colect_sfx, BLACK, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND, font, dt,Platform,wall): 
    timebarBack = pygame.image.load("assets/ui/Bar_layer1.png")
    font = pygame.font.Font(None, 36)
    running = True 
    platforms = [
        Platform(820, 600, 200, 20, WHITE),  
        Platform(1000, 400, 250, 20, WHITE),  
        Platform(600, 900, 200, 20, WHITE),  
        Platform(200, 200, 300, 20, WHITE),  
        Platform(200, 800, 100, 30, WHITE),  
        Platform(200, 500, 300, 20, WHITE), 
        Platform(1150, 700, 200, 20, WHITE), 
        Platform(1500, 350, 150, 20, WHITE),  
        Platform(1100, 200, 200, 20, WHITE),  
        Platform(600, 200, 200, 20, WHITE),   
    ]

    walls = [
        wall(1000, 422, 20, 180, WHITE),   
        wall(1500, 800, 20, 200, WHITE),    
        wall(500, 200, 20, 100, WHITE),    
    ]

    ball.update(dt, WINDOW_WIDTH, WINDOW_HEIGHT, walls,platforms)
    while running:
        dt = clock.tick(FRAMES_PER_SECOND) / 1000.0  # Delta time

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE: 
                return "start_start"
        # Drawing
        window.fill(BLACK)
        levelTimer(5, window, WINDOW_WIDTH,BLACK,font, timebarBack)
        window.blit(ball.sprite, (ball.x, ball.y))  # Draw objects
        window.blit(coin.sprite, (coin.x, coin.y))
        
        for Platform in platforms:
            Platform.draw(window)
        for wall in walls:
            wall.draw(window)

        point_score = font.render(f"Points: {coin.points}", True, WHITE)
        window.blit(point_score, (10, 10))

        ball.update(dt, WINDOW_WIDTH, WINDOW_HEIGHT, walls,platforms)
        if coin.update(ball):
            coin.get_points()
            colect_sfx.play()
            coin.loction_change(WINDOW_WIDTH, WINDOW_HEIGHT)

        for Platform in platforms:
            Platform.update(ball)
        for wall in walls:
            wall.draw(window)
       
        
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)
    
    return "start_start" 