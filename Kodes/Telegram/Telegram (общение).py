from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


from credits import bot_token

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Приветствую)")

def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Автор бота Юнусова Ульяна")

def message(update, context):
    if update.message.text == "Бот" or update.message.text == "бот":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я знаю это слово - это я!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я пока тебя не совсем понимаю, но скоро научусь")


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
