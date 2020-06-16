from itertools import combinations
from operator import mul

def main():
  #boxes = 3
  boxes = 4
  with open('24_input.txt', 'r') as input_file:
    weights = map(int, input_file.readlines())
    target = sum(weights) / boxes
    for n in range(int(len(weights) / boxes) + 2):
      subls = [x for x in list(combinations(weights,  n)) if sum(x) == target]
      if len(subls) > 0:
        break
    answer = reduce(mul, min(subls, key=lambda x: reduce(mul, x)))
    print(answer)


if __name__ == '__main__':
  main()
