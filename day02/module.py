from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    a, b = line.split(" ")
    b = int(b)
    return (a, b)


movemap = {"forward": (1, 0), "backwards": (-1, 0), "down": (0, 1), "up": (0, -1)}


def add_tuples(a, b, bfactor=1):
    return (a[0] + b[0] * bfactor, a[1] + b[1] * bfactor)


def p1():
    inp = get_input(pw)
    pos = (0, 0)
    for a, b in inp:
        pos = add_tuples(pos, movemap[a], b)
    print(pos[0] * pos[1])
    return inp


def p2(segments):
    inp = get_input(pw)
    x, y = (0, 0)
    movement = (0, 0)
    for a, b in inp:
        movement = add_tuples((0, movement[1]), movemap[a], b)
        x += movement[0]
        y += movement[0] * movement[1]

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
