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

matches = {')':'(', '>':'<', '}':'{',  ']':'['}
cpoints = {')':3, '>':25137, ']':57, '}': 1197}
dpoints = {'(':1, '<':4, '[':2, '{': 3}
closing = {d[1]:d[0] for d in matches.items()}
def p1():
    inp = get_input(pw)
    points = 0
    oks = []
    for sample in inp:
        stack = []
        currentpoints = 0
        for s in sample:
            if s in ['(', '<', '{', '[']:
                stack.append(s)
            else:
                if stack.pop() != matches[s]:
                    currentpoints += cpoints[s]
        if currentpoints != 0:
            oks.append(stack)
        points += currentpoints
    print(points)
    return oks


def p2(segments):
    total = []
    for s in segments:
        points = 0
        while len(s) > 0:
            points *= 5
            points += dpoints[s.pop()]
        total.append(points)
    total = sorted(total)
    print(len(total), total[int(len(total)/2)])
    return segments

def draw():
    from PIL import Image, ImageDraw, ImageFont
    colors = [  (255,165,0), (154,205,50), (0,128,0), (32,178,170), (0,255,255), (70,130,180), (0,0,205), (147,112,219), (255,0,255), (255,228,196), (210,105,30) ]
    images = []
    bg = (0,0,0)

    width = 1600
    height = 100
    dotwidth = width // 10

    font = ImageFont.truetype("NerdFonts/Hack Regular Nerd Font Complete Mono.ttf", 20)
    fontbold = ImageFont.truetype("NerdFonts/Hack Bold Nerd Font Complete Mono.ttf", 20)

    inp = get_input(pw)
    points = 0
    points2 = 0
    oks = []
    total = []
    posx = 0
    posy = 3
    currentstackdraw = 100
    DRAWLINE=4
    for sample in inp:
        currentstackdraw = 100
        posx = 0
        stack = []
        currentpoints = 0
        im = Image.new('RGB', (width, height), (0,0,0))
        draw = ImageDraw.Draw(im)
        for s in sample:
            im2 = im.copy()
            draw2 = ImageDraw.Draw(im2)
            highlight = False
            fnt = font
            if s in ['(', '<', '{', '[']:
                color = colors[len(stack)%len(colors)]
                stack.append((s, colors[len(stack)%len(colors)], posx))
                currentstackdraw -= DRAWLINE
            else:
                sp = stack.pop()
                if sp[0] != matches[s]:
                    color = (255, 0,0)
                    currentpoints += cpoints[s]
                    fnt = fontbold
                else:
                    color = sp[1]
                    highlight = sp
            draw.text((posx, posy), s, fill=color, anchor='lt', font=fnt)
            if highlight != False:
                draw.line(((sp[2], currentstackdraw), (posx + draw.textlength(s, font)-2, currentstackdraw)), fill=sp[1], width=2)
                currentstackdraw += DRAWLINE

            im2 = im.copy()
            draw2 = ImageDraw.Draw(im2)
            color2 = (0, 255, 0)
            if color == (255, 0,0):
                draw.line((posx, 30, posx, 130), fill=color, width=int(draw.textlength(s, font)))
                color2 = color
            draw2.text((posx, posy), s, fill=color2, anchor='lt', font=fontbold)
            if highlight != False:
                draw2.text((sp[2], posy), sp[0], fill=color2, anchor='lt', font=fontbold)
            images.append(im2)
            posx += draw.textlength(s, font)
        if currentpoints == 0:
            points2 = 0
            while len(stack) > 0:
                sp = stack.pop()
                points2 *= 5
                points2 += dpoints[sp[0]]
                s = closing[sp[0]]
                color = sp[1]

                draw.text((posx, posy), s, fill=color, anchor='lt', font=fontbold)
                draw.line(((sp[2], currentstackdraw), (posx + draw.textlength(s, font)-2, currentstackdraw)), fill=sp[1], width=2)
                currentstackdraw += DRAWLINE

                im2 = im.copy()
                draw2 = ImageDraw.Draw(im2)
                color2 = (0, 255, 0)
                draw2.text((posx, posy), s, fill=color2, anchor='lt', font=fontbold)
                draw2.text((sp[2], posy), sp[0], fill=color2, anchor='lt', font=fontbold)
                images.append(im2)
                posx += draw.textlength(s, font)
            images.append(images[-1].copy())
            images.append(images[-1].copy())
            images.append(images[-1].copy())
            im2 = im.copy()
            draw2 = ImageDraw.Draw(im2)
            draw2.text((posx + 20, posy), f'OK! {points2}', fill=(0, 255, 0), anchor='lt', font=fontbold)
            images.append(im2)
            total.append(points2)
        else:
            draw2.text((posx + 20, posy), f'Error! {currentpoints}', fill=( 255, 0, 0), anchor='lt', font=fontbold)
            images.append(im2)
        for i in range(20):
            images.append(images[-1].copy())



        points += currentpoints
    images[0].save('animation_2.gif',
           save_all=True, append_images=images[1:], optimize=False, duration=20, loop=1)
    print(points)
    total = sorted(total)
    print(total)
    print(len(total), total[len(total)//2])
    return oks

result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000*(time.time() - start), 2), 'ms')


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000*(time.time() - start), 2), 'ms')


draw()
