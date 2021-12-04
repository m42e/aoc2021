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
    return pw(line).split(" ")


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
        for i in [0, 5, 10, 15, 20]:
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


def p1():
    inp = get_input(pw)
    draw = list(map(int, inp[0].split(",")))
    inp = inp[1:]
    boards = []
    temp = []
    for sample in inp:
        if len(sample) == 0:
            boards.append(Board(copy.copy(temp)))
            temp = []
        else:
            for n in list(map(int, map(str.strip, filter(None, sample.split(" "))))):
                temp.append(n)
    boards.append(Board(copy.copy(temp)))

    for d in draw:
        for board in boards:
            board.cross(d)
            if board.check():
                board.print()
                print("components: ", board.sum(), d)
                print(board.sum() * d)
                return board.sum() * d
    return inp


def p2(segments):
    inp = get_input(pw)
    draw = list(map(int, inp[0].split(",")))
    inp = inp[2:]
    boards = []
    temp = []
    for sample in inp:
        if len(sample) == 0:
            boards.append(Board(copy.copy(temp)))
            temp = []
        else:
            for n in list(map(int, map(str.strip, filter(None, sample.split(" "))))):
                temp.append(n)
    boards.append(Board(copy.copy(temp)))

    for d in draw:
        s = 0
        for board in boards:
            board.cross(d)
            if board.check():
                s += 1

        if s == len(boards) - 1:
            for i, board in enumerate(boards):
                if board.check() == False:
                    last_winner = i
        if s == len(boards):
            board.print()
            print("winning board:", last_winner)
            print("components: ", boards[last_winner].sum(), d)
            print(boards[last_winner].sum() * d)
            return 0

    return inp


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
