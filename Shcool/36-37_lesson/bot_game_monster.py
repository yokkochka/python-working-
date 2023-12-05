import telebot
from telebot import types
import random

token = '5819314697:AAH-oskf-smvY7BOyqqvDOT0ATiA3Mu0BdI'
bot = telebot.TeleBot(token)

hp = 0
damage = 0
exp = 0
lvl = 1
monster = ['Филипп', 'Ванженс', 'Сюзи', 'Крилл']

race_database = {
    'Эльф':{'hp':15, 'damage':35},
    'Гном':{'hp':35, 'damage':20},
    'Человек':{'hp':25, 'damage':25}
    }

prof_database = {
    'Лучник':{'hp':25, 'damage':35},
    'Воин':{'hp':50, 'damage':20},
    'Маг':{'hp':15, 'damage':70}
    }

def make_race_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for race in race_database.keys():
        keyboard.add(types.KeyboardButton(text=race))
    return keyboard

def main_menu():
    global hp, damage, exp, lvl
    lvl = 1
    hp = damage = exp = 0
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать игру')
    btn2 = types.KeyboardButton('Об игре')
    
    keyboard.add(btn1, btn2)
    return keyboard

def start_quest():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('В путь!')
    btn2 = types.KeyboardButton('Вернуться в главное меню')
    
    keyboard.add(btn1, btn2)
    return keyboard

def combat():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Атаковать')
    btn2 = types.KeyboardButton('Бежать')
    btn3 = types.KeyboardButton('Вернуться в главное меню')
    
    keyboard.add(btn1, btn2, btn3)
    return keyboard
    
def make_prof_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for prof in prof_database.keys():
        keyboard.add(types.KeyboardButton(text=prof))
    return keyboard

def create_monster():
    rnd_name = random.choice(monster)
    rnd_hp = random.randint(130,155)
    rnd_damage = random.randint(130,170)
    
    return rnd_name, rnd_hp, rnd_damage

@bot.message_handler(commands=['stats'])
def stats(message):
    global hp,damage, exp, lvl
    bot.send_message(message.chat.id, text=f'Здоровье: {hp} \nУрон: {damage} \nОпыт: {exp} \nУровень: {lvl}')
    
    
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Привет, готов поиграть?)', reply_markup=main_menu())

@bot.message_handler(content_types=['text'])
def answer(message):
    global hp,damage, exp, lvl
    victim = create_monster()
    victim = list(victim)
    if (message.text == 'Начать игру'):
        bot.send_message(message.chat.id, text = 'Выберите рассу',reply_markup = make_race_menu())
        
    elif (message.text == 'Об игре'):
        bot.send_message(message.chat.id, text = 'Информация об игре')


    if (message.text == 'Эльф'):
        hp += race_database['Эльф']['hp']
        damage += race_database['Эльф']['damage']
        bot.send_message(message.chat.id, text = f'Вы высокородный Эльф и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию', reply_markup = make_prof_menu())
#         text=f'Вы высокородный Эльф и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию'
#         img = open('elf.jpg', 'rb')
#         bot.send_photo(message.chat.id, img, caption = text, reply_markup = make_prof_menu())
        
    elif (message.text == 'Гном'):
        hp += race_database['Гном']['hp']
        damage += race_database['Гном']['damage']
        bot.send_message(message.chat.id, text = f'Вы великий Гном и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию', reply_markup = make_prof_menu())
#         text = f'Вы великий Гном и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию'
#         img = open('gnom.jpg', 'rb')
#         bot.send_photo(message.chat.id, img, caption = text, reply_markup = make_prof_menu())
#         
    elif (message.text == 'Человек'):
        hp += race_database['Человек']['hp']
        damage += race_database['Человек']['damage']
        bot.send_message(message.chat.id, text = f'Вы бесстрашный герой и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию', reply_markup = make_prof_menu())
#         text = f'Вы бесстрашный герой и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию'
#         img = open('chel.png', 'rb')
#         bot.send_photo(message.chat.id, img, caption = text, reply_markup = make_prof_menu())

    if (message.text == 'Лучник'):
        hp += prof_database['Лучник']['hp']
        damage += prof_database['Лучник']['damage']
        bot.send_message(message.chat.id, text = f'Вы высококлассный лучник, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}. \nВперед к приключениям?)', reply_markup = start_quest())
