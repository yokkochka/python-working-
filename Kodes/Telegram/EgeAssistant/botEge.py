from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from EGEAssistant_bot_token import bot_token

ECONOMIC = 0
ECONOMICTASK2 = 1
ECONOMICTASK3 = 2
ECONOMICEND = 3

PROBABILITY = 4
PROBABILITYTASK4 = 5
PROBABILITYTASK5 = 6
PROBABILITYEND = 7

GEOMETRIC = 8
GEOMETRICTASK6 = 9
GEOMETRICTASK7 = 10



bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher



def start(update, context):
   
    keyboard = [[InlineKeyboardButton("Вариант 1", callback_data='1'), InlineKeyboardButton("Вариант 2", callback_data='2')],
                [InlineKeyboardButton("Вариант 3", callback_data='3'), InlineKeyboardButton("Вариант 4", callback_data='4')],
                [InlineKeyboardButton("Вариант демо-версии 2022", url='https://vpr-ege.ru/images/ege/ege2022-ma-demo-pro.pdf')],
                [InlineKeyboardButton("Спецификация", url='https://vpr-ege.ru/images/ege/ege2022-ma-demo-pro-specifikacia.pdf'), InlineKeyboardButton("Кодификатор", url='https://vpr-ege.ru/images/ege/ege2022-ma-demo-kod.pdf')],
                [InlineKeyboardButton("Отработка блоков заданий", callback_data='5')]]
    
    update.message.reply_text("Привет, я бот, созданный для отработки заданий ЕГЭ(математика профиль). Вы можете прорешать варианты ЕГЭ 2021, а так же демо-версию 2022 года. Подробнее о наших функциях в команде '/help'",
                              reply_markup=InlineKeyboardMarkup(keyboard))
    
    
def help(update, context):
    context.bot.send_message(update.effective_chat.id, "Список команд: \n /help - помощь \n /start - вернет в начало к исходной клавиатуре функционала \n /test - запустит алгоритм блоков задач на экономику, вероятность, геометрию \n Внутри алгоритма: \n /next - пропустит блок задач(до того как вы в него войдете) \n /cancel - выход из алгоритма")


