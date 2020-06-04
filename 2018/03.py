#!/usr/bin/env python3
from collections import defaultdict

def parse_line(line):
  args = line.split()
  x, y = args[2].split(',')
  y = y[:-1]
  width, height = args[3].split('x')
  return (int(args[0][1:]), int(x), int(y), int(width), int(height))


def update_cells(x, y, width, height, cells):
  for i in range(width):
    for j in range(height):
      cells[(i+x, j+y)] += 1


cells = defaultdict(lambda: 0, defaultdict(int))
data = open('03_input.txt', 'r').read().strip().split('\n')

# Part 1
for line in data:
  _, x, y, width, height = parse_line(line)
  update_cells(x, y, width, height, cells)

answer = 0
for count in cells.values():
  if count >= 2:
    answer += 1
print('Part 1 answer:', answer)


# Part 2
for line in data:
  claim_id, x, y, width, height = parse_line(line)
  found = True
  for i in range(width):
    for j in range(height):
      if cells[(x+i, y+j)] > 1:
        found = False
  if found:
    print('Part 2 answer:', claim_id)
    break
