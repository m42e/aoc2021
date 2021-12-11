from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools
from PIL import Image, ImageDraw, ImageFont

def pw(line):
    return line.strip()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


images = []
bg = (0,0,0)

width = 200
dotwidth = width // 10

font = ImageFont.truetype("NerdFonts/Hack Bold Nerd Font Complete Mono.ttf", 24)

def pg(grid, imgonly=True, comment = None):
    im = Image.new('RGB', (width, width+70), (0,0,0))
    draw = ImageDraw.Draw(im)
    for i in range(10):
        for j in range(10):
            if grid[(i, j)] > 9:
                if not imgonly:
                    print("\033[1mX\033[0m", end="")
                fill = (255, 255, 255)
            elif grid[(i, j)] == 0:
                if not imgonly:
                    print("\033[1m0\033[0m", end="")
                fill = (120, 255, 120)
            else:
                if not imgonly:
                    print(grid[(i, j)], end="")
                fill = (int(255/10*grid[(i, j)]), 0, 0)
            draw.rectangle((i*dotwidth, j*dotwidth, (i+1)*dotwidth, (j+1)*dotwidth), fill=fill)
        if not imgonly:
            print()
    if comment is not None:
        draw.text((width/2, width+30), comment, fill=(255, 255,255), anchor='mt', font=font)
    images.append(im)



def p1():
    inp = get_input(pw)
    grid = {}
    flashes = 0
    for i, sample in enumerate(inp):
        for j, s in enumerate(sample):
            grid[(i, j)] = int(s)
    for n in range(100):
        for i in range(10):
            for j in range(10):
                grid[(i, j)] += 1

        checkflash = list(reversed([(i, j) for j in range(10) for i in range(10)]))
        flashed = []

        while len(checkflash):
            i, j = checkflash.pop()
            if grid[(i, j)] >= 10 and (i, j) not in flashed:
                flashed.append((i, j))
                for d in dirs:
                    npos = (i + d[0], j + d[1])
                    if npos in grid and npos not in flashed:
                        grid[npos] += 1
                        checkflash.append(npos)
        for f in flashed:
            grid[f] = 0
            flashes += 1

        print(f"iteration {n}:")
        pg(grid, False)
        print()
    print(flashes)
    return inp


def p2(segments):
    inp = get_input(pw)
    grid = {}
    flashes = 0
    for i, sample in enumerate(inp):
        for j, s in enumerate(sample):
            grid[(i, j)] = int(s)
    flashed = []
    n = 0
    while len(flashed) != 100:
        n += 1
        for i in range(10):
            for j in range(10):
                grid[(i, j)] += 1
        checkflash = list(reversed([(i, j) for j in range(10) for i in range(10)]))
        flashed = []
        # print('----------')
        pg(grid, comment=str(n))
        while len(checkflash):
            i, j = checkflash.pop()
            # print(i,j,'-------')
            if grid[(i, j)] >= 10 and (i, j) not in flashed:
                flashed.append((i, j))
                for d in dirs:
                    if (i + d[0], j + d[1]) in grid and (
                        i + d[0],
                        j + d[1],
                    ) not in flashed:
                        grid[(i + d[0], j + d[1])] += 1
                        checkflash.append((i + d[0], j + d[1]))
                flashes += 1
        pg(grid, comment=str(n))
        for f in flashed:
            grid[f] = 0
    print(n)
    return inp


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")
images[0].save('animation.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=300, loop=1)

images.clear()

if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")

images[0].save('animation_2.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=60, loop=1)
