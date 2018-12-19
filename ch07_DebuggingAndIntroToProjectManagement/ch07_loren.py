# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:10:08 2018

@author: loren
"""

userInput = input('Please give a number?')

def simpleOperation(userInput):
    intInput = int(userInput)
    #print(type(intInput)) # used to check if cast was effective
    #result = userInput - 2 # to create an error with str
    result = intInput - 2
    return result 

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result)
print(result2)

  

