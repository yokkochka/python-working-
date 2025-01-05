
file_path = '17_3.txt'
count_par = 0
max_summa_par = -1

try:
    with open(file_path,'r') as f:
        numbers = [int(i) for i in f]
        
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):

                if numbers[i] * numbers[j] % 34 != 0:
                    count_par += 1
                    max_summa_par = max(max_summa_par,  numbers[j]+ numbers[i])

except FileNotFoundError:
    print('Error')

print(count_par)
print(max_summa_par)



