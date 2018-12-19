# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:26:19 2018

@author: loren
"""

from shapes import *
from pylab import random as r

class movingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.jitterbug = (0,0)
        self.dancingqueen = (0,0)
        self.footloose = (0,0)
        self.dx = 200
        self.dy = 200
    
    def goto(self, x, y):
        self.figure.goto(x,y)
        
    def moveTick(self):
        x = 0
        y = 0
        self.goto(x + self.dx,y + self.dy)
        self.goto(x + 2 * self.dx,y + 2 * self.dy)
           
            
class Square(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "square", diameter)
        
class Diamond(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "diamond", diameter)
        
class Circle(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "circle", diameter)
        
        
        