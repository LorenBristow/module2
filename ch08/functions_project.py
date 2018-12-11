# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:16:39 2018

@author: loren
"""
passcodeOnRecord = "loren"
availableCredit = 32

#function to verify passcode
def checkPasscode(passcodeProvided):
    if passcodeProvided == passcodeOnRecord:
        return True    
    else: #final exit until we give reattempts or reset or retrieval. 
        return False
    
def checkCredit(availableCredit):
    dataValueRequested = int(input())
    roundToFive(dataValueRequested)  
    if dataValueRequested <= availableCredit:
        availableCredit = availableCredit - dataValueRequested
        print("Thank you for your purchase. Your new data has been loaded and your available credit is now £{}".format(availableCredit))
    else:
        print("You have insufficent available credit to make a purchase of this value. Go away.")
 
def roundToFive(dataValueRequested): 
    if dataValueRequested % 5 != 0:
        dataValueRequested = dataValueRequested + (5 - (dataValueRequested % 5))  
        return dataValueRequested
    else:
        return DataValueRequested
    
    