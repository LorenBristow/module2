# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:59:34 2018

@author: loren
"""

from random import randint

def guess(attempts, range):
    start_attempts = attempts
    secretNumber = randint(1, range)
    guess = int(input("Welcome! Can you guess my secret number?"))
    attempts = attempts - 1
    while attempts > 0:
        if guess == secretNumber:
            print("That's amazing! You got it right on attempt number {}. Goodbye!".format(start_attempts-attempts))
            print(attempts)
            break
        else: 
            if guess > secretNumber:
                print("Too high.")
            else:
                print("Too low.")
            guess = int(input("Guess again! Attempts left: {}".format(attempts)))  
            print(attempts)
        attempts -= 1
    print("END_OF_GAME: thanks for playing!")    
print("END_OF_GAME: thanks for playing!")

guess(3, 3)