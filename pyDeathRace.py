import os
import pygame
import ctypes
import math

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
img_folder = os.path.join(game_folder, "imfg")

class Meta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "meta.jpg")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = (displayW / 2)
        self.rect.y = 0

class Player1(pygame.sprite.Sprite):
    # sprite for player 1
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "playerA.png")).convert()

        start = (displayW / 2 + displayW/ 10, 40)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = start
        self.xSpeed = 0
        self.ySpeed = 0
        self.angle = 0

    def update(self):
        start = (displayW / 2 + displayW/ 10, 40)
        maxspeed = 5
        deltaS = 0.25
        keystate = pygame.key.get_pressed()
        if self.rect.bottom > displayH or self.rect.top < 0 or self.rect.left < 0 or self.rect.right > displayW:
            self.rect.center = start
            self.xSpeed = 0
            self.ySpeed = 0

        elif keystate[pygame.K_UP]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.xSpeed) >= maxspeed:
                    if self.xSpeed > 0:               
                        self.xSpeed -= deltaS         
                        self.ySpeed -= deltaS            #delta Velocidad 
                    else:                                #px/fps
                        self.xSpeed += deltaS            #      ^
                        self.ySpeed -= deltaS            #  8 - |          | 
                elif abs(self.ySpeed)>= maxspeed:        #  7 - |\         |
                    if self.ySpeed > 0:                  #  6 - | \        |
                        self.ySpeed -= deltaS            #  5 - |\ \       /
                    else: self.ySpeed = (maxspeed) * -1  #  4 - | \ \     /|
                else:                                    #  3 - |  \ \   / |
                    self.ySpeed -= deltaS                #  2 - |   \ \ /  |
                    if self.xSpeed > 0:                  #  1 - |    \ X   |
                        self.xSpeed -= deltaS            #  0 - |---- X-\--| 
                    elif self.xSpeed < 0:                # -1 - |    / \ \ |
                        self.xSpeed += deltaS            # -2 - |   /   \ \|
                    else:                                # -3 - |  /     \ |
                        self.xSpeed = 0                  # -4 - | /       \|
            else:                                        # -5 - |/.........\......>  tiempo*
                self.ySpeed -= deltaS                    # abajo si xSpeed es equidistante.
                                                         # arriba si no lo es.
        elif keystate[pygame.K_DOWN]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.xSpeed) >= maxspeed:
                    if self.xSpeed > 0:                
                        self.xSpeed -= deltaS         
                        self.ySpeed += deltaS         
                    else:                             
                        self.xSpeed += deltaS         
                        self.ySpeed += deltaS         
                elif abs(self.ySpeed)>= maxspeed:        
                    if self.ySpeed < 0:
                        self.ySpeed += deltaS
                    else:
                        self.ySpeed = maxspeed
                else:                                       
                    self.ySpeed += deltaS                   
                    if self.xSpeed > 0:                     
                        self.xSpeed -= deltaS               
                    elif self.xSpeed < 0:                 
                        self.xSpeed += deltaS                
                    else:                                                
                        self.xSpeed = 0                             
            else:                                             
                self.ySpeed += deltaS
            
        elif keystate[pygame.K_LEFT]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.ySpeed) >= maxspeed:
                    if self.ySpeed > 0:               
                        self.ySpeed -= deltaS         
                        self.xSpeed -= deltaS        
                    else:                           
                        self.ySpeed += deltaS         
                        self.xSpeed -= deltaS         
                elif abs(self.xSpeed)>= maxspeed:    
                    if self.xSpeed > 0:              
                        self.xSpeed -= deltaS      
                    else:
                        self.xSpeed = (maxspeed) * -1
                        self.ySpeed = 0
                else:                               
                    self.xSpeed -= deltaS            
                    if self.ySpeed > 0:             
                        self.ySpeed -= deltaS       
                    elif self.ySpeed < 0:            
                        self.ySpeed += deltaS       
                    else:                          
                        self.ySpeed = 0               
            else:                                     
                self.xSpeed -= deltaS
                
        elif keystate[pygame.K_RIGHT]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.ySpeed) >= maxspeed:
                    if self.ySpeed > 0:                
                        self.ySpeed -= deltaS         
                        self.xSpeed += deltaS         
                    else:                             
                        self.ySpeed += deltaS         
                        self.xSpeed += deltaS         
                elif abs(self.xSpeed)>= maxspeed:        
                    if self.xSpeed < 0:
                        self.xSpeed += deltaS
                    else:
                        self.xSpeed = maxspeed
                        self.ySpeed = 0
                else:                                       
                    self.xSpeed += deltaS                   
                    if self.ySpeed > 0:                     
                        self.ySpeed -= deltaS               
                    elif self.ySpeed < 0:                 
                        self.ySpeed += deltaS                
                    else:                                                
                        self.ySpeed = 0                             
            else:                                             
                self.xSpeed += deltaS
        else:
            if self.xSpeed > 0:
                self.xSpeed -= deltaS
                if self.ySpeed > 0:
                    self.ySpeed -= deltaS
                elif self.ySpeed < 0:
                    self.ySpeed += deltaS
                else: self.ySpeed = 0
            elif self.xSpeed < 0:
                self.xSpeed += deltaS
                if self.ySpeed > 0:
                    self.ySpeed -= deltaS
                elif self.ySpeed < 0:
                    self.ySpeed += deltaS
                else: self.ySpeed = 0
            else:
                self.xSpeed = 0
                if self.ySpeed > 0:
                    self.ySpeed -= deltaS
                elif self.ySpeed < 0:
                    self.ySpeed += deltaS
                else: self.ySpeed = 0
                
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed
        self.angulo()
        
    def angulo(self):
        
        if self.ySpeed == 0 or self.xSpeed == 0:
            if self.ySpeed == 0:
                angle = 0
            else:
                if self.xSpeed > 0:
                    angle = -90
                else:
                    angle = 90
        else:
            angle = math.degrees(math.atan(self.ySpeed / self.xSpeed))
            self.image = pygame.transform.rotate(self.image, angle)

