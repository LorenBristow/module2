# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:34:58 2019

@author: loren
"""
import config
import requests

endpoint = "https://api.openweathermap.org/data/2.5/weather"

payload = {"q": "London, UK", "units":"metric", "appid":config.weather_api_key}

response = requests.get(endpoint, params = payload)
data = response.json()
print(response.url)
print(response.status_code)
print(response.headers["content-type"])
print(response.text)

temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print(u"\nIt's {}\u2103 in {}, and the sky is {}".format(temperature,name,weather))