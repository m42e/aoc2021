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
    grid = {}
    for sample in inp[:20]:
        print(sample)
        onoff, sample = sample.split(' ')
        x,y,z = sample.split(',')
        xmin, xmax = map(int, x[2:].split('..'))
        ymin, ymax = map(int, y[2:].split('..'))
        zmin, zmax = map(int, z[2:].split('..'))

        on = onoff == 'on'


        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                for z in range(zmin, zmax+1):
                    grid[(x,y,z)] = on
    print(sum(map(lambda x: 1 if x else 0, grid.values())))
    return inp

BlockDimension = collections.namedtuple('BlockDimension', ['xmin', 'xmax', 'ymin', 'ymax', 'zmin', 'zmax'])
Block = collections.namedtuple('Block', ['dimensions', 'on'])


def get_intersection(block, blockdimension):
    inter_xmin = max(block.dimensions.xmin, blockdimension.xmin)
    inter_xmax = min(block.dimensions.xmax, blockdimension.xmax)
    inter_ymin = max(block.dimensions.ymin, blockdimension.ymin)
    inter_ymax = min(block.dimensions.ymax, blockdimension.ymax)
    inter_zmin = max(block.dimensions.zmin, blockdimension.zmin)
    inter_zmax = min(block.dimensions.zmax, blockdimension.zmax)
    return BlockDimension(inter_xmin, inter_xmax, inter_ymin, inter_ymax, inter_zmin, inter_zmax)

def valid_intersetction(blockdimension):
    return blockdimension.xmin <= blockdimension.xmax and blockdimension.ymin <= blockdimension.ymax and blockdimension.zmin <= blockdimension.zmax

def getblocksize(block):
    return getdimensionssize(block.dimensions)

def getdimensionssize(dimensions):
    return (dimensions.xmax+1 - dimensions.xmin)*(dimensions.ymax+1 - dimensions.ymin)*(dimensions.zmax+1-dimensions.zmin)

def p2():
    inp = get_input(pw)
    blocks = {}
    for i, sample in enumerate(inp):
        onoff, sample = sample.split(' ')
        x,y,z = sample.split(',')
        xmin, xmax = map(int, x[2:].split('..'))
        ymin, ymax = map(int, y[2:].split('..'))
        zmin, zmax = map(int, z[2:].split('..'))

        on = onoff == 'on'

        blocks[i] = Block(BlockDimension(xmin, xmax, ymin, ymax, zmin, zmax), on)

    cubes = collections.Counter()
    for i, block in blocks.items():
        update = collections.Counter()
        for bd, value in cubes.items():
            intersection = get_intersection(block, bd)
            if valid_intersetction(intersection):
                update[intersection] -= value
        if block.on:
            update[block.dimensions] += 1 if block.on else -1
        cubes.update(update)

    print(sum(getdimensionssize(bd) * value for bd, value in cubes.items()))
    return cubes



result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2()
    print(round(1000*(time.time() - start), 2), 'ms')


