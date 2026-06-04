
# # a = int(input("Введите а: "))
# # b = int(input("Введите b: "))

# # # 1 вариант решения
# # c = 0
# # if a % 2 == 1:
# #     a += 1

# # for i in range(a, b + 1, 2):
# #     # print(i)
# #     c += 1
# # print(c)

# # # 2 вариант решения
# # c = 0
# # for i in range(a, b + 1):
# #     if i % 9 == 0:
# #         c += 1

# # print(c)



# # summa = 0
# # for i in range(5):
# #     number = int(input("Введите число: "))
# #     if abs(number) % 4 == 0 and abs(number) % 10 == 6:
# #         summa += number

# # print(summa)




# # n = int(input("Введите количество чисел последовательности: "))
# # c = 0
# # for i in range(n):
# #     number = int(input("Введите число: "))
# #     if number % 3 == 0 and number % 10 == 2:
# #         c += 1

# # print(c)





# # n = int(input("Введите кол-во чисел последовательности: "))
# # c = 0
# # for i in range(n):
# #     number = int(input("Ввиедите число: "))
# #     if number % 10 == 9: 
# #         c += 1
# # print(c)





# # # n = int(input("Число проехавших автомобилей: "))

# # # max_speed = -1
# # # min_speed = 301
# # # c = 0

# # # for i in range(n):
# # #     number = int(input("Ввиедите скорость: "))
# # #     if number > max_speed:
# # #         max_speed = number
# # #     if number < min_speed:
# # #         min_speed = number
# # #     if number <= 30:
# # #         c += 1


# # # print(max_speed - min_speed)
# # # print(c)




# # # a1 = 55
# # # a2 = 83
# # # a3 = 91

# # # # a1 = hex(a1)
# # # # a2 = oct(a2)
# # # # a3 = bin(a3)



# # # # print(a1, a2, a3)







# # # # print("abcdefghijklmnopqrstuvwxyz"[::-1])

# # # punctuation = ".,?!&$#(&$*#&$(#))"

# # # def test(x):
# # #     return list_names.count(x)

# # # with open("", 'r', encoding='utf-8') as file:
# # #     list_names = []
# # #     for i in file:
# # #         for j in punctuation:
# # #             i = i.replace(j, "")
# # #         i = i.split(" ")
# # #         for j in i:
# # #             if j[0].isupper():
# # #                 list_names.append(j)
    
# # #     print(', '.join(sorted(list(set(list_names)))))
# # #     print("Чаще всего упоминается: ", key = test)


# # # random, time, datetame, math


# # import random as rnd

# # print(rnd.randrange(1,10))


# # s = "hello"

# # a = s[::-1]
# # print(a)

# # s = "hello world"
# # a = s[len(s) - 1]
# # print(a)

# # a1 = 'acac'
# # a2 = 'hdjhj'

# # print(a1 + a2)


# # a1 = 'a1'
# # a2 = 5

# # print(a1 * a2)



# # s = "hello world"

# # print(s[1:5:2])

# # a = input()
# # print(a[-1])


# # a = "cat"

# # print(a + "dog")

# # print(a * 3)


# # s = "****hell**o w**orld***"
# # print(s.strip("*"))

# # s = "python. java. c++"

# # print(s.split(". "))


# # s = "hello world"

# # print(s.replace("l", "a", 1))


# s = "hello world"
# print(s.count("ll"))


# s = "12312.3"

# if s.isdigit() :
#     print("Строка состоит из цифр")
# else:
#     print("Строка не состоит только из цифр")


# s = "hdgfh65456gf"

# if s.isalpha():
#     print("Строка состоит из букв")
# else:    
#     print("Строка не состоит только из букв")


# s = "hsgHGHGHGHGHGfh"

# if s.islower():
#     print("Строка состоит из строчных букв")
# else:
#     print("Строка не состоит только из строчных букв")


# s = 'JfhJHJH'

# if s.isupper():
#     print("Строка состоит из заглавных букв")
# else:
#     print("Строка не состоит только из заглавных букв")


# s = "hello world"

# print(s.split())



# lst = ["asdfh", 2, 3, 4, 5]

# print(len(lst))


# cities = ["Москва", "Питер", "Казань", "Новосибирск"]

# can = "can be"
# empty = "empty"
# other = "other"

# city = input("Введите город: ")
# weight = float(input("Введите вес: "))

# if city in cities and weight % 100 == 0:
#     print(can)
# elif city in cities and weight % 100 != 0:
#     print(empty)
# else:
#     print(other)


# names = input("Введите имена через запятую и пробел: ").split(', ')
# # print(names)


# name = input("Введите имя: ")

# if name not in names:
#     names.append(name)

# a = tuple(names)

# print(a)


# Автомат обрабатывает натуральное число N по следующему алгоритму:

# Строится двоичная запись числа N.
# К полученной записи дописываются разряды по следующему принципу: если число 
# чётное, то справа дописывается 10, если нечётное – слева дописывается 1 и справа 00.
# Результат переводится в десятичную систему и выводится на экран.
# В результате работы автомата на экране появилось число, большее 107.

# Для какого наименьшего N данная ситуация возможна?
# В ответе найденное число N запишите в десятичной системе.

# for n in range(1, 100):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r + '10'
#     else:
#         r = '1' + r + '00'
#     r = int(r, 2)
#     # print(r)
#     if r > 107:
#         print(f'Результат n: {n}')
#         break

# print('x y w z f')
# alf = [0, 1]
# for x in alf:
#     for y in alf:
#         for w in alf:
#             for z in alf:
#                 f = ((z == w) and (not(x) or y) or not w)
#                 if f == 0:
#                     print(x, y, w, z, f)

# alf = sorted("ВЕСНА")
# # print(alf)
# counter = 0
# for i in alf:
#     for j in alf:
#         for k in alf:
#             for l in alf:
#                 word = i + j + k + l
#                 counter += 1
#                 # if 'Е' not in word and 'АА' not in word:
#                 #     print(counter, word)
#                 #     exit()

#                 if word.count('Е') == 0 and word.count("АА") == 0:
#                     print(counter, word)
#                     exit()
 


# def f():
#     p = 5
#     q = 7
#     return (p-1) * (q-1)


# e = 11

# for d in range(1, 40):
#     if (d * e) % f() == 1:
#         print(d)



# import turtle

# p = turtle.Pen()
# p.speed(100)

# # p.up()
# # p.forward(100)
# # p.down()
# # p.backward(200)
# # p.right(90)
# # p.forward(100)
# # p.left(90)
# # p.forward(100)

# k = 23

