#!/usr/bin/env python3

with open('./02_input.txt') as file:
  depth = 0
  horizontal = 0
  for line in file:
    data = line.strip().split(' ')
    movement, offset = data[0], int(data[1])
    if movement == 'forward':
      horizontal += offset
    elif movement == 'down':
      depth += offset
    elif movement == 'up':
      depth -= offset
  print(depth * horizontal)
