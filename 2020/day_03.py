#!/usr/bin/env python3

def main():
  with open("./input_03.txt", "r") as f:
    data = []
    for line in f:
      data.append(line.strip())

    print(slope(data, 3, 1))
    print(slope(data, 1, 1) * slope(data, 3, 1) * slope(data, 5, 1) * slope(data, 7, 1) * slope(data, 1, 2))


def slope(data, right, down):
    res = 0
    r, c = 0, 0
    while (r+down) < len(data):
      r += down
      c = (c+right) % len(data[r])
      if data[r][c] == "#":
        res += 1
    return res


if __name__ == "__main__":
  main()