# for i in range(3):
#     p.forward(12 * k)
#     p.left(270)
#     p.backward(10 * k)
#     p.right(90)

# p.up()
# p.fd(6 * k)
# p.rt(90)
# p.backward(4 * k)
# p.lt(90)

# p.down()
# for i in range(4):
#     p.forward(16 * k)
#     p.right(270)
#     p.forward(8 * k)
#     p.right(270)


# for x in range(-10, 15):
#     for y in range(-10, 10):
#         p.up()
#         p.goto(x * k, y * k)
#         p.down()
#         p.dot(3)

# turtle.done()     



# alf = "0123456789AB"

# for x in alf:
#     number1 = '154' + x + '3'
#     number2 = '1' + x + '365'

#     number1 = int(number1, 12)
#     number2 = int(number2, 12)

#     res = number1 + number2
#     if res % 13 == 0:
#         print(res / 13)



# with open(r"C:\Users\yokko\Downloads\13.txt", 'r') as file:
#     lst = [int(i) for i in file]
#     lst = list(map(int, file.read().split()))
    
#     print(lst)




# # обычный цикл while
# a = 0
# while a < 10:
#     a += 1
#     print(a)

# # пример бесконечного цикла
# while True:
#     print("hello")


# Вводить значения от пользователя пока он не ввел 0 (0 - это признак окончания последовательности)
# while True:
    # num = int(input("Введите числа: "))
    # if num == 0:
    #     break

# summa = 0
# while True:
#     num = int(input("Введите числа: "))
#     if num == 0:
#         break
#     summa += num
# print(summa)

# for переменной in последовательности 

# если последовательность есть
# s = "hello"
# s = ['a', 'b', 'ahsgdh', '2534', 234]
# for i in s:
#     print(i)

# если ее нет -> нужно ее сгенерировать
# for i in range(5):
#     print(i)


# n = int(input("ВВедите кол-во"))
# for i in range(n):
#     number = int(input("Номер: "))

# for i in range(10, 1, -1):
#     print(i)


# lst = []
# while True:
#     s = input()
#     if s == "END":
#         break
#     s = s.split(":")
#     # print(s)

#     name = s[0]
#     price = int(s[1])

#     if price > 500:
#         lst.append(name)
    
# print(lst)



# companies = input().split(" ")
# # print(companies)
# days = input().split(" ")
# # print(days)

# new_days = []
# for i in days:
#     new_days.append(int(i))
# # print(new_days)

# mean_value = sum(new_days) / len(new_days)

# for i in range(0, len(companies)):
# #0





s = 'autentification'

# len_s = len(s)
# print(4)

# print(s[-2])



# a = s[::-1]

# print(a)
# d = s.replace('a','r',1)
# s = '****hgfhgsd****hfghd****'

# d = s.strip("*")

# print(d)



# s = "1 2 3 4"

# d = s.split("*")

# print(d)



# s = "hellllo"
# print(s.count('ll'))


# s = "123123"

# if s.isdigit():
#     print("yes")
# if s.isalpha():
#     print("letters")



# 'ca' + '12' = "ca12"

# text = input()

# cat -> 0a0
# ""
# "0"
# "0a"
# "0a0"

# res_str = ""

# for i in range(0, len(text)):
#     # print(i)
#     if i % 2 == 0:
#         res_str += '0'
#     else:
#         res_str += text[i]
# print(res_str)


# s = "hello"
# s = ['cat', 'dog', '1', 'sdjhgfh']
# for i in s:
#     print(i.upper())

# lst = []

# lst.append(1)
# lst.append(3)
# lst.append(10)
# lst.append(-1)

# print(lst)

# sort()
# sorted()

# lst.sort(reverse = True)

# lst = sorted(lst, reverse = True)
# print(a)
# print(lst)

# def dop(x):
#     return x.count('a')


# lst = ['cat', 'pi', 'autentification', 'python']

# a = sorted(lst, key = dop, reverse = True)
# print(a)

# def dop(x):
#     return x[1]

# s = {"milk":50, "bread":30, "oil":70, 'avocado':100}

# # print(s.items())

# a =dict(sorted(s.items(), key = dop, reverse = True))
# print(a)

# s = (1,2,3,[5,6,8])
# s[3][2] = 10
# print(s)

# s = set()

# s.add(4)
# s.add(6)
# s.add(8)
# print(s)

# s.discard(8)
# print(s)



# s = set(input())

# print(s)

# s= [1,1,1,1,2,3]
# s= list(set(s))
# print(s)


# |
# &
# ^
# -










# a = int(input())

# # lst.remove(3)
# del lst[0]

# print(lst)








# while True:
#     s = input()
#     if s == 'END':
#         break

#     s = s.split(":")
#     name = s[0]
#     price = int(s[1])
#     if price > 500:
#         lst.append(name)
# print(name)




























# 1

# lst = []

# lst.append(1)
# lst.append(10)
# lst.append(-1)
# print(lst)

# lst.remove()
# print(lst)

# del lst[0]
# print(lst)


# # sort()
# # sorted()

# def test(x):
#     return x.count("a")

# a = ["Pi", "appleaaa", "autentification", 'cat']
# s = sorted(a, key = test, reverse = True)
# print(s)
# print(a)

# # a.sort(key = test, reverse = True)
# # print(lst)


# # dict
# s = {'one':1, 'two':2, 'three':3}

# print(s['one'])

# s = {"user1":'+79shdfgsdhfg', 'hdsgfh':'+797234673'}

# k = list(s.keys())
# print(k)

# v = list(s.values())
# print(v)

# print(s.items())

# k, v = (1, 2)
# print(k, v)

# s = {'comp5':1000, 'comp2':500, 'comp3':1500}
# s['comp4'] = 200
# print(s)

# if 1000 in s.values():
#     print('yes')


# deliv = int(input())

# # # вывести названия компаний, чья доставка дороже deliv
# for k, v in s.items():
#     if v > deliv:
#         print(k)

# def test(x):
#     return x[1]

# # [('one', 1), ('two', 2), ('three', 3)]
# a = dict(sorted(s.items(), key = test))
# print(a)


# 125 / 100 = 1.25
# 125 // 100 = 1
# 125 % 100 = 25


# a = float(input())
# print((a + a) * 2)
# print(a * a)

# 125
# a = float(input())

# m = a // 100
# a = a % 100
# d = a // 10
# s = a % 10
# print(m, "м", d, "дм",  s, "см")


# a = input()

# m = a[0:-2]
# d = a[-2]
# s = a[-1]

# print(m, "м", d, "дм",  s, "см")

