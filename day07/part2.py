#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/7#part2

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"


def test_sequence(result, parts):
    print(result, parts)
    num = parts[-1]
    if len(parts) == 1:
        return num == result
    if result % num == 0 and test_sequence(int(result / num), parts[:-1]):
        return True
    if result > num and test_sequence(result - num, parts[:-1]):
        return True

    str_result = str(result)
    str_num = str(num)
    if len(str_result) > len(str_num) and str_result.endswith(str_num):
        if test_sequence(int(str_result[: -len(str_num)]), parts[:-1]):
            return True
    return False


total = 0
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(":", 1)
        result = int(parts[0])
        parts = [int(x) for x in parts[1].split()]
        print(result)
        if test_sequence(result, parts):
            print("True")
            total += result
        print()

print("Total:", total)
