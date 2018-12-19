# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:34:06 2018

@author: loren
"""
class Animal():
    def eat(self):
        print("yum")

class Dog(Animal):
    def bark(self):
        print("Woof!")
            
class Cat(Animal):
    def meow(self):
        print("Meow")
        
class Robot():
    def move(self):
        print("...move move move...")
        
class CleanRobot(Robot):
    def clean(self):
        self.move()
        print("I vacuum dust")

class CookRobot(Robot):
    def cook(self):
        print("I make rice")

class SuperRobot():
    def __init__(self):
        self.o1 = Robot()   #note - could not use a 0 here, had to use o for the numbers
        self.o2 = Dog()
        self.o3 = CleanRobot()
  
    def playGame(self):
        print("alphago game")
    
    def move(self):
        return self.o3.move()
    
    def eat(self):
        return self.o1.eat()
    
    def bark(self):
        return self.o2.bark()   
    
    def clean(self):
        return self.o3.clean()

    def __str__(self):
        return (self.o2.name)

olly = SuperRobot()
olly.bark()  
olly.move()
olly.clean()
atti = CookRobot()
atti.cook()


