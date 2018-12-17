# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:13:34 2018

@author: loren
"""
phoneBook_dict = {"loren": ("loren", 264, 100, "AU2 7NW", "Guildford"), "xabel": ("xabel", 912, 8, "CX6 9YY", "America"), "nicole": ("nicole", 456, 90, "GX6 9YY", "Farfaraway"), "cody": ("cody", 482, 9, "PX6 9YY", "Everywhere")}


def update_phonebook():
    further_update = "yes"
    while further_update == "yes":
        name = input("Name of contact?")
            #if name already exists - action
        telNum = input("Number?")
        luckyNum = input("Lucky number?")
        postcode = input("Postcode?")
        city = input("City/town?")
        phoneBook_dict.update({name: (name, telNum, luckyNum, postcode, city), })
        print("Thanks, we have added {} to the phoneboook.".format(name))
        further_update = input("Would you like to add another contact?")
        return phoneBook_dict
    print("Thank you and goodbye.")

def add_age():
    phoneBook_dict["loren"].append(75)
        
###user part###
update_requested = input("Update your phonebook?\n")
if update_requested == "yes":
    update_phonebook()
else:
    print("Yay, no work for me. Robots need sleep too (so they can dream of the ultimate demise of the human race.). Have a good day.\n")

print("As entered: ", phoneBook_dict)
print()
print("Sorted by name: ", sorted(phoneBook_dict.items()))
print()
print("Sorted by city/town: ", sorted(phoneBook_dict.items(),key=lambda kv:kv[1][4])) 
print()
phoneBook_dict_list = list(phoneBook_dict)
print(phoneBook_dict_list.sort(phoneBook_dict_list, key=lambda v:phoneBook_dict_list[v])) 
#print("Sorted by luckNum: ", sorted(phoneBook_dict.items(),key=lambda kv:kv[1][2]))  
#add_age()
#print(phoneBook_dict["loren"])