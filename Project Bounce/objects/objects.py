#==================================imports=================================#
import pygame
import random
import os

#==================================Ball====================================#
class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        self.x = 50
        self.y = 1000
        self.width = 100
        self.height = 100
        self.hitboxWidth = 50
        self.hitboxHeight = 80
        self.speed = 400
        self.gravity = 800
        self.xVel = 0
        self.yVel = 0
        self.sprite = pygame.image.load(os.path.join("Project Bounce", "assets", "ui", "PlanetPink.png")) #chat gpt

        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        self.sfx = pygame.mixer.Sound(os.path.join("Project Bounce", "assets", "sounds", "bounce.wav"))

    def update(self, dt, screen_width, screen_height, walls,platforms):
        self.move(dt)
        self.do_gravity(dt)
        self.check_boundaries(screen_width, screen_height, walls,platforms, dt)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.x += self.speed * dt
    
    def do_gravity(self, dt):
        self.yVel += self.gravity * dt  
        self.y += self.yVel * dt


    def check_boundaries(self, screen_width, screen_height, walls,platforms, dt):
        def check_collision(a, b):
            if (a.x + a.width > b.x and a.x < b.x + b.width and
                a.y + a.height > b.y and a.y < b.y + b.height):  # General collision check
                
                # is collision aan de left of right
                if a.x + a.width - b.x < b.x + b.width - a.x:
                    return "left"
                elif b.x + b.width - a.x < a.x + a.width - b.x:
                    return "right"
            return None
        
        for wall in walls:  
            leftRight = check_collision(self, wall)
            if check_collision(self, wall): 
                if leftRight == "left":
                    self.x = self.x - self.x * dt
                    self.sfx.play()
                    self.xVel = -700
                elif leftRight == "right":
                    self.sfx.play()
                    self.x = self.x + self.x * dt
                else:
                    return None

        if self.y < 0:
            self.y = 0
            self.yVel = -self.yVel
        elif self.y > screen_height - self.height:
            self.y = screen_height - self.height
            self.sfx.play()
            self.yVel = -700
    
        if self.x < 0:
            self.x = 0
        elif self.x > screen_width - self.width:
            self.x = screen_width - self.width

#==================================Coin====================================#
class Coin(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        xValueMAX = screen_width - ((screen_width/100) * 10) #hoe hoog de coin can spawnen
        yValueMAX = screen_height - ((screen_height/100) * 10) #hoe breed de coin can spawnen

        xValueMIN = (screen_width / 100) * 0 #de minimum margin waar de coin kan spawnen
        yValueMIN = (screen_height / 100) * 5 #dde minimum margin waar de coin kan spawnen

        self.x = random.randint(int(xValueMIN), int(xValueMAX))
        self.y = random.randint(int(yValueMIN), int(yValueMAX))
        self.width = 50
        self.height = 50
        
        self.points = 0
        self.sprite = pygame.image.load(os.path.join("Project Bounce","assets","img","coin.png"))
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))

    def update(self, ball):
        if self.collides_with_ball(ball):
            return True
        else:
            return False

    def collides_with_ball(self, ball):
        if self.x + self.width > ball.x and self.x < ball.x + ball.width and self.y + self.height > ball.y and self.y < ball.y + ball.height:
            return True
        else:
            return False
    
    def get_points(self):
        self.points = self.points + 1

    def loction_change(self,screen_width, screen_height):
        xValueMAX = screen_width - ((screen_width/100) * 10) #hoe hoog de coin can spawnen
        yValueMAX = screen_height - ((screen_height/100) * 10) #hoe breed de coin can spawnen

        xValueMIN = (screen_width / 100) * 0 #de minimum margin waar de coin kan spawnen
        yValueMIN = (screen_height / 100) * 5 #dde minimum margin waar de coin kan spawnen

        self.x = random.randint(int(xValueMIN), int(xValueMAX))
        self.y = random.randint(int(yValueMIN), int(yValueMAX))

    
        
