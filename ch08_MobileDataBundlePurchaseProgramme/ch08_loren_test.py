# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:13:00 2018

@author: loren
"""

from ch08_loren_functions_project import *

 Test call to programme:
print ('TEST EXAMPLE 1')
# database input, you will still need to check user pin
result = checkPasscode('1234')
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = checkPasscode('2345')
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = checkPasscode('3456')
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')