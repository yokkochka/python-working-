from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from credits import bot_token
import os

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def get_data_from_file(day):
    f = open(day, "r", encoding = 'utf-8')
    data = f.read()
    f.close()
    return data

def write_to_wall(update, context):
    wall = open('wall.txt', 'a')
    result = ''
    for arg in context.args:
        result += arg + ' '
    wall.write(str(update.message.from_user['username']) + ": " + result + '\n')
    wall.close()
    
def clear(update, context):
    wall = 'wall.txt'
    os.remove(wall)

def show_wall(update, context):
    try:
        context.bot.send_message(update.effective_chat.id, get_data_from_file("wall.txt"))
    except:
        context.bot.send_message(update.effective_chat.id, 'Доска пуста, напиши на ней что-нибудь! \n (Для этого напиши команду /writewall и через пробел текст)')
        


def get_day(update, context):
    keyboard = [[InlineKeyboardButton("Понедельник", callback_data='1'), InlineKeyboardButton("Вторник", callback_data='2')],
                [InlineKeyboardButton("Среда", callback_data='3'), InlineKeyboardButton("Четверг", callback_data='4')],
                [InlineKeyboardButton("Пятница", callback_data='5'), InlineKeyboardButton("Суббота", callback_data='11')]]
    update.message.reply_text('Выбери день недели', reply_markup=InlineKeyboardMarkup(keyboard))

def get_subj(update, context):
    keyboard = [
        [InlineKeyboardButton("Математика", callback_data='7'),
         InlineKeyboardButton("Русский язык", callback_data='8')],
        [InlineKeyboardButton("Литература", callback_data='9'),
         InlineKeyboardButton("Английский язык", callback_data='10')], ]

    update.message.reply_text('Выбери предмет', reply_markup=InlineKeyboardMarkup(keyboard))

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Это бот для расписания! Ничего не забывай!")

def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Лишь попроси бота, и он поможет тебе с расписанием и некоторыми предметами!")

def help(update, context):
    context.bot.send_message(update.effective_chat.id, "Команды: \n /start - начинает работу бота \n /info - по факту бесполезная функция :3 \n /getsubj - дз по предметам \n /getday - расписание \n /writewall 'какой-то текст' - записывает текст на стену \n /showwall - показать сообщения на стене \n /clear - отчистка стены")

def button(update, context):
    query = update.callback_query
    query.answer()
    
    if query.data == "1":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("mon.txt"))
    elif query.data == "2":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("tue.txt"))
    elif query.data == "3":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("wed.txt"))
    elif query.data == "4":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("thu.txt"))
    elif query.data == "5":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("fri.txt"))
    elif query.data == "7":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("math.txt"))
    elif query.data == "8":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("rus.txt"))
    elif query.data == "9":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("lit.txt"))
    elif query.data == "10":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("eng.txt"))
    elif query.data == "11":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("sat.txt"))  
    else:
        context.bot.send_message(update.effective_chat.id, "Нет такого дня пока что!")

    
button_handler = CallbackQueryHandler(button)
get_subj_handler = CommandHandler('getsubj', get_subj)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
help_handler = CommandHandler('help', help)
clear_handler = CommandHandler('clear', clear)
info_handler = CommandHandler('info', info)
write_to_wall_handler = CommandHandler('writewall', write_to_wall)
show_wall_handler = CommandHandler('showwall', show_wall)
get_day_handler = CommandHandler('getday', get_day)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(clear_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(get_subj_handler)
dispatcher.add_handler(get_day_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(write_to_wall_handler)
dispatcher.add_handler(show_wall_handler)

updater.start_polling()
updater.idle()
