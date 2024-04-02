import numpy as np

def ak_count(A, k, wg, delta_t, tao):
    if k == 0:
        return 0
    else:
        return (4*A / (k * wg * delta_t)) * np.sin(k * wg * tao / 2)


wg = 6.28 * 10**3 
wv = wg / 2        

# Произвольные
A = 1              
delta_t = 0.1      
tao = 1            

for k in range(-10, 11):
     print(f'a{k}: {ak_count(A, k, wg, delta_t, tao)}')

