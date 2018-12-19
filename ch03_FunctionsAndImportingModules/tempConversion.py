# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:37:17 2018

@author: loren
"""
def convert_temp():
    celcius = int(input("Input a temp in celcius for conversion?"))
    fahrenheit = celcius * 9 / 5 + 32
    kelvin = celcius + 273.15
    print("That's " + str(fahrenheit) + " in fahrenheit and " + str(kelvin) + " in kelvin.")
    return "That's " + str(fahrenheit) + " in fahrenheit and " + str(kelvin) + " in kelvin."

convert_temp()