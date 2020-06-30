#!/usr/bin/env python3
from collections import defaultdict

# {state_name: {0: [val_to_write, dir, new_state], 1: [...]},}
test_input = {
  'a': {
    0: [1, 'r', 'b'],
    1: [0, 'l', 'b'],
  },
  'b': {
    0: [1, 'l', 'a'],
    1: [1, 'r', 'a'],
  }
}

real_input = {
  'a': {
    0: [1,'r','b'],
    1: [0,'l','c'],
  },
  'b': {
    0: [1,'l','a'],
    1: [1,'r','c'],
  },
  'c': {
    0: [1,'r','a'],
    1: [0,'l','d'],
  },
  'd': {
    0: [1,'l','e'],
    1: [1,'l','c'],
  },
  'e': {
    0: [1,'r','f'],
    1: [1,'r','a'],
  },
  'f': {
    0: [1,'r','a'],
    1: [1,'r','e'],
  },
}


def solve(states, steps):
  tape = defaultdict(lambda: 0, defaultdict(int))
  cursor = 0
  curr_state = 'a'

  for step in range(steps):
    operations = states[curr_state][tape[cursor]]
    tape[cursor] = operations[0]
    cursor += 1 if operations[1] == 'r' else -1
    curr_state = operations[2]
  
  return list(tape.values()).count(1)


print(solve(test_input, 6))
print(solve(real_input, 12261543))