# distance = float(input())
# count = float(input())
# price = float(input())

# litrov = (count * distance) / 100

# all_price = litrov * price * 2
# print("Стоимость поездки на дачу и обратно:", all_price)


# a = input()
# if a == '1' or a == 'направо':
#     print('Коня потеряешь')
# elif a == '2' or a == 'налево':
#     print("Голову сложишь")
# elif a == '3' or a == 'вперед':
#     print('Невесту найдешь')



# print(abs(-18) % 10)




# n = input()
# sm = 0
# i = 0
# while i < len(n):
#     sm += int(n[i])
#     i += 1

# print(sm)


# a = int(input())
# n = int(input())

# res = 1

# while n > 0:
#     res *= a
#     n -= 1

# print(res)



# 3 3x3

# от 1 до 9

# 0 0 0 
# 0 0 0
# 0 0 0


# 1 2 3
# 8 9 4
# 7 6 5


# s = input()
# lst_ord = [ord(i) for i in s]
# ind_min = lst_ord.index(min(lst_ord))
# ind_max = lst_ord.index(max(lst_ord))
# print(s[ind_min], s[ind_max])


# s = "hello world0246246"

# # s.count()
# a = s.count('0') + s.count('2') + s.count('4') + s.count('6') + s.count('8')

# print(a)?

# s.replace("element", "new_element", 1)

# s = "hello world"
# s = s.replace('l', '*', 1)
# print(s)


# s.strip()
# s = "******hello**world******"
# s = s.strip("*")
# print(s)


# # s= input("Введите строку:")
# s = "hello;world;python;java"
# s = s.split(';')
# print(s)


# s = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if n % 4 ==0 and n % 10 == 2:
#         s += n
# print(s)



# not_suitable = "Посмотрим другие переменные"
# p = input()
# price = int(input())

# if price < 1000:
#     print(f"Точно берем {p}!")
# else:
#     print(not_suitable)

# summa = 0
# while True:
#     s = input()
#     if s == 'конец':
#         break
#     s = s.split(", ")
#     if s[0] == 'сестра':
#         summa += int(s[2])

# print(summa)



# names = input().split(", ")
# prices = input().split(", ")
# n = int(input())

# for i in range(0, len(names)):
#     if int(prices[i]) <= n:
#         print(names[i])
#         n -= int(prices[i])




# import turtle
# import math

# p = turtle.Pen()
# turtle.bgcolor('black')
# p.speed(100)


# # n % 7 = 0,1,2,3,4,5,6 

# # n % 4 = 0,1,2,3 
# # n % 3 = 0,1,2
# # n % 2 = 0,1
 

# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# num_angels = 6
# angle = 360 / num_angels


# for i in range(300):
#     index = i % len(colors)
#     p.color(colors[index])
#     p.forward(math.sqrt(i) * 10)
#     p.right(angle)
#     # p.right(angle + 1)



# turtle.done()





# f = 4

# t = f"Сегодня у меня было {f} уроков"

# print(t)



# a = 'abcdefghijklmnopqrstuvwxyz'
# string = input(" ")
# string1 = ""
# for i in string:
#     k = a.find(i)
#     k = k + 3
#     if k > 26:
#         k %= 26
#     # print(k, string)
#     string1 += string[k]
# print(string1)


# import pandas as pd

# df = pd.read_excel(r'C:\Users\yokko\Downloads\f\9.ods', engine='odf')


# with open(r'C:\Users\yokko\Downloads\f\10.odt') as file:
#     data = file.read()
# #     print(data.count("то") + data.count("То"))


# import turtle

# p = turtle.Pen()
# p.speed(100)
# # p.forward(180)
# # p.right(90)
# # print(p.heading())
# # print(p.xcor(), p.ycor())
# k = 20
# p.right(180)
# # p.forward(k*2)
# p.right(90)
# # p.forward(k*40)
# p.right(90)
# # p.forward(2*k)

# for i in range(4):
#     p.circle(-5*k, 180)

# for x in range(-6, 10):
#     for y in range(-11, 5):
#         p.up()
#         p.goto(k * x, k* y)
#         p.down()
#         p.dot(4)


# turtle.done()




# s = '10010010.10000000.00000000.00000000'
# for i in s.split('.'):
#     print(int(i, 2), end = ".")


# print(int('10111111', 2))



# dict
# d = {'one':'один', 'two':"два", 'three':'три'}

# d_key = list(d.keys())
# print(d_key)

# d_value = list(d.values())
# print(d_value)

# print(d.items())
# a, b = (1, 2)
# print(a)
# print(b)

# d = {'coffee':450, 'milk':100, 'bread':60}
# money = 500

# for k, v in d.items():
#     if money > v:
#         print(k)
#         money -= v


# print("x y w z f")
# alf = [0, 1]
# for x in alf:
#     for y in alf:
#         for w in alf:
#             for z in alf:
#                 f = ((not(x) or y) == (not(y) or z)) and (y or w)
#                 if f == True:
#                     print(x, y, w, z, f)
#                 # print(x,y,w,z)

# 0 0 0 0
# 0 0 0 1
# 0 0 1 0
# 0 0 1 1
# 0 1 0 0
# 0 1 0 1
# 0 1 1 0
# 0 1 1 1





# for n in range(100, 100000):
#     lst = []
#     n = str(n)
#     for i in range(len(n) - 2):
#         lst.append(int(n[i] + n[i+1] + n[i+2]))
#     max_v = max(lst)
#     min_v = min(lst)
#     r = max_v - min_v
#     if r == 415:
#         print(n)
#         break



# alf = "ABCDX"
# count = 0

# for i in alf:
#     for j in alf:
#         for k in alf:
#             for l in alf:
#                 word = i + j + k + l
#                 if word[0] == 'X' and word.count('X') == 1 or word.count('X') == 0:
#                     count += 1
# print(count)






# alf = "ВИНТ"


# count = 0
# for i in alf:
#     for j in alf:
#         for k in alf:
#             for l in alf:
#                 for m in alf:
#                     word = i + j + k + l + m
#                     count += 1
#                     # print(count, word)
#                     if count == 1019:
#                         print(count, word)
#                         exit()






# import turtle
# ts = turtle.Screen()
# ts.bgcolor('red')
# ts.setup(width=400, height=400)

# p = turtle.Pen()

# # p.up()
# # p.forward(200)
# # p.down()
# # p.forward(200)


# p.goto(-300, 300)

# p.home()

# turtle.done()

# print(chr(16 + 64))

# s = "Python is fun!"
# res_s = ""

