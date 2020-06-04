#!/usr/bin/env python3
from collections import defaultdict

def parse_line(line):
  args = line.strip().split()
  x, y = args[2].split(',')
  y = y[:-1]
  width, height = args[3].split('x')
  return (int(x), int(y), int(width), int(height))


def update_cells(x, y, width, height, cells):
  for i in range(width):
    for j in range(height):
      cells[(i+x, j+y)] += 1


cells = defaultdict(lambda: 0, defaultdict(int))
with open('03_input.txt', 'r') as data:
  for line in data:
    x, y, width, height = parse_line(line)
    update_cells(x, y, width, height, cells)

answer = 0
for count in cells.values():
  if count >= 2:
    answer += 1
print('Answer:', answer)
