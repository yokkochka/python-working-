file_path="17_6.txt"
count=0

max_znach=0
max_sum=-1

try:
    file=open(file_path, "r")
    numbers=[int(i) for i in file]

    for n in numbers:
        count_nechet=0
        count_chet=0
        for b in str(n):
            if b in "02468":
                count_chet+=1
            else:
                count_nechet+=1

        if count_chet==count_nechet:
            max_znach=max(max_znach, n)



    for i in range(0, len(numbers)-1):
        flag=1
        for j in str(numbers[i]):
            for k in str(numbers[i+1]):
                if int(j)<=int(k):
                    flag=0
                    break
        
        if flag==1 and (numbers[i]+numbers[i+1]) < max_znach:
            count+=1
            max_sum = max(max_sum, numbers[i] + numbers[i+1])
except FileNotFoundError:
    print("файл не найден")

print(count)
print(max_sum)