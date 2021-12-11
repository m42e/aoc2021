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


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def pg(grid):
    for i in range(10):
        for j in range(10):
            if grid[(i, j)] > 9:
                print("\033[1mX\033[0m", end="")
            elif grid[(i, j)] == 0:
                print("\033[1m0\033[0m", end="")
            else:
                print(grid[(i, j)], end="")
        print()


def p1():
    inp = get_input(pw)
    grid = {}
    flashes = 0
    for i, sample in enumerate(inp):
        for j, s in enumerate(sample):
            grid[(i, j)] = int(s)
    for n in range(100):
        for i in range(10):
            for j in range(10):
                grid[(i, j)] += 1

        checkflash = list(reversed([(i, j) for j in range(10) for i in range(10)]))
        flashed = []

        while len(checkflash):
            i, j = checkflash.pop()
            if grid[(i, j)] >= 10 and (i, j) not in flashed:
                flashed.append((i, j))
                for d in dirs:
                    npos = (i + d[0], j + d[1])
                    if npos in grid and npos not in flashed:
                        grid[npos] += 1
                        checkflash.append(npos)
        for f in flashed:
            grid[f] = 0
            flashes += 1

        print(f"iteration {n}:")
        pg(grid)
        print()
    print(flashes)
    return inp


def p2(segments):
    inp = get_input(pw)
    grid = {}
    flashes = 0
    for i, sample in enumerate(inp):
        for j, s in enumerate(sample):
            grid[(i, j)] = int(s)
    flashed = []
    n = 0
    while len(flashed) != 100:
        n += 1
        for i in range(10):
            for j in range(10):
                grid[(i, j)] += 1
        checkflash = list(reversed([(i, j) for j in range(10) for i in range(10)]))
        flashed = []
        # print('----------')
        while len(checkflash):
            i, j = checkflash.pop()
            # print(i,j,'-------')
            # pg(grid)
            if grid[(i, j)] >= 10 and (i, j) not in flashed:
                flashed.append((i, j))
                for d in dirs:
                    if (i + d[0], j + d[1]) in grid and (
                        i + d[0],
                        j + d[1],
                    ) not in flashed:
                        grid[(i + d[0], j + d[1])] += 1
                        checkflash.append((i + d[0], j + d[1]))
                flashes += 1
                # pg(grid)
        for f in flashed:
            grid[f] = 0
        print(len(flashed))
    print(n)
    return inp


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
