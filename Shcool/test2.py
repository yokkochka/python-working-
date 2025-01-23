
animals = ['cat', 'dog', 'duck', 'bird', 'fox']

# append() - функция допавления в конец списка
animals.append('camel')
print(animals)

# insert() - функция добавления элемента на определенное место (индекс) в списке
animals.insert(2, "pig")
print(animals)

# remove() - функция удадения по ЗНАЧЕНИЮ
animals.remove("bird")
print(animals)

# del - ключевое слово, которое позволяет удалить элемент по его индексу
del animals[-1]
print(animals)

# sort() - сортирует по возрастанию (reverse = True - сортировка по уюыванию)
animals.sort()
print(animals)

animals.sort(reverse=True)
print(animals)

# clear() - отчистка
animals.clear()
print(animals)