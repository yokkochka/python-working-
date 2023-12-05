from tkinter import*

def destroy():    # Функция цдаления button
    btn.destroy()    # Метод для удаления виджета

def hello():    # Задание
    print('Hello')
    btn_hello['bg'] = 'purple'
    root['bg'] = 'yellow'

def print_click():
    print('клик')
    btn.configure(bg = 'blue')    # Меняем цвет после
    root['bg'] = 'black'    # Изменение цвета стартового окна

root = Tk()

root.title('Стартовое окно')    # Заголовок
root.geometry('500x500')    # Размеры стартового окна
root['bg'] = 'red'    # Цвет фона

#метод grid
btn = Button(root, bg ='green', text ='button', font = ('Ariel', 15, 'bold'), command = print_click)
#при нажатии на кнопку будет запускаться функция, указанная в command
btn.grid(column = 2, row = 3)    #расположение кнопки

btn_hello = Button(root, bg = 'yellow', text = 'Hello', font = ('Arial', 15), command = hello)
btn_hello.grid(column = 0, row = 2, ipadx = 5, ipady = 4)    # ipax и ipay - внутренние отступы

delete_button = Button(root, bg ='purple', text ='Удалить кнопку button', font = ('Ariel', 15), command = destroy)
delete_button.grid(column = 1, row = 1, columnspan = 2, padx = 7, pady = 10)
#columnspan - сколько стобиков займет виджет, padx/pady внешние отступы кнопки от сетки

root.mainloop()