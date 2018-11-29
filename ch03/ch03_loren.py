# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#can apply upper to variable through assignment (name = name.upper()) or by directly 
#applying upper to the string in the .format (.format(name.upper())). Note that applying
#the .upper to the outside of the format bracket applies upper to everything, not just the name 
print("What's your name?")
name = input()
#name = name.upper()
print("Hello {}!".format(name))
print("Hello {}!".format(name.upper()))
print("Hello {}!".format(name).upper())

print("Oh hi {}!".format(name.title()))

print("Where are you from?")
country = input()
print("I'm from {}.".format(country))

#remember that all user inputs are recognised as strings by python. 
#So if you ask e.g. for age and user inputs a number this is automatically
#converted to a string and will need to be cast to int or float to be used in calcs. 

def hello_world():
    print()
    print("Hello World!")
hello_world()
    
def name():
    print("What's your name?")
    name = input()
    print("***")
    print("The user's name is {}".format(name))
    print(2+2)
name()

def hello_world():
    print()
    name()
hello_world()

def name():
    print("What's your name?")
    name = input()
    print("***")
    print("The user's name is {}".format(name))
    print("What number would you like to know the power of?")
    choice = input()
    print(choice + ' to the power of ' + choice + ' is ' + str(int(choice)*int(choice)))
name()

