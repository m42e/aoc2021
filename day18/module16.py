from aoc.input import get_input
import copy
import itertools
import functools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    return line.strip()


def split(lst, index):
    return int(lst[:index],2), lst[index:]


def parse_packet(b, packets):
    version, b = split(b, 3)
    typ, b = split(b, 3)
    if typ == 4:
        number = 0
        stop = False
        while not stop:
            stop = b[0] != "1"
            n, b = split(b[1:], 4)
            number <<= 4
            number += n
        packets.append((version, typ, [number]))
    else:
        lengthtype, b = split(b, 1)
        nl = 15 - 4 * lengthtype
        l, b = split(b, nl)
        if lengthtype == 0:
            pl = len(b)
            sub = []
            while (pl - len(b)) < l:
                b = parse_packet(b, sub)
            packets.append((version, typ, sub))
        else:
            sub = []
            for _ in range(l):
                b = parse_packet(b, sub)
            packets.append((version, typ, sub))
    return b

def p1():
    inp = get_input(pw)
    binary = ""
    for sample in inp:
        x = int(sample, 16)
        binary += f"{x:04b}"

    packets = []
    parse_packet(binary, packets)

    def gv(packet):
        if isinstance(packet, tuple):
            return packet[0] + sum([gv(x) for x in packet[2]])
        return 0

    print(gv(packets[0]))
    return packets


def p2(packets):
    def gp(packet):
        operators = {
            0: lambda x, y: x + y,
            1: lambda x, y: x * y,
            2: lambda x, y: min(x, y),
            3: lambda x, y: max(x, y),
            5: lambda x, y: 1 if x > y else 0,
            6: lambda x, y: 1 if x < y else 0,
            7: lambda x, y: 1 if x == y else 0,
        }
        if packet[1] == 4:
            return packet[2][0]
        op = operators[packet[1]]
        return functools.reduce(op, [gp(x) for x in packet[2]])

    print(gp(packets[0]))
    return 0


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
