# x = [0,1,2,3,4,5,6,7,8,9]
# res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# x1 = x[1::2]
# x2 = x[-2::-2]

# count_x2 = 0
# count_x1 = 0
# for i in range(len(x)):
#     if i % 2 == 0:
#         res[i]=x2[count_x2]
#         count_x2+=1
#     else:
#         res[i]= x1[count_x1]
#         count_x1+=1
    
# # print(res)
# book = "Harry Potter"
# book2 = "Kolobok"
# book3 = "Rusalochka"
# print("За лето девочка прочитала ", book, "а затем ей в школе порекомендовали", book2, ". Она ее прочитала и \
#       захотела прочитать еще и ", book3)

# print(f"за лето девочка прочитала {book}, а затем ей в школе порекомендовали {book2}. Она ее прочитала и \
#       захотела прочитать еще и {book3}")



# elements = {"quote": [], "title": [], "year": []}

# string = "'May the Force be with you,' — 'Star Wars', 197.%'The first rule of Fight Club is: you do not talk about Fight Club' — 'Fight Club', 1999.%'I see you' — 'Avatar', 2009."
# # Разрезаем строку по сиволу одинарной кавычки, формируем из этих подстрок список
# string = string.split("'")
# # Удаляем самый первый элемент, т.к. он будет пустым
# del string[0]
# # Получаем следующий список
# # ['May the Force be with you,', ' — ', 'Star Wars', ', 197.%', 'The first rule of Fight Club is: you do not talk about Fight Club', ' — ', 'Fight Club', ', 1999.%', 'I see you', ' — ', 'Avatar', ', 2009.']
# # На каждую цитату из фильма + название фильма + год выхода фильма приходится 4 элемента списка (учитывается тире между)
# # Проходимся по нему(по каждому его элементу)
# for i in range(len(string)):
#     # Если это первый элемент из четверки
#     if i % 4 == 0:
#         # Определяем цитату
#         quote = ''
#         # Проходимся по всей цитате
#         for j in string[i]:
#             # Если символ буква или пробел
#             if j.isalpha() or j == " ":
#                 # Добавляем этот символ
#                 quote += j
#         # В конце заносим сформированную цитату в словарь
#         elements["quote"].append(quote)
#     # Если это 3 элемент четверки, то это название фильма, делаем то же самое
#     elif i % 4 == 2:
#         title = ''
#         for j in string[i]:
#             if j.isalpha() or j == " ":
#                 title += j
#         elements["title"].append(title)
#     # Если это 4 элемент четверки, то это год
#     elif i % 4 == 3:
#         year = ''
#         for j in string[i]:
#             if j.isdigit():
#                 year += j
#         # Добавляем в словарь в типе данных int
#         elements["year"].append(int(year))

# # Просится не делать вывод, но он тут есть, чтобы проверить правильность
# # Можно удалить строку или закомментировать
# print(elements)






# restaurants = {
#     "Alice": {"Pizza Hut": "++", "Tokyo City": "++", "Beer House": "+"},
#     "Bob": {"Pizza Hut": "+", "Tokyo City": "+", "Beer House": "++"},
#     "Charlie": {"Pizza Hut": "--", "Tokyo City": "+", "Beer House": "++"}
# }

# def calculate_score(preference):
#     # Функция для преобразования предпочтений в баллы
#     if preference == "++":
#         return 2
#     elif preference == "+":
#         return 1
#     elif preference == "-":
#         return -1
#     elif preference == "--":
#         return -2
#     else:
#         return 0  # Обработка других случаев (если есть)

# def calculate_restaurant_score(restaurant_preferences):
#     # Функция для расчета общего балла для ресторана
#     return sum([calculate_score(pref) for pref in restaurant_preferences.values()])

# def find_best_restaurant(restaurants):
#     best_score = float("-inf")  # Начальное значение лучшего балла
#     best_restaurant = ""  # Начальное значение лучшего ресторана

#     for restaurant_name, preferences in restaurants.items():
#         score = calculate_restaurant_score(preferences)
#         # Обновляем лучший ресторан, если текущий ресторан имеет более высокий балл или имеет равный балл, но больше "++" оценок
#         if score > best_score or (score == best_score and preferences.get("++", 0) > restaurants[best_restaurant].get("++", 0)):
#             best_score = score
#             best_restaurant = restaurant_name

#     return best_restaurant

# best_restaurant = find_best_restaurant(restaurants)

# print("Лучший ресторан:", best_restaurant)






