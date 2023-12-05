from tkinter import *

root = Tk()

def btn1_click():
    pass_label['text'] = pass_label['text'] + "1"

def btn2_click():
    pass_label['text'] = pass_label['text'] + "2"

def btn3_click():
    pass_label['text'] = pass_label['text'] + "3"

def btn4_click():
    pass_label['text'] = pass_label['text'] + "4"

def btn5_click():
    pass_label['text'] = pass_label['text'] + "5"

def btn6_click():
    pass_label['text'] = pass_label['text'] + "6"

def btn7_click():
    pass_label['text'] = pass_label['text'] + "7"

def btn8_click():
    pass_label['text'] = pass_label['text'] + "8"

def btn9_click():
    pass_label['text'] = pass_label['text'] + "9"
    
def password():
    val_pass = '123456789'
    if val_pass == pass_label['text']:
        check_label['text'] = 'Открыто'
    else:
        check_label['text'] = 'Закрыто'

pass_label = Label()
btn_frame = Frame(root)

btn1 = Button(btn_frame, text='1', command=btn1_click)
btn2 = Button(btn_frame, text='2', command=btn2_click)
btn3 = Button(btn_frame, text='3', command=btn3_click)
btn4 = Button(btn_frame, text='4', command=btn4_click)
btn5 = Button(btn_frame, text='5', command=btn5_click)
btn6 = Button(btn_frame, text='6', command=btn6_click)
btn7 = Button(btn_frame, text='7', command=btn7_click)
btn8 = Button(btn_frame, text='8', command=btn8_click)
btn9 = Button(btn_frame, text='9', command=btn9_click)

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

submit_btn = Button(text='Проверка', command=password)
check_label = Label()


submit_btn.pack()
check_label.pack()
btn_frame.pack()
pass_label.pack()
root.mainloop()
