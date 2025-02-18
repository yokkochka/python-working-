# import tkinter as tk
# from PIL import Image

# root = tk.Tk()
# root.title("Test window")

# root.geometry("400x400+700+400")

# lb1 = tk.Label(root, text = "1", anchor = "e", width = 30)
# lb1.pack()

# lb2 = tk.Label(root, text = "2", background = "yellow")
# lb2.pack()

# lb3 = tk.Label(root, text = "3", relief = "solid", borderwidth = 5)
# lb3.pack()

# lb4 = tk.Label(root, text = "4", cursor="circle")
# lb4.pack()

# lb5 = tk.Label(root, text = "5", font = ("Arial", 20, "bold"))
# lb5.pack()

# lb6 = tk.Label(root, text = "6", foreground = "red")
# lb6.pack()

# lb7 = tk.Label(root, text = "7", height = 3, bg = "lightblue")
# lb7.pack()

# image = Image.open("image.png")
# image = image.resize((40, 40))
# image.save("image1.png")
# image = tk.PhotoImage(file = "image1.png", width=40)
# lb8 = tk.Label(root, image=image, width = 40, height=40)
# lb8.pack()

# lb9 = tk.Label(root, text = "9", padx = 20, pady = 10, bg = "lightgreen")
# lb9.pack()

# textvariable = tk.StringVar()
# textvariable.set("Text variable")
# lb10 = tk.Label(root, text = "10", textvariable=textvariable)
# lb10.pack()

# def change_text():
#     global textvariable
#     textvariable.set("Text changed")
# button_for_lb10  = tk.Button(root, text = "Press me to chenge text", command = change_text)
# button_for_lb10.pack()

# lb11 = tk.Label(root, text = "11 11 11", wraplength=25)
# lb11.pack()

# root.mainloop()




# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x400+500+400")
# root.title("Первое окно")

# root2 = tk.Toplevel()
# root2.geometry("400x400+900+400")
# root2.title("Второе окно")

# label = tk.Label(root, text = "Я первый лейбл!", bg = "lightblue", fg = "darkblue", font = ("Arial", 14, "bold"))
# label.pack()

# label2 = tk.Label(root2, text = "Я второй лейбл!", bg = "lightgreen", fg = "darkgreen", font = ("Arial", 12, "italic"))
# label2.pack()

# root.mainloop()



# import tkinter as tk


# root = tk.Tk()
# root.geometry("400x400+500+400")
# root.title("Окно")

# def first_click():
#     text.set("А теперь на вторую")

# def second_click():
#     text.set("Нажми на первую кнопку")


# text = tk.StringVar(value="Нажми на кнопку")

# lbl = tk.Label(root, textvariable=text)
# lbl.pack()

# btn1 = tk.Button(root, text = "Первая кнопка", command = first_click)
# btn1.pack()

# btn2 = tk.Button(root, text = "Вторая кнопка", command = second_click)
# btn2.pack()


# root.mainloop()



# import tkinter as tk

# def callback_function():
#     print("Кнопка нажата!")

# root = tk.Tk()
# root.title("Пример использования атрибутов Button")

# button1 = tk.Button(root, text="Click Me (command)", command=callback_function)
# button1.pack(pady=10)

# button2 = tk.Button(root, text="Click Me (disabled)", state="disabled")
# button2.pack(pady=10)

# button3 = tk.Button(root, text="Click Me (default)", default="active")
# button3.pack(pady=10)

# button4 = tk.Button(root, text="Click Me (overrelief)", overrelief="sunken")
# button4.pack(pady=10)

# root.mainloop()




# import tkinter as tk

# def create_composition():
#     name = entry_name.get()
#     surname = entry_surname.get()
#     activity = entry_activity.get()
#     place = entry_place.get()
#     weather = entry_weather.get()
#     memorable_event = entry_event.get()
#     student_class = entry_class.get()

#     composition = (
#         f"Сочинение: 'Как я провел лето'\n\n"
#         f"Это было удивительное лето!\n"
#         f"Летом я занимался(ась) {activity}. Мне очень понравилось, потому что "
#         f"это именно то, что я люблю.\n"
#         f"Я провел(а) лето {place}, где было замечательная {weather} погода.\n"
#         f"Самое запоминающееся событие лета - {memorable_event}. "
#         f"Это был момент, который я никогда не забуду.\n\n"
#         f"Ученица(ик) {student_class} класса {name} {surname}"
#     )

#     text.set(composition)


# root = tk.Tk()
# root.geometry("700x600+500+400")
# root.title("Опросник для сочинения")

# # Вопросы и поля ввода
# label_name = tk.Label(root, text="Как вас зовут?")
# label_name.pack()
# entry_name = tk.Entry(root)
# entry_name.pack()

