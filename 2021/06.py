#!/usr/bin/env python3

DAYS = 80
test = [3,4,3,1,2]

def part1(fish):
  for day in range(DAYS):
    tmp = []  
    for (i, n) in enumerate(fish):
      if n == 0:
        tmp.append(8)
        fish[i] = 6
      else:
        fish[i] -= 1
    fish.extend(tmp)
  print(len(fish))

with open('./06_input.txt', 'r') as file:
  data = list(map(int, file.read().strip().split(',')))
  part1(data)
