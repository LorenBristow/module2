# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:54:39 2018

@author: loren
"""


import datetime
now = datetime.datetime.now()
print(datetime.datetime.now())
endOfDay = datetime.datetime.now().replace(hour=17,minute=0,second=0,microsecond=0)
print(endOfDay)
timeLeft = endOfDay - now
print(timeLeft)
timeNeededMinutes = 20 * 29
print(timeNeededMinutes)
timeLeftForExtract = str(timeLeft)
print(timeLeft)
timeLeftMinutes = int(timeLeftForExtract[0]) * 60 + int(str(timeLeftForExtract[2]+timeLeftForExtract[3]))
print(timeLeftMinutes)

def enoughTimeLeft(timeLeftMinutes,timeNeededMinutes):
    if timeLeftMinutes >= timeNeededMinutes:
        surplus = timeLeftMinutes - timeNeededMinutes
        print("Enough time is left. This is possible and will remain so if you start assessing within {} minutes.".format(surplus))
    else:
        deficit = timeNeededMinutes - timeLeftMinutes
        print("Nope. No. Cannot be done. There are {} minutes too few left.".format(deficit))
       
        
        
        
enoughTimeLeft(timeLeftMinutes,timeNeededMinutes)