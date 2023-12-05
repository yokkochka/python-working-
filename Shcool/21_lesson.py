class Zoo_animal:
    def __init__(self, weight, food, sleep):
        self.weight = weight
        self.food = food
        self.sleep = sleep

class Reptiles(Zoo_animal):
    def __init__(self, weight, food, sleep, period):
        super().__init__(weight, food, sleep)
        self.period = period
        
class Birds(Zoo_animal):
    def __init__(self, weight, food, water, sleep, feather_color):
        super().__init__(weight, food, sleep)
        self.feather_color = feather_color

class Predator(Zoo_animal):
    def __init__(self, weight, food, water, sleep, fangs_size):
        super().__init__(weight, food, sleep)
        self.fangs_size = fangs_size      


elephant = Zoo_animal(5000, 'grass', 2 )
print('Cлон', elephant.weight, elephant.food, elephant.sleep)

python = Reptiles(60, 'birds', 18, 35 )
print('Питон', python.weight, python.food, python.sleep, python.period)

parrot = Birds(0.1, 'Семена', 11, 'Голубой')
print('Попугай', parrot.weight, parrot.food, parrot.sleep, parrot.feather_color)

lion = Predator(190, 'Мясо', 20, 6)
print('Лев', lion.weight, lion.food, lion.sleep, lion.fangs_size)


class Paren1:
    def func1(self):
        print("Это функция первого родительского класса")
class Paren2:
    def func2(self):
        print("Это функция второго родительского класса")

class Child(Paren1,Paren2):
    def func3(self):
        print("Это функция дочернего класса")

child=Child()
child.func1()
child.func2()
child.func3()


