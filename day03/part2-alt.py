#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/3#part2
# Alternative that doesn't use regex

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample2.txt"

with open(filename, "r", encoding="utf-8") as f:
    code = f.read()

total = 0
for section in code.split("do()"):
    enabled_section = section.split("don't()", 1)[0]
    for mul in enabled_section.split("mul(")[1:]:
        mul = mul.split(")", 1)[0]
        parts = mul.split(",")
        if len(parts) != 2:
            continue
        if not (parts[0].isascii() and parts[0].isdecimal()):
            continue
        if not (parts[1].isascii() and parts[1].isdecimal()):
            continue
        total += int(parts[0]) * int(parts[1])

print("Total:", total)
