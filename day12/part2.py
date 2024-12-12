#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/12

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

    def rotated(self):
        return Coord(-self.y, self.x)


class Region:
    def __repr__(self):
        return f"({self.plant} {', '.join([repr(c) for c in self.plots])})"

    def __init__(self, plant, *coords):
        self.plant = plant
        self.plots = set(coords)


SIDES = [
    Coord(1, 0),
    Coord(0, 1),
    Coord(-1, 0),
    Coord(0, -1),
]


rows = 0
cols = 0
regions = []
with open(filename, "r") as f:
    last_row = []
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        cols = 0
        left_region = None
        next_row = []
        for plant in line:
            coord = Coord(rows, cols)
            if left_region and left_region.plant == plant:
                if (
                    last_row
                    and last_row[cols] != left_region
                    and last_row[cols].plant == plant
                ):
                    regions.remove(left_region)
                    last_row[cols].plots |= left_region.plots
                    for i, r in enumerate([*next_row]):
                        if r == left_region:
                            next_row[i] = last_row[cols]
                    left_region = last_row[cols]
                left_region.plots.add(coord)
                next_row.append(left_region)
            elif last_row and last_row[cols].plant == plant:
                left_region = last_row[cols]
                left_region.plots.add(coord)
                next_row.append(left_region)
            else:
                left_region = Region(plant, coord)
                regions.append(left_region)
                next_row.append(left_region)
            cols += 1
        last_row = next_row
        rows += 1

total = 0
for region in regions:
    edges = {side: set() for side in SIDES}
    for coord in region.plots:
        for side in SIDES:
            if coord + side not in region.plots:
                edges[side].add(coord)
    sides = 0
    for side, coords in edges.items():
        for coord in coords:
            if coord + side.rotated() not in coords:
                sides += 1
    total += sides * len(region.plots)
    print(region, "Sides:", sides)

print("Cost:", total)
