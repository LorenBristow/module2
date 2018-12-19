# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:15:53 2018

@author: loren
"""


import random

#need to rewrite cleaner using sub-routines. 
class Customer():
#"""Return a Customer object whose name is *name* and starting balance is *balance*."""
    def __init__(self, name,  has_overdraft=False, balance=0.00):
        self.name = name
        self.balance = balance
        self.has_overdraft = has_overdraft   
                
#"""Return the balance remaining after withdrawing *amount* dollars."""        
    def withdraw(self, withdrawl_amount):
        withdrawl_amount = int(withdrawl_amount)
        if withdrawl_amount > self.balance:
            print("Withdrawl amount is greater than available balance.\n")
            if self.has_overdraft == False:
                print("You don't have an overdraft available so you cannot draw this amount. Please withdraw an amount which is equal to or smaller than your available balance of £", self.balance," or apply for an overdraft")
            #later - add option to change amount requested for withdrawl here or apply for overdraft.
                does_customer_want_overdraft = input("Would you like to apply for an overdraft? \n  Please respond 'y' for yes or 'n' for no.\n")            
               #need to remember that naming variable of input to something other than input was important to this actually working. 
                if does_customer_want_overdraft == 'y':
                    print("Thank you for your application for an overdraft. We are considering your application.\n")
                    print("Wait for it....")
                    print("Wait for it....")
                    print("Wait for it....")
                    print("Wait for it....")
                    print("Wait for it....")
                    choice_overdraft_list = [True, False]
                    choice_overdraft = random.choice(choice_overdraft_list)
                    print(choice_overdraft)
                    if choice_overdraft == True:
                        print("Congratulations, your application is successful and you are now free to weigh yourself down in debt to your heart's delight <3!\n")
                    elif choice_overdraft == False:
                        print("Unfortunately your application is denied based on a random 50/50 decision. Goodbye.")
                else:
                    "Thank you for your response. Please contact us should you change your mind.\n"
                #raise RuntimeError("Amount greater than available balance.")            
        else: 
            self.balance -= withdrawl_amount
            print("Thank you for your withdrawl. Your balance has been updated.\n")
        return self.balance

#"""Return the balance remaining after depositing *amount* dollars."""
    def deposit(self, deposit_amount):
        deposit_amount = int(deposit_amount)
        choice_is_deposit_suspicious = [True, False]
        choice_is_deposit_suspicious = random.choice(choice_is_deposit_suspicious)
        if choice_is_deposit_suspicious == False:
            self.balance += deposit_amount
            print("Thank you for your deposit. Your balance has been updated.\n")
            return self.balance
        elif choice_is_deposit_suspicious == True:
            print("We have randomly determined that your deposit is SUSPICIOUS. \nPlease got to jail while we drag this matter through court over 5 or so years.\nYou will have the support of a sub-standard lawyer until your funds run dry.")
        
    def __str__(self): #need to add overdraft choice
        return ("CUSTOMER ACCOUNT STATUS:\n  Customer " + self.name + " has a balance of £" + str(self.balance) + ".\n  Overdraft Indicator: " + str(self.has_overdraft) + ".\n\n" )
#Note - Nothing marks the end of the class block. It's all about indentation.  
        
class Employee(): 
    def __init__(self, name, rights):
        self.name = name
        self.rights =  True
        