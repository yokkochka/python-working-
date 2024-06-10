import random,time
print("Привет!Сейчас ты будешь играть с ботом в камень, ножницы, бумага.")
time.sleep(2)
print("В каждом раунде ты должен выбрать камень,ножницы или бумага.")
time.sleep(2)
print("Игра будет продолжаться пока каждый игрок не наберет 3 балла")
time.sleep(2)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
user_score=0
bot_score=0
bot_list=["камень","ножницы","бумага"]
while user_score<3 and bot_score <3:
    print("Новый раунд")
    user_choice=input("Введите камень,ножницы или бумага").lower().strip()
    bot_choice=random.choice(bot_list)
    print(f"Вы выбрали {user_choice}, бот выбрал {bot_choice}")
    if user_choice==bot_choice:
        print("Ничья")
        user_score+=1
        bot_score+=1
    elif (bot_choice=="камень" and user_choice=="ножницы") or (bot_choice=="ножницы" and user_choice=="бумага") or (bot_choice=="бумага" and user_choice=="камень"):
        bot_score+=1
        print("Бот победил")
    elif (user_choice=="бумага" and bot_choice=="камень") or (user_choice=="камень" and bot_choice=="ножницы") or (user_choice=="ножницы" and bot_choice=="бумага"):
        user_score+=1
        print("Пользователь победил")
    else:
        print("Некоректный ввод")