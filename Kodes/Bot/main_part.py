from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from credit import bot_token

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def info(update, context):
    context.bot.send_message(update.effective_chat.id, "")
    
    
    
info_handler = CommandHandler('info', info)    


dispatcher.add_handler(info_handler)


updater.start_polling()
updater.idle()