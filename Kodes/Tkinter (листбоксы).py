# from tkinter import *
# 
# root = Tk()
# 
# listbox = Listbox(width=20, height=10, selectmode = SINGLE)
# listbox.pack()
# 
# for element in ("Первый", "Второй", "Третий"):
#     listbox.insert(0, element)
#     
# root.mainloop()



from tkinter import *

root = Tk()

def add_sell():
    listbox.insert(END, entry.get())

listbox = Listbox(width=20, height=10, selectmode = SINGLE)
entry = Entry(width=40)
button = Button(width=40, text='Добавить', command=add_sell)

listbox.pack()
entry.pack()
button.pack()

root.mainloop()