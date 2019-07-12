#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:29:20 2018

@author: bkolev95
"""

Fdegrees = [] # create a list of F temperatures
for degrees in range(0, 101, 10):
    Fdegrees.append(degrees)
    
Cdegrees = [] # create a list of C temps
for F in Fdegrees:
    C = (F - 32)*(5/9)
    Cdegrees.append(C)
    
Aprox = []
for F in Fdegrees:
    A = (F - 30)/2
    Aprox.append(A)
    
Nested = [Fdegrees, Cdegrees, Aprox]

for j in range(len(Nested)):
    print(Nested[j])
    #for f in j:
        #print(f)
    
for i in range(len(Fdegrees)): #index the F temps and C temps
    C = Cdegrees[i]
    F = Fdegrees[i]
    A = Aprox[i]

    
    print("%.1f %d %d" % (F, C, A))