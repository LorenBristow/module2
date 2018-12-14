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


#def makes10(a, b):
#    if ((a + b) == 10) or (a == 10 or b == 10):
#        print("True")
#    else:
#        print("False")
#makes10(10, 10)

#def makes10(a, b):
#  if ((a + b) == 10):
#    print("true")
#    return "True"
#  elif (a == 10):
#    print("true")  
#    return "True"
#  elif (b == 10):
#    print("true")  
#    return "True"
#  else:
#    print("fasle")
#    return "False"
#makes10(10, 10)