# for i in s:
#     if i.isalpha():
#         o = str(ord(i.upper()) - 64)
#     else:
#         o = i
#     res_s += o

# print(res_s)


# n = int(input())

# for i in range(1, n + 1):
#     print(i * "*")


# a000
# s = input()
# summa = 0
# for i in s:
#     if i.isdigit():
#         summa += int(i)
    
# if summa == 0 and s.count('0') == 0:
#     print('Цифр нет')
# else:
#     print(summa)


# s = input()

# s = s.replace(' ', '_').replace('.', '').replace(',', '')
# print(s)


# s = input().split()
# a = []

# for i in s:
#     # d = i[0].upper() + i[1:]
#     d = i.capitalize()
#     a.append(d)

# print(' '.join(a))



# n = int(input())

# matr = []

# for i in range(n):
#     m = []
#     for j in range(n):
#         m.append(0)
#     matr.append(m)

# print(matr)

def output(matr, n, m):
    for i in range(n):
        for j in range(m):
            print(f"{matr[i][j]:^3}", end = ' ')
        print()

# x = 0
# y = 0
# number = 1
# # 1 - вправо, 2 - вниз, 3 - влево, 4 - вверх
# flag_move = 1
# wall_left = -1
# wall_bottom = n
# wall_right = n
# wall_top = 0

# try: 
#     while number <= n**2:
#         # output(matr)
#         # print()

#         matr[x][y] = number
        
#         if flag_move == 1 and y + 1 == wall_right:
#             flag_move = 2
#             wall_right -= 1
#         elif flag_move == 2 and x + 1 == wall_bottom:
#             wall_bottom -= 1
#             flag_move = 3
#         elif flag_move == 3 and y - 1 == wall_left:
#             wall_left += 1
#             flag_move = 4
#         elif flag_move == 4 and x - 1 == wall_top:
#             flag_move = 1
#             wall_top += 1


#         if flag_move == 1:
#             y += 1
#         elif flag_move == 2:
#             x += 1
#         elif flag_move == 3:
#             y -= 1
#         elif flag_move == 4:
#             x -= 1

#         number += 1
    
# except Exception as e:
#     print(e)

# finally:
#     output(matr)


# n = int(input())
# m = int(input())

# matr = []
# for i in range(n):
#     s = input().split()
#     d = [int(j) for j in s]
#     matr.append(d)

# output(matr, n, m)

# k, l = input().split()
# k = int(k)
# l = int(l)

# for stroka in range(n):
#     a = matr[stroka][k]
#     matr[stroka][k] = matr[stroka][l]
#     matr[stroka][l] = a

# output(matr, n,m)









# n = input().split()
# # n_new = []
# # # print(n)
# # for i in n:
# #     n_new.append(int(i))

# # print(n_new)



# n = list(map(int, n))
# print(n)





# 14.1
# import sys
# sys.set_int_max_str_digits(0)

# def ten_to_other(n, osn):
#     alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     res = ''
#     while n > osn:
#         ost = n % osn
#         res += alf[ost]
#         n = n // osn
#     res += alf[n]
#     return res[::-1]




# r = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
# r = ten_to_other(r, 27)
# # more_9  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# c = 0
# for i in r:
#     if i > '9':
#         c += 1
# print(c)    



# 14.2

# alf = "0123456789ABCDEFGHIJKLMNOPQRS"

# for x in alf:
#     n1 = "923" + x + '874'
#     n2 = '524' + x + "6152"
#     n1 = int(n1, 29)
#     n2 = int(n2, 29)
#     res = n1 + n2
#     if res % 28 == 0 and x == 'R':
#         print(res / 28)



# 14.3
# bin() - > 2
# hex() - > 16
# oct() - > 8

# def ten_to_other(n, osn):
#     alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     res = ''
#     while n > osn:
#         ost = n % osn
#         res += alf[ost]
#         n = n // osn
#     res += alf[n]
#     return res[::-1]



    
# for x in range(1, 3001):
#     res = 9 * 11 ** 210 + 8 * 11 ** 150 - x
#     res = ten_to_other(res, 11)
#     # print(res)
#     if res.count("0") == 60:
#         print(x)



# def G(n):
#     if n >= 10:
#         return G(n - 2)
#     else:
#         return 2 * n

# def F(n):
#     return 2 * (G(n - 3) + 8)

# print(F(15548))

# "key" : "value"

# G = {'one' : 1, 'two' : 2}
# print(G['one'])

# G = {}

# for n in range(100000):
#     if n < 10:
#         G[n] = 2 * n
#     else:
#         G[n] = G[n - 2] + 1

# print(2 * (G[15548 - 3]) + 8)


# def F(n):
#     if n == 0:
#         return 0
#     elif n> 0 and n % 2 == 0:
#         return F(n / 2)
#     elif n % 2 == 1:
#         return 1 + F(n-1)
    

# c = 0
# for n in range(1, 1001):
#     if F(n) == 3:
#         c += 1
# print(c)





# def F(n):
#     # if n == 1:
#     #     return 1
#     # elif n == 2:
#     #     return 2

#     if n == 1 or n == 2:
#         return n
#     elif n > 2 and n % 2 == 0:
#         return int( (3 * n + F(n - 3)) / 3 )
#     elif n > 2 and n % 2 != 0:
#         return int( (7 * n + F(n - 1) - F(n - 2)) / 5 )

# print(F(35))



# s = ["cat", 'dog', 'lake', 'fox', 'autentification']

# lst = [len(i) for i in s]

# print(lst)


# "FILM, 90, 200"

# while True:
#     s = input()
#     if s == "СТОП":
#         break
#     s = s.split(", ")
#     if int(s[1]) > 50 and int(s[2]) > 200:
#         print(s[0])





# import turtle


# p = turtle.Pen()
# p.circle(80)


# p.backward(100)


# p.dot(100)



# # p.hideturtle()
# # ts = turtle.Screen()
# # ts.bgcolor('cyan')
# # p.fillcolor('red')

# # p.begin_fill()
# # for i in range(4):
# #     p.forward(200)
# #     p.right(90)
# # p.end_fill()

# # p.showturtle()

# turtle.done()



# s = [i for i in range(1, 11) if i % 2 == 0]

# s = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         s.append(i)


# print(s)

# # n =   # Сколько элементов послежовательности будет
# s = [int(input()) for i in range(int(input())  )]

# # index_first_otric = [1 if i < 0 else 0 for i in s].index(1)

# a = int(input())
# b = int(input())

# r = [i for i in s if not(a <= i <= b)]
# r += [0] * (len(s) - len(r))


# print(r)


# # for i 
# #     fhjhsgdhf




