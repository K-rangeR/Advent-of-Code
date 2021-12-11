#!/usr/bin/env python3

def p(heightmap):
  for r in heightmap:
    for c in r:
      print(c, end='')
    print()

with open('09_input.txt', 'r') as file:
  heightmap = []
  for line in file:
    line = line.strip()
    line = '9' + line + '9'
    heightmap.append(line)
  all_max = len(heightmap[0]) * '9'
  heightmap.insert(0, all_max)
  heightmap.append(all_max)

  # part 1
  answer = 0
  height = len(heightmap) - 1
  width = len(heightmap[0]) - 1
  for r in range(1, height):
    for c in range(1, width):
      center = int(heightmap[r][c])
      surrounding = [
        heightmap[r-1][c], # up
        heightmap[r+1][c], # down
        heightmap[r][c-1], # left
        heightmap[r][c+1], # right
      ]
      surrounding = map(int, surrounding)
      answer += center+1 if center < min(surrounding) else 0
  print(answer)
