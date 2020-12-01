#!/usr/bin/env python3

def main():
  with open("./01_input.txt", "r") as f:
    expense_report = []
    for line in f:
      expense_report.append(int(line.strip()))

    p1_answer = part_1(expense_report)
    print(p1_answer)

    p2_answer = part_2(expense_report)
    print(p2_answer)


# Just brute force it
def part_1(report):
  for (i,expense1) in enumerate(report):
    for (j,expense2) in enumerate(report):
      if i != j and (expense1 + expense2 == 2020):
        return expense1 * expense2
  return -1


# Just brute force it again!
def part_2(report):
  for (i,expense1) in enumerate(report):
    for (j,expense2) in enumerate(report):
      for (k,expense3) in enumerate(report):
        if (i != j and i != k) and (expense1 + expense2 + expense3 == 2020):
          return expense1 * expense2 * expense3
  return -1


if __name__ == "__main__":
  main()
