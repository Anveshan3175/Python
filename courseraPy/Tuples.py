#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 21:09:32 2017

@author: anveshan
"""

#%%List
## The list can be extended.
marksList = [20,34,56,43,67]
marksList.insert(5,97)
id(marksList)
marksList.append(55)
marksList.extend([78,25])
# Id remains same
id(marksList)
## The list can be modified
marksList[0]
marksList[0] = 28 # value at zero index is modified
##List is homogeneous
marksList[0] = "red"

#%% Tuples
a = 34,72,89
print(a)
x,y = 65,43
print(x,y)
r,s = 1,2,3 # this would give error in tuple creation


#%%
mixedTuple = ('df',77,89)
marksTuple = (34,67,89,46,90)
marksTuple[-2:]
#marksTuple[0] = 66 # this will not work.
id(marksTuple)
marksTuple += (66,)
id(marksTuple)

#%%

