import pygame,sys, random, time
from pygame.math import Vector2
from os import path

# Класс змейки
class Snake:
    def __init__(self, fruit):
        # Список, содержащий информацию о блоках змейки
        self.snake_body=[Vector2(5,10), Vector2(4,10), Vector2(3,10)]  
        self.movement = Vector2(1,0)
        self.fruit = fruit
        self.collision = False

        self.head_up = pygame.image.load("images/blue_head_up.png").convert_alpha()
        self.head_down = pygame.image.load("images/blue_head_down.png").convert_alpha()
        self.head_left = pygame.image.load("images/blue_head_left.png").convert_alpha()
        self.head_right = pygame.image.load("images/blue_head_right.png").convert_alpha()

        self.snake_DownToLeft = pygame.image.load("images/blue_snake_DownToLeft.png").convert_alpha()
        self.snake_DownToRight = pygame.image.load("images/blue_snake_DownToRight.png").convert_alpha()
        self.snake_UpToLeft = pygame.image.load("images/blue_snake_UpToLeft.png").convert_alpha()
        self.snake_UpToRight = pygame.image.load("images/blue_snake_UpToRight.png").convert_alpha()
        
        self.snake_horizontal = pygame.image.load("images/blue_snake_horizontal.png").convert_alpha()
        self.snake_vertical = pygame.image.load("images/blue_snake_vertical.png").convert_alpha()

        self.tail_up = pygame.image.load("images/blue_tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("images/blue_tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("images/blue_tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("images/blue_tail_right.png").convert_alpha()
        
        self.bite = pygame.mixer.Sound('music/bite.ogg')
        self.music_game_over = pygame.mixer.Sound('music/game_over.ogg')

    # Функция, отрисовывающая змейку  
    def draw_snake_body(self):
        for ind, block in enumerate(self.snake_body):
            self.head_graphics()
            self.tail_graphics()


            # Проверка какой вектор направления, в зависимости от этого и отрисовываем голову
            if ind == 0:
                win.blit(self.head_variable, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))

            elif ind == len(self.snake_body)-1:
                win.blit(self.tail_variable, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))

            else:
                previos = self.snake_body[ind+1] - block
                next = self.snake_body[ind-1] - block
                if previos.x == next.x:
                    win.blit(self.snake_vertical, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))
                elif previos.y== next.y:
                    win.blit(self.snake_horizontal, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))
                else:
                    if previos.x == -1 and next.y == -1 or previos.y == -1 and next.x == -1:
                        win.blit(self.snake_UpToLeft, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))
                    elif previos.x == 1 and next.y == -1 or previos.y == -1 and next.x == 1:
                        win.blit(self.snake_UpToRight, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))
                    elif previos.x == -1 and next.y == 1 or previos.y == 1 and next.x == -1:
                        win.blit(self.snake_DownToLeft, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))
                    elif previos.x == 1 and next.y == 1 or previos.y == 1 and next.x == 1:
                        win.blit(self.snake_DownToRight, (int(block.x*SIZE), int(block.y*SIZE), SIZE,SIZE))


    def tail_graphics(self):
        vector_calculation = self.snake_body[len(self.snake_body)-2] - self.snake_body[len(self.snake_body)-1]
        # Переменная self.tale_variable будет хранить в себе выбор того, что нужно отрисовать
        if vector_calculation == Vector2(0,1): self.tail_variable = self.tail_down
        elif vector_calculation == Vector2(0,-1): self.tail_variable = self.tail_up
        elif vector_calculation == Vector2(1,0): self.tail_variable = self.tail_right
        elif vector_calculation == Vector2(-1, 0): self.tail_variable = self.tail_left

    def head_graphics(self):
        # Переменная self.head_variable будет хранить в себе выбор того, что нужно отрисовать
        if self.movement == Vector2(0,1): self.head_variable = self.head_down
        elif self.movement == Vector2(0,-1): self.head_variable = self.head_up
        elif self.movement == Vector2(1,0): self.head_variable = self.head_right
        elif self.movement == Vector2(-1, 0): self.head_variable = self.head_left



        # Проходимся по списку, по каждому блоку змейки
        #for i in self.snake_body:    
            # Отрисовываем этот блок
            #pygame.draw.rect(win,(0, 0, 255), (int(i.x*SIZE), int(i.y*SIZE), SIZE,SIZE))


    def move_snake(self):
        if self.collision == True:
             # Копируем весь список
            copy_snake = self.snake_body[:]
            # Вставляем напервое место(0) блок тела сдвинутый на вектор движения
            copy_snake.insert(0,copy_snake[0]+self.movement)
            # Теперь обновляем список snake_body чтобы 
            # в нем хранились акктуальные данные о блоках змеи
            self.snake_body = copy_snake[:]
            self.collision = False
        else:
             # Копируем весь список, кроме одного последнего элемента
            copy_snake = self.snake_body[:-1]
            # Вставляем напервое место(0) блок тела сдвинутый на вектор движения
            copy_snake.insert(0,copy_snake[0]+self.movement)
            # Теперь обновляем список snake_body чтобы 
            # в нем хранились акктуальные данные о блоках змеи
            self.snake_body = copy_snake[:]
                
       
    def collision_check(self):
        if self.fruit.pos == self.snake_body[0]:
            # Вызываем функция рандомный позиции фрукта
            self.fruit.random_position()
            self.new_block()
            self.bite.play()
        for i in self.snake_body[1:]:
            if i == fruit.pos:
                fruit.random_position()

    def new_block(self):
        self.collision = True
        fruit.index_icon_fruits = random.randint(0,3)

    # Столкновение с телом змеи или стенами
    def wall_and_body_collisions(self):
        if (not ( 0 <= self.snake_body[0].x < COUNT_CELL)) or (not ( 0 <= self.snake_body[0].y < COUNT_CELL)):
            self.game_over()
        copy = self.snake_body[1:]
        if self.snake_body[0] in copy:
            self.game_over()

    def game_over(self):
        self.music_game_over.play()
        global game_close
        game_close = True
        


