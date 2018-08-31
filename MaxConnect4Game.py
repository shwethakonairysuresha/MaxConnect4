#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import re

def drawaiagent(tabledraw=[]):
    def table(tabledraw):

        if tabledraw==0: return "0"
        if tabledraw==1: return "1"
        if tabledraw==2: return "2"

    p=5
    print "----------------- "
    while(p>-1):
        print "|",table(tabledraw[p][0]),table(tabledraw[p][1]),table(tabledraw[p][2]),table(tabledraw[p][3]),table(tabledraw[p][4]),table(tabledraw[p][5]),table(tabledraw[p][6]),"|"
        p=p-1
    print "----------------- "
    s = open("computer.txt", "w+")
    p=5
    while(p>-1):
        s.write(table(tabledraw[p][0]))
        s.write(table(tabledraw[p][1]))
        s.write(table(tabledraw[p][2]))
        s.write(table(tabledraw[p][3]))
        s.write(table(tabledraw[p][4]))
        s.write(table(tabledraw[p][5]))
        s.write(table(tabledraw[p][6]))
        s.write("\n")
        p=p-1
    s.write("2")

def drawhuman(tabledraw=[]):
    def table(tabledraw):
        if tabledraw==0: return "0"
        if tabledraw==1: return "1"
        if tabledraw==2: return "2"
    p=5
    print "----------------- "
    while(p>-1):
        print "|",table(tabledraw[p][0]),table(tabledraw[p][1]),table(tabledraw[p][2]),table(tabledraw[p][3]),table(tabledraw[p][4]),table(tabledraw[p][5]),table(tabledraw[p][6]),"|"
        p=p-1
    print "----------------- "
    s = open("human.txt", "w+")
    p=5
    while(p>-1):
        s.write(table(tabledraw[p][0]))
        s.write(table(tabledraw[p][1]))
        s.write(table(tabledraw[p][2]))
        s.write(table(tabledraw[p][3]))
        s.write(table(tabledraw[p][4]))
        s.write(table(tabledraw[p][5]))
        s.write(table(tabledraw[p][6]))
        s.write("\n")
        p=p-1
    s.write("1")

def win(state_of_board=[]):
    z1=[1,1,1,1]
    z2=[2,2,2,2]
    u=0
    v=0
    #checking horizontal values
    for x in range(6):
        for y in range(4):
            if [state_of_board[x][y],state_of_board[x][y+1],state_of_board[x][y+2],state_of_board[x][y+3]]==z1:
                u+=1
            if [state_of_board[x][y],state_of_board[x][y+1],state_of_board[x][y+2],state_of_board[x][y+3]]==z2:
                v+=1

    #checking vertical values
    for x in range(7):
        for y in range(3):
            if [state_of_board[y][x], state_of_board[y+1][x], state_of_board[y+2][x], state_of_board[y+3][x]]==z1:
                u+=1
            if [state_of_board[y][x], state_of_board[y+1][x], state_of_board[y+2][x], state_of_board[y+3][x]]==z2:
                v+=1

    #checking diagonal values left to right
    for y in range(3):
        for x in range(4):
            if [state_of_board[y][x], state_of_board[y+1][x+1], state_of_board[y+2][x+2], state_of_board[y+3][x+3]]==z1:
                u+=1
            if [state_of_board[y][x], state_of_board[y+1][x+1], state_of_board[y+2][x+2], state_of_board[y+3][x+3]]==z2:
                v+=1


    #checking diagonal values right to left
    for y in range(3):
        for x in range(6,2,-1):
            if [state_of_board[y][x], state_of_board[y+1][x-1], state_of_board[y+2][x-2], state_of_board[y+3][x-3]]==z1:
                u+=1
            if [state_of_board[y][x], state_of_board[y+1][x-1], state_of_board[y+2][x-2], state_of_board[y+3][x-3]]==z2:
                v+=1
    return u

def winhu(state_of_board=[]):
    z1=[1,1,1,1]
    z2=[2,2,2,2]
    u=0
    v=0
    #checking horizontal values
    for x in range(6):
        for y in range(4):
            if [state_of_board[x][y],state_of_board[x][y+1],state_of_board[x][y+2],state_of_board[x][y+3]]==z1:
                u+=1
            if [state_of_board[x][y],state_of_board[x][y+1],state_of_board[x][y+2],state_of_board[x][y+3]]==z2:
                v+=1

    #checking vertical values
    for x in range(7):
        for y in range(3):
            if [state_of_board[y][x], state_of_board[y+1][x], state_of_board[y+2][x], state_of_board[y+3][x]]==z1:
                u+=1
            if [state_of_board[y][x], state_of_board[y+1][x], state_of_board[y+2][x], state_of_board[y+3][x]]==z2:
                v+=1

    #checking diagonal values left to right
    for y in range(3):
        for x in range(4):
            if [state_of_board[y][x], state_of_board[y+1][x+1], state_of_board[y+2][x+2], state_of_board[y+3][x+3]]==z1:
                u+=1
            if [state_of_board[y][x], state_of_board[y+1][x+1], state_of_board[y+2][x+2], state_of_board[y+3][x+3]]==z2:
                v+=1


    #checking diagonal values right to left
    for y in range(3):
        for x in range(6,2,-1):
            if [state_of_board[y][x], state_of_board[y+1][x-1], state_of_board[y+2][x-2], state_of_board[y+3][x-3]]==z1:
                u+=1
            if [state_of_board[y][x], state_of_board[y+1][x-1], state_of_board[y+2][x-2], state_of_board[y+3][x-3]]==z2:
                v+=1
    return v

def ch(state_of_board=[]):
    cols=[]; rows=[]
    for col in range(7):
        for row in range(6):
            if state_of_board[row][col]==0:
                cols.append(col)
                rows.append(row)
                break
    return cols, rows
isNum=re.compile("[^0-9]")

def hmove(state_of_board, col):
    cols, rows = ch(state_of_board)
    if isNum.match(col)==None and col!='': col=int(col)-1
    while col not in cols:
        print "Invalid move: column is full!!"
        col=raw_input("Re-enter column no. to make your move:")
        if isNum.match(col)==None and col!='': col=int(col)-1
    state_of_board[rows[cols.index(col)]][col]=2
