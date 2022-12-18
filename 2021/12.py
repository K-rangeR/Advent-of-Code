#!/usr/bin/env python3

def is_small_cave(name):
  for c in name:
    if c.isupper():
      return False
  return True


def print_all_paths(src, dst, graph):
  pass


def print_all_paths_recur(n, dst, graph, visited, path):
  pass


with open('./12_test_01.txt', 'r') as file:
  graph = dict()
  for line in file:
    tokens = line.strip().split('-')
    from_node, to_node = tokens[0], tokens[1]
    if from_node not in graph:
      graph[from_node] = []
    if to_node not in graph:
      graph[to_node] = []
    graph[from_node].append(to_node)
    graph[to_node].append(from_node)

  print_all_paths('start', 'end', graph)
