import random
import string
class sudoku:
    chars = string.ascii_letters+string.digits+"._"
    board = [[['*' for _ in range(8)] for _ in range(8)] for _ in range(16)]
    def __init__(self):
        self.board = [[['*' for _ in range(8)] for _ in range(8)] for _ in range(16)]
    def fill(self, n):
        while n:
            x, y = random.choices(range(0, 32), k=2)
            box = ((y//8)*4)+x//8
            num = self.chars[random.randint(0, 63)]
            if self.check(x, y, num):
                self.board[box][x%8][y%8] = num
                n -= 1


    def check(self, x, y, n):

        # checking line:
        if n in [self.board[((y//8)*4)+(i//8)][i%8][y%8] for i in range(0, 32)]:
            return False
        # checking column
        if n in [self.board[x//8+(i//8)*4][x%8][i%8] for i in range(0, 32)]:
            return False
        # checking box
        if n in [self.board[((y//8)*4)+x//8][i][j] for i in range(0, 8) for j in range(0, 8)]:
            return False
        # checking if here
        if self.board[((y//8)*4)+x//8][x%8][y%8] != '*':
            return False
        return True

    def get(self, x, y):
       return self.board[((y//8)*4)+x//8][x%8][y%8]
if __name__ == "__main__":
    s = sudoku()
    s.fill(random.randint(200, 300))
    #for i in range(0, 64):
    #    for j in range(0, 64):
    #        symb = ' '
    #        if j%8 == 7:
    #            symb = " | "
    #        print("{}{}".format(s.get(j, i), symb), end='')
    #    if i%8 == 7:
    #        print('\n'+'-'*142)    
    #    else:
    #        print()
    
    for i in range(0, 32):
        for j in range(0, 32):
            print(s.get(j, i), end='')
        print()
        
