from random import choice
from time import sleep
counter_player = 0
counter_bot = 0
is_broken = False
bot_list = ["камень", "ножницы", "бумага"]
print('Ты открываешь глаза')
sleep(1)
print('Комната, в которой ты находишься, тебе не знакома')
sleep(1)
print('Ты встаешь, осматриваешь комнату и в это время слышишь голос')
sleep(2)
print('Он говорит о том, что тебе придется сыграть в игру если ты хочешь выбраться отсюда...')
sleep(2)
print('Что ж, тебе предстоит сыграть три раунда с Ежиком')
print()
sleep(1)
print('Уверена, игра тебе знакома!')
print()
sleep(1)
for i in range(3):
    player  = input('Выбери: камень, ножницы, или бумага')
    bot = choice(bot_list)

    print('Ты выбираешь:', player + '!')
    print('Ежик выбирает:', bot + '!')

    if player == bot:
        print('Ничья!')
        counter_bot += 1
        counter_player += 1
    elif (player == 'камень' and bot =='ножницы') or (player == 'ножницы' and bot == 'бумага') or (player == 'бумага' and bot == 'камень'):
        print('Ты победил!')
        counter_player += 1
    elif (player == 'ножницы' and bot =='камень') or (player == 'бумага' and bot == 'ножницы') or (player == 'камень' and bot == 'бумага'):
        print('Побелил Ежик!')
        counter_bot += 1
    else:
         print('Проверь не допустил ли ты ошибок')
         is_broken = True
         break
    print()
    sleep(2)

if is_broken == True:
    print()
else:
    if counter_player > counter_bot:
        print('Счет:', counter_player, ':', counter_bot)
        print('Ты выиграл!')
    elif counter_player == counter_bot:
        print('Счет:', counter_player, ':', counter_bot)
        print('Ничья!')
    else:
        print('Счет:', counter_bot, ':', counter_player)
        print('Выиграл Ежик!')
    sleep(1)
    print()
    print('Ты чувствуешь как проваливаешься в темноту...')
    sleep(4)
    print('На утро, проснувшись от звона будильника')
    sleep(2)
    print('Тебе остается лишь думать, что твой сон был интересным...')
