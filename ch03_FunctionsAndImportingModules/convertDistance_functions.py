# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:30:17 2018

@author: Loren
"""

def convertMilesToKilometers():
    kilometersRunByUser = round(float(input("How many miles did you run?")) * 1.6)
    print("Well done! That means you ran " + str(kilometersRunByUser) +" kilometers!")
    
def convertKilometersMiles():
    milesRunByUser = round(float(input("How many kilometers did you run?")) /1.6)
    print("Well done! That means you ran " + str(milesRunByUser) + " miles!")
    
def whichMeasure():
    userInput = input("Well done on going for a run! Did you measure your run in kilometers (km) or miles (m)?")
    if userInput == "km":
        convertKilometersMiles()      
    elif userInput == "m": 
        convertMilesToKilometers()      
    else:
        print("Sorry that is not a valid input.")
#    return userInput
#
#userInput = whichMeasure()


#other practice
'''def addsTwoNumbersTogether():
    firstNumber = 8
    secondNumber = 1
    print(("Maths is fun. {} plus {} = " + str(firstNumber + secondNumber)).format(firstNumber, secondNumber))
    print(int(secondNumber) - 9)
addsTwoNumbersTogether()   
   
def multiply(num1tomultiply,num2tomultiply):
    print(num1tomultiply*num2tomultiply)
    
multiply(2,-2)'''





