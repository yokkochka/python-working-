# 1
# class Person:
#     # Конструктор класса
#     def __init__(self, name, age):
#         self.name = name  # Атрибут объекта
#         self.age = age    # Атрибут объекта

#     # Метод для вывода приветствия
#     def greet(self):
#         return f"Привет, меня зовут {self.name}, и мне {self.age} лет."
    

# person = Person('Вася', 21)
# print(person.name)  # Вася
# print(person.age)   # 21
# print(person.greet())  # Привет, меня зовут Вася, и мне 21 лет.




# 2
# class Person:
#     """
#     Класс для представления человека.

#     Атрибуты:
#     name (str): Имя человека.
#     age (int): Возраст человека.

#     Методы:
#     greet(): Возвращает строку приветствия.
#     """
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Привет, меня зовут {self.name}, и мне {self.age} лет."

# print(Person.__doc__)  # Строка документации




# 4
# class Counter:
#     def __init__(self):
#         self.count = 0  # Атрибут, отслеживающий значение

#     def increment(self):
#         self.count += 1  # Увеличиваем значение атрибута на 1

#     def get_count(self):
#         return self.count
    
# counter = Counter()
# counter.increment()
# counter.increment()
# print(counter.get_count())  # 2


# 5
# class Example:
#     shared_value = 10  # Атрибут класса

#     def __init__(self, unique_value):
#         self.unique_value = unique_value  # Атрибут объекта
    


# obj1 = Example(5)
# obj2 = Example(15)

# print(obj1.shared_value)  # 10 (общий для всех)
# print(obj2.shared_value)  # 10

# print(obj1.unique_value)  # 5 (уникальный)
# print(obj2.unique_value)  # 15

# obj1.shared_value = 20
# print(obj2.shared_value)  # 20

# Example.shared_value = 25
# obj3 = Example(25)
# print(obj3.shared_value)  # 25


# 6
# class Animal:
#     def eat(self):
#         print("Животное ест.")

# class Dog(Animal):
#     def bark(self):
#         print("Собака лает.")

# dog = Dog()
# dog.eat()  # Наследуется от Animal
# dog.bark()  # Уникальный метод класса Dog


# 7
# class Counter:
#     def __init__(lalala):
#         lalala.count = 0  # Атрибут, отслеживающий значение

#     def increment(lalala):
#         lalala.count += 1  # Увеличиваем значение атрибута на 1

#     def get_count(lalala):
#         return lalala.count
    

# counter = Counter()
# counter.increment()
# counter.increment()
# print(counter.get_count())  # 2



# 8
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Приватный атрибут

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return True
#         return False

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())  # 150

# print(account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'


# 9
# class Animal:
#     def eat(self):
#         print("Животное ест.")

# class Pet:
#     def play(self):
#         print("Домашнее животное играет.")

# class Dog(Animal, Pet):  # Наследуем от двух классов Animal и Pet
#     def bark(self):
#         print("Собака лает.")

# print(Dog.mro())



# # 10
# class A:
#     def show(self):
#         print("Метод класса A")

# class B(A):
#     def show(self):
#         print("Метод класса B")

# class C(A):
#     def show(self):
#         print("Метод класса C")

# class D(B, C):
#     pass

# d = D()
# d.show()  # Метод класса B, т.к. он первый в MRO
# print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# 11

# class Car:
#     def __init__ (self, model, year, mileage):
#         self.model = model
#         self.year = year
#         self.mileage = mileage
    
#     def drive(self, km):
#         self.mileage += km

#     def get_info(self):
#         return f"{self.model} ({self.year}г.), пробег: {self.mileage} км."

# car = Car('Audi', 2018, 0)
# car.drive(100)
# car.drive(200)
# print(car.get_info())  

# car2 = Car('BMW', 2019, 0)
# car2.drive(300)
# car2.drive(400)
# print(car2.get_info())




# practice 1
# class Cat:
#     def say_meow(self):
#         print("Meow, meow, meow!")

# cat = Cat()
# cat.say_meow()