# Класс фрукта
class Fruit:
    def __init__(self):
        
        # Загружаем картинку
        self.red_apple = pygame.image.load("images/fruits/red_apple.png").convert_alpha()
        # Изменяем ее размеры под размер однойнашей ячейки
        self.red_apple = pygame.transform.scale(self.red_apple, (SIZE,SIZE))
        # И говорим игнорировать белый цвет (фон) картинки
        self.red_apple.set_colorkey('white')

        self.green_apple = pygame.image.load("images/fruits/green_apple.png").convert_alpha()
        self.green_apple = pygame.transform.scale(self.green_apple, (SIZE,SIZE))
        self.green_apple.set_colorkey('white')

        self.banana = pygame.image.load("images/fruits/banana.png").convert_alpha()
        self.banana = pygame.transform.scale(self.banana, (SIZE,SIZE))
        self.banana.set_colorkey('white')

        self.orange = pygame.image.load("images/fruits/orange.png").convert_alpha()
        self.orange = pygame.transform.scale(self.orange, (SIZE,SIZE))
        self.orange.set_colorkey('white')


        self.icon_fruits = ( self.orange, self.red_apple, self.green_apple, self.banana)

        self.index_icon_fruits = 0

        self.random_position()
    
    # Функция, отрисовывающая фрукт
    def draw_fruit(self):
        # Отрисовываем фрукт
        #pygame.draw.rect(win,(166, 114, 126), (int(self.pos.x*SIZE), int(self.pos.y*SIZE), SIZE,SIZE))
        win.blit(self.icon_fruits[self.index_icon_fruits], (int(self.pos.x*SIZE), int(self.pos.y*SIZE), SIZE,SIZE))
    def random_position(self):
        # Координата отрисовки фрукта по Х
        self.x = random.randint(0,COUNT_CELL-1)    
        # Координата отрисовки фрукта по Y
        self.y = random.randint(0,COUNT_CELL-1)
        # Создаем переменную с вектором этих координат
        self.pos = Vector2(self.x, self.y)

    def draw_grass(self):
        # Проходимся по всем строкам
        for i in range(COUNT_CELL):
            # Если они под четным номером
            if i %2==0:
                # То проходимся по всем колонкам
                for j in range(COUNT_CELL):
                    # И на четных местах
                    if j % 2 == 0:
                        # Распологаем квадратик более темного цвета
                        pygame.draw.rect(win,GRASS_COLOR, (int(j*SIZE), int(i*SIZE), SIZE,SIZE))
            # Если не под четным
            else:
                # Так же проходимся по колонкам
                for j in range(COUNT_CELL):
                    # И на нечетных позициях
                    if j % 2 != 0:
                        # Распологаем квадратики потемнее
                        pygame.draw.rect(win,GRASS_COLOR, (int(j*SIZE), int(i*SIZE), SIZE,SIZE))
    def create_score(self):
        # Определяем шрифт
        font_style = pygame.font.SysFont('chalkduster.tttf',50)
        # Создаем "сообщение", которое будем отображать 
        mes = font_style.render('Счет: '+ str(len(snake.snake_body)-3) , True, (0,0,0))
        # Отображаем
        win.blit(mes, [10, 10])




