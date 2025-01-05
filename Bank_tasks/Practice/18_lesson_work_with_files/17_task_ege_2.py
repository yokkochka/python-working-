


file_path = '17_2.txt'
count_troek = 0
min_summa_troek = 100000000000000000

try:
    with open(file_path,'r') as f:
        numbers = [int(i) for i in f]
        max_znach_24 = numbers[0]

        for i in numbers:
            if i % 100 == 24:
                max_znach_24 = max(max_znach_24, i)

        for i in range(len(numbers)-2):
            troyka = [numbers[i], numbers[i + 1], numbers[i + 2]]
            count_3_znach_chislo = 0

            for j in troyka:
                if 99 < abs(j) < 1001:
                    count_3_znach_chislo += 1

            if count_3_znach_chislo == 1 and sum(troyka) > max_znach_24:
                count_troek += 1
                min_summa_troek = min(min_summa_troek, sum(troyka))

except FileNotFoundError:
    print('File nor find')

print(count_troek)
print(min_summa_troek)




