<<<<<<< HEAD
s = "hello world hello world"

# # string.replace("first symbol(s)", "second stmbol(s)", count) - функция заменяет первые указанные символы в строке
# #  на вторые указанные (заданное количество раз)


# print(s.replace('l', '*'))    # ВСЕ найденные символы будут заменены на * 
# print(s.replace('l', '*', 1))    # ТОЛЬКО ОДИН ПЕРВЫЙ НАЙДЕННЫЙ СИМВОЛ будет заменен  

# print(s.replace('l', ''))    # ВСЕ найденны символы будут заменены на пустую строку (как будто удалены)
# print(s.replace('world', '***'))    # Зменяться могут не только символ на символ, но и последовательность символов на символ.последовательность символов


# string.count("symbol(s)") - функция, которая считает количество символа(символов) в строке

# print(s.count("hello"))
# print(s.count("l"))
# print(s.count("zzzzzz"))


# string.strip() - функция, которая удаляет начальные и конечные пробелы

# s = "       jsd       fjs       djfj        "
# print(s.strip())


# string.split("принцип деления") - функция, которая разделяеь строку на подстроку по указанному принципу

# s = "1 2 3 4"

# print(s.split(" "))




s = "hello world"

if "o" in s:
    s = s.replace()
=======
# print(input("Введите часы и минуты: ").split("*"))

a, b = map(int, input("Введите часы и минуты: ").split())
# a = int(a)
# b = int(b)
print(a, ":", b)

print(type(a), ":", type(b))
>>>>>>> 607abec4b6b42fe4ab4f61e0d585a3e7b0191286


