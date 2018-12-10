# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:38:02 2018

@author: loren
"""

#all about precedence

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    print("no")  
    return 0
  elif you >= 8 or date >= 8:
      print("yes")  
      return 2
  else:
      print("maybe")  
      return 1


date_fashion(6,4)
