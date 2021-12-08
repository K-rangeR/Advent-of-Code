#!/usr/bin/env python3

test = [3,4,3,1,2]

def answer(fishes, sim_to=80):
  days = [0] * 9
  for fish in fishes:
    days[fish] += 1

  for day in range(sim_to):
    move = days[0]
    for i in range(1, 9):
      days[i-1] = days[i]
    days[6] += move
    days[8] = move

  print(sum(days))


with open('./06_input.txt', 'r') as file:
  one = list(map(int, file.read().strip().split(',')))
  two = [x for x in one]
  answer(one)
  answer(two, 256)
