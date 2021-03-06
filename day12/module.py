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


def parse(inp):
    lines = collections.defaultdict(set)
    for sample in inp:
        fr, to = sample.split("-")
        lines[fr].add(to)
        lines[to].add(fr)
    return lines


def p1():
    inp = get_input(pw)
    lines = parse(inp)

    paths = set()
    visit = [("start",)]
    while len(visit) > 0:
        current = visit.pop()
        for x in lines[current[-1]]:
            ccount = current.count(x)
            if x == x.lower() and ccount > 0:
                continue
            if x in ["start", "end"] and current.count(x) >= 1:
                continue
            p = current + (x,)
            if x == "end":
                paths.add(p)
            else:
                visit.append(p)
    print(len(paths))
    return inp


def p2(segments):
    inp = get_input(pw)
    lines = parse(inp)

    paths = set()
    visit = [(("start",), False)]
    count = 0
    part1 = 0
    while len(visit) > 0:
        count += 1
        current, hasdoublevisit = visit.pop()
        for x in lines[current[-1]]:
            ccount = 0
            if x == x.lower():
                ccount = int(x in current)
                if ccount >= 2 or (ccount == 1 and (x == "start" or hasdoublevisit)):
                    continue
            p = current + (x,)
            if x == "end":
                paths.add(p)
            else:
                visit.append((p, ccount == 1 or hasdoublevisit))
    print(len(paths))
    print(f"tested {count} paths, {part1/1000.0}")
    return paths


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
