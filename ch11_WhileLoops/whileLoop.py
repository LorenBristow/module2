# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:26:08 2018

@author: loren
"""

#x = 33
#count = 0
#while x >= 1:
#    print(x, ":", end="")
#    x = x/2
#    count += 1
#print(x)
##print(count)

def gun(n):  #review this - not from a code perspective, from a maths persepctive. 
    trisum = 0
    while n > 0:
        trisum = trisum + n
        n -= 1
        print(trisum)
        print(n)
    print(trisum)
    print(n)

gun(5)

def create_dictionary(className):
        classResults = {}
        result(class_size,classResults)
        

def result(class_size,classResults):  # what is the best practice for exiting while loop. Break not being optimal and not wanting to assign a fake value to a variable. 
    while class_size > 0:
        class_size -= 1
        student_name = input("Student's name?")
        mark_given = int(input("What is the mark given?"))
        if mark_given >= 70:
            student_result = "First Class Pass"
            classResults.update({student_name: (mark_given, student_result), })
            print("First class pass")
            print(classResults)
            mark_given = 0
            #break
        elif mark_given >= 40:
            student_result = "Pass"
            classResults.update({student_name: (mark_given, student_result), })
            print("Pass, but there is room for improvement")    
            mark_given = 0
            print(classResults)
            #break
        else: 
            student_result = "Fail"
            classResults.update({student_name: (mark_given, student_result), })
            print("Fail.")
            mark_given = 0
            print(classResults)
            #break
    f = open("{}.txt".format(className), "r+")
    f.write(classResults)
    f.close()

className = input("What class are you inputting marks for?")
class_size = int(input("How many students are in the class?")) 
create_dictionary(className)




