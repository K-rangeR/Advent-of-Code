#!/usr/bin/env python3
from enum import Enum

class Direction(Enum):
  NORTH=1
  SOUTH=2
  EAST=3
  WEST=4

move = {
    Direction.NORTH: lambda row, col: (row-1, col),
    Direction.SOUTH: lambda row, col: (row+1, col),
    Direction.EAST: lambda row, col: (row, col+1),
    Direction.WEST: lambda row, col: (row, col-1),
}

def consume_network():
  network = []
  with open('./input.txt', 'r') as f:
    for line in f:
      if len(line) == 1:
        continue
      network.append([c for c in line if c != '\n'])
  return network

network = consume_network()

def main():
  # position is a three element tuple:
  # (row, col, dir_facing)
  path = []
  position = get_init_postion()
  while not at_end(position):
    position = step(position, path)
  print(''.join(path))


def get_init_postion():
  return (0, network[0].index('|'), Direction.SOUTH)


def at_end(pos):
  return not (can_move(Direction.NORTH, pos) or
              can_move(Direction.SOUTH, pos) or
              can_move(Direction.EAST, pos) or
              can_move(Direction.WEST, pos))


def step(pos, path):
  return move_straight(pos, path) if not_at_switch(pos) else change_direction(pos)


def not_at_switch(pos):
  row, col, _ = pos
  return network[row][col] != '+'


def move_straight(pos, path):
  row, col, _ = pos
  cell = network[row][col]
  if cell.isalpha():
    path.append(cell)
  return move_in_same_direction(pos)


def move_in_same_direction(pos):
  row, col, dir_facing = pos
  new_row, new_col = move[dir_facing](row, col)
  return (new_row, new_col, dir_facing)


def change_direction(pos):
  row, col, dir_facing = pos
  if can_move(Direction.NORTH, pos) and dir_facing != Direction.SOUTH:
    dir_facing = Direction.NORTH
  elif can_move(Direction.SOUTH, pos) and dir_facing != Direction.NORTH:
    dir_facing = Direction.SOUTH
  elif can_move(Direction.EAST, pos) and dir_facing != Direction.WEST:
    dir_facing = Direction.EAST
  else:
    dir_facing = Direction.WEST
  return move_in_same_direction((row, col, dir_facing))


def can_move(direction, pos):
  row, col, _ = pos
  new_row, new_col = move[direction](row, col)
  return in_bounds(new_row, new_col) and not_empty_cell(new_row, new_col)


def in_bounds(row, col): return 0 <= row < len(network) and 0 <= col < len(network[0])
def not_empty_cell(row, col): return network[row][col] != ' '


if __name__ == '__main__':
  main()