#         text = f'Вы высококлассный лучник, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}. \nВперед к приключениям?)'
#         img = open('lyk.jpg', 'rb')
#         bot.send_photo(message.chat.id, img, caption = text, reply_markup = start_quest())
        
    elif (message.text == 'Воин'):
        hp += prof_database['Воин']['hp']
        damage += prof_database['Воин']['damage']
        bot.send_message(message.chat.id, text = f'Вы мощный воин, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}. \nВперед к приключениям?)', reply_markup = start_quest())
#         text = f'Вы мощный воин, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}. \nВперед к приключениям?)'
#         img = open('mech.jpg', 'rb')
#         bot.send_photo(message.chat.id, img, caption = text, reply_markup = start_quest())

    elif (message.text == 'Маг'):
        hp += prof_database['Маг']['hp']
        damage += prof_database['Маг']['damage']
        bot.send_message(message.chat.id, text = f'Вы великий маг, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}. \nВперед к приключениям?)', reply_markup = start_quest())
#         text = f'Вы великий маг, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}. \nВперед к приключениям?)'
#         img = open('posoh.jpg', 'rb')
#         bot.send_photo(message.chat.id, img, caption = text, reply_markup = start_quest())


    if (message.text == 'В путь!'):
        event = random.randint(1,2)
        if event == 1:
            bot.send_message(message.chat.id, text='Пока никто не встретился... Идем дальше?', reply_markup = start_quest())
        elif event == 2:
            bot.send_message(message.chat.id, text='А вот и монстр!')
            bot.send_message(message.chat.id, text=f'Ого! Встретился монстр! Монстра зовут {victim[0]}, у него {victim[1]} очков здоровья и вот такой урон: {victim[2]}', reply_markup = combat())
        
        
    elif (message.text == 'Вернуться в главное меню'):
        hp = 0
        damage = 0
        bot.send_message(message.chat.id, text='Вы вернулись в гравное меню', reply_markup = main_menu())
        
    if (message.text == 'Атаковать'):
        victim[1] -= damage
        if victim[1] <= 0:
            if exp >= lvl*30:
                lvl += 1
                hp += 25* lvl
                damage += 15 * lvl
                bot.send_message(message.chat.id, text=f'Твой уровень повысился! Теперь у тебя {lvl} уровень, {hp} очков здоровья и {damage} урона')
            exp += 10*lvl
            bot.send_message(message.chat.id, text=f'Враг повержен! За победу ты получаешь {10*lvl} очков опыта. Теперь у тебя {exp} очков опыта') 
            bot.send_message(message.chat.id, text=f'Продолжаем путешествовать?', reply_markup=start_quest())
        elif victim[1]  > 0:
            bot.send_message(message.chat.id, text='Монстр не умер!')
            hp -= victim[2] 
            bot.send_message(message.chat.id, text=f'Монстр атакует!')
            if hp <= 0:
                
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
                btn1 = 'Вернуться в главное меню'
                keyboard.add(btn1)
                bot.send_message(message.chat.id, text='Победа за монстром', reply_markup=keyboard)
            elif hp>0:
                bot.send_message(message.chat.id, text=f'Теперь у монстра {victim[1]} очков здоровья и {victim[2]} урон, а у тебя {hp} очков здоровья и урон {damage}. Что делать?', reply_markup=combat())
    elif (message.text == 'Бежать'):
        plan = random.randint(1,2)
        if plan == 1:
            damage += 30
            hp += 50
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = 'В путь!'
            btn2 = 'Вернуться в главное меню'
            keyboard.add(btn1, btn2)
            bot.send_message(message.chat.id, text = f'Вы сумели сбежать от монстра! За хорошую стратегию у тебя теперь {hp} очков здоровья и урон {damage}! Продолжаем путешествие?', reply_markup=keyboard)
        elif plan == 2:
            hp -= victim[2]
            bot.send_message(message.chat.id, text = 'О ужас! побег не удался и монстр атакует!')
            if hp<=0:
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = 'Вернуться в главное меню'
                keyboard.add(btn1)
                bot.send_message(message.chat.id, text='Победа за монстром!',reply_markup=keyboard)
            elif hp>0:
                bot.send_message(message.chat.id, text=f'Теперь у монстра {victim[1]} очков здоровья и {victim[2]} урон, а у тебя {hp} очков здоровья. Что будешь делать?', reply_markup= start_quest())
            



bot.polling(non_stop=True)
