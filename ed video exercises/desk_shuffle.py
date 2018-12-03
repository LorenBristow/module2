# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:33:17 2018

@author: loren
"""

import random

seating = ["Hien", "Loren", "Iza","Seraphine", "Ottilie", "Muna", "Sarika", "Rachel",\
           "Katharina", "Ellen", "Kirsty", "Kate", "Leanne", "Milly", "Maggie", "Amina",\
           "Gracy", "Mabel", "Jennifer", "Mandy", "Harriet", "Tilly","Roxy", "Aminat","Mari",\
           "Pam", "Fabiana", "Amanda", "Martina"]
random.shuffle(seating)
print(seating)
print()
for n in range(0,16,4):
    print(seating[n:n+4])
    print()
for n in range(16,19):
    print(seating[n:n+3])    
#for n in range(0,30,4):
#    print(seating[n:n+4])
# 
