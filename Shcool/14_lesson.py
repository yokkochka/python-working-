#Первый блок - работа с canvas

from tkinter import *
root = Tk()
root.title('Холст')

canvas = Canvas(bg = 'red', width = 100, height = 250)    # Создаем холст, заливаем цветом, задаем размеры
canvas.pack()    # Отображаем
print(canvas['width'],canvas['height'])   # Выведет ширину и высоту холста в пкс

# Практика - создание второго холста
second_canvas = Canvas(bg = 'black')
second_canvas.pack()
print(second_canvas['width'],second_canvas['height'])

# Второй способ поменять размеры:
# canvas['width'] = 100
# canvas['height'] = 100
# print(canvas['width'],canvas['height'])

# Третий способ поменять размеры:
# canvas.configure(width = 750)
# canvas.configure(height = 100)
# print(canvas['width'],canvas['height'])

root.mainloop()




#Второй блок работа с canvas, все остальное в коммент
from tkinter import *
root = Tk()
root.title('Холст')
canvas = Canvas(bg = 'red', width = 750, height = 550)
canvas.pack()
canvas.create_line(0,0,750,550)    # Первая линия
canvas.create_line(750, 0, 0, 550)
canvas.create_rectangle(250,100,345,150, fill = 'yellow', outline = 'green', width = 3, activefill = 'white')
# Создаем прямоугольник(строчкой выше)
canvas.create_oval(50, 500, 150, 540)    # Создаем овал
canvas.create_polygon(10, 150, 40, 100, 70, 150)    # Создаем многоугольник(треугольник)


root.mainloop()


