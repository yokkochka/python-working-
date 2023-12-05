from tkinter import *

def check():
    if var1.get() == 1 and var2.get() == 1:
        label['text'] = "Обе кнопки нажаты"
    elif var1.get() == 1 and var2.get() == 0:
        label['text'] = "Первая кнопка нажата"
    elif var1.get() == 0 and var2.get() == 1:
        label['text'] = "Вторая кнопка нажата"
    else:
        label['text'] = "Ничего не выбрано"

root = Tk()

var1 = BooleanVar()
var1.set(0)
var2 = BooleanVar()
var2.set(0)

first_check = Checkbutton(text="Первая кнопка", variable=var1, onvalue=1, offvalue=0, command=check)
second_check = Checkbutton(text="Вторая кнопка", variable=var2, onvalue=1, offvalue=0, command=check)
label = Label(text="Ничего не выбрано", width=25, height=5)

first_check.pack()
second_check.pack()
label.pack()

root.mainloop()