# def calculate_score(preference):
#     # Функция для преобразования предпочтений в баллы
#     if preference == "++":
#         return 2
#     elif preference == "+":
#         return 1
#     elif preference == "-":
#         return -1
#     elif preference == "--":
#         return -2
#     else:
#         return 0  # Обработка других случаев (если есть)



# restaurants = {
#     "Alice": {"Pizza Hut": "++", "Tokyo City": "++", "Beer House": "+"},
#     "Bob": {"Pizza Hut": "+", "Tokyo City": "+", "Beer House": "++"},
#     "Charlie": {"Pizza Hut": "--", "Tokyo City": "+", "Beer House": "++"}
# }

# # Получаем список названий ресторанов
# restaurant_names = list(restaurants["Alice"].keys())
# # Сортируем для того, чтобы если при совпадении баллов выводился первый в алфавитном порядке
# restaurant_names = sorted(restaurant_names)

# # Создаем доп. словарь для сохранения статистики того, сколько баллов у каждого рестарана
# dop_restaurants = {}

# for i in restaurant_names:
#     dop_restaurants[i] = 0

# # После этого мы получаем словарь такого вида
# # {'Pizza Hut': 0, 'Tokyo City': 0, 'Beer House': 0}


# # Проходимся по всем людям
# for user, ratings in restaurants.items():
#     # Проходимся по каждому рестарану
#     for restaurant, rating in ratings.items():
#         # Вычисляем изменение балла
#         dop_restaurants[restaurant] += calculate_score(rating)
        
# # Вычисляем значение максимального балла
# max_ball = max( dop_restaurants.values())

# # Проходимся словарю и ищем совпадение максимального балла
# for name, balls in dop_restaurants.items():
#     if balls == max_ball:
#         best_restaurant = name
#         break


# # Можно убрать, значение сохраняется в переменной best_restaurant
# print(best_restaurant)







# import re

# def report_refiner(report, **filters):
#     lines = report.split('\n')
#     result = []

#     direction_type = filters.get('type')

#     for line in lines:
#         if direction_type == 'interview' and 'interview' in line:
#             # Parse interview report
#             name_match = re.search(r'Name: (\w+)', line)
#             age_match = re.search(r'Age: (\d+)', line)
#             gender_match = re.search(r'Gender: (\w+)', line)
#             phone_match = re.search(r'Phone: (\+7-\d{1}-\d{3}-\d{2}-\d{2})', line)

#             if name_match and age_match and gender_match and phone_match:
#                 name = name_match.group(1)
#                 age = int(age_match.group(1))
#                 gender = gender_match.group(1)
#                 phone = phone_match.group(1)

#                 # Apply filters
#                 if ('minimum_age' not in filters or age >= filters['minimum_age']) and \
#                    ('gender' not in filters or gender == filters['gender']):
#                     result.append({'name': name, 'age': age, 'gender': gender, 'phone number': phone})

#         elif direction_type == 'market' and 'market' in line:
#             # Parse market research report
#             company_match = re.search(r'Company: (\w+)', line)
#             url_match = re.search(r'URL: (\S+)', line)
#             income_match = re.search(r'Income: (\d+)', line)
#             profit_match = re.search(r'Profit: (\d+)', line)
#             tin_match = re.search(r'TIN: (\d+)', line)

#             if company_match and url_match and income_match and profit_match and tin_match:
#                 company_name = company_match.group(1)
#                 url = url_match.group(1)
#                 income = int(income_match.group(1))
#                 profit = int(profit_match.group(1))
#                 tin = int(tin_match.group(1))

#                 # Apply filters
#                 if ('minimum_profitability' not in filters or (income > 0 and profit/income >= filters['minimum_profitability'])) and \
#                    ('region' not in filters or tin_match and tin_match.group(1).startswith(filters['region'])):
#                     result.append({'company name': company_name, 'url': url, 'income': income, 'profit': profit, 'TIN': tin})

#     return result

# # Пример использования функции с фильтрами
# report_example = """
# Interview Report
# Name: John
# Age: 30
# Gender: Male
# Phone: +7-9хх-ххх-хх-хх

# Market Research Report
# Company: ABC Inc.
# URL: http://abc.com
# Income: 100000
# Profit: 20000
# TIN: 123456789012
# """

# result = report_refiner(report_example, type='interview', minimum_age=25, gender='Male')
# print(result)

# result = report_refiner(report_example, type='market', minimum_profitability=0.2, region='123')
# print(result)


# import matplotlib.pyplot as plt
# import numpy as np

# # Значения импульсной характеристики
# n = np.array([0, 1, 2])
# h_n = np.array([3/4, 5/4, 5.3/4])

