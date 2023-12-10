# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:58:36 2022

@author: beama
"""

strat = open("advent_day3.txt", "r")

data = strat.read()

org_list = data.splitlines()

def halfs(string):
    h1,h2 = string[:len(string)//2], string[len(string)//2:]
    return [h1, h2]


def has_dupes(split_list):
    for i in range(len(split_list[0])):
        if split_list[1].count(split_list[0][i]) > 0:
            return True;
    return False;

def which_dupes(split_list):
    dupe = []
    for i in range(len(split_list[0])):
        if split_list[1].count(split_list[0][i]) > 0:
            if split_list[0][i] not in dupe:
                dupe = dupe + [split_list[0][i]];
    return dupe;


def all_d(lista):
    all_dupes = []
    for i in range(len(lista)):
        hs = halfs(lista[i]);
        if has_dupes(hs):
            all_dupes = all_dupes + which_dupes(hs);
    return all_dupes;

all_test = all_d(org_list)

import string
alphabet_lowercase = list(string.ascii_lowercase)

alpha_dict_lowercase = {letter:idx for idx, letter in enumerate(alphabet_lowercase, start=1)}

alphabet_uppercase = list(string.ascii_uppercase)

alpha_dict_uppercase = {letter:idx for idx, letter in enumerate(alphabet_uppercase, start=27)}

def count_priorities(lista):
    count=0
    for character in lista:
        if character.isupper():
            count = count + alpha_dict_uppercase[character];
        else:
            count = count + alpha_dict_lowercase[character];
    return count;

test_count=count_priorities(all_test)
            
# part two

#strings=[org_list[0],org_list[1],org_list[2]]

#common = set.intersection(*map(set,strings))

def badge(lista):
    all_common = []
    for i in range(0,len(lista),3):
        threestrings = [lista[i],lista[i+1],lista[i+2]]
        all_common = all_common + list(set.intersection(*map(set,threestrings)));
    return all_common;

test_badge = badge(org_list)

count_badge = count_priorities(test_badge)
