#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:29:51 2017

@author: anveshan
"""
#%%
def printEven(limit):
    """This function prints even numbers till the number we have supplied"""
    i = 0
    while(i <= limit ):
        print(i,",")
        i += 2
#%%
def count_down():
    """ This function counts to 1 from 10 """
    count = 10
    while (count >= 0):
        print(count,end=" ") ### appends to same line
        count -= 1
    print() ### starts new line
    print("Blast off now")

#%%
def cheer():
    """ This function uses for loop instead of while loop"""
    for i in range(2,9,2): # range is 2 to 9 with increments of 2
        print(i,end=" ")
    print()
#%%
def count_down_loop():
    """ count down using for loop """
    for i in range(10,0,-1):
        print(i,end=" ")
    print()
#%%
lst = [1,2,3,4,5,6,7,8,9]
#%%
fulList = range(2,20,2)
filterList = list(range(2,20,2))















