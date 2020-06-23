#!/usr/bin/env python3
from enum import Enum


class Direction(Enum):
  NORTH = 1
  EAST = 2
  SOUTH = 3
  WEST = 4


class Pos:
  def __init__(self, row, col):
    self.row = row
    self.col = col


def main():
  grid = []
  with open('19_input.txt', 'r') as input_file:
    for line in input_file:
      line = [token for token in line.strip('\n')]
      grid.append(line)

  start_row, start_col = 0, grid[0].index('|')
  direction = Direction.SOUTH
  position = Pos(start_row, start_col)
  answer = ''

  while moveable(position, grid):
    at = grid[position.row][position.col]
    if at.isalnum():
      answer += at
    elif at == '+':
      direction = change_dir(position, direction, grid)
    move(direction, position)

  print('Answer:', answer)


def moveable(pos, grid):
  if grid[pos.row][pos.col] == ' ':
    print('Off the path:', pos.row, pos.col)
    return False
  return (0 <= pos.row < len(grid)) and \
         (0 <= pos.col < len(grid[0]))


def move(direction, pos):
  if direction == Direction.NORTH:
    pos.row -= 1
  elif direction == Direction.EAST:
    pos.col += 1
  elif direction == Direction.SOUTH:
    pos.row += 1
  else:
    pos.col -= 1


def change_dir(pos, old_dir, grid):
  moves = {
    Direction.NORTH: lambda p: grid[p.row-1][p.col] != ' ',
    Direction.EAST: lambda p: grid[p.row][p.col+1] != ' ',
    Direction.SOUTH: lambda p: grid[p.row+1][p.col] != ' ',
    Direction.WEST: lambda p: grid[p.row][p.col-1] != ' ',
  }
  del moves[get_opposite_dir(old_dir)]
  for (new_dir, check) in moves.items():
    if check(pos):
      return new_dir
  print('Could not find a valid move at:', pos.row, pos.col)
  return old_dir


def get_opposite_dir(direction):
  if direction == Direction.NORTH:
    return Direction.SOUTH
  elif direction == Direction.EAST:
    return Direction.WEST
  elif direction == Direction.SOUTH:
    return Direction.NORTH
  else:
    return Direction.EAST


if __name__ == '__main__':
  main()
