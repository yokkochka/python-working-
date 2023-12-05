from tkinter import *

def fun_addition():
    num_1 = int(first_num.get())
    num_2 = int(second_num.get())
    result_lab['text'] = str(num_1 + num_2)

def fun_subtraction():
    num_1 = int(first_num.get())
    num_2 = int(second_num.get())
    result_lab['text'] = str(num_1 - num_2)

def fun_multiplication():
    num_1 = int(first_num.get())
    num_2 = int(second_num.get())
    result_lab['text'] = str(num_1 * num_2)
    
def fun_division():
    num_1 = int(first_num.get())
    num_2 = int(second_num.get())
    result_lab['text'] = str(num_1 / num_2)

root = Tk()

lab = Label(width=40, text="Введите два числа и выберите что с ними сделать")
first_num = Entry(text="Первое число")
second_num = Entry(text="Второе число")

addition = Button(width=40, text="Сложение", command=fun_addition, bg='#6549D7')
subtraction = Button(width=40, text="Вычитание", command=fun_subtraction, bg='#60D4AE')
multiplication = Button(width=40, text="Умножение", command=fun_multiplication, bg='#FFB740')
division = Button(width=40, text="Деление", command=fun_division, bg='#846FD7')

result_lab = Label(width=40, text="Результат: ")

lab.pack()
first_num .pack()
second_num.pack()
addition.pack()
subtraction.pack()
multiplication.pack()
division.pack()
result_lab.pack()

root.mainloop()