# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:13:34 2018

@author: loren
"""

phoneBook_dict = {"loren": (264, 100, "AU2 7NW", "Guildford"), "xabel": (912, 8, "CX6 9YY", "America"), "nicole": (456, 90, "GX6 9YY", "Farfaraway"), "cody": (482, 9, "PX6 9YY", "Everywhere")}

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
        print("Thanks, we have added {} to the phonebook.".format(name))
        further_update = input("Would you like to add another contact?")
        return phoneBook_dict
         
#values_to_edit = list(phoneBook_dict["loren"])
#            values_to_edit.append(65)
#            phoneBook_dict["loren"] = tuple(values_to_edit)
        
###user part###
update_requested = input("Update your phonebook with a new contact?\n")
if update_requested == "yes":
    update_phonebook()
#else:
#    print("Yay, no more work for me. Robots need sleep too (so they can dream of the ultimate demise of the human race.). Have a good day.\n")
new_field = input("Would you like to add any new information to your existing contacts?")
if new_field == "yes":
    new_field_name = input("What is the name of the new field?")
    for key in phoneBook_dict:
        value_for_new_field = input("What should {} for {} be?".format(new_field_name, key))
        phonebook_value_list = list(phoneBook_dict[key])
        phonebook_value_list.append(value_for_new_field)
        phoneBook_dict[key] = tuple(phonebook_value_list)
      
print("As entered: ", phoneBook_dict)
print()
print("Sorted by name: ", sorted(phoneBook_dict.items()))
print()
print("Sorted by city/town: ", sorted(phoneBook_dict.items(),key=lambda kv:kv[1][3])) 
print()


#phoneBook_dict_list = list(phoneBook_dict)
#print(phoneBook_dict_list.sort(phoneBook_dict_list, key=lambda v:phoneBook_dict_list[v])) 
#print("Sorted by luckNum: ", sorted(phoneBook_dict.items(),key=lambda kv:kv[1][2]))  
#add_age()
#print(phoneBook_dict["loren"])

#record = str(phoneBook_dict["loren"])
#print(record)

f = open("phonebook.txt", "w")
f.write(str(sorted(phoneBook_dict.items())))
f.close()


