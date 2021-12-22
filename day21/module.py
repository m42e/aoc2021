from aoc.input import get_input
import copy
import itertools
import time
import collections
import functools
import re
from aoc.partselector import part_one, part_two
import functools
SPLITCHAR = ","

import sys
sys.setrecursionlimit(65000)

def pw(line):
    return line.strip()


def pwl(line):
    return line.split(SPLITCHAR)


def pwi(line):
    return int(line)


def pwli(line):
    return list(map(int, line.split(SPLITCHAR)))


def inputpart2(line):
    return re.match("^$", line) is not None

def die(i, p=False):
    if i > 100:
        i = 1
    v = i
    if p:
        print(i, end=',')
    i+=1
    if i > 100:
        i = 1
    v+= i
    if p:
        print(i, end=',')
    i+=1
    if i > 100:
        i = 1
    v+= i
    if p:
        print(i, end=' ')
    return v
def p1():
    inp = get_input(pw)
    players = [1, 3]
    playerpoints = [0, 0]
    i = 1
    ind = 0
    rolled = 0
    roll = 1
    def move(ind, roll):
        roll += players[ind%2]
        while roll > 10:
            roll -= 10
        playerpoints[ind] += roll
        return roll

    while playerpoints[0] < 1000  and playerpoints[1] < 1000:
        players[ind%2] = move(ind%2, die(roll))
        print(ind%2, '[',  die(roll, True), ']', playerpoints[ind%2], players[ind%2])
        ind += 1 
        i += 3
        roll +=3
        if (roll > 100):
            roll -= 100
    print(i)
    print(playerpoints)
    print((i-1) * (playerpoints[0] if playerpoints[1] > 1000 else playerpoints[1]))
    print(players[0]*players[1])
    return inp




def p2(segments):
    frequency = list(collections.Counter(map(sum, itertools.product([1,2,3], repeat=3))).items())
    print(frequency)

    universes = {(0, 1, 0, 3): 1}
    p0wins = 0
    p1wins = 0
    while universes:
        print(len(universes))
        nuv = collections.defaultdict(int)
        current = list(universes.items())
        for state, similar in current:
            score1, pos1, score2, pos2 = state
            for roll, count in frequency:
                p0 = pos1 + roll
                while(p0 > 10):
                    p0 -= 10
                s1 = score1 + p0
                if s1 >= 21:
                    p0wins += similar * count
                    continue
                for roll_p2, count_2 in frequency:
                    p1 = pos2 + roll_p2
                    while(p1 > 10):
                        p1 -= 10
                    s2 = score2 + p1
                    if s2 >= 21:
                        p1wins += similar * count * count_2
                        continue
                    nuv[(s1, p0, s2, p1)] += similar * count * count_2
        universes = nuv
    print(max(p0wins, p1wins))
    return max(p0wins, p1wins)

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000*(time.time() - start), 2), 'ms')


