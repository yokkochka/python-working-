

# user_input = 1
# while user_input != 0:
#     user_input = int(input("Введиет число: "))
#     print(user_input**2)
    
    
user_input = int(input("Введите число: "))
while user_input != 0:
    if (user_input == -1):
        break
    print(user_input ** 2)
    user_input = int(input("Введите число: "))
else:
    print("Программа завершилась аварийно! Будте внимательнее!")


