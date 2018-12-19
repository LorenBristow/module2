# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:55:58 2018

@author: loren
"""



def extra_end(str):
    print(len(str))
    print((str[(len(str)-1)]+str[(len(str)-1)])*3)
extra_end('cat')


def extra_end_otherway(str):
    print(str[:-4])
extra_end_otherway('amazing')