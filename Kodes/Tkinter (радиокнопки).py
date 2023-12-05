# from tkinter import *
# 
# root = Tk()
# 
# r1 = Radiobutton(text='Первая кнопка')
# r2 = Radiobutton(text='Вторая кнопка')
# 
# r1.pack()
# r2.pack()
# 
# root.mainloop()


# from tkinter import *
# 
# root = Tk()
# 
# r_var = BooleanVar()
# r_var.set(0)
# r1 = Radiobutton(text="Первая кнопка", variable=r_var, value=0)
# r2 = Radiobutton(text="Вторая кнопка", variable=r_var, value=1)
# 
# r1.pack()
# r2.pack()
# 
# root.mainloop()

from tkinter import *

root = Tk()

def change():
    if var.get() == 0:
        label["text"] = "Смешарики, Шрек"
    elif var.get() == 1:
        label["text"] = "Мстители, Работа над ошибками"
    elif var.get() == 2:
        label["text"] = "Унесенные ветром, Кинг-Конг"


var = IntVar()
var.set(0)
label_1 = Label(text="Наши рекомендации для вас:")

r1 = Radiobutton(text="0-7", variable=var, value=0)
r2 = Radiobutton(text="7-14", variable=var, value=1)
r3 = Radiobutton(text="14-21", variable=var, value=2)

button = Button(text="Изменить", command=change)
label = Label(width=40, height=10)


label_1.pack()

r1.pack()
r2.pack()
r3.pack()
button.pack()
label.pack()

root.mainloop()

