import pygame
import sys
import random


pygame.init()

screen = pygame.display.set_mode((350, 600)) 
clock = pygame.time.Clock()

class Apple:
    def __init__(self , image , position , spped):
        self.image = apple_image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = spped
    def move(self):
        self.rect.y += self.speed
        
        
# variables
speed = 3
Score = 0        
        
TILESIZE = 32 

# floor
floor_image  = pygame.image.load("src/assets/floor.png").convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE *15, TILESIZE * 5))
floor_rect = floor_image.get_rect(bottomleft = (0, screen.get_height()))
# player
palyer_image = pygame.image.load("src/assets/player_static.png").convert_alpha()
palyer_image = pygame.transform.scale(palyer_image, (TILESIZE , TILESIZE * 2))
palyer_rect = palyer_image.get_rect(center = (screen.get_width() / 2, 
                                             screen.get_height() - floor_image.get_height() - (palyer_image.get_height() / 2)))


# apple
apple_image = pygame.image.load("src/assets/apple.png").convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TILESIZE , TILESIZE ))

apples = [
    Apple(apple_image, (100, 0), 3),
    Apple(apple_image, (300, 0), 3),
    Apple(apple_image, (300, 0), 3),
]

# font
font = pygame.font.Font('src/assets/PixeloidMono.ttf', TILESIZE//2)

# sound
pickup = pygame.mixer.Sound("src/assets/powerup.mp3")
pickup.set_volume(0.1)
def update():
    global speed
    global Score
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        palyer_rect.x += 8
    elif keys[pygame.K_LEFT]:
        palyer_rect.x -= 8
    
    for apple in apples:
        apple.move()
        if apple.rect.top >= floor_rect.top:
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), speed))
            continue

        if palyer_rect.colliderect(apple.rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), speed))
            pickup.play()
            speed += 0.05
            Score += 1
            break
        
def draw():
    screen.fill("lightblue")    
    screen.blit(floor_image, floor_rect)
    screen.blit(palyer_image, palyer_rect)
 
    for apple in apples:
        screen.blit(apple.image, apple.rect)
        apple.rect.y += apple.speed
    
    score_text = font.render(f'Score: {int(Score)}', True, 'white')   
    score_speed = font.render(f'Speed: {int(speed)}', True, 'white')   
    screen.blit(score_text, (5, 5)) 
    screen.blit(score_speed, (5, 30)) 
       
 
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    update()
    draw()        
    clock.tick(60)        
    pygame.display.update()
