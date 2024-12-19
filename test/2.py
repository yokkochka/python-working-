# def calculate_max_thrill_score(final_score):
#     x, y = map(int, final_score.split(':'))
#     if x == 0 or y == 0:
#         return 0
    
#     return min(x, y)

# final_score = input()
# print(calculate_max_thrill_score(final_score))




def calculate_max_thrill_score(final_score):
    x, y = map(int, final_score.split(':'))
    
    if x == 0 or y == 0:
        return 0
    
    # Находим минимальное количество переворотов (наибольшее количество смен лидерства)
    # и максимальное количество смен лидерства
    thrill_score = 2 * min(x, y)
  
    
    return thrill_score

final_score = input()
print(calculate_max_thrill_score(final_score))
