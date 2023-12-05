from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice

from credits import bot_token

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def validator(update, context):
    user_pass = context.args[0]
    has_digit = False
    for i in range(len(user_pass)):
        if user_pass[i].isdigit():
            has_digit = True
            break
    if len(user_pass) >= 8 and has_digit:
        context.bot.send_message(update.effective_chat.id, 'Ваш пароль безопасен')
    elif len(user_pass) < 8:
        context.bot.send_message(update.effective_chat.id, 'Ваш пароль слишком короткий')
    else:
        context.bot.send_message(update.effective_chat.id, 'В вашем пароле нет цифр')


validator_handler = CommandHandler('validator', validator)

dispatcher.add_handler(validator_handler)



updater.start_polling()
updater.idle()