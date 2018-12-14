# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:03:56 2018

@author: loren
"""

salary = {} #creates empty dictionary
salary["al"] = 20000
print(salary)
salary["bo"] = 50000
print(salary)
salary["bo"] = 55000
print(salary)
salary["al"] = int(20000 *1.1)
print(salary)
salary[7] =("Joke", "Chen", "Bond") # just to show that key and value can 
#be any data type and any number of them. NOTE! can't start number with 0!
print(salary)

print(salary["bo"]) #getting values

salary["al"] += 2000
print(salary["al"]) 

phonenumbers ={}
phonenumbers["mabel"] = 913
phonenumbers["amanda"] = 858
phonenumbers["ottilie"] = 344
print(phonenumbers)

digits = {"mabel": 3914, "amanda": 5858, "ottilie": 8344} # shorter way than phonenumbers above. 
print(digits)
digits["amanda"] +=1
print(digits)

#delete a 'key value pair' 
del digits["mabel"] # same as delete item in list. 'del' function is not Obj. oriented.
print(digits)

print(digits.keys())
print(digits.values())

print(type(digits.keys()))
print(type(digits.values()))

digits_keys = list(digits.keys())
print(digits_keys)
print(digits_keys[0]) # fetch out a specific key

#note - key lookup error - trying to lookup a key that's not in dictionary = error = crash. major.
#so use 'in' logic to first test for existence and only proceed if exists == True.

#lookupName = "loren"   #use variable for test to make easy to reuse and change only one thing i.e key here. 
#if lookupName in digits:
#    print(lookupName, ":", digits[lookupName])
#else:
#    print(input("Create {}?".format(lookupName)))
#    if input == "yes": # need to complete this. 
#      
  
counts = {"a":3, "c":1, "b":5}
labels = list(counts.keys())
print(counts)
print(labels)

labels.sort(key=lambda v:counts[v]) # puts labesl in asc order of count. 
print(labels)

print(sorted(counts.items(), key=lambda kv:kv[1]))


lucky = {}
lucky["amanda"] = [7, 4]
lucky["ottilie"] = [5, 2]
lucky["mabel"] = [4, 12]
print(lucky)
lucky_keys = list(lucky.keys())
print(lucky_keys)
lucky_keys.sort(key=lambda v:lucky[v]) # need to understand how to sort by values instead of keys. 
print("x", lucky_keys)
lucky_values = list(lucky.values())
print(lucky_values)

print(sorted(lucky.items(), key=lambda kv:kv[0])) #sorts by key
print(sorted(lucky.items(), key=lambda kv:kv[1])) # sorts on first part of the list within each tuple
print(sorted(lucky.items(), key=lambda kv:kv[1][1])) # sorts by second part of the list within each tuple


print()
print()

abc = {1:("greg", "january", 7), 2:("anna", "october", 3), 3:("mag", "november", 13) }
print(abc)
abc_keys = list(abc.keys())
print(abc_keys)
abc_keys.sort(key=lambda k:abc[k]) #going by names
print('straight k',abc_keys)
abc_keys.sort(key=lambda k:abc[k][1])  #going by months
print(abc_keys)
abc_keys.sort(key=lambda k:abc[k][2])  #going by months
print(abc_keys)

#''' ON ORDERING IN DICT - ORDER OF ENTRY
#accepted
#It does rather depend on what you mean by first. In Python 3.6, entries in a dictionary are ordered by the key, but probably not quite in the way you expect.
#
#To take your example:
#
#>>> data = {"Key1" : "Value1", "Key2" : "Value2"}
#Now add the key 0:
#
#>>> data[0] = "Value0"
#>>> data
#{'Key1': 'Value1', 'Key2': 'Value2', 0: 'Value0'}
#So the zero comes at the end. But if you construct the dict from scratch, like this:
#
#>>> data = {0: "Value0", "Key1" : "Value1", "Key2" : "Value2"}
#you get this result instead
#
#>>> data
#{0: 'Value0', 'Key1': 'Value1', 'Key2': 'Value2'}
#This illustrates the principle that you should not depend on the ordering, which is defined only by the dict implementation, which, in CPython 3.6 and later, is order of entry. To illustrate that point in a different way:
#
#>>> data = {0: "Value0", "Key1" : "Value1", "Key2" : "Value2"}
#>>> sorted(data.keys())
#Traceback (most recent call last):
#  File "<pyshell#42>", line 1, in <module>
#    sorted(data.keys())
#TypeError: '<' not supported between instances of 'str' and 'int'
#Guido has this to say on the subject:
#
#I'd like to handwave on the ordering of ... dicts. Yes, in CPython 3.6 and in PyPy they are all ordered, but it's an implementation detail. I don't want to force all other implementations to follow suit. I also don't want too many people start depending on this, since their code will break in 3.5. (Code that needs to depend on the ordering of keyword args or class attributes should be relatively uncommon; but people will start to depend on the ordering of all dicts all too easily. I want to remind them that they are taking a risk, and their code won't be backwards compatible.)'''