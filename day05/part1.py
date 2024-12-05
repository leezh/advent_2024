#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/5

import sys
import functools

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

ordering_pairs = {}


def insert_pair(a, b):
    ordering_pairs[(min(a, b), max(a, b))] = a < b


def sort_pair(a, b):
    ordering = ordering_pairs.get((min(a, b), max(a, b)))
    if ordering is None:
        return 1
    return 1 if ordering == (a > b) else -1


total = 0
page_section = False
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            page_section = True
            continue
        if not page_section:
            pairs = [int(x) for x in line.split("|", 1)]
            assert len(pairs) == 2
            insert_pair(*pairs)
            continue
        pages = [int(x) for x in line.split(",")]
        sorted_pages = sorted(pages, key=functools.cmp_to_key(sort_pair))
        if sorted_pages == pages:
            total += pages[int(len(pages) / 2)]

print("Total:", total)
