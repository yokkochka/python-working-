<<<<<<< HEAD
import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption('Беги Форест')

skysurface = pygame.image.load('graphics/sky.jpg').convert()
groundsurface = pygame.image.load('graphics/ground.png').convert()
font = pygame.font.Font(None, 50)
textsurface = font.render('Score 0', False, "Black")
text_rectangle = textsurface.get_rect(center=(650, 50))
snailsurface = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rectangle = snailsurface.get_rect(midbottom=(600, 300))
mysurface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
my_rectangle = mysurface.get_rect(midbottom=(80, 300))

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(skysurface, (0, 0))
    screen.blit(groundsurface, (0, 300))
    screen.blit(textsurface, (650, 50))


    snail_rectangle.x -= 1
    if snail_rectangle.left <= 0:
        snail_rectangle.right = 800
    screen.blit(snailsurface, snail_rectangle)


    screen.blit(mysurface, (my_rectangle))


    if my_rectangle.colliderect(snail_rectangle):
        print('Упс!')


    pygame.display.update()


    clock.tick(60) 
=======
# import requests
# from bs4 import BeautifulSoup
# import re

# def mean(lst1, lst2):
#     return list(map(lambda x, y: (x + y) / 2, lst1, lst2))

# def site_request(url):
#     response = requests.get(url)
#     bs = BeautifulSoup(response.text, 'lxml')
#     return bs

# def count_days_after_min(lst):
#     return len(lst[:lst.index(min(lst))])

# def shift_words(all_words):
#     i = 0
#     while i < len(all_words):
#         if 'а' in all_words[i]:
#             if i > 0:
#                 all_words[i-1], all_words[i] = all_words[i], all_words[i-1]
#                 i -= 1  
#         elif 'о' in all_words[i]:
#             if i > 2:
    
#                 all_words[i-3],all_words[i-2], all_words[i-1], all_words[i] = all_words[i],all_words[i-3], all_words[i-2], all_words[i-1]
#                 i -= 3  
#         i += 1 
#     return all_words


    


# bs = site_request('https://meteoinfo.ru/forecasts/russia/moscow-area/moscow')
# temp = bs.find_all('span', class_='fc_temp_short')

# temp = list( map( int, [i[:i.find('.')] for i in [i.text for i in temp]]))
# site1_days = temp[::2]
# site1_nights = temp[1::2]

# if len(site1_days) > len(site1_nights):
#     del site1_days[0]
# elif len(site1_days) < len(site1_nights):
#     del site1_nights[-1]

# site1_mean = mean(site1_days, site1_nights)

# print(f"\nsite 1: {site1_mean}")
# print(f"item 2.4: {count_days_after_min(site1_days)}")




# bs = site_request('https://www.meteovesti.ru/pogoda_10/27612')
# temp = bs.find_all('div', class_='_h1 m-0 mt-4 ms-2 me-2 text-right temper')

# site2_days = list( map( int, [i[:i.find('°')] for i in [i.text for i in temp]]))

# site2_nights = [i.get('data-night') for i in temp]
# site2_nights = list( map( int, [i[:i.find('°')] for i in site2_nights]))
# site2_mean = mean(site2_days, site2_nights)

# print(f"\nsite 2: {site2_mean}")
# print(f"item 2.4: {count_days_after_min(site2_days)}")



# bs= site_request('https://pogoda.mail.ru/prognoz/moskva/extended/')
# temp = bs.find_all('span', class_='text text_block text_bold_medium margin_bottom_10')

# site3 = list( map( int, [i[:i.find('°')] for i in [i.text for i in temp]]))

# site3_days = site3[2::4]
# site3_nights = site3[::4]
# site3_mean = mean(site3_days, site3_nights)

# print(f"\nsite 3: {site3_mean}")
# print(f"item 2.4: {count_days_after_min(site3_days)}")



# bs= site_request('https://weather.rambler.ru/v-moskve/7-days/')
# temp = bs.find_all('span', class_='Njqa')

# site4 = list( map( int, [i[:i.find('°')] for i in [i.text for i in temp]]))

# site4_days = site4[2::4]
# site4_nights = site4[::4]
# site4_mean = mean(site4_days, site4_nights)

# print(f"\nsite 4: {site4_mean}")
# print(f"item 2.4: {count_days_after_min(site4_days)}")


