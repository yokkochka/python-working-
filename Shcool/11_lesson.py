# import turtle
# t = turtle.Pen()    #необходимо для рисования
# t.shape('turtle')    #курсор
# 
# t.color('green')    #цвет
# t.pensize(2)    #ширина
# t.forward(100)    #команда, которая двигает ручку вперед
# 
# t.left(45)    #поворот налево на 45 градусов
# t.color('yellow')
# t.pensize(5)
# t.forward(100)
# 
# t.right(87)
# t.color('red')
# t.pensize(1)
# t.forward(100)
# 
# t.left(45)
# t.backward(100)   # рисовать не вперед, а назад
# 
# for i in range(36):
#     t.circle(100)
#     t.left(50)
# 
# 
# #Отрисовка квадрата
# import turtle
# t = turtle.Pen()
# t.shape('turtle')
# t.color('red')
# t.pensize(5)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# Второй вариант отрисовки квадрата + заливка

# import turtle
# t = turtle.Pen()
# t.up()    #поднять перо
# t.goto(200,200)
# t.shape('turtle')
# t.color('red')
# turtle.bgcolor('violet')    #цвет фона
# 
# t.fillcolor('red')    #обозначаем цвет заливки и фигуры
# t.begin_fill()    #отмечаем начало заливки
# t.down()    #опустить перо
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# t.end_fill()


# Прикольный цикл
# t2 = turtle.Pen()
# t2.up()
# t2.goto(-100,-100)
# t2.shape('circle')
# t2.color('blue')
# 
# t2.fillcolor('blue')
# t2.begin_fill()
# t2.down()
# for i in range(36):
#     t2.forward(100)
#     t2.left(50)
# t2.end_fill()
#     
    

import turtle
t = turtle.Pen()
ts = turtle.Screen()
ts.title('Rakushka')
t.speed(100)
ts.setup(1000,1000)
ts.bgcolor('black')
t.color('white')

size = 0
for i in range(70):
    t.circle(size)
    t.left(5)
    size+= 3



  


