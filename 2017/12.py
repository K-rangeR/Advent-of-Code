#!/usr/bin/env python3

pt1_count = 0

def main():
  graph = {}
  with open('12_input.txt', 'r') as f:
    for line in f:
      tokens = line.strip().split()
      node = int(tokens[0])
      neighbors = [int(token.strip(',')) for token in tokens[2:]]
      graph[node] = neighbors

  part_1(graph)
  part_2(graph)


def part_1(graph):
  contains_id(graph, 0, {})
  print('Answer part 1:', pt1_count)


def part_2(graph):
  connected_components, visited = 0, {}
  for node in graph.keys():
    if node not in visited:
      contains_id(graph, node, visited) 
      connected_components += 1
  print('Answer part 2:', connected_components)


def contains_id(graph, curr_node, visited):
  if curr_node in visited:
    return

  global pt1_count
  pt1_count += 1
  visited[curr_node] = True
  for neighbor in graph[curr_node]:
    contains_id(graph, neighbor, visited)
    visited[neighbor] = True


if __name__ == '__main__':
  main()
