# import pygame
# import random
# 
# 
# WIDTH = 300
# HEIGHT = 300
# 
# FPS = 30
# 
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREEN = (0,255,0)
# 
# posX = 80
# posY = 80
# speed = 15
# 
# 
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Крестики-нолики')
# clock = pygame.time.Clock()
# 
# field = [['','',''],
#          ['','',''],
#          ['','','']]
# 
# run = True
# game_over = False
# 
# def draw_grid():
#     pygame.draw.line(screen, BLACK, (100,0),(100,300), 3)
#     pygame.draw.line(screen, BLACK, (200,0),(200,300), 3)
#     pygame.draw.line(screen, BLACK, (0,100),(300,100), 3)
#     pygame.draw.line(screen, BLACK, (0,200),(300,200), 3)
# 
# def draw_tic_tac_toe():
#      for i in range(3):
#          for j in range(3):
#              if field[i][j] == '0':
#                  pygame.draw.circle(screen, BLACK, (j*100+50, i*100+50), 45, 3)
#              elif field[i][j] == 'x':
#                  pygame.draw.line(screen, BLACK,(j*100+5, i*100+5), (j*100+95, i*100+95), 3)
#                  pygame.draw.line(screen, BLACK,(j*100+95, i*100+5), (j*100+5, i*100+95), 3)
# 
# def get_win_check(symbol):
#     flag_win = False
#     global win
# 
#     for line in field:
#         if line.count(symbol) == 3:
#             flag_win = True
#             win = [[0, field.index(line)], [1, field.index(line)], [2, field.index(line)]]
#     for i in range(3):
#         if field[0][i] == field[1][i] == field[2][i] == symbol:
#             flag_win = True
#             win = [[i,0],[i,1],[i,2]]
#     if field[0][0] == field[1][1] == field[2][2] == symbol:
#             flag_win = True
#             win = [[0,0],[1,1],[2,2]]
#     if field[0][2] == field[1][1] == field[2][0] == symbol:
#             flag_win = True
#             win = [[0,2],[1,1],[2,0]]
#     return flag_win
# 
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             
#         if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             pos = pygame.mouse.get_pos()
#             if field[pos[1]//100][pos[0]//100]=='':
#                 field[pos[1]//100][pos[0]//100]= 'x'
#                 x, y, = random.randint(0,2), random.randint(0,2)
#                 while field[x][y] != '':
#                     x,y = random.randint(0,2), random.randint(0,2)
#                 field[x][y] = '0'
# 
#             player_win = get_win_check('x')
#             ai_win = get_win_check('0')
#             rezult = field[0].count('x') + field[0].count('0') + field[1].count('x') + field[1].count('0')+field[2].count('x') + field[2].count('0')
#             
#             if player_win or ai_win:
#                 if player_win:
#                     game_over = True
#                     pygame.display.set_caption('Вы победили')
#                 else:
#                     pygame.display.set_caption('Победил компьютер')
#             elif rezult == 8:
#                 pygame.display.set_caption('Ничья')
#                 
#                
#     screen.fill(WHITE)
# 
#     if game_over:
#         pygame.draw.rect(screen,GREEN,(win[0][0]*100,win[0][1]*100, 100, 100))
#         pygame.draw.rect(screen,GREEN,(win[1][0]*100,win[1][1]*100, 100, 100))
#         pygame.draw.rect(screen,GREEN,(win[2][0]*100,win[2][1]*100, 100, 100))
# 
#     draw_tic_tac_toe()
#     draw_grid()
#     
#     pygame.display.flip()
#     
# pygame.quit()




# 
# ШАБЛОН
# import pygame
# 
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREEN = (0,255,0)
# 
# posX = 80
# posY = 80
# speed = 15
# 
# WIDTH = 360
# HEIGHT = 480
# FPS = 30
# 
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 
# pygame.display.set_caption('My Game')
# 
# clock = pygame.time.Clock()
# 
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#                 
#     screen.fill(BLUE)
# #     pygame.draw.circle(screen, GREEN,(posX,posY), 60)
#     pygame.display.flip()
# pygame.quit()



import pygame
import random

# игровые переменные
WIDTH = 300
HEIGHT = 300

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создание игрового окна из шаблона
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
clock = pygame.time.Clock()

# список значений в клетках построчно
field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]
# переменная цикла
run = True
# переменная проверки завершения игры
game_over = False


# отрисовка сетки
def draw_grid():
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 3)


# отрисовка крестов и нулей
def draw_tic_tac_toe():
    for i in range(3):
        for j in range(3):
            if field[i][j] == "0":
                pygame.draw.circle(screen, BLACK, (j * 100 + 50, i * 100 + 50), 45, 3)
                
            elif field[i][j] == "x":
                pygame.draw.line(screen, (0, 0, 0), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(screen, (0, 0, 0), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)



# вычисление результата игры
def get_win_check(symbol):  # передаём список и символ участника
    flag_win = False
    global win
    # перебираем подсписки
    for line in field:
        if line.count(symbol) == 3:  # если в подсписке все 3 символа совпадают=горизонтальный ряд
            flag_win = True
            win = [[0, field.index(line)], [1, field.index(line)], [2, field.index(line)]]
    # собрана вертикальный ряд
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == symbol:
            flag_win = True
            win = [[i, 0], [i, 1], [i, 2]]
            print(win)
    # проверка на диагональные линии
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
        print(win)
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]
        print(win)
    return flag_win


while run:
    clock.tick(FPS)  # переключение кадров
    # цикл проверки всех событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # проверка нажатия на "закрыть"
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # проверка клика мышки на поле
            pos = pygame.mouse.get_pos()  # координаты мышки
            if field[pos[1] // 100][pos[0] // 100] == "":  # на какое поле нажали
                field[pos[1] // 100][pos[0] // 100] = "x"  # присваивание значения нажатия(всегда играем за крестик)
                x, y = random.randint(0, 2), random.randint(0, 2)  # первая генерация клетки
                while field[x][y] != "":  # пока эта клетка не пуста
                    x, y = random.randint(0, 2), random.randint(0, 2)  # генерируем другую
                field[x][y] = "0"  # присваиваем значение клетке, если её выбрал бо

            player_win = get_win_check("x")  # проверка на выигрыш игрока
            ai_win = get_win_check("0")  # проверка на выигрыш бота
            rezult = field[0].count("x") + field[0].count("0") + field[1].count("x") + field[1].count("0") + field[2].count("x") + field[2].count("0")
            if player_win or ai_win:  # проверяем выиграл ли кто-нибудь
                game_over = True  # останавливаем проверку кликов мышкой
                if player_win:
                    pygame.display.set_caption("Вы победили")
                else:
                    pygame.display.set_caption("Компьютер победил")
            # cкладываем количество крестов и нулей в каждой строке списка(4 хода игрок+4 хода бот = 8)
            elif rezult == 8:
                game_over = True
                pygame.display.set_caption("Ничья")
    # отрисовка всех элементов
    screen.fill(WHITE)
    if game_over:
        pygame.draw.rect(screen, GREEN, (win[0][0] * 100, win[0][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[2][0] * 100, win[2][1] * 100, 100, 100))
        font_style = pygame.font.SysFont(None, 50)
        mes = font_style.render('Закройте окно', True, BLACK)
        screen.blit(mes,[30, 145])
    draw_tic_tac_toe()
    draw_grid()
    pygame.display.flip()
pygame.quit()
        
