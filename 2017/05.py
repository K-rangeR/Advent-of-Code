#!/usr/bin/env python3
data = open('05_input.txt', 'r').read().strip().split('\n')
data = [int(i) for i in data]

offset, steps = 0, 0
while offset < len(data):
  jump = data[offset]
  data[offset] += 1 if jump < 3 else -1
  offset += jump
  steps += 1

print('Answer:', steps)
