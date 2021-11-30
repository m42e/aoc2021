#!/bin/bash

day=$(date +'%-d')
day0=$(date +'%d')

# /usr/bin/open https://adventofcode.com/2020/day/$day/input

curl -b cookies.txt https://adventofcode.com/2020/
#curl -b cookies.txt https://adventofcode.com/2020/day/$day -o day$day0/index.html
