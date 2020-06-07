#!/usr/bin/env python3

def main():
  polymer = list(open('05_input.txt', 'r').read().strip())

  stack = [polymer[0]] 
  for unit in polymer[1:]:
    if len(stack) == 0:
      stack.append(unit)
      continue
    top = stack[-1]
    if same_but_different_case(top, unit):
      stack.pop()
    else:
      stack.append(unit)

  print('Answer:', len(stack))

  
def same_but_different_case(a, b):
  if a.lower() == b.lower():
    ascii_code = abs(ord(a) - ord(b))
    return ascii_code == 32
  return False


if __name__ == '__main__':
  main()
