# Напишите функцию, которая принимает список my_list = [10, 20, 30, 40, 50] и возвращает их среднее значение.

def calculate_madium_znach(numbers):
    if len(numbers) == 0:
        return 0  # Возвращаем 0 в случае пустого списка для избежания деления на ноль
    summa = sum(numbers)
    medium_znach = summa / len(numbers)
    return medium_znach

# Пример использования функции:
my_list = [10, 20, 30, 40, 50]
result = calculate_madium_znach(my_list)
print("Среднее значение списка:", result)




# Напишите функцию, которая принимает от пользователя список  и возвращает их среднее значение.

def calculate_madium_znach(numbers):
    if len(numbers) == 0:
        return 0  # Возвращаем 0 в случае пустого списка для избежания деления на ноль
    summa = sum(numbers)
    medium_znach = summa / len(numbers)
    return medium_znach


my_list = []
kol_numbers= int(input("Введите количество цифр в списке: "))
for i in range(kol_numbers):
    my_list.append(float(input("Введите значение из списка: ")))

result = calculate_madium_znach(my_list)
print("Среднее значение списка:", result)



# Создайте функцию, которая принимает число и возвращает True, если число четное, и False, если число нечетное.
# - Запроси у пользователя число
# - Отправь его в функцию
# - Если число четное - верни True
# - Если число нечетное - верни False
# - В зависимости от того, что вернулось функцией выведи результат: четное число или нет

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Пример использования функции:
num = int(input("Введите число: "))
if is_even(num):
    print("Число четное")
else:
    print("Число нечетное")




# Напишите рекурсивную функцию, которая принимает число и возвращает его факториал (произведение всех целых чисел от 1 до этого числа).
# Попробуй использовать вызов функции в print() и f-строку

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования функции:
number = int(input("Введите число для вычисления факториала: "))

print(f"Факториал числа {number} равен {factorial(number)}")




# Создайте функцию, которая принимает число и определяет, является ли оно простым (имеет только два делителя: 1 и само число).

# Для проверки числа на простоту, необходимо проверить делители числа. Однако нет необходимости проверять все числа до чиса включительно, 
# достаточно ограничиться проверкой до квадратного корня из числа. (Т.к. если найдутся делители до значения корня числа, то это уже означает 
# что число не простое, а если не найдется - то из-за парности делителей это будет означать, что делителей и нет)
# Можно разобрать число 36 и 29

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Пример использования функции:
num = int(input("Введите число: "))
if is_prime(num):
    print(f"Число {num} - простое.")
else:
    print(f"Число {num} - не является простым.")





# Напишите две функции, которые принимает температуру в градусах Цельсия и возвращают ее эквивалент в градусах Фаренгейта и Кельвинах


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Пример использования функций:
temperature_in_celsius = float(input("Введите температуру в градусах Цельсия: "))

fahrenheit = celsius_to_fahrenheit(temperature_in_celsius)
kelvin = celsius_to_kelvin(temperature_in_celsius)

print(f"{temperature_in_celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
print(f"{temperature_in_celsius} градусов Цельсия = {kelvin} Кельвина")






# Напиши функцию, которая принимает строку и возвращает True, если строка является палиндромом (читается одинаково в обоих направлениях).

def is_palindrome(s):
    s = s.lower()  # Приводим все символы строки к нижнему регистру для учета регистронезависимости
    s = s.replace(" ", "")

    return s == s[::-1]  # Возвращаем True, если строка читается одинаково в обоих направлениях

# Пример использования функции:

# stroka = "А роза упала на лапу Азора"
stroka= input("Введите строку: ")

if is_palindrome(stroka):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")





is_even = lambda x: x % 2 == 0
print(is_even(7))  # Выведет: False
print(is_even(10)) # Выведет: True