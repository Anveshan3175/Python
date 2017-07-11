#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

wordCnt = 0
lineCnt = 0
charCnt = 0


fileName = sys.argv[1]

iFile = open(fileName)

for line in iFile:
    lineCnt += 1
    for word in line.split():
        charCnt += len(word)
        wordCnt += 1
iFile.close()
print("Number of lines",lineCnt)
print("Number of words",wordCnt)
print("Number of chars",charCnt)
    


