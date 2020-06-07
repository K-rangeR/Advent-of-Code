#!/usr/bin/env python3
import math
from string import ascii_lowercase

def main():
  polymer = list(open('05_input.txt', 'r').read().strip())
  print('Answer part 1:', reacted_len(polymer))
  part_two(polymer)


def part_two(polymer):
  min_len = math.inf
  for c in ascii_lowercase:
    tmp_polymer = [unit for unit in polymer]
    tmp_polymer[:] = [unit for unit in tmp_polymer if unit != c and unit != c.upper()]
    min_len = min(min_len, reacted_len(tmp_polymer))
  print('Answer part 2:', min_len)


def reacted_len(polymer):
  stack = [polymer[0]] 
  for unit in polymer[1:]:
    if len(stack) == 0:
      stack.append(unit)
      continue
    top = stack[-1]
    if same_but_different_case(top, unit):
      stack.pop()
    else:
      stack.append(unit)
  return len(stack)

  
def same_but_different_case(a, b):
  if a.lower() == b.lower():
    ascii_code = abs(ord(a) - ord(b))
    return ascii_code == 32
  return False


if __name__ == '__main__':
  main()
