# Пример того, как определять порядок действий скобками

print( (8 + 3) *  5)
print( 8 + (3 * 5) )




# Практика: давай напишем простой калькулятор:

# Первым делом поприветствуй пользователя и скажи что умеет 
# калькулятор

# - Запроси два числа 
# - Выведи результат их умножения

print('Привет пользователь, я - начинающий калькулятор! Я уже умею умножать')
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print(num1, '*', num2, '=', num1 * num2)



# Практика: “Перевод времени”
# Инопланетяне не имеют понятия о земных днях, часах и минутах, 
# они умеют определять время только в секундах. Давайте напишем 
# программу, которая будет помогать инопланетянам и переводить 
# кол-во секунд в дни, часы и минуты


# Перевод секунд
sek = int(input('Инопланетянин! Вводи количество секунд: '))

days = sek // (24*60*60)
sek = sek - (days * (24*60*60) )

hours = sek // (60*60)
sek = sek - (hours * (60*60))

min = sek // 60
sek = sek - (min*60)
print('Получается: ',days,'дней, ',hours,'часов, ', min,'минут,',sek,'секунд!')




# Практика: определение цифр числа
# Пользователь вводит трехзначение число, программа должна 
# через пробел вывести его цифры


# Определение цифр трехзначного числа
number = int(input('Введи трехзначное число'))

num3 = number % 10
number //= 10

num2 = number % 10
number //= 10

num1 = number % 10
number //= 10

print(num1, num2, num3)




# Практика: число-перевертыш
# В предыдущем задании мы научились получать цифры числа, теперь, 
# используя эту информацию, нужно из числа, например, 789 получить 
# число 987

# Подсказка: 987 = 9*100 + 8*10 + 7


number = int(input('Введи трехзначное число: '))

num3 = number % 10
number //= 10

num2 = number % 10
number //= 10

num1 = number % 10
number //= 10

#print(num1, num2, num3)
reverse_number = num3*100 + num2*10 + num1
print('Число-перевертыш: ', reverse_number)




# Практика: Полив роз

# Родители отправили нас на дачу и сказали что за домом стоит 
# бочка со специальным раствором, которым нужно полить розы. 
# Так же они выдали нам 3-литровое ведро. Напиши программу, которая 
# определит, сколько нам нужно сделать заходов чтобы полить цветы

# Условия:
#   - Число литров в бочке вводится с клавиатуры
#   - Набирать можно только полные ведра, то есть за один заход мы 
#         можем забрать из бочки толко 3 литра
#   - Программа выводит кол-во заходов и кол-во оставшихся литров в 
#         бочке


barrel = int(input('Введите сколько литров раствора в бочке: '))
bucket = 3

passes = barrel // bucket
liters_in_the_barrel = barrel - 3 * passes

print(passes, 'заходов мы совершили,', liters_in_the_barrel, 'осталось в бочке')




x = int(input("Введите значение х: "))
y = int(input("Введите значение y: "))


print(round(((x + y)/(x + 1)) - ((x*y - 12)/(34 + x)), 3))


