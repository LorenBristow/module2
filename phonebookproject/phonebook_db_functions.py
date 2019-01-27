# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:25:32 2019

@author: loren
"""

import sqlite3
from phonebook_user_input import *

conn = sqlite3.connect("phonebook.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS business(business_name TEXT, business_category TEXT, address1 TEXT, town_city TEXT, county TEXT, postcode TEXT, telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS person(surname TEXT, firstname TEXT, address1 TEXT, town_city TEXT, county TEXT, postcode TEXT, telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS coordinate_mapping(town_city TEXT, postcode TEXT, x_coordinate REAL, y_coordinate REAL)")

#create_table()

def data_entry_business():
    c.execute("INSERT INTO business VALUES('Pizza Express','restaurant','136-140 Herne Hill','herne hill',' London',' SE24 9QH','020 7738 3373')")                
    conn.commit()
    c.close()
    conn.close()
    
def data_entry_person():
    c.execute("INSERT INTO person VALUES('Wright','H','Flat 11 Wodehouse Place 41 Epsom Road','Guildford','Surrey','GU1 3HX','01483 614446')")                
    conn.commit()
    c.close()
    conn.close()

#data_entry_business()
#data_entry_person()
    
    
c.execute("SELECT postcode FROM person")    
postcodelist = c.fetchall()



#####USER INPUTS    


#     
#def search_for_person():
#    surname_entered = input("Surname of person?")
#    location_entered = input("Town/city or postcode?")
#    c.execute("SELECT * FROM person WHERE surname=?", (surname_entered,))
#    for row in c.fetchall():
#        print(row)
#    #c.execute('SELECT * FROM db_name WHERE City=?' , (city_searched,)); 
#    #here City is the column in your table and city_searched is the variable you are filtering by)
    #print(row)

##search_type = input("Search for person or business?")
#raw_input("Search for person or business?\n")
#search_type = raw_input
#
#if search_type == "person":
#    print("person")
#elif search_type == "business":
#    print("business")
#else:
#    print("unrecognised search type")
    
    
    

