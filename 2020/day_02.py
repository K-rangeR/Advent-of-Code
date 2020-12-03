#!/usr/bin/env python3

def main():
  #part1()
  part2()


def part1():
  answer = 0
  with open("./input_02.txt", "r") as f:
    for line in f:
      tokens = line.strip().split(" ")
      nrange = tokens[0].split("-")
      letter = tokens[1][:1]
      pwd = tokens[2]
      count = 0
      for c in pwd:
        if c == letter:
          count += 1
      if int(nrange[0]) <= count <= int(nrange[1]):
        answer += 1
    print(answer)


def part2():
  answer = 0
  with open("./02_input.txt", "r") as f:
    for line in f:
      tokens = line.strip().split(" ")
      nrange = tokens[0].split("-")
      letter = tokens[1][:1]
      pwd = "#" + tokens[2]
      p1, p2 = pwd[int(nrange[0])], pwd[int(nrange[1])]
      if p1 == p2:
        continue
      elif p1 == letter or p2 == letter:
        answer += 1
    print(answer)
  

if __name__ == "__main__":
  main()
