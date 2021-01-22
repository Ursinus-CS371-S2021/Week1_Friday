#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:27:51 2021

@author: ctralie
"""

arr = [3, 7, 1, 4, 7, 2]

# The "Java way" of looping, with indices
for i in range(len(arr)):
    print(i, arr[i])

# The "pythonic way" of looping, with indices
# NOTE: Works on other collections like sets and maps
for i, x in enumerate(arr):
    print(i, x)


# Ex) Average every other element in arr
avg = 0
# Don't need indices:  General pattern: For element 
# in collection, do something with element
for x in arr[0::2]:
    print(x, end = ' ')
    avg += x
print("Avg = ", avg/len(arr[0::2]))