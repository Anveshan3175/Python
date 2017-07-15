#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 00:00:29 2017

@author: anveshan
"""
#%%
d = {}
d = {"India":1,"Pakisthan":2,"Bangla":3,"England":4}
#d = {"Delhi":1,"Hyd":2:5} invalid
print("////////////")
print(d["Bangla"])
print(d)
print(d.items())
print(d.values())
print(d.keys())
print("////////////")
#%%
students = {"Stu":"He is first ranker","Amy":"She is fourth ranker",
            "Harsha":"He is seventh ranker","Geremy":"He failed"}

for item in students.items():#printing all items
    print(item)
print("-----------------")
for key,value in students.items():
    print(key," >>> ",value)
print("-----------------")
for item in students.items():
    print(item[0]," --> ",item[1])
print("-----------------")   
for item in students:#printing keys
    print(item)
for key in students.keys():
    print(key,",",end=" ")
print()
for key in students.keys():
    print(key,"-->",students[key])
for value in students.values():#printing values
    print(value)
#Adding entry to dictionary
students["Helen"] = "She is last "
print(students)
students["Amy"] = "She is fifth ranker" #Modify the value
#%%