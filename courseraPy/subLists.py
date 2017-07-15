#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 23:15:56 2017

@author: anveshan
"""
#%%
places = [["India","Delhi",7],["China","Being"] ]

#%%

def parse_lists(lists):
    """ This function parses multiple lists """
    for i in range(0,len(lists),1):
        ##print("The element is: ",lists[i])
        for j in range(0,len(lists[i]),1):
            print("The element is: ",lists[i][j])

#%%
def calculate_Population(popList):
    """ Calculates population of country"""
    totalPulation = 0
    for i in range(0,len(popList),1):
        #for j in range(0,len(popList[i]),1):
        totalPulation += popList[i][1]
        print("agg Population is ", popList[i][1])
    print("Total population of country is ",totalPulation)
#%%
IndPop = [["Hyderabad",1000],["Bombay",3000],["Delhi",6000]]           
#%%       
def average(nlis):
    """ This function calculates the average of the list"""
    sum = 0
    for i in range(0,len(nlis),1):
        sum += nlis[i]
        print("Number in the list is ",nlis[i])
    print("Average of the list is ",sum/len(nlis))
#%%
numlis = [65,44,3,56,48,74,7,97,95,42]
numlis2 = [4,6,8,12,2,7,19]
#%%
average(numlis)
#%%
average(numlis2)
#%%
def percent(marks):
    """Calculate percentage of marks"""
    sum = 0
    for mark in marks:
        sum += mark
    print("Percentage is ",(sum/len(marks)))
#%%
















