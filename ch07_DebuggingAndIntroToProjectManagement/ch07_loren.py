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

 '''DESCRIPTION OF DEBUGGING 
The first button is for you to start running your code until the break point.
The second button allows you to run your code line-by-line until the breakpoint.
The third one is for stepping into the sections (class and functions) that you would
like to dig into more and the fourth button is for you to step out when you feel that the
error is not related to the current section.
The fourth button is for you to go to the next breakpoint (if you have setup multiple
ones) and the last, square shaped button is for you to exit debugging mode and go
back to normal coding mode.'''
