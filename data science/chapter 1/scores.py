#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:57:59 2018

@author: bkolev95
"""
scores = []
# score of player no. 0:
scores.append([12, 16, 11, 12])
# score of player no. 1:
scores.append([9])
# score of player no. 2:
scores.append([6, 9, 11, 14, 17, 15, 14, 20])
print(scores)

for p in range(len(scores)):
    for g in range(len(scores[p])):
        score = scores[p][g]
        print('%4d' % (score))
    
