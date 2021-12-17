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

def pwl(line):
    return line.split(SPLITCHAR)


def pwi(line):
    return int(line)


def pwli(line):
    return list(map(int, line.split(SPLITCHAR)))


def inputpart2(line):
    return re.match("^$", line) is not None


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]

Size = collections.namedtuple("Size", ["minx", "maxx", "miny", "maxy"])

def getsize(grid):
    minx, miny = list(grid.keys())[0]
    maxx, maxy = list(grid.keys())[-1]
    return Size(minx, maxx, miny, maxy)

def pg(grid, path=[]):
    size = getsize(grid)
    for y in range(size.miny, size.maxy + 1):
        for x in range(size.minx, size.maxx + 1):
            if (x, y) in path:
                print("\033[1m", end="")
            print(grid[(x, y)], end="")
            if (x, y) in path:
                print("\033[0m", end="")
        print()
    print(len(grid))

def makegrid(inp):
    grid = {}
    for y, sample in enumerate(inp):
        for x, s in enumerate(sample):
            grid[(x, y)] = int(s)
    return grid

def p1():
    inp = get_input(pw)
    _, inp = inp.split(': ')
    xx, yy = inp.split(', ')
    inpx =  tuple(map(int,xx[2:].split('..')))
    inpy =  tuple(map(int,yy[2:].split('..')))
    print(inpx, inpy)

    def step(probe):
        def decreasex(x):
            if x == 0:
                return 0
            if x > 0:
                return x-1
            if x < 0:
                return x+1
        return (probe[0] + probe[2], probe[1] + probe[3], decreasex(probe[2]), probe[3]-1)
    hit = []
    for velx in range(0, inpx[1]+1):
        for vely in range(inpy[0], -inpy[0]):
            probe = (0, 0, velx, vely)
            cont = True
            maxy = inpy[0]
            while cont:
                probe = step(probe)
                cont = ((probe[0] < inpx[1] and (probe[2] > 0 or probe[0] > inpx[0])) and probe[1] > inpy[0])
                maxy = max(probe[1], maxy)
                if (probe[0] <= inpx[1] and probe[0] >= inpx[0]) and (probe[1] >= inpy[0] and probe[1] <= inpy[1]):
                    hit.append((velx, vely, maxy))
                    break

    print(max(map(lambda x: x[2], hit)))
    return hit


def p2(hit):
    print(len(set(map(lambda x: (x[0], x[1]), hit))))
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