# s = input().split(" ")

# d = [i.count('0') + i.count('1') + i.count('2') + i.count('3') + i.count('4') + i.count('5') + i.count('6') + i.count('7') + i.count('8') + i.count('9') for i in s]

# max_val = -1
# word_max_val = ""
# min_val = 100000000
# word_min_val = ""

# for i in range(len(s)):
#     if d[i] > max_val:
#         max_val = d[i]
#         word_max_val = s[i]
#     if d[i] < min_val:
#         min_val = d[i]
#         word_min_val = s[i]


# word_max_val = s[d.index(max(d))]
# word_min_val = s[d.index(min(d))]


# print(d)
# print(word_max_val)
# print(word_min_val)




# s = input().split()

# d = [ sum([int(j)for j in i if j.isdigit()]) for i in s ]

# word_max_val = s[d.index(max(d))]
# word_min_val = s[d.index(min(d))]

# print(d)
# print(word_max_val)
# print(word_min_val)



# a = int(input())

# # a = a + 1
# a -= 5

# print(a)


# print(9/3)


# a = -25

# a = abs(a)
# print(a)



# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r + '10'
#     else:
#         r = '1' + r + '00'
#     r = int(r,2)
#     if r > 107:
#         print(n)
#         break


# res = 11.25 + 20.75
# print(res)

# print(hex(32)[2:])



# alf = [0, 1]
# print("x y w z f")
# for x in alf:
#     for y in alf:
#         for w in alf:
#             for z in alf:
#                 # print(x, y, w, z)
#                 f = (z == w) and (not(x) or y) or not(w)
#                 if f == False:
#                     print(x, y, w, z, f)



# from itertools import product

# a = product(sorted("ВЕСНА"), repeat = 4)
# c = 0

# for i in a:
#     s = "".join(i)
#     c += 1
#     if "Е" not in s and "АА" not in s:
#         print(c, s)
#         break





# print(f"{bin(192)[2:]}.{bin(168)[2:]}.{bin(108)[2:]}.{bin(157)[2:]}")
# print(f"{bin(255)[2:]}.{bin(255)[2:]}.{bin(255)[2:]}.{bin(192)[2:]}")

# print(int('10000000', 2))


# p = 5
# q = 7
# e = 11

# for d in range(1, 40):
#     if (d * e) % ((p-1) * (q-1)) == 1:
#         print(d)


# one_number = (10 * 1024 * 1024 * 1024) / 4635815 
# print(one_number) 

# d = (int(one_number) * 8) / 2468
# print(d)



# import turtle

# p = turtle.Pen()
# p.speed(100)
# k = 35

# for i in range(3):
#     p.forward(12 * k)
#     p.left(270)
#     p.backward(10 * k)
#     p.right(90)

# p.up()

# p.forward(6 * k)
# p.right(90)
# p.backward(4 * k)
# p.left(90)

# p.down()

# for i in range(4):
#     p.forward(16 * k)
#     p.right(270)
#     p.forward(8 * k)
#     p.right(270)


# for x in range(-1, 8):
#     for y in range(-1, 8):
#         p.up()
#         p.goto(x * k, y * k)
#         p.down()
#         p.dot(3)


# alf = "0123456789AB"
# for x in alf:
#     n1 = '154' + x + '3'


# turtle.done()


# alf = "0123456789AB"
# for k in alf:
#     for j in alf:
#         for i in alf:
#             number = k + j + i
#             print(number)



# alf = [0, 1]
# print("x y w z f")

# for x in alf:
#     for y in alf:
#         for w in alf:
#             for z in alf:
#                 f = not(not(w) or y) or (not(z) or x) or not(z)
#                 if f == True:
#                     f = 1
#                 else:
#                     f = 0
#                 print(x, y, w, z, f)


# # print([0] * 5)

# # 1 if i < 0 else 0 - тернальный оператор
# # значение_если_истина УСЛОВИЕ ИНАЧЕ значение_если_ложь

# # [9,2,-3,-4,1,-2] -> [0,0,1,1,0,1]

# lst = [float(input()) for i in range(int(input()))]

# index_first_otr = [1 if i < 0 else 0 for i in lst].index(1)
# summa = sum([abs(lst[i]) for i in range(index_first_otr + 1, len(lst))])

# a = float(input("Введите а: "))
# b = float(input("Введите b: "))

# res = [i for i in lst if not(a <= i <= b)] 
# res = res + [0] * (len(lst) - len(res))

# not(x% A == 0)
# x % A != 0

# print(lst)
# print(index_first_otr)
# print(summa)
# print(res)



# for A in range(1, 200):
#     if all((x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0)) for x in range(1, 200)):
#         print(A)



# for A in range(1, 200):
#     count = 0
#     for x in range(1, 200):
#         if ((x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))) == 1:
#             count += 1
#     if count == 199:
#         print(A)



# for A in range(1, 200):
#     if all( ((x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0)) )  for x in range(1, 200)):
#         print(A)



# # print(-18 % 5)


# for A in range(1, 2000):
#     if all(((x % A != 0) <= ((x % 10 == 0) <= (x % 12 != 0)))   for x in range(1, 200)):
#         print(A)



# print( 12 & 6)



# for A in range(0, 200):
#     if all(((x & A != 0) <= ((x & 10 == 0) <= (x & 3 != 0))) for x in range(0, 200)):
#         print(A)



# for A in range(0, 200):
#     if all((((x & 28 != 0) or (x & 45 != 0)) <= ((x & 17 == 0) <= (x & A != 0))) for x in range(0, 200)):
#         print(A)


# for A in range(0, 200):
#     if all(((x & 33 == 0) <= ((x & 45 != 0) <= (x & A != 0))) for x in range(0,200)):
#         print(A)
        # break



# for A in range(0, 200):
#     if all(((2*x + 3 * y > 30) or (x + y <= A) ) for x in range(0, 200) for y in range(0, 200)):
#         print(A)
#         break



# # for x in range(0,10):
# #     for y in range(0, 10):

# # print([(x, y) for x in range(0, 10) for y in range(0, 10)])



# for A in range(0, 200):
#     if all(((3 * x + 4 * y != 70) or (A > x) or (A > y)) for x in range(0, 200) for y in range(0, 200)):
#         print(A)
#         break


# d  = [y for x in (18, 91, 3, 43, 72, 115) for y in (x, x + 0.1, x - 0.1)]

