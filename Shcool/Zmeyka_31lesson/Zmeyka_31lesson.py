import pygame
import random, time
from os import path

pygame.init()

dis_width = 800
dis_height = 600

YELLOW = (255, 255, 102)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)

FPS = 5

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

snake_block = 30
snake_step = 30

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0
length = 2

foodx = random.randrange(0, dis_width - snake_block)
foody = random.randrange(0, dis_height - snake_block)

# Музыка
music_dir = path.join(path.dirname(__file__), 'music')

pygame.mixer.music.load(path.join(music_dir, 'long.mp3'))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

am = pygame.mixer.Sound(path.join(music_dir, 'short.ogg'))
am.set_volume(0.5)

game_over = pygame.mixer.Sound(path.join(music_dir, 'game_over.ogg'))
game_over.set_volume(0.5)

# Картинка
img_dir = path.join(path.dirname(__file__), 'img')

bg = pygame.image.load(path.join(img_dir, 'fon_grass.jpg')).convert()
bg = pygame.transform.scale(bg, (dis_width, dis_height))
bg_rect = bg.get_rect()

head_images = [pygame.image.load(path.join(img_dir, 'HeadR.png')).convert(),
               pygame.image.load(path.join(img_dir, 'HeadL.png')).convert(),
               pygame.image.load(path.join(img_dir, 'HeadB.png')).convert(),
               pygame.image.load(path.join(img_dir, 'HeadT.png')).convert()]

snake_tail_img = [pygame.image.load(path.join(img_dir, 'tailright.png')).convert(),
                  pygame.image.load(path.join(img_dir, 'tailleft.png')).convert(),
                  pygame.image.load(path.join(img_dir, 'taildown.png')).convert(),
                  pygame.image.load(path.join(img_dir, 'tailup.png')).convert(),
                  ]
def draw_head(i, snake_list):
    snake_head_img_now = head_images[i]
    snake_head = pygame.transform.scale(snake_head_img_now, (snake_block, snake_block))
    snake_head.set_colorkey(BLACK)
    snake_head_rect = snake_head.get_rect(x=snake_list[-1][0], y=snake_list[-1][1])
    dis.blit(snake_head, snake_head_rect)
    
