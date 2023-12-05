from tkinter import *

root = Tk()

book = {
    0: '445-241-12',
    1: '442-555-41',
    2: '448-112-37',
    3: '441-536-52'
    }

def num():
    lab['text'] = book[var.get()]
    
var = IntVar()

Vasya = Radiobutton(text="Вася", variable=var, value=0, indicatoron=0)
Misha = Radiobutton(text="Миша", variable=var, value=1, indicatoron=0)
Senya = Radiobutton(text="Сеня", variable=var, value=2, indicatoron=0)
Dima = Radiobutton(text="Дима", variable=var, value=3, indicatoron=0)

button = Button(text="Узнать номер", command = num)
lab = Label(width=20, height=10)

Vasya.pack()
Misha.pack()
Senya.pack()
Dima.pack()
button.pack()
lab.pack()

root.mainloop()