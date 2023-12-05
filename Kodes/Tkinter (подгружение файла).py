# from tkinter import *
# from tkinter import messagebox as mb
# from tkinter import filedialog as fd
# 
# root = Tk()
# 
# def openfile():
#     file = fd.askopenfilename()
#     if len(file) > 32:
#         mb.showinfo(message = "Файл представляет угрозу")
#     else:
#         mb.showinfo(message = "Файл прошел проверку")
# 
# btn = Button(text='Открыть файл', command=openfile)
# btn.pack()
# 
# root.mainloop()






from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

root = Tk()

def openfile():
    file = fd.askopenfilename()
    label['text'] = file

def openfiles():
    files = fd.askopenfilenames()
    for file in files:
        filelist.insert(END, file)
    
btn = Button(text='Открыть файл', command=openfile)
btn.pack()
label = Label(height=3)
label.pack()

s_btn = Button(text='Открыть файлы', command=openfiles)
filelist = Listbox(width=85)
s_btn.pack()
filelist.pack()

root.mainloop()