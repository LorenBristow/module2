# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:47:11 2018

@author: loren
"""

from moving_shapes import *

frame = Frame()
shape1 = Square(frame, 100)
for i in range(100):
    shape1.moveTick()
    