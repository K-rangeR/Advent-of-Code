#!/usr/bin/env python3

def get_max_bank_index(banks):
  max_blocks, max_blocks_index = banks[0], 0
  for (i,blocks) in enumerate(banks[1:]):
    if blocks > max_blocks:
      max_blocks, max_blocks_index = blocks, i+1
  return max_blocks_index


def redistribute_blocks(banks, from_block):
  blocks, i = banks[from_block], (from_block+1 % len(banks))
  banks[from_block] = 0
  while blocks >= 1:
    banks[(i % len(banks))] += 1
    blocks -= 1
    i += 1


banks = open('06_input.txt', 'r').read().strip().split('\t')
banks = [int(i) for i in banks]
mem_states = {tuple(banks):0}
cycle = 0

while True:
  cycle += 1
  index = get_max_bank_index(banks)
  redistribute_blocks(banks, index)
  if tuple(banks) in mem_states:
    break
  else:
    mem_states[tuple(banks)] = cycle

print('Answer:', (cycle - mem_states[tuple(banks)]))
