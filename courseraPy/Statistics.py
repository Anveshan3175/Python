#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 05:18:45 2017

@author: anveshan
"""

#%%
def testException(num):
    """This function tested exception"""
   # num = "test"
    
    try:
        neg = (-1) * num
        print(neg)
    except Exception as e:
       print(e)
    print("finally")


#%%
def test_try():
    """ This function tests try block """
    numb = input("Enter a number")
    print(type(numb))
    try:
        num = float(numb)
        print(num)
    except Exception as e: # if there is exception,we wont crash,we will catch it
        print(e)
    print("Exiting the program")
#%%
import random
temps = []
random.seed(77)
for i in range (0,20):
    temps.append(random.randint(20,95))

#%%
import statistics
def test_stat(temp):
    print(temp)
    "This function runs stats"
    print("The mean is : ",statistics.mean(temp))
    #print("The mode is : ",statistics.mode(temp))
    temp.sort()
    #print(temp)
    print("The median is : ",statistics.median(temp))
    print("The std deviation is : ",statistics.stdev(temp))
    try:
        print("The mode is : ",statistics.mode(temp))
    except statistics.StatisticsError as e:
        print (e)
    print("Variance is ",statistics.variance(temp))
    print("Max value of list : ",max(temp))
    print("Min value of list : ",min(temp))
    print("Sum of list : ",sum(temp))
    print("Avg value of list : ",(sum(temp)/len(temp)))
#%%
test_stat(temps)
#%%
import platform
print(platform.python_version())
#%%



















