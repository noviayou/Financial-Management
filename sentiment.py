#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:56:07 2018

@author: noviayou
"""

from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word, True) for word in words])

positive_vocab=["awesome","innovation","outstanding","fantastic","terrific","good","great"]
negative_vocab=["bad","terrible","useless","hate"]
netural_vocab=["Blockchain","is","was","know","technology"]

positive_features=[(word_feats(pos),"pos") for pos in positive_vocab]
negative_features=[(word_feats(neg),"neg") for neg in negative_vocab]
netural_features=[(word_feats(neu),"neu") for neu in netural_vocab]

train=positive_features+negative_features+netural_features



cl=NaiveBayesClassifier(train)



twi=r"/Users/noviayou/Downloads/twitter"
import json
day1=r"/Users/noviayou/Downloads/twitter/00.json"
text=json.loads(day1)
print (text)

