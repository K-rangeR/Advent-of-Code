#!/usr/bin/env python3
curr_freq = 0
computed_freqs = {}

freqs = open('01_input.txt', 'r').read().strip().split('\n')
i = 0
while True:
  curr_freq += int(freqs[i]) 
  if curr_freq in computed_freqs:
    print('Answer:', curr_freq)
    break
  else:
    computed_freqs[curr_freq] = 1
  i += 1
  if i >= len(freqs):
    i = 0
