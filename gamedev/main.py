import pygame
from sys import exit

def show_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    text_surface = font.render(f'Время: {current_time}', False, "Black")
    text_rectangle = text_surface.get_rect(center=(650, 50))
    screen.blit(text_surface, text_rectangle)
    return current_time

def reset_game():
    global my_rectangle, snail_rectangle, gravity, game_active, start_time
    my_rectangle.midbottom = (150, 300)
    snail_rectangle.midbottom = (800, 300)
    gravity = 0
    start_time = int(pygame.time.get_ticks() / 1000)
    game_active = True

def show_message(text, sub_text):
    title_surface = font.render(text, True, "Black")
    title_rect = title_surface.get_rect(center=(400, 150))
    screen.blit(title_surface, title_rect)

    sub_surface = font_small.render(sub_text, True, "Black")
    sub_rect = sub_surface.get_rect(center=(400, 250))
    screen.blit(sub_surface, sub_rect)

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Беги, Форест!')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 30)

sky_surface = pygame.image.load('graphics/sky.jpg').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(800, 300))

player_surface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
my_rectangle = player_surface.get_rect(midbottom=(150, 300))

gravity = 0

game_active = False
start_time = 0

while True:
    screen.fill("White")
    if game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and my_rectangle.bottom >= 300:
                    gravity = -13

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
    
        snail_rectangle.x -= 4
        if snail_rectangle.right <= 0:
            snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)
    
        gravity += 0.5
        my_rectangle.y += gravity
        if my_rectangle.bottom >= 300:
            my_rectangle.bottom = 300

        screen.blit(player_surface, my_rectangle)
        score = show_score()
    
        if my_rectangle.colliderect(snail_rectangle):
            game_active = False 

    else:
        if start_time == 0:
            show_message("Беги, Форест!", "Нажмите ПРОБЕЛ для старта")
        else:
            show_message(f"Вы проиграли! Счёт: {score}", "Нажмите ПРОБЕЛ, чтобы сыграть снова")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()

    pygame.display.update()
    clock.tick(60)
