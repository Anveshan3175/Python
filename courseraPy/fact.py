#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:31:38 2017

@author: anveshan
"""

#%%
def fact(n):
    """ This is calculate factorial of number through recursion """
    if (n > 1):
        return n * fact(n-1)
    else :
        return 1
    

#%%
fact(5)
#%%
def factorial(n):
    """ Calculate factorial using while """
    fact = 1
    while(n > 1):
        fact = n * fact
        n = n - 1
    return fact
#%%
factorial(5)
#%%
def callFact():
    num = input("Enter a number :")
    print("The factorial is ",factorial(int(num)))
#%%