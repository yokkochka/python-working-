import random as rnd
import pygame, sys   
from pygame.locals import *
from os import path
import os


class Game:
    def __init__(self):
        self.WIN_WIDTH = 640    # Размеры окна
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

        # Цыет фона
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

        # Проверка чтобы кол-во карточек на доске не привышало 
        # кол-во возможных комбинаций цвет-форма иконок
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
        pygame.mixer.music.set_volume(0.2)

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
            

            # Render text on buttons
            interrupt_text = self.button_font.render("Прервать", True, self.button_text_color)
            interrupt_text_rect = interrupt_text.get_rect(center=interrupt_button_rect.center)
            self.WIN.blit(interrupt_text, interrupt_text_rect)

            self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)
            self.create_mes(f'Шагов осталось: {self.STEP}', self.ROSE,220,0,'comicsans', 25)
            self.create_mes(f'Счет: {self.SCORE}', self.ROSE,540,0,'comicsans', 25)

            # Цикл обработки событий
            for event in pygame.event.get():
                # Теперь при нажатии на esc будет происходитьзакрытие окна
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

                # player_name = input("Введите ваше имя: ")
                # self.save_to_leaderboard(player_name, self.LVL)
                


            card_pos_mouse_x, card_pos_mouse_y = self.card_definition(pos_mouse_x, pos_mouse_y)
            
            # Если установлены координаты карточки, на которую указывает курсор
            if card_pos_mouse_x != None and card_pos_mouse_y != None:
                # Если эта карта закрыта
                if not open_boxes[card_pos_mouse_x][card_pos_mouse_y]:
                    # Анимируем закрывающий квадратик на увеличение
                    self.selection_highlighting(card_pos_mouse_x, card_pos_mouse_y)

                # Если эта корта закрыта и мы по ней кликнули
                if not open_boxes[card_pos_mouse_x][card_pos_mouse_y] and mouse_clicked:
                    # Запускаем функцию открытия карточки
                    self.opening_cards([(card_pos_mouse_x, card_pos_mouse_y)], board)
                    # И говорим что теперь эта карточка открыта (в структуре)
                    open_boxes[card_pos_mouse_x][card_pos_mouse_y] = True
                    # Если переменная = None, то эта первая карточка, на которую мы кликнули
                    if click_on_the_first_card == None:
                        # Указываем в этой переменной координаты карточки на которую кликнули
                        # и которая теперь открыта
                        click_on_the_first_card = (card_pos_mouse_x, card_pos_mouse_y)
                    # Если в ней не None, то первая карточка уже была кликнута, соответственно,
                    # это вторая кликнутая карточка и мы можем сравнить иконки в них
                    else:
                        # Запрашиваем значение цвет-форма гконок в двух карточках
                        card_color_1, card_shape_1 = self.shape_and_color(board, click_on_the_first_card[0], click_on_the_first_card[1])
                        card_color_2, card_shape_2 = self.shape_and_color(board, card_pos_mouse_x, card_pos_mouse_y)
                        # Если значения не совпадают
                        if card_shape_1 == card_shape_2 and card_color_1 == card_color_2:
                            self.SCORE += 1
                        if card_shape_1 != card_shape_2 or card_color_1 != card_color_2:
                            # мы ждем 1000 миллисекунд (1 секунду)
                            self.STEP -= 1
                            pygame.time.wait(1000)
                            # Запускаем функцию закрытия карточек
                            self.closing_cards([(click_on_the_first_card[0],click_on_the_first_card[1]),(card_pos_mouse_x,card_pos_mouse_y)],board) 
                            # И снова указываем карточки как закрытые (в структуре)
                            open_boxes[click_on_the_first_card[0]][click_on_the_first_card[1]] = False
                            open_boxes[card_pos_mouse_x][card_pos_mouse_y] = False
                        # Проверяем на победу
                        elif self.victory(open_boxes):
                            # Запускаем анимацию
                            self.victory_animation(board, open_boxes)
                            # Ждем 1 секунду
                            pygame.time.wait(1000)

                            # Берем глобальные переменные

                            # Увеличиваем уровень на 1
                            self.LVL +=1
                            
                            if self.LVL <= 4:
                                # Добавляем значения, чтобы в след.раунде увеличить кол-во карт на доске
                                self.COUNTS_CARDS_X += 2
                                self.COUNTS_CARDS_Y += 2
                                self.STEP = self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y
                                # Повторяем проверку что у у нас четное кол-во карт
                                assert(self.COUNTS_CARDS_X*self.COUNTS_CARDS_Y)%2 == 0, 'Error'

                                # Высчитываем отступы между окном и доской
                                self.X_INDENTS = int((self.WIN_WIDTH - (self.COUNTS_CARDS_X * (self.BOX_SIZE + self.INDENTS))) / 2)
                                self.Y_INDENTS = int((self.WIN_HEIGHT - (self.COUNTS_CARDS_Y * (self.BOX_SIZE + self.INDENTS))) / 2)
                        
                            
                            # Запускаем игру заново:
                            # Создаем рандомную доску
                            board = self.random_board() 
                            # Создаем структуру 
                            open_boxes = self.generate_open_boxes(False)
                            # Отрисовываем доск
                            self.draw_board(board, open_boxes)
                            self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)
                            self.create_mes(f'Шагов осталось: {self.STEP}', self.ROSE,230,0,'comicsans', 25)
                            self.create_mes(f'Счет: {self.SCORE}', self.ROSE,540,0,'comicsans', 25)
                            pygame.display.update()     # Обновлем окно
                            pygame.time.wait(500)

                            # Запускаем стартовую анимацию
                            self.opening_cards_at_the_beginning(board)
                        # После того как мы либо нашли две одинаковые карточки
                        # либо закрылись две разные, снова ставим значение None
                        click_on_the_first_card = None

            pygame.display.update()     # Обновлем окно
            self.CLOCK.tick(self.FPS)



    def random_board(self):
        img = []
        for i in self.COLORS:
            for j in self.SHAPES:
                img.append( (i, j) )

        rnd.shuffle(img)
        # Высчитываем сколько картинок намнужно исходя из размеров доски
        count_imgs = int(self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y / 2) 
        # Берем только столько картинок, сколько нужно для доски в двойном размере каждую
        img = img[:count_imgs] * 2 
        rnd.shuffle(img) 

        # Создаем список уже для доски
        board = []
        for _ in range(self.COUNTS_CARDS_X):    
            column = []   
            for _ in range(self.COUNTS_CARDS_Y):    
                column.append(img[0])   
                del img[0]    
            board.append(column)  
        return board



    def generate_open_boxes(self, flag):   # Функция задает стартовое знаечние ячейкам - все они закрыты 
        open_boxes = []
        for _ in range(self.COUNTS_CARDS_X): 
            open_boxes.append([flag]*self.COUNTS_CARDS_Y) 
        
        return open_boxes


    def draw_board(self, board, boxes):
        for i in range(self.COUNTS_CARDS_X):
            for j in range(self.COUNTS_CARDS_Y):
                # Проходимся по каждой карточке и считываем ее верхнюю левую координату координату
                left, top = self.left_top_coord(i, j)
                if not boxes[i][j]:  
                    # Отрисовываем квадрат, который будет ее закрывать
                    pygame.draw.rect(self.WIN, self.BOX_COLOR, (left, top, self.BOX_SIZE,self.BOX_SIZE))
                else:    # Если карточка откыта
                    shape, color = self.shape_and_color(board, i, j)
                    self.draw_icon(color, shape, i, j)
                    


