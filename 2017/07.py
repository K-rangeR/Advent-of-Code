#!/usr/bin/env python3
graph = {}
with open('07_input.txt', 'r') as input_data:
  for line in input_data:
    line = line.strip().split(' ')
    if len(line) > 2:
      edges = [tower.strip(',') for tower in line[3:]]
      graph[line[0]] = {edge: None for (i, edge) in enumerate(edges)}
    else:
      graph[line[0]] = {}

for node in graph.keys():
  found = False
  for node2 in graph.keys():
    if node in graph[node2]:
      found = True
      break
  if not found:
    print('Answer:', node)
    break
