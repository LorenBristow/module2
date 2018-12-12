# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:21 2018

@author: loren
"""
from bank_functions import *

Joke = Customer("Joke De Winter", False, 1000) # This is an instance of the class Customer. 


print("What would you like to do today?\n1. Make a withdrawl.\n2. Make a deposit.")
customerActivityChosen = int(input())
if customerActivityChosen == 1:
    withdrawl_amount = input("How much would you like to withdraw?\n")
    Joke.withdraw(withdrawl_amount)

        

  

        


#Loren = Customer("Loren Bristow", True, 500)
#Loren.deposit(500)
#Loren.withdraw(700)

#print(Joke, Loren)





    
    