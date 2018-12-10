# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:29:54 2018

@author: loren
"""
#My first submission - correct
def parrot_trouble(talking, hour):
  if talking:
    if (hour < 7) or (hour > 20):
      return True
    else:
      return False
  else:
    return False

#My second submission - shorter - correct
def parrot_trouble(talking, hour):
  if talking and ((hour < 7) or (hour > 20)):
      return True
  else:
    return False


#
##Solution and notes from Codingbat
#    Solution:
#def parrot_trouble(talking, hour):
#  return (talking and (hour < 7 or hour > 20))
#  # Need extra parenthesis around the or clause
#  # since and binds more tightly than or.
#  # and is like arithmetic *, or is like arithmetic +