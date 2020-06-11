#!/usr/bin/env python3

def main():
  marks = [i for i in range(0, 256)]
  lengths = open('10_input.txt', 'r').read().strip().split(',')
  lengths[:] = [int(i) for i in lengths]
  marksp, skip_size = 0, 0

  for length in lengths:
    reverse_sublist(marks, marksp, length) 
    marksp = (marksp + (length + skip_size)) % len(marks)
    skip_size += 1

  print('Answer:', (marks[0] * marks[1]))


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
