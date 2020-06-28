#!/usr/bin/env python3
from enum import Enum


class Direction(Enum):
  NORTH = 1
  SOUTH = 2
  EAST = 3
  WEST = 4


class Turn(Enum):
  RIGHT = 0
  LEFT = 1


class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def inc_x(self): self.x += 1
  def dec_x(self): self.x -= 1
  def inc_y(self): self.y += 1
  def dec_y(self): self.y -= 1


class VirusCarrier:
  update_dir_facing = {
    (Direction.NORTH, Turn.RIGHT): Direction.EAST,
    (Direction.NORTH, Turn.LEFT): Direction.WEST,
    (Direction.SOUTH, Turn.RIGHT): Direction.WEST,
    (Direction.SOUTH, Turn.LEFT): Direction.EAST,
    (Direction.EAST, Turn.RIGHT): Direction.SOUTH,
    (Direction.EAST, Turn.LEFT): Direction.NORTH,
    (Direction.WEST, Turn.RIGHT): Direction.NORTH,
    (Direction.WEST, Turn.LEFT): Direction.SOUTH,
  }


  update_x_y = {
    Direction.NORTH: (lambda pos: pos.dec_y()),
    Direction.SOUTH: (lambda pos: pos.inc_y()),
    Direction.EAST:  (lambda pos: pos.inc_x()),
    Direction.WEST:  (lambda pos: pos.dec_x()),
  }


  opposite_dir = {
    Direction.NORTH: Direction.SOUTH,
    Direction.SOUTH: Direction.NORTH,
    Direction.EAST: Direction.WEST,
    Direction.WEST: Direction.EAST,
  }


  def __init__(self, direction_facing, position, grid):
    self.direction_facing = direction_facing
    self.nodes_infected = 0
    self.position = position
    self.grid = grid


  def burst(self):
    self._face_new_dir()
    self._update_curr_node()
    self._move()


  def _face_new_dir(self):
    pos = (self.position.y, self.position.x)
    if pos not in self.grid:
      self.grid[pos] = '.'

    if self.grid[pos] == '.':
      self._update_dir(Turn.LEFT)
    elif self.grid[pos] == '#':
      self._update_dir(Turn.RIGHT)
    elif self.grid[pos] == 'F':
      self.direction_facing = VirusCarrier.opposite_dir[self.direction_facing]


  def _update_dir(self, turn):
    self.direction_facing = VirusCarrier.update_dir_facing[(self.direction_facing, turn)]


  def _update_curr_node(self):
    pos = (self.position.y, self.position.x)
    if self.grid[pos] == '.':
      self.grid[pos] = 'W'
    elif self.grid[pos] == 'W':
      self.nodes_infected += 1
      self.grid[pos] = '#'
    elif self.grid[pos] == '#':
      self.grid[pos] = 'F'
    elif self.grid[pos] == 'F':
      self.grid[pos] = '.'


  def _move(self):
    update_pos = VirusCarrier.update_x_y[self.direction_facing]
    update_pos(self.position)


def main():
  grid = dict()
  with open('22_input.txt', 'r') as grid_file:
    line_count = 0
    for line in grid_file:
      for (i,node) in enumerate(line.strip()):
        grid[(line_count,i)] = node
      line_count += 1

  start_x = start_y = line_count // 2
  pos = Position(start_x, start_y)
  carrier = VirusCarrier(Direction.NORTH, pos, grid)

  for i in range(10000000):
    carrier.burst()

  print(carrier.nodes_infected)


if __name__ == '__main__':
  main()
