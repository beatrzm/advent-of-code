# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:51:16 2022

@author: beama
"""

# opening the file in read mode
advent = open("advent_day1.txt", "r")

data = advent.read()

list_str = [l.split('\n') for l in data.split('\n\n') if l]

list_int = [[int(float(j)) for j in i] for i in list_str] 

sums=[]
for i in range(len(list_int)):
    sums=sums+[sum(list_int[i])]
    
max_cal = max(sums)

max_index=sums.index(max_cal)
three_max = [max_cal]
for i in range(2):
    sums.pop(max_index)
    new_max = max(sums)
    three_max = three_max + [new_max]
    max_index=sums.index(new_max)
    
sum_threemax = sum(three_max)
