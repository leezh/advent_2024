#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/4

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

puzzle = {}
rows = 0
cols = 0
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        cols = 0
        for c in line:
            puzzle[cols, rows] = c
            cols += 1
        rows += 1


def get_item(x, y):
    return puzzle.get((x, y), ".")


def sample(x, y, dx, dy):
    result = []
    for i in range(4):
        result.append(get_item(x + dx * i, y + dy * i))
    return "".join(result)


directions = [
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, -1),
    (0, +1),
    (+1, -1),
    (+1, 0),
    (+1, +1),
]
total = 0
for x in range(cols):
    for y in range(rows):
        if puzzle[x, y] != "X":
            continue
        for d in directions:
            if sample(x, y, *d) == "XMAS":
                total += 1

print("Total:", total)
