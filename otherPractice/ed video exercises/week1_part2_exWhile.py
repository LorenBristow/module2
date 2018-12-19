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
print("Goodbye!\n")

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
while widget <= 10 and widget > 0:  #unnecessary to have the range - given i  
                                    #had set widget=10 it will alwys be <=10 i.e. redundant.
    print(widget)
    widget -= 2
    
## There are always many ways to solve a programming problem. Here is one:
#print("Hello!")
#num = 10
#while num > 0:
#    print(num)
#    num -= 2
#
## Here is another:
#num = 11
#print("Hello!")
#while num > 1:
#    num -= 1
#    if num %2 == 0:
#        print(num)
#    
    
    
#EXERCISE 3   #to ponder later - is there potential for an infinite loop here?
print("EXERCISE 3")
widget = 0
end = 6
while end > 0:
    widget = widget + end
    end -= 1
print(widget)

#This was my first solution which worked but i used a break to prevent inf loop which 
#was unnec. if i wrote the while expression better. 
#widget = 0
#end = 6
#while end != 0:
#    if end <0:
#        break
#    widget = widget + end
#    end -= 1
#print(widget)


## Here is one of a few ways to solve this problem:
#total = 0
#current = 1
#while current <= end:
#    total += current
#    current += 1
#
#print(total)
    
    