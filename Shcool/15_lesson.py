# Игра сщик

from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=1000, height = 500, bg = 'black')
canvas.pack()


light = canvas.create_oval(20,20,120,120, fill = 'white')

# for i in range(80):
#     canvas.move(light, 5, 0)
#     canvas.update()
#     time.sleep(0.05)

def move_light(event):
    if event.keysym == 'Up':
        canvas.move(light, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(light, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(light,-5, 0)
    elif event.keysym == 'Right':
        canvas.move(light, 5, 0)
        
canvas.bind_all('<Up>', move_light)
canvas.bind_all('<Down>', move_light)
canvas.bind_all('<Left>', move_light)
canvas.bind_all('<Right>', move_light)

canvas.create_text(100, 100, text='Hello world!', fill = 'black', font=('Arial', 30))
        
        
        
tk.mainloop()