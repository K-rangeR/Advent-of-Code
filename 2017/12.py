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
  contains_id_zero(graph, 0, {})
  print('Answer:', pt1_count)


def contains_id_zero(graph, curr_node, visited):
  if curr_node in visited:
    return

  global pt1_count
  pt1_count += 1
  visited[curr_node] = True
  for neighbor in graph[curr_node]:
    contains_id_zero(graph, neighbor, visited)
    visited[neighbor] = True


if __name__ == '__main__':
  main()
