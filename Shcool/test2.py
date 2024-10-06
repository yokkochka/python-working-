
# 1
# 2
# 3
# 4
# 5
matrix = [[1], [2], [3], [4], [5]]

# 1 2 3 4 5
matrix = [[1,2,3,4,5]]


# 1 2
# 3 4
matrix = [[1,2], [3,4]]

# 1 2 3
# 4 5 6
# 7 8 9
matrix = [[1,2,3], [4,5,6], [7,8,9]]


# 1 2
# 3 4 умноэить на 2
matrix = [[1,2], [3,4]] 

for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

print('----------------------------')

matrix_x2 = [[1*2,2*2], [3*2, 4*2]]

for i in matrix_x2:
    for j in i:
        print(j, end = ' ')
    print()
print('----------------------------')

# Транспонирование (замена строк на слобцы)
# 1 2   ->  1 3 
# 3 4   ->  2 4
# matrix = [[1,2], [3,4]]

# Перемножение матриц
# 1 2     0   ->  1*0 + 2*5 -> 10
# 3 4  *  5   ->  3*0 + 4*5 -> 20



# Транспонирование (m - кол-во строк n - кол-во столбцов)
# Создание пустого списка - матрицы
matrix = []

m = int(input("Введитекол-во строк: "))
n = int(input("Введитекол-во столбцов: "))

# Ввод матрицы пользователем

for i in range(m):
    # [[1,2], [3,4]]
    matrix.append(list())
    for j in range(n):
        matrix[i].append(int(input("Введите элемент матрицы: ")))

# print(matrix)
# Вывод матрицы
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

# Создаем матрицу для транспонирования и заполняем ее нулями
transparent_matrix = []
for i in range(m):
    # [[0,0],[0,0]]
    transparent_matrix.append(list())
    for j in range(n):
        transparent_matrix[i].append(0)

# print(transparent_matrix)

# Транспонировать матрицу
for i in range(m):
    for j in range(n):
        transparent_matrix[j][i] = matrix[i][j]
        
for i in transparent_matrix:
    for j in i:
        print(j, end = ' ')
    # print()


