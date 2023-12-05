
try:
    mark = int(input('Введите свою оценку (от 0 до 100): '))
    if 0 <= mark <= 30:
        print(mark, '- Ты можешь лучше!')
    elif 31 <= mark <= 50:
        print(mark, '- Удовлетворительно!')
    elif 51 <= mark <= 70:
        print(mark, '- Хорошая работа!')
    elif 71 <= mark <= 90:
        print(mark, '- Отличная работа!')
    elif 91 <= mark <= 100:
        print(mark, '- Замечательная работа!')
    else: 
        print('Оценка должна быть больше 0')
except ValueError:
    print('Ошибка: некорректный ввод данных')

