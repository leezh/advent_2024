#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/9#part2

import dataclasses
import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"


@dataclasses.dataclass
class File:
    position: int
    size: int
    file_id: int | None = None

    def __repr__(self):
        return ("." if self.file_id is None else str(self.file_id)) * self.size


disk = []
position = 0
file_id = 0
is_block = True
with open(filename, "r") as f:
    for c in f.read():
        if not c.isdigit():
            continue
        size = int(c)
        if is_block:
            file = File(position, size, file_id)
            file_id += 1
        else:
            file = File(position, size)
        disk.append(file)
        position += size
        is_block = not is_block

index = 0
while index < len(disk):
    if disk[index].file_id is not None:
        index += 1
        continue
    space = disk[index]
    to_move = None
    for file in reversed(disk[index:]):
        if file.file_id is not None and file.size <= space.size:
            to_move = file
            disk.remove(file)
            break
    if to_move is None:
        index += 1
        continue
    to_move.position = space.position
    space.position += to_move.size
    space.size -= to_move.size
    disk.insert(index, to_move)
    index += 1

print("".join([repr(f) for f in disk]))

checksum = 0
for file in disk:
    if file.file_id is None:
        continue
    for p in range(file.position, file.position + file.size):
        checksum += p * file.file_id

print("Checksum:", checksum)
