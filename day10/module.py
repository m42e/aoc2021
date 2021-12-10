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

def p1():
    inp = get_input(pw)
    stack = []
    points = 0 
    for sample in inp:
        for s in sample:
            if s in ['(', '<', '{', '[']:
                stack.append(s)
            else:
                c = stack.pop()
                if s == ')':
                    if c == '(':
                        continue
                    points+=3
                if s == '>':
                    if c == '<':
                        continue
                    points+=25137
                if s == ']':
                    if c == '[':
                        continue
                    points+=57
                if s == '}':
                    if c == '{':
                        continue
                    points+=1197

    print(points)
    return inp


def p2(segments):
    inp = get_input(pw)
    total = []
    inp = get_input(pw)
    points = 0
    for sample in inp:
        stack = []
        broken = False
        points = 0
        for s in sample:
            if s in ['(', '<', '{', '[']:
                stack.append(s)
            else:
                c = stack.pop()
                if s == ')':
                    if c == '(':
                        continue
                    broken = True
                    break
                if s == '>':
                    if c == '<':
                        continue
                    broken = True
                    break
                if s == ']':
                    if c == '[':
                        continue
                    broken = True
                    break
                if s == '}':
                    if c == '{':
                        continue
                    broken = True
                    break

        points = 0
        if not broken:
            while len(stack) > 0:
                points *= 5
                c = stack.pop()
                if c == '(':
                    points += 1
                if c == '[':
                    points += 2
                if c == '{':
                    points += 3
                if c == '<':
                    points += 4
            total.append(points)
    total = sorted(total)
    print(len(total), total[int(len(total)/2)])
    return inp

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000*(time.time() - start), 2), 'ms')