# practice 2
# class Cat:
#     """
#     This is a cat class
#     It has a method say_meow() that outputs the meow of a cat
#     """
#     def say_meow(self):
#         print("Meow, meow, meow!")

# cat = Cat()
# cat.say_meow()

# print(cat.__doc__)


# practice 3
# class Cat:
#     """
#     This is a cat class
#     It has a method say_meow() that outputs the meow of a cat
#     """
#     def __init__ (self, color_eyes, coat_color, breed, tail_length):
#         self.color_eyes = color_eyes
#         self.coat_color = coat_color
#         self.breed = breed
#         self.tail_length = tail_length

#     def say_meow(self):
#         print("Meow, meow, meow!")
    
#     def get_info(self):
#         print(f"Breed: {self.breed}, color of eyes: {self.color_eyes}, coat color: {self.coat_color}, tail length: {self.tail_length}")

# cat_british = Cat("green", "orange", "british", "long")
# cat_mine_coon = Cat("yellow", "grey", "mine coon", "long")
# cat_bobtail = Cat("yellow", "black", "bobtail", "short")

# cat_british.get_info()
# cat_mine_coon.get_info()
# cat_bobtail.get_info()



# practice 4

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}")

# class Worker(Person):
#     def __init__(self, name, job):
#         super().__init__(name)
#         self.job = job
#     def work(self):
#         print(f"Я работаю как {self.job}")

# class Lead(Worker, Person):
#     def __init__(self, name, job):
#         super().__init__(name, job)

#     def i_am_lead(self):
#         print("Я руковожу проектом!")

# people = Lead("Миша", "Менеджер проекта")
# people.introduce()
# people.work()
# people.i_am_lead()



# practice 5

# class Flyable:
#     def fly(self):
#         print("Объект летает")

# class Walkable:
#     def walk(self):
#         print("Объект ходит")

# class Bird(Flyable, Walkable):
#     def chirp(self):
#         print("Птица чирикает")

# bird = Bird()
# bird.fly()
# bird.walk()
# bird.chirp()




# practice 6

# class Product:
#     def __init__(self, name, price, stock):
#         self.__name = name
#         self.__price = price
#         self.__stock = stock
    
#     def set_price(self, price):
#         self.__price = price
    
#     def add_stock(self, amount):
#         self.__stock += amount

#     def sell(self, amount):
#         if self.__stock >= amount:
#             self.__stock -= amount
#             return True
#         return False

#     def get_info(self):
#         return f"Product: {self._name}, price: {self._price}, stock: {self._stock}"
    

# print("Создается объект продукта: молоко, в количестве 10 штук и стоимостью 100 рублей")
# print("Создается объект продукта: кофе, в количестве 5 штук и стоимостью 200 рублей")
# milk = Product("Milk", 100, 10)
# coffee = Product("Coffee", 200, 5)

# print("Симуляция поставки продуктов...")

# amount_coffee = int(input("Сколько кофе привезли на склад? "))
# coffee.add_stock(amount_coffee)
# print("Информация о кофе: ", coffee.get_info())

# amount_milk = int(input("Сколько молока привезли на склад? "))
# milk.add_stock(amount_milk)
# print("Информация о молоке: ", milk.get_info())

# print("Симуляция продажи продуктов...")
# user_choice = input("Какой продукт вы хотите купить? (кофе/молоко) ").lower()

# if user_choice == "кофе":
#     amount = int(input("Сколько пачек кофе вы хотите купить? "))
#     if coffee.sell(amount):
#         print("Продажа успешна")
#     else:
#         print("Продажа не удалась")
#     print("Информация о кофе: ", coffee.get_info()) 
# elif user_choice == "молоко":
#     amount = int(input("Сколько пачек молока вы хотите купить? "))
#     if milk.sell(amount):
#         print("Продажа успешна")
#     else:
#         print("Продажа не удалась")
#     print("Информация о молоке: ", milk.get_info())
# else:
#     print("Такого продукта нет в нашем магазине")






# practice 7

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    

# def print_area(object):
#     print(f"Площадь фигуры: {object.area()}")

