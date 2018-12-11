# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:10:08 2018

@author: loren
"""

userInput = input('Please give a number?')

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result 

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

  

