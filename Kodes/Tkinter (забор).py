from tkinter import *

def oak_fence():
    num = int(your_entry.get())
    if num >= 6:
        result_label['text'] = 'Досок хватает'
    else:
        result = 'Не хватило досок: '+ str(6 - num)
        result_label['text'] = result
        
root = Tk()

greetings = Label(width=40,text="Сколько досок есть в инвентаре?")
your_entry = Entry(width=40)
your_button = Button(text="Посчитать", command=oak_fence)
result_label = Label(width=40)

greetings.pack()
your_entry.pack()
your_button.pack()
result_label.pack()

root.mainloop()



# from tkinter import *
# def oak_fence():
#     num = int(your_entry.get())
#     if num >= 6:
#         result_label["text"] = "Досок хватает!"
#     else:
#         result = "Не хватило " + str(6 - num) + " досок :("
#         result_label["text"] = result
# 
# 
# root = Tk()
# 
# greetings = Label(width=40, text="Сколько есть досок в инвентаре?", font="Courier", background="light blue")
# your_entry = Entry(width=40)
# your_button = Button(text="Посчитать", command=oak_fence, background="light yellow")
# result_label = Label(width=40, background="peach puff", fg="blue")
# 
# greetings.pack()
# your_entry.pack()
# your_button.pack()
# result_label.pack()
# 
# root.mainloop()