#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/3#part2

import re
import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample2.txt"

mul_regex = re.compile(r"do\(\)|don't\(\)|mul\(([0-9]+),([0-9]+)\)")


with open(filename, "r", encoding="utf-8") as f:
    code = f.read()

total = 0
enabled = True
for result in mul_regex.finditer(code):
    command = result.group(0).split("(", 1)[0]
    if command == "don't":
        enabled = False
    elif command == "do":
        enabled = True
    elif enabled:
        a = int(result.group(1))
        b = int(result.group(2))
        total += a * b

print("Total:", total)
