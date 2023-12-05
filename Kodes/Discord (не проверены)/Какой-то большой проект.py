from aiogram import Bot, types, executor

from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.dispatcher.filters import Text

from config import token
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

from random import choice

waiting_rooms = set()
chat_rooms = {}

jokes = ['Как приятно выйти из-за рабочего компьютера после восьми часов работы и усесться, наконец, отдыхать за домашний!', 'Опытный разработчик всегда посмотрит направо и налево, даже если переходит улицу с односторонним движением.', 'Зачем нужно плохое ПО? Без него у многих программистов не будет работы.']
# jokes = ['Как приятно выйти из-за рабочего компьютера после восьми часов работы и усесться, наконец, отдыхать за домашний!', 'Опытный разработчик всегда посмотрит направо и налево, даже если переходит улицу с односторонним движением.', 'Что нужно, чтобы всегда писать хороший код? Представляйте себе, что читать и саппортить ваш продукт будет маньяк-убийца, которому кто-то сказал, где вы живете.', 'Зачем нужно плохое ПО? Без него у многих программистов не будет работы.', 'Основные изменения в новой версии программы: исправлены старые баги, добавлены новые.', 'Не работает код? Не нужно переживать! Если все будет работать, то вы можете оказаться безработным.', 'Главная проблема при работе со штатом программистов: никогда не поймешь, чем заняты сотрудники, пока не окажется, что уже наступил дедлайн.', 'Если вы посмотрите на код, который вы писали более полугода назад, то, скорей всего, вам покажется, что автор – кто-то другой.', 'Если бы строители работали так же, как программисты кодят, то любая птица, присевшая отдохнуть на крыше дома, могла бы стать причиной гибели цивилизации.', 'Существует два вида языков программирования: одни – все ругают, другими не пользуются.']

bot = Bot(token)
dp = Dispatcher(bot)



# Начальная функция старт

@dp.message_handler(commands=['start'])
async def process_start_command(message):
    
    button_search_for_an_interlocutor = KeyboardButton('Поиск собеседника')
    item1 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item1.add(button_search_for_an_interlocutor)

    await message.reply("Привет! Я анонимный чат-бот, нажимай на кнопку и начинай общение! \nЕсли захочешь вернуться обратно, используй команду /menu \n Напоминание! Прежде чем начать новый диалог, убедитесь, что вы вышли из предыдущей чат-комнаты", reply_markup=item1)



# Функция меню
   
@dp.message_handler(commands=['menu'])
async def main_menu_command(message):
    
    menu_topics_for_conversation = KeyboardButton('Вопросы для разговора')
    menu_communication_rules = KeyboardButton('Политика бота')
    
    item2 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item2.add(menu_topics_for_conversation, menu_communication_rules)

    await message.reply("Вы перешли к меню", reply_markup=item2)



# Функция помощь

@dp.message_handler(commands=['help'])
async def help_command(message):
    await message.reply('Держи полный список функционала бота! \n \start - запускает бота, но сначала убедитесь что вы закончили диалог и вышли из "комнаты" \n \help - отправляет памятку использования бота \n \menu - откроет доступные для вас к кнопки')



# Функция рандомных шуток

@dp.message_handler(Text(equals="Шутки от программистов"))
async def process_start_command(message):
    
    my_user_id = message.from_user.id
    another_user_id = chat_rooms[my_user_id]
    global jokes
    a = len(jokes)
    
    if a != 0:
        joke = choice(jokes)
        await bot.send_message(chat_id = my_user_id, text = joke)
        await bot.send_message(chat_id = another_user_id, text = joke)
        jokes.remove(joke)
        
    elif len(jokes) == 0:
        await bot.send_message(chat_id = my_user_id, text = 'Мои шутки закончились, но я могу рассказать их еще раз :3')
        jokes = ['Как приятно выйти из-за рабочего компьютера после восьми часов работы и усесться, наконец, отдыхать за домашний!', 'Опытный разработчик всегда посмотрит направо и налево, даже если переходит улицу с односторонним движением.', 'Зачем нужно плохое ПО? Без него у многих программистов не будет работы.']
#         jokes = ['Как приятно выйти из-за рабочего компьютера после восьми часов работы и усесться, наконец, отдыхать за домашний!', 'Опытный разработчик всегда посмотрит направо и налево, даже если переходит улицу с односторонним движением.', 'Что нужно, чтобы всегда писать хороший код? Представляйте себе, что читать и саппортить ваш продукт будет маньяк-убийца, которому кто-то сказал, где вы живете.', 'Зачем нужно плохое ПО? Без него у многих программистов не будет работы.', 'Основные изменения в новой версии программы: исправлены старые баги, добавлены новые.', 'Не работает код? Не нужно переживать! Если все будет работать, то вы можете оказаться безработным.', 'Главная проблема при работе со штатом программистов: никогда не поймешь, чем заняты сотрудники, пока не окажется, что уже наступил дедлайн.', 'Если вы посмотрите на код, который вы писали более полугода назад, то, скорей всего, вам покажется, что автор – кто-то другой.', 'Если бы строители работали так же, как программисты кодят, то любая птица, присевшая отдохнуть на крыше дома, могла бы стать причиной гибели цивилизации.', 'Существует два вида языков программирования: одни – все ругают, другими не пользуются.']
   
   

