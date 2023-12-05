import tkinter as tk
import random as rnd
 


class Task:
    def __init__(self):
        # Создаем окно приложения
        self.root = tk.Tk()

        self.root.title("METANIT.COM")    # Даем название окну
        self.root.geometry("1200x500")
        self.list_applications = []

        self.canvas = tk.Canvas(width = 1200,height = 500)
        self.canvas.pack()
        self.list_distances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.genetate_buttons()
        self.create_processes()

        
    # Функция, которая создает кнопку генерации взодящих заявок
    def genetate_buttons(self):
        btn1 = tk.Button(text="Generate", command = self.generate_applications)
        btn1.place(x = 570, y=470)
        
    def create_processes(self):
        lbl2 = tk.Label(text = "Processing", background = "lightgrey", width = 170, height = 2)
        lbl2.place(x = 0, y = 130)

        lbl3 = tk.Label(text = "Storage device", background = "lightgrey", width = 170, height = 2)
        lbl3.place(x = 0, y = 220)

        lbl4 = tk.Label(text = "Successfully", background = "lightgrey", width = 170, height = 2)
        lbl4.place(x = 0, y = 300)

        lbl5 = tk.Label(text = "Unsuccessful", background = "lightgrey", width = 170, height = 2)
        lbl5.place(x = 0, y = 380)

    def generate_applications(self):
        list_appl = []
        k = 1
        while (k <= 11):
            rand = rnd.randint(1,10000)/1000
            count = 0
            for j in range(len(list_appl)):
                if abs(list_appl[j] - rand) >= 0.4:
                    count += 1
            if count == len(list_appl):
                list_appl.append(rand)
                k += 1
                
        list_appl.sort()
        j = 0

        for i in range(1, 11):
            self.list_applications.append(list([i, list_appl[j], rnd.randint(10,30)/10]))
            j += 1

        for i in range(10):
            self.list_distances[i] = round(self.list_applications[i][1]*100, 3)
        self.generate_labels()
        print(self.list_applications)
        print(self.list_distances)

    def generate_labels(self):
        lbl1 = tk.Label(text = str(self.list_applications[0][1]))
        lbl1.place(x =self.list_distances[0], y = 30)

        lbl2 = tk.Label(text = str(self.list_applications[1][1]))
        lbl2.place(x = self.list_distances[1], y = 30)

        lbl3 = tk.Label(text = str(self.list_applications[2][1]))
        lbl3.place(x = self.list_distances[2], y = 30)

        lbl4 = tk.Label(text = str(self.list_applications[3][1]))
        lbl4.place(x = self.list_distances[3], y = 30)

        lbl5 = tk.Label(text = str(self.list_applications[4][1]))
        lbl5.place(x = self.list_distances[4], y = 30)

        lbl6 = tk.Label(text = str(self.list_applications[5][1]))
        lbl6.place(x = self.list_distances[5], y = 30)

        lbl7 = tk.Label(text = str(self.list_applications[6][1]))
        lbl7.place(x = self.list_distances[6], y = 30)

        lbl8 = tk.Label(text = str(self.list_applications[7][1]))
        lbl8.place(x = self.list_distances[7], y = 30)

        lbl9 = tk.Label(text = str(self.list_applications[8][1]))
        lbl9.place(x = self.list_distances[8], y = 30)

        lbl10 = tk.Label(text = str(self.list_applications[9][1]))
        lbl10.place(x = self.list_distances[9], y = 30)

        self.canvas.create_line(0, 25, 1150, 25,arrow="last")
        lbl11 =tk.Label(text = "t")
        lbl11.place(x=1150, y = 26)

        self.process()
        
    def process(self):
        time_processing = 0
        time_storage = 0
        color = '#6495ED'

        for i in range(10):
            if time_processing == 0:
                time_processing += (self.list_applications[i][2] + self.list_applications[i][1])
                self.canvas.create_line(self.list_distances[i]+10, 50, self.list_distances[i]+10, 150, time_processing*100+10, 150, time_processing*100+10, 300, activefill=color, width=3, arrow="last")
            elif time_storage == 0:
                time_storage += (self.list_applications[i][2] + self.list_applications[i][1])
                self.canvas.create_line(self.list_distances[i]+10, 50, self.list_distances[i]+10, 250, time_storage*100+10, 250, time_storage*100+10, 300, activefill=color, width=3, arrow="last")
            elif self.list_applications[i][1] >= time_processing:
                time_processing = (self.list_applications[i][2] + self.list_applications[i][1])
                self.canvas.create_line(self.list_distances[i]+10, 50, self.list_distances[i]+10, 150, time_processing*100+10, 150, time_processing*100+10, 300, activefill=color, width=3, arrow="last")
            elif self.list_applications[i][1] >= time_storage:
                time_storage = (self.list_applications[i][2] + self.list_applications[i][1])
                self.canvas.create_line(self.list_distances[i]+10, 50, self.list_distances[i]+10, 250, time_storage*100+10, 250, time_storage*100+10, 300, activefill=color, width=3, arrow="last")
            else:
                self.canvas.create_line(self.list_distances[i]+10, 50, self.list_distances[i]+10, 380, activefill=color, width=3, arrow="last")
            

    def run(self):
        self.root.mainloop()
        



 
if __name__ == "__main__": 
    task = Task()
    task.run()




