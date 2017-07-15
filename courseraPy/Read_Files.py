#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 01:32:19 2017

@author: anveshan
"""
#%%
def read_file(filename):
    """ This fucntion reads from file and prints"""
    infile = open(filename)
    
    for line in infile:
        print(line,end=" ")
    infile.close()

#%%
#read_file("Jhonny.txt")
read_file("/home/anveshan/python/Jhonny.txt")
#%%
def read_write_file(inputFile,outputFile):
    """ This function reads from one file and writes to another"""
    iFile = open(inputFile)
    oFile = open(outputFile,'w')
    
    for line in iFile:
        oFile.write(line)
    
    iFile.close()
    oFile.close()    
#%%
read_write_file("/home/anveshan/python/Jhonny.txt","/home/anveshan/python/Output.txt")
#%%
def copy_from_console_to_file(fileName):
    """Function reads from console and writes to file"""
    oFile = open(fileName,'w')
    while True:
        line = input("Enter the text.To stop, enter 'stop'")
        if line == "stop":
            break
        oFile.write(line+"\n")
        
    oFile.close()
    
    
#%%
copy_from_console_to_file("/home/anveshan/python/Output.txt")
#%%
    