# print("Создается объект круга с радиусом 5...")
# circle = Circle(5)
# print_area(circle)

# print("Создается объект прямоугольника с шириной 5 и высотой 10...")
# rectangle = Rectangle(5, 10)
# print_area(rectangle)




# Создайте классы Author, Book, Library. 
# Класс Author должен содержать имя автора и список его книг. 
# Класс Book должен содержать атрибуты title, author и year. 
# Класс Library должен содержать список книг и методы для добавления и поиска книг по названию.
# Реализуйте методы для отображения информации о книге и авторе, геттеры и сеттеры для необходимых атрибутов.
# Создайте несколько авторов, создайте несколько книг, добавьте их в списки соответствующих авторов, в библиотеку и выведите информацию о книгах и авторах.
# Попробуйте найти существующую и несуществующую книги в библиотеке по названию.

# class Author:
#     def __init__(self, name):
#         self.__name = name
#         self.__books = []

#     def get_name(self):
#         return self.__name
    
#     def get_books(self):
#         return self.__books
    
#     def set_name(self, name):
#         self.__name = name

#     def set_books(self, books):
#         self.__books = books

#     def get_info(self):
#         return f"Author: {self.__name}, books: {[i.get_title() for i in self.__books]}"

#     def add_book(self, book):
#         self.__books.append(book)


# class Book:
#     def __init__(self, title, author, year):
#         self.__title = title
#         self.__author = author
#         self.__year = year

#     def get_title(self):
#         return self.__title
    
#     def get_author(self):
#         return self.__author
    
#     def get_year(self):
#         return self.__year
    
#     def set_title(self, title):
#         self.__title = title

#     def set_author(self, author):
#         self.__author = author

#     def set_year(self, year):   
#         self.__year = year

#     def get_info(self):
#         return f"Book: {self.__title}, author: {self.__author}, year: {self.__year}"
    

# class Library:
#     def __init__(self):
#         self.__books = []

#     def add_book(self, book):
#         self.__books.append(book)

#     def find_book(self, title):
#         for book in self.__books:
#             if book.get_title() == title:
#                 return book
#         return None

#     def get_info(self):
#         for book in self.__books:
#             print(book.get_info())


# print("\nСоздается объект автора Джордж Оруэлл...\n")
# author_J_O = Author("Джордж Оруэлл")

# print("Создается объект книги 1984...")
# book_1984 = Book("1984", author_J_O.get_name(), 1949)
# author_J_O.add_book(book_1984)

# print("Создается объект книги Скотный двор...")
# book_S_D = Book("Скотный двор", author_J_O.get_name(), 1945)
# author_J_O.add_book(book_S_D)

# print("Создается объект книги Дорога в Вигенс...")
# book_D_V = Book("Дорога в Вигенс", author_J_O.get_name(), 1934)
# author_J_O.add_book(book_D_V)

# print("\nИнформация о книгах автора:")
# print(author_J_O.get_info())


# print("\nСоздается объект библиотеки...")
# library = Library()
# library.add_book(book_1984)
# library.add_book(book_S_D)
# library.add_book(book_D_V)

# print("\nИнформация о книгах в библиотеке:")
# library.get_info()


# print("\nСоздается объект автора Лев Толстой...\n")
# author_L_T = Author("Лев Толстой")

# print("Создается объект книги Война и мир...")
# book_V_i_M = Book("Война и мир", author_L_T.get_name(), 1869)
# author_L_T.add_book(book_V_i_M)

# print("Создается объект книги Анна Каренина...")
# book_A_K = Book("Анна Каренина", author_L_T.get_name(), 1877)
# author_L_T.add_book(book_A_K)

# print("Создается объект книги Воскресение...")
# book_Voskresenie = Book("Воскресение", author_L_T.get_name(), 1899)
# author_L_T.add_book(book_Voskresenie)

# print("\nИнформация о книгах автора:")
# print(author_L_T.get_info())


# library.add_book(book_V_i_M)
# library.add_book(book_A_K)
# library.add_book(book_Voskresenie)

# print("\nИнформация о книгах в библиотеке:")
# library.get_info()

