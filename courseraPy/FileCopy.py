#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

iFile = open(file1)
oFile = open(file2,'w')

for line in iFile:
    oFile.write(line)
    
iFile.close()
oFile.close()

# anveshan@anveshan-All-Series:~/python$ python FileCopy.py Jhonny.txt Output.txt
    
