# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:34:10 2019

@author: loren
"""
import sqlite3
conn = sqlite3.connect("phonebook.db")
c = conn.cursor()
from phonebook_db_functions import *

c.execute("SELECT postcode FROM person")    
postcode = c.fetchall()
#print(postcode)
cleanpostcode = ""
for i in postcode:
    for char in i[1]:
#        print(i)
        cleanpostcode = cleanpostcode + str(i)
        print(cleanpostcode)
