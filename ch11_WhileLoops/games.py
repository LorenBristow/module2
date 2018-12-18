# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:59:34 2018

@author: loren
"""

from random import randint

def guess(attempts, range):
    secretNumber = randint(1, range)
    guess = int(input("Welcome! Can you guess my secret number?"))
    attempts = attempts - 1
    while attempts > 0:
        if guess == secretNumber:
            print("That's amazing! Goodbye!")
            print(attempts)
            break
        else:    
            guess = int(input("Guess again!"))  
            print(attempts)
        attempts -= 1
print("END_OF_GAME: thanks for playing!")

guess(3, 20)