# print("\nПоиск книги Война и мир в библиотеке...")
# finded_book = library.find_book("Война и мир")
# print(finded_book.get_info() if finded_book != None else "Книга не найдена")

# print("\nПоиск книги Преступление и наказание в библиотеке...")
# finded_book = library.find_book("Преступление и наказание")
# print(finded_book.get_info() if finded_book != None else "Книга не найдена")






# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#     def area(self):
#         return self.__width * self.__height
#     def perimeter(self):
#         return 2 * (self.__width + self.__height)

# rectangle = Rectangle(5, 10)
# print(rectangle.area())
# print(rectangle.perimeter())




# class BankAccount:
#     def __init__(self, code):
#         self.__code = code
#         self.__balance = 0

#     def account_replenishment(self, amount):
#         if amount > 0:
#             print("Пополнение счета на", amount, "рублей")
#             self.__balance += amount
#             return True
#         print("Ошибка")
#         return False
    
#     def account_withdrawal(self, amount):
#         if amount > 0 and self.__balance >= amount:
#             print("Снятие со счета", amount, "рублей")
#             self.__balance -= amount
#             return True
#         print("Ошибка")
#         return False
    
#     def get_info(self):
#         return f"Account: {self.__code}, balance: {self.__balance}"
    
# print("Создается объект банковского счета c кодом '0123456789'...")
# account = BankAccount("0123456789")

# account.account_replenishment(100)

# print(account.get_info())

# account.account_withdrawal(50)

# print(account.get_info())

# account.account_withdrawal(100)

# print(account.get_info())

# account.account_replenishment(-100)

# print(account.get_info())


# from abc import ABC, abstractmethod
# from random import randint

# class Company:
#     def __init__(self, name):
#         self._name = name
#         self._employees = []

#     def add_employee(self, employee):
#         self._employees.append(employee)
    
#     def remove_employee(self, employee):
#         self._employees.remove(employee)
    
#     def calculate_total_salary(self):
#         total_salary = 0
#         for employee in self._employees:
#             total_salary += employee.get_salary()
#         return total_salary
    
#     def get_info(self):
#         for employee in self._employees:
#             print(employee.get_info())


# class Employee(ABC):
#     def __init__(self, name, position, salary):
#         self._name = name
#         self._position = position
#         self._salary = salary
#         self._bonus = False

#     def get_name(self):
#         return self._name
    
#     def get_position(self):
#         return self._position
    
#     def get_bonus(self):
#         return self._bonus

#     def get_salary(self):
#         return self._salary + self.calculate_bonus()
    
#     def set_name(self, name):
#         self._name = name
    
#     def set_position(self, position):
#         self._position = position
    
#     def set_salary(self, salary):
#         if salary > 0:
#             self._salary = salary
#         else:
#             print("Salary must be positive.")
    
#     def set_bonus(self, bonus):
#         if isinstance(bonus, bool):
#             self._bonus = bonus
#         else:
#             print("Bonus must be a boolean value.")
    
#     def get_info(self):
#         return f"Employee: {self._name}, position: {self._position}, salary: {self._salary}, bonus: {self._bonus}"
    
#     @abstractmethod
#     def calculate_bonus(self):
#         pass
    

# class Manager(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, "Manager", salary)
#         self._department = "Management"
    
#     def calculate_bonus(self):
#         if self._bonus:
#             return 0
#         else:
#             return self._salary * 0.4
        
# class Developer(Employee):
#     def __init__ (self, name, salary, programming_language):
#         super().__init__(name, "Developer", salary)
#         self._programming_language = programming_language
    
#     def calculate_bonus(self):
#         if self._bonus:
#             return 0
#         else:
#             return self._salary * 0.5
        
# class HR(Employee):
#     def __init__ (self, name, salary, recruited_employees):
#         super().__init__(name, "HR", salary)
#         self._recruited_employees = recruited_employees
    
#     def get_salary(self):
#         return self._salary + self.calculate_bonus()
    
#     def calculate_bonus(self):
#         if self._bonus:
#             return 0
#         else:
#             return self._salary * (0.01 * self._recruited_employees)


