import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Беги Форест')

skysurface = pygame.image.load('graphics/sky.jpg').convert()
groundsurface = pygame.image.load('graphics/ground.png').convert()
font = pygame.font.Font(None, 50)
textsurface = font.render('Score 0', False, "Black")
text_rectangle = textsurface.get_rect(center=(650, 50))
snailsurface = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rectangle = snailsurface.get_rect(midbottom=(600, 300))
mysurface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
my_rectangle = mysurface.get_rect(midbottom=(80, 300))

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(skysurface, (0, 0))
    screen.blit(groundsurface, (0, 300))
    screen.blit(textsurface, (650, 50))


    snail_rectangle.x -= 1
    if snail_rectangle.left <= 0:
        snail_rectangle.right = 800
    screen.blit(snailsurface, snail_rectangle)


    screen.blit(mysurface, (my_rectangle))


    if my_rectangle.colliderect(snail_rectangle):
        print('Упс!')


    pygame.display.update()


    clock.tick(60) 