# label_surname = tk.Label(root, text="Ваша фамилия?")
# label_surname.pack()
# entry_surname = tk.Entry(root)
# entry_surname.pack()

# label_activity = tk.Label(root, text="Чем вы занимались этим летом?")
# label_activity.pack()
# entry_activity = tk.Entry(root)
# entry_activity.pack()

# label_place = tk.Label(root, text="Где вы проводили лето?")
# label_place.pack()
# entry_place = tk.Entry(root)
# entry_place.pack()

# label_weather = tk.Label(root, text="Какая была погода летом?")
# label_weather.pack()
# entry_weather = tk.Entry(root)
# entry_weather.pack()

# label_event = tk.Label(root, text="Какое событие запомнилось больше всего?")
# label_event.pack()
# entry_event = tk.Entry(root)
# entry_event.pack()

# label_class = tk.Label(root, text="Какой класс вы посещаете?")
# label_class.pack()
# entry_class = tk.Entry(root)
# entry_class.pack()

# button_submit = tk.Button(root, text="Создать сочинение", command=create_composition)
# button_submit.pack()

# text = tk.StringVar(value = "")

# label_result = tk.Label(root, textvariable=text, justify="left")
# label_result.pack()

# root.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.title("Регистрация")
# root.geometry("400x400+500+400")

# def say_login_and_password():
#     if entry_password.get() != entry_confirm_password.get():
#         print("Пароли не совпадают")
#         return
#     print(f"Логин: {entry_name.get()}")
#     print(f"Пароль: {entry_password.get()}")

# label_name = tk.Label(root, text="Имя")
# label_name.pack()
# entry_name = tk.Entry(root)
# entry_name.pack()

# label_surname = tk.Label(root, text="Фамилия")
# label_surname.pack()
# entry_surname = tk.Entry(root)
# entry_surname.pack()

# label_email = tk.Label(root, text="Электронная почта")
# label_email.pack()
# entry_email = tk.Entry(root)
# entry_email.pack()

# label_password = tk.Label(root, text="Пароль")
# label_password.pack()
# entry_password = tk.Entry(root, show="*")
# entry_password.pack()

# label_confirm_password = tk.Label(root, text="Подтвердите пароль")
# label_confirm_password.pack()
# entry_confirm_password = tk.Entry(root, show="*")
# entry_confirm_password.pack()

# button_register = tk.Button(root, text="Регистрация", command=say_login_and_password)
# button_register.pack()

# root.mainloop()



import tkinter as tk

def create_composition():
    name = entry_name.get()
    surname = entry_surname.get()
    activity = entry_activity.get()
    place = entry_place.get()
    weather = entry_weather.get()
    memorable_event = entry_event.get()
    student_class = entry_class.get()

    composition = (
        f"Сочинение: 'Как я провел лето'\n\n"
        f"Это было удивительное лето!\n"
        f"Летом я {activity}. Мне очень понравилось, потому что "
        f"это именно то, что я люблю.\n"
        f"Я провел(а) лето {place}, где была {weather} погода.\n"
        f"Самое запоминающееся событие лета - {memorable_event}. "
        f"Это был момент, который я никогда не забуду.\n\n"
        f"Ученица(ик) {student_class} класса {name} {surname}"
    )

    text.set(composition)


root = tk.Tk()
root.geometry("700x600+500+400")
root.title("Опросник для сочинения")

# Вопросы и поля ввода
label_name = tk.Label(root, text="Как вас зовут?")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_surname = tk.Label(root, text="Ваша фамилия?")
label_surname.pack()
entry_surname = tk.Entry(root)
entry_surname.pack()

label_activity = tk.Label(root, text="Чем вы занимались этим летом?")
label_activity.pack()
entry_activity = tk.Entry(root)
entry_activity.pack()

label_place = tk.Label(root, text="Где вы проводили лето?")
label_place.pack()
entry_place = tk.Entry(root)
entry_place.pack()

label_weather = tk.Label(root, text="Какая была погода летом?")
label_weather.pack()
entry_weather = tk.Entry(root)
entry_weather.pack()

label_event = tk.Label(root, text="Какое событие запомнилось больше всего?")
label_event.pack()
entry_event = tk.Entry(root)
entry_event.pack()

label_class = tk.Label(root, text="Какой класс вы посещаете?")
label_class.pack()
entry_class = tk.Entry(root)
entry_class.pack()

button_submit = tk.Button(root, text="Создать сочинение", command=create_composition)
button_submit.pack()

text = tk.StringVar(value = "")

label_result = tk.Label(root, textvariable=text, justify="left")
label_result.pack()

root.mainloop()

