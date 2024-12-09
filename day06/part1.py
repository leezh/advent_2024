#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/6

import sys
import dataclasses


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

    def rotated(self):
        return Coord(-self.y, self.x)

    def in_bounds(self, rows, cols):
        return 0 <= self.x < cols and 0 <= self.y < rows


filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

obstacles = []
rows = 0
cols = 0
direction = Coord(0, -1)
position = Coord(0, 0)
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        cols = 0
        for c in line:
            coord = Coord(cols, rows)
            if c == "#":
                obstacles.append(coord)
            elif c == "^":
                position = coord
            cols += 1
        rows += 1

visited = {position}
while True:
    next_step = position + direction
    if not next_step.in_bounds(rows, cols):
        break
    if next_step in obstacles:
        direction = direction.rotated()
        continue
    position = next_step
    visited.add(position)

print("Steps:", len(visited))
