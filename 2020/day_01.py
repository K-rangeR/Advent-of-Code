#!/usr/bin/env python3

def main():
  with open("./input_01.txt", "r") as f:
    expense_report = []
    for line in f:
      expense_report.append(int(line.strip()))

    p1_answer = part_1(expense_report)
    print(p1_answer)

    better_1 = part_1_better(expense_report)
    print(better_1)

    p2_answer = part_2(expense_report)
    print(p2_answer)

    better_2 = part_2_better(expense_report)
    print(better_2)


# Just brute force it
def part_1(report):
  for (i,expense1) in enumerate(report):
    for (j,expense2) in enumerate(report):
      if i != j and (expense1 + expense2 == 2020):
        return expense1 * expense2
  return -1


# Better solution for part 1
def part_1_better(report):
  set_report = set(report)
  for expense in report:
    diff = 2020 - expense
    if diff in set_report:
      return expense * diff
  return -1
    

# Just brute force it again!
def part_2(report):
  for (i,expense1) in enumerate(report):
    for (j,expense2) in enumerate(report):
      for (k,expense3) in enumerate(report):
        if (i != j and i != k) and (expense1 + expense2 + expense3 == 2020):
          return expense1 * expense2 * expense3
  return -1


# Better solution for part 2
def part_2_better(report):
  set_report = set(report)
  for expense1 in report:
    for expense2 in report:
      diff = 2020 - expense1 - expense2
      if diff in set_report:
        return diff * expense1 * expense2
  return -1


if __name__ == "__main__":
  main()
