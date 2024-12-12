#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/2#part2

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"


def check_report(levels, dampen=True):
    directions = [a < b for a, b in zip(levels[:-1], levels[1:])]
    trend = True if directions.count(True) > len(levels) / 2 else False
    differences = [abs(a - b) for a, b in zip(levels[:-1], levels[1:])]
    safe_difference = [1 <= d <= 3 for d in differences]

    if False in safe_difference:
        if dampen:
            index = safe_difference.index(False)
            if check_report([*levels[:index], *levels[index + 1 :]], False):
                return True
            if check_report([*levels[: index + 1], *levels[index + 2 :]], False):
                return True
        return False
    if (not trend) in directions:
        if dampen:
            index = directions.index(not trend)
            if check_report([*levels[:index], *levels[index + 1 :]], False):
                return True
            if check_report([*levels[: index + 1], *levels[index + 2 :]], False):
                return True
        return False
    return True


safe_reports = 0
with open(filename, "r", encoding="utf-8") as f:
    for report in f.readlines():
        report = report.strip()
        if not report:
            continue
        levels = [int(x) for x in report.split()]
        if check_report(levels):
            safe_reports += 1
            print(report, "Safe")
        else:
            print(report, "Unsafe")

print("Safe Reports:", safe_reports)
