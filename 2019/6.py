#!/usr/bin/env python3
from enum import Enum
import sys


class Node:
  def __init__(self, name, parent_name, level):
    self.name = name
    self.parent_name = parent_name
    self.visited = False
    self.level = level


def read_graph(graph_file):
  global incoming_edges
  graph = dict()
  with open(graph_file, 'r') as f:
    for line in f:
      line = line.rstrip().split(')')
      key, value = line[0], line[1]
      node = Node(value, key, -1)
      if key in graph:
        graph[key].append(node)
      else:
        graph[key] = [node]

      if value not in graph:  
        graph[value] = []
  return graph


def fill_in_levels(graph):
  fill_in_levels_recur(graph, graph['COM'], 1)


def fill_in_levels_recur(graph, nodes, level):
  if len(nodes) == 0:
    return

  for node in nodes:
    fill_in_levels_recur(graph, graph[node.name], level+1)
    node.level = level


graph = read_graph('input.txt')
fill_in_levels(graph)

'''
for (key,value) in graph.items():
  print('==================')
  print(key)
  for n in value:
    print(n.name, n.visited, n.parent_name, n.level)
'''


def get_node(node_name, graph):
  for value in graph.values():
    for v in value:
      if v.name == node_name:
        return v
  return None


def find_santa(you, san, graph):
  curr_node = get_node(you.parent_name, graph)
  res = []
  while True:
    curr_node.visited = True
    if curr_node.name == san.name:
      # santa may be on the same branch
      return res

    if curr_node.level >= san.level:
      # back up to parent of the current node
      res.append(curr_node)
      curr_node = get_node(curr_node.parent_name, graph)
      continue

    # go down to a node
    if go_down(curr_node, res, graph):
      break
    else:
      res.append(curr_node)
      curr_node = get_node(curr_node.parent_name, graph)

  return res


def go_down(node, res_lst, graph):
  if node.name == 'SAN': # found santa
    return True

  if len(graph[node.name]) == 0: # can not go down any more
    return False
  
  node.visited = True
  for child in graph[node.name]:
    if child.visited: # skip branch that has already been visited
      continue

    res_lst.append(child)
    if go_down(child, res_lst, graph):
      return True
    res_lst.pop()

  return False


you = get_node('YOU', graph)
san = get_node('SAN', graph)

if you and san:
  print(len(find_santa(you, san, graph)) - 1)
else:
  print('could not find you or san')


'''
Start at YOU
Back up to SAN level minus one
Explore all children of the that node (not including the one you came from)
If not found back up again (only visit up to the depth of SAN)
Again ignore the branch you just came from
'''

'''
res = 0
for nodes in graph.values():
  for node in nodes:
    res += node.level

print(res)
'''
