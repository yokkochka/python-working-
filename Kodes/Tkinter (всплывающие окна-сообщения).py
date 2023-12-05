from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

root = Tk()

def check():
    answer = mb.askyesno(
        message="Произвести операцию?")
    if answer:
        mb.showinfo('Ок, сейчас будет произведена операция!')
        label['text'] = "Мир"
root = Tk()
btn = Button(text='Вывести надпись', command=check)
btn.pack()
label = Label(height=3)
label.pack()

root.mainloop()