# print("\nСоздается объект компании Company1...")
# company1 = Company("Company1")

# print("Создается объекты сотрудников...")
# for i in range(randint(1, 3)):
#     manager = Manager("Manager" + str(i), randint(20000, 100000))
#     if randint(0,1):
#         manager.set_bonus(True)
#     company1.add_employee(manager)

# for i in range(randint(1, 3)):
#     developer = Developer("Developer" + str(i), randint(20000, 100000), "Python")
#     if randint(0,1):
#         developer.set_bonus(True)
#     company1.add_employee(developer)

# for i in range(randint(1, 3)):
#     hr = HR("HR" + str(i), randint(20000, 100000), randint(1, 10))
#     if randint(0,1):
#         hr.set_bonus(True)
#     company1.add_employee(hr)

# print("\nИнформация о сотрудниках компании Company1:")
# company1.get_info()

# print("\nCоздается объект компании Company2...")
# company2 = Company("Company2")

# print("Создается объекты сотрудников...")
# for i in range(randint(1, 3)):
#     manager = Manager("Manager" + str(i), randint(20000, 100000))
#     if randint(0,1):
#         manager.set_bonus(True)
#     company2.add_employee(manager)

# for i in range(randint(1, 3)):
#     developer = Developer("Developer" + str(i), randint(20000, 100000), ["Java", "Python", "C++"][randint(0, 2)])
#     if randint(0,1):
#         developer.set_bonus(True)
#     company2.add_employee(developer)

# for i in range(randint(1, 3)):
#     hr = HR("HR" + str(i), randint(20000, 100000), randint(1, 10))
#     if randint(0,1):
#         hr.set_bonus(True)
#     company2.add_employee(hr)

# print("\nИнформация о сотрудниках компании Company2:")
# company2.get_info()

# print("\n        Батл компаний этого месяца")
# total_salary_company1 = company1.calculate_total_salary()
# total_salary_company2 = company2.calculate_total_salary()

# print("\nЗарплата сотрудников компании Company1:", total_salary_company1)
# print("Зарплата сотрудников компании Company2:", total_salary_company2)

# if total_salary_company1 > total_salary_company2:
#     print("Победила компания Company1")
# elif total_salary_company1 < total_salary_company2: 
#     print("Победила компания Company2")
# else:
#     print("Ничья")







# class ClothingItem:
#     def __init__(self, name, size, price, quantity):
#         self.__name = name
#         self.__size = size
#         self.__price = price
#         self.__quantity = quantity

#     def get_name(self):
#         return self.__name

#     def get_size(self):
#         return self.__size

#     def get_price(self):
#         return self.__price

#     def get_quantity(self):
#         return self.__quantity

#     def set_name(self, name):
#         self.__name = name

#     def set_size(self, size):
#         self.__size = size

#     def set_price(self, price):
#         if price > 0:
#             self.__price = price
#         else:
#             print("Цена должна быть положительной.")

#     def set_quantity(self, quantity):
#         if quantity >= 0:
#             self.__quantity = quantity
#         else:
#             print("Количество не может быть отрицательным.")


#     def get_info(self):
#         return f"{self.__name} ({self.__size}), Цена: {self.__price} рублей, Количество: {self.__quantity}"




# class Store:
#     def __init__(self, name):
#         self.__name = name
#         self.__items = []

#     def add_item(self, item):
#         self.__items.append(item)
        
#     def get_name(self):
#         return self.__name
      
#     def remove_item(self, item_name):
#         if item_name in self.__items:
#             self.__items.remove(item_name)

#     def list_items(self):
#         print(f"Товары в магазине {self.get_name()}:")
#         for item in self.__items:
#             print(item.get_info())

#     def get_total_value(self):
#         total_value = 0
#         for item in self.__items:
#             total_value += item.get_price() * item.get_quantity()
#         return total_value

# print("\nСоздается объект магазина 'Магазин одежды'...")
# store = Store("Магазин одежды")

