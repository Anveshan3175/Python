#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:39:18 2017

@author: anveshan
"""

#%%
def basic_string():
    """ This is basic string"""
    print("Hi There".split( ))
    
#%%
def get_char_from_string():
    """ Demo for extracting chars from string"""
    word = 'penchant'
    length = len(word)
    for i in range (0,length,1):
        print(word[i],end=" ")
    
    
#%%
get_char_from_string()
#%%
def basic_list():
    """ This is demo of basic lists """
    num_list = [3,4,9,1,7,5,2,6,8]
    length = len(num_list)
    print("Length of list is ",length)
    print("List is ",num_list,end="")
    print()
    for i in range(0,length,1):
        print(num_list[i] * 4,",", end =" ")
    print()
    ## index start from 0. In range, last index is excluded
    print("Printing range 2 to 7 ",num_list[2:7])
    print()
    print("printing all numbers from first to index 6",num_list[:7])
    print()
    print("Printing all number from 3 to last index",num_list[3:])
        
#%%
basic_list()
#%%
def basic_list_ext():
    """ Some more basic list functionalities """
    str_list = ['e','j','k','r','f','a','w','q']
    print(str_list)
    str_list.append('m')
    print(str_list)
    print("'z' is in the list : ",'z' in str_list)
    print("'K' is in the list : ",'k' in str_list)
    if('w' in str_list):
        print("w is in list")
    if('r' in str_list or 'w' in str_list):
        print("Either 'r' or 'w' is in the list ")
    if('z' not in str_list):
        print("'z' is not in the list ")
    if('j' in str_list and 'f' in str_list):
        print("Both 'j' and 'f' are in list ")
    
#%%
basic_list_ext()
#%%
alphas = ['a','w','b','j','a','b','a','y','a']
numList = [1,2,3,4,5,6,7,8,9]
negList = [3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4]
lastList = numList[5:]
#%%
def count_a_b(alist):
    """ This function counts number of a's """
    cnt = 0
    for i in range(0,len(alist),1):
        if(alist[i] == 'a'):
            cnt += 1
    print("Number of a's are ",cnt)
    cnt = 0
    for let in alist:
        if let == 'b':
            cnt += 1
    print("Number of b's are ",cnt)
#%%
count_a_b(alphas)
#%%
def average(nlist):
    """ This function computes the average of the numbers """
    sum = 0
    for num in nlist:
        sum += num
    print("The computed average of list ",sum/(len(nlist)),end = "")
    print(".The count is ",len(nlist))
#%%
average(negList)
#%%
def print_list(alist):
    """ This function prints all elements in the list """
    for ele in alist :
        print(ele)
#%%
letter_list = ['a','b','c']
cap_list = ['A','B','C','D']
misc_list = ['ball',3.14,-78,"university",'f']
#%%
print_list(misc_list)
#%%





















