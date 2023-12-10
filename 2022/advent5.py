# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:18:55 2022

@author: beama
"""

stack1=['Q','S','W','C','Z','V','F','T']
stack2=['Q','R','B']
stack3=['B','Z','T','Q','P','M','S']
stack4=['D','V','F','R','Q','H']
stack5=['J','G','L','D','B','S','T','P']
stack6=['W','R','T','Z']
stack7=['H','Q','M','N','S','F','R','J']
stack8=['R','N','F','H','W']
stack9=['J','Z','T','Q','P','R','B']

all_stacks = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]


with open('moves_only_vf.txt') as f:
    # Read space-delimited file and replace all empty spaces by commas
    data = f.read().replace('\t', ',')
    
move_list = data.splitlines()

all_move = []
for i in range(len(move_list)):
    all_move = all_move + [[int(item) for item in move_list[i].split(',') if item.isdigit()]]
    
small_move=[[3,8,2],[3,1,5],[2,7,4]]

#lista de moves é tipo [[3,8,2],[3,1,5],[2,7,4]], mexe 3 do 8 p o 2 e por ai adiante

def moving(lista_moves,listastacks):
    for i in range(len(lista_moves)):
        popped_list=[]
        for j in range(lista_moves[i][0]):
            popped = listastacks[lista_moves[i][1]-1].pop();
            popped_list = popped_list + [popped]
            #print(popped_list)
        #print(i)
        listastacks[lista_moves[i][2]-1] = listastacks[lista_moves[i][2]-1] + popped_list
    last_el_list=[]
    for m in range(len(listastacks)):
        last_el_list = last_el_list + [listastacks[m][-1]]
    return last_el_list;
    #return listastacks;

testing_stack = moving(all_move,all_stacks)

#part two

def moving2(lista_moves,listastacks):
    for i in range(len(lista_moves)):
        popped_list=[]
        for j in range(lista_moves[i][0]):
            popped = listastacks[lista_moves[i][1]-1].pop();
            popped_list = popped_list + [popped]
            #print(popped_list)
        #print(i)
        listastacks[lista_moves[i][2]-1] = listastacks[lista_moves[i][2]-1] + popped_list[::-1]
    last_el_list=[]
    for m in range(len(listastacks)):
        last_el_list = last_el_list + [listastacks[m][-1]]
    return last_el_list;
    #return listastacks;

