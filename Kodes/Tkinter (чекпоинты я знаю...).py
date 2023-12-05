from tkinter import *

def check():
    label['text'] = 'Я знаю:' + var1.get() + ', ' + var2.get() + ', ' + var3.get()

root = Tk()

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()


first_check = Checkbutton(text="Python", variable=var1, onvalue="Python", offvalue='', command=check)
second_check = Checkbutton(text="Java", variable=var2, onvalue="Java", offvalue='', command=check)
third_check = Checkbutton(text="C#", variable=var3, onvalue="C#", offvalue='', command=check)
label = Label(width=25, height=5)

first_check.pack()
second_check.pack()
third_check.pack()
label.pack()

root.mainloop()