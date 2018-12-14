# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:52:03 2018

@author: loren
"""

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

fruitsalad = ['prear','oirange','ptapaya','pseach','luemon','cdherry', 'maango','blanana', 'afpple','satrawberry']
print()
print()
print(fruitsalad)
print(sorted(fruitsalad, key = lambda s: s[1]))
print(fruitsalad.pop(2))



