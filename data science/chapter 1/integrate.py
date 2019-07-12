#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:00:32 2018

@author: bkolev95
"""
print("---------")
C = 20
dC = 5
while C <= 40:
    F = (9/5)*C + 32
    print("The temp in C is %.2f and in F: %.2f" % (C, F) )
    C += dC
print("---------")
    