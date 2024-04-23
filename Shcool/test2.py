# chetvert = { 'Misha' : {'math':[4,5], 'rus':[4,4], 'info':[5,3]}, 
#              'Kolya' : {'math':[5,4,4], 'rus':[4,3], 'info':[5,2]},
#              'Tanya' : {'math':[5,4], 'rus':[3,3], 'info':[5,5]}   }

# choice = int(input('Меню\n  1 - Добавить оценку\n  2 - Выставить четвертные оценки'))

# if choice == 1:
#     name = input('Введите имя ученика: ')
#     subject = input("Введите предмет: ")
#     mark = int(input('Введите оценку: '))

#     chetvert_keys = list(chetvert.keys())

#     for i in chetvert_keys:
#         if i == name:
#             name_keys = list(chetvert[i].keys())
#             for j in name_keys:
#                 if j == subject:
#                     chetvert[i][j].append(mark)
#     print(chetvert)


# elif choice == 2:
#     chetvert_keys = list(chetvert.keys())
#     for i in chetvert_keys:
#         print(i, ":")
#         i_keys = list(chetvert[i].keys())
#         for j in i_keys:
#             print(j , ":", sum(chetvert[i][j])/len(chetvert[i][j]))
#         print()

# else:
#     print('Некорректный ввод')


# [1, 2, {}, [], set() ]





# stroka= 'Иллюминатор'

# ind = stroka.find('ы')
# if ind == -1:
#     print('Такого символа в строке нет')
# else:
#     print(f'искомый индекс: {ind}')



# print('"Гарри Поттер" - \nмой любимый фильм')
# print("'Гарри Поттер' - мой любимый фильм")


# print('\'Гарии Поттер\' - мой любимый фильм')

# sep = ... end = ...

# \n, \t
# print(1, 2, 3, 4, 5, sep="*")


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end = ' ')
#     print()





n = '3555'
m = 3
summa = 0
for i in range(2000):
    n = n + '5'
    m += 1
    while "25" in n or '355' in n or '555' in n:
        if '25' in n:
            n = n.replace("25", "3", 1)
        elif '355' in n:
            n = n.replace('355', '52', 1)
        elif '555' in n:
            n = n.replace('555', '23', 1)
    summa = n.count('2')* 2 + n.count('3')*3 + n.count('5')* 5
    
    if summa == 27:
        print(m)
        break