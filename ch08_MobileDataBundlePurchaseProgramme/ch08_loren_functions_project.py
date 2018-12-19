# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:16:39 2018

@author: loren
"""
passcodeOnRecord = "1234"
availableCredit = 34.55
    
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
    return passcodeOnRecord
    
def checkCredit(availableCredit):
    dataValueRequested = int(input())
    print(dataValueRequested, "before round test") # test
    dataValueRequested_multipleOf5 = dataValueRequested + (5 - (dataValueRequested % 5))  
    print(dataValueRequested, "after round test") #test
    if dataValueRequested_multipleOf5 <= availableCredit:
        availableCredit = availableCredit - dataValueRequested_multipleOf5
        print("Thank you for your purchase. Your new data has been loaded and your available credit is now £{}.".format(availableCredit))
    else:
        print("You have insufficent available credit to make a purchase of this value. Go away.")
        
    
#def roundToFive(dataValueRequested): 
#    dataValueRequested = dataValueRequested + (5 - (dataValueRequested % 5))  
#    return dataValueRequested 
    