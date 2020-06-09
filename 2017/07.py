#!/usr/bin/env python3

class Node:
  def __init__(self, name, weight, neighbors):
    self.name = name
    self.weight = weight
    if len(neighbors):
      self.neighbors = {neighbor: None for neighbor in neighbors}
    else:
      self.neighbors = {}


graph = []
with open('07_input.txt', 'r') as input_data:
  for line in input_data:
    line = line.strip().split(' ')
    name = line[0]
    weight = int(line[1][1:-1])
    if len(line) > 2:
      edges = [tower.strip(',') for tower in line[3:]]
      graph.append(Node(name, weight, edges))
    else:
      graph.append(Node(name, weight, []))


# Part 1
for node in graph:
  found = False
  for node2 in graph:
    if node.name in node2.neighbors:
      found = True
      break
  if not found:
    print('Answer:', node.name)
    break
