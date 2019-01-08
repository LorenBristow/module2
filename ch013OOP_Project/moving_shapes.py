# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:26:19 2018

@author: loren
"""
###to do:

#bounce off eachother?
#image on bounce?
#background colour based on which bounces?
from shapes import *
from pylab import random as r
import random
import math

class movingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
                      
        self.minx = self.diameter/2
        self.miny = self.diameter/2
        
        self.maxx = frame.width - self.minx 
        self.maxy = frame.height - self.miny
        
        self.x = int(self.minx + r() * (self.maxx - self.minx))
        self.y = int(self.miny + r() * (self.maxy - self.miny))
      
       
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()
        
        self.area = diameter ** 2
               
    def pudding(self, x, y): # pudding was 'goto' - duplicate naming. 
        self.figure.goto(x,y)
        
    def moveTick(self):
        if self.x + self.dx > self.maxx:
            self.x = self.maxx
            self.dx = -1 * self.dx
            print("I am a maxx {} and my area is {} square units.".format(self.shape, self.area))
  
        elif self.x + self.dx < self.minx:
            self.x = self.minx
            self.dx = abs(self.dx)
            print("I am a minx {} and my area is {} square units.".format(self.shape, self.area))
        else:
            self.x += self.dx
            
        if self.y + self.dy > self.maxy:
            self.y = self.maxy
            #self.y -= self.dy
            self.dy = -1 * self.dy
            print("I am a maxy {} and my area is {} square units.".format(self.shape, self.area))
        elif self.y + self.dy < self.miny:
            self.y = self.miny
            #self.y += self.dy            
            self.dy = abs(self.dy)
            print("I am a miny {} and my area is {} square units.".format(self.shape, self.area))
        else:
            self.y += self.dy
                
        self.pudding(self.x, self.y) 
  
    def bounce(self):
        pass
        
class Square(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "square", diameter)  
       
class Diamond(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "diamond", diameter)
        #self.diameter = round(math.sqrt((diameter**2 + diameter**2)))
        self.diameter = math.sqrt((diameter**2 + diameter**2))
        self.minx = self.diameter/2
        self.miny = self.diameter/2 
        self.maxx = frame.width - self.minx
        self.maxy = frame.height - self.miny 

class Circle(movingShape):
    def __init__(self, frame, diameter):
        movingShape.__init__(self, frame, "circle", diameter)
        self.area = round(math.pi * ((diameter/2) ** 2))
        
        