



# user_input = int(input("Введите число: "))

# sum_ch = 0
# while user_input != 0:
#     if (user_input >= 0):
#         sum_ch += user_input
#     else:
#         print("Ошибка ввода. Невозможно посчитать значение суммы. Попробуйте заново")
#         break
#     user_input = int(input("Введите число: "))
# else:
#     print(f"Сумма введенных чисел составляет: {sum_ch}")
    
    
# print(-9 % 7)

# Ф(n) Функция Эйлера - кол-во взаимнопростых пар от 1 до n
# Ф(10) -> 1 3 7 9 -> 4
# Если число(а) простые
# формула для подсчета: Ф(р) = p-1, Ф(pq) = (p-1)(q-1)

# Ф(12) Ф(2*6) = 1 * 2 * 2 = 4
# 1 5 7 11

# print(12 * 30)


# def fi(n):
#     f = n
#     if n%2 == 0:
#         while n%2 == 0:
#             n = n // 2
#         f = f // 2
#     i = 3
#     while i*i <= n:
#         if n%i == 0:
#             while n%i == 0:
#                 n = n // i
#             f = f // i
#             f = f * (i-1)
#         i = i + 2
#     if n > 1:
#         f = f // n
#         f = f * (n-1)
#     return f


# print(fi(85) + fi(33) + fi(27) + (-27%14))

# print(10 * 2 + 18 - 13 + 4 * 16)



# kb = Kb^-1 (mod(Ф(N)))

# N = 7*13
# Ф(N) = (7-1)(13-1) = 6*12 = 72
# Kb=a = 5, kb - ?
# x = a^(-1) mod N
# 5x - 1 = 72y
# y = 1: 5x - 1 = 72
# y = 2: 5x - 1 = 144
        # 5x = 144 + 1
        # x = 145 / 5
        # x = 29



# a = 10
# while a >= 10:
#     print("Больше 10")
#     a = int(input())
#     if (a == 0):
#         break
# else:
#     print("Сработал else")



# import random
# a = ['a', 'b', 'c', 'd', 'e']

# print(random.choice(a))


# print(random.random())

# print(random.randrange(1,3))



# num = 1
# while num < 10:
#     if (num % 3 == 0):
#         num += 1
#         continue
#     print(num)
#     num += 1





# import random

# print(random.randrange(1, 4))


# a = 1
# while a <= 20:
#     if a % 3 != 0:
#         a += 1
#         continue
#     print(a)
#     a += 1




# (№ 6918) (Е. Джобс) Маша выписывает в алфавитном порядке буквенные 
# слова длиной 4 символа, составленные из букв М, А, Р, И, Я. 
# М,А,Р,И,Я -> 5 символов -> 5сс -> 0,1,2,3,4 -> 
# 0 -> A
# 1 -> И
# 2 -> М
# 3 -> Р
# 4 -> Я
# alf = "АИМРЯ"
# Начало списка выглядит так:
# 1. АААА -> 0000
# 2. АААИ -> 0001
# 3. АААМ -> 0002
# 4. АААР -> 0003
# 5. АААЯ -> 0004
# ...
# Какое слово стоит в списке под номером 211?


# 2cc -> алфавит состоит из 2 значений (0, 1)
# 3сс -> 3 значения (0, 1, 2)
# 8сс -> 8 значений (0, .. , 7)
# 16сс -> 16 значений (0, ... , 9, A, B, C, D, E, F)

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ...
# 000, 001, 010, 011, 100, 101, 110, 111 ...
# 000, 001, 002, 010, 011, 012 ... 
 
# alf = "АИМРЯ"

# alf = "01"

# for i in alf:
#     for j in alf:
#         for k in alf:
#             bin_str = i+j+k
#             print(bin_str)

# alf = "АИМРЯ"
# counter = 0
# for i in alf:
#     for j in alf:
#         for k in alf:
#             for l in alf:
#                 counter += 1
#                 str = i + j + k + l
#                 # print(counter, str)
#                 if counter == 211:
#                     print(str)
                    
                    
                    
# (№ 6854) (PRO100-ЕГЭ) Исполнитель 
# Редактор получает на вход строку цифр и преобразовывает её. 
# Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.
# 1. заменить (v, w) -> replace(v, w, 1)
# 2. нашлось (v) -> if v in str:
# 
# Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. 
# Если цепочки v в строке нет, эта команда не изменяет строку. 
# Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
# Дана программа для исполнителя Редактор:
# НАЧАЛО
# ПОКА нашлось (12) ИЛИ нашлось (322) ИЛИ нашлось (222)
#   ЕСЛИ нашлось (12)
#     ТО заменить (12, 2)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (322)
#     ТО заменить (322, 21)
#   КОНЕЦ ЕСЛИ
#   ЕСЛИ нашлось (222)
#     ТО заменить (222, 3)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «1», 
# за которой следуют n цифр «2» (3 < n < 1000). Определите наибольшее возможное 
# количество цифр «2» в строке, 
# которая может быть результатом выполнения программы.

# # 1 2n  (3 < n < 1000)
# max_count_2 = -1
# count_2 = 0
# for n in range(4, 1000):
#     str = "1" + ("2" * n)
#     # print(str)
#     while "12" in str or "322" in str or "222" in str:
#         if "12" in str:
#             str = str.replace("12", "2", 1)
#         if "322" in str:
#             str = str.replace("322", "21", 1)
#         if "222" in str:
#             str = str.replace("222", "3", 1)
#     # print(str)
#     count_2 = str.count("2")
#     # if count_2 > max_count_2:
#     #     max_count_2 = count_2
#     max_count_2 = max(count_2, max_count_2)

# print(max_count_2)


# str = "cat"
# # str[0]
# # 0, 1, 2, 3, 4

# # индексы
# # "cat" -> 3 -> 2

# index = 0
# # len(str)-1  = последний индекс строки
# while index <= len(str) - 1:
#     print(str[index])
#     index += 1


# symbol = "я"
# if symbol == symbol.lower():
#     print("строчной")
# else:
#     print("прописной")



# counter = -1
# flag = 1

# if (counter >= 0):
#     flag = 0
# x

# while counter < 10 and flag == 1:
#     print(counter)
#     counter += 1



from turtle import *
from time import sleep
 
pen = Pen()
pen.goto(0,0)
pen.left(90)
k = 20
for i in range(7):
    pen.forward(10*k)
    pen.right(120)
# print(pen.distance(0, 0))

for i in range(0, 12):
    for j in range(0, 12):
        pen.up()
        pen.goto(i*k,j*k)
        pen.down()
        pen.dot(10//2)

sleep(1000)