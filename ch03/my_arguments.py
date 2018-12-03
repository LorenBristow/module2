# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:30:17 2018

@author: Loren
"""


measureType = input("km or m?")

def convertMilesToKilometers():
    kilometersRunByUser = round(float(input("How many miles did you run?")) * 1.6)
    print("Well done! That means you ran " + str(kilometersRunByUser) +" kilometers!")

def convertKilometersMiles():
    milesRunByUser = round(float(input("How many kilometers did you run?")) /1.6)
    print("Well done! That means you ran " + str(milesRunByUser) + " miles!")

def whichMeasure():
    if measureType == "km":
        convertKilometersMiles()
    else: convertMilesToKilometers()
    
    

whichMeasure()

#other practice
#def addsTwoNumbersTogether():
#    firstNumber = 8
#    secondNumber = 1
#    print(("Maths is fun. {} plus {} = " + str(firstNumber + secondNumber)).format(firstNumber, secondNumber))
#    print(int(secondNumber) - 9)
#addsTwoNumbersTogether()    
#   
#def multiply(num1tomultiply,num2tomultiply):
#    print(num1tomultiply*num2tomultiply)
#    
#multiply(2,-2)
#
#



