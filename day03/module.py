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

def i(line):
    return int(line.strip())

def ss(line):
    return pw(line).split(' ')

addv = {'0': -1, '1': 1}
def p1():
    inp = get_input(pw)
    bits = collections.defaultdict(int)
    for sample in inp:
        for i, b in enumerate(sample):
            bits[i] += addv[b]
    e = int(''.join(['1' if x >0 else '0' for x in bits.values()]), 2)
    g = int(''.join(['0' if x >0 else '1' for x in bits.values()]), 2)
    print(g*e)
    return inp


def p2(segments):
    inp = get_input(pw)

    def getMCB(inp, pos):
        bits = 0
        for sample in inp:
            bits += addv[sample[pos]]
        return bits

    oxygen = copy.copy(inp)
    co2 = copy.copy(inp)

    for i in range(len(inp[0])):
        if len(oxygen) > 1:
            bit = getMCB(oxygen, i)
            oxygen = list(filter(lambda x: x[i] == ('1' if bit >= 0 else '0'), oxygen))
        if len(co2) > 1:
            bit = getMCB(co2, i)
            co2 = list(filter(lambda x: x[i] == ('1' if bit < 0 else '0'), co2))
    print(int(''.join(co2[0]), 2)*int(''.join(oxygen[0]), 2))
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


