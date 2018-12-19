# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:57:10 2018

@author: loren
"""

def sum_double(a, b):
    if a == b:
        print((a + b) * 2)
    else:    
        print(a + b)
    
sum_double(1, 2)    

def front_back(str):
    #needed an if statement to deal with str length of 1 which has index out of range beyond 0!
    
    print(str[-1] + str[1:-1] + str[0])
    return str[-1] + str[1:-1] + str[0]

front_back("loren")

def make10(a, b):
   if (a + b) == 10 or (a == 10 or b == 10):
       print("True")
   else:
       print("False")
make10(10, 5)
make10(6, 4)
make10(10,10)

## i kept getting this wrong  on submission -STUPID, had quotes around True and False. 
#def makes10(a, b):
#  if (a + b) == 10 or (a == 10 or b == 10):
#    return True
#  else:
#    return False

def not_string(str):
  if (str[0:3] == "not"):
      return not_string
  else:
      return "not" + str

#not_string("notnow")
#not_string("justnow")
not_string("a")


def no_teen_sum(a, b, c):
  if a in  [13, 14, 17, 18, 19]:
    fix_teen(a)
  if b in  [13, 14, 17, 18, 19]:
    fix_teen(b)
  if c in  [13, 14, 17, 18, 19]:
    fix_teen(c)
  print(a+b+c)
  return a + b + c

def fix_teen(n):
  n = 0
  
no_teen_sum(2, 4, 15)