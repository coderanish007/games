# import random

# ladder = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
# snake = {32:10, 34:6, 48:26, 62:18, 88:24, 95:56, 97:78}

# pos1 = 0
# pos2 = 0 

# A_=input("Enter Player 1 name: ")
# B_=input("Enter Player2 name: ")

# def move(pos):
#     dice = random.randint(1,6)
#     print(f"Dice: {dice}")
#     pos = pos + dice
#     if pos in snake:
#         print('Bitten by snake!!!')
#         pos = snake[pos]
#         print("Position:",pos)

#     elif pos in ladder:
#         print('Climed by ladder')
#         pos = ladder[pos]
#         print(f"Position: {pos}")

#     else:
#         print(f"Position:{pos}")
#     print("\n")
#     return pos

# while True:
#     A=input(f"{A_}\nPress any key to roll the Dice-> ")
#     pos1 = move(pos1)
#     if pos1 >= 100:
#         print(f"GAME OVER!!\n{A_} WON!!!")
#         break
#     B = input(f"{B_}\nPress any key to roll the Dice-> ")
#     pos2 = move(pos2)
#     if pos2 >= 100:
#         print(f"GAME OVER!!\n{B_} WON!!!")
#         break


import random

ladder = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
snake = {32:10, 34:6, 48:26, 62:18, 88:24, 95:56, 97:78}

pos1 = 0 #player 1
pos2 = 0 #player2

def move(pos):
    dice = random.randint(1,6)
    print('you have rolled',dice)
    
    old_pos = pos
    pos += dice

    if pos> 100:
        pos =old_pos
    if pos in ladder:
        print("we found a ladder, let's move up")
        pos = ladder[pos]

    elif pos in snake:
        print("we got bitten by snake,go down")
        pos = snake[pos]
    print('New Position:', pos)
    return pos

def start():
    global pos1,pos2
    while True:
        A=input("Player 1\nPress any key to roll the Dice-> ")
        pos1 = move(pos1)
        if pos1 >= 100:
            print(f"GAME OVER!!\n{A} WON!!!")
            break
        B = input("Player 2\nPress any key to roll the Dice-> ")
        pos2 = move(pos2)
        if pos2 >= 100:
            print(f"GAME OVER!!\n{B} WON!!!")
            break
__init__=".__snake_n_ladder__"
start()