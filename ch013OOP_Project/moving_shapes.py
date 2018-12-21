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
        self.x = 0
        self.y = 0
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()
        
    def goto(self, x, y):
        self.figure.goto(x,y)
        
    def moveTick(self):
        if r() < 0.4:
            self.goto(self.x - self.dx,self.y - self.dy)
            self.x = self.x - self.dx
            self.y = self.y - self.dy
        else:
            self.goto(self.x + self.dx,self.y + self.dy)
            self.x = self.x + self.dx
            self.y = self.y + self.dy
        
class Square(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "square", diameter)
        self.x =50
        self.y = 50    
        
class Diamond(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "diamond", diameter)
        self.x =100
        self.y = 50
        
class Circle(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "circle", diameter)
        self.x =50
        self.y = 200
        
        