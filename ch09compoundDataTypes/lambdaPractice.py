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

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
print(x2)
print(sorted(x2))
print(sorted(x2, key=lambda s:s[0]))