class Player2(pygame.sprite.Sprite):
    # sprite for player 2
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "playerC.png")).convert()

        start = (displayW / 2 + displayW/ 10, 85)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = start
        self.xSpeed = 0
        self.ySpeed = 0

    def update(self):
        start = (displayW / 2 + displayW/ 10, 85)
        
        maxspeed = 5
        deltaS = 0.25
        keystate = pygame.key.get_pressed()
        if self.rect.bottom > displayH or self.rect.top < 0 or self.rect.left < 0 or self.rect.right > displayW:
            self.rect.center = start
            self.xSpeed = 0
            self.ySpeed = 0
        elif keystate[pygame.K_w]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.xSpeed) >= maxspeed:
                    if self.xSpeed > 0:               
                        self.xSpeed -= deltaS         
                        self.ySpeed -= deltaS            #delta Velocidad 
                    else:                                #px/fps
                        self.xSpeed += deltaS            #      ^
                        self.ySpeed -= deltaS            #  8 - |          | 
                elif abs(self.ySpeed)>= maxspeed:        #  7 - |\         |
                    if self.ySpeed > 0:                  #  6 - | \        |
                        self.ySpeed -= deltaS            #  5 - |\ \       /
                    else: self.ySpeed = (maxspeed) * -1  #  4 - | \ \     /|
                else:                                    #  3 - |  \ \   / |
                    self.ySpeed -= deltaS                #  2 - |   \ \ /  |
                    if self.xSpeed > 0:                  #  1 - |    \ X   |
                        self.xSpeed -= deltaS            #  0 - |---- X-\--| 
                    elif self.xSpeed < 0:                # -1 - |    / \ \ |
                        self.xSpeed += deltaS            # -2 - |   /   \ \|
                    else:                                # -3 - |  /     \ |
                        self.xSpeed = 0                  # -4 - | /       \|
            else:                                        # -5 - |/.........\......>  tiempo*
                self.ySpeed -= deltaS                    # abajo si xSpeed es equidistante.
                                                         # arriba si no lo es.
        elif keystate[pygame.K_s]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.xSpeed) >= maxspeed:
                    if self.xSpeed > 0:                
                        self.xSpeed -= deltaS         
                        self.ySpeed += deltaS         
                    else:                             
                        self.xSpeed += deltaS         
                        self.ySpeed += deltaS         
                elif abs(self.ySpeed)>= maxspeed:        
                    if self.ySpeed < 0:
                        self.ySpeed += deltaS
                    else:
                        self.ySpeed = maxspeed
                else:                                       
                    self.ySpeed += deltaS                   
                    if self.xSpeed > 0:                     
                        self.xSpeed -= deltaS               
                    elif self.xSpeed < 0:                 
                        self.xSpeed += deltaS                
                    else:                                                
                        self.xSpeed = 0                             
            else:                                             
                self.ySpeed += deltaS
            
        elif keystate[pygame.K_a]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                if abs(self.ySpeed) >= maxspeed:
                    if self.ySpeed > 0:               
                        self.ySpeed -= deltaS         
                        self.xSpeed -= deltaS        
                    else:                           
                        self.ySpeed += deltaS         
                        self.xSpeed -= deltaS         
                elif abs(self.xSpeed)>= maxspeed:    
                    if self.xSpeed > 0:              
                        self.xSpeed -= deltaS      
                    else:
                        self.xSpeed = (maxspeed) * -1
                        self.ySpeed = 0
                else:                               
                    self.xSpeed -= deltaS            
                    if self.ySpeed > 0:             
                        self.ySpeed -= deltaS       
                    elif self.ySpeed < 0:            
                        self.ySpeed += deltaS       
                    else:                          
                        self.ySpeed = 0               
            else:                                     
                self.xSpeed -= deltaS
                
        elif keystate[pygame.K_d]:
            if abs(self.xSpeed) + abs(self.ySpeed) >= maxspeed:
                
                if abs(self.ySpeed) >= maxspeed:
                    if self.ySpeed > 0:                
                        self.ySpeed -= deltaS         
                        self.xSpeed += deltaS         
                    else:                             
                        self.ySpeed += deltaS         
                        self.xSpeed += deltaS         
                elif abs(self.xSpeed)>= maxspeed:        
                    if self.xSpeed < 0:
                        self.xSpeed += deltaS
                    else:
                        self.xSpeed = maxspeed
                        self.ySpeed = 0
                else:                                       
                    self.xSpeed += deltaS                   
                    if self.ySpeed > 0:                     
                        self.ySpeed -= deltaS               
                    elif self.ySpeed < 0:                 
                        self.ySpeed += deltaS                
                    else:                                                
                        self.ySpeed = 0                             
            else:                                             
                self.xSpeed += deltaS
        else:
            if self.xSpeed > 0:
                self.xSpeed -= deltaS
                if self.ySpeed > 0:
                    self.ySpeed -= deltaS
                elif self.ySpeed < 0:
                    self.ySpeed += deltaS
                else: self.ySpeed = 0
            elif self.xSpeed < 0:
                self.xSpeed += deltaS
                if self.ySpeed > 0:
                    self.ySpeed -= deltaS
                elif self.ySpeed < 0:
                    self.ySpeed += deltaS
                else: self.ySpeed = 0
            else:
                self.xSpeed = 0
                if self.ySpeed > 0:
                    self.ySpeed -= deltaS
                elif self.ySpeed < 0:
                    self.ySpeed += deltaS
                else: self.ySpeed = 0
             
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

