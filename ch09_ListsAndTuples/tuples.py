# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:51:02 2018

@author: loren
"""

a = [0,1,2,3,4,5,6,7,8,9]
print(a)
del a[-1]
print(a)

b = (0,1,2,3,4,5,6,7,8,9,)
print(b)
#del b[-1] # error- can't remove things from a tuple 
print(b)


a[1] = 50 #adds value to the list at the position indiacted. overwrites.
print(a)

#b[1] = 50 # errror can't change a tuple! immutable
print(b)

a.append('loren')
print(a)

#b.append('loren') # errror can't change a tuple! immutable
print(b)

#can cast list to tuple and tuple to list. useful when needing to change tuple. 
#make it a list, change, then put back to tuple where secure. 
#note - can't use if/else to test tuple
