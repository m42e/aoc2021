import copy
import itertools
import time
import collections
import re
import functools

def pw(line):
    return line.strip()

def main():
    inp = open('data/data.txt', 'r').readlines()
    #inp = open('data/sample.txt', 'r').readlines()
    a = int(inp[0])
    s = []
    for i, sample in enumerate(inp[:-3]):
        s.append(int(inp[i]) + int(inp[i+1]) + int(inp[i+2]))
    cnt = 0
    for sample in s:
        b = int(sample)
        if (b > a):
            cnt = cnt + 1
        a = b
    print(cnt)


if __name__ == '__main__':
    main()
