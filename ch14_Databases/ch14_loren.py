# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:25:32 2019

@author: loren
"""

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect("task1.db")
c = conn.cursor()

###TASK 1 - CREATE TABLE AND INSERT DATA
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO StuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()    
    
###TASK 2 - INSERT DATA AUTOMATICALLY WITH VARIABLES
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "Python"
    value = random.randrange(0,10)
    c.execute("INSERT INTO StuffToBuild(unix, datestamp, keyword, value) VALUES (?,?,?,?)", (unix, date, keyword, value))
    conn.commit()
    
###TASK 3 - READ/SELECT DATA FROM DATABASE
def read_from_db_all():
    c.execute("SELECT * FROM stuffToBuild WHERE value = 8")
    for row in c.fetchall():
        print(row)
        
def read_from_db2():
    c.execute("SELECT * FROM stuffToBuild WHERE value = 8 and unix > 1537027981.80716 and unix < 1547028218.3566")
    for row in c.fetchall():
        print(row[0::3])
