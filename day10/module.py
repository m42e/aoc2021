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

matches = {')':'(', '>':'<', '}':'{',  ']':'['}
cpoints = {')':3, '>':25137, ']':57, '}': 1197}
dpoints = {'(':1, '<':4, '[':2, '{': 3}
def p1():
    inp = get_input(pw)
    points = 0
    oks = []
    for sample in inp:
        stack = []
        currentpoints = 0
        for s in sample:
            if s in ['(', '<', '{', '[']:
                stack.append(s)
            else:
                if stack.pop() != matches[s]:
                    currentpoints += cpoints[s]
        if currentpoints != 0:
            oks.append(stack)
        points += currentpoints
    print(points)
    return oks


def p2(segments):
    total = []
    for s in segments:
        points = 0
        while len(s) > 0:
            points *= 5
            points += dpoints[s.pop()]
        total.append(points)
    total = sorted(total)
    print(len(total), total[int(len(total)/2)])
    return segments

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000*(time.time() - start), 2), 'ms')


