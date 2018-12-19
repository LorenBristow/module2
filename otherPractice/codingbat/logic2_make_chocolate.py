# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:40:32 2018

@author: loren
"""

def make_chocolate(small, big, goal):
  if ((big * 5) + small) < goal:
    return -1
  elif ((big * 5) + small) == goal:
    return small
  elif ((big * 5) + small) > goal:
    if (big * 5) > goal:
      big = goal // 5
      if small >= goal - (big * 5):
        return (goal - (big * 5))
      else:
        return -1
    elif (big * 5) == goal:
        return 0
    elif (big * 5) < goal:
      return goal - (big * 5)
     
  
    
