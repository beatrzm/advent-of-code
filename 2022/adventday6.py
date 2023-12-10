# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:55:54 2022

@author: beama
"""

import numpy as np

day6 = open("advent_day6.txt", "r")

data = day6.read()

#quantos caracteres sao preciso p encontrar os primeiros 4 caracteres diferentes --> NAO!

#quantos caracteres sao precisos p encontrar os ultimos 4 caracteres diferentes
def four_dif_final(string):
    i=0;
    list_dif = [];
    for i in range(len(string)):
        list_dif = string[i:i+4]
        #print(list_dif)
        if len(set(list_dif))==4:
            return i+4;
        
        
#sol_teste = four_dif_final('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')  
        
sol = four_dif_final(data)

#part two

def fourteen_dif_final(string):
    i=0;
    list_dif = [];
    for i in range(len(string)):
        list_dif = string[i:i+14]
        #print(list_dif)
        if len(set(list_dif))==14:
            return i+14;

sol2 = fourteen_dif_final(data)
        