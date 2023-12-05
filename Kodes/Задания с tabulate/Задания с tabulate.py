# # Первое задание первый скрин
# from math import *
# x=0
# polozhit = 0
# proizv_otric = 1
# 
# while x <=10:
#     count = sqrt(x+2*x**2) * sin(x)
#     if count > 0:
#         polozhit += 1
#     elif count <0:
#         proizv_otric *= count
#     x+=0.7
# 
# print(f'Произведение отрицательных элементов: {proizv_otric}, оличество положительных: {polozhit}')
    
# 
# 
# 
# Второе задание первый скрин
# from tabulate import tabulate
# from math import *
# 
# data = []
# x = -pi
# index = 0
# 
# max_ch = -100000
# min_ch = 1000000
# 
# while x<=pi:
#     count = round(sin(x),2)
#     if count >= max_ch:
#         max_ch = count
#     elif count <= min_ch:
#         min_ch = count
#     k = [round(x, 2), count]
#     data.append(k)
#     index += 1
#     x += pi/3
#     
# col_names = ["х", "Результат"]
# 
# print(f'Максимальное значение: {max_ch}, минимальное число: {min_ch}')
#   
# # Первый вариант таблицы
# print(tabulate(data, headers=col_names))
# 
# # Второй вариант таблицы
# print(tabulate(data, headers=col_names, tablefmt="grid", showindex="always"))



# # Первое задание второй скрин
# from tabulate import tabulate
# from math import *
# 
# data = []
# x = -5
# index = 0
# sum = 0
# 
# 
# while x<=5:
#     count = x**2-12
#     if 0.5 < count < 4:
#         sum +=count
#     
#     k = [x, count]
#     data.append(k)
#     
#     index += 1
#     x += 0.2
#     
# col_names = ["х", "Результат"]
# 
# print(f'Среднее арифметическое, полученное в соответствии с условием: {sum/index}')
#   
# # Первый вариант таблицы
# print(tabulate(data, headers=col_names))
# 
# # Второй вариант таблицы
# print(tabulate(data, headers=col_names, tablefmt="grid", showindex="always"))
# 




# Второе задание второй скрин

# i = 2
# x = i
# a = 0
# while i <= 10:
#     a += x+5
#     i += 1
# print(f'значение а: {a}')
# 
# i = 2
# b = 1
# while i <= 10:
#     b *= 1-x
#     i += 1
# print(f'значение b: {b}')
# 
# print(f'значение z: {a-2*b}')


















