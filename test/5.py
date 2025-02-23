import random as rnd
import pygame, sys  
from pygame.locals import *
from os import path

WIN_WINDTH = 640   
WIN_HEIGHT = 480

FPS = 30  

LIGHTBLUE = (151, 157, 226)
YELLOW = (218, 230, 112)
SKINCOLOR = (218, 177, 124)
PURPLE = (193, 131, 195)
MINT = (141, 200, 191)
GRAY = (119, 136, 153)
DARKBLUE = (30, 75, 107)
ROSE = (255, 228, 225)
CORAL = (214, 107, 107)
GREEN = (25, 210, 37)

LVL = 1

BGCOLOR = DARKBLUE

SPEED_CARDS = 8    
BOX_SIZE = 40     
INDENTS = 10   

COUNTS_CARDS_X = 2 
COUNTS_CARDS_Y = 2   

BOX_COLOR = ROSE  

DISK = 'disk'
SQUARE = 'square'
CIRCLE = 'circle'
TRIANGLE = 'triangle'
HEART = 'heart'

COLORS = (LIGHTBLUE, YELLOW, SKINCOLOR, PURPLE, MINT, CORAL, GREEN)
SHAPES = (DISK, SQUARE, CIRCLE, TRIANGLE, HEART)

assert(COUNTS_CARDS_X*COUNTS_CARDS_Y) % 2 == 0, 'Error'   
X_INDENTS = int((WIN_WINDTH - (COUNTS_CARDS_X * (BOX_SIZE + INDENTS)))/2)    
Y_INDENTS = int((WIN_HEIGHT - (COUNTS_CARDS_Y * (BOX_SIZE + INDENTS))) / 2)     

assert len(COLORS) * len(SHAPES) * 2 >= COUNTS_CARDS_X * COUNTS_CARDS_Y, "Error"


def main():
    global WIN, CLOCK
    pygame.init()  

    WIN = pygame.display.set_mode((WIN_WINDTH, WIN_HEIGHT))   
    pygame.display.set_caption('Memory')   
    CLOCK = pygame.time.Clock() 
    
    pos_mouse_x = 0
    pos_mouse_y = 0

    click_on_the_first_card = None

    board = random_board() 
    open_boxes = generate_open_boxes(False)

    WIN.fill(BGCOLOR)  

    global LVL
    create_mes(f'Уровень: {LVL}', ROSE, 10, 0, 'comicsans', 25)

    draw_board(board, open_boxes)

    while True:    
        mouse_clicked = False
        WIN.fill(BGCOLOR)  

        draw_board(board, open_boxes)
        create_mes(f'Уровень: {LVL}', ROSE, 10, 0, 'comicsans', 25)

        for event in pygame.event.get():
        
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                pos_mouse_x, pos_mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                pos_mouse_x, pos_mouse_y = event.pos
                mouse_clicked = True
        
        card_pos_mouse_x, card_pos_mouse_y = card_definition(pos_mouse_x, pos_mouse_y)

        if card_pos_mouse_x != None and card_pos_mouse_y != None:
            if not open_boxes[card_pos_mouse_x][card_pos_mouse_y]:
                selection_highlighting(card_pos_mouse_x, card_pos_mouse_y)

            if not open_boxes[card_pos_mouse_x][card_pos_mouse_y] and mouse_clicked:
                open_boxes[card_pos_mouse_x][card_pos_mouse_y] = True

                if click_on_the_first_card == None:
                    click_on_the_first_card = (card_pos_mouse_x, card_pos_mouse_y)
                else:
                    card_color_1, card_shape_1 = shape_and_color(board, click_on_the_first_card[0], click_on_the_first_card[1])
                    card_color_2, card_shape_2 = shape_and_color(board, card_pos_mouse_x, card_pos_mouse_y)

                    if card_shape_1 != card_shape_2 or card_color_1 != card_color_2:
                        pygame.time.wait(1000)

                        open_boxes[click_on_the_first_card[0]][click_on_the_first_card[1]] = False
                        open_boxes[card_pos_mouse_x][card_pos_mouse_y] = False
                    elif victory(open_boxes):
                        victory_animation(board, open_boxes)
                        pygame.time.wait(1000)

                        global COUNTS_CARDS_X, COUNTS_CARDS_Y, Y_INDENTS, X_INDENTS, BOX_SIZE, INDENTS

                        LVL += 1
                        if LVL <= 4:
                            COUNTS_CARDS_X += 2
                            COUNTS_CARDS_Y += 2

                            assert(COUNTS_CARDS_X*COUNTS_CARDS_Y) % 2 == 0, 'Error'

                            X_INDENTS = int((WIN_WINDTH - (COUNTS_CARDS_X * (BOX_SIZE + INDENTS))) / 2)
                            Y_INDENTS = int((WIN_HEIGHT - (COUNTS_CARDS_Y * (BOX_SIZE + INDENTS))) / 2)

                        board = random_board() 
                        open_boxes = generate_open_boxes(False)

                        draw_board(board, open_boxes)
                        create_mes(f'Уровень: {LVL}', ROSE, 10, 0, 'comicsans', 25)
                        pygame.display.update()    
                        pygame.time.wait(500)

                click_on_the_first_card = None

        pygame.display.update()    
        CLOCK.tick(FPS)