# # print(d)
# r = []
# for a1 in d:
#     for a2 in d:
#         # print(a1, a2)
#         if a2 >= a1 and all(((18 <= x <= 91) <= ((not(3 <= x <= 43)) <= (((not(72<= x <= 115)) and (not(a1 <= x <= a2))) <= (not(18 <= x <= 91)))))   for x in d):
#             # r.append(a2 - a1)
#             # "2" + '3' -> '23'
#             # [2,3,4] + [5,6] -> [2,3,4,5,6]
#             r += [a2 - a1]
# print(round(min(r)))




# d = [y for x in (130, 171, 150, 185) for y in (x, x + 0.1, x - 0.1)] 
# r = []    # создаем список

# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all(((130 <= x <= 171) <= (((150 <= x <= 185) and (not(a1 <= x <= a2))) <= (not(130 <= x <= 171)))) for x in d):
#             r.append(a2 - a1)


# print(round(min(r)))




# d = [y for x in (10, 40, 5, 15, 35, 50) for y in (x, x+0.1, x-0.1)]

# r = []


# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all((((a1 <= x <= a2) or (10 <= x <= 40)) or ((5 <= x <= 15) <= (35 <= x <= 50))) for x in d):
#             r.append(a2 -a1)

# print(round(min(r)))




# lst = [1,2,3,-2,0,1,0,2]


# stroka = input()
# bukv = input()


# if stroka.startswith(bukv) and len(stroka) > 5:
#     print("Подходит")
# else:
#     print("Что-то не так")



# озеро (зе) -> 1

# print(stroka.find(bukv))
# if stroka.find(bukv) == 0 and len(stroka) > 5:
#     print("Подходит")
# else:
#     print("Что-то не так")



# len_bukv = len(bukv)

# if stroka[0:len_bukv] == bukv and len(stroka) > 5:
#     print("Подходит")
# else:
#     print("Что-то не так")



# for i in range(0,len(bukv)):
#     if stroka[i] != bukv[i]:
#         print("Что-то не так")
#         break
# else:
#     print("Подходит")






# alf = "0123456789AB"

# for x in alf:
#     n1 = '154' + x + '3'
#     n2 = '1' + x + "365"

#     n1 = int(n1, 12)
#     n2 = int(n2, 12)

#     res = n1 + n2

#     if res % 13 == 0:
#         print(res / 13)



# with open(r"C:\Users\yokko\Downloads\13 (1).txt") as file:
#     data = [int(i) for i in file]

# n = min([i for i in data if abs(i) % 15 != 0])
# c = []
# for i in range(0, len(data) - 1):
#     if abs(data[i]) % n == 0 and abs(data[i+1]) % n == 0:
#         # c.append(data[i] + data[i+1])
#         c += [data[i] + data[i+1]]

# print(len(c), max(c))




# a = input("Введите строку: ")

# if len(a) > 5 and not a.isdigit():
#     print("Да")
# else:
#     print("Нет")



# b = input("Введите строку: ").lower()

# b = b.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*').replace('y', '*')

# if b.count("**") == 0:
#     print("Нет")
# else:
#     print("Да")

    



# a = 10
# b = 4

# a, b = b, a
# print(a, b)


# with open(r"C:\Users\yokko\Desktop\DEMO_17.txt") as file:
#     # используется тогда, когда данные в файле записаны через пробел
#     # data = list(map(int, file.read().split()))
#     # print(data)

#     # используется тогда, когда данные в файле записаны через перенос строки (в столюик)
#     data = [int(i) for i in file]

# # нахождение мин двухзначное через цикл
# # min_dvuznach = float("inf")
# # for i in data:
# #     if i > 9 and i < 100 and i < min_dvuznach:
# #         min_dvuznach = i

# # print(min_dvuznach)

# # нахождение мин двухзначного через генератор списков
# min_dvuznach = min([i for i in data if i > 9 and i < 100])
# # print(min_dvuznach)

# res = []

# for i in range(0, len(data) - 1):
#     # print(data[i], data[i + 1])
#     first = data[i]
#     second = data[i + 1]
#     count = 0
#     if first > 9 and first < 100:
#         count += 1
#     if second > 9 and second < 100:
#         count += 1

#     if count == 1 and (first + second) % min_dvuznach == 0:
#         res.append(first + second)


# print(len(res), max(res))


# # print(data)



# когда пары и порядок следования элементов не важен

# with open(r"C:\Users\yokko\Downloads\17.txt") as file:
#     data = [int(i) for i in file]

# # print(data)

# res = []
# for i in range(0, len(data) - 1):
#     for j in range(i + 1, len(data)):
#         # print(i, j)
#         first = data[i]
#         second = data[j]
#         if (first + second) % 117 == 0:
#             res.append(first + second)

# print(len(res), max(res))



# в случае если тройки не идущих подряд элементов

# with open(r"C:\Users\yokko\Downloads\17 (1).txt") as file:
#     data = [int(i) for i in file]


# res = []
# for i in range(0, len(data)):
#     for j in range(i + 1, len(data)):
#         for k in range(0, len(data)):
#             if k != i and k != j:
#                 first = data[i]
#                 second = data[j]
#                 third = data[k]

        

# s = [float(input()) for i in range(int(input()))]


# # 1
# # s_1_0 = len(s) - [1 if i <= -1 else 0 for i in s][::-1].index(1) - 1

# # 2
# r = [i for i in s if i <= -1][-1]
# index_last_otr = s.index(r)

# print("w x y z f")
# alf = [0, 1]

# for w in alf:
#     for x in alf:
#         for y in alf:
#             for z in alf:
#                 f = not(w) or ((not(z) or y) and x)
#                 print(w, x, y, z, f)



# a = 26 + 26 **2 + 26 ** 3 + 26 ** 4 + 26 ** 5

# b = (5 * 26 ** 5 + 3 * 26 ** 4 + 4 * 26 ** 3 + 2 * 26 **2 + 1 * 26) + 1

# print(a + b)


# print('Мой любимый сериал - "Декстер"')
# print("Мой любимый сериал - 'Декстер'")


# print("Мой любимый сериал - \"Декстер\"")



# print('1',2,"3",4, sep = "*")
# print(1, end= ' ')
# print(2)
# print(3)



# print("gdgf \t hgdsjfhg jshgdfh \n\n")


# import turtle
# import random

# p = turtle.Pen()


# # p.left(180)

# # p.right(30)
# # print(p.heading())

# # p.setheading(150)
# # p.write("Hello world", font = ("Arial", 40))


# x = random.randint(-300, 300) 
# y = random.randint(-300, 300)

# p.goto(x, y)

# print(p.xcor(), p.ycor())

# turtle.done()

#  1 вариант

