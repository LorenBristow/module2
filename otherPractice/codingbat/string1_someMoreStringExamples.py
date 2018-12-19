# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:43:27 2018

@author: loren
"""

def left2(str):
    print(str[2:(len(str))] + str[0:2])
    return str[2:(len(str))] + str[0:2]
left2("loren")

####

def make_abba(a, b):
    print(a + b + b + a)
    return a + b + b + a
make_abba("Merry", "Christmas")

####

def make_tags(tag, word):
    print("<" + tag + ">" + word + "</" + tag + ">")    
    return "<" + tag + ">" + word + "</" + tag + ">"
make_tags("body", "heart")