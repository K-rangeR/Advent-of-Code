#!/usr/bin/env python3
def differ_by_one(id1, id2):
  res = ''
  answer_found = False
  for (i, l1) in enumerate(id1):
    for (j, l2) in enumerate(id2):
      if id1[i] == id2[j] and i == j:
        res += id1[i] 
      elif id1[i] != id2[j] and i == j:
        answer_found = True
  return res if answer_found and len(res) == len(id1)-1 else ''


ids = open('02_input.txt', 'r').read().strip().split('\n')
for box_id in ids:
  for box_id2 in ids:
    if box_id == box_id2:
      continue
    res = differ_by_one(box_id, box_id2)
    if res:
      print('Answer:', res)
      break
