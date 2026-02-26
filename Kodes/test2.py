import random
import time
from blessed import Terminal

term = Terminal()

def main():
    # Создается переменная для сохранения значения позиции пользователя по оси х 
    # (term.width // 2 - это получение середины размерности терминала)
    player_x = term.width // 2
    player_y = term.height - 3
    cars = []  
    score = 0
    tick = 0

    for i in range(50):
        side = random.choice(["left", "right"])
        y = random.randint(2, term.height - 4)
        x = random.randint(2, term.width - 4)
        if side == "left":
            cars.append([x, y, +1])   
        else:
            cars.append([x, y, -1]) 


    with term.cbreak(), term.hidden_cursor():
        key = None
        while key not in ("q", "Q", 'й', "Й"):
            print(term.move(player_y, player_x) + " ")

            key = term.inkey(timeout=0.05)

            if key.name == "KEY_LEFT":
                player_x -= 1
            elif key.name == "KEY_RIGHT":
                player_x += 1
            elif key.name == "KEY_UP":
                player_y -= 1
            elif key.name == "KEY_DOWN":
                player_y += 1

            player_x = max(1, min(term.width - 2, player_x))
            player_y = max(1, min(term.height - 2, player_y))

           
            if player_y <= 1:
                print(term.move(term.height // 2, term.width // 2 - 4) + term.green("YOU WIN!"))
                print(term.move(term.height // 2 + 1, term.width // 2 - 6) + f"Your score: {score}")
                print(term.move(term.height // 2 + 3, term.width // 2 - 10) + "Press any key to exit...")
                term.inkey()
                return

       
            tick += 10
            if tick % 10 == 0:
                side = random.choice(["left", "right"])
                y = random.randint(2, term.height - 4)
                if side == "left":
                    cars.append([1, y, +1])   
                else:
                    cars.append([term.width - 2, y, -1]) 

            new_cars = []
            for cx, cy, dx in cars:
                print(term.move(cy, cx) + " ")
                cx += dx
                if 1 < cx < term.width - 1:
                    new_cars.append([cx, cy, dx])
                
            cars = new_cars

            for cx, cy, dx in cars:
                if cx == player_x and cy == player_y:
                    print(term.move(term.height // 2, term.width // 2 - 5) + term.red("GAME OVER"))
                    print(term.move(term.height // 2 + 1, term.width // 2 - 6) + f"Your score: {score}")
                    print(term.move(term.height // 2 + 3, term.width // 2 - 10) + "Press any key to exit...")
                    term.inkey()
                    return


            print(term.move(player_y, player_x) + term.green("@"))
            for cx, cy, dx in cars:
                print(term.move(cy, cx) + term.yellow("#"))

            time.sleep(0.05)

if __name__ == "__main__":
    main()