import random as rnd
import pygame, sys   # Импорты
from pygame.locals import *
from os import path


class Game:
    def __init__(self):
        self.WIN_WINDTH = 640    # Прописываем необходимые размеры окна
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
        self.WIN = 0
        self.CLOCK = 0

        # Определяем цвет стартового окна
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
        self.CIRCLE = 'circle'
        self.TRIANGLE = 'triangle'
        self.HEART = 'heart'

        # Список цветов
        self.COLORS = (self.LIGHTBLUE, self.YELLOW, self.SKINCOLOR, self.PURPLE, self.MINT, self.CORAL, self.GREEN)
        # Список форм иконок
        self.SHAPES = (self.DISK, self.SQUARE, self.CIRCLE, self.TRIANGLE, self.HEART)

        # Проверка на четное количество карточек
        assert(self.COUNTS_CARDS_X*self.COUNTS_CARDS_Y) % 2 == 0, 'Error'   
        # Высчитываем по Х где рисовать доску, чтобы она была посередине
        self.X_INDENTS = int((self.WIN_WINDTH - (self.COUNTS_CARDS_X * (self.BOX_SIZE + self.INDENTS)))/2)    
        # Высчитываем по Y где рисовать доску, чтобы она была посередине
        self.Y_INDENTS = int((self.WIN_HEIGHT - (self.COUNTS_CARDS_Y * (self.BOX_SIZE + self.INDENTS))) / 2)     

        # Проверка чтобы кол-во карточек на доске не привышало 
        # кол-во возможных комбинаций цвет-форма иконок
        assert len(self.COLORS) * len(self.SHAPES) * 2 >= self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y, "Error"

        self.main()


    def main(self):
        pygame.init()   # Инициализируем PyGame, обязательно для работы

        # Музыка
        dir = path.join(path.dirname(__file__), 'music_dir')
        pygame.mixer.music.load(path.join(dir, 'music.mp3'))
        # Параметр -1 для зацикливания фоновой фузыки
        pygame.mixer.music.play(-1)

        self.WIN = pygame.display.set_mode((self.WIN_WINDTH,self.WIN_HEIGHT))    # Создаем окно
        pygame.display.set_caption('Memory')    # Задаем название
        self.CLOCK = pygame.time.Clock() 
        
        pos_mouse_x = 0
        pos_mouse_y = 0

        click_on_the_first_card = None

        # Создаем рандомную доску
        board = self.random_board() 
        open_boxes = self.generate_open_boxes(False)


        self.WIN.fill(self.BGCOLOR)   # Заливаем окноs

        
        self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)
            
        # Запускаем начальную анимацию
        self.opening_cards_at_the_beginning(board)

        while True:     # Каждый проход цикла нужно перерисовывать окно
            mouse_clicked = False
            self.WIN.fill(self.BGCOLOR)   # Поэтому заново заливаем фон
            # Вызываем функцию отрисовки доски
            self.draw_board(board, open_boxes)

            self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)

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
            
            card_pos_mouse_x, card_pos_mouse_y = self.card_definition(pos_mouse_x, pos_mouse_y)
            

            
            # Если установлены координаты карточки, на которую указывает курсор
            if card_pos_mouse_x != None and card_pos_mouse_y != None:
                # Если эта корта закрыта
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
                        if card_shape_1 != card_shape_2 or card_color_1 != card_color_2:
                            # мы ждем 1000 миллисекунд (1 секунду)
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
                                # Повторяем проверку что у у нас четное кол-во карт
                                assert(self.COUNTS_CARDS_X*self.COUNTS_CARDS_Y)%2 == 0, 'Error'

                                # Высчитываем отступы между окном и доской
                                self.X_INDENTS = int((self.WIN_WINDTH - (self.COUNTS_CARDS_X * (self.BOX_SIZE + self.INDENTS))) / 2)
                                self.Y_INDENTS = int((self.WIN_HEIGHT - (self.COUNTS_CARDS_Y * (self.BOX_SIZE + self.INDENTS))) / 2)
                            
                            # Запускаем игру заново:
                            # Создаем рандомную доску
                            board = self.random_board() 
                            # Создаем структуру 
                            open_boxes = self.generate_open_boxes(False)
                            # Отрисовываем доск
                            self.draw_board(board, open_boxes)
                            self.create_mes(f'Уровень: {self.LVL}', self.ROSE, 10,0,'comicsans', 25)
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
        # Создаем список в котором будут содержаться все возможные комбинации цвет-форма
        img = []
        for i in self.COLORS:
            for j in self.SHAPES:
                img.append( (i, j) )

        rnd.shuffle(img) # Замешиваем список
        # Высчитываем сколько картинок намнужно исходя из размеров доски
        count_imgs = int(self.COUNTS_CARDS_X * self.COUNTS_CARDS_Y / 2) 
        # Берем только столько картинок, сколько нужно для доски в двойном размере каждую
        img = img[:count_imgs] * 2 
        rnd.shuffle(img)    # И снова замешиваем

        # Создаем список уже для доски
        # Это будет двумерный список, состоящий из списков, содержащих инфу о каждой колонке
        board = []
        for _ in range(self.COUNTS_CARDS_X):    # Проходимся по кол-ву колонок
            column = []    # Создаем пустой список для колонки
            for _ in range(self.COUNTS_CARDS_Y):    # Проходимся по каждому элементу
                column.append(img[0])    # Помещаем туда пару цвет-форма
                del img[0]    # И удаляем из списка, чтобы не было повторов
            board.append(column)    # Добавляем в список доски колонку
        return board


    def generate_open_boxes(self, flag):   # Функция задает стартовое знаечние ячейкам - все они закрыты 
        # Создаем двумерный список для ячеек
        open_boxes = []
        for _ in range(self.COUNTS_CARDS_X): 
            open_boxes.append([flag]*self.COUNTS_CARDS_Y) 
        return open_boxes


    def draw_board(self, board, boxes):
        for i in range(self.COUNTS_CARDS_X):
            for j in range(self.COUNTS_CARDS_Y):
                # Проходимся по каждой карточке и считываем ее верхнюю левую координату координату
                left, top = self.left_top_coord(i, j)
                if not boxes[i][j]:    # Если карточка закрыта
                    # Отрисовываем квадрат, который будет ее закрывать
                    # Квадрат отображается на окне WIN, цветом BOX_COLOR, на координатах и размером:
                    pygame.draw.rect(self.WIN, self.BOX_COLOR, (left, top, self.BOX_SIZE,self.BOX_SIZE))
                else:    # Если карточка откыта
                    shape, color = self.shape_and_color(board, i, j)
                    self.draw_icon(color, shape, i, j)
                    



    def left_top_coord(self, i, j):
        # Кол-во карточки размером BOX_SIZE с учетом отступом (iNDENTS) + 
        # отступ от границы окна до доски (X_INDENTS)
        left = i * (self.BOX_SIZE + self.INDENTS) + self.X_INDENTS
        top = j * (self.BOX_SIZE + self.INDENTS) + self.Y_INDENTS 
        #print(left, top)
        return (left, top)

    def shape_and_color(self, board, i, j):
        # В board обращаемся к нужной ячейке, в ней кортеж (shape, color)  
        return board[i][j][0], board[i][j][1]


    def draw_icon(self, shape, color, i, j):
        left, top = self.left_top_coord(i, j)    #узнаем координату ячейки 
        # В зависимости от формы отрисовываем нужную фигуру
        if shape == self.DISK:
            pygame.draw.circle(self.WIN, color, (left + 20, top + 20), 17)
            pygame.draw.circle(self.WIN, self.BGCOLOR, (left + 20, top + 20), 12)
        elif shape == self.SQUARE:
            pygame.draw.rect(self.WIN, color, (left + 5, top + 5, self.BOX_SIZE - 10, self.BOX_SIZE - 10))
            pygame.draw.rect(self.WIN, self.BGCOLOR, (left + 10, top + 10, self.BOX_SIZE - 20, self.BOX_SIZE - 20))
        elif shape == self.CIRCLE:
            pygame.draw.rect(self.WIN, color, (left + 5, top + 5, self.BOX_SIZE - 10, self.BOX_SIZE - 10))
        elif shape == self.TRIANGLE:
            pygame.draw.polygon(self.WIN, color, [[left+20, top+5], [left+5, top+35], [left+35, top+35]])
        elif shape == self.HEART:
            pygame.draw.polygon(self.WIN, color, [[left+20, top+35], [left+5, top+20], [left+5, top+15], [left+10, top+10], [left+15, top+10], [left+20, top+16], [left+25, top+10], [left+30, top+10], [left+35, top+15], [left+35, top+20]])



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
    


