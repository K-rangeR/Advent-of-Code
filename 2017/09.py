#!/usr/bin/env python3

data = open('09_input.txt', 'r').read().strip()

group_stack = ['{']
garbage_stack = []
score, i, garbage_chars = 1, 1, 0
while i < len(data):
  piece = data[i]
  if len(garbage_stack) == 0 and piece == '{':
    group_stack.append(piece)
    score += len(group_stack)
    i += 1
  elif len(garbage_stack) == 0 and piece == '}':
    group_stack.pop()
    i += 1
  elif len(garbage_stack) == 0 and piece == '<':
    garbage_stack.append(piece)
    i += 1
  elif piece == '>':
    garbage_stack.pop()
    i += 1 
  elif piece == '!':
    i += 2 
  else:
    if len(garbage_stack) != 0:
      garbage_chars += 1
    i += 1

print('Score:', score)
print('Garbage chars:', garbage_chars)
