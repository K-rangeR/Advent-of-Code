#!/usr/bin/env python3
import collections

def most(col):
  c = {'0': 0, '1': 0}
  for n in col:
    c[n] += 1
  if c['0'] >= c['1']:
    return ('0', '1')
  else:
    return ('1', '0')


def build_col_array(contents):
  data = [[] for i in range(len(contents[0]))]
  for line in contents:
    i = 0
    for c in line:
      data[i].append(c)
      i += 1
  return data


def run_filter(contents, column, column_idx, rating_type):
  res = [row for row in contents]
  count = collections.Counter(column).most_common(2)
  large, small = count[0], count[1]
  same = large[1] == small[1]
  target = ''
  if rating_type == 'oxygen':
    target = large[0] if not same else '1'
  elif rating_type == 'co2':
    target = small[0] if not same else '0'
  res = list(filter(lambda row: row[column_idx] == target, res))
  return res


def two_helper(contents, columns, col_idx, rating_type):
  if len(contents) == 1:
    return contents
  
  filtered = run_filter(contents, columns[col_idx], col_idx, rating_type)
  contents = filtered
  columns = build_col_array(contents)
  return two_helper(contents, columns, col_idx+1, rating_type)


def two(contents, columns):
  ox = two_helper(contents, columns, 0, 'oxygen')[0]
  co2 = two_helper(contents, columns, 0, 'co2')[0]
  return int(''.join(ox), 2) * int(''.join(co2), 2)


with open('./03_input.txt') as file:
  contents = file.read().strip().split('\n')
  data = [[] for i in range(len(contents[0]))]
  for line in contents:
    i = 0
    for c in line:
      data[i].append(c)
      i += 1
  g = []
  e = []
  for col in data:
    (i, j) = most(col)
    g.append(i)
    e.append(j)
  print(int(''.join(g), 2) * int(''.join(e), 2))

  print(two(contents, data))
