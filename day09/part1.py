#!/usr/bin/env python3
#
# Entry for https://adventofcode.com/2024/day/9

import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "sample.txt"

disk = []
block_id = 0
is_block = True
with open(filename, "r") as f:
    for c in f.read():
        if not c.isdigit():
            continue
        size = int(c)
        if is_block:
            disk.extend([block_id] * size)
            block_id += 1
        else:
            disk.extend([None] * size)
        is_block = not is_block

blocks = [x for x in disk if x is not None]
compressed = []
rindex = len(blocks) - 1
for i, c in enumerate(disk[: len(blocks)]):
    if c is None:
        c = blocks[rindex]
        rindex -= 1
    compressed.append(c)

checksum = sum([index * block_id for index, block_id in enumerate(compressed)])
print("".join(["." if x is None else str(x) for x in disk]))
print("".join(["." if x is None else str(x) for x in compressed]))
print("Checksum:", checksum)
