#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/11#part2

import functools
import math
import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

with open(filename, "r") as f:
    stones = [int(x.strip()) for x in f.read().split()]


@functools.cache
def count_stones(amount, level):
    if level == 0:
        return 1
    if amount == 0:
        return count_stones(1, level - 1)
    digits = int(math.log10(amount)) + 1
    if digits % 2 == 1:
        return count_stones(amount * 2024, level - 1)
    string = str(amount)
    left = int(string[: digits // 2])
    right = int(string[digits // 2 :])
    return count_stones(left, level - 1) + count_stones(right, level - 1)


total = 0
for stone in stones:
    total += count_stones(stone, 75)

print("Total:", total)
