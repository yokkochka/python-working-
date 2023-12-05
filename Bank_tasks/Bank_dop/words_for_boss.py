# Руководителю иногда бывает сложно подобрать слова для речи. Помогите ему создав генератор случайных фраз из задаваемых слов. 
# Генератор должен работать так: вы вводите существительные (по одному на строку), после чего идет “стоп слово” и вы пишете глаголы, 
# также до “стоп слова”. После этого количество фраз которые нужно сгенерировать. и вывести фразы. с-существительное, г-глагол, 
# типы фраз сгс,гсс,ссг. (Фразы могут иметь ошибки в склонениях и падежах)


import random as rnd

list_s = []
list_g = []

input_stroka = ""

while input_stroka != "стоп":
    input_stroka = input("Введите существительное: ")
    list_s.append(input_stroka)

del list_s[len(list_s)-1]


input_stroka = ""
while input_stroka != "стоп":
    input_stroka = input("Введите глагол: ")
    list_g.append(input_stroka)

del list_g[len(list_g)-1]


count_phrase = int(input("Введите количество фраз: "))

for i in range(count_phrase):
    variant = rnd.randint(1,3)
    # Формируем предложение типа сгс
    if variant == 1:
        print(f"Формат сгс: {rnd.choice(list_s)} {rnd.choice(list_g)} {rnd.choice(list_s)}")

    # Формируем предложение типа гсс
    elif variant == 2:
        print(f"Формат гсс: {rnd.choice(list_g)} {rnd.choice(list_s)} {rnd.choice(list_s)}")

    # Формируем предложение типа ссг
    elif variant == 3:
        print(f"Формат ссг:  {rnd.choice(list_s)} {rnd.choice(list_s)} {rnd.choice(list_g)}")



