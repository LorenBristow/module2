# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:33:17 2018

@author: loren
"""
##NOTES, COMMENTS, PROBLEMS, TO-DOS:
##some people sat at ends i.e did not actually sit next to neighbour in the list
##people may want to change direction? C
##HeinLoren not seen as same as LorenHein so need to create an expanded list 
##---------------------------------------------

import random
####
print()
###CURRENT SEATING
print("The current seating:\n".upper())
current_seating = ["Hien", "Loren", "Iza","Seraphine", "Ottilie", "Muna", "Sarika", "Rachel",\
           "Katharina", "Ellen", "Kirsty", "Kate", "Leanne", "Milly", "Maggie", "Amina",\
           "Gracy", "Mabel", "Jennifer", "Mandy", "Harriet", "Tilly","Roxy", "Aminat","Mari",\
           "Pam", "Fabiana", "Amanda", "Martina"]
print(current_seating)
print()

###CURRENT SEATING PAIRS(NEIGHBOURS)
print("Pairs of current neighbours:\n".upper()) #based on original seating
for n in range(28):
    current_neighbour_pairs = str(current_seating[n]) + str(current_seating[n+1])
    print(current_neighbour_pairs, end=", ")
random.shuffle(current_seating)
print() 
print()

###RANDOM SEATING
print("The randomly shuffled seating:\n".upper())
print(current_seating)
print()

###RANDOM SEATING PAIRS(NEW NEIGHBOURS)
print("Neighbours in shuffled seating:\n".upper()) #based on shuffled seating
for n in range(28):
    new_neighbour_pairs = str(current_seating[n]) + str(current_seating[n+1])
    print(new_neighbour_pairs, end=", ")
print()  
print()

##need to create the comparison fo tuples here. 

###RANDOM SEATING PAIRS(NEW NEIGHBOURS)---only apply to final random list w/out repeat pairs. 
#print("The randomly shuffled seating separated into desk banks of 3 and 4:\n".upper())
#
#for n in range(0,20,4): #5 rows of 4 people
#    print("Bank of 4 desks: ", seating[n:n+4])
#for n in range(20,29,3): #3 rows of 3 people
#    print("Bank of 3 desks: ",seating[n:n+3])   
#print()
#
