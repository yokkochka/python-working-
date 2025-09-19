min_sum = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
max_zn = -1
count_tro_podyclv = 0
file_path = '17_2.txt'
max_24 = 0
try:
    
    file = open(file_path,'r')
    numbers = list(map(int,file.readlines()))
    # print(numbers)
    for j in numbers:
        if j % 100 == 24 and j > max_24:
            max_24 = j
    print(max_24)
    for i in range(len(numbers)-2):
        cject = 0
        a = numbers[i],numbers[i+1],numbers[i+2]
        
        if len(str(a[0])) == 3:
            cject += 1
        if len(str(a[1])) == 3:
            cject += 1
        if len(str(a[2])) == 3:
            cject += 1
        # print(cject,sum(a))
        if cject == 1 and sum(a) > max_24:
 
            count_tro_podyclv += 1
            if min_sum > sum(a):
                min_sum = sum(a)
# print(int(min_sum))                           
except FileNotFoundError:
    print('файл не найден')
except IOError:
    print('ошибка при чтении файла')

print(f'троек: {count_tro_podyclv},минимальная сумма найденных троек: {int(min_sum)} ')