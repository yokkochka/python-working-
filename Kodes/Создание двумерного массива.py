# Первый способ
import numpy as np
n = int(input('kolvo strok'))
m = int(input('kolvo stolbcov'))
matrix = []
for i in range(n*m):
    matrix.append(int(input('Vvod chisla cpicka')))


matrix= np.array(matrix).reshape(n,m)
matrix =matrix.tolist()
print(matrix)

# Второй способ
n = int(input('kolvo strok'))
m = int(input('kolvo stolbcov'))

mat = [[0 for i in range(n)]for i in range(m)]
for i in range(n):
    for j in range(m):
        mat[i][j] = int(input('Vvod chisla cpicka'))
print(mat)