# Если музыка идет с задержкой, то можно прописать эту строчку
# pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

SIZE = 40   # Задаем размер ячейки
COUNT_CELL = 20   # Задаем количество ячеек в строке

BGCOLOR = (175,215,70)
GRASS_COLOR = (167,209,61)
win = pygame.display.set_mode((SIZE*COUNT_CELL, SIZE*COUNT_CELL))   # Размер окна зависит от кол-ва ячеек 

FPS= 60
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake(fruit)

# Создаем событие
SCREEN_UPDATE= pygame.USEREVENT
# Создаем таймер, который будет запускать событие раз в 250 миллисекунд
pygame.time.set_timer(SCREEN_UPDATE,100)

# Фоновая музыка
music_dir = path.join(path.dirname(__file__), 'music')
pygame.mixer.music.load(path.join(music_dir, 'background_song.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

game_close = False

def main():
    global snake, fruit
    fruit = Fruit()
    snake = Snake(fruit)

    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    while True:
        ### Для перезапуска
        global game_close
        while game_close:
                pygame.mixer.music.stop()
                time.sleep(0.6)
                snake.music_game_over.stop()
                
                font_style = pygame.font.SysFont('chalkduster.tttf',50)
                mes = font_style.render('Вы проиграли!', True, (0,0,0))
                win.blit(mes, [270, 200])

                font_style = pygame.font.SysFont('chalkduster.tttf',50)
                mes = font_style.render('Нажмите "R" для перезапуска игры', True, (0,0,0))
                win.blit(mes, [100, 300])

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_e):
                        game_close = False
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            game_close = False
                            main()
                pygame.display.update()
        ###

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_e):
                pygame.quit()
                sys.exit()
            # Событие, работающее по таймеру запускает функцию движения змейки
            if event.type ==SCREEN_UPDATE:
                snake.move_snake()
                snake.collision_check()
                snake.wall_and_body_collisions()
            # Если происходит нажатие на клавиатуре
            if event.type == pygame.KEYDOWN:
                # Если нажата была кнопка вверх
                if event.key == pygame.K_UP:
                    # Мы задаем вертор, который при сложении даст смещение вверх
                    
                    if snake.movement != Vector2(0, 1):
                        snake.movement = Vector2(0,-1)
                if event.key == pygame.K_DOWN:
                    if snake.movement != Vector2(0, -1):
                        snake.movement = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if snake.movement != Vector2(1, 0):
                        snake.movement = Vector2(-1,0)
                if event.key == pygame.K_RIGHT:
                    if snake.movement != Vector2(-1, 0):
                        snake.movement = Vector2(1,0)


        win.fill(pygame.Color(BGCOLOR))
        fruit.draw_grass()
        fruit.create_score()
        fruit.draw_fruit()
        snake.draw_snake_body()
        
        # Бесконечно обновляем и отображаем окно, чтобы оно не закрывалось
        pygame.display.update() 
        clock.tick(FPS)


if __name__ == "__main__": 
    main()