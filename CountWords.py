#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

fileName = sys.argv[1]
wordDict = {}
iFile = open(fileName)

for line in iFile:
    for word in line.lower().split():
        word = word.strip("'?,.;!/\"")
        if word not in wordDict:
            wordDict[word] = 0
        wordDict[word] = wordDict[word]+1
        
iFile.close()
word_list = sorted(wordDict)
for word in word_list:
    print(wordDict[word],word)
#print(wordDict)
key_list = wordDict.keys()
print("------------------")
for key in sorted(key_list):
    print(key,wordDict[key])
     

#anveshan@anveshan-All-Series:~/python$ python CountWords.py Jhonny.txt