def buttons(update, context):
    query = update.callback_query
    query.answer()
    
    if query.data == "1":
        sending_img = open("1_1.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("1_2.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("1_3.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("1_4.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        
    elif query.data == "2":
        sending_img = open("2_1.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("2_2.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("2_3.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("2_4.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        
    elif query.data == "3":
        sending_img = open("3_1.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("3_2.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("3_3.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("3_4.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        
    elif query.data == "4":
        sending_img = open("4_1.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("4_2.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("4_3.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        sending_img = open("4_4.png", "rb")
        context.bot.send_document(update.effective_chat.id, sending_img)
        
    elif query.data == "5":
        context.bot.send_message(update.effective_chat.id, "Чтобы перейти к данному разделу нужна команда /test")
    else:
        context.bot.send_message(update.effective_chat.id, "Я не знаю что ты хочешь, чтобы я сделал")

        
def start_conversation(update, context):
    context.bot.send_message(update.effective_chat.id, "Начнем с блока текстовых экономических задач, введите ответ чтобы узнать правильный и перейти к следующей задаче. Если хотите пропустить весь блок, введите команду /next, для того чтобы выйти из этого раздела введите команду /cancel")
    context.bot.send_message(update.effective_chat.id, "1. Вклад в размере 20 млн рублей планируется открыть на четыре года. В конце каждого года банк увеличивает вклад на 10% по сравнению с его размером в начале года. Кроме того, в начале третьего и четвёртого годов вкладчик ежегодно пополняет вклад на х млн рублей, где х — целое число. Найдите наибольшее значение х, при котором банк за четыре года начислит на вклад меньше 17 млн рублей.")
    return ECONOMIC


def task2(update, context):
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: 24")
    context.bot.send_message(update.effective_chat.id, "2. Миша и Маша положили в один и тот же банк одинаковые суммы под 10% годовых. Через год сразу после начисления процентов Миша снял со своего счета 5000 рублей, а еще через год снова внес 5000 рублей. Маша, наоборот, через год доложила на свой счет 5000 рублей, а еще через год сразу после начисления процентов сняла со счета 5000 рублей. Кто через три года со времени первоначального вложения получит большую сумму и на сколько рублей?")
    return ECONOMICTASK2

def task3(update, context):
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: Маша, на 1100 рублей")
    context.bot.send_message(update.effective_chat.id, "3. Вклад планируется открыть на четыре года. Первоначальный вклад составляет целое число миллионов рублей. В конце каждого года банк увеличивает вклад на 10% по сравнению с его размером в начале года. Кроме этого, в начале третьего и четвёртого годов вкладчик ежегодно пополняет вклад на 3 млн рублей. Найдите наименьший размер первоначального вклада, при котором банк за четыре года начислит на вклад больше 5 млн рублей.")
    return ECONOMICTASK3
    
def end_economic(update, context):
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: 9 млн рублей")
    context.bot.send_message(update.effective_chat.id, "Вы закончили блок экономических задач, введите команду /next чтобы перейти к задачам на вероятность")
    return ECONOMICEND


def skip_answ_economic(update, context):
    context.bot.send_message(update.effective_chat.id, "Данный блок - задачи на вероятность, если забыли команды, введите /help")
    context.bot.send_message(update.effective_chat.id, "1. В кармане у Миши было четыре конфеты — «Грильяж», «Белочка», «Коровка» и «Ласточка», а также ключи от квартиры. Вынимая ключи, Миша случайно выронил из кармана одну конфету. Найдите вероятность того, что потерялась конфета «Грильяж»")
    return PROBABILITY


def task4(update, context):
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: 0.25")
    context.bot.send_message(update.effective_chat.id, "2. На рок-фестивале выступают группы — по одной от каждой из заявленных стран. Порядок выступления определяется жребием. Какова вероятность того, что группа из Дании будет выступать после группы из Швеции и после группы из Норвегии? Результат округлите до сотых")
    return PROBABILITYTASK4

def task5(update, context):
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: 0.33")
    context.bot.send_message(update.effective_chat.id, "3. В некотором городе из 5000 появившихся на свет младенцев 2512 мальчиков. Найдите частоту рождения девочек в этом городе. Результат округлите до тысячных")
    return PROBABILITYTASK5

def end_probability(update, context):
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: 0.498")
    context.bot.send_message(update.effective_chat.id, "Вы закончили блок задач на вероятность, введите команду /next")
    return PROBABILITYEND


def geometric(update, context):
    context.bot.send_message(update.effective_chat.id, "Следующий блок - геометрические задачи, если забыли команды, введите /help")
    context.bot.send_message(update.effective_chat.id, "1. В прямоугольном треугольнике ABC точки M и N — середины гипотенузы AB и катета BC соответственно. Биссектриса угла BAC пересекает прямую MN в точке L. \n а) Докажите, что треугольники AML и BLC подобны. \n б) Найдите отношение площадей этих треугольников, если Cos угла BAC = 7/25")
    return GEOMETRIC


def task6(update, context):
    img = open("geo_task1.png", "rb")
    context.bot.send_document(update.effective_chat.id, img)
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: \n Пункт а на фотографии \n б) 25/36")
    context.bot.send_message(update.effective_chat.id, "2. В правильной четырёхугольной пирамиде SABCD сторона основания AB равна боковому ребру SA. Медианы треугольника SBC пересекаются в точке M. \n а) Докажите, что AM=AD. \n б) Точка N — середина AM. Найдите SN, если AD=6.")
    return GEOMETRICTASK6

def task7(update, context):
    img = open("geo_task2.png", "rb")
    context.bot.send_document(update.effective_chat.id, img)
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: \n Пункт а на фотографии \n б) корень из 15:")
    context.bot.send_message(update.effective_chat.id, "3. Дана правильная шестиугольная пирамида SABCDEF с вершиной S. \n а) Докажите, что плоскость, проходящая через середины рёбер SA и SD и вершину C, делит апофему грани ASB в отношении 2 : 1, считая от вершины S. \n б) Найдите отношение, в котором плоскость, проходящая через середины рёбер SA и SD и вершину C, делит ребро SF, считая от вершины S.")
    return GEOMETRICTASK7


def end_geometric(update, context):
    img = open("geo_task3.png", "rb")
    context.bot.send_document(update.effective_chat.id, img)
    context.bot.send_message(update.effective_chat.id, "Правильный ответ: \n Пункт а на фотографии \n б) 1/2")
    context.bot.send_message(update.effective_chat.id, "Вы закончили блок геометрических задач, на этом все :3")
    return ConversationHandler.END


def help(update, context):
    update.message.reply_text('Список команд: \n /help - помощь \n /start - вернет в начало к исходной клавиатуре функционала \n /test - запустит алгоритм блоков задач на экономику, вероятность, геометрию \n Внутри алгоритма: \n /next - пропустит блок задач(до того как вы в него войдете) \n /cancel - выход из алгоритма')



def cancel(update, context):
    update.message.reply_text('Вы завершили тестовые задания')
    return ConversationHandler.END



task2_handler = MessageHandler(Filters.text, task2)
task3_handler = MessageHandler(Filters.text, task3)
task4_handler = MessageHandler(Filters.text, task4)
task5_handler = MessageHandler(Filters.text, task5)
task6_handler = MessageHandler(Filters.text, task6)
task7_handler = MessageHandler(Filters.text, task7)

end_economic_handler = MessageHandler(Filters.text, end_economic)
end_probability_handler = MessageHandler(Filters.text, end_probability)
end_geometric_handler = MessageHandler(Filters.text, end_geometric)



help_handler = CommandHandler('help', help)
start_conversation_handler = CommandHandler('test', start_conversation)
skip_answ_economic_handler = CommandHandler('next', skip_answ_economic)
geometric_handler = CommandHandler('next', geometric)

cancel_handler = CommandHandler('cancel', cancel)





conv_handler = ConversationHandler(
    entry_points=[start_conversation_handler],
    states={
        ECONOMIC: [skip_answ_economic_handler, task2_handler, help_handler],
        ECONOMICTASK2: [task3_handler, help_handler],
        ECONOMICTASK3: [end_economic_handler, help_handler],
        ECONOMICEND: [skip_answ_economic_handler, help_handler],
        PROBABILITY: [geometric_handler, task4_handler, help_handler],
        PROBABILITYTASK4: [task5_handler, help_handler],
        PROBABILITYTASK5: [end_probability_handler, help_handler],
        PROBABILITYEND: [geometric_handler, help_handler],
        GEOMETRIC: [task6_handler, help_handler],
        GEOMETRICTASK6: [task7_handler, help_handler],
        GEOMETRICTASK7: [end_geometric_handler, help_handler],
    }, fallbacks=[cancel_handler])


dispatcher.add_handler(conv_handler)

dispatcher.add_handler(CallbackQueryHandler(buttons))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))



updater.start_polling()
updater.idle()