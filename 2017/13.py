#!/usr/bin/env python3

class Wall:
  def __init__(self, depth, range_num):
    self.depth = depth
    if range_num != -1:
      self.ls = ['' for i in range(range_num)]
      self.ls[0] = 'S'
    else:
      self.ls = ['.']
    self.at = 0
    self.going_up = True
    self.range_num = range_num

  def move(self):
    if self.range_num == -1:
      return

    if self.at == len(self.ls) - 1:
      self.going_up = False
    elif self.at == 0:
      self.going_up = True

    self.ls[self.at] = ''
    self.at += 1 if self.going_up else -1
    self.ls[self.at] = 'S'


def main():
  layers = list()
  with open('13_input.txt', 'r') as input_data:
    for line in input_data:
      depth, range_num = line.strip().split(':')
      depth, range_num = int(depth), int(range_num)
      start = len(layers)
      end = start + (depth - len(layers))
      for i in range(start, end):
        layers.append(Wall(i, -1))
      layers.append(Wall(depth, range_num))

  total_severity = 0
  depth_at = 0
  while depth_at < len(layers):
    if caught(depth_at, layers):
      total_severity += depth_at * layers[depth_at].range_num
    depth_at += 1
    scan(layers)

  print('Answer:', total_severity)
    

def caught(depth_at, layers):
  return layers[depth_at].ls[0] == 'S'


def scan(layers):
  for wall in layers:
    wall.move()


if __name__ == '__main__':
  main()
