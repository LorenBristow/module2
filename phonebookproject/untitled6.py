# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 18:39:13 2019

@author: loren
"""

def sum13(nums):
  result = 0    
  for i in range(len(nums)):
    if 13 in nums:
        nums[i] = 0
        nums[i + 1] = 0  
  for i in range(len(nums)):
     result = result + nums[i]
  print(result)
  return result

#sum13([1, 2, 2, 1])
#sum13([1, 1])
sum13([1, 2, 2, 1, 13])

'''
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''
