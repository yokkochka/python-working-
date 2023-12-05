from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os

root = Tk()

def open_file():
    file = fd.askopenfilename()
    answer = mb.askyesno(message="Удалить файл?")
    if answer:
        os.remove(file)
        mb.showinfo('', 'Файл удален')

btn = Button(text='Открыть файл', command=open_file)

btn.pack()
root.mainloop()
