#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/2

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

safe_reports = 0
with open(filename, "r", encoding="utf-8") as f:
    for report in f.readlines():
        report = report.strip()
        if not report:
            continue
        levels = [int(x) for x in report.split()]
        directions = [a < b for a, b  in zip(levels[:-1], levels[1:])]
        differences = [abs(a - b) for a, b  in zip(levels[:-1], levels[1:])]
        is_unsafe = False
        if len([d for d in differences if d < 1 or d > 3]) != 0:
            is_unsafe = True
        if directions.count(True) != 0 and directions.count(False) != 0:
            is_unsafe = True
        if not is_unsafe:
            safe_reports += 1
        print(report, "Unsafe" if is_unsafe else "Safe")

print("Safe Reports:", safe_reports)

