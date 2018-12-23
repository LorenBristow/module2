# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:26:19 2018

@author: loren
"""

from shapes import *
from pylab import random as r
import random

class movingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.x = random.randint(diameter/2, (frame.width - diameter/2))
        self.y = r() * 800
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()
        
    def goto(self, x, y):
        self.figure.goto(x,y)
        
    def moveTick(self):
        if r() < 0.5:
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
        self.x = r() * 100
        self.y = r() * 100    
        
class Diamond(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "diamond", diameter)
        self.x = r() * 100
        self.y = r() * 100
        
class Circle(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "circle", diameter)
        self.x = r() * 100
        self.y = r() * 100
        
        