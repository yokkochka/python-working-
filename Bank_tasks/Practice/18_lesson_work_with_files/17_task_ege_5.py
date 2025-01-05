file_path = '17_5_dz.txt'
count_troek = 0
max_summa_elementov = -1
max_znach_321 = 0

try:
    with open(file_path, 'r') as f:
        numbers = [int(i) for i in f]

        for i in numbers:
            if i % 1000 == 321:
                max_znach_321 = max(max_znach_321, i)

        for i in range(len(numbers) - 2):
            troyka = [numbers[i], numbers[i + 1], numbers[i + 2]]
            count_5_znach_cisel = 0

            for j in troyka:
                if 9999 < j < 1000000:
                    count_5_znach_cisel += 1

            if (troyka[0] % 5 == 0 or troyka[1] % 5 == 0 or troyka[2] % 5 == 0) and count_5_znach_cisel == 2 and sum(troyka) > max_znach_321:
                count_troek += 1
                max_summa_elementov = max(max_summa_elementov, sum(troyka))

except FileNotFoundError:
    print('Error')

print(count_troek)
print(max_summa_elementov)


