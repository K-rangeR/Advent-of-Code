#!/usr/bin/env python3
import re
import sys


def eval_binary_expr(operand1, operator, operand2):
  operand1 = int(operand1)
  operand2 = int(operand2)
  if operator == 'AND':
    res = operand1 & operand2
  elif operator == 'OR':
    res = operand1 | operand2
  elif operator == 'LSHIFT':
    res = operand1 << operand2
  elif operator == 'RSHIFT':
    res = operand1 >> operand2
  else:
    print('Unknown binary operator:', operator)
    sys.exit(1)
  return str(res)


def is_integer(s):
  if s[0] in ('-', '+'):
    return s[1:].isdigit()
  return s.isdigit()


def solve_for(wire, circuit):
  expression = circuit[wire]
  operator = expression[1]

  if operator == 'ASSIGN':
    if not is_integer(expression[0]):
      expression[0] = solve_for(expression[0], circuit)
    return str(expression[0])

  elif operator == 'NOT':
    if not is_integer(expression[2]):
      expression[2] = solve_for(expression[2], circuit)
    return str(~(int(expression[2])))

  else:
    if not is_integer(expression[0]):
      expression[0] = solve_for(expression[0], circuit)
    if not is_integer(expression[2]):
      expression[2] = solve_for(expression[2], circuit)

    return eval_binary_expr(expression[0], operator, expression[2])


assign_pattern = re.compile(r'(\w+) -> (\w+)')
binary_pattern = re.compile(r'(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)')
not_pattern    = re.compile(r'NOT (\w+) -> (\w+)')

circuit = {}
with open('07_input.txt') as circuit_input:
  for line in circuit_input:
    match = assign_pattern.match(line)
    if match:
      circuit[match.group(2)] = [match.group(1), 'ASSIGN', None]

    match = binary_pattern.match(line)
    if match:
      circuit[match.group(4)] = [match.group(1), match.group(2), match.group(3)]

    match = not_pattern.match(line)
    if match:
      circuit[match.group(2)] = [None, 'NOT', match.group(1)]

answer = solve_for('a', circuit)
print('Answer:', answer)
