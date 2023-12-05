skobki = {'(': ')', '[':']', '{':'}'}

def proverka (str):
    flag = True
    for i in range(0, len(str), 2):
        try:
            if skobki[str[i]] != str[i+1]:
                flag = False
        except:
            flag = False

    if flag == True:
        print('Строка правильная')
    else:
        print('Строка неправильная')
        

str = input('Введите строку скобок: ')
if len(str) % 2 == 1:
    str = str[0:-1]

proverka(str)

