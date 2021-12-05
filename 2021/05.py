#!/usr/bin/env python3

X, Y = 0, 1


def print_board(board):
  for r in board:
    for n in r:
      print(n, end=' ')
    print('')


def is_vertical(line_segment):
  start, end = line_segment
  return start[X] == end[X]


def is_horizontal(line_segment):
  start, end = line_segment
  return start[Y] == end[Y]


def draw_on_board(line_segment, board):
  greater_than_two_count = 0
  p1, p2 = line_segment

  if is_vertical(line_segment):
    # move down
    x = p1[X]
    start_y, end_y = min(p1[Y], p2[Y]), max(p1[Y], p2[Y])
    while start_y <= end_y:
      board[start_y][x] += 1
      greater_than_two_count += 1 if board[start_y][x] == 2 else 0
      start_y += 1
    return greater_than_two_count

  if is_horizontal(line_segment):
    # move right
    y = p1[Y]
    start_x, end_x = min(p1[X], p2[X]), max(p1[X], p2[X])
    while start_x <= end_x:
      board[y][start_x] += 1
      greater_than_two_count += 1 if board[y][start_x] == 2 else 0
      start_x += 1
    return greater_than_two_count

  return 0


def split_to_int(token):
  return list(map(int, token.split(',')))


with open('./05_input.txt', 'r') as file:
  max_x = max_y = -1
  line_segments = []
  for line in file:
    tokens = line.strip().split(' ')
    start, end = split_to_int(tokens[0]), split_to_int(tokens[2])
    line_segments.append((start, end))
    max_x = max(max_x, start[X], end[X])
    max_y = max(max_y, start[Y], end[Y])

  board = [[0 for j in range(max_y+1)] for i in range(max_x+1)]

  # part 1
  answer = 0
  for line_segment in line_segments:
    answer += draw_on_board(line_segment, board)
  print(answer)