def draw_tail(i, snake_list):
    snake_tail_img_now = snake_tail_img[i]
    snake_tail = pygame.transform.scale(snake_tail_img_now, (snake_block, snake_block))
    snake_tail.set_colorkey(WHITE)
    snake_tail_rect = snake_tail.get_rect(x=snake_list[0][0], y=snake_list[0][1])
    dis.blit(snake_tail, snake_tail_rect)
 
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
    i = 0
    run = True
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    length = 1
    snake_list = []
    
    foodx = random.randrange(0, dis_width-snake_block)
    foody = random.randrange(0, dis_height-snake_block)
    
    # Отрисовка еды (убрать строку с зеленым квадратом)
    food_img = [pygame.image.load(path.join(img_dir, 'apple.png')).convert(),
                    pygame.image.load(path.join(img_dir,'strawberry.png')).convert(),
                    pygame.image.load(path.join(img_dir, 'plum.png')).convert(),
                    pygame.image.load(path.join(img_dir, 'banan.png')).convert(),
                    pygame.image.load(path.join(img_dir,'orange.png')).convert(),
                    pygame.image.load(path.join(img_dir,'cherry.png')).convert(),
                    pygame.image.load(path.join(img_dir,'grape.png')).convert()]

    food = pygame.transform.scale(random.choice(food_img), (snake_block, snake_block))
    food.set_colorkey(WHITE)
    food_rect = food.get_rect(x=foodx, y=foody)
    
    
    
    while run:
        while game_close:
            pygame.mixer.music.stop()
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
                    i = 1
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_step
                    y1_change = 0
                    i = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_step
                    i = 3
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_step
                    i = 2
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
            game_close = True
            game_over.play()
        x1 += x1_change
        y1 += y1_change
        
        
        

        
        dis.fill(BLUE)
        dis.blit(bg, bg_rect)
        dis.blit(food, food_rect)
        create_mes(f'Текущий счет: {length-1}', BLACK, 0,0,'comicsans', 25)
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]
            
        for x in snake_list[1:]:
            snake_img = pygame.image.load(path.join(img_dir, 'body3.png')).convert()
            snake = pygame.transform.scale(snake_img, (snake_block, snake_block))
            snake.set_colorkey(WHITE)
            dis.blit(snake, (x[0], x[1]))
            
        for x in snake_list[1:-1]:
            if x == snake_head:
                game_close = True
                game_over.play()
                
        
            
        draw_head(i, snake_list)
        draw_tail(i, snake_list)
        pygame.display.update()
        
        if eating_check(x1, y1, foodx, foody):
            foodx = random.randrange(0, dis_width-snake_block)
            foody = random.randrange(0, dis_height-snake_block)
            
            # Отрисовка еды (убрать строку с зеленым квадратом)
            food_img = [pygame.image.load(path.join(img_dir, 'apple.png')).convert(),
                    pygame.image.load(path.join(img_dir,'strawberry.png')).convert(),
                    pygame.image.load(path.join(img_dir, 'plum.png')).convert(),
                    pygame.image.load(path.join(img_dir, 'banan.png')).convert(),
                    pygame.image.load(path.join(img_dir,'orange.png')).convert(),
                    pygame.image.load(path.join(img_dir,'cherry.png')).convert(),
                    pygame.image.load(path.join(img_dir,'grape.png')).convert()]

            food = pygame.transform.scale(random.choice(food_img), (snake_block, snake_block))
            food.set_colorkey(WHITE)
            food_rect = food.get_rect(x=foodx, y=foody)
    
            length += 1
            am.play()

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    quit()
    
gameloop()

