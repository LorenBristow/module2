# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:27:58 2018

@author: loren
"""

my_favourite_fruits = ["apples", "orange", "banana"]
#print(my_favourite_fruits[0])  ##list runs from position 0(index position) to position (n-1). Thus -1 returns last item on the list. 

x = ["this", 55, "that", my_favourite_fruits]
#print(x[3])
#
#print(x[-1][-3]) #each item is an ordered array so can drill into them. 
#print(x[-2][-3]) #drilling into the letters in 'that' at position -2, -3. 
#print(x[2][1])


print(x)
y = x
print(y)
#y = x.remove(my_favourite_fruits) 
x.remove(my_favourite_fruits) # from x remove the item in the brackets
print(x)
print(y) #gives outcome of 'none' because y is now a function(x.remove()) not a variable?

y.append("hello")
print(x)
print(y)
y = x.append("hello") 
print(y)

#explore this more - x and y are now sharing same memory space so tend 
#to change together and seem to be able to use the variable names 
#interchangebly to effect change to both. 

q = ["Loren", "Chen", "Mabel", "Katie", "Amanda", "Loren"]
print(q)
q.remove("Loren") #only removes the first occurrence of duplicate "Loren"
print(q)
q.append("Chen")
print(q)

#need to explore how to remove all occurence of something (ie above if i wanted to remove all Loren not just duplicate one)
#need to explore how to specify which occurence to remove - eg if i wanted to take out only 2nd loren
