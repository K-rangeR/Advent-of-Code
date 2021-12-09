#!/usr/bin/env python3

# 1 4 7 8
unique_nums = [2, 7, 3, 4]

with open('./08_input.txt', 'r') as file:
  answer = 0
  for line in file:
    line = line.strip().split()
    idx = line.index('|')
    output_vals = line[idx+1:]
    for val in output_vals:
      answer += 1 if len(val) in unique_nums else 0
  print(answer)
