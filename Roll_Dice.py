"""PRESS YES TO ROLL AGAIN AND NO TO EXIT AND RUN HOME"""
import random

min_value = 1
max_value = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Dice Rolling.......")
    print("Dice Rolled\nThe Values Are:")

    print(random.randint(min_value,max_value))
    print(random.randint(min_value,max_value))

    roll_again = input("Do you want to ROLL AGAIN????????")
    