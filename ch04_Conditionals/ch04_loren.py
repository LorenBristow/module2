# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:58:56 2018

@author: loren
"""

###TASK 3 

number = input("Enter a number between 1 and 10:")
number = int(number)

if number > 10:
    print("Too high!")
elif number <= 0:
    print("Too low!")
else:
    print("Your number is: " + str(number))    

###TASK 4
    
age_list = [14, 20, 68]
for age in age_list:
    if age < 13:
        print("Child")
    elif age <= 19:
        print("Teen")
    elif age <= 65:
        print("Adult")
    else:
        print("Pensioner")

####