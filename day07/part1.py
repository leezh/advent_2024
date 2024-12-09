#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/7

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"


def test_sequence(result, parts):
    for i, x in reversed([*enumerate(parts)]):
        if i > 0 and result % x == 0:
            if test_sequence(result / x, parts[:i]):
                return True
        result -= x
    return result == 0


total = 0
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(":", 1)
        result = int(parts[0])
        parts = [int(x) for x in parts[1].split()]
        if test_sequence(result, parts):
            total += result

print("Total:", total)
