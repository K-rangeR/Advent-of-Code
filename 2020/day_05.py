#!/usr/bin/env python3

with open("./input_05.txt", "r") as f:
  ids = []
  max_id = -1
  for line in f:
    line = line.strip()
    r_search = line[:7]
    c_search = line[7:]

    min_seat, row, max_seat = 0, 0, 127
    for c in r_search:
      row = (min_seat + max_seat) // 2
      if c == "F":
        max_seat = row
      else:
        min_seat = row

    min_col, col, max_col = 0, 0, 7
    for c in c_search:
      col = (min_col + max_col) // 2
      if c == "R":
        min_col = col
      else:
        max_col = col

    id = max_seat * 8 + max_col
    ids.append(id)
    max_id = max(id, max_id)

print(max_id)

ids.sort()
for a,b in zip(ids, ids[1:]):
  if a != b-1:
    print(a+1)
    break
