



# s = 'cat'

# a = len(s)
# print(a)



# s = 'hello'

# print(s[4] + s[5] + s[7])

# print(s[::-1])

# len(string) - оперделение длины строки

# string.split() - разрезает строку
# a = "gf djfh gf djfsh"

# a = a.split()
# print(a)
# >> ['gf', 'djhsgdf','sdhf', 'jdsfh']



a = 'Аня, Катя, Маша, Вера'
a = a.split()
print(a)

for i in a:
    # print(i)
    if i[0] == 'А' and i.replace(',', '')[-1] == 'я':
        print('Строка подходит: ', i)

# string.repalce('a', 'o') - замена символов строки
# string.count('a') - считает кол-во определенных символов строки




