# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:57:39 2019

@author: loren
"""
'''Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter on a new line.

For every third letter, write it to the console in lowercase instead.

For every fourth letter, write its numeric position in the alphabet to the console instead (e.g. instead of outputting 'D' output '4').

If a letter satisfies both rules 2 and 3, write out its numeric position followed by the letter in lowercase (e.g. 'L' should be output as '12l').'''

#Question 1:
import string
alphabet = string.ascii_lowercase.upper()
for i in alphabet:
    print(i.upper())

#Question 2:
for i in range(len(alphabet)):
    if (i+1) % 3 == 0:
        print(alphabet[i].lower())
    else:
        print(alphabet[i])

#Question 3:
for i in range(len(alphabet)):
    if (i+1) % 4 == 0:
        print(i)
    else:
        print(alphabet[i])

#Question 4:
        