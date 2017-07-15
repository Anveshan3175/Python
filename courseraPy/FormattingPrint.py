#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 06:20:44 2017

@author: anveshan
"""
#%%
nam1 = '"Teddy" Roosevelt'
nam2 = 'Theodore "Teddy" Roosevelt'
age = 60
wt = 199.1515115
#%%
out1 = "name: {0} age:{1} weight:{2}"
#%%
print("name: {0} age:{1} weight:{2}".format(nam1,age,wt))
print("name: {0} age:{1} weight:{2}".format(nam2,age,wt))
#%%
""" Right aligned, lower and upper limit for character spaces """
out2 = "name: {0:>26} age:{1:>4} weight:{2:>10}"
#%%
print("name: {0:>26} age:{1:>4} weight:{2:>10}".format(nam1,age,wt))
print("name: {0:>26} age:{1:>4} weight:{2:>10}".format(nam2,age,wt))

#%%
print("name: {0:<26} age:{1:<4} weight:{2:<10}".format(nam1,age,wt))
print("name: {0:<26} age:{1:<4} weight:{2:<10}".format(nam2,age,wt))
#%%
""" 5 decimal places, 2 of which are to the right"""
out3 = "name: {0:>26} age:{1:>4} weight:{2:>5.2f}"
#%%
print("name: {0:>26} age:{1:>4} weight:{2:>5.2f}".format(nam1,age,wt))
print("name: {0:>26} age:{1:>4} weight:{2:>5.2f}".format(nam2,age,wt))
#%%
print(out1.format(nam1,age,wt))
print(out2.format(nam1,age,wt))
print(out3.format(nam1,age,wt))
#%%
s = "my short string"
n = 5.1234
#%%
print("start||{0:25}||End".format(s))
print("start||{0:25}||End".format(n))
#%%
s = "hello, there"
out1 = "start||{}||End"
print(out1.format(s))
out1 = "start||{0}||End"
print(out1.format(s))
out1 = "start||{0:25}||End" #25 spaces
print(out1.format(s))
out1 = "start||{0:>25}||End" #25 spaces, right aligned
print(out1.format(s))
out1 = "start||{0:<25}||End" #25 spaces, left aligned
print(out1.format(s))
out1 = "start||{0:^25}||End" #25 spaces, centered
print(out1.format(s))
#%%


























