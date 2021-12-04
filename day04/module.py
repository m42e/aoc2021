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


class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.crossed = []

    def cross(self, i):
        if i in self.numbers:
            a = self.numbers.index(i)
            self.crossed.append(a)

    def check(self):
        for i in range(0, 5):
            if all([x in self.crossed for x in range(i, 25, 5)]):
                return True
        for i in range(0, 25, 5):
            if all([x in self.crossed for x in range(i, i + 5)]):
                return True
        return False

    def print(self):
        for i in range(0, 25, 5):
            for x in range(i, i + 5):
                if x in self.crossed:
                    print("\033[1m\033[31m", end="")
                print(f"{self.numbers[x]:02}", end=" ")
                if x in self.crossed:
                    print("\033[0m", end="")
            print()
        print()

    def sum(self):
        s = 0
        for i in range(len(self.numbers)):
            if i not in self.crossed:
                s += self.numbers[i]
        return s


def parse_bingo(inp):
    draw = list(map(int, inp[0].split(",")))
    inp = inp[2:]
    boards = []
    for board_start in range(0, len(inp), 6):
        boards.append(
            Board(
                [
                    int(x)
                    for y in inp[board_start : board_start + 5]
                    for x in filter(None, y.split(" "))
                ]
            )
        )

    return draw, boards


def p1():
    inp = get_input(pw)
    draw, boards = parse_bingo(inp)

    for d in draw:
        for board in boards:
            board.cross(d)
            if board.check():
                board.print()
                return board.sum() * d
    return 0


def p2(segments):
    inp = get_input(pw)
    draw, boards = parse_bingo(inp)

    for d in draw:
        for board in boards:
            board.cross(d)

        if len(boards) == 1 and boards[0].check():
            boards[0].print()
            return boards[0].sum() * d
        boards = [x for x in boards if not x.check()]

    return 0


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(result1)
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    r = p2(result1)
    print(r)
    print(round(1000 * (time.time() - start), 2), "ms")
