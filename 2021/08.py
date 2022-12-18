#!/usr/bin/env python3

# 1 4 7 8
unique_nums = [2, 7, 3, 4]

tt = 'tt' # top top
tl = 'tl' # top left
tr = 'tr' # top right
m  = 'm'  # middle
bl = 'bl' # bottom left
br = 'br' # bottom right
bb = 'bb' # bottom bottom

line_pos = [tt, tl, tr, m, bl, br, bb]

nums_to_labels = {
  9: [tt, tl, tr, m, br, bb],
  8: [tt, tl, tr, m, bl, br, bb],
  7: [tt, tr, br],
  6: [tt, tl, m, bl, br, bb],
  5: [tt, tl, m, br, bb],
  4: [tl, tr, m, br],
  3: [tt, tr, m, br, bb],
  2: [tt, tr, m, bl, bb],
  1: [tr, br],
  0: [tt, tl, tr, bl, br, bb],
}

def part1():
  with open('./08_input.txt', 'r') as file:
    answer = 0
    for line in file:
      line = line.strip().split()
      idx = line.index('|')
      output_vals = line[idx+1:]
      for val in output_vals:
        answer += 1 if len(val) in unique_nums else 0
    print(answer)

unique_nums_map = {
  3: 7,
  2: 1,
  4: 4,
  7: 8,
}

def part2():
  data = []
  with open('./08_test_2.txt', 'r') as file:
    for line in file:
      line = line.strip().split()
      idx = line.index('|')
      input_vals = line[0:idx]
      output_vals = line[idx+1:]
      data.append((input_vals, output_vals))

  answer = 0
  for d in data:
    answer += decode(d)

def decode(data):
  codes = {}
  input_pattern, output_pattern = data[0], data[0]

  # find what is know beforehand
  for pattern in input_pattern:
    pl = len(pattern)
    if pl in unique_nums_map:
      key = ''.join(sorted(pattern))
      codes[key] = unique_nums_map[pl]

  return 0

def does_not_have(line, nums):
  for num in nums.keys():
    if line not in nums_to_labels[num]:
      return num
  return -1

def calc_feq_tbl(nums):
  tbl = {}
  for pos in line_pos:
    n = 0.0
    for layout in nums.values():
      print(pos, layout, (pos in layout))
      n += 1 if pos in layout else 0
    tbl[pos] = n / len(nums)
  return tbl

#part1()
#part2()
print(calc_feq_tbl(nums_to_labels))
