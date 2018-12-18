# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:52:31 2018

@author: loren
"""
from random import randint

def dice_game():
    user_prediction = input("odd, even or quit?")
    while user_prediction != "quit":
        roll_value = randint(1, 6) + randint(1, 6)
        if roll_value % 2 == 0:
            result = "even"
            print("Dice roll is even!\n")
        else: 
            result = "odd"
            print("Dice roll is odd! Isn't that wierd ;P\n")
        if user_prediction == result:
            print("You win.")
            user_prediction = input("odd, even or quit?")
        else:
            print("Sorry, you lose.")
            user_prediction = input("odd, even or quit?")
print("Thanks for playing. See you later.")
dice_game()       