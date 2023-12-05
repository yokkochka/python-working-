import turtle
ts = turtle.Screen()
ts.setup(1000, 1000)
turtle.bgcolor('violet')

ts.title('Сложня черепашья графика')

t = turtle.Pen()
t.hideturtle()    #сделает черепашку у линии невидимой

# t.shape('circle')
# t.color('blue')
# t.forward(200)
# 
# ts.clear()    #отчищает область


#для спирали с кружочками то что выше ДОЛЖНО БЫТЬ НЕ ЗАКОМЕНЧЕНО
# turtle.bgcolor('black')
# colors = ['red', 'green', 'blue', 'yellow']
# quantity = len(colors)
# for i in range(100):
#     t.pencolor(colors[i%quantity])
#     t.circle(i)
#     t.left(91)
    
#для спирали с именами
# t.speed(20)
# turtle.bgcolor('black')
# colors = ['red', 'green', 'blue', 'yellow']
# quantity = len(colors)
# Ulyana = turtle.textinput('Ведите имя', 'Как тебя зовут?')    #вводим свое имя
# for i in range(100):
#     t.pencolor(colors[i%quantity])    #смена цвета
#     t.up()    #обязательно поднимаем и опускаем перо, чтобы за именем не тянулась прямая
#     t.forward(i*4)    #увеличение расстояния, если этого не будет, то будет наслоение
#     t.down()
#     t.write(Ulyana, font = ('Arial', int((i+4)/4)))    #выводит текст, который мы вводим + увеличение шрифта
#     t.left(91)

#отрисовка вируса
# turtle.bgcolor('black')
# t.speed(50)
# t.color('green')
# t.up()
# b = 0
# t.goto(0,0)
# t.down()
# while b < 200:
#     t.right(b)
#     t.forward(b*3)
#     b += 1
    
#Отрисовка самолетика ВСЕ КРОМЕ ЭТОГО КОДА В КОММЕНТ
import turtle
t = turtle.Pen()
ts = turtle.Screen()
ts.title('Самолетик')

# Солнышко
t.up()
t.goto(250,250)
t.down()
t.color('yellow')
t.fillcolor('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()

# Правое крыло
t.color('black')
t.pensize(5)
t.up()
t.home()    # Вернет ручку в изначальное положение
t.down()
t.fillcolor('blue')
t.begin_fill()
t.goto(-300,150)
t.goto(100,50)
t.goto(0,0)
t.end_fill()

# Тело самолетика
t.goto(-30,-125)
t.goto(-50,-50)
# 
# 
# Левое крыло
t.fillcolor('blue')
t.begin_fill()
t.goto(-300,150)
t.goto(-125,-125)
t.goto(-50,-50)
t.goto(-30,-125)
t.goto(-85,-85)
t.end_fill()

# # Линии от движения
# 
t.pensize(3)
t.up()
t.goto(75,25)
t.down()
t.goto(200,0)
t.up()
t.goto(50,-5)
t.down()
t.goto(250,-30)
t.up()
t.goto(10,-80)
t.down()
t.goto(100,-150)
t.penup()
t.goto(-80,-125)
t.pendown()
t.goto(120,-200)












