# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:16:39 2018

@author: loren
"""
passcodeOnRecord = "loren"
availableCredit = 32

#function to verify passcode
def checkPasscode(passcodeProvided):
    attemptsCounter = 1   #what about memory of previous visit - should be blocked forever. 
    while attemptsCounter < 3:
        if passcodeProvided == passcodeOnRecord:
            return True    
        else: 
            print("The passcode you have entered is incorrect. You have {} remaining attempts.\nWhat is your passcode?".format(3 - attemptsCounter))
            passcodeProvided = input()
            attemptsCounter += 1  
            
    
def checkCredit(availableCredit):
    dataValueRequested = int(input())
    print(dataValueRequested, "before round test") # test
    dataValueRequested = dataValueRequested + (5 - (dataValueRequested % 5))  
    print(dataValueRequested, "after round test") #test
    if dataValueRequested <= availableCredit:
        availableCredit = availableCredit - dataValueRequested
        print("Thank you for your purchase. Your new data has been loaded and your available credit is now £{}.".format(availableCredit))
    else:
        print("You have insufficent available credit to make a purchase of this value. Go away.")
 
#def roundToFive(dataValueRequested): 
#    dataValueRequested = dataValueRequested + (5 - (dataValueRequested % 5))  
#    return dataValueRequested 
    