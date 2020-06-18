#!/usr/bin/env python3
from functools import reduce


def main():
  key = 'hwlqcszp'
  used_count = 0
  for i in range(128):
    digest = knot_hash(key + '-' + str(i))
    digest_bin = [bin(int(hex_digit, 16))[2:].zfill(4) for hex_digit in digest]
    digest_bin = ''.join(digest_bin)
    used_count += digest_bin.count('1')
  print('Used:', used_count)


def knot_hash(val):
  lengths = [ord(letter) for letter in val]
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

  return knot_hash


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
