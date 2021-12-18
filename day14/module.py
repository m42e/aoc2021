from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools

SPLITCHAR = ' -> '

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

def p1():
    return p2(10)


def p2(cnt):
    inp = get_input(pw, inputpart2, pwl)
    base = inp[0][0] + ' '
    rules = {}
    for sample in inp[1]:
        rules[sample[0]] = sample[1]

    patterns = collections.defaultdict(int)
    for p in range(0, len(base)-1):
        patterns[base[p:p+2]] += 1

    for _ in range(cnt):
        npatterns = collections.defaultdict(int)
        for pattern, pc in patterns.items():
            if pattern in rules:
                npatterns[pattern[0] + rules[pattern]] += pc
                npatterns[rules[pattern] + pattern[1]] += pc
            else:
                npatterns[pattern] += pc
        patterns = npatterns

    cnt = collections.defaultdict(int)
    for pattern, count in patterns.items():
        cnt[pattern[0]] += count

    s = sorted(cnt.items(), key=lambda x: x[1])
    print(s[-1][1] - s[0][1])
    return inp

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2(40)
    print(round(1000*(time.time() - start), 2), 'ms')


