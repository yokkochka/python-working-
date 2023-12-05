from tkinter import *
 
root = Tk()
frame = Frame(root)

def add_tasks():
    tasks_listbox.insert(END, tasks_entry.get())
    tasks_entry.delete(0, END)

def moving_tasks(): 
    completed_listbox.insert(END, tasks_listbox.get(tasks_listbox.curselection()))    #  Добавляю в список выполненных задач по возвращенному индексу выбранного курсором элемента
    tasks_listbox.delete(tasks_listbox.curselection())    #  Удаляю этот элемент из исподного списка
    
    
def add_completed():
    completed_listbox.insert(END, completed_entry.get())
    completed_entry.delete(0, END)
    
def moving_completed(): 
    tasks_listbox.insert(END, completed_listbox.get(completed_listbox.curselection())) 
    completed_listbox.delete(completed_listbox.curselection())
    
lab = Label(frame, text='Задачи')
lab2 = Label(frame, text='Выполнено')

tasks_listbox = Listbox(frame)
tasks_entry = Entry(frame)
tasks_btn = Button(frame, text='Добавить', command=add_tasks)

button = Button(frame, text='Переместить в выполненные', command=moving_tasks)
button2 = Button(frame, text='Переместить в задачи', command=moving_completed)

completed_listbox = Listbox(frame)
completed_entry = Entry(frame)
completed_btn = Button(frame, text='Добавить', command=add_completed)
 
 
lab.grid(row=0, column=0)
lab2.grid(row=0, column=2)

tasks_listbox.grid(row=1, column=0)
tasks_entry.grid(row=2, column=0)
tasks_btn.grid(row=3, column=0)

button.grid(row=2, column=1)
button2.grid(row=3, column=1)

completed_listbox.grid(row=1, column=2)
completed_entry.grid(row=2, column=2)
completed_btn.grid(row=3, column=2)


frame.pack()
root.mainloop()
