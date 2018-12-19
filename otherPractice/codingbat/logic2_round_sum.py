# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:03:57 2018

@author: loren
"""

def round_sum(a, b, c):
    a = round10(a) 
    b = round10(b)
    c = round10(c)
    print (a + b + c)
    
    
def round10(n):
    if n % 10 >=5:
       n = int(n + (10 - (n % 10)))
    else:
       n = int(n - (n % 10))
    print(n)
   
round_sum(12, 13, 18)


