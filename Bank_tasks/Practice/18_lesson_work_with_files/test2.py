

file = open("file5.txt", 'r')

# data = list(map(int, file.readline().split()))

data = [10, 5, 12, 1, 8, 9, 10, 5]

for i in range(len(data) - 2):
    print(data[i], data[i+1], data[i+2])