# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:00:39 2018

@author: loren
"""

from moving_shapes import *
frame = Frame()
numshapes = 3
shapes = []
for i in range(numshapes):
    shapes.append(Square(frame, 100))
    shapes.append(Circle(frame, 100))
    shapes.append(Diamond(frame, 100))
for i in range(100):
    for shape in shapes:
        shape.moveTick()