# min_len = min(len(site1_mean), len(site2_mean), len(site3_mean), len(site4_mean))
# site1_mean = site1_mean[:min_len]
# site2_mean = site2_mean[:min_len]
# site3_mean = site3_mean[:min_len]
# site4_mean = site4_mean[:min_len]


# bs = site_request('https://meteoinfo.ru/forecasts/russia/moscow-area/moscow')
# temp = bs.find_all('td', class_='td_short_gr')

# temp = [i for i in [i.text for i in temp] if any(day in i for day in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"])]
# dates = list(map(int, [re.search(r'\d+', day).group() for day in temp]))
# temp = [re.split(r'\d', day, 1)[0] for day in temp]


# for i in range(min_len):
#     print(f"date: {dates[i]}, day: {temp[i]}, mean temperature: {(site1_mean[i] + site2_mean[i] + site3_mean[i] + site4_mean[i]) / 4}, ")






# print(dates)

# all_words = []
# len_words = 0
# count_a_o = 0

# for i in temp:
#     bs = site_request('https://ru.wikipedia.org/wiki/' + i)
#     temp = bs.find('p').text
#     all_words += temp.split()

# len_words += len(all_words)
# count_a_o += sum(1 for word in all_words if 'а' in word or 'о' in word)
    
# print(f"itmem 2.6: {len_words} (len), {count_a_o} (count a or o)")
# print(all_words)

# shift_all_words = shift_words(all_words)
# print("\n", shift_all_words)




f = open('320_17.txt', 'r')

data = list(map(int, [i for i in f]))

count = 0
min_summ = 1000000000
min_element = 10000000000

for i in data:
    if i < min_element:
        min_element = i

for i in range(len(data)-1):
    for j in range(i, len(data)):


for i in range(len(data) - 2):
    # print(data[i], data[i+1])
    # para = [data[i], data[i+1]]
    if data[i] % 111 == min_element or data[i+1] % 111 == min_element :
        count += 1
        if data[i] + data[i+1] < min_summ:
            min_summ = data[i] + data[i+1]

print(count, min_summ)





# teacher_loger = {
#                     'M':'567',
#                     'R':'123',
#                     'I':'890'
#                 }

# class_journal = {
#                     "Ivanov Ivan": 
#                         {
#                             'math': [4], 
#                             'rus': [5,5,5,4], 
#                             'info': [5,5,5]
#                         },
#                     "Petya Petrov":
#                         {
#                             'math':[5,5,5],
#                             'run':[4,4],
#                             'info':[5,3,4]
#                         },
#                     "Kirill Kirillov":
#                         {   
#                             'math':[4,4,5],
#                             'rus':[5,3,3],
#                             'info':[4,4,4,5]
#                         }
#                 }

# # [math, rus, info]
# list_subjects = list(list(class_journal.values())[0].keys())
# # ["Ivanov Ivan", "Petr Petrov", "Kirill Kirrilov"]
# list_students = list(class_journal.keys())


# main_menu = "\nВы хотите: \n\t1) Добавлить оценку, \n\t2) Вывести топ лучших учеников по предмету\n"
# print(main_menu)
# choise = input("Введите 1 или 2: ")

# if choise == '1':
#     login = input("\nВведите свое имя: ")
#     password = input("Введите пароль: ")
    
#     index_subject = 0
#     autorized = False

#     for loger_login, loger_password in teacher_loger.items():
#         if loger_login == login and loger_password == password:
#             autorized = True
#             break
#         index_subject += 1

#     if autorized == True:
#         print(f"Вы вошли как {login}, ваш предмет: {list_subjects[index_subject]}")
#         print("\nДоступные ученики: ")
#         for i in range(len(list_students)):
#             print(f"\t{i+1}) {list_students[i]}")
#         name_student = input("\nВведите имя ученика, которому хотите добаить оценку: ")
#         mark_student = int(input("Введите оценку ученика: "))
#         class_journal[name_student][list_subjects[index_subject]].append(mark_student)
#         print("\nОценка успешно добавлена!\n\nТекущий классный журнал:")
#         for i, j in class_journal.items():
#             print(f"\t{i}:")
#             for k, l in j.items():
#                 print(f"\t\t{k}: {l}")
#             print()

#     else:
#         print('Такого пользователя нет!')

# elif choise == '2':
#     print("Вы выбрали второй пункт")
# else:
#     print("Такого пункта нет, будте внимательнее!")
>>>>>>> fc63bacfecd34fb7a4ab584de4b34413aba29363
