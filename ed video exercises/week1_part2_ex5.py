# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:35:22 2018

@author: loren
"""
#PRE-EXAMPLE
#
print("pre-example\n")
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

#output: 5, 4
## NB I OFTEN MAKE THE SAME MISTAKE - if does NOT loop. 
#Therefore one run to end, not go back with num decremented by 1. 
#Careless.

#example 1 - NB lesson = the loop ignores/overwrites earlier binding of var num
#
print("example 1\n")
num = 10
for num in range(5):
    print(num)
print(num)

#example 2 - NB lesson = the division (/) results in a float result automatically in P3. 
print("example 2\n")
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) # result will be a float even though both inputs are int type.
                        # in P3 every division yields a float whether inputs were float or int. 
                        #in P2 3/2 = 1 (assumes int in want int out.) 
                        #to get float you would have had to do 3.0/2 = 1.5. 