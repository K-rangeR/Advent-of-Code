#!/usr/bin/env python3

buffer_len = 1
curr_pos = 0
steps = 337
next_to_val = -1

for i in range(1, 50000001):
  next_pos = (curr_pos + steps) % buffer_len
  if next_pos == 0:
    next_to_val = i 
  curr_pos = next_pos+1
  buffer_len += 1

print('Part #2:', next_to_val)
