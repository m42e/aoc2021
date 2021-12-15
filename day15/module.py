from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools

SPLITCHAR = ","


def pw(line):
    return line


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
    # minx = min(map(lambda x: int(x[0]), grid.keys()))
    # maxx = max(map(lambda x: int(x[0]), grid.keys()))
    # miny = min(map(lambda x: int(x[1]), grid.keys()))
    # maxy = max(map(lambda x: int(x[1]), grid.keys()))
    return Size(minx, maxx, miny, maxy)


def pg(grid, path):
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


def p1():
    inp = get_input(pw)
    grid = {}
    for y, sample in enumerate(inp):
        for x, s in enumerate(sample):
            grid[(x, y)] = int(s)
    visit = [([(0, 0)], 0)]
    min_path = 99999
    _, maxx, _, maxy = getsize(grid)
    visited = {}
    while len(visit) > 0:
        path, leng = visit.pop()
        x, y = path[-1]
        for d in dirs:
            npos = (x + d[0], y + d[1])
            if npos not in grid:
                continue
            if npos in path:
                continue

            tleng = leng + grid[npos]

            if npos in visited:
                if visited[npos] <= tleng or tleng > min_path:
                    continue
            visited[npos] = tleng
            if npos == (maxx, maxy):
                min_path = min(min_path, tleng)
            else:
                visit.insert(0, ([npos], tleng))

    print(min_path)

    # print(min(list(map(lambda x: x[1], paths))))
    return inp


def p2(segments):
    inp = get_input(pw)
    grid = {}
    li = len(inp)
    ls = len(inp[0])
    for y, sample in enumerate(inp):
        for x, s in enumerate(sample):
            grid[(x, y)] = int(s)
            for xa in range(0, 5):
                for ya in range(0, 5):
                    v = int(inp[y][x])
                    v += xa + ya
                    while v > 9:
                        v -= 9
                    grid[(x + ls * xa, y + li * ya)] = v
    p2c(grid)


def p2c(grid):
    minx, maxx, miny, maxy = getsize(grid)
    visited = {
        (x, y): 100000000 for x in range(-1, maxx + 2) for y in range(-1, maxy + 2)
    }
    visited[(0, 0)] = 0
    rnd = 0
    changed = {(x, y): True for x in range(maxx + 1) for y in range(maxy + 1)}
    while any(changed) > 0:
        for pos in list(changed):
            x, y = pos
            themin = min([visited[(x + d[0], y + d[1])] for d in dirs]) + grid[pos]
            if themin < visited[pos]:
                visited[pos] = themin
            else:
                del changed[pos]
        print(rnd, len(changed))
        rnd += 1

    print(maxx, maxy, visited[(maxx, maxy)])
    # print(visited)


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
