#!/usr/bin/env python3

def one():
  with open('./01_input.txt', 'r') as file:
    prev = 100000000
    inc = 0
    for line in file:
      n = int(line.strip())
      if n > prev:
        inc += 1
      prev = n
    print(inc)


def two():
  i, j = 0, 3
  prev = 0
  inc = 0
  with open('./01_input.txt', 'r') as file:
    data = file.read().strip().split('\n')
    data = list(map(int, data))
    while j < len(data):
      n = sum(data[i:j])
      if n > prev:
        inc += 1
      i += 1
      j += 1
      prev = n
  print(inc)

  
def main():
  one()
  two()


if __name__ == '__main__':
  main()
