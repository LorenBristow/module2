# -*- coding: utf-8 -*-

def hello_world():
    print()
    print("Hello World!")
    return 2+2
hello_world()

def name():
    print("What's your name?")
    name = input()
    print("Hello {}!".format(name))
    print("Hello {}!".format(name.upper()))
    print("Hello {}!".format(name).upper()) # everything is upper case
    print("***")
    print("The user's name is {}".format(name))
    print("Oh hi {}!".format(name.title()))
    print("Where are you from?")
    country = input()
    print("You're from {}.".format(country))
    print("What number would you like to know the power of?")
    choice = input()
    print(choice + ' to the power of ' + choice + ' is ' + str(int(choice)*int(choice)))
    return name
name()

#can apply upper to variable through assignment (name = name.upper()) or by directly 
#applying upper to the string in the .format (.format(name.upper())). Note that applying
#the .upper to the outside of the format bracket applies upper to everything, not just the name 
    
#remember that all user inputs are recognised as strings by python. 
#So if you ask e.g. for age and user inputs a number this is automatically
#converted to a string and will need to be cast to int or float to be used in calcs. 
