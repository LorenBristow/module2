# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:33:47 2018

@author: loren
"""

import random

random_int = random.randint(0,10) 
print(random_int) 
#randint() gives rand no btw 2 boundaries inclusive.                  
#randint(0,1) gives either 0 or 1.     



fruit = ["apple", "orange", "pear", "peach", "cherry"]
random_fruit = random.choice(fruit)
print(random_fruit)
#give it a list and it picks a random element of the list

seating = ["Hien", "Loren", "Iza","Seraphine", "Ottilie", "Muna", "Sarika", "Rachel", "Katharina", "Ellen", "Kirsty", "Kate", "Leanne", "Milly", "Maggie", "Amina", "Gracy", "Mabel", "Jennifer", "Mandy", "Harriet", "Tilly", "Aminat","Mari", "Pam", "Roxy", "Amanda", "Martina"]
random.shuffle(seating)
print(seating)