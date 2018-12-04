# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:28:46 2018

@author: loren


"""
##  Functions name pieces of code the way variables name strings and numbers. 
##  They take arguments (none or one or many).
##   def stands for 'define'.

def print_two(*args):  
    arg1, arg2 = args
    print ("arg1: {}, ".format(arg1), "arg2: {}".format(arg2))

# this versions skips the unpacking args in the first line - unnecessary.
def print_two_again(arg1, arg2):  
    print ("arg1: {}, ".format(arg1), "arg2: {}".format(arg2))
  
def print_one(arg1):
    print("arg1: {}, ".format(arg1))

def print_none():
    print("I got nothin'.")

print_two("'Zed'", "'Shaw'")  
print_two_again("'Zed'", "'Shaw'")  
print_one("'First!'")
print_none()