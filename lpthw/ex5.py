# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:17:45 2018

@author: Loren
"""

my_name = "Zed A. Shaw"
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print("Let's talk about {}".format(my_name))
print("He's {} inches tall".format(my_height))
print("He's {} pounds heavy".format(my_weight))
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.".format(my_eyes, my_hair))
print("If I add {}, {}, {} I get ".format(my_age, my_weight, my_height)  + str(my_age + my_weight + my_height))