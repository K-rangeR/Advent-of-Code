#!/usr/bin/env python3
from functools import reduce

def main():
  #part_1()
  part_2()

  
def part_1():
  marks = [i for i in range(0, 256)]
  lengths = open('10_input.txt', 'r').read().strip().split(',')
  lengths[:] = [int(i) for i in lengths]
  marksp, skip_size = 0, 0

  for length in lengths:
    reverse_sublist(marks, marksp, length) 
    marksp = (marksp + (length + skip_size)) % len(marks)
    skip_size += 1

  print('Answer:', (marks[0] * marks[1]))


def part_2():
  lengths = open('10_input.txt', 'r').read().strip()
  lengths = [ord(letter) for letter in lengths]
  lengths.extend([17, 31, 73, 47, 23])
  marks = [i for i in range(256)] 
  marksp, skip_size = 0, 0

  for round_count in range(64):
    for length in lengths:
      reverse_sublist(marks, marksp, length) 
      marksp = (marksp + (length + skip_size)) % len(marks)
      skip_size += 1

  blocks, i = [], 0
  while i < len(marks):
    blocks.append(reduce((lambda x, y: x ^ y), marks[i:i+16]))
    i += 16

  knot_hash = ''
  for block in blocks:
    knot_hash += hex(block)[2:]

  print('Knot Hash:', knot_hash)


def reverse_sublist(marks, start, size):
  end = (start + (size - 1)) % len(marks)
  marks_to_swap = size / 2
  while marks_to_swap >= 1:
    marks[start], marks[end] = marks[end], marks[start]
    start = (start + 1) % len(marks)
    end = (end - 1) % len(marks)
    marks_to_swap -= 1
    

if __name__ == '__main__':
  main()
