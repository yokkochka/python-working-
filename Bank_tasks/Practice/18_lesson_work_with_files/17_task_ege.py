file_path = '17.txt'
count = 0 
max_znach = 0

try:
    with open(file_path , 'r') as f:

        # numbers = list(map(int, f.readline().split())) - если в файле данные перечислены через пробел в строку
        # numbers = [(int) for i in f] - еслиданные в файле перечислены в столбик
        
        numbers = [int(i) for i in f]

        for i in range(len(numbers) - 2):
            triangle = list([numbers[i], numbers[i + 1], numbers[i + 2]])
            triangle.sort()

            if (triangle[2]**2 == triangle[0]**2 + triangle[1]**2):
                count += 1
                max_znach = max(max_znach, triangle[2] + triangle[0] + triangle[1])

except FileNotFoundError:
    print('Файл не найден')

else: 
    print(count)
    print(max_znach)




    