class Dummy1(pygame.sprite.Sprite):
    # sprite for dummy 1
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "playerG.png")).convert()

        start = ((displayW / 2 + displayW/ 10) + 70, 40)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = start
        self.xSpeed = 0
        self.ySpeed = 0

    def update(self):
        start = ((displayW / 2 + displayW/ 10) + 70, 40)
        maxspeed = 12
        deltaS = 1.7
        if self.rect.bottom > displayH or self.rect.top < 0 or self.rect.left < 0 or self.rect.right > displayW:
            self.rect.center = start
            self.xSpeed = 0
            self.ySpeed = 0 
            
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

class Dummy2(pygame.sprite.Sprite):
    # sprite for dummy 1
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "playerM.png")).convert()

        start = ((displayW / 2 + displayW/ 10) + 70, 85)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = start
        self.xSpeed = 0
        self.ySpeed = 0

    def update(self):
        start = ((displayW / 2 + displayW/ 10) + 70, 85)
        maxspeed = 12
        deltaS = 1.7
        if self.rect.bottom > displayH or self.rect.top < 0 or self.rect.left < 0 or self.rect.right > displayW:
            self.rect.center = start
            self.xSpeed = 0
            self.ySpeed = 0 
            
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

meta = Meta()
player1 = Player1()
player2 = Player2()
dummy1 = Dummy1()
dummy2 = Dummy2()

all_sprites.add(meta)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(dummy1)
all_sprites.add(dummy2)

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
