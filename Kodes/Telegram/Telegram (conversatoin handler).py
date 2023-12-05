from telegram import ReplyKeyboardMarkup, Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

from credits import bot_token

GENDER = 0
PHOTO = 1
BIO = 2
VIDEO = 3

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


def start(update, context):
    reply_keyboard = [['Мужчина', 'Женщина']]
    update.message.reply_text(
        'Добрый день! Вас приветствует Крупная Компания! Расскажите о себе, вы мужчина или женщина?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return GENDER


def gender(update, context):
    update.message.reply_text(
        'Отлично! Теперь отправьте нам свою фотографию, мы заведем личную карточку, или отправьте /skip если хотите пропустить этот шаг')
    return PHOTO


def photo(update, context):
    user = update.message.from_user
    photo_file = update.message.document.get_file()
    photo_file.download('user_photo.jpg')
    update.message.reply_text(
        'Отлично! Вы сегодня прекрасно выглядите! Теперь отправьте краткое сообщение о себе, или отправьте /skip если хотите пропустить этот шаг')

    return BIO


def skip_photo(update, context):
    update.message.reply_text('Значит без фото! Окей, отправьте краткое сообщение о себе или отправьте /skip.')
    return BIO

def bio(update, context):
    update.message.reply_text(
        'Отлично! Мы получили ваше резюме - теперь в следующем сообщении вы можете отправить видеорезюме или написать /skip, чтобы пропустить этот шаг')
    return VIDEO


def skip_bio(update, context):
    update.message.reply_text(
        'Давайте продолжим без резюме! В следующем сообщении вы можете отправить видеорезюме или написать /skip, чтобы пропустить этот шаг ')
    return VIDEO

def video(update, context):
    user = update.message.from_user
    video_file = update.message.document.get_file()
    video_file.download(user + '_video.mp4')
    update.message.reply_text('Отлично - мы свяжемся с вами!')

    return ConversationHandler.END


def skip_video(update, context):
    update.message.reply_text('Возможно, мы свяжемся с вами!')
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text('Надеюсь вы еще нам напишите - возможно мы нуждаемся именно в вас!')
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
gender_handler = MessageHandler(Filters.regex('^(Мужчина|Женщина)$'), gender)
photo_handler = MessageHandler(Filters.document.category("image"), photo)
skip_photo_handler = CommandHandler('skip', skip_photo)
cancel_handler = CommandHandler('cancel', cancel)
bio_handler = MessageHandler(Filters.text, bio)
skip_bio_handler = CommandHandler('skip', skip_bio)
video_handler = MessageHandler(Filters.document.category("video"), video)
skip_video_handler = CommandHandler('skip', skip_video)
conv_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        GENDER: [gender_handler],
        PHOTO: [photo_handler, skip_photo_handler],
        BIO: [bio_handler, skip_bio_handler],
        VIDEO: [video_handler, skip_video_handler]
    }, fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
