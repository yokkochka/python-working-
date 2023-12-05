kosti = []
for i in range(6):
    for j in range(6):
        for k in range(6):
            a = []
            a.append(i+1)
            a.append(j+1)
            a.append(k+1)
            kosti.append(sorted(a))
var1 = len(kosti)
print(kosti)
print("--------")
kosti = sorted(kosti)
print('--------')
print(var1)

counter = 0
for i in range(len(kosti) - 1):
    if kosti[i] != kosti[i+1]:
        counter += 1
        print(kosti[i])
print(counter)