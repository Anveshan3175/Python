#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:14:57 2017

@author: anveshan
"""

#%%
def testEquals():
    """ This method test equals"""
    while True:
        print("If you enter 999, program exits")
        
        number1 = input("Enter first number : ")
        
        if(not(number1) or not(number1.isdigit())):
            number1 = input("Enter valid number : ")
        else:
            number1 = int(number1)
            
        number2 = input("Enter second number : ")
        
        if(not(number2) or not(number2.isdigit())):
            input("Enter valid number : ")
        else:
            number2 = int(number2)
        
        if((int(number1) == 999) or (int(number2) == 999)):
            print("Program is exiting")
            break
        else:
            if(number1 == number2):
                print("Numbers you have entered are equal")
            else:
                print("Numbers you have entered are not equal")

#%%
def testEqualsDebug():
    """ This is to debug above issue"""
    while True:
        print("Enter a number other than 999 to continue")
        number = input("Enter your number")
        
        if(number == '999'):
            break
        else:
            print(number * 10)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
