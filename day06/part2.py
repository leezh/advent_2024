#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/6#part2

import os
import sys
import dataclasses

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

CLEAR = "".join([" " * int(os.getenv("COLUMNS", "80")), "\r"])


@dataclasses.dataclass
class Coord:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __add__(a, b):
        return Coord(a.x + b.x, a.y + b.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def rotated(self):
        return Coord(-self.y, self.x)

    def in_bounds(self, rows, cols):
        return 0 <= self.x < cols and 0 <= self.y < rows


obstacles = set()
rows = 0
cols = 0
position = Coord(0, 0)
direction = Coord(0, -1)
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        cols = 0
        for c in line:
            coord = Coord(cols, rows)
            if c == "#":
                obstacles.add(coord)
            elif c == "^":
                position = coord
            cols += 1
        rows += 1


visited = {position}
new_obstacles = set()
while True:
    obstacle = position + direction
    if (
        obstacle.in_bounds(rows, cols)
        and obstacle not in obstacles
        and obstacle not in visited
    ):
        obstacles.add(obstacle)
        sub_position = position
        sub_direction = direction.rotated()
        xforms = {(sub_position, sub_direction)}
        while True:
            next_step = sub_position + sub_direction
            if not next_step.in_bounds(rows, cols):
                break
            if next_step in obstacles:
                sub_direction = sub_direction.rotated()
                continue
            sub_position = next_step
            xform = (sub_position, sub_direction)
            if xform in xforms:
                new_obstacles.add(obstacle)
                break
            xforms.add(xform)
        obstacles.discard(obstacle)

    next_step = position + direction
    if not next_step.in_bounds(rows, cols):
        break
    if next_step in obstacles:
        direction = direction.rotated()
        continue
    position = next_step
    visited.add(position)

print("Loops:", len(new_obstacles))
print("Steps:", len(visited))
