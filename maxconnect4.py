#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

from MaxConnect4Game import *
import sys

infile = sys.argv[2]

gametable = []
try:
    myfile = open(infile, 'r')
    d = []
    for ln in myfile:
        for char in ln:
            if char != "\n":
                print char
                d.append(int(char))

except IOError:
    sys.exit("\nError opening input file.\nCheck file name.\n")

ps = 0
gametable = [[d[ps], d[ps + 1], d[ps + 2], d[ps + 3], d[ps + 4], d[ps + 5], d[ps + 6]],
         [d[ps + 7], d[ps + 8], d[ps + 9], d[ps + 10], d[ps + 11], d[ps + 12], d[ps + 13]],
         [d[ps + 14], d[ps + 15], d[ps + 16], d[ps + 17], d[ps + 18], d[ps + 19], d[ps + 20]],
         [d[ps + 21], d[ps + 22], d[ps + 23], d[ps + 24], d[ps + 25], d[ps + 26], d[ps + 27]],
         [d[ps + 28], d[ps + 29], d[ps + 30], d[ps + 31], d[ps + 32], d[ps + 33], d[ps + 34]],
         [d[ps + 35], d[ps + 36], d[ps + 37], d[ps + 38], d[ps + 39], d[ps + 40], d[ps + 41]]]
gametable.reverse()

utset = []
utset = [[3, 4, 5, 7, 5, 4, 3],
              [4, 6, 8, 10, 8, 6, 4],
              [5, 8, 11, 13, 11, 8, 5],
              [5, 8, 11, 13, 11, 8, 5],
              [4, 6, 8, 10, 8, 6, 4],
              [3, 4, 5, 7, 5, 4, 3]]

def utfunc(board):
    u = 0
    sum = 0
    for x in range(0, 6):
        for y in range(0, 7):
            if board[x][y] == 1:
                sum += utset[x][y]
            elif board[x][y] == 2:
                sum -= utset[x][y]
    return u + sum

clnum = [2, 3, 1, 4, 0, 6, 5]

def ch(tbdata):
    global clnum
    col = []
    for x in clnum:
        for y in range(6):
            if tbdata[y][x] == 0:
                col.append([y, x])
                break
    return col

def play(tbdata, y, next):
    val = ch(tbdata)
    tbdata[val[y][0]][val[y][1]] = next

def minmax(tbdata, dif):
    def mainminmax(tbdata, dif, first, second):
        el = [];
        inf = -10000000
        for r, s in ch(tbdata):
            tbdata[r][s] = 1
            inf = max(inf, amin(tbdata, dif - 1, first, second))
            el.append(inf)
            tbdata[r][s] = 0
        if not el:
            drawaione(gametable)
            agen = win(gametable)
            human = winhu(gametable)
            if agen == human:
                print "Score: AI Agent =", agen, ", Player =", human
                print ""
            else:
                print "Score: AI Agent =", agen, ", Player =", human
                print ""
        else:
            infinity = max(el)
            index = el.index(infinity)
            return [index, infinity]

    def amax(tbdata, dif, first, second):
        col = ch(tbdata)
        if (dif == 0 or not col):
            return utfunc(tbdata)
        inf = -10000000
        for r, s in col:
            tbdata[r][s] = 1
            inf = max(inf, amin(tbdata, dif - 1, first, second))
            tbdata[r][s] = 0
            if inf >= second: return inf
            first = max(first, inf)
        return inf

    def amin(tbdata, dif, first, second):
        col = ch(tbdata)
        if (dif == 0 or not col):
            return utfunc(tbdata)
        inf = +10000000
        for r, s in col:
            tbdata[r][s] = 2
            inf = min(inf, amax(tbdata, dif - 1, first, second))
            tbdata[r][s] = 0
            if inf <= first: return inf
            second = min(second, inf)
        return inf
    return mainminmax(tbdata, dif, -10000000, +10000000)

def shmove(tbdata):
    global clnum
    dif = 1
    reach = minmax(tbdata, depp)
    try:
        return reach[0]
    except TypeError:
        sys.exit(1)

agent = 0
player = 0
mode_of_game = sys.argv[1]
first = sys.argv[3]
dep = sys.argv[4]
depp = int(dep)
if mode_of_game == 'one-move' or mode_of_game == 'interactive':
    print ""
else:
    print('%s is an unrecognized game mode' % mode_of_game)
    sys.exit(1)

def drawaione(tabledraw=[]):
    def tb(tabledraw):
        if tabledraw == 0: return "0"
        if tabledraw == 1: return "1"
        if tabledraw == 2: return "2"

    p = 5
    print "----------------- "
    while (p > -1):
        print "|", tb(tabledraw[p][0]), tb(tabledraw[p][1]), tb(tabledraw[p][2]), tb(tabledraw[p][3]), tb(tabledraw[p][4]), tb(tabledraw[p][5]), tb(tabledraw[p][6]), "|"
        p = p - 1
    print "----------------- "
    s = open(first, "w+")
    p = 5
    while (p > -1):
        s.write(tb(tabledraw[p][0]))
        s.write(tb(tabledraw[p][1]))
        s.write(tb(tabledraw[p][2]))
        s.write(tb(tabledraw[p][3]))
        s.write(tb(tabledraw[p][4]))
        s.write(tb(tabledraw[p][5]))
        s.write(tb(tabledraw[p][6]))
        s.write("\n")
        p = p - 1
    s.write("2")

if mode_of_game == 'one-move':
    print "Player 1 = Disc 1 , Opponent = Disc 2"
    print ""
    print "Current board state:"
    drawaione(gametable)
    if d[42] == 1:
        print "Player 1's move:"
        play(gametable, shmove(gametable), 1)
    if d[42] == 2:
        print "Not making a move as it is opponent player's turn:"
    drawaione(gametable)

if mode_of_game == 'interactive':
    if first == 'human-next' or first == 'computer-next':
        print ""
    else:
        print('%s is an unrecognized first player name' % first)
        sys.exit(1)
    if first == 'human-next':
        print "AI Agent = Disc 1 , Human Player = Disc 2"
        print ""
        print "Current board state:"
        drawhuman(gametable)
        while ch(gametable):
            agen = win(gametable)
            human = winhu(gametable)
            if agen == human:
                print "Score: AI Agent =", agen, ", Player =", human
            else:
                print "Score: AI Agent =", agen, ", Player =", human
            m = raw_input("Enter column no. to make your move: ")
            hmove(gametable, m)
            drawhuman(gametable)
            play(gametable, shmove(gametable), 1)
            print "AI Agent's Move:"
            drawaiagent(gametable)
    else:
        print "AI Agent = Disc 1 , Human Player = Disc 2"
        print ""
        print "Current board state:"
        while ch(gametable):
            drawaiagent(gametable)
            play(gametable, shmove(gametable), 1)
            print "AI Agent's Move:"
            drawaiagent(gametable)
            agen = win(gametable)
            human = winhu(gametable)
            if agen == human:
                print "Score: AI Agent =", agen, ", Player =", human
            else:
                print "Score: AI Agent =", agen, ", Player =", human
            m = raw_input("Enter column no. to make your move: ")
            print "Player's move:"
            hmove(gametable, m)
            drawhuman(gametable)

agen = win(gametable)
human = winhu(gametable)
if agen == human:
    print "Score: AI Agent =", agen, ", Player =", human
else:
    print "Score: AI Agent =", agen, ", Player =", human
