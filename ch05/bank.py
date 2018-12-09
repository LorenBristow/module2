# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:21 2018

@author: loren
"""


class Customer():

#"""A customer of ABC Bank with a checking account. Customers have the following properties:
#Attributes:
#name: A string representing the customer's name.
#balance: A float tracking the current balance of the customer's account."""

#"""Return a Customer object whose name is *name* and starting balance is *balance*."""
    def __init__(self, name,  has_overdraft=False, balance=0.00):
        self.name = name
        self.balance = balance
        self.has_overdraft = has_overdraft
        
#"""Return the balance remaining after withdrawing *amount* dollars."""        
    def withdraw(self, withdrawl_amount):
        if withdrawl_amount > self.balance:
            print("Withdrawl amount is greater han available balance.\n")
            if self.has_overdraft == False:
                print("You don't have an overdraft available so you cannot draw this amount. Please withdraw an amount which is equal to or smaller than your available balance of £\n", self.balance,"\n")
                does_customer_want_overdraft = input("Would you like to apply for an overdraft? \n  Please respond 'y' for yes or 'n' for no.\n")            
               #need to remember that naming variable of input to something other than input was important to this actually working. 
                if does_customer_want_overdraft == 'y':
                    print("Thank you for your application for an overdraft. We will be in touch soon.\n")
                else:
                    "Thank you for your response. Please contact us should you change your mind.\n"
                #raise RuntimeError("Amount greater than available balance.")            
        else: 
            self.balance -= withdrawl_amount
            print("Thank you for your withdrawl. Your balance has been updated.\n")
        return self.balance

#"""Return the balance remaining after depositing *amount* dollars."""
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Thank you for your deposit. Your balance has been updated.\n")
        return self.balance
        
    def __str__(self): #need to add overdraft choice
        return ("CUSTOMER ACCOUNT STATUS:\n  Customer " + self.name + " has a balance of £" + str(self.balance) + ".\n  Overdraft Indicator: " + str(self.has_overdraft) + ".\n" )
    
#Note - Nothing marks the end of the class block. It's all about indentation.
        
Joke = Customer("Joke De Winter", False, 1000) # This is an instance of the class Customer. 
#Joke.deposit(500)
#Joke.withdraw(10000)
#Loren.deposit(500)
#Loren.withdraw(700)
print(Joke)

#make another role - eg bank worker also with attributes



    
    