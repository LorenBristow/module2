# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:41:36 2018

@author: loren
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:27:58 2018

@author: loren
"""

my_favourite_fruits = ["apples", "orange", "banana"]
#print(my_favourite_fruits[0])  ##list runs from position 0(index position) to position (n-1). Thus -1 returns last item on the list. 

x = ["this", 55, "that", my_favourite_fruits]
print(x[3])

print(x[-1][-3]) #each item is an ordered array so can drill into them. 
print(x[-2][-3]) #drilling into the letters in 'that' at position -2, -3. 
print(x[2][1])


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
print(x[-1:0]) #there's nowhere to go from -1. it is the final position
print(x[-3:-1]) #note - doesn't mean read backwards. just indicating where to start and then continues froward from there. 
print(x[0:0])

#sorting a list
#2 ways - sorted() which makes copy and retunrs copy sprted. 
#.sort() is list-class specific method and changes the original list in it's place. Alters list. 

mabels_doof = ['pear', 'apple', 'banana', 'naartjie']
print(mabels_doof)
mabels_food = sorted(mabels_doof)
#sorted(mabels_doof)
print(mabels_doof) # unchanged by the sort action.
print(mabels_food) #makes alphabetical
mabels_food = sorted(mabels_doof, reverse=True)
print(mabels_doof)
print(mabels_food)


mabels_snep = ['orange pen','pink pen', 'multi-coloured pen','pink pen', 'prockey pen', 'pink pen', 'some other pen']
print(mabels_snep)

#mabels_pens = mabels_snep
mabels_snep.sort() #changes the existing list, no copy created
print(mabels_snep)
#print(mabels_pens)


#DELETING & REMOVING IN LISTS - - - .remove() , del , .pop()
mabels_snep.remove('orange pen') # removes first matching named item from the list, can't take an index
print(mabels_snep)

del mabels_snep[-2]
print(mabels_snep)

print(type(mabels_snep))
mabels_snep.pop(1) 
print(mabels_snep)

test = [1,2,3,4,5]
test.pop(1)
print(test)

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["xa", "sb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)

#lambda is a placeholder for any operation. 
# λx.x2 + 1 denotes the function x2 + 1.

x2 = [('a', 3, z), ('c', 1, y), ('A', 5, x)]
print(x2)
print(sorted(x2))
print(sorted(x2, key = lambda s: s[2][2])) #s:s parts of the compound data type
print(sorted(x2, key = lambda s: s[2][1][1])) #final number is going into the string and looking at the 2nd position ie the 2nd letter