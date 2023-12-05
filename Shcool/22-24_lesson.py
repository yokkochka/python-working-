import tkinter as tk
import time, random

root= tk.Tk()
root.title('Прыг-скок')
root.resizable(0,0)
root.wm_attributes('-topmost', 1)
canvas = tk.Canvas(root, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
root.update()

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.hit_bottom = False
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if (pos[3]+10) >= paddle_pos[1] and (pos[3]+10) <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            
        if self.hit_paddle(pos)==True:
            self.y = -2
            
            
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            
    
            
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = color)
        self.canvas.move(self.id,250,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        
    def turn_right(self, event):
        self.x = 2
    def turn_left(self,event):
        self.x = -2
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450,10,text=self.score,font=('Courier', 15), fill = color)
        
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)
            



paddle = Paddle(canvas, 'white')
ball = Ball(canvas, paddle, 'red')

while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
        root.update_idletasks()
        root.update()
        time.sleep(0.01)
