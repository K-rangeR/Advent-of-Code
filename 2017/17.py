#!/usr/bin/env python3

circular_buffer = [0]
curr_pos = 0
steps = 337

for i in range(1, 2018):
  next_pos = (curr_pos + steps) % len(circular_buffer)
  circular_buffer.insert(next_pos+1, i)
  curr_pos = next_pos+1

index_of_2017 = circular_buffer.index(2017)
adjacent_index = (index_of_2017 + 1) % len(circular_buffer)

print('Part #1:', circular_buffer[adjacent_index])
