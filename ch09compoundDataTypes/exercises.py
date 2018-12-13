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
y = x.append("hallo") 
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
#delete and overwrite?

print()

#can use math operators to connect different lists into one list
ani = ["the", "cat", "sat"]
print(ani)
mals = ["on", "the", "mat"]
print(mals)

animals = ani + mals
print(animals)

anianimals = ani + animals 
print(anianimals)

animalsani = animals + ani
print(animalsani)

#SET # https://www.programiz.com/python-programming/set
my_set = {1, 2, 3, 3} # sets have no duplicates 
print(my_set) # the duplicate does not show in the print. set removes dupes.

my_set = {1.0, "Hello", (1, 2, 3)} # set with mixed data types
print(my_set)

#we can make a set from a list
another_set = set(['mugs', 'cups', 'spoons', 'plates', 'plates'])
print(another_set)

#Creating an empty set is a bit tricky.
#Empty curly braces {} will make an empty dictionary in Python. 
#To make a set without any elements we use the set() function without any argument.

# initialize a with {}
a = {}

# check data type of a
# Output: <class 'dict'>
print(type(a))

# initialize a with set()
a = set()

# check data type of a
# Output: <class 'set'>
print(type(a))


#SLICING A LIST - note - more permissive than index. index beyond range gives error. 
#slicing will just give what's available in the range.
print(x)
print(x[1:4])
print(x[3:6])
print(x[-3]) # slicing using neg appears to only be able to take 1 position, not a range.
print(x[-3:-1]) #note - doesn't mean read backwards. just indicating where to start and then continues froward from there. 
print(x[0:0])