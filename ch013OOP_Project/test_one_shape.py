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
    
#me mucking about to learn the behaviours#    
#movingShape1 = movingShape(frame,"square", 150)
#movingShape1.goto(0,0)
#x = 50
#y = 50
#while x < 400:
#    movingShape1.goto(x,y)
#    x = x * 1.1
#    y = y * 1.1
#    movingShape1.goto(x,y)
#    movingShape1.goto(360,360)
#x = 360
#y = 360
#while x > 50:
#    movingShape1.goto(x,y)
#    x = x * 0.9
#    y = y * 0.9
#    movingShape1.goto(x,y)
#frame.close()
#end of mucking about