from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools

def pw(line):
    return line.strip().split(' | ')

def pwli(line):
    return list(map(int, line.strip()))
def pwi(line):
    return int(line.strip())


def p1():
    inp = get_input(pw)
    d = collections.defaultdict(int)
    count = 0
    for sample in inp:
        s = sample[1]
        m = {'a': '', 'b': '', 'c': '', 'e': '', 'd': '', 'f': '', 'g': ''}
        counts = {7:0, 1:0, 8:0, 4:0}
        for n in sorted(s.split(' '), key=len):
            if len(n) == 2:
                m['c'] += n
                m['f'] += n
                count += 1
            if len(n) == 3:
                m['a'] += n
                m['c'] += n
                m['f'] += n
                count += 1
            if len(n) == 4:
                m['f'] += n
                m['b'] += n
                m['d'] += n
                m['c'] += n
                count += 1
            if len(n) == 7:
                m['a'] += n
                m['b'] += n
                m['c'] += n
                m['d'] += n
                m['e'] += n
                m['f'] += n
                m['g'] += n
                count += 1


    print(count)
    return inp


def diff(a, b):
    res = ''
    for c in a:
        if c in b:
            continue
        res += c
    for c in b:
        if c in a:
            continue
        res += c
    return res

def overlap(a, b):
    res = ''
    for c in a:
        if c in b:
            res += c
    return res

def p2():
    inp = get_input(pw)
    d = collections.defaultdict(int)
    count = 0
    for sample in inp:
        s = sample[0]
        m = {'a': '', 'b': '', 'c': '', 'e': '', 'd': '', 'f': '', 'g': ''}
        n = {4: '', 8: '', 1: '', 7: ''}
        counts = {7:0, 1:0, 8:0, 4:0}
        for c in sorted(s.split(' '), key=len):
            if len(c) == 2:
                n[1] = ''.join(sorted(c))
            if len(c) == 3:
                n[7] = ''.join(sorted(c))
            if len(c) == 4:
                n[4] = ''.join(sorted(c))
            if len(c) == 7:
                n[8] = ''.join(sorted(c))
        top = diff(n[7], n[1])
        middleleft = diff(n[4], n[1])
        print(n, top, middleleft, '#', sample[0], '|', sample[1])
        number = ''
        for x in sample[1].split(' '):
            x = ''.join(sorted(x))
            print(x, end=' ')
            if x in n.values():
                for h,i in n.items():
                    if i == x:
                        #print(h)
                        number += str(h)
                continue
            if len(x) == 5:
                is_three = overlap(x, sorted(n[1]))
                if len(is_three) == 2:
                    number += '3'
                else:
                    #print('2 or 5')
                    dd = diff(n[1], n[4])
                    is_five = overlap(x, dd)
                    if len(is_five) == 2:
                        #print('5')
                        number += '5'
                    else:
                        #print('2')
                        number += '2'
                continue
            if len(x) == 6:
                outer = False
                is_six = overlap(x, sorted(n[1]))
                print('---', x, is_six)
                if len(is_six) == 1:
                    number += '6'
                    continue
                else:
                    dd = diff(n[1], n[4])
                    is_nine = overlap(x, dd)
                    print('---', x, is_six, is_nine)
                    if len(is_nine) == 2:
                        number += '9'
                    else:
                        number += '0'
                    continue
            print()
        print(int(number))
        count += int(number)

    print(count)

    return 0

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2()
    print(round(1000*(time.time() - start), 2), 'ms')


