#!/usr/bin/env python3
import functools
import operator

def p(heightmap):
  for r in heightmap:
    for c in r:
      print(c, end='')
    print()


def find_low_points(heightmap):
  low_points = [] # [(r, c, n), (r, c, n), ...]
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
      if center < min(surrounding):
        low_points.append((r, c, center))
  return low_points


def part_2(heightmap, low_points):
  res = []
  for point in low_points:
    res.append(part_2_recur(heightmap, point[0], point[1]))
  res.sort()
  return res[-3:]


def part_2_recur(heightmap, row, col):
  if heightmap[row][col] == '9' or heightmap[row][col] == 'X':
    return 0

  heightmap[row][col] = 'X'
  res = 1
  res += part_2_recur(heightmap, row-1, col) # up
  res += part_2_recur(heightmap, row+1, col) # down
  res += part_2_recur(heightmap, row, col+1) # right
  res += part_2_recur(heightmap, row, col-1) # left

  return res


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
  low_points = find_low_points(heightmap)
  for point in low_points:
    answer += point[2] + 1
  print(answer)

  # part 2
  heightmap = list(map(lambda row: list(row), heightmap))
  top_three = part_2(heightmap, low_points)
  answer = functools.reduce(operator.mul, top_three)
  print(answer)
