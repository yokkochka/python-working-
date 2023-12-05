import turtle
t = turtle.Pen()
ts = turtle.Screen()
ts.title('Rakushka')
t.speed(100)
ts.setup(1000,1000)
ts.bgcolor('black')
t.color('white')

size = 5

for i in range(70):

    t.circle(size)
    t.left(5)
    size+= 3