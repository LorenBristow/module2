# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:16:18 2018

@author: loren
"""
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {} cheeses!".format(cheese_count, boxes_of_crackers))
    print("You have {} boxes of crackers!".format(boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 100
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#MY FUNCTION
idealRatio = float(input("What's the ideal cheese-to-cracker ratio?"))
currentRatio = amount_of_cheese / amount_of_crackers
if currentRatio < idealRatio:
    print("The current ratio is only {}. Get more cheese!".format(int(currentRatio)))
else: 
    print("We've checked and the minimum cheese-to-cracker ratio has been met...let's get this party started!")

