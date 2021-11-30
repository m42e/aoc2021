#!/bin/bash

day=$(date +'%-d')
day0=$(date +'%d')
time=$(date +'%H')

# /usr/bin/open https://adventofcode.com/2021/day/$day/input

current_epoch=$(date +%s)
if [ $time -gt 6 ]; then
  day0=$(( $day0 + 1 ))
fi
if [ $day0 -gt 25 ]; then
  day0=01
fi
target_epoch=$(date -j "12${day0}06002021.00" +%s)

mkdir -p day$day0/data/
cp module.py day$day0/
touch day$day0/data/sample.txt

sleep_seconds=$(( $target_epoch - $current_epoch +1))
echo "Sleep for $sleep_seconds"
sleep $sleep_seconds

day=$(date +'%-d')
day0=$(date +'%d')
curl -b cookies.txt https://adventofcode.com/2021/day/$day/input -o day$day0/data/data.txt
curl -b cookies.txt https://adventofcode.com/2021/day/$day/ -o day$day0/index.html

cat day$day0/data/data.txt
