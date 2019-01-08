# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:00:39 2018

@author: loren
"""

from moving_shapes import *
frame = Frame()
numshapes = 2
size = 100
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame, size))
    #shapes.append(Circle(frame, size))
    #shapes.append(Diamond(frame, size))

for i in range(100):
    for shape in shapes:
        shape.moveTick()
   
    
#frame.close()        