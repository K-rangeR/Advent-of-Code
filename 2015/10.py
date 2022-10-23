#!/usr/bin/env python3

def custom_split(string):
  res = []
  tmp = [string[0]]
  for c in string[1:]:
    if c == tmp[0]:
      tmp.append(c)
    else:
      res.append(tmp)
      tmp = [c]
  res.append(tmp)
  return res


def look_and_say(string):
  return ''.join([str(len(token)) + str(token[0]) for token in custom_split(string)])


string = '3113322113'
for _ in range(40):
  string = look_and_say(string)
print(len(string))
