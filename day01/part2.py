#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/1#part2

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

left_multiset = {}
right_multiset = {}

with open(filename, "r", encoding="utf-8") as f:
    for line in f.readlines():
        entries = line.split()
        if len(entries) != 2:
            continue
        left = int(entries[0])
        left_multiset[left] = left_multiset.get(left, 0) + 1
        right = int(entries[1])
        right_multiset[right] = right_multiset.get(right, 0) + 1

total_score = 0
for number, left_count in left_multiset.items():
    right_count = right_multiset.get(number, 0)
    score = number * left_count * right_count
    print(number, "Left:", left_count, "Right:", right_count, "Score:", score)
    total_score += score

print("Total:", total_score)

