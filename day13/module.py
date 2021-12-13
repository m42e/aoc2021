from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools

SPLITCHAR = ','

def pw(line):
    return line.strip()

def pwl(line):
    return line.strip().split(SPLITCHAR)

def pwi(line):
    return int(line.strip())

def pwli(line):
    return list(map(int, line.strip().split(SPLITCHAR)))

def inputpart2(line):
    return re.match("^$", line) is not None

Size = collections.namedtuple('Size', ['minx', 'maxx', 'miny', 'maxy'])

def getsize(grid):

    minx = min(map(lambda x: int(x[0]), grid.keys()))
    maxx = max(map(lambda x: int(x[0]), grid.keys()))
    miny = min(map(lambda x: int(x[1]), grid.keys()))
    maxy = max(map(lambda x: int(x[1]), grid.keys()))
    return Size(minx, maxx, miny, maxy)

def pg(grid, c='c', cc=0):
    size = getsize(grid)

    for y in range(size.miny, size.maxy+1):
        for x in range(size.minx, size.maxx+1):
            if (x,y) in grid:
                print('█', end='')
            else:
                print(' ', end='')
        if c == 'y':
            if y == cc:
                print()
                print('-------------')
            else:
                print()
        else:
            print()
    print(len(grid))



def p1():
    #inp, inp2 = get_input(pw, inputpart2, pwi)
    inp = get_input(pw, inputpart2)
    grid = {}
    for sample in inp[0]:
        sample = list(map(int, sample.split(',')))
        grid[(sample[0], sample[1])] = '#'
    #pg(grid)
    print(len(grid))
    for s in inp[1]:
        size = getsize(grid)
        s = s[11:]
        c = s[0]
        cc = int(s[2:])
        if c == 'x':
            for y in range(size.miny, size.maxy+1):
                for x in range(cc, size.maxx+1):
                    if (x,y) in grid:
                        grid[(size.maxx-x, y)] = '#'
                        del grid[(x,y)]
        if c == 'y':
            for y in range(cc, size.maxy+1):
                for x in range(size.minx, size.maxx+1):
                    if (x,y) in grid:
                        grid[(x, size.maxy-y)] = '#'
                        del grid[(x,y)]
        print(len(grid))
    pg(grid)
    return grid


def p2(grid):
    try:
        import numpy as np
        imgdata = []
        size = getsize(grid)
        imgdataplain = []
        for y in range(size.miny-10, size.maxy+10):
            imgdata.append([])
            imgdata.append([])
            for x in range(size.minx-10, size.maxx+10):
                if (x,y) in grid:
                    v = 255
                else:
                    v = 0
                imgdata[-2].append(v)
                imgdata[-2].append(v)
                imgdata[-1].append(v)
                imgdata[-1].append(v)
                imgdataplain.append(v)

        img = np.array(imgdata, np.uint8)
        import easyocr
        reader = easyocr.Reader(['en'])
        print('imported ocr')
        print(reader.readtext(img)[0][1])
    except:
        print('install easyocr, or read yourself')
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


