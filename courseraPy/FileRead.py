#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

fileName = sys.argv[1]

iFile = open(fileName)

for line in iFile:
    print(line,end=" ")
    
iFile.close()

# anveshan@anveshan-All-Series:~/python$ python FileRead.py Jhonny.txt