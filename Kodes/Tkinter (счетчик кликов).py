from tkinter import *
def button_pressed():
    lab_2['text'] = str(int(lab_2['text']) + 1)

root = Tk()
lab = Label(width=40, text="Всего кликов:")
lab_2 = Label(width=40, text = '0')
button = Button(width=10, text="Кликай", command=button_pressed)

lab.pack()
lab_2.pack()
button.pack()

root.mainloop()