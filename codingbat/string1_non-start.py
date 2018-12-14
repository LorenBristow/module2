# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:16:26 2018

@author: loren
"""

def non_start(a, b):
   print(a[1:(len(a))] + b[1:(len(b))] )
   return a[1:(len(a))] + b[1:(len(b))]
non_start("loren", "laughs")

#note - had initially used a-1 for end of range and that gave error - a is a string! 
#thus used length which gives exclusive end point