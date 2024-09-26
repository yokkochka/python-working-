# list() - функция, которая переводит данные (значения) в тип данных list

# my_set = {1, 2, 3}
# print(type(my_set))

# dop_var = list(my_set)
# print(type(dop_var))
# print(dop_var)

# [[1 2 3] 
# [4 5 6] 
# [7 8 9]]


# my_list = [[1,2,3], [4,5,6,['a',['*', '('],'b','c']], [7,8,9]]
# print(my_list[1][3][1][0])


# my_list = ['ant', 'bee', 'fly', 'helicopter']
# my_list[3] = 'dragonfly'
# print(my_list)


# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# c = a + b
# print(c)

# # c = a * b
# # print(c)

# c = a * 2
# print(c)

# # c = a / 2
# # print(c)


my_list = ['first', 'second', 'third', 'fourth']

# append() - функция, которая добавляет элемент В КОНЕЦ списка
my_list.append('fifth')
print(my_list)

# remove() - функция, которая удаляет элементы из списка ПО ЗНАЧЕНИЮ
my_list.remove('first')
print(my_list)

# insert() - функция, которая добавляет элемент НА ОПРЕДЕЛЕННОЕ место в списке
my_list.insert(2, "sixth")
print(my_list)

# del - КЛЮЧЕВОЕ СЛОВО с помощью которого можно удалить эелемнт ПО ИНДЕКСу из списка
del my_list[2]
print(my_list)

# sort() - функция, которая сортирует элементы списка в поряде возрастания
my_list = [1, 4, 5, 6,3, 2, 0, 11, -4, 6]
my_list.sort()
print(my_list)

# sort(reverse=True) - функция, которая сортирует в порядке убывания
my_list.sort(reverse=True)
print(my_list)

# clear() - функция полной отчистки списка
my_list.clear()
print(my_list)




# my_list = ['adasda', 'adasdasdasdasda', 'asd']
# min_len_el = 10000000000000


# for i in my_list:
#     if len(i) < min_len_el:
#         min_len_el = len(i)
# print(min_len_el)
