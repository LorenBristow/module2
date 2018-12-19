# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:42:18 2018

@author: loren
"""
#my solution with print lines
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    print("Both smiling - that's TROUBLE!")
    return True
  elif a_smile == False and b_smile == False:
    print("Neither smiling - that's TROUBLE!")  
    return True
  else:
    print("Only 1 smiling - no trouble today.")    
    return False

monkey_trouble(False, False)

#my solution for codingbat submission
def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  elif a_smile == False and b_smile == False:
    return True
  else:
    return False

####solution given by Codingbat
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)