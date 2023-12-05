import telebot
from os import remove

bot = telebot.TeleBot('5819314697:AAH-oskf-smvY7BOyqqvDOT0ATiA3Mu0BdI')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, ты написал мне /start')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Благодарим вас за использование бота "Повторюшка". \n Данный бот отправляет в ответ все, что вы ему отправите.')
    

@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id, message.text)
    
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    file_id = message.photo[-1].file_id
    print(file_id)
    file_info = bot.get_file(file_id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('image','wb') as new_file:
        new_file.write(downloaded_file)
    photo = open('image', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    remove('image')

    
bot.polling(non_stop = True)
