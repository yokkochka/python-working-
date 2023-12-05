from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from credits import bot_token
from PIL import Image, ImageFont, ImageDraw

def set_meme_text(username, ts, bs):
    img = Image.open(username + "_photo.jpg")
    rgb_img = img.convert("RGB")
    title_font = ImageFont.truetype('arial.ttf', 60)
    width, height = rgb_img.size
    meme = ImageDraw.Draw(rgb_img)
    meme.text(((width / 2 - width / 4), height/4), ts, (0, 0, 0), font=title_font)
    meme.text(((width / 2 - width / 4), height - height / 4), bs, (0, 0, 0), font=title_font)
    rgb_img.save(username + "_meme.jpg")
    
PHOTO = 0
TOP_STRING = 1
BOT_STRING = 2
VIDEO = 3

bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text('Добро пожаловать в генератор мемов!Отпарвьте фото, что бы начать с ним работать!')
    return PHOTO

def photo(update, context):
    user = str(update.message.from_user['username'])
    photo_file = update.message.document.get_file()
    photo_file.download(user + '_photo.jpg')
    update.message.reply_text('Отлично! Теперь добавь верхнюю надпись или отправь /skip если хочешь пропустить этот шаг')
    return TOP_STRING

def top_string(update, context):
    global top_s
    update.message.reply_text('Смешно =) А теперь вводи нижнюю надпись или отправь /skip если хочешь пропустить этот шаг')
    top_s = update.message.text
    return BOT_STRING

def skip_top_string(update, context):
    update.message.reply_text('Тогда пиши что должно быть внизу или отправь /skip если хочешь пропустить этот шаг')
    return BOT_STRING

def bottom_string(update, context):
    user = str(update.message.from_user['username'])
    update.message.reply_text('Лови результат')
    bot_s = update.message.text
    set_meme_text(user, top_s, bot_s)
    sending_img = open(user + "_meme.jpg", "rb")
    context.bot.send_document(update.effective_chat.id, sending_img)
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text('Жаль! Пиши снова, если захочешь повторить!')
    return ConversationHandler.END


start_hendler = CommandHandler('start', start)
photo_handler = MessageHandler(Filters.document.category("image"), photo)
top_string_handler = MessageHandler(Filters.text &amp; ~Filters.command, top_string)
skip_top_string_handler = CommandHandler('skip', skip_top_string)
bottom_string_handler = MessageHandler(Filters.text &amp; ~Filters.command, bottom_string)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(
    entry_points=[start_hendler],
    states={
        PHOTO: [photo_handler],
        TOP_STRING: [top_string_handler, skip_top_string_handler],
        BOT_STRING: [bottom_string_handler]
    }, fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()