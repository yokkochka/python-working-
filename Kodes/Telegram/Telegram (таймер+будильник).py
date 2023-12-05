from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from credits import bot_token

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def alarm(context):
    job = context.job
    context.bot.send_message(job.context, 'ДЗЗЗЫНЬ! Время прошло')


def set_timer(update, context):
    due = int(context.args[0])
    if due < 0:
        context.bot.send_message(update.effective_chat.id, 'Нельзя ставить таймер меньше 0 секунд')
        return
    context.job_queue.run_once(alarm, due, context=update.effective_chat.id, name=str(update.effective_chat.id))
    context.bot.send_message(update.effective_chat.id, 'Таймер установлен')


set_handler = CommandHandler("set", set_timer)

dispatcher.add_handler(set_handler)

updater.start_polling()
updater.idle()