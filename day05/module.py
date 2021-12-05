from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools

max_coords = (0, 0)
def lines(line, diags=False):
    global max_coords
    first, second = line.split(' -> ')
    seg = tuple(map(int, first.split(','))), tuple(map(int, second.split(',')))
    linepoints = []
    max_coords = max([max_coords[0], seg[0][0], seg[1][0]]), max([max_coords[1], seg[0][1], seg[1][1]])
    if seg[0][0] == seg[1][0] or seg[0][1] == seg[1][1] :
        y1 = min(seg[0][0], seg[1][0])
        y2 = max(seg[0][0], seg[1][0])
        x1 = min(seg[0][1], seg[1][1])
        x2 = max(seg[0][1], seg[1][1])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                linepoints.append((x,y))
    elif diags:
        y1 = seg[0][0]
        y2 = seg[1][0]
        x1 = seg[0][1]
        x2 = seg[1][1]
        for o in range(0, abs(y2-y1)+1):
            ox = o if (x2>x1)  else -o
            oy = o if (y2>y1)  else -o
            linepoints.append((x1+ox,y1+oy))
    return linepoints

def nodiags(line):
    return lines(line, False)

def withdiagonals(line):
    return lines(line, True)

mark= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

from drawille import Canvas

def draw(points):
    c = Canvas()
    for x in range(0,max_coords[0]):
        for y in range(0,max_coords[1]):
            if (x,y) in points:
                c.set(x,y)
    print(c.frame())

def count(lines):
    total = 0
    points = collections.defaultdict(int)
    for i, line in enumerate(lines):
        for p in line:
            points[p] +=1
    for p in points.values():
        if p > 1:
            total += 1

    return total, points

def p1():
    inp = get_input(nodiags)
    cnt = 0
    cnt, p = count(inp)
    print(cnt)
    return cnt


def p2(segments):
    inp = get_input(withdiagonals)
    cnt = 0
    cnt, p = count(inp)
    print(cnt)
    return cnt

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000*(time.time() - start), 2), 'ms')


