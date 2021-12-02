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


m = {"forward": (1, 0), "backwards": (-1, 0), "down": (0, 1), "up": (0, -1)}


def p1():
    inp = get_input(pw)
    x, y = (0, 0)
    for sample in inp:
        a, b = sample.split(" ")
        n = m[a]
        x += n[0] * int(b)
        y += n[1] * int(b)
    print(x * y)
    return inp


def p2(segments):
    inp = get_input(pw)
    x, y = (0, 0)
    aim = 0
    for sample in inp:
        a, b = sample.split(" ")
        n = m[a]
        tmp = n[0] * int(b)
        aim += n[1] * int(b)
        x += tmp
        y += tmp * aim

    print(x * y)
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