# import pygame
# from os import path
# import time
# import random
# pygame.init()
# 
# WIDTH=800
# HEIGHT= 800
# 
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# #создаем дисплей
# screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
# pygame.display.set_caption('Змейка на PyGame')
# #путь к сторонним файлам 
# img_dir = path.join(path.dirname(__file__), 'img')
# # music_dir = path.join(path.dirname(__file__), 'music')
# #загрузка фона
# bg = pygame.image.load(path.join(img_dir,'Fon_grass.jpg')).convert()
# bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
# bg_rect = bg.get_rect()
# #загрузка музыки
# # pygame.mixer.music.load(path.join(music_dir, 'Intense.mp3'))
# # pygame.mixer.music.play()
# # pygame.mixer.music.set_volume(0.1)
# # am = pygame.mixer.Sound(path.join(music_dir,'apple_bite.ogg'))
# # am.set_volume(0.5)
# #задаем скорость
# snake_speed = 15
# #внутриигровое время
# clock = pygame.time.Clock()
# 
# #шрифты для надписей
# font_style = pygame.font.SysFont(None, 32)
# score_font = pygame.font.SysFont("comicsansms", 25)
# #функция для вывода финальной записи
# def message(msg, color):
#     mes = font_style.render(msg, True, color)
#     screen.blit(mes, [WIDTH/16, HEIGHT/2])
# #функция подсчета очков
# def score_for_snake(score):
#     value = score_font.render("Ваш счет: " + str(score), True, RED)
#     screen.blit(value, [0, 0])
# #создание блоков для змеи
# def new_block(snake_body):
#     for x in snake_body:
#         pygame.draw.rect(screen,BLACK, [x[0], x[1], 10, 10])
# #игровая функция, в ней находиться игровой цикл
# def game():
#     #создание еды
#     foodx = round(random.randrange(0, WIDTH - 10) / 10) * 10
#     foody = round(random.randrange(0, HEIGHT - 10) / 10) * 10
#     #загрузка и размещение картинки еды
#     food_img =  [pygame.image.load(path.join(img_dir, 'f_1.png')).convert(), pygame.image.load(path.join(img_dir, 'f_2.png')).convert(),pygame.image.load(path.join(img_dir, 'f_3.png')).convert(),pygame.image.load(path.join(img_dir, 'f_4.png')).convert(),pygame.image.load(path.join(img_dir, 'f_5.png')).convert() ]
#     food = pygame.transform.scale(random.choice(food_img), (10,10))
#     food.set_colorkey(WHITE)
#     food_rect = food.get_rect(x = foodx, y = foody)
#     #координаты для змеи
#     xcor = WIDTH/2
#     ycor = HEIGHT/2
#     x = 0
#     y = 0
#     #список элементов змеи
#     snake_body = []
#     #длина змеи
#     length = 1
#     #переменные для циклов
#     run = True
#     end = False
#     #основной игровой цикл
#     while run:
#         #цикл для перезагрузки игры или выхода из игры
#         while end == True:
#             screen.fill(BLUE)
#             message("Ты проиграл! Нажми 'C' для продолжения  или 'Q'-для выхода", RED)
#             pygame.display.update()
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:                    
#                     if event.key == pygame.K_q:
#                         run = False
#                         end = False
#                     if event.key == pygame.K_c:
#                         game()
#         #обработка событий (закрытие окна, нажатие на клавиши)
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     run = False
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         x = -10
#                         y = 0
#                     elif event.key == pygame.K_RIGHT:
#                         x = 10
#                         y = 0
#                     elif event.key == pygame.K_UP:
#                         y = -10
#                         x = 0
#                     elif event.key == pygame.K_DOWN:
#                         y = 10
#                         x = 0
#         #проверка на касание границ
#         if xcor >= WIDTH or xcor < 0 or ycor >= HEIGHT or ycor < 0:
#             end = True
#         #изменение координат змеи
#         xcor += x
#         ycor += y
#         #заливка экрана и отображение всех элементов на дисплее
#         screen.fill(BLUE)
#         screen.blit(bg, bg_rect)
#         screen.blit(food, food_rect)
#         #pygame.draw.rect(screen, BLUE, (xcor, ycor, 10,10))
#         #pygame.draw.rect(screen, GREEN, (foodx, foody, 10,10))
# 
#         #заполнение списка змеи
#         snake_head = []
#         snake_head.append(xcor)
#         snake_head.append(ycor)
#         snake_body.append(snake_head)
#         if len(snake_body) > length:
#             del snake_body[0]
#             
#         for z in snake_body [:-1]:
#             if z == snake_head:
#                 end = True
#         new_block(snake_body)
#         score_for_snake(length -1)
#         pygame.display.update()
#         #съедание еды 
#         if xcor == foodx and ycor == foody:
#             foodx = round(random.randrange(0, WIDTH - 30) / 10) * 10
#             foody = round(random.randrange(0, HEIGHT - 30) / 10) * 10
#             food_img =  [pygame.image.load(path.join(img_dir, 'f_1.png')).convert(), pygame.image.load(path.join(img_dir, 'f_2.png')).convert(),pygame.image.load(path.join(img_dir, 'f_3.png')).convert(),pygame.image.load(path.join(img_dir, 'f_4.png')).convert(),pygame.image.load(path.join(img_dir, 'f_5.png')).convert() ]
#             food = pygame.transform.scale(random.choice(food_img), (10,10))
#             food.set_colorkey(WHITE)    
#             food_rect = food.get_rect(x = foodx, y = foody)
#             #меняем длину змеи (заодно и счет на дисплее измениться)
#             length += 1
#             #звуковой эффект
# #             am.play()
#         #переворот дисплея
#         pygame.display.flip()
#         #скорость отображения кадров (зависит от скорости змеи)
#         clock.tick(snake_speed)
# 
#     #message('Ты проиграл!', RED)
#     pygame.display.update()
#     time.sleep(2)
#     pygame.quit()
#     quit()
# #перезапуск игровой функции
# game()


