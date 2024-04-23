# a = 10
# b = 5
# print(a= b)




# x = 5
# print('x =', x + 3)




# d = {1:'one', 3:'three', 2:'two', '4':'four'}

# d.pop('4')
# d.setdefault(5, 'five')
# # d.sorted()

# print(d)



# def run_rec(is_raining, temperature):
#     ________
#         return "На улице дождь"
#     elif temperature< 5:   
#         return "Слишком холодно"
#     ________
#         return "На пробежку!"
#     else:
#         return "Слишком жарко"

# raining = False
# temperature= 6
# print(run_rec(raining, temperature))




# movies = []

# ______
#     movie = input("Введите фильм: )
#     ______
#         break
#     else:
#         movies.append(movie)
# print(movies)




# def score(cf, *scores):
#     for i in scores:
#         print(cf*i)

# cf = 0.2
# scores = [4, 5, 4]
# score(cf, scores)



# def dop():
#     a= 9

# print(dop())



# import re

# str = '3 товара за 200.99'
# pat = r'\d+.\d'
# match = re.search(pat, str)

# print(match.group())




from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def move(self):
        pass

class Queen(Piece):
    def move(self):
        print('Ход фурзя')

a = Piece()
b = Queen()

a.move(), b.move()