import pygame
import os

class Platform:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)  # Create a Rect for collision detection
        self.sfx = pygame.mixer.Sound(os.path.join("Project Bounce","assets","sounds","bounce.wav"))

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

# 50/50 ai srry meneer kon het egt niet meer aan T-T
    def update(self, ball):
        if self.vertical_collision_bottom(ball):
            print("Bottom collision")
            self.sfx.play()
            ball.yVel = -700
            ball.y = self.y - ball.height 
            return True
        elif self.vertical_collision_top(ball):
            print("Top collision")
            self.sfx.play()
            ball.yVel = 700
            ball.y = self.y + self.height  
            return True

        # Check horizontal collision (left and right)
        if self.horizontal_collision_left(ball):

            return True
        elif self.horizontal_collision_right(ball):
            
            return True

        return False

    def vertical_collision_bottom(self, ball):
        return (ball.y + ball.hitboxHeight >= self.y and ball.y < self.y + self.height and
                ball.x + ball.hitboxWidth > self.x and ball.x < self.x + self.width and ball.yVel > 0)

    def vertical_collision_top(self, ball):
        return (ball.y <= self.y + self.height and ball.y + ball.hitboxHeight > self.y and
                ball.x + ball.hitboxWidth > self.x and ball.x < self.x + self.width and ball.yVel < 0)

    def horizontal_collision_left(self, ball):
        return (ball.x <= self.x + self.width and ball.x + ball.hitboxWidth > self.x and
                ball.y + ball.hitboxHeight > self.y and ball.y < self.y + self.height and ball.xVel < 0)

    def horizontal_collision_right(self, ball):
        return (ball.x + ball.hitboxWidth >= self.x and ball.x < self.x + self.width and
                ball.y + ball.hitboxHeight > self.y and ball.y < self.y + self.height and ball.xVel > 0)
    

# wall
class Wall:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)  # Create a Rect for collision detection

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
