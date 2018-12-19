# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:03:59 2018

@author: loren
"""
#my submission - correct. 
def lone_sum(a, b, c):
  if a != b and a != c and b != c: #initially i worte this as a != b != c which was incorrect. only eval the first 2.  
    return a + b + c
  elif a == b == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif c == b:
    return a

#codebat solution - interesting!
    #effectively sets everything to 0 ie. assumes all are equal then tests against this. 
# def lone_sum(a, b, c):
#  sum = 0
#  if a != b and a != c: sum += a
#  if b != a and b != c: sum += b
#  if c != a and c != b: sum += c
#  
#  return sum

