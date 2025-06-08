import time
import random

puntaje = 0
puntajedebot = 0

while True:
    player = input("Выбери камень, ножницы или бумагу :")
    if player == "камень" or player == "бумага" or player == "ножницы":
        bot = random.randint(1,3)
        
        if bot == 1:
            bot = "камень"
        elif bot == 2:
            bot = "ножницы"
        else:
            bot = "бумага"
            
        print("Камень! Ножницы! Бумага!")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        
        print("Бот выбрал:", bot)
        
        if bot == player:
            print("Ничья!")
        elif player == "камень" and bot == "ножницы":
            print("Ты победил!")
            puntaje = puntaje + 1
        elif player == "бумага" and bot == "камень":
            print("Победил бот!")
            puntaje = puntaje + 1
        elif player == "ножницы" and bot == "бумага":
            print("Ты победил!")
            puntaje = puntaje + 1
        else:
            print("Победил бот!")
            puntajedebot = puntajedebot + 1
            
        print("Результаты: ", puntaje, "\nBot:", puntajedebot)
    else:
        print("Что-то пошло не так")