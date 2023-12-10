# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:15:08 2022

@author: beama
"""

# Read in the file
with open('advent_day4.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('-', ',')

# Write the file out again
with open('advent_day4.txt', 'w') as file:
  file.write(filedata)
  
final_data = open("advent_day4.txt", "r")

data = final_data.read()

strat_list = data.splitlines()


all_list = []
for i in range(len(strat_list)):
    all_list = all_list + [[int(item) for item in strat_list[i].split(',') if item.isdigit()]]

def check_overlap(lista):
    count=0;
    for i in range(len(lista)):
        if lista[i][0]<= lista[i][2] <= lista[i][1] and lista[i][0]<= lista[i][3] <= lista[i][1]:
            print(lista[i][0],lista[i][1],lista[i][2],lista[i][3])
            count = count+1;
        elif lista[i][2]<= lista[i][0] <= lista[i][3] and lista[i][2]<= lista[i][1] <= lista[i][3]:
            #print(lista[i][0],lista[i][1],lista[i][2],lista[i][3])
            count=count+1;
    return count;

overlap_count = check_overlap(all_list)

#part two

def semi_check_overlap(lista):
    count=0;
    for i in range(len(lista)):
        if lista[i][0]<= lista[i][2] <= lista[i][1] or lista[i][0]<= lista[i][3] <= lista[i][1]:
            print(lista[i][0],lista[i][1],lista[i][2],lista[i][3])
            count = count+1;
        elif lista[i][2]<= lista[i][0] <= lista[i][3] or lista[i][2]<= lista[i][1] <= lista[i][3]:
            #print(lista[i][0],lista[i][1],lista[i][2],lista[i][3])
            count=count+1;
    return count;

parttwo_overlap = semi_check_overlap(all_list)