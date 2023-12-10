# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:36:21 2022

@author: beama
"""

strat = open("advent_day2.txt", "r")

data = strat.read()

strat_list = data.splitlines()

score_AY = 8 #win, player playes rock (A) i play paper (Y): 2 (for chosing paper) + 6 for win
score_AX = 4 #tie, rock vs rock: 1 for rock + 3 for tie
score_AZ = 3 #loss, 0 for loss + 3 for scissor 

score_BX = 1
score_BY = 5 #tie, paper vs paper: 2 for paper + 3 for tie
score_BZ = 9 #win, paper vs scisor: 3 for paper + 6 for win 

score_CX = 7 #win, scissor vs rock: 1 for rock + 6 for win
score_CY = 2 #loss, scissor vs paper: 2 for paper + 0 for loss
score_CZ = 6 

score_total = 0;
for i in strat_list:
    if i == 'A Y':
        score_total = score_total + score_AY;
    if i == 'A X':
        score_total = score_total + score_AX;
    if i == 'A Z':
        score_total = score_total + score_AZ;
    if i == 'B X':
        score_total = score_total + score_BX;
    if i == 'B Y':
        score_total = score_total + score_BY;
    if i == 'B Z':
        score_total = score_total + score_BZ;
    if i == 'C X':
        score_total = score_total + score_CX;
    if i == 'C Y':
        score_total = score_total + score_CY;
    if i == 'C Z':
        score_total = score_total + score_CZ;

# part two

score2_AY = 4 #need to tie to rock, chose rock. 1 for rock + 3 for tie
score2_AX = 3 #need to lose, need to chose scisor. 3 for chosing paper + 0 for loss
score2_AZ = 8 #need to win, chose paper. 2 for paper + 6 for win

score2_BX = 1 #need to lose to paper, chose rock. 1 for rock + 0 for loss
score2_BY = 5 #need to tie to paper, chose paper. 2 for paper + 3 for tie
score2_BZ = 9 #need to win to paper. chose scisor, 3 for scisor + 6 for win

score2_CX = 2 #need to lose to scisor, chose paper. 2 for paper + 0 for loss
score2_CY = 6 #need to tie to scisor, chose scisor. 3 for scisor + 3 for tie
score2_CZ = 7 #need to win to scisor, chose rock. 1 for rock + 6 for win

score_total2 = 0;
for i in strat_list:
    if i == 'A Y':
        score_total2 = score_total2 + score2_AY;
    if i == 'A X':
        score_total2 = score_total2 + score2_AX;
    if i == 'A Z':
        score_total2 = score_total2 + score2_AZ;
    if i == 'B X':
        score_total2 = score_total2 + score2_BX;
    if i == 'B Y':
        score_total2 = score_total2 + score2_BY;
    if i == 'B Z':
        score_total2 = score_total2 + score2_BZ;
    if i == 'C X':
        score_total2 = score_total2 + score2_CX;
    if i == 'C Y':
        score_total2 = score_total2 + score2_CY;
    if i == 'C Z':
        score_total2 = score_total2 + score2_CZ;