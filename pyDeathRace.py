import os
import pygame
import ctypes

# Def colores y fps

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
celeste = (0, 255, 255)
purple = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
fps = 30

#assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Meta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "meta.jpg")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = (displayW / 2)
        self.rect.y = 0

class Player1(pygame.sprite.Sprite):
    # sprite for player 1
    start = ((displayW / 2) + (display / 10))
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "playerA.png")).convert()
        
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = ((displayW / 2) + (displayW / 8) , 0)
        self.xSpeed = 0
        self.ySpeed = 0

    def update(self):
        maxspeed = 15
        deltaS = 2
        keystate = pygame.key.get_pressed()
        if self.rect.bottom > displayH or self.rect.top < 0 or self.rect.left < 0 or self.rect.right > displayW:
            self.rect.center = (displayW / 2, displayH *.8)
            self.xSpeed = 0
            self.ySpeed = 0
        elif keystate[pygame.K_LEFT]:
            if self.xSpeed + self.ySpeed >= maxspeed:
                self.xSpeed = maxspeed - self.ySpeed
            else: self.xSpeed -= deltaS
        elif keystate[pygame.K_RIGHT]:
            if self.xSpeed + self.ySpeed >= maxspeed:
                self.xSpeed = maxspeed - self.ySpeed
            else: self.xSpeed += deltaS
        elif keystate[pygame.K_DOWN]:
            if self.xSpeed + self.ySpeed >= maxspeed:
                self.ySpeed = maxspeed - self.xSpeed
            else: self.ySpeed += deltaS
        elif keystate[pygame.K_UP]:
            if self.xSpeed + self.ySpeed >= maxspeed:
                self.ySpeed = maxspeed - self.xSpeed
            else: self.ySpeed -= deltaS
        
            
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed
        

pygame.init()

res = ctypes.windll.user32
scale = round(1012 / res.GetSystemMetrics(0))
displayW = int(1012 * (scale))
displayH = int(750 * (scale))
gameDisplay = pygame.display.set_mode((displayW, displayH))
clock = pygame.time.Clock()
mapa = pygame.image.load(os.path.join(img_folder, "track.jpg")).convert()

pygame.display.set_caption('pyDeathRace')


all_sprites = pygame.sprite.Group()
player1 = Player1()
meta = Meta()
all_sprites.add(meta)
all_sprites.add(player1)
#game loop
running = True
while running:
    #keep this runiing at the right speed
    clock.tick(fps)
    #Process imput (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        
    #Update
    gameDisplay.blit(mapa, (0, 0))
    all_sprites.update()
    
    
    #Draw / Render
    all_sprites.draw(gameDisplay)
    # *after* drawing everyting, flip the display
    pygame.display.flip()
    
        

                    #(where, color, {x, y, w, h)
    #pygame.draw.rect(gameDisplay, blue, [0, 0, 180, 40])
    #pygame.draw.rect(gameDisplay, red, [180, 0, 440, 40])
    #pygame.draw.rect(gameDisplay, blue, [620, 0, 180, 40])

    
    pygame.display.update()



pygame.quit()
quit()
