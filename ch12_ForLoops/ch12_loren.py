# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:38:10 2018

@author: loren
"""

###TASK 1 - LOOP THROUGH A LIST
print("TASK 1")
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print(item)

###TASK 2 - UPDATE LIST VALUES 
print("TASK 1")
x = ["aa", "bb", "cc"]
print(x)
x[1] = 33 # overwrite
print(x)
x.append("dd") # appending to list
print(x)

###TASK 3 - CREATE AND PRINT LIST
#Converting to string for printing, adding operations (& example of ambiguity and sequencing!), looping through list
values = [875, 23, 451]
for val in values:
    print("--->" + str(val))
    print("--->" + str(val + 50)) 
#note that sequencing will print one of each of these print lines at a time. 
#not blocks of 3 - would need separate for loop for that. 
    
values = ["this", 55, "that"]
for item in values:
    print("***", item)
    
###TASK 4 - LOOP THROUGH A STRING
for char in "yes":
    print(char)
    
for char in "yes":
    print(char, end="")
    print() # need empty line so next result doesn't start at end of this result line

for char in "yes yes yes":
    print(char.split("y")) # investigate nuances of .split(). eg appears to be making each thing inidiv. list. 

###TASK 5 - LOOPING THROUGH A TUPLE
my_shopping_cart_tuple = tuple(my_shopping_cart)
print(my_shopping_cart_tuple)
for item in my_shopping_cart_tuple:
    print(item)
    
##TASK 6 - LOOPING THROUGH A DICTIONARY
salary = {"al" : 20000, "bo": 50000, "ced": 1500}
print(salary)
for indiv_sal in sorted(salary.items(), reverse=True):
    print(indiv_sal) 

##TASK 7 - MORE WITH DICTIONARIES
densities = {"iron":( 7.8, 10, 50), "gold":(19.3, 1000, 10), "zinc":(7.13, 500, 30), "lead": (11.4, 5, 20)}
print(densities)
metals = list(densities)
print(metals) # only keys printed
metals.sort(reverse=True, key=lambda m:densities[m]) # sorting on values of dictionary 'densities', NOT sorted on keys!
print(metals)
metals = sorted(densities.keys(), reverse=True) #keys are now a list sorted in reverse 
print(metals) 
metals = sorted(densities.values(), reverse=True) #values are now a list sorted in reverse 
print(metals) 
metals = sorted(densities.items(), reverse=True) #key value pair (tuples) are now a list sorted in reverse 
print(metals) 
#metals.sort(reverse=True, key=lambda m:densities[m]) #note originlly had this after the sorted() commands and created an error. 
#sorted changes nature of that on whihc it operates and can create complicatoins if not anticipated. 

#for metal in metals:#go back to page 121 above 'search and operations..' to work through formatting. slides 24 and 25
#    print(metal, densities, end="")

###TASK 8 - COMBINE COUNTING LOOP AND CONDITIONALS TO FILTER OUT VALUES
for metal in densities:
    if densities[metal][0]>10:
        print("{} has a density greater than 8.".format(metal))
            #EXTRA CHALLENGE - FIGURE OUT HOW TO PRINT ONE LINE LISTING THEM ALL IN SENTENCE THAT ADAPTS TO NUMBER OF INPUTS. EG IF ONLY 1 ITEM THE LANGUAGE IS DIFFERENT TO PLURAL. 

###TASK 9 - DESIGN AND SUM FUNCTION
values = [3, 12, 9]
total = 0
for val in values:
    print("Before adding", val, "total is", total)
    total += val
    print("After adding", val, "total is", total)
    print("  SUBTOTAL:" + str(total))
print("TOTAL:" + str(total))    

def sumValues(l):
    sumV = 0
    for val in l:
        sumV += val
    return sumV
print(sumValues(values))
    
sumValues(values)

###TASK 10 - USING A LOOP WITH INDEX VALUES
print(list(range(3)))
sweetList = ["candy", "cakes", "sugar"]
print(len(sweetList))
print(range(len(values)))

for i in range(len(values)): # referring to 'values' in TASK 9
    values[i] = values[i] * 2
    print(values) #seeing effect of each iteration of loop 
print(values)   #seeing final outcome

###TASK 11 - USING A LOOP WITH RANGE FUNCTION
for i in range(3, 10, 2):
    print(i)
    
###TASK 12 - BREAK IN FOR LOOP
nums = [2,3,65,23,123,432,3]    
for n in nums:
    if n > 100:
        print("found:", n)
        break

nums = [1, 5, 30, 200, 101, 100, 22]
for index in range(len(nums)):
    print("loop index", index, "with value", nums [index])
    if nums[index] > 100:
        print("break", nums[index], "with index", index)
        break

###TASK 13 - USING NESTED LOOPS
outer_vals = [1, 2, 3]
inner_vals = ["A", "B", "C"]
d = {}
for o_val in outer_vals:
    for i_val in inner_vals:
        d[o_val] = i_val
        print(o_val, i_val)
print(d)
print()

##TASK 14 - MULTIPLICATION
for i in range(1,7):
    for j in range(1,11):
        print("{0:>3}".format(i*j), end="")
    print("\n")
print()
#extend example to 10 * 10 table
for i in range(1,11):
    for j in range(1,11):
        print("{0:>10}".format(i*j), end="")
    print("\n")     
print()

###EXTRA EXAMPLE IN CLASS - CHRISTMAS WISHLIST
#def buildMyChristmasList():
#    christmasWishList = {1:("candy"), 2:("puppies"), 3:("piles of gold coin"), 4:("immovable property")}
#    print("Original List:" + str(christmasWishList))
#    enough = "not enough"
#    while enough != "enough":
#        christmasWishList.update({"5": input("What else would you like, Greedy?")})
#        enough = input("Enough yet? Type 'enough'.")      
#    print("Extra greedy List:" + str(christmasWishList))
#
#
#buildMyChristmasList()       

