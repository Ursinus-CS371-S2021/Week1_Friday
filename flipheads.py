#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:10:02 2021

@author: ctralie
"""

import random

heads_in_row = 0
num_flips = 0

while heads_in_row < 10:
    num_flips += 1
    if random.choice([0, 1]) == 1:
        heads_in_row += 1
    else:
        heads_in_row = 0
    num_flips += 1
print(num_flips)