# alf = "УЧЕНИК"
# count = 0
# for i in alf:
#     for j in alf:
#         for k in alf:
#             for t in alf:
#                 for y in alf:
#                     word = i + j + k + t + y
#                     if word[0] == 'У' and word[4] == 'К':
#                         count += 1
#                         # print(word)

# print(count)

# #  2 вариант

# alf = "УЧЕНИК"
# res = []
# for i in alf:
#     for j in alf:
#         for k in alf:
#             for t in alf:
#                 for y in alf:
#                     word = i + j + k + t + y
#                     if i == 'У' and y == 'К':
#                         res.append(word)
#                         # print(word)

# print(len(res))


# alf = sorted("АЛГОРИТМ")
# print(alf)
# counter_2 = 0
# # alf = "АГИЛМОРТ"
# count = 0
# for i in alf:
#     for j in alf:
#         for k in alf:
#             for t in alf:
#                 for y in alf:
#                     word = i + j + k + t + y
#                     count += 1
#                     if count % 2 != 0 and i != 'Г' and word.count('И') >= 2:
#                         counter_2 += 1
                        
# print(counter_2)



# alf = "0123456"
# counter = 0
# for x in alf:
#     for y in alf:
#         for z in alf:
#             for c in alf:
#                 number = x + y + z + c
#                 if int(x) > int(y) > int(z) > int(c):
#                     counter += 1

# print(counter)



# if '32' > '101':
#     print("yes")
# else:
#     print('No')


                    




# alf = '0123456789ABCDEF'
# even = '02468ACE'
# counter = 0
# for x in alf:
#     for y in alf:
#         for z in alf:
#             for c in alf:
#                 number = x + y + z + c

#                 new_number = number.replace('0', '*')
#                 new_number = new_number.replace('2', '*')
#                 new_number = new_number.replace('4', '*')
#                 new_number = new_number.replace('6', '*')
#                 new_number = new_number.replace('8', '*')
#                 new_number = new_number.replace('A', '*')
#                 new_number = new_number.replace('C', '*')

#                 # print(new_number)


#                 if number.count('E') == 1 and "*E" not in new_number and "E*" not in new_number and "EE" not in new_number:
#                     # print(number)
#                     counter += 1

# print(counter)



# alf = '0123456789ABCDEF'
# even = '02468ACE'
# counter = 0
# for x in alf:
#     for y in alf:
#         for z in alf:
#             for c in alf:
#                 number = x + y + z + c

#                 index_E = number.find('E')
#                 if number.count("E") == 1 and index_E == 0 and number[1] not in even:
#                     counter += 1
#                 elif number.count("E") == 1 and index_E == 3 and number[2] not in even:
#                     counter += 1
#                 elif number.count("E") == 1 and number[index_E - 1] not in even and number[index_E + 1] not in even:
#                     counter += 1
# print(counter)




# with open(r"C:\Users\yokko\Desktop\Новый текстовый документ.txt") as file:
#     data = [[int(j) for j in i.replace('\n', "").split("\t")] for i in file]

# print(data)

# for i in data:
#     print()


# alf = "012345"
# counter = 0
# for x in alf:
#     for y in alf:
#         for z in alf:
#             number = x + y + z
#             if int(x) >= int(y) >= int(z):
#                 counter += 1
# print(counter)




# alf = '0123456789'
# counter = 0

# for x in alf:
#     for y in alf:
#         for z in alf:
#             for c in alf:
#                 number = x + y + z + c

#                 even_numer = number.replace('0', "*")
#                 even_numer = even_numer.replace('2', "*")
#                 even_numer = even_numer.replace('4', "*")
#                 even_numer = even_numer.replace('6', "*")
#                 even_numer = even_numer.replace('8', "*")

#                 odd_number = number.replace('1', "*")
#                 odd_number = odd_number.replace('3', "*")
#                 odd_number = odd_number.replace('5', "*")
#                 odd_number = odd_number.replace('7', "*")
#                 odd_number = odd_number.replace('9', "*")

#                 if number.count(x)== 1 and number.count(y) == 1 and \
#                     number.count(z) == 1 and number.count(c) == 1 and \
#                         "**" not in even_numer and "**" not in odd_number:
#                             counter += 1
                    


# print(counter)


# alf = sorted("ПОЛИНА")
# counter = 0

# for x in alf:
#     for y in alf:
#         for z in alf:
#             for c in alf:
#                 word = x + y + z + c

#                 glas_word = word.replace('А', "*").replace('О', "*").replace('И', "*")
#                 soglas_word = word.replace('П', "*").replace('Л', "*").replace('Н', "*")

#                 if "**" not in glas_word and "**" not in soglas_word:
#                     counter += 1


# print(counter)





# lst = (1,2,34)
# print(lst[1])
# lst[0] = 100

# print(lst)

# a = tuple([12,3,4,5])

# print(a)
# print(type(a))


# b = (25,31,2)




# a = 10

# print(type(a))

# b = a + 4

# b = "123"

# print(type(b))



# print(int())





# c = '2'

# print(type(c))
# print(c)

# c = int(c)
# print(type(c))
# print(c)

# print(c** 2)


# a = int(input())

# print(a)
# print(type(a))


# count() - считает количество вхождений элемента в строку или список
# возвращает значение, используется через точку к переменной в которой нужен поиск
# нужно понимать что передать в аргументе -> функция count() требует передачи искомой подстроки
# понимать что возвращается и какого типа данных

# s = "hello"
# a = s.count("l")

# print(a)
# print(type(a))




# a = " "
# b = ""

# print(bool(a))
# print(bool(b))  


# if "":
#     print("True")

# int()



# a = 10

# a = a + 1
# a += 1

# print(round(35.980564, 3))


# x = int(input("Введите х: "))
# y = int(input("Введите у: "))

# # res = (x + y) / (x + 1) - (x * y - 12) / (34 + x)
# res = ((x + y) / (x + 1)) - ((x * y - 12) / (34 + x))
# res = round(res, 3)

# print(res)

# res = []
# while True:
#     s = input()
#     if s == "EXIT":
#         break
#     s = s.split("/")
#     if len(s) != 3:
#         continue

#     if int(s[1])  > 90 or int(s[2]) < 740:
#         res.append(s[0])

# print(res)
# "" += '0' -> "0" += '4' -> '04'

# def perevod(n, osn):
#     alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     res = ''
#     while n >= osn:
#         ost = n % osn
#         res += alf[ost]
#         n = n // osn
#     res += alf[n]
#     return res[::-1]

# # min_var = 10000000000
# max_var = -1
# for N in range(1, 1000):
#     r = perevod(N, 2)
#     if N % 2 == 0:
#         r = '10' + r
#     else:
#         r = '1' + r + '01'
    
