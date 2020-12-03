#!/usr/bin/env python3

def main():
  with open("./03_input.txt", "r") as f:
    data = []
    for line in f:
      data.append(line.strip())

    print(slope(data, 3, 1))
    print(slope(data, 1, 1) * slope(data, 3, 1) * slope(data, 5, 1) * slope(data, 7, 1) * slope(data, 1, 2))


def slope(data, r, d):
    c = 0
    x, y = 0, 0
    while True:
      if x >= len(data):
        break

      if data[x][y] == "#":
        c += 1

      if y+r >= len(data[x]):
        y = (y+r) % len(data[x])
      else:
        y += r

      x += d

    return c


if __name__ == "__main__":
  main()