# Функция, возвращающая левую верхнюю координату карточки
    def left_top_coord(self, i, j):
        # Кол-во карточки размером BOX_SIZE с учетом отступом (iNDENTS) + 
        # отступ от границы окна до доски (X_INDENTS)
        left = i * (self.BOX_SIZE + self.INDENTS) + self.X_INDENTS
        top = j * (self.BOX_SIZE + self.INDENTS) + self.Y_INDENTS 
        
        return (left, top)


    def shape_and_color(self, board, i, j):
        # В board обращаемся к нужной ячейке, в ней кортеж (shape, color)  
        return board[i][j][0], board[i][j][1]

    #  Функция отрисовки иконок
    def draw_icon(self, shape, color, i, j):

        left, top = self.left_top_coord(i, j)    #узнаем координату ячейки 
        
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
            pygame.draw.polygon(self.WIN, color, [[left+20, top+35], [left+5, top+20], [left+5, top+15], [left+10, top+10], [left+15, top+10], [left+20, top+16], [left+25, top+10], [left+30, top+10], [left+35, top+15], [left+35, top+20]])
            pygame.draw.polygon(self.WIN, self.BGCOLOR, [[left+20, top+35], [left+10, top+20], [left+30, top+20]])
            pygame.draw.line(self.WIN, color, (left + 5, top + 20), (left + 35, top + 20), 3)



    def opening_cards_at_the_beginning(self, board):
        # Создаем дополнительный список
        dop_boxes = []
        # Получаем список кортежей координат всех карточек
        for i in range(self.COUNTS_CARDS_X):
            for j in range(self.COUNTS_CARDS_Y):
                dop_boxes.append((i, j))
        # Перемешиваем, чтобы открывались всегда разные
        rnd.shuffle(dop_boxes)
        # Запускаем функцию, которая сгруппирует их в группы по 4 карточки
        grouping = self.grouping_cards(4, dop_boxes)
        
        # Проходимся по каждой такой группе
        for i in grouping:
            # Функция открытия
            self.opening_cards(i,board)
            # Функция закрытия
            self.closing_cards(i, board)


    # Функция группировки
    def grouping_cards(self, num, dop_boxes):
        # Создаем двумерный список, элементом будет список из
        # кортежей координат 4 карточек
        groups = []
        # Принцип этого описан в методичке
        for i in range(0, len(dop_boxes), num):
            groups.append(dop_boxes[i:i+num])
        return groups
        
    # Функция открытия карточек    
    def opening_cards(self, grouping,board):
        # Принцип описан в методичке
        for i in range(self.BOX_SIZE, -1, -self.SPEED_CARDS):
            self.game_board(board, grouping, i)


    # Функция закрытия карточек
    def closing_cards(self, grouping, board):
        for i in range(0, self.BOX_SIZE+1, self.SPEED_CARDS):
            self.game_board(board, grouping, i)

    # Функция доски, отрисовывающая открытие/закрытия
    def game_board(self, board, grouping, closing_on_pixels):
        # Проходимся в одной из групп карточек по каждой карточке
        for i in grouping:
            # Получаем координату карточки
            left, top = self.left_top_coord(i[0], i[1])
            # Отрисовываем задний фон открытия в цвет дона окна
            pygame.draw.rect(self.WIN, self.BGCOLOR, (left, top, self.BOX_SIZE, self.BOX_SIZE))
            # Получаем цвет и форму иконки
            color, shape = self.shape_and_color(board, i[0], i[1])
            # Отрисовываем иконку
            self.draw_icon(shape,color, i[0], i[1])
            # Отрисовываем коробочку (принцип в методичке)
            if closing_on_pixels > 0:
                pygame.draw.rect(self.WIN, self.BOX_COLOR, (left, top, closing_on_pixels, self.BOX_SIZE))
        # Обязательно обновляем
        pygame.display.update()
        self.CLOCK.tick(self.FPS)

    # Функция, определяющая над какой карточкой находится курсор
    def card_definition(self, pos_mouse_x, pos_mouse_y):
        # Перебираем все карточки
        for i in range(self.COUNTS_CARDS_X):
            for j in range(self.COUNTS_CARDS_Y):
                # Определяем координаты очередной карточки
                left, top = self.left_top_coord(i, j)
                # Определяем место, занимаемое карточкой
                place_card = pygame.Rect(left, top, self.BOX_SIZE, self.BOX_SIZE)
                # Если координаты курсора входят в область нахождения карточки
                if place_card.collidepoint(pos_mouse_x, pos_mouse_y):
                    # Возвращаем координаты этой карточки
                    return(i, j)
        # Если такой карточки не найдено, возвращаем пустоту
        return (None, None)


    # Функция, отрисовывающая обводку выбранной карточки
    def selection_highlighting(self, x, y):
        # Запрос координат для отрисовки
        left, top = self.left_top_coord(x,y)
        pygame.draw.rect(self.WIN, self.ROSE, (left-5, top-5, self.BOX_SIZE+10, self.BOX_SIZE+10), 5)

    # Функция определения победы
    def victory(self, open_boxes):
        # Проходимся по всей структуре
        for i in open_boxes:
            # Если хоть в одном элементе структуры есть False (закрытая карточка)
            if False in i:
                # Возвращаем 0
                return 0
        # Если закрытой карточки нет, то возвращаем 1
        return 1

    # Функция анимации при поедел
    def victory_animation(self, board, board_with_open_boxes):
        # Берем цвета для анимации
        color_1 = self.DARKBLUE
        color_2 = self.GRAY
        # Повторяться будет 11 раз
        for _ in range(10):
            # Делаем смену цвета (чтобы менялось каждый раз на другое)
            color_1, color_2 = color_2, color_1
            # Заливаем фон цветом
            self.WIN.fill(color_1)
            # Не забываем при этом отрисовывать доску с иконками
            self.draw_board(board, board_with_open_boxes)
            # Одновляем доску
            pygame.display.update()
            # Ждем 250 миллисекунд
            pygame.time.wait(250)

   
        

    def save_leaderboard(self, scores):
        # Сортировка счетов по убыванию
        scores.sort(key=lambda x: x[1], reverse=True)

        # Сохранение только первых 10 результатов
        top_10_scores = scores[:8]

        with open("leaderboard.txt", "w") as file:
            for score in top_10_scores:
                file.write(f"{score[0]}: {score[1]}\n")

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

    

    def display_leaderboard(self):
        # Your existing code here
        scores = self.load_leaderboard()
        # Clear the screen
        self.WIN.fill(self.BGCOLOR)

        # Display the leaderboard on the game window
        text_y = 50

        # Display title
        title_text = self.font.render("ТОП-8 лучших результатов", True, self.ROSE)
        title_rect = title_text.get_rect(center=(self.WIN_WIDTH // 2, 20))
        self.WIN.blit(title_text, title_rect)

        # Display scores
        for i, (name, score) in enumerate(scores, start=1):
            score_text = self.font.render(f"{i}. {name}: {score}", True, self.ROSE)
            score_rect = score_text.get_rect(center=(self.WIN_WIDTH // 2, text_y))
            self.WIN.blit(score_text, score_rect)
            text_y += 30

    #     pygame.display.flip()
        self.create_mes(f'Хочешь занести себя в таблицу лидеров?', self.ROSE, 80,300,'comicsans', 25)
        self.create_mes(f'Твой счет: {self.SCORE}', self.ROSE, 240,330,'comicsans', 25)

        # Create Yes/No buttons
        yes_button_rect = pygame.Rect(self.WIN_WIDTH // 4 - self.button_width // 2, 400, self.button_width, self.button_height)
        no_button_rect = pygame.Rect(self.WIN_WIDTH // 2 - self.button_width // 2, 400, self.button_width, self.button_height)
        restart_button_rect = pygame.Rect(3 * self.WIN_WIDTH // 4 - self.button_width // 2, 400, self.button_width, self.button_height)

        pygame.draw.rect(self.WIN, self.button_color, yes_button_rect)
        pygame.draw.rect(self.WIN, self.button_color, no_button_rect)
        pygame.draw.rect(self.WIN, self.button_color, restart_button_rect)

        # Render text on buttons
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

        # Wait for a key press or button press before returning to the main loop
        wait_for_key_press = True
        while wait_for_key_press:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        wait_for_key_press = False

                # Check for mouse click on buttons
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
                        # Handle No button click
                        self.create_mes('Вы можете перезапустить игру', self.ROSE, 180, 450, 'comicsans', 20)
                        pygame.display.flip()
                    elif restart_button_rect.collidepoint(event.pos):
                        # Handle No button click
                        self.LVL = 1
                        self.STEP = 4
                        self.SCORE = 0
                        self.COUNTS_CARDS_X = 2  # Количество карточек по горизонтали
                        self.COUNTS_CARDS_Y = 2    # Количество карточек по вертикали
                        # Проверка на четное количество карточек
                        assert(self.COUNTS_CARDS_X*self.COUNTS_CARDS_Y) % 2 == 0, 'Error'   
                        # Высчитываем по Х где рисовать доску, чтобы она была посередине
                        self.X_INDENTS = int((self.WIN_WIDTH - (self.COUNTS_CARDS_X * (self.BOX_SIZE + self.INDENTS)))/2)    
                        # Высчитываем по Y где рисовать доску, чтобы она была посередине
                        self.Y_INDENTS = int((self.WIN_HEIGHT - (self.COUNTS_CARDS_Y * (self.BOX_SIZE + self.INDENTS))) / 2)     

                        # Проверка чтобы кол-во карточек на доске не привышало 
                        # кол-во возможных комбинаций цвет-форма иконок
                        assert len(self.COLORS) * len(self.SHAPES) * 2 >= self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y, "Error"

                        wait_for_key_press = False
        if enter_flag == 1:
            self.main()
        else:
            self.display_leaderboard()

    
    
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
        # Формируем шрифт и размер текста в переменну. стиля текста
        font_style = pygame.font.SysFont(font, size)
        # Формируем текст сообщения и его цвет
        mesg = font_style.render(msg, True, color)
        # Отображаем
        self.WIN.blit(mesg, [x, y])

 # Запускаем главную функцию игры
game = Game()
    


