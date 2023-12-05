from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler

from credits import bot_token

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет!")


start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
