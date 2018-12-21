# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:40:09 2018

@author: loren
"""

values = [4,3,6,5,2,1]
n = len(values)
print(len(values))
print(range(n-1)) #6 positions. although don't think an issue if longer range as will stop once all in right place. just waste of energy. 
counter = 0
for i in range(0, n-1):
    counter += 1
    if values[i] > values[i + 1]:
        print(value[i])
        print(i + 1)
        values[i], values[i + 1] = values [i + 1], values[i]  #switching the values. 
        print(i)
        print(i + 1)
print(counter)
print(values)
             