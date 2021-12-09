from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools

def pw(line):
    return line.strip()

def pwi(line):
    return int(line.strip())

def pwli(line):
    return list(map(int, line.strip()))

def p1():
    inp = get_input(pw)
    lowpoints = []
    coords = []
    for i, sample in enumerate(inp):
        for j, c in enumerate(sample):
            alllow = True
            if j != 0:
                alllow = alllow and (int(c) < int(inp[i][j-1]))
            if i != 0:
                alllow = alllow and (int(c) < int(inp[i-1][j]))
            if i+1 < len(inp):
                alllow = alllow and (int(c) < int(inp[i+1][j]))
            if j+1 < len(sample):
                alllow = alllow and (int(c) < int(inp[i][j+1]))
            if alllow:
                lowpoints.append(int(c)+1)
                coords.append((i, j))

    print(sum(lowpoints))
    return coords


def p2(coords):
    inp = get_input(pw)
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    walked = {}
    for c in coords:
        walked[c] = set([c])
        walklist = []
        def addwalk(loc):
            for d in dirs:
                if (loc[0] + d[0], loc[1] + d[1]) not in walked[c]:
                    walklist.append((loc[0] + d[0], loc[1] + d[1], int(inp[loc[0]][loc[1]])))

        addwalk(c)
        while len(walklist):
            i,j,v = walklist.pop()
            if i >= 0 and j>= 0 and i < len(inp) and j < len(inp[0]):
                if (int(inp[i][j]) < 9):
                    walked[c].add((i,j))
                    addwalk((i,j))

    mul=1
    for v in sorted(walked.items(), key=lambda x: len(x[1]))[-3:]:
        mul = mul * len(v[1])
    print(mul)


    return 0

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000*(time.time() - start), 2), 'ms')


