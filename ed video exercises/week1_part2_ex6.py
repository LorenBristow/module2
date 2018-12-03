# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:10:24 2018

@author: loren
"""
#ex1
print("ex1\n")
myStr = '6.00x'

for char in myStr:
    print(char)

print('done\n')



#ex 2
print("ex2\n")
greeting = 'Hello!' 
count = 0

for letter in greeting: #letter is simply an assigned variable here, not a keyword. change all letter to dog and will still work. 
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter, end = ",")

print('done')

#ex 3
print("ex3\n")
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1    #spaces are counted here.
                        #note i != I in python. so 'I' doesn't satisfy first if check for 'i'.
print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 



