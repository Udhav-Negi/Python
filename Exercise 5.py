# S = -1 
# W = 0
# G = 1

import random as rd

while True:
    x = input("Enter any number\n-1 for Snake\n0 for Water \n1 for Gun\nPrint q to Quit\n")
    y = rd.randint(-1, 1)
    print(f"You {x}")
    print(f"Computer {y}")
    if x == 'q':
        break
    elif x == -1:
        print("You won") if y == 0 else print("You Lose")
        # pass
    elif x == 0:
        print("You won") if y == 1 else print("You Lose")
        # pass
    elif x == 1:
        print("You won") if y == -1 else print("You Lose")
        # pass
    else:
        print("Please enter valid input")

    