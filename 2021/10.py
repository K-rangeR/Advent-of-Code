#!/usr/bin/env python3

scores = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

open_ = ['(', '[', '{', '<']
close_ = [')', ']', '}', '>']

with open('./10_input.txt', 'r') as file:
  prog = []
  for line in file:
    prog.append(line.strip())

  # part 1
  total_score = 0
  for l in prog:
    stack = []
    for token in l:
      if token in open_:
        stack.append(token)
      elif token in close_:
        o = stack.pop()
        idx = close_.index(token)
        if open_[idx] != o:
          total_score += scores[token]
          break
  print(total_score)
