#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 04:31:25 2017

@author: anveshan
"""
#%%
import csv
    
def read_csv(fileName):
    csvFile = open(fileName)
    for row in csv.reader(csvFile):# each row is read into list
        print(row)
    csvFile.close()
#%%
read_csv("phones.csv") 
#%%
def csv_read_file1(fileName):
    """ This function reads the rows and writes into list """
    csvfileReader = open(fileName)
    data = []
    for row in csv.reader(csvfileReader):
        data.append(row)
    print(data)
    csvfileReader.close()
#%%
csv_read_file1("phones.csv")
#%%
def csv_read_file2(fileName):
    csvFileReader = open(fileName)
    
    for row in csv.reader(csvFileReader):
        #for item in row:
            #print(item)
        print(row)
        print(row[0],row[1],row[2])
    csvFileReader.close()
#%%
csv_read_file2("BooksRead.csv")
#%%
import csv
import types

def write_csv(fileName):
    """ Write to csv """
    
    strList = [["name","place"],
               ["Anvesh","hyd"],
               ["Pavan","sec"]]
    if type(fileName) is str:
        fw = open(fileName,'w',newline = '')
        for item in strList:
            csv.writer(fw).writerow(item)
        fw.close()
    else:
        print("Input is not string")


#%%
write_csv("BooksRead.csv")
#%%
import types
import csv

def write_csv_keyboard(fileName):
    """ Takes input from keyboard and writes to file """
    details = []
    if type(fileName) is str:
        fw = open(fileName,'w',newline='')
        print("press enter to exit")
        while True:
            col1 = input("Enter person name: ")
            if col1 == "":
                break
            col2 = input("Enter person phone: ")
            if col2 == "":
                break
            col3 = input("Enter person city: ")
            if col3 == "":
                break
            col4 = input("Enter person profession: ")
            if col4 == "":
                break
            else:
                #row = [col1,col2,col3,col4]
                row = []
                row.append(col1)
                row.append(col2)
                row.append(col3)
                row.append(col4)
                print(row)
                csv.writer(fw).writerow(row)
        fw.close()
#%%
write_csv_keyboard("PersonDetails.csv")
#%%
import csv

def update_csv(oldFile,newFile):
    """ This function updates the files """
    oFile = open(oldFile)
    nFile = open(newFile,"w",newline="")
    
    for row in csv.reader(oFile):
        #nFile.write(row)
        csv.writer(nFile).writerow(row)
    oFile.close()
    nFile.close()
#%%
update_csv("PersonDetails.csv","PersonDetails_Mod.csv")
#%%




















