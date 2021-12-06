from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools

def pw(line):
    return list(map(int, line.strip().split(',')))


def p1():
    inp = get_input(pw)
    last = 300
    for i in range(80):
        newinp = []
        for sample in inp:
            if sample == 0:
                newinp.append(6)
                newinp.append(8)
            else:
                sample = sample -1
                newinp.append(sample)
        inp = newinp
        print(len(inp), last - len(inp))
        last = len(inp)

    print(len(inp))
    return inp


def p2(segments):
    inp = get_input(pw)
    days = 256
    add = [0]*(days+10)
    current = len(inp)
    for c in inp:
        add[c-1] +=1
    print(current)

    for i in range(days-1):
        current += add[i]
        add[i+7] += add[i]
        add[i+9] += add[i]

    print(current)
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


