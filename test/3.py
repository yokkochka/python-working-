
from collections import Counter

def minimum(a, b):
    freq = Counter(a) + Counter(b)
    a_list = list(a)
    
    result = []

    for i in range(len(a_list)):
        for c in sorted(freq):
            if freq[c] > 0:
                result.append(c)
                freq[c] -= 1
                break
    
    return ''.join(result)

a = input().strip()
b = input().strip()

print(minimum(a, b))
