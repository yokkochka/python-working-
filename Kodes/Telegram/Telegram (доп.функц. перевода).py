from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice

from credits import bot_token


bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
dictionary = {"Яблоко": "Apple", "Груша": "Pear", "Банан": "Banana", "Киви": "Kiwi", "Абрикос": "Apricot", "Персик": "Peach", "Апельсин": "Orange", "Лайм": "Lime", "Манго": "Mango", "Слива": "Plum"}


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Приветствую)")
    context.bot.send_message(update.effective_chat.id, "Так же вы можете использать команды: /info и /roll, последняя выдаст рандомное число от 1 до 6 для игры в кубики, добавлена новая команда: /joke, она выдает рандомную шутку, а если вы напишите слова категории фрукты, то бот скажет вам из перевод на английский язык")

def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Автор бота Юнусова Ульяна")

def roll(update, context):
    numbers = [1, 2, 3, 4, 5, 6]
    num = choice(numbers)
    context.bot.send_message(chat_id=update.effective_chat.id, text=num)
    
def joke(update, context):
    jokes = ['Как приятно выйти из-за рабочего компьютера после восьми часов работы и усесться, наконец, отдыхать за домашний!', 'Опытный разработчик всегда посмотрит направо и налево, даже если переходит улицу с односторонним движением.', 'Что нужно, чтобы всегда писать хороший код? Представляйте себе, что читать и саппортить ваш продукт будет маньяк-убийца, которому кто-то сказал, где вы живете.', 'Зачем нужно плохое ПО? Без него у многих программистов не будет работы.', 'Основные изменения в новой версии программы: исправлены старые баги, добавлены новые.', 'Не работает код? Не нужно переживать! Если все будет работать, то вы можете оказаться безработным.', 'Главная проблема при работе со штатом программистов: никогда не поймешь, чем заняты сотрудники, пока не окажется, что уже наступил дедлайн.', 'Если вы посмотрите на код, который вы писали более полугода назад, то, скорей всего, вам покажется, что автор – кто-то другой.', 'Если бы строители работали так же, как программисты кодят, то любая птица, присевшая отдохнуть на крыше дома, могла бы стать причиной гибели цивилизации.', 'Существует два вида языков программирования: одни – все ругают, другими не пользуются.']
    k = choice(jokes)
    context.bot.send_message(chat_id=update.effective_chat.id, text=k)
    
def translator(update, context):
    key = str(update.message.text)
    if key in dictionary:
        context.bot.send_message(chat_id=update.effective_chat.id, text=dictionary[key])
    elif update.message.text == "Бот" or update.message.text == "бот":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я знаю это слово - это я!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я пока тебя не совсем понимаю, но скоро научусь")

def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, "Я не знаю эту команду")


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
roll_handler = CommandHandler('roll', roll)
joke_handler = CommandHandler('joke', joke)
translator_handler = MessageHandler(Filters.text, translator)
unknown_handler = MessageHandler(Filters.command, unknown)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(roll_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(translator_handler)
dispatcher.add_handler(unknown_handler)



updater.start_polling()
updater.idle()