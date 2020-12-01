#!/usr/bin/env python3

def main():
  with open("./01_input.txt", "r") as f:
    expense_report = []
    for line in f:
      expense_report.append(int(line.strip()))

    p1_answer = part_1(expense_report)
    print(p1_answer)


def part_1(report):
  for (i,expense1) in enumerate(report):
    for (j,expense2) in enumerate(report):
      if i != j and (expense1 + expense2 == 2020):
        return expense1 * expense2
  return -1


if __name__ == "__main__":
  main()