#     r = int(r, 2)
#     if r <= 1234 and r > max_var:
#         max_var = r

# print(max_var)

# "sdfsh" -> str
# 1 2 10 -5 -> int
# 3.4 -5.2 -> float
# True False -> bool

# print(1234 % 10)
# print(1234 % 100)

# # 17

# # n = int(input())
# # max_var = -1
# # for i in range(n):
# #     num = int(input())
# #     if num % 6 == 0 and num % 10 == 4 and num > max_var:
# #         max_var = num

# # print(max_var)

# # # 17 dop
# # n = int(input())
# # max_var = 1
# # for i in range(n):
# #     num = int(input())
# #     if num % 6 == 0 and num % 10 == 4:
# #         max_var *= num

# # print(max_var)
# summa = 0
# count = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     if abs(num) % 5 == 0 and abs(num) % 2 == 0:
#         summa += num
#         count += 1

# if count == 0:
#     print( "NO")
# else:
#     sr = summa / count
#     # print(round(sr, 2))

#     sr = str(sr)
#     index_dot = sr.find('.')
#     index_dot += 3
#     sr = sr[ 0: index_dot]
#     print(float(sr))

# 5 mod 3

# "1 2 3 4" -> ['1', '2', '3', '4']-> [1, 2, 3, 4]

# '30\t13\t41\t22\t25\t57\t52\t75\n'
# '42 83 2 4 23 53 19 53'

# with open(r"C:\Users\yokko\Desktop\9_task.txt", 'r') as file:
#     # 1 данные записаны в единыую строчку через пробел/запятую/слеш
#     # data = list(map(int, file.read().split(" ")))
#     # 2 каждая строчка - это отдельная запись
#     data = [i.replace("\n", "") for i in file]

# count = 0

# for i in data:
#     i =list(map(int,  i.split("\t")))
#     # print(i)
#     mean = sum(i) / len(i)
#     # четные заметные
#     count_even_zanet = 0
#     # нечетные заметные
#     count_odd_zanet = 0
#     # четные
#     summa_even = 0
#     # нечетных
#     summa_odd = 0
#     for j in i:
#         if j % 2 == 0:
#             summa_even += j
#             if j > mean:
#                 count_even_zanet += 1
#         else:
#             summa_odd += j
#             if j > mean:
#                 count_odd_zanet += 1
#     if count_even_zanet < count_odd_zanet and summa_even > summa_odd:
#         count += 1

# print(count)


# with open(r"C:\Users\yokko\Desktop\9_task_2.txt", 'r') as file:
#     # data = [i.replace('\n', "") for i in file]
#     data = [list(map(int, i.replace('\n', "").split("\t"))) for i in file]

# res_string_number = 0
# min_summa = float("inf")


# string_number = 0
# for i in data:
#     string_number += 1

#     # [1,2,3,4,5,5,5] -> {1,2,3,4,5} -> [1, 1, 1, 1, 3, 3, 3]
#     # [1,2,3,4,4,5,5] -> {1,2,3,4,5} -> [1, 2, 3, 2, 2, 2, 2]
    
#     v = [i.count(j) for j in i]
#     if v.count(1) == 4 and v.count(3) == 3:
#             nepovtor = [j for j in i if i.count(j) == 1]
#             mean_nepovtor = sum(nepovtor) / len(nepovtor)
#             # [1,2,3,4,5,5,5] -> [5, 5, 5] -> 5
#             povtor = [j for j in i if i.count(j) == 3][0]
#             max_value = max(i)
#             min_value = min(i)
#             if mean_nepovtor >= povtor and max_value % min_value != 0 and sum(i) < min_summa:
#                 min_summa = sum(i)
#                 res_string_number = string_number

# print(res_string_number)

                 
                
# with open(r"C:\Users\yokko\Desktop\9_task_3.txt") as file:
#     data = [i.replace("\n", "") for i in file]

# # print(data)

# count = 0
# for i in data:
#     i = list(map(int, i.split("\t")))
#     # [1,2,3,4,4,4] -> [1, 1, 1, 3, 3, 3]
#     v = [i.count(j) for j in i]
#     if v.count(1) == 3 and v.count(3) == 3:
#         # [1,2,3,4,4,4] -> [4,4,4] -> 4
#         povtor = [j for j in i if i.count(j) == 3][0]
#         # [1,2,3,4,4,4] -> [1, 2, 3] 
#         nepovtor = [j for j in i if i.count(j) == 1]
#         mean_nepovtor = sum(nepovtor) / len(nepovtor)
#         if povtor >= mean_nepovtor:
#             count += 1
# print(count)


                
# with open(r"C:\Users\yokko\Desktop\9_task_3.txt") as file:
#     data = [i.replace("\n", "") for i in file]

# count = 0
# for i in data:
#     i = list(map(int, i.split("\t")))
#     # print(i)
#     v = sorted(i)
#     # print(v)
#     step = v[1] - v[0]
#     if v[3] ** 2 > v[0] * v[1] * v[2]: 
#         count += 1
#     elif v[2] - v[1] == step and v[3] - v[2] == step:
#         count += 1
# print(count)


# t = (65, 77, 109)


# if s.endswith(('.com', '.ru')):
    



# # print(count)




# # a = ['i', 'have', 'three', 'pets']
# a = ['1', '5', '3']

# b = int(''.join(a))

# print(b)


# a = [0, -1, 10, -3]
# print(a)

# b = {0, -1, 10, -3}
# print(b)

# a = list("caaat")
# print(a)

# b = set('caaat')
# print(b)



# a=10, 30
# print(a)
# print(type(a))

# x = 4
# if 3 < x < 5:
#     print("x больше 3 и меньше 5")


# def perevod(n, osn):
#     alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     res = ''
#     while n >= osn:
#         ost = n % osn
#         res += alf[ost]
#         n = n // osn
#     res += alf[n]
#     return res[::-1]

# summa = 0
# counter = 0

# n = int(input())

# for i in range(n):
#     a = int(input())
#     semer = perevod(a, 7)
#     # print(semer)
#     if semer[-1] == '1':
#         counter += 1
#         summa += a

# if counter == 0:
#     print('NO')
# else:
#     print(counter)





# while True:
#     a = int(input())
#     if a == 0:
#         break




# a = int(input())


# print(type(a))





a = 'Нина'
b = 'Танцами'

# print("Тебя зовут", a, "ты увлекаешься", b)
print(f"Табея зовут {2 + 2} ты увлекаешься {b}")






