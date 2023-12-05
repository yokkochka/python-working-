
try:
    age = int(input('Введите свое любимое число: '))
    if age >= 50:
        print('Число больше 50')
    else:
        print('Число меньше 50')
except ValueError:
    print('Ошибка: некорректный ввод')
