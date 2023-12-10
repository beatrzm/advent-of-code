# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:09:04 2022

@author: beama
"""
import numpy as np

# =============================================================================
# with open('advent_day7_f.txt') as f:
#     # Read space-delimited file and replace all empty spaces by commas
#     data = f.read().replace('\t', ',')
# 
# tree_list = data.splitlines()
# 
# 
# trees = []
# for i in range(len(tree_list)):
#     trees = trees + [[int(item)
#                       for item in tree_list[i].split(',') if item.isdigit()]]
# 
# tree_matrix = np.array(trees)
# =============================================================================


# def visible_inside(nparray):
#    i=1
#    vis = 0
#    while i<len(nparray[1]-1):
#        j=1
#        while j<len(nparray[1]-1):
#            for w in range(j):
#                if nparray[i,j] < nparray[i,j-w]:



#def visible_inside2(nparray):
#    vis = 0
#    for i in range(len(nparray)):
#        min_line = np.amin(nparray[i]);
#        print(i)
#        print(min_line)
#        min_col = np.amin(nparray[:,np.argmin(nparray[i])]);
#        print(nparray[:,np.argmin(nparray[i])])
#        print(min_col)
#        if min_line < min_col:
#            vis = vis+1;
#    return vis;

# =============================================================================
# def visible_inside3(nparray):
#     vis=0;
#     i=1;
#     while i<len(nparray-1):
#         j=1;
#         while j<len(nparray[1]-1):
#             print(nparray[i,j],np.amax(np.delete(nparray[i,:],[i,j])),np.max(np.delete(nparray[:,j],[i,j])))
#             if nparray[i,j] >= np.amax(np.delete(nparray[i,:],[i,j])):
#                 vis = vis+1;
#             if nparray[i,j] > np.amax(np.delete(nparray[:,j],[i,j])):
#                 vis=vis+1;
#             j=j+1;
#         i=i+1;
#     return vis;
# =============================================================================

# =============================================================================
# def invisible_inside4(nparray):
#     vis=0;
#     i=1;
#     while i<len(nparray-1):
#         j=1;
#         while j<len(nparray[1]-1):
#             if nparray[i,j] >= nparray[i,j-1]:
#                 return invisible_inside4()
# 
# test_trees = np.array([[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]])
# =============================================================================

with open('advent_day7.txt', 'r') as file:
    trees = list(map(lambda x: list(map(lambda y: int(y), list(x))), file.read().split('\n')))

max_x = len(trees[0])-1
max_y = len(trees)-1

def adjacent_trees(lista,x,y): #devolve dicionario de todas as adjacentes
    return {'left': [lista[y][i] for i in range(0,x)],
            'right': [lista[y][i] for i in range(x+1,max_x+1)],
            'top': [lista[i][x] for i in range(0,y)],
            'bottom': [lista[i][x] for i in range(y+1,max_y+1)]
        }

test_adj = adjacent_trees(trees, 0, 4)
    

def visible_trees(lista):
    vis = (max_x*2)+(max_y*2)
    for y in range(1,max_y):
        for x in range(1,max_x):
            current = lista[y][x]
            adj_current = adjacent_trees(lista, x, y)
            
            if max(adj_current['left']) < current:
                vis = vis+1
            elif max(adj_current['right']) < current:
                vis=vis+1;
            elif max(adj_current['top']) < current:
                vis=vis+1;
            elif max(adj_current['bottom']) < current:
                vis=vis+1;
    return vis;

result = visible_trees(trees)
    
    