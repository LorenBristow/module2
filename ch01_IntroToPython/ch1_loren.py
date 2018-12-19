# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:28:02 2018

@author: 612383225
"""

#note - check you are in a dedicated console - tools, prefs, run.
print("Hello world!")
A = 2+3        
B = 2.9+3.2 #Python 3 automatically converts to float where there is a point. 
C = (3.2/2.0)+7
D = 2**3 #exponentiation (what a word!)
E = 4**(1/2)
F = str(6)+'abacus' # joins 2 strings without space between. For space use , instead of +.
G = str(6),'abacus' # note the outcome here is a tuple. per test below. 
print (A)
print (B)
print (C)
print (D)
print (E)
print (F)
print (G)
print (type(G))