# print("\nСоздается объекты товаров...")
# item1 = ClothingItem("Футболка", "M", 500, 10)
# item2 = ClothingItem("Брюки", "L", 1500, 5)
# item3 = ClothingItem("Обувь", "42", 3000, 2)

# store.add_item(item1)
# store.add_item(item2)
# store.add_item(item3)

# print("Список товаров в магазине:")
# store.list_items()

# print("\nобновление количества товара 'Футболка' на 12")
# item1.set_quantity(12)

# print("\nОбновленный список товаров в магазине:")
# store.list_items()

# print(f"\nОбщая стоимость товаров в магазине: {store.get_total_value()} рублей")

# print("\nУдаление товара 'Брюки' из магазина...")
# store.remove_item(item2)

# print("\nСписок товаров после удаления товара 'Брюки':")
# store.list_items()

# print(f"\nОбщая стоимость товаров в магазине после удаления: {store.get_total_value()} рублей")




# class Product:
#     def __init__(self, name, size, price, quantity):
#         self.__name = name
#         self.__size = size
#         self.__price = price
#         self.__quantity = quantity

#     def get_name(self):
#         return self.__name

#     def get_size(self):
#         return self.__size

#     def get_price(self):
#         return self.__price

#     def get_quantity(self):
#         return self.__quantity

#     def set_name(self, name):
#         self.__name = name

#     def set_size(self, size):
#         self.__size = size

#     def set_price(self, price):
#         if price > 0:
#             self.__price = price
#         else:
#             print("Цена должна быть положительной.")

#     def set_quantity(self, quantity):
#         if quantity >= 0:
#             self.__quantity = quantity
#         else:
#             print("Количество не может быть отрицательным.")

#     def get_info(self):
#         return f"{self.__name} ({self.__size}), Цена: {self.__price} рублей, Количество: {self.__quantity}"


# class ClothingItem(Product):
#     def __init__(self, name, size, price, quantity, material):
#         super().__init__(name, size, price, quantity)
#         self.__material = material 

#     def get_material(self):
#         return self.__material

#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info}, Материал: {self.__material}"


# class Store:
#     def __init__(self, name):
#         self.__name = name
#         self.__items = []

#     def add_item(self, item):
#         self.__items.append(item)
        
#     def get_name(self):
#         return self.__name

#     def remove_item(self, item):
#         if item in self.__items:
#             self.__items.remove(item)

#     def list_items(self):
#         print(f"Товары в магазине {self.get_name()}:")
#         for item in self.__items:
#             print(item.get_info())

#     def get_total_value(self):
#         total_value = 0
#         for item in self.__items:
#             total_value += item.get_price() * item.get_quantity()
#         return total_value



# print("\nСоздается объект магазина 'Магазин одежды'...")
# store = Store("Магазин одежды")

# print("\nСоздаются объекты товаров...")

# item1 = ClothingItem("Футболка", "M", 500, 10, "Хлопок")
# item2 = ClothingItem("Брюки", "L", 1500, 5, "Хлопок")
# item3 = ClothingItem("Шорты", "L", 1500, 5, "Шерсть")

# store.add_item(item1)
# store.add_item(item2)
# store.add_item(item3)

# print("Список товаров в магазине:")
# store.list_items()

# print("\nОбновление количества товара 'Футболка' на 12")
# item1.set_quantity(12)

# print("\nОбновленный список товаров в магазине:")
# store.list_items()

# print(f"\nОбщая стоимость товаров в магазине: {store.get_total_value()} рублей")

# print("\nУдаление товара 'Брюки' из магазина...")
# store.remove_item(item2)

# print("\nСписок товаров после удаления товара 'Брюки':")
# store.list_items()

# print(f"\nОбщая стоимость товаров в магазине после удаления: {store.get_total_value()} рублей")



from abc import ABC, abstractmethod
from random import randint

class Company:
    def __init__(self, name):
        self._name = name
        self._employees = []

    def add_employee(self, employee):
        self._employees.append(employee)
    
    def remove_employee(self, employee):
        self._employees.remove(employee)
    
    def calculate_total_salary(self):
        total_salary = 0
        for employee in self._employees:
            total_salary += employee.get_salary()
        return total_salary
    
    def get_info(self):
        for employee in self._employees:
            print(employee.get_info())


