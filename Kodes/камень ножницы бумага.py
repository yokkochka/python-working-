import time
import random

print('Здравствуй, игрок! Это игра Камень-ножницы-бумага')
time.sleep(3)
print('Есть несколько правил: \n1) Игра ведётся до 3 очков')
time.sleep(3)
print('2) На каждом этапе игры нужно выбрать "Камень", "Ножницы" или "Бумага"')

time.sleep(5)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('Поехали!')

user_score = 0
bot_score = 0
start_list = ['Камень', 'Ножницы', 'Бумага']

while user_score != 3 and bot_score != 3:
    print('\t\t\t\t\tНОВЫЙ РАУНД')
    user_choice = input('Введите ваш выбор: ')
    bot_choice = random.choice(start_list)

    print(f'\t\tВыбор игрока: {user_choice}\t\t\t\t\tВыбор бота: {bot_choice}')
    
    if user_choice == bot_choice:
        user_score += 1
        bot_score += 1
        print('Ничья!')
    elif user_choice == 'Ножницы' and bot_choice == 'Камень':
        bot_score +=1
        print('Победил бот')
    elif user_choice == 'Камень' and bot_choice == 'Ножницы':
        user_score += 1
        print('Победил игрок')
    elif user_choice == 'Бумага' and bot_choice == 'Камень':
        user_score += 1
        print('Победил игрок')
    elif user_choice == 'Камень' and bot_choice == 'Бумага':
        bot_score += 1
        print('Победил бот')
    elif user_choice == 'Ножницы' and bot_choice == 'Бумага':
        user_score += 1
        print('Победил игрок')
    elif user_choice == 'Бумага' and bot_choice == 'Ножницы':
        bot_score += 1
        print('Победил бот')
    else:
        print('Ошибка раунда')

    print('\t\t\t\t\tТЕКУЩИЙ СЧЁТ')
    print(f'\t\tИгрок: {user_score}\t\t\t\t\tБот: {bot_score}')
    time.sleep(3)



time.sleep(3)
print('\t\t\t\t\tИТОГИ')

if user_score > bot_score:
    print('Победил игрок!')
elif bot_score > user_score:
    print('Победил бот!')
else:
    print('Ничья!')

print('\t\t\t\t\tФИНАЛЬНЫЙ СЧЁТ ИГРЫ')
print(f'\t\tИгрок: {user_score}\t\t\t\t\tБот: {bot_score}')








