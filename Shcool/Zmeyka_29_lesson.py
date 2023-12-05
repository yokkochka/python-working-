# Шаблон

# import pygame
# WIDTH = 360
# HEIGHT = 480
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# FPS = 30
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("My Game")
# run = True
# clock = pygame.time.Clock()
# while run:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     screen.fill(BLUE)
#     pygame.display.flip()
# pygame.quit()

import pygame
import random

dis_width = 800
dis_height = 600

YELLOW = (255, 255, 102)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)

FPS = 5

pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

snake_block = 30
snake_step = 30

snake_list = []


x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0
length = 1

foodx = random.randrange(0, dis_width - snake_block)
foody = random.randrange(0, dis_height - snake_block)

def eating_check(xcor, ycor, foodx, foody):
    if foodx-snake_block <= xcor <= foodx+snake_block:
        if foody-snake_block <= ycor <=foody+snake_block:
            return True
    else:
        return False
    


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_step
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_step
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_step
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_step
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
        run = False
    x1 += x1_change
    y1 += y1_change
    
    dis.fill(BLUE)
    pygame.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])
    
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > length:
        del snake_list[0]
    for x in snake_list[:-1]:
        if x == snake_head:
            run = False
            
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block,snake_block])
    pygame.display.update()
    
    if eating_check(x1, y1, foodx, foody):
        foodx = random.randrange(0, dis_width-snake_block)
        foody = random.randrange(0, dis_height-snake_block)
        length += 1

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
quit()














