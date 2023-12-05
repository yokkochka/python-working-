from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

from credits import bot_token

#все что нужно для бота
bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

#первый хэнлер start
def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет! Для поиска информации в wiki отправь команду \n/find запрос")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()