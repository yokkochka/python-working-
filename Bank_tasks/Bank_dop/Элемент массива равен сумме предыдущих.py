'''
Ссылка: https://leetcode.com/problems/running-sum-of-1d-array/

Дан массив nums. Мы определяем текущую сумму массива как runningSum[i] = sum(nums[0]…nums[i]).
Вернуть текущую сумму nums.

Пример 1:
Ввод: nums = [1,2,3,4]
 Выход: [1,3,6,10]
 Объяснение: Текущая сумма получается следующим образом: [1, 1+2, 1+2+3, 1+2+ 3+4].

Пример 2:
Ввод: nums = [1,1,1,1,1]
 Вывод: [1,2,3,4,5]
 Объяснение: Текущая сумма получается следующим образом: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Пример 3:
Ввод: nums = [3,1,2,10,1]
 Вывод: [3,4,6,16,17]
 
Ограничения:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
'''


# Решение 
# nums = [1,2,3,4]
# nums = [1,1,1,1,1]
nums = [3,1,2,10,1]

for i in range(1, len(nums)): nums[i] += nums[i-1]
print(nums)



# Вставка в leetcode

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)): nums[i] += nums[i-1]
#         return nums