class Employee(ABC):
    def __init__(self, name, position, salary):
        self._name = name
        self._position = position
        self._salary = salary
        self._bonus = False

    def get_name(self):
        return self._name
    
    def get_position(self):
        return self._position
    
    def get_bonus(self):
        return self._bonus

    def get_salary(self):
        return self._salary + self.calculate_bonus()
    
    def set_name(self, name):
        self._name = name
    
    def set_position(self, position):
        self._position = position
    
    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("Salary must be positive.")
    
    def set_bonus(self, bonus):
        if isinstance(bonus, bool):
            self._bonus = bonus
        else:
            print("Bonus must be a boolean value.")
    
    def get_info(self):
        return f"Employee: {self._name}, position: {self._position}, \
            salary: {self._salary}, bonus: {self._bonus}"
    
    @abstractmethod
    def calculate_bonus(self):
        pass
    

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Manager", salary)
        self._department = "Management"
    
    def calculate_bonus(self):
        if self._bonus:
            return 0
        else:
            return self._salary * 0.4
        
class Developer(Employee):
    def __init__ (self, name, salary, programming_language):
        super().__init__(name, "Developer", salary)
        self._programming_language = programming_language
    
    def calculate_bonus(self):
        if self._bonus:
            return 0
        else:
            return self._salary * 0.5
        
class HR(Employee):
    def __init__ (self, name, salary, recruited_employees):
        super().__init__(name, "HR", salary)
        self._recruited_employees = recruited_employees
    
    def get_salary(self):
        return self._salary + self.calculate_bonus()
    
    def calculate_bonus(self):
        if self._bonus:
            return 0
        else:
            return self._salary * (0.01 * self._recruited_employees)


print("\nСоздается объект компании Company1...")
company1 = Company("Company1")

print("Создается объекты сотрудников...")
for i in range(randint(1, 3)):
    manager = Manager("Manager" + str(i), randint(20000, 100000))
    if randint(0,1):
        manager.set_bonus(True)
    company1.add_employee(manager)

for i in range(randint(1, 3)):
    developer = Developer("Developer" + str(i), randint(20000, 100000), "Python")
    if randint(0,1):
        developer.set_bonus(True)
    company1.add_employee(developer)

for i in range(randint(1, 3)):
    hr = HR("HR" + str(i), randint(20000, 100000), randint(1, 10))
    if randint(0,1):
        hr.set_bonus(True)
    company1.add_employee(hr)

print("\nИнформация о сотрудниках компании Company1:")
company1.get_info()

print("\nCоздается объект компании Company2...")
company2 = Company("Company2")

print("Создается объекты сотрудников...")
for i in range(randint(1, 3)):
    manager = Manager("Manager" + str(i), randint(20000, 100000))
    if randint(0,1):
        manager.set_bonus(True)
    company2.add_employee(manager)

for i in range(randint(1, 3)):
    developer = Developer("Developer" + str(i), randint(20000, 100000), \
                          ["Java", "Python", "C++"][randint(0, 2)])
    if randint(0,1):
        developer.set_bonus(True)
    company2.add_employee(developer)

for i in range(randint(1, 3)):
    hr = HR("HR" + str(i), randint(20000, 100000), randint(1, 10))
    if randint(0,1):
        hr.set_bonus(True)
    company2.add_employee(hr)

print("\nИнформация о сотрудниках компании Company2:")
company2.get_info()

print("\n        Батл компаний этого месяца")
total_salary_company1 = company1.calculate_total_salary()
total_salary_company2 = company2.calculate_total_salary()

print("\nЗарплата сотрудников компании Company1:", total_salary_company1)
print("Зарплата сотрудников компании Company2:", total_salary_company2)

if total_salary_company1 > total_salary_company2:
    print("Победила компания Company1")
elif total_salary_company1 < total_salary_company2: 
    print("Победила компания Company2")
else:
    print("Ничья")