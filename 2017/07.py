#!/usr/bin/env python3
import sys

class Node:
  def __init__(self, name, weight, neighbors):
    self.name = name
    self.weight = weight
    if len(neighbors):
      self.neighbors = {neighbor: None for neighbor in neighbors}
    else:
      self.neighbors = {}


graph = {}
with open('07_input.txt', 'r') as input_data:
  for line in input_data:
    line = line.strip().split(' ')
    name = line[0]
    weight = int(line[1][1:-1])
    if len(line) > 2:
      edges = [tower.strip(',') for tower in line[3:]]
      graph[name] = Node(name, weight, edges)
    else:
      graph[name] = Node(name, weight, [])


# Part 1
start_node = None
for node_name in graph.keys():
  found = False
  for node2_name in graph.keys():
    if node_name in graph[node2_name].neighbors:
      found = True
      break
  if not found:
    start_node = node_name
    break
print('Answer part #1:', start_node)


def find_loner_weight_index(weights):
  wmap = {}
  for (i, weight) in enumerate(weights):
    if weight in wmap:
      wmap[weight].append(i)
    else:
      wmap[weight] = [i]
  
  for (weight, index_ls) in wmap.items():
    if len(index_ls) == 1:
      return index_ls[0]

  return -1 # something is wrong


# Part 2
def calc_weight_diff(graph, node_name):
  if node_name not in graph:
    print('ERROR: %s is not in graph' % (node_name))
    sys.exit(1)

  node = graph[node_name]
  if len(node.neighbors) == 0:
    return node.weight

  weights = []
  for neighbor in node.neighbors.keys():
    weight = calc_weight_diff(graph, neighbor)
    if weight == -1:
      return -1
    weights.append(weight)

  if weights.count(weights[0]) == len(weights):
    return weights[0] * len(weights) + node.weight
  else:
    loner_index = find_loner_weight_index(weights)
    if loner_index == -1:
      print('ERROR: more than on weight was different')
      sys.exit(1)
    diff = abs(weights[loner_index] - weights[(loner_index+1) % len(weights)])
    bad_node_name = list(node.neighbors.keys())[loner_index]
    bad_node = graph[bad_node_name]
    print('Answer:', bad_node.weight - diff)
    return -1 # solution found

calc_weight_diff(graph, start_node)
