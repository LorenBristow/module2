# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:47:27 2018

@author: loren
"""

from shapes import *

frame = Frame()
s1 = Shape("square", 100)
s1.goto(200, 100)
x = 200
y = 100
for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5
frame.close()


