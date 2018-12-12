# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:21 2018

@author: loren
"""

from bank_functions import *
loren=Customer('Loren', True, 500)
# sucker# = Customer("name", bool_hasoverdraft, bal)
print("WELCOME TO THE BAD BAD BANK\nWHERE GETTING WHAT YOU ASK FOR IS GETTING WHAT YOU PAY FOR...\nand you pay close to nothing.\n" )
print("Who goes there?!\n")
name = input()
name = name.title()
sucker1 = Customer(name)
print(sucker1)

#existing or not
 # This is an instance of the class Customer. 

print("What would you like to do today?\n1. Make a withdrawl.\n2. Make a deposit.")
customerActivityChosen = int(input())
if customerActivityChosen == 1:
    withdrawl_amount = input("How much would you like to withdraw?\n")
    loren.withdraw(withdrawl_amount)
elif customerActivityChosen == 2:
    deposit_amount = input("OK Money-bags, how much would you like to deposit?\n")
    loren.deposit(deposit_amount)
        

  

        


#Loren = Customer("Loren Bristow", True, 500)
#Loren.deposit(500)
#Loren.withdraw(700)

#print(Joke, Loren)





    
    