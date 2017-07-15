#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 18:17:38 2017

@author: anveshan
"""
#%%

str1 = "Hi there. This is to be displayed "+\
"in a single line"

str2 = ("Hi there. This is another way "
"to be displayed in the single line")

#%%
import random
def make_random(last):
    ''' This is an example of random function'''
    rList = []
    for i in range(1,last,1):
        rList.append(random.randint(1,100))
    return rList   


#%%
def call_make_random():
    ran_list = make_random(20)
    print("List of random numbers is",ran_list)
#%%
import random
def same_random(end,seed):
    rList=[]
    random.seed(seed)
    for i in range(1,end):
        rList.append(random.randint(1,100))
    return rList
#%%
def call_same_random():
    print("Random same list is :",same_random(10,7))
#%%
import random
def make_random_real(seed=0):
    if seed != 0:
        random.seed(seed)
    rList = []
    for i in range(1,10):
        rList.append(random.random())
    return rList
#%%
def call_make_random_real():
    print("The random list is ",make_random_real(17))
#%%
call_make_random_real()
#%%
def sorted_list():
    """ This function sorts the list"""
    rList = []
    for i in range(1,10):
        rList.append(random.randint(1,100))
    print(id(rList),"List is :",rList)
    rList.sort()
    print(id(rList),"List is :",rList)

#%%
sorted_list()
#%%
sorted([45,12,89,34,4,98])
#%%
def list_aphabets(word):
    ''' This function generates alphabets from word'''
    for char in word:
        print(char,",",end="")
    print()
    print(list(word))
    charList = list(word)# Converts string to elements in list
    seperator = ","
    print(seperator.join(charList))#joins the chars
#%%
list_aphabets("pneumonia")
#%%
import random
def make_alpha_list(seed=0):# default value
    """ Function creates alphabet list """
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    #print(alphabets)
    alphaList = []
    if seed != 0:
        random.seed(seed)
        
    for i in range(1,10):
       # print(i,end="")
        alphaList.append(random.choice(alphabets))
    print("Printing random list")
    print("unsorted list : ",alphaList)
    alphaList.sort()
    print("sorted list : ",alphaList)
    return alphaList
        
    
#%%
make_alpha_list()
#%%
alist = make_alpha_list(40)
#%%
alist = ['r','y','u']
alist.sort()
print(alist)
#%%
import platform
print(platform.python_version())
#%%
alphaList = ['q','W','t','y','F','w','d','x','M']
alphaList.sort()
print(alphaList)
#%%
alphaList = ['q','W','t','y','F','w','d','x','M']
alphaList.sort(key=str.lower)
print(alphaList)
#%%
strList = ["ant","Bun","Ted","Uno","Loe","str"]
print(strList)
strList.sort()
print(strList)
strList.sort(key=str.lower)
print(strList)
#%%













