# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:22:51 2018

@author: loren
"""
#EXERCISE 1
#Convert the following into code that uses a while loop.
#
#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!
print("EXERCISE 1")
widget = 2
while(widget<=10):
    print(widget)
    widget = widget + 2
print("Goodbye!")

## There are many ways to solve this problem! Here is one:
#num = 2
#while num < 11:
#    print(num)
#    num += 2 #could have used incrementer instead of rewriting variable name
#print("Goodbye!")
#
## Here is another:
#num = 2
#while num <= 10:
#    print(num)
#    num += 2
#print("Goodbye!")
#
## And another:
#num = 0
#while True:
#    num += 2
#    print(num)
#    if num >= 10:
#        print("Goodbye!")
#        break
#
## And one more:
#num = 1
#while num <= 10:
#    if num % 2 == 0:
#        print(num)
#    num += 1
#print("Goodbye!")
#
## There are always many, many different ways to solve a programming
## problem. Here are just four examples and surely there are quite
## a few more.

#EXERCISE 2
print("EXERCISE 2")
widget = 10
print("Hello!")
while widget range(0,10):
    print(widget)
    widget -= 2
    

    