from tkinter import *
from tkinter import messagebox as mb

root = Tk()

def def_counter():
    count = int(br_entry.get()) + int(lan_entry.get()) + int(din_entry.get())
    mb.showinfo('', count)
    
def clean1():
    br_entry.delete(0,END)
    
def clean2():
    lan_entry.delete(0,END)
    
def clean3():
    din_entry.delete(0,END)
    

frame = Frame(root)

br_label = Label(frame, text='Завтрак', width=10)
br_entry = Entry(frame, width=10)
br_button = Button(frame, text='Очистить', width=10, command=clean1)

lan_label = Label(frame, text='Обед', width=10)
lan_entry = Entry(frame, width=10)
lan_button = Button(frame, text='Очистить', width=10, command=clean2)

din_label = Label(frame, text='Ужин', width=10)
din_entry = Entry(frame, width=10)
din_button = Button(frame, text='Очистить', width=10, command=clean3)

counter = Button(text='Рассчитать калории', command=def_counter)



br_label.grid(row=0, column=0)
br_entry.grid(row=0, column=1)
br_button.grid(row=0, column=2)
lan_label.grid(row=1, column=0)
lan_entry.grid(row=1, column=1)
lan_button.grid(row=1, column=2)
din_label.grid(row=2, column=0)
din_entry.grid(row=2, column=1)
din_button.grid(row=2, column=2)



frame.pack()
counter.pack()
root.mainloop()