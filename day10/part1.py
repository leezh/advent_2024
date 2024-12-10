#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/10

import dataclasses
import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"


@dataclasses.dataclass
class Coord:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(a, b):
        return Coord(a.x + b.x, a.y + b.y)

    def next_to(self, other):
        if -1 <= self.x - other.x <= 1 and self.y == other.y:
            return True
        if -1 <= self.y - other.y <= 1 and self.x == other.x:
            return True
        return False


SIDES = [
    Coord(1, 0),
    Coord(0, 1),
    Coord(-1, 0),
    Coord(0, -1),
]

rows = 0
cols = 0
elevations = {x: [] for x in range(10)}
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        cols = 0
        for c in line:
            elevations[int(c)].append(Coord(cols, rows))
            cols += 1
        rows += 1

total = 0
for peak in elevations[9]:
    coords = {peak}
    for i in reversed(range(9)):
        connections = set()
        for coord in coords:
            for side in SIDES:
                if coord + side in elevations[i]:
                    connections.add(coord + side)
        coords = connections
    total += len(coords)

print("Total:", total)
