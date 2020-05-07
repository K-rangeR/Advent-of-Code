#!/usr/bin/env python3
import json

def get_sum(item, jump_red=False):
  if isinstance(item, str):
    return 0

  if isinstance(item, int):
    return item

  if isinstance(item, dict):
    if jump_red and 'red' in item.values():
      return 0
    return sum([get_sum(obj, jump_red) for obj in item.values()])

  if isinstance(item, list):
    return sum([get_sum(obj, jump_red) for obj in item])


with open('12_input.txt') as i:
  json_obj = json.load(i)

answer = get_sum(json_obj, True)
print('Answer:', answer)
