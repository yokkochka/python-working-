#Исправьте ошибки
a = -5
b = int('one')
for i in range(5)
a = a + b
    c = -5/a
    print(c)
    
#Перепишите цикл под try-except
while True:
    a= input('Введите число: ')
    b = input('Введите второе число: ')
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print('На ноль делить нельзя')
        else:
            print(int(a)/int(b))
            break
    else:
        print('Подерживаются только числа')