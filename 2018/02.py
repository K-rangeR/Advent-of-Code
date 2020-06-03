#!/usr/bin/env python3
def count_occurences(cnt):
  two = 0
  three = 0
  for letter in cnt.keys():
    if cnt[letter] == 2:
      two += 1
    elif cnt[letter] == 3:
      three += 1

  if two >= 1 and three >= 1:
    return 5
  elif two >= 1:
    return 2
  elif three >= 1:
    return 3
  else:
    return 0


exactly_twice = 0
exactly_three = 0
with open('02_input.txt', 'r') as f:
  for box_id in f:
    box_id = box_id.strip()
    cnt = dict()
    for c in box_id:
      if c in cnt:
        cnt[c] += 1
      else:
        cnt[c] = 1
    res = count_occurences(cnt)
    if res == 5: # both
      exactly_twice += 1
      exactly_three += 1
    elif res == 2:
      exactly_twice += 1
    elif res == 3:
      exactly_three += 1
    
checksum = exactly_twice * exactly_three
print('Checksum:', checksum)
