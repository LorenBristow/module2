# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:48:24 2018

@author: loren
"""

#TASK 2.2 - slides - practice passing arguments to functions. 

a1 = "hello"
a2 = "<3 love"
b1 = "world"
b2 = "coding"


def hello_world_2args(a,b): # a and b are the parameters of the function
    print("{} {}".format(a,b))
    
hello_world_2args(a1, b1) # passing arguments into the function
hello_world_2args(a2,b2)