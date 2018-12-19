# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:10:05 2018

@author: loren
"""
#dummy passcode to check - passcode is loren

from ch08_loren_functions_project import *
  
#user to enter passcode for verification
print("What is your passcode?\n")
passcodeProvided = input() #maybe make invisible/masked?
#maybe step to change pcode if want/reset. or register if not exitisng user. 
#verification of passcode
if checkPasscode(passcodeProvided) == True:
    print("Thank you. The passcode provided is correct. Indicate what you would like to do by entering the number?\n 1. Check your available credit.\n 2. Purchase a data bundle.") # # #her's where all the action happens. 
    whichOption = int(input())  #need to restrict to single number only - 1 or 2. 
    if whichOption == 1: #check balance
        print("You have £{} credit available.".format(availableCredit)) #another what would you like to do step?
    elif whichOption == 2: # buy data
        print("How much data would you like to purchase in £?\nNote that purchases can only be made in multiples of 5 and your entry will be rounded up to meet this criteria.")
        checkCredit(availableCredit)
    else:
        print("Invalid selection.\nExterminate!Exterminate!EXTERMINATE!")#not a valid option - error, give menu again incl exit option. 
else:
    print("Unfortunately you have entered an incorrect passcode and you are now locked out for eternity and will never be able to buy data again. Please go away.")
    

#create objects and classes - use OOP for customers to know their initial value and maybe typical bundle size
### use flask to pass this to a web front end :)
#database type interaction?
#lights and sounds when wrong - criminal 