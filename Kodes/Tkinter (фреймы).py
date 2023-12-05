# from tkinter import *
# 
# root = Tk()
# 
# topframe = Frame(root)
# botframe = Frame(topframe)
# 
# first_label = Label(topframe, width=10, bg='red', text="Первый")
# second_label = Label(topframe, width=10, bg='yellow', text="Второй")
# third_label = Label(botframe, width=10, bg='green', text="Третий")
# fourth_label = Label(botframe, width=10, bg='blue', text="Четвертый")
# 
# topframe.pack()
# botframe.pack()
# first_label.pack(side=LEFT)
# second_label.pack(side=LEFT)
# third_label.pack(side=LEFT)
# fourth_label.pack(side=LEFT)
# 
# root.mainloop()







from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

f_entry = Entry(frame)
s_entry = Entry(frame)
t_entry = Entry(frame)
button = Button(frame, text="Отправить")

f_entry.grid(row=0, column=0)
s_entry.grid(row=0, column=1)
t_entry.grid(row=0, column=2)
button.grid(row=1, column=1)

root.mainloop()