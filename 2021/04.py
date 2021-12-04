#!/usr/bin/env python3
import re

def print_board(board):
  for row in board:
    for cell in row:
      print(cell[1], end=' ')
    print()


def mark_on_board(n, board):
  for (i, row) in enumerate(board):
    for (j, cell) in enumerate(row):
      if cell[1] == n:
        board[i][j] = (True, cell[1])
        return


def mark_on_all(n, boards):
  for board in boards:
    mark_on_board(n, board)


def sum_of_non_marked(board):
  res = 0
  for row in board:
    unselected_cells = list(filter(lambda cell: not cell[0], row))
    res += sum(map(lambda cell: cell[1], unselected_cells))
  return res


def scan_row_for_winner(board):
  for row in board:
    ls = list(filter(lambda cell: cell[0], row))
    if len(ls) == 5:
      return sum_of_non_marked(board)
  return -1


def board_has_winner(board):
  if (res := scan_row_for_winner(board)) != -1:
    return res

  cols = [[] for i in range(5)]
  for r in range(5):
    for c in range(5):
      cols[c].append(board[r][c])

  return scan_row_for_winner(cols)


def check_for_winner(boards):
  for board in boards:
    if (res := board_has_winner(board)) != -1:
      return res
  return -1


with open('./04_input.txt') as file:
  # read first line
  line = file.readline().strip()
  inputNums = list(map(int, line.split(',')))

  # read and skip second line
  file.readline()

  # read rest of file
  boards = []
  curr_board = []
  for line in file:
    if len(line) == 1:
      boards.append(curr_board)
      curr_board = []
      continue
    nums = list(map(int, line.strip().split()))
    curr_board.append(list(map(lambda n: (False, n), nums)))

  for num in inputNums:
    mark_on_all(num, boards)
    has_winner = check_for_winner(boards)
    if has_winner != -1:
      print(has_winner * num)
      break
