#!/usr/bin/env python3
import sys


def main():
  with open('21_input.txt', 'r') as rules_file:
    lines = rules_file.read().strip().split('\n')

  rules = expand_rules(lines)
  art = to_pixel('.#./..#/###')
  for i in range(5):
    print('width:', len(art[0]), 'height:', len(art))
    size = len(art[0])
    d = (2 if size % 2 == 0 else 3)
    partitions = partition(art, d)
    art = apply_rules(partitions, rules, d)
    print()

  print('Answer:', light_on_count(art))


def expand_rules(lines):
  expanded_rules = {} 
  for line in lines:
    lhs, rhs = map(to_pixel, line.split('=>'))
    for r in range(4):
      expanded_rules[lhs] = rhs
      expanded_rules[flip(lhs)] = rhs
      lhs = rotate(lhs)
  return expanded_rules


def to_pixel(text):
  bits = {'.': 0, '#': 1}
  pixels = []
  for token in text.split('/'):
    pixels.append(tuple(bits[p] for p in token.strip()))
  return tuple(pixels)


def rotate(text):
  return tuple(zip(*reversed(text)))


def flip(text):
  return tuple(tuple(reversed(row)) for row in text)


def partition(art, d):
  res = []
  for outer_row in range(0, len(art), d):
    for inner_col in range(0, len(art[0]), d):
      tmp = [] 
      for inner_row in range(outer_row, outer_row+d):
        tmp.append(tuple(art[inner_row][inner_col:inner_col+d]))
      res.append(tuple(tmp))
  return tuple(res)


def apply_rules(partitions, rules, d):
  output = tuple(rules[partition] for partition in partitions)
  print('boxes:', len(partitions), 'box width:', len(partitions[0]), 'd:', d)
  boxes = max(1, len(partitions) // d)
  expand_map = {2:3, 3:4}
  new_art = []
  for rows in range(boxes):
    for i in range(expand_map[d]):
      tmp = []
      for j in range(boxes):
        tmp.extend(output[j][i])
      new_art.append(tuple(tmp))
  return tuple(new_art)


def light_on_count(art):
  count = 0
  for row in art:
    count += row.count(1) 
  return count


def print_art(art):
  for row in art:
    print(row)
  print()


if __name__ == '__main__':
  main()
