import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)

posX = 80
posY = 80
speed = 15

WIDTH = 360
HEIGHT = 480
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
    screen.fill(BLUE)
#     pygame.draw.circle(screen, GREEN,(posX,posY), 60)
    pygame.display.flip()
    
        
    
    
    
pygame.quit()

