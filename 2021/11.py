#!/usr/bin/env python3

def p(energy):
  for r in energy:
    for c in r:
      print(c, ' ', end='')
    print()


def read_input(file_name):
  res = []
  with open(file_name, 'r') as file:
    for line in file:
      line = line.strip()
      tokens = [int(t) for t in line]
      res.append(tokens)
  return res


def step(energy):
  cache = {}
  flash_points = {}
  flashes = 0
  for r in range(len(energy)):
    for c in range(len(energy[r])):
      energy[r][c] += 1
      if energy[r][c] >= 10:
        flash_points[(r,c)] = True

  for p in flash_points.keys():
    flash(energy, p[0], p[1], cache, False)

  # count 0
  for r in range(len(energy)):
    for c in range(len(energy[r])):
      if energy[r][c] == 0:
        flashes += 1

  return flashes 


def flash(energy, r, c, cache, inc):
  if r < 0 or r >= len(energy) or c < 0 or c >= len(energy[0]):
    return

  if (r,c) in cache:
    return

  if inc:
    energy[r][c] += 1
  
  if energy[r][c] >= 10:
    energy[r][c] = 0    # flash
    cache[(r,c)] = True # "visit"

    flash(energy, r-1, c-1, cache, True) # top left diagonal
    flash(energy, r-1, c, cache, True)   # top
    flash(energy, r-1, c+1, cache, True) # top right diagonal
    flash(energy, r, c-1, cache, True)   # left
    flash(energy, r, c+1, cache, True)   # right
    flash(energy, r+1, c-1, cache, True) # bottom left diagonal
    flash(energy, r+1, c, cache, True)   # bottom
    flash(energy, r+1, c+1, cache, True) # bottom right diagonal


def p1():
  energy = read_input('./11_input.txt')

  answer = 0
  for i in range(100):
    r = step(energy)
    answer += r
  print(answer)


def p2():
  energy = read_input('./11_input.txt')

  s = 1
  while True:
    flashes = step(energy)
    if flashes == 100:
      print(s)
      break
    s += 1


#p1()
p2()
