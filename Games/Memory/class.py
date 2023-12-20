import random as rnd
import pygame, sys   
from pygame.locals import *
from os import path
import os


class Game:
    def __init__(self):
        self.WIN_WIDTH = 640 
        self.WIN_HEIGHT = 480

        self.FPS = 30   # Переменная для фпс

        # Цвета
        self.LIGHTBLUE = (151, 157, 226)
        self.YELLOW = (218, 230, 112)
        self.SKINCOLOR = (218, 177, 124)
        self.PURPLE = (193, 131, 195)
        self.MINT = (141, 200, 191)
        self.GRAY = (119, 136, 153)
        self.DARKBLUE = (30, 75, 107)
        self.ROSE = (255, 228, 225)
        self.CORAL = (214, 107, 107)
        self.GREEN = (25, 210, 37)

        self.LVL = 1
        self.STEP = 4
        self.SCORE = 0
        self.WIN = 0
        self.CLOCK = 0

        # Цвет фона
        self.BGCOLOR = self.DARKBLUE

        self.SPEED_CARDS = 8     # Скорость открытия/закрытия карточек
        self.BOX_SIZE = 40      # Размер одной карточки в пикселях
        self.INDENTS = 10    # Отступы между карточками

        self.COUNTS_CARDS_X = 2  # Количество карточек по горизонтали
        self.COUNTS_CARDS_Y = 2    # Количество карточек по вертикали

        self.BOX_COLOR = self.ROSE   # Цвет для коробочек
        
        # Формы иконок
        self.DISK = 'disk'
        self.SQUARE = 'square'
        self.SQUARE_WITH_CIRCLE = 'circle'
        self.TRIANGLE = 'triangle'
        self.HEART = 'heart'
        
        # Настройки для кнопок      
        self.button_width = 100
        self.button_height = 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)

        # Настройки для окна ввода
        self.input_box = pygame.Rect(self.WIN_WIDTH // 2.75, 250, 200, 40)
        self.input_color_inactive = pygame.Color('lightskyblue3')
        self.input_color_active = pygame.Color('dodgerblue2')
        self.input_text = ''
        self.input_active = False

        # Настройки шрифтов
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 36)
        self.button_font = pygame.font.SysFont(None, 30)
        self.input_font = pygame.font.SysFont(None, 40)

        # Список цветов
        self.COLORS = (self.LIGHTBLUE, self.YELLOW, self.SKINCOLOR, self.PURPLE, self.MINT, self.CORAL, self.GREEN)
        # Список форм иконок
        self.SHAPES = (self.DISK, self.SQUARE, self.SQUARE_WITH_CIRCLE, self.TRIANGLE, self.HEART)

        # Проверка на четное количество карточек
        assert(self.COUNTS_CARDS_X*self.COUNTS_CARDS_Y) % 2 == 0, 'Error'   
        # Высчитываем по Х где рисовать доску, чтобы она была посередине
        self.X_INDENTS = int((self.WIN_WIDTH - (self.COUNTS_CARDS_X * (self.BOX_SIZE + self.INDENTS)))/2)    
        # Высчитываем по Y где рисовать доску, чтобы она была посередине
        self.Y_INDENTS = int((self.WIN_HEIGHT - (self.COUNTS_CARDS_Y * (self.BOX_SIZE + self.INDENTS))) / 2)     

        # Проверка чтобы кол-во карточек на доске не привышало кол-во возможных комбинаций цвет-форма иконок
        assert len(self.COLORS) * len(self.SHAPES) * 2 >= self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y, "Error"

        self.main()


    def main(self):
        pygame.init()
        
        # Музыка
        dir = path.join(path.dirname(__file__), 'music_dir')
        pygame.mixer.music.load(path.join(dir, 'music.mp3'))
        # Параметр -1 для зацикливания фоновой фузыки
        pygame.mixer.music.play(-1)
        # Решулируем громкость фоновой музыки
        pygame.mixer.music.set_volume(0)

        self.WIN = pygame.display.set_mode((self.WIN_WIDTH,self.WIN_HEIGHT))  
        pygame.display.set_caption('Memory')
        self.CLOCK = pygame.time.Clock() 
        
        pos_mouse_x = 0
        pos_mouse_y = 0

        click_on_the_first_card = None

        # Запуск начальных функций
        board = self.random_board() 
        open_boxes = self.generate_open_boxes(False)

        self.WIN.fill(self.BGCOLOR) 

        # Надпись об уровне
        self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)
        self.create_mes(f'Шагов осталось: {self.STEP}', self.ROSE,230,0,'comicsans', 25)
        self.create_mes(f'Счет: {self.SCORE}', self.ROSE,540,0,'comicsans', 25)
            
        self.opening_cards_at_the_beginning(board)

        while True:    
            mouse_clicked = False
            self.WIN.fill(self.BGCOLOR) 
            # Вызываем функцию отрисовки доски
            self.draw_board(board, open_boxes)

            interrupt_button_rect = pygame.Rect(self.WIN_WIDTH // 2 - self.button_width // 2, 400, self.button_width, self.button_height)
            pygame.draw.rect(self.WIN, self.button_color, interrupt_button_rect)
            
            interrupt_text = self.button_font.render("Прервать", True, self.button_text_color)
            interrupt_text_rect = interrupt_text.get_rect(center=interrupt_button_rect.center)
            self.WIN.blit(interrupt_text, interrupt_text_rect)

            self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)
            self.create_mes(f'Шагов осталось: {self.STEP}', self.ROSE,220,0,'comicsans', 25)
            self.create_mes(f'Счет: {self.SCORE}', self.ROSE,540,0,'comicsans', 25)

            # Цикл обработки событий
            for event in pygame.event.get():
                # Теперь при нажатии на esc будет происходить закрытие окна
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEMOTION:
                    pos_mouse_x, pos_mouse_y = event.pos

                elif event.type == MOUSEBUTTONUP:
                    pos_mouse_x, pos_mouse_y = event.pos
                    mouse_clicked = True

                elif event.type == MOUSEBUTTONDOWN:
                    if interrupt_button_rect.collidepoint(event.pos):
                        self.STEP = 0


            if self.STEP == 0:
                self.display_leaderboard()


            card_pos_mouse_x, card_pos_mouse_y = self.card_definition(pos_mouse_x, pos_mouse_y)
            
            # Если установлены координаты карточки, на которую указывает курсор
            if card_pos_mouse_x != None and card_pos_mouse_y != None:

                # Если эта карта закрыта
                if not open_boxes[card_pos_mouse_x][card_pos_mouse_y]:
                    self.selection_highlighting(card_pos_mouse_x, card_pos_mouse_y)

                # Если эта корта закрыта и мы по ней кликнули
                if not open_boxes[card_pos_mouse_x][card_pos_mouse_y] and mouse_clicked:
                    self.opening_cards([(card_pos_mouse_x, card_pos_mouse_y)], board)
                    open_boxes[card_pos_mouse_x][card_pos_mouse_y] = True

                    # Если переменная = None, то эта первая карточка, на которую мы кликнули
                    if click_on_the_first_card == None:
                        click_on_the_first_card = (card_pos_mouse_x, card_pos_mouse_y)

                    # Если в ней не None, то это вторая кликнутая карточка и мы можем сравнить иконки в них
                    else:
                        card_color_1, card_shape_1 = self.shape_and_color(board, click_on_the_first_card[0], click_on_the_first_card[1])
                        card_color_2, card_shape_2 = self.shape_and_color(board, card_pos_mouse_x, card_pos_mouse_y)

                        # Если значения не совпадают
                        if card_shape_1 == card_shape_2 and card_color_1 == card_color_2:
                            self.SCORE += 1

                        if card_shape_1 != card_shape_2 or card_color_1 != card_color_2:
                            self.STEP -= 1

                            pygame.time.wait(1000)
                            self.closing_cards([(click_on_the_first_card[0],click_on_the_first_card[1]),(card_pos_mouse_x,card_pos_mouse_y)],board) 
                            open_boxes[click_on_the_first_card[0]][click_on_the_first_card[1]] = False
                            open_boxes[card_pos_mouse_x][card_pos_mouse_y] = False

                        # Проверяем на победу
                        elif self.victory(open_boxes):
                            self.victory_animation(board, open_boxes)
                            pygame.time.wait(1000)
                            self.LVL +=1
                            
                            if self.LVL <= 4:
                                self.COUNTS_CARDS_X += 2
                                self.COUNTS_CARDS_Y += 2
                                self.STEP = self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y
                                # Повторяем проверку что у у нас четное кол-во карт
                                assert(self.COUNTS_CARDS_X*self.COUNTS_CARDS_Y)%2 == 0, 'Error'

                                # Высчитываем отступы между окном и доской
                                self.X_INDENTS = int((self.WIN_WIDTH - (self.COUNTS_CARDS_X * (self.BOX_SIZE + self.INDENTS))) / 2)
                                self.Y_INDENTS = int((self.WIN_HEIGHT - (self.COUNTS_CARDS_Y * (self.BOX_SIZE + self.INDENTS))) / 2)
                        
                            
                            # Запускаем игру заново:
                            board = self.random_board() 
                            open_boxes = self.generate_open_boxes(False)
                            self.draw_board(board, open_boxes)

                            self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)
                            self.create_mes(f'Шагов осталось: {self.STEP}', self.ROSE,230,0,'comicsans', 25)
                            self.create_mes(f'Счет: {self.SCORE}', self.ROSE,540,0,'comicsans', 25)

                            pygame.display.update()    
                            pygame.time.wait(500)

                            self.opening_cards_at_the_beginning(board)
                        click_on_the_first_card = None

            pygame.display.update() 
            self.CLOCK.tick(self.FPS)


    # Функция создает структуру доски
    # Создаем двумерный список, хранит информацию о цвете и форме карточки
    def random_board(self):
        img = []
        for i in self.COLORS:
            for j in self.SHAPES:
                img.append( (i, j) )

        rnd.shuffle(img)
        count_imgs = int(self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y / 2) 
        img = img[:count_imgs] * 2 
        rnd.shuffle(img) 



        board = []
        for _ in range(self.COUNTS_CARDS_X):    
            column = []   
            for _ in range(self.COUNTS_CARDS_Y):    
                column.append(img[0])   
                del img[0]    
            board.append(column)  
        return board


    # Функция задает стартовое знаечние ячейкам - все они закрыты
    def generate_open_boxes(self, flag):    
        open_boxes = []
        for _ in range(self.COUNTS_CARDS_X): 
            open_boxes.append([flag]*self.COUNTS_CARDS_Y) 
        
        return open_boxes

    # Функция, которая рисует доску
    def draw_board(self, board, boxes):
        for i in range(self.COUNTS_CARDS_X):
            for j in range(self.COUNTS_CARDS_Y):
                left, top = self.left_top_coord(i, j)

                if not boxes[i][j]:  
                    pygame.draw.rect(self.WIN, self.BOX_COLOR, (left, top, self.BOX_SIZE,self.BOX_SIZE))

                else:
                    shape, color = self.shape_and_color(board, i, j)
                    self.draw_icon(color, shape, i, j)
                    


    # Функция, возвращающая левую верхнюю координату карточки
    def left_top_coord(self, i, j):
        left = i * (self.BOX_SIZE + self.INDENTS) + self.X_INDENTS
        top = j * (self.BOX_SIZE + self.INDENTS) + self.Y_INDENTS 
        
        return (left, top)

    # Функция, возвращающая цвет и форму карточки
    def shape_and_color(self, board, i, j):
        # В board обращаемся к нужной ячейке, в ней кортеж (shape, color)  
        return board[i][j][0], board[i][j][1]

    #  Функция отрисовки иконок
    def draw_icon(self, shape, color, i, j):
        left, top = self.left_top_coord(i, j) 
        
        if shape == self.DISK:
            pygame.draw.circle(self.WIN, color, (left + 20, top + 20), 17)
            pygame.draw.circle(self.WIN, self.BGCOLOR, (left + 20, top + 20), 13)
            pygame.draw.circle(self.WIN, color, (left + 20, top + 20), 5)
            pygame.draw.arc(self.WIN, color, (left + 10, top + 10, self.BOX_SIZE - 20, self.BOX_SIZE - 20), 0, 180, 3)

        elif shape == self.SQUARE:
            pygame.draw.rect(self.WIN, color, (left + 5, top + 5, self.BOX_SIZE - 10, self.BOX_SIZE - 10))
            pygame.draw.rect(self.WIN, self.BGCOLOR, (left + 10, top + 10, self.BOX_SIZE - 20, self.BOX_SIZE - 20))
            pygame.draw.rect(self.WIN, color, (left + 15, top + 15, self.BOX_SIZE - 30, self.BOX_SIZE - 30))
            pygame.draw.line(self.WIN, color, (left + 6, top + 5), (left + self.BOX_SIZE - 7, top + self.BOX_SIZE - 7), 3)

        elif shape == self.SQUARE_WITH_CIRCLE:
            pygame.draw.rect(self.WIN, color, (left + 5, top + 5, self.BOX_SIZE - 10, self.BOX_SIZE - 10))
            pygame.draw.circle(self.WIN, self.BGCOLOR, (left + 20, top + 20), 10)
            pygame.draw.line(self.WIN, color, (left + 5, top + 20), (left + self.BOX_SIZE - 10, top + 20), 3)

        elif shape == self.TRIANGLE:
            pygame.draw.polygon(self.WIN, color, [[left+20, top+5], [left+5, top+35], [left+35, top+35]])
            pygame.draw.polygon(self.WIN, self.ROSE, [[left+20, top+5], [left+12, top+20], [left+28, top+20]])
            pygame.draw.polygon(self.WIN, self.BGCOLOR, [[left+20, top+10], [left+15, top+25], [left+25, top+25]])
            pygame.draw.line(self.WIN, color, (left + 5, top + 35), (left + 35, top + 35), 3)

        elif shape == self.HEART:
            pygame.draw.polygon(self.WIN, color, [[left+20, top+35], [left+5, top+20], [left+5, top+15], [left+10, top+10], \
                                                  [left+15, top+10], [left+20, top+16], [left+25, top+10], [left+30, top+10], \
                                                    [left+35, top+15], [left+35, top+20]])
            pygame.draw.polygon(self.WIN, self.BGCOLOR, [[left+20, top+35], [left+10, top+20], [left+30, top+20]])
            pygame.draw.line(self.WIN, color, (left + 5, top + 20), (left + 35, top + 20), 3)


    # Функция анимации открытия карточек в начале уровня
    def opening_cards_at_the_beginning(self, board):
        dop_boxes = []

        for i in range(self.COUNTS_CARDS_X):
            for j in range(self.COUNTS_CARDS_Y):
                dop_boxes.append((i, j))
        
        rnd.shuffle(dop_boxes)
        
        grouping = self.grouping_cards(4, dop_boxes)
        
        for i in grouping:
            self.opening_cards(i,board)
            self.closing_cards(i, board)


    # Функция группировки
    def grouping_cards(self, num, dop_boxes):
        groups = []

        for i in range(0, len(dop_boxes), num):
            groups.append(dop_boxes[i:i+num])

        return groups
        
    # Функция открытия карточек    
    def opening_cards(self, grouping,board):
        for i in range(self.BOX_SIZE, -1, -self.SPEED_CARDS):
            self.game_board(board, grouping, i)


    # Функция закрытия карточек
    def closing_cards(self, grouping, board):
        for i in range(0, self.BOX_SIZE+1, self.SPEED_CARDS):
            self.game_board(board, grouping, i)

    # Функция доски, отрисовывающая открытие/закрытия
    def game_board(self, board, grouping, closing_on_pixels):
        
        for i in grouping:
            left, top = self.left_top_coord(i[0], i[1])
           
            pygame.draw.rect(self.WIN, self.BGCOLOR, (left, top, self.BOX_SIZE, self.BOX_SIZE))
            
            color, shape = self.shape_and_color(board, i[0], i[1])
            self.draw_icon(shape,color, i[0], i[1])
            
            if closing_on_pixels > 0:
                pygame.draw.rect(self.WIN, self.BOX_COLOR, (left, top, closing_on_pixels, self.BOX_SIZE))
        
        pygame.display.update()
        self.CLOCK.tick(self.FPS)

    # Функция, определяющая над какой карточкой находится курсор
    def card_definition(self, pos_mouse_x, pos_mouse_y):
        
        for i in range(self.COUNTS_CARDS_X):
            for j in range(self.COUNTS_CARDS_Y):
                left, top = self.left_top_coord(i, j)
                
                place_card = pygame.Rect(left, top, self.BOX_SIZE, self.BOX_SIZE)
                
                if place_card.collidepoint(pos_mouse_x, pos_mouse_y):
                    return(i, j)
        
        return (None, None)


    # Функция, отрисовывающая обводку выбранной карточки
    def selection_highlighting(self, x, y):
        left, top = self.left_top_coord(x,y)
        pygame.draw.rect(self.WIN, self.ROSE, (left-5, top-5, self.BOX_SIZE+10, self.BOX_SIZE+10), 5)

    # Функция определения победы
    def victory(self, open_boxes):
        for i in open_boxes:
            if False in i:
                return 0

        return 1

    # Функция анимации при победе
    def victory_animation(self, board, board_with_open_boxes):
        color_1 = self.DARKBLUE
        color_2 = self.GRAY

        for _ in range(10):
            color_1, color_2 = color_2, color_1
            self.WIN.fill(color_1)
            self.draw_board(board, board_with_open_boxes)
           
            pygame.display.update()
            pygame.time.wait(250)

   
        
    # Функция сохранения статистики лидеров
    def save_leaderboard(self, scores):
        # Сортировка счетов по убыванию
        scores.sort(key=lambda x: x[1], reverse=True)

        # Сохранение только первых 8 результатов
        top_10_scores = scores[:8]

        with open("leaderboard.txt", "w") as file:
            for score in top_10_scores:
                file.write(f"{score[0]}: {score[1]}\n")

    # Функция считывания данных из файла
    def load_leaderboard(self):
        scores = []
        file_path = os.path.join(os.path.dirname(__file__), "leaderboard.txt")

        if os.path.exists(file_path):
            with open("leaderboard.txt", "r") as file:
                for line in file:
                    name, score = line.strip().split(": ")
                    scores.append((name, int(score)))
        else:
            print(f"Файл {file_path} не найден.")

        return scores

    
    # Функция отображения и навигации при приостановке/проигрыше
    def display_leaderboard(self):
        scores = self.load_leaderboard()
        self.WIN.fill(self.BGCOLOR)

        text_y = 50
        # Вывод файла
        title_text = self.font.render("ТОП-8 лучших результатов", True, self.ROSE)
        title_rect = title_text.get_rect(center=(self.WIN_WIDTH // 2, 20))
        self.WIN.blit(title_text, title_rect)

        for i, (name, score) in enumerate(scores, start=1):
            score_text = self.font.render(f"{i}. {name}: {score}", True, self.ROSE)
            score_rect = score_text.get_rect(center=(self.WIN_WIDTH // 2, text_y))
            self.WIN.blit(score_text, score_rect)
            text_y += 30

        # Навигация
        self.create_mes(f'Хочешь занести себя в таблицу лидеров?', self.ROSE, 80,300,'comicsans', 25)
        self.create_mes(f'Твой счет: {self.SCORE}', self.ROSE, 240,330,'comicsans', 25)

        yes_button_rect = pygame.Rect(self.WIN_WIDTH // 4 - self.button_width // 2, 400, self.button_width, self.button_height)
        no_button_rect = pygame.Rect(self.WIN_WIDTH // 2 - self.button_width // 2, 400, self.button_width, self.button_height)
        restart_button_rect = pygame.Rect(3 * self.WIN_WIDTH // 4 - self.button_width // 2, 400, self.button_width, self.button_height)

        pygame.draw.rect(self.WIN, self.button_color, yes_button_rect)
        pygame.draw.rect(self.WIN, self.button_color, no_button_rect)
        pygame.draw.rect(self.WIN, self.button_color, restart_button_rect)

        yes_text = self.button_font.render("Yes", True, self.button_text_color)
        yes_text_rect = yes_text.get_rect(center=yes_button_rect.center)
        self.WIN.blit(yes_text, yes_text_rect)

        no_text = self.button_font.render("No", True, self.button_text_color)
        no_text_rect = no_text.get_rect(center=no_button_rect.center)
        self.WIN.blit(no_text, no_text_rect)

        restart_text = self.button_font.render("Restart", True, self.button_text_color)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        self.WIN.blit(restart_text, restart_text_rect)

        enter_flag = 1 
        pygame.display.flip()

        wait_for_key_press = True
        while wait_for_key_press:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEBUTTONDOWN:

                    if yes_button_rect.collidepoint(event.pos):
                        self.input_text = self.get_user_name()
                        new_score = self.SCORE  
                        scores.append((self.input_text, new_score))
                        scores.sort(key=lambda x: x[1], reverse=True)  # Сортировка по счету
                        self.save_leaderboard(scores)
                        enter_flag = 0
                        wait_for_key_press = False

                    elif no_button_rect.collidepoint(event.pos):
                        self.create_mes('Вы можете перезапустить игру', self.ROSE, 180, 450, 'comicsans', 20)
                        pygame.display.flip()

                    elif restart_button_rect.collidepoint(event.pos):
                        self.LVL = 1
                        self.STEP = 4
                        self.SCORE = 0
                        self.COUNTS_CARDS_X = 2 
                        self.COUNTS_CARDS_Y = 2 
                       
                        assert(self.COUNTS_CARDS_X*self.COUNTS_CARDS_Y) % 2 == 0, 'Error'   
                        # Высчитываем по Х где рисовать доску, чтобы она была посередине
                        self.X_INDENTS = int((self.WIN_WIDTH - (self.COUNTS_CARDS_X * (self.BOX_SIZE + self.INDENTS)))/2)    
                        # Высчитываем по Y где рисовать доску, чтобы она была посередине
                        self.Y_INDENTS = int((self.WIN_HEIGHT - (self.COUNTS_CARDS_Y * (self.BOX_SIZE + self.INDENTS))) / 2)     

                        # Проверка чтобы кол-во карточек на доске не привышало кол-во возможных комбинаций цвет-форма иконок
                        assert len(self.COLORS) * len(self.SHAPES) * 2 >= self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y, "Error"

                        wait_for_key_press = False

        if enter_flag == 1:
            self.main()

        else:
            self.display_leaderboard()

    
    # Функция ввода имени пользователя
    def get_user_name(self):
        self.input_active = True
        while self.input_active:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.input_active = False
                        return self.input_text
                    
                    elif event.key == K_BACKSPACE:
                        self.input_text = self.input_text[:-1]

                    else:
                        self.input_text += event.unicode

            self.WIN.fill((30, 30, 30))
            self.draw_input_box()
            pygame.display.flip()
        
    # Функция отрисовки интерфейса для ввода
    def draw_input_box(self):

        if self.input_active:
            color = self.input_active
        else:
            color =  self.input_color_inactive
        
        pygame.draw.rect(self.WIN, color, self.input_box, 2)

        self.create_mes('Введите свое имя', self.ROSE, 220, 150, 'comicsans', 25)
        text = self.input_font.render(self.input_text, True, (255, 255, 255))
        width = max(200, text.get_width()+10)
        input_box_rect = pygame.Rect(self.WIN_WIDTH // 2.75, 250, width, 40)
        self.WIN.blit(text, (input_box_rect.x+5, input_box_rect.y+5))
        pygame.draw.rect(self.WIN, (255, 255, 255), input_box_rect, 2)

        if self.input_active and pygame.time.get_ticks() % 1000 < 500:
            cursor_x = input_box_rect.x + text.get_width() + 5
            cursor_y = input_box_rect.y + 5
            pygame.draw.line(self.WIN, (255, 255, 255), (cursor_x, cursor_y), (cursor_x, cursor_y + 30), 2)


     # Функция отрисовки надписи
    def create_mes(self, msg, color, x,y, font, size):
        font_style = pygame.font.SysFont(font, size)
        mesg = font_style.render(msg, True, color)
        self.WIN.blit(mesg, [x, y])

 # Запускаем главную функцию игры
game = Game()
    


