
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


def create_monster():
    rnd_name = random.choice(monster)
    rnd_hp = random.randint(130,155)
    rnd_damage = random.randint(130,170)
    
    return rnd_name, rnd_hp, rnd_damage

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton('Начать игру')
    btn2 = types.KeyboardButton('Об игре')
    
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Привет, готов поиграть?)', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    global hp,damage, exp, lvl
    victim = create_monster()
    victim = list(victim)
    if (message.text == 'Начать игру'):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        btn1 = types.KeyboardButton('Эльф')
        btn2 = types.KeyboardButton('Гном')
        
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, text = 'Выберите рассу',reply_markup = keyboard)
        
    elif (message.text == 'Об игре'):
        bot.send_message(message.chat.id, text = 'Информация об игре')


    if (message.text == 'Эльф'):
        hp += 15
        damage += 35
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        btn1 = types.KeyboardButton('Лучник')
        btn2 = types.KeyboardButton('Воин')
        
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, text=f'Вы высокородный Эльф и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию', reply_markup = keyboard)
        
    elif (message.text == 'Гном'):
        hp += 30
        damage += 25
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        btn1 = types.KeyboardButton('Лучник')
        btn2 = types.KeyboardButton('Воин')
        
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, text=f'Вы великий Гном и сейчас ваше здоровье равно:{hp}, а урон равен: {damage}. Осталось выбрать профессию', reply_markup = keyboard)

    if (message.text == 'Лучник'):
        hp += 30
        damage += 45
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        btn1 = types.KeyboardButton('В путь!')
        btn2 = types.KeyboardButton('Вернуться в главное меню')
        
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, text=f'Вы высококлассный лучник, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}. \n Вперед к приключениям?)', reply_markup = keyboard)
        
    elif (message.text == 'Воин'):
        hp += 80
        damage += 50
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        btn1 = types.KeyboardButton('В путь!')
        btn2 = types.KeyboardButton('Вернуться в главное меню')
        
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, text=f'Вы мощный воин, в это значит, что ваше здоровье равно:{hp}, а урон равен: {damage}.  \n Вперед к приключениям?)', reply_markup = keyboard)


    if (message.text == 'В путь!'):
        event = random.randint(1,2)
        if event == 1:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            btn1 = types.KeyboardButton('В путь!')
            btn2 = types.KeyboardButton('Вернуться в главное меню')
            
            keyboard.add(btn1, btn2)
            bot.send_message(message.chat.id, text='Пока никто не встретился... Идем дальше?', reply_markup = keyboard)
        elif event == 2:
            bot.send_message(message.chat.id, text='А вот и монстр!')
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            
            btn1 = types.KeyboardButton('Атаковать')
            btn2 = types.KeyboardButton('Бежать')
            btn3 = types.KeyboardButton('Вернуться в главное меню')
            
            keyboard.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, text=f'Ого! Встретился монстр! Монстра зовут {victim[0]}, у него {victim[1]} очков здоровья и вот такой урон: {victim[2]}', reply_markup = keyboard)
        
        
    elif (message.text == 'Вернуться в главное меню'):
        hp = 0
        damage = 0
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        btn1 = types.KeyboardButton('Начать игру')
        btn2 = types.KeyboardButton('Об игре')
        
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Вы вернулись в гравное меню', reply_markup = keyboard)
        
    if (message.text == 'Атаковать'):
        victim[1] -= damage
        if victim[1] <= 0:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = 'В путь!'
            btn2 = 'Вернуться в главное меню'
            keyboard.add(btn1, btn2)
            exp += 10*lvl
            if exp >= lvl*30:
                lvl += 1
                hp += 25* lvl
                damage += 15 * lvl
                bot.send_message(message.chat.id, text=f'Твой уровень повысился! Теперь у тебя {lvl} уровень, {hp} очков здоровья и {damage} урона')
                exp += 10*lvl
            bot.send_message(message.chat.id, text=f'Враг повержен! За победу ты получаешь {10*lvl} очков опыта. Теперь у тебя {exp} очков опыта') 
            bot.send_message(message.chat.id, text=f'Продолжаем путешествовать?', reply_markup=keyboard)
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
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
                btn1 = 'Атаковать'
                btn2 = 'В путь!'
                btn3 = 'Вернуться в главное меню'
                keyboard.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, text=f'Теперь у монстра {victim[1]} очков здоровья и {victim[2]} урон, а у тебя {hp} очков здоровья. Что делать?', reply_markup=keyboard)
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
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = 'В путь!'
                btn2 = 'Вернуться в главное меню'
                keyboard.add(btn1, btn2)
                bot.send_message(message.chat.id, text=f'Теперь у монстра {victim[1]} очков здоровья и {victim[2]} урон, а у тебя {hp} очков здоровья. Что будешь делать?', reply_markup= keyboard)
            



bot.polling(non_stop=True)