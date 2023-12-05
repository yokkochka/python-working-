import tkinter as tk

class Calculator:
    def __init__(self):
        # Активное окно
        self.window = tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(0,0)
        self.window.title('Calculator')
        # Словари
        self.digits = {7:(1,1), 8:(1,2), 9:(1,3),
                       4:(2,1), 5:(2,2), 6:(2,3),
                       1:(3,1), 2:(3,2), 3:(3,3),
                       0:(4,2), '.':(4,1)}
        
        
        self.operations = {'/':'\u00F7','+':'+', '-':'-', '*':'x'}
        
        # Значения выражений
        self.total_expression = ''
        self.current_expression = ''
        
        
        # Создание рамок дисплея и кнопок
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        
        self.total_label, self.label =self.create_display_labels()
        
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_sqrt_button()
        self.create_square_button()
        self.create_equals_button()
        self.create_clear_button()
        
        self.buttons_frame.rowconfigure(0, weight = 1)
        
        for i in range(1,5):
            self.buttons_frame.rowconfigure(i, weight = 1)
            self.buttons_frame.columnconfigure(i, weight = 1)
        
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
        
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text='\u221ax', bg = 'white', fg = 'black', font=('Arial', 24, 'bold'), borderwidth = 0, command = self.sqrt)
        button.grid(row=0,column = 3, sticky = tk.NSEW)
        
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()
        
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text='x\u00b2', bg = 'white', fg = 'black', font=('Arial', 24, 'bold'), borderwidth = 0, command = self.square)
        button.grid(row=0,column = 2, sticky = tk.NSEW)
        
    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_label()
        self.update_total_label()    
        
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg = 'white', fg = 'black', font=('Arial', 24, 'bold'), borderwidth = 0, command = self.clear)
        button.grid(row=0, column = 1, sticky = tk.NSEW)
    
    # Равно
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg = 'lightblue', fg = 'black', font=('Arial', 24, 'bold'), borderwidth = 0, command= self.evaluate)
        button.grid(row=4, column = 3, columnspan = 2, sticky = tk.NSEW)
     
     
     
    # Кнопки операций
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg = 'white', fg = 'black', font=('Arial', 24, 'bold'), borderwidth = 0, command = lambda x=operator: self.append_operator(x))
            button.grid(row=i,column = 4, sticky = tk.NSEW)
            i += 1    
     
    # Кнопки цифр
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg='white', fg = 'black', font=('Arial', 24, 'bold'), borderwidth = 0, command = lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column = grid_value[1], sticky=tk.NSEW)
    
    # Строки ввода выражения   
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg = '#F5F5F5', fg = '#25262E', padx = 24, font=('Arial',40, 'bold'))
        total_label.pack(expand = True, fill = 'both')
        
        label = tk.Label(self.display_frame, text = self.current_expression,anchor = tk.E, bg='#F5F5F5', fg = 'black',padx = 24, font = ('Arial', 40, 'bold'))
        label.pack(expand = True, fill = 'both')
        return total_label, label
    
      
    # 
    def append_operator(self,operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_total_label()
        self.update_label()
        
        #button = tk.Button(self,buttons_frame, text = symbol, bg = 'white', fg = 'black', font = ('Arial', 24, 'bold'), borderwidth = 0, command = lambda x=digit: self.add_to_expression(x))
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ''
        except ZeroDivisionError:
            self.current_expression = 'Error'
        finally:
            self.update_label()
    
    
     # Рамка дисплея   
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg='#F5F5F5')
        frame.pack(expand=True, fill='both')    # астянется на всю возможную ширину 
        return frame
    
    # Рамка дисплея кнопок
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame
    
    # Заполнение текущего выражения
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    # Обновление строк выражений
    def update_total_label(self):
        expression= self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text = self.total_expression)
        
    def update_label(self):
        self.label.config(text = self.current_expression[:11])
     

    # Чтобы программа не закрывалась сама по себе
    def run(self):
        self.window.mainloop()
      
      
if __name__ == "__main__":    #позволяет запустить класс как отдельную програмку
    calc = Calculator()
    calc.run()

