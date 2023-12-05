from tkinter import *

def red_button_pressed():
    lab["text"] = "Красный - Стой!"


def yellow_button_pressed():
    lab["text"] = "Желтый - Погоди!"


def green_button_pressed():
    lab["text"] = "Зеленый - Можно ехать!"
root = Tk()
lab = Label(width=40)

button_red = Button(command=red_button_pressed, bg="red", width=10)
button_yellow = Button(command=yellow_button_pressed, bg="yellow", width=10)
button_green = Button(command=green_button_pressed, bg="green", width=10)


lab.pack()
button_red.pack()
button_yellow.pack()
button_green.pack()

root.mainloop()