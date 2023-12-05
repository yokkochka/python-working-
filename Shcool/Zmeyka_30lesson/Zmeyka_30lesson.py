import pygame
import random, time
from os import path

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

music_dir = path.join(path.dirname(__file__), 'music')
main = pygame.mixer.Sound(path.join(music_dir, 'long.mp3'))
main.set_volume(0.1)

am = pygame.mixer.Sound(path.join(music_dir, 'short.ogg'))
am.set_volume(0.5)

game_over = pygame.mixer.Sound(path.join(music_dir, 'game_over.ogg'))
game_over.set_volume(0.5)

def create_mes(msg, color, x, y, font_name, size):
    font_style = pygame.font.SysFont(font_name, size)
    mes = font_style.render(msg, True, color)
    dis.blit(mes, [x,y])

def eating_check(xcor, ycor, foodx, foody):
    if foodx-snake_block <= xcor <= foodx+snake_block:
        if foody-snake_block <= ycor <=foody+snake_block:
            return True
    else:
        return False
    
def gameloop():
    main.play()
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    length = 1
    snake_list = []
    
    foodx = random.randrange(0, dis_width-snake_block)
    foody = random.randrange(0, dis_height-snake_block)
    game_close = False
    run = True
    while run:
        while game_close:
            main.stop()
            time.sleep(1.3)
            game_over.stop()
            dis.fill(RED)
            create_mes('Вы проиграли!', BLACK, 200, 200, 'chalkduster.tttf', 70)
            create_mes('Нажмите Q для выхода и С для перезапуска игры', BLACK, 25, 300, 'times', 35)
            create_mes(f'Текущий счет: {length-1}', BLACK, 0,0,'comicsans', 25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
            pygame.display.update()
            
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
            game_close = True
            game_over.play()
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(BLUE)
        create_mes(f'Текущий счет: {length-1}', BLACK, 0,0,'comicsans', 25)
        pygame.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
                game_over.play()
                
        for x in snake_list:
            pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block,snake_block])
        pygame.display.update()
        
        if eating_check(x1, y1, foodx, foody):
            foodx = random.randrange(0, dis_width-snake_block)
            foody = random.randrange(0, dis_height-snake_block)
            length += 1
            am.play()

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    quit()
    
gameloop()















