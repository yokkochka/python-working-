# from easygui import *
# 
# example_str1 = "Все счастливые семьи похожи друг на друга!"
# example_str2 = "Буря мглою небо кроет, вихри снежные крутя..."
# example_str3 = "Батон, буханку, баранку пекарь испек спозаранку"
# 
# str = enterbox("Введите первую строку")
# if str == example_str1:
#     msgbox("Вы все решили правильно")
# else:
#     msgbox("Вы совершили ошибку")
#     
# str2 = enterbox("Введите вторую строку")
# if str2 == example_str2:
#     msgbox("Вы все решили правильно")
# else:
#     msgbox("Вы совершили ошибку")
#     
# str3 = enterbox("Введите третью строку")
# if str3 == example_str3:
#     msgbox("Вы все решили правильно")
# else:
#     msgbox("Вы совершили ошибку")

# from easygui import *
# msg = "Введите информацию о себе"
# title = "Данные о пользователе"
# fieldNames = ["Имя", "Фамилия", "Отчество", "Страна", "Город", "Адрес"]
# fieldValues = []  # мы должны начать с пустого списка для правильной работы метода.
# fieldValues = multenterbox(msg, title, fieldNames)
# # msgbox(fieldValues)
# 
# for i in range(len(fieldValues)):
#     print(fieldValues[i])

from easygui import *
msg = 'Ведите информацию о клиенте банка'
title = 'Расчет кредита'
fieldNames = ['Имя клиента', 'Фамилия клиента', 'Возраст клиента', 'Требуемая сумма', 'Количество лет']
fieldValues = []
fieldValues = multenterbox(msg, title, fieldNames)

if(18 <= int(fieldValues[2]) <= 25 and int(fieldValues[3]) > 100000) or (int(fieldValues[2]) < 18):
    msgbox('В кредите отказано!')
else:
    mont_pay = (int(fieldValues[3]) + 0.05 * int(fieldValues[3])) / int(fieldValues[4])
    msgbox('Ежемесячный платеж: ' + str(mont_pay) + 'рублей')