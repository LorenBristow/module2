# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:00:46 2018

@author: loren
"""

#my solution  - correct

def sorta_sum(a, b):
  if (a + b >= 10) and (a + b <= 19):
    return 20
  else:
    return a + b
  
#coding bat solution
#declares the sum then uses that as opposed to calculating each time. 
#Does this have a positive impact on performance?
    
#def sorta_sum(a, b):
#  sum = a + b
#  if sum >= 10 and sum <= 19:
#    return 20
#  return sum
