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
greeting = 'Hello!'   #note - ! qualifies as a letter
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter, end = ",")

print('done')

