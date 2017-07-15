#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#anveshan@anveshan-All-Series:~/python$ python UpdateCSVFiles.py StudentMarks.csv StudEvaluation.csv
import csv
import sys

ipFileLoc = sys.argv[1]
opFileLoc = sys.argv[2]

# populating data
iFile = open(ipFileLoc,"w",newline="")
student= [["Anveshan",90],
          ["Shyam",45],
          ["Frank",23],
          ["sai",32]]

for row in student:
    csv.writer(iFile).writerow(row)

iFile.close()

# reading data and writing to new file
iFile = open(ipFileLoc)
oFile = open(opFileLoc,"w",newline="")

for row in csv.reader(iFile):
    passOrFail = "Pass"
    if int(row[1]) < 35:
        passOrFail = "Fail"
    writeRow = []
    writeRow.append(row[0])
    writeRow.append(row[1])
    writeRow.append(passOrFail)
    csv.writer(oFile).writerow(writeRow)
iFile.close()
oFile.close()






