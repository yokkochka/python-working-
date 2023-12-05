from tkinter import *
import random

root = Tk()
root.title('Кнопки')
root.geometry('250x250')

def click():
    colors = ['brown', 'silver', "gray", "pink", "dark blue", "red", 'blue', "green", "yellow", "orange"]
    btn.configure(bg=random.choice(colors))
    lbl = Label(root, bg='black', text='Правильная кнопка', font=("Arial", 12), fg="dark blue")
    lbl.place(x=0, y=0, width=250, height=75)

def click_1():
    colors = ["red", 'blue', "green", "yellow", "orange", "purple"]
    colors_1 = ['brown', 'silver', "black", "gray", "pink", "dark blue"]
    lbl = Label(root, bg='black', text='Неправильная кнопка', font=("Arial", 12), fg="white")
    lbl.place(x=0, y=175, width=250, height=75)
    lbl.configure(fg=random.choice(colors), bg=random.choice(colors_1))

btn = Button(root, bg='red', text='1', font=("Ariel", 15), command=click)
btn1 = Button(root, bg='blue', text='2', font=("Ariel", 15), command=click_1)
btn2 = Button(root, bg='green', text='3', font=("Ariel", 15), command=click_1)
btn3 = Button(root, bg='yellow', text='4', font=("Ariel", 15), command=click_1)
btn.place(x=0,y=75,width=125,height=50)
btn1.place(x=125,y=75,width=125,height=50)
btn2.place(x=0,y=125,width=125,height=50)
btn3.place(x=125,y=125,width=125,height=50)

root.mainloop()