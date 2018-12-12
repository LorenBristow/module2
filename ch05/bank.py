# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:21 2018

@author: loren
"""

from bank_functions import *
print("WELCOME TO THE BAD BAD BANK\nWHERE GETTING WHAT YOU ASK FOR IS GETTING WHAT YOU PAY FOR...\nand you pay close to nothing.\n" )
# sucker# = Customer("name", bool_hasoverdraft, bal)
sucker = Customer(input("Who goes there?!\n").title(), False, 0) # only works for new customers. need logic for existing to not lose history.
print(sucker)
print("What would you like to do today?\n1. Make a withdrawl.\n2. Make a deposit.")
customerActivityChosen = int(input())
if customerActivityChosen == 1:
    withdrawl_amount = input("How much would you like to withdraw?\n")
    sucker.withdraw(withdrawl_amount)
elif customerActivityChosen == 2:
    deposit_amount = input("OK Money-bags, how much would you like to deposit?\n")
    sucker.deposit(deposit_amount)
        




    
    