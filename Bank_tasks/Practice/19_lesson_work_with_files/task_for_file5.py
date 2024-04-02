# Открываем файл для чтения
with open('file5.txt', 'r') as file:
    # Читаем строку из файла и разделяем ее по пробелам, преобразуя каждый элемент в число
    numbers = list(map(int, file.readline().split()))

    # Вычисляем среднее значение чисел
    average = sum(numbers) / len(numbers)

    print("Среднее значение чисел в файле:", average)
