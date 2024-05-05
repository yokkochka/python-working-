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




# n = '3555'
# m = 3
# summa = 0
# for i in range(2000):
#     n = n + '5'
#     m += 1
#     while "25" in n or '355' in n or '555' in n:
#         if '25' in n:
#             n = n.replace("25", "3", 1)
#         elif '355' in n:
#             n = n.replace('355', '52', 1)
#         elif '555' in n:
#             n = n.replace('555', '23', 1)
#     summa = n.count('2')* 2 + n.count('3')*3 + n.count('5')* 5
    
#     if summa == 27:
#         print(m)
#         break


# import matplotlib.pyplot as plt

# # Создаем структурную схему
# def draw_decoder_structure():
#     fig, ax = plt.subplots(figsize=(8, 6))
#     ax.axis('off')  # Отключаем отображение осей

#     # Рисуем блоки
#     blocks = [
#         {"name": "Входные данные", "position": (0.1, 0.9)},
#         {"name": "Извлечение информации", "position": (0.1, 0.7)},
#         {"name": "Генерация проверочных символов", "position": (0.1, 0.5)},
#         {"name": "Проверка ошибок", "position": (0.1, 0.3)},
#         {"name": "Коррекция ошибок", "position": (0.1, 0.1)},
#         {"name": "Выходные данные", "position": (0.1, -0.1)}
#     ]

#     for block in blocks:
#         ax.text(block["position"][0], block["position"][1], block["name"],
#                 fontsize=12, ha='left', va='center', bbox=dict(facecolor='lightgray', edgecolor='black', boxstyle='round,pad=0.5'))

#     # Рисуем стрелки между блоками
#     for i in range(len(blocks) - 1):
#         ax.annotate('', xy=blocks[i + 1]["position"], xytext=blocks[i]["position"],
#                     arrowprops=dict(facecolor='black', arrowstyle='->'))

#     plt.title('Структурная схема декодера')
#     plt.show()

# # Рисуем структурную схему декодера
# draw_decoder_structure()

# a = 0
# if a:
#     print('True')
# else:
#     print("False")



my_tuple = ([1, 2, 3], "dog", [[88, 99, [23, "cat", 32]],{"a", "b", "c"}])

a = my_tuple[2][0][2][1]
print(a)