# # Построение графика
# plt.stem(n, h_n, basefmt='b', markerfmt='bo', linefmt='b-')
# plt.title('Импульсная характеристика')
# plt.xlabel('n')
# plt.ylabel('h[n]')
# plt.grid(True)
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np

# # Значения импульсной характеристики
# n = np.arange(0, 10)
# h_n = (1/4) * (2/3)**n - (1/4) * (3/2)**n

# # Построение графика
# plt.stem(n, h_n, basefmt='b', markerfmt='bo', linefmt='b-')
# plt.title('Импульсная характеристика')
# plt.xlabel('n')
# plt.ylabel('h[n]')
# plt.grid(True)
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np

# # Частоты для анализа
# omega = np.linspace(0, 2*np.pi, 1000)

# # Передаточная функция
# H = (3 + 5*np.exp(-1j*omega) + 5.3*np.exp(-2j*omega)) / (4*np.exp(-2j*omega) + 8*np.exp(-1j*omega) + 4)

# # АЧХ и ФЧХ
# magnitude = np.abs(H)
# phase = np.angle(H, deg=True)  # в градусах

# # Построение графиков
# plt.figure(figsize=(12, 6))

# # АЧХ
# plt.subplot(2, 1, 1)
# plt.plot(omega, magnitude)
# plt.title('АЧХ')
# plt.xlabel('Частота (рад/с)')
# plt.ylabel('|H(jω)|')
# plt.grid(True)

# # ФЧХ
# plt.subplot(2, 1, 2)
# plt.plot(omega, phase)
# plt.title('ФЧХ')
# plt.xlabel('Частота (рад/с)')
# plt.ylabel('Фаза (градусы)')
# plt.grid(True)

# plt.tight_layout()
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# # Частоты для анализа
# omega = np.linspace(0, 2*np.pi, 1000)

# # Передаточная функция
# H = (1 + 3*np.exp(-1j*omega)) / (6.4 + 9*np.exp(-1j*omega) + 6*np.exp(-2j*omega))

# # АЧХ и ФЧХ
# magnitude = np.abs(H)
# phase = np.angle(H, deg=True)  # в градусах

# # Построение графиков
# plt.figure(figsize=(12, 6))

# # АЧХ
# plt.subplot(2, 1, 1)
# plt.plot(omega, magnitude)
# plt.title('АЧХ')
# plt.xlabel('Частота (рад/с)')
# plt.ylabel('|H(jω)|')
# plt.grid(True)

# # ФЧХ
# plt.subplot(2, 1, 2)
# plt.plot(omega, phase)
# plt.title('ФЧХ')
# plt.xlabel('Частота (рад/с)')
# plt.ylabel('Фаза (градусы)')
# plt.grid(True)

# plt.tight_layout()
# plt.show()


# n = int(input("Введите четырехзначное число: "))
# summa = (n//1000) + (n% 1000 // 100) + (n % 100 // 10) + (n % 10)

# if 0 <= summa <= 9:
#     print("Минимальный ранг") 
# elif 10 <= summa <= 18:
#     print("Малый ранг") 
# elif 19 <= summa <= 27:
#     print("Средний ранг") 
# elif 28 <= summa <= 36:
#     print("Высший ранг") 


# # filsbmvqelk
# # ebiil

# alf = 'abcdefghijklmnopqrstuvwxyz'
# stroka = input("Введите зашифрованную строку: ")

# # print(alf[alf.find("o")-3])
# for i in stroka:
#     print(alf[alf.find(i)+3], end="")

# summa = 0
# .... 
# summa += 1


# import numpy as np
# import matplotlib.pyplot as plt
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# # Задаем временной ряд
# temperatures = np.array([25, 28, 30, 29, 27, 24, 22])

# # Строим ACF и NACF
# # plot_acf(temperatures, lags=6, title='Autocorrelation Function (ACF)')
# # plt.show()

# plot_pacf(temperatures, lags=2, title='Partial Autocorrelation Function (PACF)')
# plt.show()




# n= int(input('Введите кол-во учеников: '))
# spisok = []

# for i in range(n):
#     spisok.append(input("Введите ФИ и оценки по 3 предметам: ").strip())

# sr_m = 0
# sr_f = 0
# sr_i = 0

# for i in range(n):
#     dop = spisok[i].split()
#     print(dop)
#     sr_m += int(dop[2])
#     sr_f += int(dop[3])
#     sr_i += int(dop[4])


# # print(sr_m/n, sr_f/n, sr_i/n)



# stroka = 'sshdff'
# counter = 0
# for i in stroka:
#     if i == 'f':
#         counter += 1

# print(counter)

test = 101