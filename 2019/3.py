#!/usr/bin/env python3
import sys

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y


class Line:
  def __init__(self, p1, p2, horizontal):
    self.p1 = p1
    self.p2 = p2
    self.horizontal = horizontal

    
def get_taxicab_dist(p1, p2):
  return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def intersect(l1, l2):
  # parallel lines don't cross
  if l1.p1.x == l2.p1.x and l1.p2.x == l2.p2.x:
    return False
  
  if l1.p1.y == l2.p1.y and l1.p2.y == l2.p2.y:
    return False

  if l1.horizontal:
    max_x = max(l1.p1.x, l1.p2.x)
    min_x = min(l1.p1.x, l1.p2.x)
    mid_x = l2.p1.x

    max_y = max(l2.p1.y, l2.p2.y)
    min_y = min(l2.p1.y, l2.p2.y)
    mid_y = l1.p1.y
  else: # l2 is horizontal
    max_x = max(l2.p1.x, l2.p2.x)
    min_x = min(l2.p1.x, l2.p2.x)
    mid_x = l1.p1.x

    max_y = max(l1.p1.y, l1.p2.y)
    min_y = min(l1.p1.y, l1.p2.y)
    mid_y = l2.p1.y

  if (min_x <= mid_x <= max_x) and (min_y <= mid_y <= max_y):
    return Point(mid_x, mid_y)
  
  return False


def get_all_lines(wires, start):
  wire_lines = []
  prev_point = start
  for i in wires:
    d = i[0]
    l = int(i[1:])

    print(d, l)
    if d == 'L' or d == 'R':
      # change x
      print('change in x')
      x = (prev_point.x + l) if (d == 'R') else (prev_point.x - l)
      new_point = Point(x, prev_point.y)
    else:
      # change y
      print('change in y')
      y = (prev_point.y + l) if (d == 'U') else (prev_point.y - l)
      new_point = Point(prev_point.x, y)

    print('(', prev_point.x, prev_point.y, ')')
    print('(', new_point.x, new_point.y, ')')
    print('===========================')

    horizontal = True if (new_point.y == prev_point.y) else False
    new_line = Line(prev_point, new_point, horizontal=horizontal)
    prev_point = new_point

    wire_lines.append(new_line)

  return wire_lines

'''
wire_one = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
wire_two = ['U62','R66','U55','R34','D71','R55','D58','R83']

wire_one = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
wire_two = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

wire_one = ['R8', 'U5', 'L5', 'D3']
wire_two = ['U7', 'R6', 'D4', 'L4']
'''

with open('a.txt', 'r') as f:
  wire_one = f.readline().split(',')
  wire_two = f.readline().split(',')

start_point = Point(0, 0)
wire_one_lines = get_all_lines(wire_one, start_point)
wire_two_lines = get_all_lines(wire_two, start_point)

intersections = []
for line in wire_one_lines:
  for line2 in wire_two_lines:
    intersect_p = intersect(line, line2)
    if intersect_p and (intersect_p.x != 0 and intersect_p.y != 0):
      taxicab_dist = get_taxicab_dist(start_point, intersect_p)
      intersections.append(taxicab_dist)

print(min(intersections))
