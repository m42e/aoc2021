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


def prints(sample, explode = -1, split=-1):
    level = False
    exploded = False
    d=0
    for i, c in enumerate(sample):
        if c == '[':
            d+=1
        if i == explode-4:
            exploded = True
            print('\033[31m', end='')
        elif i == split:
            print('\033[32m', end='')
        elif d >= 5 and not exploded:
            level = True
            print('\033[34m', end='')
        if c == ']':
            d-=1
        print(c, end='')
        if i == explode or i == split or (level and d < 5):
            exploded = False
            level = False
            print('\033[0m', end='')
    print()

def p1():
    inp = get_input(pw)
    s = 0
    sample = list(inp[0])
    for cs in inp[1:]:
        sample = ['['] + sample + [',']  + list(cs) + [']']
        print(''.join(sample))
        print('===============================')
        depth = 0
        lastnumber = 0
        lastnumber_index = None
        lastexplode = None
        lastexplode_index = []
        action = True
        explode = 0
        last_action = ''
        last_actionpos = None
        while action:
            action = False
            i = 0
            depth = 0
            while i < len(sample):
                c = sample[i]
                if c == ']':
                    depth -= 1
                    if depth >= 4:
                        prints(sample, i, -1)
                        explode += 1
                        action = True
                        last_action = 'explode'
                        last_actionpos = i
                        first = int(sample[i-3])
                        second = int(sample[i-1])
                        for lastnumber_index in range(i-4, -2, -1):
                            if sample[lastnumber_index].isnumeric():
                                break
                        if lastnumber_index >= 0:
                            sample[lastnumber_index] = str(int(sample[lastnumber_index]) + first)
                        for nextnumber_index in range(i, len(sample)):
                            if sample[nextnumber_index].isnumeric():
                                break
                        else:
                            nextnumber_index = len(sample)
                        if nextnumber_index < len(sample) :
                            sample[nextnumber_index] = str(int(sample[nextnumber_index]) + second)
                        for _ in range(4):
                            del sample[i-4]
                        sample[i-4] = "0"
                        i = i-4

                if c == '[':
                    depth += 1
                i += 1
            i = 0
            while i < len(sample):
                c = sample[i]
                if len(c) > 1:
                    prints(sample, -1, i)
                    sample[i] = '['
                    a = int(c) // 2
                    b = (int(c)+1) // 2
                    sample.insert(i+1, str(a))
                    sample.insert(i+2, ',')
                    sample.insert(i+3, str(b))
                    sample.insert(i+4,']')
                    action = True
                    will_explode = False
                    for nextnumber_index in range(i, len(sample)):
                        if sample[nextnumber_index].isnumeric():
                            break
                    else:
                        nextnumber_index = len(sample)
                    d = 0
                    for c in sample[:nextnumber_index]:
                        if c == '[':
                            d+=1
                        if c == ']':
                            d-=1
                        if d > 4:
                            will_explode = True
                    if will_explode:
                        break
                i += 1

        print(''.join(sample))
        stack = []
        for c in sample:
            if c.isnumeric():
                stack.append(int(c))
                continue
            if c == ']':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*2 + b*3)
        print(stack[0])
        s += stack[0]
    print(s, sample)
    return inp


def p2(segments):
    inp = get_input(pw)
    s = 0
    sample = list(inp[0])
    m = 0
    for cs in itertools.combinations(inp, 2):
        sample = ['['] + list(cs[0]) + [',']  + list(cs[1]) + [']']
        print(''.join(sample))
        print('===============================')
        depth = 0
        lastnumber = 0
        lastnumber_index = None
        lastexplode = None
        lastexplode_index = []
        action = True
        explode = 0
        last_action = ''
        last_actionpos = None
        while action:
            action = False
            i = 0
            depth = 0
            while i < len(sample):
                c = sample[i]
                # print( ''.join(sample), i, c, depth,)
                # print(' '*(i),  end ='')
                # print('^')
                if c == ']':
                    depth -= 1
                    if depth >= 4:
                        prints(sample, i, -1)
                        explode += 1
                        action = True
                        last_action = 'explode'
                        last_actionpos = i
                        first = int(sample[i-3])
                        second = int(sample[i-1])
                        for lastnumber_index in range(i-4, -2, -1):
                            if sample[lastnumber_index].isnumeric():
                                break
                        if lastnumber_index >= 0:
                            sample[lastnumber_index] = str(int(sample[lastnumber_index]) + first)
                        for nextnumber_index in range(i, len(sample)):
                            if sample[nextnumber_index].isnumeric():
                                break
                        else:
                            nextnumber_index = len(sample)
                        if nextnumber_index < len(sample) :
                            sample[nextnumber_index] = str(int(sample[nextnumber_index]) + second)
                        for _ in range(4):
                            del sample[i-4]
                        sample[i-4] = "0"
                        i = i-4

                if c == '[':
                    depth += 1
                i += 1
            i = 0
            while i < len(sample):
                c = sample[i]
                if len(c) > 1:
                    prints(sample, -1,i)
                    sample[i] = '['
                    a = int(c) // 2
                    b = (int(c)+1) // 2
                    sample.insert(i+1, str(a))
                    sample.insert(i+2, ',')
                    sample.insert(i+3, str(b))
                    sample.insert(i+4,']')
                    action = True
                    will_explode = False
                    for nextnumber_index in range(i, len(sample)):
                        if sample[nextnumber_index].isnumeric():
                            break
                    else:
                        nextnumber_index = len(sample)
                    d = 0
                    for c in sample[:nextnumber_index]:
                        if c == '[':
                            d+=1
                        if c == ']':
                            d-=1
                        if d > 4:
                            will_explode = True
                    if will_explode:
                        break
                i += 1

        print(''.join(sample))
        stack = []
        for c in sample:
            if c.isnumeric():
                stack.append(int(c))
                continue
            if c == ']':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*2 + b*3)
        print(stack[0])
        s += stack[0]
        m = max(m, stack[0])
    print(m)
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


