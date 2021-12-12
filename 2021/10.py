#!/usr/bin/env python3

scores = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

more_scores = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}

open_ = ['(', '[', '{', '<']
close_ = [')', ']', '}', '>']


def part2(prog):
  all_scores = []
  for l in prog:
    stack = []
    for token in l:
      if token in open_:
        stack.append(token)
      elif token in close_:
        o = stack.pop()

    close_tokens = []
    for token in stack[::-1]:
      idx = open_.index(token)
      close_tokens.append(close_[idx])

    score = 0
    for token in close_tokens:
      score *= 5
      score += more_scores[token]

    all_scores.append(score)

  all_scores.sort()
  return all_scores[len(all_scores)//2]


with open('./10_input.txt', 'r') as file:
  prog = []
  for line in file:
    prog.append(line.strip())

  correct_prog = []

  # part 1
  total_score = 0
  for l in prog:
    err_found = False
    stack = []
    for token in l:
      if token in open_:
        stack.append(token)
      elif token in close_:
        o = stack.pop()
        idx = close_.index(token)
        if open_[idx] != o:
          total_score += scores[token]
          err_found = True
          break
    if not err_found:
      correct_prog.append(l)

  print(total_score)
  print(part2(correct_prog))
