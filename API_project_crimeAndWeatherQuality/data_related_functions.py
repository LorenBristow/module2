# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:10:30 2019

@author: loren
"""

import sqlite3
import json
import time
import datetime
import requests
import csv

conn = sqlite3.connect("crimeAndWeatherQuality.db")
c = conn.cursor()


##### STEP 1 - POPULATE TABLE WITH CRIMES BY LOCATION VIA POLICE API. #####

def create_table_crimeStats():
    #c.execute("DROP TABLE crimeStats")
    c.execute("CREATE TABLE IF NOT EXISTS crimeStats(crime_id REAL, month TEXT, crime_category TEXT, x_coord REAL, y_coord REAL)")
#create_table_crimeStats()
    
def create_and_load_dates_of_available_crime_data():
    c.execute("CREATE TABLE IF NOT EXISTS dates_of_available_crime_data(date TEXT)")
    fname = open('dates_for_crime_stats.csv', 'r')
    count = 0
    reader = csv.reader(fname, delimiter=',')
    for i in reader: 
        date = i[2]
        c.execute("INSERT INTO dates_of_available_crime_data(date) VALUES (?)", (date,)) #always remember last comma to make tuple otherwise incorrect no. of bindings error. 
        conn.commit()
        count +=1
    print(count)
#create_and_load_dates_of_available_crime_data()
    
def data_entry_crimeStats():
    all_dates = c.execute("SELECT * FROM dates_of_available_crime_data")
    all_dates_list = []
    for each_date in all_dates:
        all_dates_list.append(each_date)
    conn.commit()
    print(all_dates_list)
    
    count_response_not_200 = 0
    count_response_200 = 0
    count_empty_list = 0
    count_of_postcodes = 0
    
    for item in all_dates_list:
        all_postcodes = c.execute("SELECT * FROM postcodes_by_coords")
        for i in all_postcodes: 
            count_of_postcodes += 1
            lat = i[1]
            lng = i[2]
            date = item
            endpoint = "https://data.police.uk/api/crimes-street/all-crime?"  
            payload = {"lat": lat, "lng":lng, "date":date}
            response = requests.get(endpoint, params = payload)
            if response.status_code == 200:
                print(response.url)
                count_response_200 += 1
                data = response.json()
                print(type(data))
                if not data: ####CHECK TO SEE THAT LIST IS NOT EMPTY. IF IT IS INDEX OUT OF RANGE ERROR OCCURS.
                    count_empty_list += 1
                    pass
                else:
                    count_hit_limit_of_15_per_second = 0 # note - haven't actually tested for number by TIME. Just slowing on 15. 
                    for result in data: 
                        crime_id = data[0]["id"]
                        date = data[0]["month"]
                        category = data[0]["category"]
                        lat = data[0]["location"]["latitude"]
                        lng = data[0]["location"]["longitude"]          
                        c.execute("INSERT INTO crimeStats(crime_id, month, crime_category, x_coord, y_coord) VALUES (?, ?, ?, ?, ?)", (crime_id, date, category, lat, lng))
                        conn.commit()   
                        count_hit_limit_of_15_per_second += 1
                        if count_hit_limit_of_15_per_second >= 15:
                            time.sleep(1)
                            count_hit_limit_of_15_per_second = 0
            else:
                count_response_not_200 += 1
        #        print(response.text)
    print("count_response_not_200 = " + str(count_response_not_200), "count_response_200 = " + str(count_response_200), "count_empty_list = " + str(count_empty_list), "count_of_postcodes = " + str(count_of_postcodes))
#data_entry_crimeStats()

##### END OF STEP 1. #####

##### STEP 2 - POPULATE TABLE WITH POSTCODES AND COORDINATES FROM EXCEL FILE. #####

def create_table_postcodes_by_coords():
    #c.execute("DROP TABLE postcodes_by_coords")
    c.execute("CREATE TABLE IF NOT EXISTS postcodes_by_coords(postcode TEXT, x_coord REAL, y_coord REAL)")
#create_table_postcodes_by_coords()
    
def read_in_postcodes_by_coords():
    fname = open('postcodes_geo.csv', 'r')
    count=0
    reader = csv.reader(fname, delimiter=',')
    for i in reader: 
        postcode = i[0]
        lat = i[13]
        lng = i[14]
        c.execute("INSERT INTO postcodes_by_coords(postcode, x_coord, y_coord) VALUES (?, ?, ?)", (postcode, lat, lng))
        conn.commit()
        count +=1
    print(count) # test number of records iterated matches file = 3112
#read_in_postcodes_by_coords()

##### END OF STEP 2. #####

##### STEP 3 - POPULATE TABLE CARBON INTENSTIY. #####

def create_table_CarbonIntensity():
    #c.execute("DROP TABLE carbonIntensity")
    c.execute("ALTER TABLE carbonIntensity ADD COLUMN region_name TEXT")
    #c.execute("CREATE TABLE IF NOT EXISTS carbonIntensity(date_time_from NUMERIC, date_time_to NUMERIC, intensity_forecast REAL, intensity_index TEXT, regionid NUMERIC, postcode NUMERIC)")
#create_table_CarbonIntensity()
    
def read_in_CarbonIntensity():
    #all_postcodes = c.execute("SELECT * FROM postcodes_by_coords")
    #for i in all_postcodes: 
        ####for 14_day_block in date_blocks: #need to read in from csv the from and to blocks. 
        ####need to later make them into months. what's the real stat method? ave of 2 2 week blocks is not same as average of individual 28 days. make this good - rolling average?
    date_query_from = '2018-12-15' #need to make dynamic
    date_query_to = '2018-12-28' #need to make dynamic
    postcode = 'RG10'  #need to make dynamic
    endpoint = 'https://api.carbonintensity.org.uk/regional/intensity/{}/{}/postcode/{}'.format(date_query_from, date_query_to, postcode)
    #payload = {"postcode":postcode}
    response = requests.get(endpoint)
    #print(endpoint)
    if response.status_code == 200:
        print(response.url)
        data = response.json()
        if data:
            date_time_from = data["data"]["data"][0]["from"]
            date_time_to = data["data"]["data"][0]["to"]
            intensity_forecast = data["data"]["data"][0]["intensity"]["forecast"]
            intensity_index = data["data"]["data"][0]["intensity"]["index"]
            region_name = data["data"]["shortname"]
            regionid = data["data"]["regionid"] # * call key in dict then key in dict whereas for crime it's list first so slice to index position which is a dict then call key in dictionary. 
            #print(regionid, region_name, date_time_from,date_time_to, intensity_forecast,intensity_index) # test results match example api called. All OK :)
            c.execute("INSERT INTO CarbonIntensity(date_time_from, date_time_to, intensity_forecast, intensity_index, regionid, postcode, region_name) VALUES (?, ?, ?, ?, ?, ?, ?)", (date_time_from, date_time_to, intensity_forecast, intensity_index, regionid, postcode, region_name))
            conn.commit()
    elif response.status_code == 400:
        print("error - bad request - 400")
    elif response.status_code == 500:
        print("error - internal server error - 500")
    ##
#        lat = i[1]
#        lng = i[2]
#        date = item
#        endpoint = "https://data.police.uk/api/crimes-street/all-crime?"  
#        payload = {"lat": lat, "lng":lng, "date":date}
#        response = requests.get(endpoint, params = payload)
#        if response.status_code == 200:
#            print(response.url)
#            count_response_200 += 1
#            data = response.json()
#            print(type(data))
#            if not data: ####CHECK TO SEE THAT LIST IS NOT EMPTY. IF IT IS INDEX OUT OF RANGE ERROR OCCURS.
#                count_empty_list += 1
#                pass
#            else:
#                count_hit_limit_of_15_per_second = 0 # note - haven't actually tested for number by TIME. Just slowing on 15. 
#                for result in data: 
#                    crime_id = data[0]["id"]
#                    date = data[0]["month"]
#                    category = data[0]["category"]
#                    lat = data[0]["location"]["latitude"]
#                    lng = data[0]["location"]["longitude"]          
#                    c.execute("INSERT INTO crimeStats(crime_id, month, crime_category, x_coord, y_coord) VALUES (?, ?, ?, ?, ?)", (crime_id, date, category, lat, lng))
#                    conn.commit()   
#                    count_hit_limit_of_15_per_second += 1
#                    if count_hit_limit_of_15_per_second >= 15:
#                        time.sleep(1)
#                        count_hit_limit_of_15_per_second = 0
#        else:
#                count_response_not_200 += 1
#    ##
#    
read_in_CarbonIntensity()

##### END OF STEP 3. #####
    