def random_board():
    img = []
    for i in COLORS:
        for j in SHAPES:
            img.append((i, j))

    rnd.shuffle(img)

    count_imgs = int(COUNTS_CARDS_X * COUNTS_CARDS_Y / 2) 

    img = img[:count_imgs] * 2 
    rnd.shuffle(img)   

    board = []
    for _ in range(COUNTS_CARDS_X):   
        column = []   
        for _ in range(COUNTS_CARDS_Y):   
            column.append(img[0])   
            del img[0]   
        board.append(column)   
    return board


def generate_open_boxes(flag):  
    open_boxes = []
    for i in range(COUNTS_CARDS_X): 
        open_boxes.append([flag] * COUNTS_CARDS_Y) 
    return open_boxes


def draw_board(board, boxes):
    for i in range(COUNTS_CARDS_X):
        for j in range(COUNTS_CARDS_Y):
            left, top = left_top_coord(i, j)
            if not boxes[i][j]:   
                pygame.draw.rect(WIN, BOX_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
            else:   
                shape, color = shape_and_color(board, i, j)
                draw_icon(color, shape, i, j)


def left_top_coord(i, j):
    left = i * (BOX_SIZE + INDENTS) + X_INDENTS
    top = j * (BOX_SIZE + INDENTS) + Y_INDENTS 
    return (left, top)


def shape_and_color(board, i, j):
    return board[i][j][0], board[i][j][1]


def draw_icon(shape, color, i, j):
    left, top = left_top_coord(i, j)   
    if shape == DISK:
        pygame.draw.circle(WIN, color, (left + 20, top + 20), 17)
        pygame.draw.circle(WIN, BGCOLOR, (left + 20, top + 20), 12)
    elif shape == SQUARE:
        pygame.draw.rect(WIN, color, (left + 5, top + 5, BOX_SIZE - 10, BOX_SIZE - 10))
        pygame.draw.rect(WIN, BGCOLOR, (left + 10, top + 10, BOX_SIZE - 20, BOX_SIZE - 20))
    elif shape == CIRCLE:
        pygame.draw.rect(WIN, color, (left + 5, top + 5, BOX_SIZE - 10, BOX_SIZE - 10))
    elif shape == TRIANGLE:
        pygame.draw.polygon(WIN, color, [[left + 20, top + 5], [left + 5, top + 35], [left + 35, top + 35]])
    elif shape == HEART:
        pygame.draw.polygon(WIN, color, [[left + 20, top + 35], [left + 5, top + 20], [left + 5, top + 15], [left + 10, top + 10], [left + 15, top + 10], [left + 20, top + 16], [left + 25, top + 10], [left + 30, top + 10], [left + 35, top + 15], [left + 35, top + 20]])


def card_definition(pos_mouse_x, pos_mouse_y):
    for i in range(COUNTS_CARDS_X):
        for j in range(COUNTS_CARDS_Y):
            left, top = left_top_coord(i, j)
            place_card = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
            if place_card.collidepoint(pos_mouse_x, pos_mouse_y):
                return (i, j)
    return (None, None)


def selection_highlighting(x, y):
    left, top = left_top_coord(x, y)
    pygame.draw.rect(WIN, ROSE, (left - 5, top - 5, BOX_SIZE + 10, BOX_SIZE + 10), 5)


def victory(open_boxes):
    for i in open_boxes:
        if False in i:
            return 0
    return 1


def victory_animation(board, board_with_open_boxes):
    color_1 = DARKBLUE
    color_2 = GRAY
    for _ in range(10):
        color_1, color_2 = color_2, color_1
        WIN.fill(color_1)
        draw_board(board, board_with_open_boxes)
        pygame.display.update()
        pygame.time.wait(250)


def create_mes(msg, color, x, y, font, size):
    font_style = pygame.font.SysFont(font, size)
    mesg = font_style.render(msg, True, color)
    WIN.blit(mesg, [x, y])


if __name__ == "__main__":   
    main()
