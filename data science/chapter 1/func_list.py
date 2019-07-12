#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:01:03 2018

@author: bkolev95
"""

def make_list(start, stop, step):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value = value + step
    return result

my_list = make_list(10, 100, 1)
print(my_list)