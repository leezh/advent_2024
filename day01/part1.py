#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/1

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

left_list = []
right_list = []

with open(filename, "r", encoding="utf-8") as f:
    for line in f.readlines():
        entries = line.split()
        if len(entries) != 2:
            continue
        left_list.append(int(entries[0]))
        right_list.append(int(entries[1]))

left_list = sorted(left_list)
right_list = sorted(right_list)

total_distance = 0
for left, right in zip(left_list, right_list):
    distance = abs(left - right)
    print(left, "<--", distance, "-->", right)
    total_distance += distance

print("Total:", total_distance)

