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

def p1():
    inp = get_input(pw)
    binary = ''
    for sample in inp:
        x = int(sample, 16)
        binary += f'{x:04b}'
    packets = []
    def parse_packet(b, packets):
        x = 0
        version = b[x: x+3]
        typ = b[x+3: x+6]
        x += 6
        if typ == '100':
            number = ''
            stop = False
            while not stop:
                number += b[x+1: x+5]
                stop = b[x] != '1'
                x+=5
            packets.append((version, typ, [number]))
        else:
            #operator
            lengthtype = b[x]
            x+=1
            nl = 15 if lengthtype == '0' else 11
            length = b[x:x+nl]
            x+=nl
            l = int(length, 2)
            if lengthtype == '0':
                content = b[x: x + l]
                pos = x
                bp = b[pos:]
                sub = []
                while pos-x < l and any(filter(lambda x: x=='1', b[pos:])):
                    sp = parse_packet(b[pos:], sub)
                    pos += sp
                packets.append((version, typ, sub))
                x=pos
            else:
                pos = x
                sub = []
                for _ in range(l):
                    sp = parse_packet(b[pos:], sub)
                    pos += sp
                packets.append((version, typ, sub))
                x=pos


        return x
    x = 0
    while x < len(binary) and any(filter(lambda x: x=='1', binary[x:])):
        x += parse_packet(binary[x:], packets)

    def gv(packet):
        if isinstance(packet, list):
            return sum([gv(x) for x in packet])
        if isinstance(packet, tuple):
            return int(packet[0], 2) + gv(packet[2]) 
        return 0
    print(gv(packets))
    return packets


def p2(packets):
    def gp(packet):
        operators = {
            '000': lambda x, y: x+y,
            '001' : lambda x,y: x*y,
            '010' : lambda x,y: min(x,y),
            '011' : lambda x,y: max(x,y),
            '101' : lambda x,y: 1 if x>y else 0,
            '110' : lambda x,y: 1 if x<y else 0,
            '111' : lambda x,y: 1 if x==y else 0,
        }
        if isinstance(packet, tuple):
            if packet[1] == '100':
                return int(packet[2][0], 2)
            op = operators[packet[1]]
            return functools.reduce(op, [gp(x) for x in packet[2]])
        return int(packet, 2)
    print(gp(packets[0]))
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


