#!/usr/bin/env python3
import collections

test = [16,1,2,0,4,2,7,1,2,14]

def solve(crabs):
  to = max(crabs)
  curr_min = 10000000000000
  cache = {}
  for i in range(to):
    fuel = 0
    for c in crabs:
      n = abs(c - i)
      if n in cache:
        fuel += cache[n]
      else:
        s = sum([x for x in range(1, n+1)])
        cache[n] = s
        fuel += s
    curr_min = min(curr_min, fuel)
  print(curr_min)


with open('./07_input.txt', 'r') as file:
  crabs = list(map(int, file.read().strip().split(',')))
  solve(crabs)
