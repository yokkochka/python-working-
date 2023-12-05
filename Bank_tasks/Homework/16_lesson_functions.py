# # Создай функцию, которая принимает коэффициенты квадратного уравнения и возвращает корни этого уравнения.


# def solve_quadratic_equation(a, b, c):
#     discriminant = b**2 - 4*a*c

#     if discriminant > 0:
#         root1 = (-b + (discriminant)**0.5) / (2*a)
#         root2 = (-b - (discriminant)**0.5) / (2*a)
#         return (root1, root2)
#     elif discriminant == 0:
#         root = -b / (2*a)
#         return root
#     else:
#         return "Комплексные корни, уравнение не имеет решения в действительных числах"

#  # Коэффициенты a, b, c соответственно для уравнения x^2 - 3x + 2 = 0
# coefficients_a = int(input("Введите коэффициент a: "))
# coefficients_b = int(input("Введите коэффициент b: "))
# coefficients_c = int(input("Введите коэффициент c: "))
# result = solve_quadratic_equation(coefficients_a, coefficients_b, coefficients_c)
# print("Корни квадратного уравнения:", result)





# Напиши функцию, которая принимает строку и число n, и возвращает строку, обрезанную до n символов, добавив многоточие, если строка была обрезана.

def truncate_string(stroka, n):
    if len(stroka) > n:
        res_stroka = stroka[:n] + "..."  # Обрезаем строку до n символов и добавляем многоточие
        return res_stroka
    else:
        return stroka

# Пример использования функции:
stroka = input("Введите строку: ")
n = int(input("Введите : "))
result = truncate_string(stroka, n)
print("Результат:", result)


