# из таблицы 1.1 для моего варианта: 
# алгоритм : Ri+1 = |[( Ri + Ri-1 ) *K1] | 
# k1 - 1,2 -5 
# r0 - 0,3217 - 0,5763 
# r1 - 0,254 - 0,484 
# q - 20 
# 
# 
# из таблицы 1.2 для моего вариванта: 
# критические точки распределения: хи квадрат 
# число степеней свободы k - 4 
# уровни значимости: 
# 0.01 : 13,3
# 0.025: 11,1 
# 0.05: 9,5 
# 0.95: 0,711 
# 0.975: 0,484 
# 0.99: 0,297



import numpy as np
import pandas as pd
import random


def create_seq(r0, r1, n, k1):
    seq = [r0, r1]
    for i in range(2, n):
        seq.append(abs((seq[i - 1] + seq[i - 2]) * k1) % 1)

    return seq


def run_experiments(r0_range, r1_range, n, k_values, experiments):
    results = []

    for i in range(experiments):
        r0 = random.uniform(r0_range[0], r0_range[1])
        r1 = random.uniform(r1_range[0], r1_range[1])
        k = random.choice(k_values)
        seq = create_seq(r0, r1, n, k)
        mean = np.mean(seq)
        var = np.var(seq)

        results.append([i, r0, r1, k, mean, var])

    df = pd.DataFrame(results, columns=["Эксперимент", "R0", "R1", "K", "Мат. ожидание", "Дисперсия"])
    return df


N = int(input("Введите количсетво чисел последовательности: "))

experiments = 12 
K_values = [1.2, 2.0, 3.0, 4.0, 5.0] 
R0_range = (0.3217, 0.5763)
R1_range = (0.254, 0.484)
q = 20


df = run_experiments(R0_range, R1_range, N, K_values, experiments)
print(df.to_string(index=False))

# print(create_seq(0.3217, 0.254, 300, 2))