# Функция рандомных вопросов/тем для общения

@dp.message_handler(Text(equals="Вопросы для разговора"))
async def topics_for_conversation(message):
    
    my_user_id = message.from_user.id
    
    await bot.send_message(chat_id = my_user_id, text = 'Список вопросов видите только вы')
    await bot.send_message(chat_id = my_user_id, text = '1. Чем ты увлекаешься? Есть ли постоянное хобби? \n 2. Как ты относишься к животным? \n 3. Были ли вы на море, на каком именно? Сколько дней отдыхала? Чем ты там занималась? \n 4. Чем предпочитаешь заниматься в свободное время? \n 5. Кто ты по знаку зодиака и Восточному календарю?')
       

# Политика/правила бота

@dp.message_handler(Text(equals="Политика бота"))
async def communication_rules(message):
    
    my_user_id = message.from_user.id
    
    await bot.send_message(chat_id = my_user_id, text = 'На данный момент политика бота видна только вам')
    await bot.send_message(chat_id = my_user_id, text = '1. Вежливость – не опускайтесь до грубости и откровенного хамства \n 2. Не используйте ненормативную лексику \n 3. Запрещены аудио и видео сообщения, а также обмен фото, это все-таки анонимный чат \n 4. Если собеседник ведет себя неуважительно, то вы можете воспользоваться кнопкой "жалоба", и об этом узнает разработчик бота')
       

# Отправка жалобы

@dp.message_handler(Text(equals="Жалоба"))
async def complaint(message):
    
    my_user_id = message.from_user.id
    another_user_id = chat_rooms[my_user_id]
    author_id = '786957726'
    
    await bot.send_message(chat_id = author_id, text = str(another_user_id) + ' ведет себя не хорошо, ему высылается предупреждение от ' + str(my_user_id))
    await bot.send_message(chat_id = my_user_id, text = 'Ваша жалоба отправлена')
    await bot.send_message(chat_id = another_user_id, text = 'Вам делается замечание и пожелание не повторять больше такого, если продолжите - администратор бота ограничит вам доступ')
    
    objectionable = []
    objectionable.append(another_user_id)
    
    

# Основные функции



# Поиск собеседника

@dp.message_handler(Text(equals="Поиск собеседника"))
async def join_room_handler(message):
    
    my_user_id = message.from_user.id
    
    try:
        another_user_id = waiting_rooms.pop()
        chat_rooms[another_user_id] = my_user_id
        chat_rooms[my_user_id] = another_user_id
        
        button_leave_the_room = KeyboardButton('Покинуть комнату')
        jokes = KeyboardButton('Шутки от программистов')
        topics_for_conversation = KeyboardButton('Вопросы для разговора')
        communication_rules = KeyboardButton('Политика бота')
        complaint = KeyboardButton('Жалоба')
        
        item3 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        item3.add(button_leave_the_room, jokes, communication_rules, topics_for_conversation, complaint)

        
        await bot.send_message(chat_id = my_user_id, text='Собеседник найден, начинайте общение', reply_markup=item3)
        await bot.send_message(chat_id = another_user_id, text='Собеседник найден, начинайте общение', reply_markup=item3)
        
    except KeyError:
        
        if chat_rooms.get(my_user_id) is None:
            waiting_rooms.add(my_user_id)
            await bot.send_message(chat_id = my_user_id, text='Вы в комнате ожидания' )
            
        else:
            await bot.send_message(chat_id = my_user_id, text='Ты не можешь сделать это сейчас' )



# Пкинуть комнату
      
@dp.message_handler(Text(equals="Покинуть комнату"))
async def leave_room_handler(message):
    
    my_user_id = message.from_user.id
    
    try:
        another_user_id = chat_rooms[my_user_id]
        
        del chat_rooms[another_user_id]
        del chat_rooms[my_user_id]
        
        await bot.send_message(chat_id = another_user_id, text = 'Ваш собеседник покинул комнату')
        await bot.send_message(chat_id = my_user_id, text = 'Вы покинули комнату')
        
    except KeyError:
        await bot.send_message(chat_id = my_user_id, text = 'Вы не в чат-комнате')        



# Функция общения

@dp.message_handler()
async def chat_rooms_message_handler(message):
    my_user_id = message.from_user.id
    
    try:
        await bot.send_message(chat_id = chat_rooms[my_user_id], text = message.text)
    except KeyError:
        
        await bot.send_message(chat_id = my_user_id, text = 'Вы не в чат-комнате')


       
if __name__ == '__main__':
    executor.start_polling(dp)

