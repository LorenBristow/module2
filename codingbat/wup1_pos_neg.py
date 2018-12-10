# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:31:45 2018

@author: loren
"""

def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0:
      return True
    else:
      return False  ## i had originally forgotten this line. 
  elif (a > 0 and b < 0) or (a < 0 and b > 0):
      return True
  else:
    return False


