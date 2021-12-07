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
    msq = 0
    m = 9999999999999
    for x in range(0, 1000):
        s = 0
        for sample in inp:
            s+=abs(sample-msq)
        if s < m:
            print(msq, s)
            m = s
        msq+=1


    return inp


def p2(segments):
    inp = get_input(pw)
    msq = 0
    m = 9999999999999
    for x in range(0, 1000):
        s = 0
        for sample in inp:
            current = 0
            for i in range(0, abs(sample-msq)+1):
                current+=i
            s+= current


        if s < m:
            print(msq, s)
            m = s
        msq+=1
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


