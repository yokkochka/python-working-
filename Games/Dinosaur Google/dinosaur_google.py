import pygame
from sys import exit
pygame.init()

WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dinosaur Google')

FPS = 60
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(FPS)

