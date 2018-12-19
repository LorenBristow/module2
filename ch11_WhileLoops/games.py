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