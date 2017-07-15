#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 17:07:55 2017

@author: anveshan
"""
#%%
import random
#%%
print(random.random())
print(random.randint(3,30))
#%%
import random

verbs=["goes","cooks","shoots","faints","chews","screams"]
nouns=["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","this","that"]

def sentence():
    article = random.choice(articles)
    noun = random.choice(nouns)
    adverb = random.choice(adverbs)
    verb = random.choice(verbs)
    
    our_sentence = article +" "+noun +" "+verb+" "+adverb+"."
    our_sentence = our_sentence.capitalize()
    
    print(our_sentence)
#%%
def poem():
    """ This is how we create poems"""
    ##for i in range(0,4,1):
    for i in range(4):
        sentence()
#%%
poem()
#%%