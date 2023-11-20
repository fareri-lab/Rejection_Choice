#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:48:35 2023

@author: jordansiegel
"""
import statistics

age = [30,34,31,35,23,20,30,34,32,36,25,29,32,18,23,32,28,26,36,31,25,27,23,
       20,29,29,26,31,30,22,19,32,32,22,22,21,34,32,25,23,30,33,25,28,21,23,
       19,32,26,34,24,27,30,30,32,30,22,28,26,26,23,23,34,23,27,25,32,30,32
       ,19,25,24,35,26,23,23,26,30,32,28,28,22,35,25]
len(age)

meanage = statistics.mean(age)
stddevage = statistics.stdev(age)
print(meanage)
print(stddevage)








