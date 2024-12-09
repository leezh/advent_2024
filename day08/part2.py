#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/8#part2

import dataclasses
import itertools
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

    def __sub__(a, b):
        return Coord(a.x - b.x, a.y - b.y)

    def in_bounds(self, rows, cols):
        return 0 <= self.x < cols and 0 <= self.y < rows

    def as_rect(self, size):
        return pygame.Rect((self.x * size, self.y * size), (size, size))


rows = 0
cols = 0
antennas = {}
with open(filename, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        cols = 0
        for c in line:
            coord = Coord(cols, rows)
            if c.isalnum():
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append(coord)
            cols += 1
        rows += 1

antinodes = set()
for freq, coords in antennas.items():
    for a, b in itertools.combinations(coords, 2):
        antinodes.add(a)
        antinodes.add(b)
        antinode = a + (a - b)
        while antinode.in_bounds(rows, cols):
            antinodes.add(antinode)
            antinode += a - b
        antinode = b + (b - a)
        while antinode.in_bounds(rows, cols):
            antinodes.add(antinode)
            antinode += b - a

print(len(antinodes))
